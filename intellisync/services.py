"""Agent execution services for IntelliSync.

Workers and QA supervisors use a local Ollama chat endpoint. Model assignments
are explicit configuration, not inferred. The scheduler is opt-in and refuses
to start if any required model or QA ownership is missing.
"""
from __future__ import annotations

import json
import os
import sqlite3
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any

from .runtime import IntelliSync, InvalidTransition, RuntimeErrorBase, utc_now

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_AGENT_CONFIG = Path(__file__).parent / "config" / "agents.json"


class ServiceConfigurationError(RuntimeErrorBase):
    pass


class OllamaClient:
    def __init__(self, endpoint: str, timeout_s: int = 180):
        self.endpoint = endpoint.rstrip("/")
        self.timeout_s = timeout_s

    def chat(self, model: str, messages: list[dict[str, str]],
             temperature: float = 0.2) -> str:
        if not model:
            raise ServiceConfigurationError("No Ollama model is assigned to this agent.")
        body = json.dumps({
            "model": model,
            "messages": messages,
            "stream": False,
            "options": {"temperature": temperature}
        }).encode("utf-8")
        req = urllib.request.Request(
            self.endpoint + "/api/chat", data=body,
            headers={"Content-Type": "application/json"}, method="POST"
        )
        try:
            with urllib.request.urlopen(req, timeout=self.timeout_s) as response:
                data = json.loads(response.read().decode("utf-8"))
        except urllib.error.URLError as exc:
            raise RuntimeErrorBase(f"Local Ollama endpoint unavailable: {exc}") from exc
        content = (data.get("message") or {}).get("content", "")
        if not isinstance(content, str) or not content.strip():
            raise RuntimeErrorBase("Ollama returned an empty response.")
        return content.strip()


class MessageHub:
    """Persistent direct messages and shared feeds in the runtime SQLite DB."""
    def __init__(self, db_path: str | Path):
        self.db_path = str(db_path)
        with sqlite3.connect(self.db_path) as con:
            con.execute("""
                CREATE TABLE IF NOT EXISTS agent_messages (
                    message_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    feed TEXT NOT NULL,
                    sender TEXT NOT NULL,
                    recipient TEXT,
                    package_id TEXT,
                    subject TEXT NOT NULL,
                    body TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    read_at TEXT
                )
            """)
            con.execute("CREATE INDEX IF NOT EXISTS idx_agent_messages_feed ON agent_messages(feed,message_id)")
            con.commit()

    def send(self, sender: str, subject: str, body: str, feed: str = "command",
             recipient: str | None = None, package_id: str | None = None) -> int:
        if not sender.strip() or not subject.strip() or not body.strip():
            raise ValueError("Message sender, subject and body are required.")
        with sqlite3.connect(self.db_path) as con:
            cur = con.execute(
                """INSERT INTO agent_messages(feed,sender,recipient,package_id,subject,body,created_at)
                VALUES(?,?,?,?,?,?,?)""",
                (feed, sender, recipient, package_id, subject, body, utc_now())
            )
            con.commit()
            return int(cur.lastrowid)

    def read(self, feed: str = "command", recipient: str | None = None,
             limit: int = 50) -> list[dict[str, Any]]:
        with sqlite3.connect(self.db_path) as con:
            con.row_factory = sqlite3.Row
            if recipient:
                rows = con.execute(
                    """SELECT * FROM agent_messages WHERE feed=? AND (recipient IS NULL OR recipient=?)
                    ORDER BY message_id DESC LIMIT ?""", (feed, recipient, limit)
                ).fetchall()
            else:
                rows = con.execute(
                    "SELECT * FROM agent_messages WHERE feed=? ORDER BY message_id DESC LIMIT ?",
                    (feed, limit)
                ).fetchall()
            return [dict(row) for row in rows]


class TrinityCoordinator:
    """Top-level coordinator services for queue oversight and escalations."""
    def __init__(self, runtime: IntelliSync, messages: MessageHub):
        self.runtime = runtime
        self.messages = messages

    def snapshot(self) -> dict[str, Any]:
        with sqlite3.connect(self.runtime.db_path) as con:
            packages = {row[0]: row[1] for row in con.execute(
                "SELECT status,COUNT(*) FROM packages GROUP BY status")}
            station_runs = {row[0]: row[1] for row in con.execute(
                "SELECT status,COUNT(*) FROM station_runs GROUP BY status")}
        return {
            "coordinator": "Trinity",
            "packages": packages,
            "station_runs": station_runs,
            "ready": station_runs.get("ready", 0),
            "in_progress": station_runs.get("in_progress", 0),
            "awaiting_qa": station_runs.get("qa_pending", 0),
            "rework": station_runs.get("rework", 0),
            "escalation_required": station_runs.get("blocked", 0)
        }

    def audit_qa(self, run_id: str, qa_result: dict[str, Any]) -> dict[str, Any]:
        qa = qa_result.get("qa", {})
        checks = qa.get("checks", [])
        audit = {
            "reviewed_by": "Trinity",
            "qa_decision": qa.get("decision"),
            "checks_present": bool(checks),
            "feedback_present": bool(qa.get("feedback")),
            "confidence": qa.get("confidence"),
            "audit_status": "recorded" if checks and qa.get("feedback") else "escalate"
        }
        with sqlite3.connect(self.runtime.db_path) as con:
            row = con.execute("SELECT package_id,station_id FROM station_runs WHERE run_id=?",
                              (run_id,)).fetchone()
        if row:
            self.messages.send("Trinity", "QA oversight audit",
                               json.dumps(audit, ensure_ascii=False),
                               feed="command", package_id=row[0])
        return audit

    def escalate(self, subject: str, details: str, package_id: str | None = None) -> int:
        return self.messages.send("Trinity", subject, details, feed="command",
                                  package_id=package_id)


class AgentServices:
    def __init__(self, runtime: IntelliSync, config_path: str | Path = DEFAULT_AGENT_CONFIG,
                 client: OllamaClient | None = None):
        self.runtime = runtime
        self.config_path = Path(config_path)
        self.config = json.loads(self.config_path.read_text(encoding="utf-8"))
        self.client = client or OllamaClient(
            self.config.get("ollama", {}).get("endpoint", "http://127.0.0.1:11434")
        )
        self.messages = MessageHub(runtime.db_path)
        self.trinity = TrinityCoordinator(runtime, self.messages)

    def _model_for(self, agent_id: str) -> str:
        model = self.config.get("models", {}).get(agent_id)
        if not model:
            raise ServiceConfigurationError(
                f"No model configured for {agent_id}; set it in intellisync/config/agents.json."
            )
        return model

    def _work_record(self, run_id: str) -> dict[str, Any]:
        with sqlite3.connect(self.runtime.db_path) as con:
            con.row_factory = sqlite3.Row
            row = con.execute("""
                SELECT r.*, p.package_type, p.payload_json, p.version
                FROM station_runs r JOIN packages p USING(package_id)
                WHERE r.run_id=?
            """, (run_id,)).fetchone()
            if not row:
                raise RuntimeErrorBase("Station run not found.")
            return dict(row)

    def execute_station(self, run_id: str) -> str:
        item = self._work_record(run_id)
        if item["status"] != "ready":
            raise InvalidTransition("Only a ready station run can be executed.")
        station = next((s for s in self.runtime.stations if s["station_id"] == item["station_id"]), None)
        if not station:
            raise ServiceConfigurationError(f"Station config missing: {item['station_id']}")
        self.runtime.claim(item["package_id"], item["station_id"], item["agent_id"])
        payload = json.loads(item["payload_json"])
        feedback = item.get("qa_feedback") or ""
        system = (
            f"You are the {station['role']} production specialist for Hustle City. "
            "Work only within the supplied package scope. Respect approved project canon. "
            "Return a useful, structured production deliverable. Do not claim external files "
            "or engine assets were created unless actually created by an available tool."
        )
        user = json.dumps({
            "package_id": item["package_id"], "package_version": item["version"],
            "package_type": item["package_type"], "station": station,
            "approved_input": payload, "QA_correction_feedback": feedback,
            "instruction": "Produce this station's deliverable. Include assumptions, dependencies, risks and handoff notes."
        }, ensure_ascii=False, indent=2)
        output = self.client.chat(self._model_for(item["agent_id"]),
                                  [{"role": "system", "content": system},
                                   {"role": "user", "content": user}])
        self.runtime.submit(item["package_id"], item["station_id"], item["agent_id"],
                            output, event_key=f"{run_id}:submission")
        self.messages.send(item["agent_id"], "Deliverable submitted",
                           f"Package {item['package_id']} is waiting for QA at {item['station_id']}.",
                           feed="command", package_id=item["package_id"])
        return output

    def review_station(self, run_id: str) -> dict[str, Any]:
        item = self._work_record(run_id)
        if item["status"] != "qa_pending":
            raise InvalidTransition("Only a QA-pending run can be reviewed.")
        qa_id = item["qa_supervisor_id"]
        system = (
            "You are an independent Hustle City QA supervisor. Evaluate the deliverable "
            "against the task scope, completeness, consistency, feasibility and upstream "
            "constraints. Be strict but constructive. Never approve work merely to move the queue. "
            "Respond with ONLY JSON: {\"decision\":\"approve\" or \"reject\","
            "\"feedback\":\"specific findings\", \"checks\":[\"...\"], \"confidence\":0.0}."
        )
        user = json.dumps({
            "package_id": item["package_id"], "package_type": item["package_type"],
            "station_id": item["station_id"], "production_agent": item["agent_id"],
            "approved_input": json.loads(item["payload_json"]),
            "deliverable": item["output_text"],
            "review_instruction": "Reject if a material requirement is missing, unsupported, contradictory or unusable."
        }, ensure_ascii=False, indent=2)
        raw = self.client.chat(self._model_for(qa_id),
                               [{"role": "system", "content": system},
                                {"role": "user", "content": user}], temperature=0)
        try:
            decision = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise RuntimeErrorBase("QA response was not valid JSON; left in QA queue for human review.") from exc
        if decision.get("decision") not in ("approve", "reject"):
            raise RuntimeErrorBase("QA response has no valid decision; left in QA queue.")
        if not isinstance(decision.get("feedback"), str) or not isinstance(decision.get("checks"), list):
            raise RuntimeErrorBase("QA response schema invalid; left in QA queue.")
        # Trinity's gate audits the QA record before any approval can release downstream work.
        confidence = float(decision.get("confidence", 0))
        qa_policy = self.config.get("qa", {})
        audit_ok = (
            (not qa_policy.get("require_nonempty_checks", True) or bool(decision["checks"]))
            and (not qa_policy.get("require_feedback", True) or bool(decision["feedback"].strip()))
            and (decision["decision"] != "approve" or confidence >= float(
                qa_policy.get("minimum_auto_approval_confidence", 0.85)
            ))
        )
        if not audit_ok:
            self.messages.send("Trinity", "QA decision held for oversight",
                               f"QA result for {item['package_id']} at {item['station_id']} lacks required evidence or confidence. Human review required. Raw QA: {json.dumps(decision)}",
                               feed="command", package_id=item["package_id"])
            return {"result": "human_review_required", "qa": decision}
        result = self.runtime.review(item["package_id"], item["station_id"], qa_id,
                                     decision["decision"], decision["feedback"],
                                     event_key=f"{run_id}:qa")
        self.messages.send(qa_id, "QA decision recorded",
                           f"{item['package_id']} at {item['station_id']}: {result}.",
                           feed="command", package_id=item["package_id"])
        return {"result": result, "qa": decision}

    def audit_qa(self, run_id: str, qa_result: dict[str, Any]) -> dict[str, Any]:
        return self.trinity.audit_qa(run_id, qa_result)


class Scheduler:
    """Opt-in local scheduler. Bounded workers; queue state remains in SQLite."""
    def __init__(self, services: AgentServices, max_workers: int = 1):
        if max_workers < 1:
            raise ValueError("max_workers must be at least one.")
        self.services = services
        self.runtime = services.runtime
        self.max_workers = max_workers
        self._validate_ready()

    def _validate_ready(self) -> None:
        for station in self.runtime.stations:
            qa = station.get("qa_supervisor_id")
            if not qa:
                raise ServiceConfigurationError(
                    f"QA owner not configured for {station['station_id']}; scheduler will not start."
                )
            self.services._model_for(station["agent_id"])
            self.services._model_for(qa)

    def tick(self) -> dict[str, Any]:
        with sqlite3.connect(self.runtime.db_path) as con:
            con.row_factory = sqlite3.Row
            ready = con.execute(
                "SELECT run_id FROM station_runs WHERE status='ready' ORDER BY rowid LIMIT ?",
                (self.max_workers,)
            ).fetchall()
            pending = con.execute(
                "SELECT run_id FROM station_runs WHERE status='qa_pending' ORDER BY rowid LIMIT ?",
                (self.max_workers,)
            ).fetchall()
        outcomes: list[dict[str, Any]] = []
        # Process existing QA queue first, then new production. The next tick
        # picks up the downstream run released by a successful QA review.
        def review_one(row: sqlite3.Row) -> dict[str, Any]:
            try:
                reviewed = self.services.review_station(row["run_id"])
                audit = self.services.audit_qa(row["run_id"], reviewed)
                return {"run_id": row["run_id"], "qa": reviewed, "trinity_audit": audit}
            except Exception as exc:
                return {"run_id": row["run_id"], "error": str(exc)}

        def execute_one(row: sqlite3.Row) -> dict[str, Any]:
            try:
                self.services.execute_station(row["run_id"])
                return {"run_id": row["run_id"], "result": "submitted_for_qa"}
            except Exception as exc:
                return {"run_id": row["run_id"], "error": str(exc)}

        # Bound concurrent model calls. SQLite claim transactions prevent duplicate ownership.
        with ThreadPoolExecutor(max_workers=self.max_workers) as pool:
            outcomes.extend(pool.map(review_one, pending))
            outcomes.extend(pool.map(execute_one, ready))
        return {"processed": len(outcomes), "outcomes": outcomes, "recovery": self.runtime.recover()}

    def run_forever(self, interval_s: float = 2.0) -> None:
        if interval_s < 0.25:
            raise ValueError("Scheduler recovery interval cannot be below 0.25 seconds.")
        while True:
            self.tick()
            time.sleep(interval_s)


def main() -> int:
    import argparse
    parser = argparse.ArgumentParser(description="Hustle City IntelliSync agent services")
    parser.add_argument("--db", default=str(ROOT / "data" / "intellisync.sqlite3"))
    parser.add_argument("--config", default=str(DEFAULT_AGENT_CONFIG))
    parser.add_argument("--max-workers", type=int, default=1)
    parser.add_argument("--interval", type=float, default=2.0)
    parser.add_argument("--once", action="store_true")
    args = parser.parse_args()
    try:
        runtime = IntelliSync(args.db)
        services = AgentServices(runtime, args.config)
        scheduler = Scheduler(services, args.max_workers)
        if args.once:
            print(json.dumps(scheduler.tick(), indent=2))
        else:
            print("IntelliSync scheduler running. Ctrl+C to stop.", flush=True)
            scheduler.run_forever(args.interval)
        return 0
    except (RuntimeErrorBase, sqlite3.Error, OSError, ValueError) as exc:
        print(f"intellisync-services: {exc}", file=__import__("sys").stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
