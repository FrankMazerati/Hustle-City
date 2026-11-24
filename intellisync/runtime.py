"""Durable, event-driven package relay for Hustle City IntelliSync.

Coordinates work without pretending an LLM worker is active. Workers submit
deliverables, QA records independent decisions, and approval creates the next
station run. SQLite is the initial local persistence adapter.
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = Path(__file__).parent / "config" / "assembly_line.json"
DEFAULT_DB = ROOT / "data" / "intellisync.sqlite3"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


class RuntimeErrorBase(Exception):
    """Base exception for expected runtime errors."""


class InvalidTransition(RuntimeErrorBase):
    """Raised when a command does not match the current task state."""


class ConfigurationError(RuntimeErrorBase):
    """Raised when the assembly-line configuration is incomplete."""


class IntelliSync:
    def __init__(self, db_path: str | Path = DEFAULT_DB,
                 config_path: str | Path = DEFAULT_CONFIG):
        self.db_path = Path(db_path)
        self.config_path = Path(config_path)
        self.config = json.loads(self.config_path.read_text(encoding="utf-8"))
        self.stations = self.config.get("stations", [])
        if not self.stations:
            raise ConfigurationError("Pipeline has no stations.")
        self._validate_pipeline()
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._initialize()

    def _validate_pipeline(self) -> None:
        ids = [s.get("station_id") for s in self.stations]
        if any(not value for value in ids) or len(ids) != len(set(ids)):
            raise ConfigurationError("Every station needs a unique station_id.")
        for station in self.stations:
            if not station.get("agent_id") or not station.get("role"):
                raise ConfigurationError("Every station needs agent_id and role.")

    def _connect(self) -> sqlite3.Connection:
        con = sqlite3.connect(self.db_path, timeout=30)
        con.row_factory = sqlite3.Row
        con.execute("PRAGMA foreign_keys=ON")
        con.execute("PRAGMA journal_mode=WAL")
        return con

    def _initialize(self) -> None:
        with self._connect() as con:
            con.executescript("""
            CREATE TABLE IF NOT EXISTS packages (
                package_id TEXT PRIMARY KEY,
                project TEXT NOT NULL,
                package_type TEXT NOT NULL,
                version INTEGER NOT NULL,
                status TEXT NOT NULL,
                current_station TEXT,
                pipeline_json TEXT NOT NULL,
                payload_json TEXT NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS station_runs (
                run_id TEXT PRIMARY KEY,
                package_id TEXT NOT NULL REFERENCES packages(package_id),
                station_id TEXT NOT NULL,
                agent_id TEXT NOT NULL,
                qa_supervisor_id TEXT NOT NULL,
                status TEXT NOT NULL,
                attempt INTEGER NOT NULL DEFAULT 1,
                output_text TEXT,
                qa_feedback TEXT,
                started_at TEXT,
                submitted_at TEXT,
                reviewed_at TEXT,
                UNIQUE(package_id, station_id, attempt)
            );
            CREATE INDEX IF NOT EXISTS idx_station_runs_queue
                ON station_runs(status, station_id);
            CREATE TABLE IF NOT EXISTS events (
                event_id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_key TEXT NOT NULL UNIQUE,
                package_id TEXT NOT NULL REFERENCES packages(package_id),
                event_type TEXT NOT NULL,
                actor_id TEXT NOT NULL,
                details_json TEXT NOT NULL,
                created_at TEXT NOT NULL
            );
            """)

    def _record_event(self, con: sqlite3.Connection, package_id: str,
                      event_type: str, actor_id: str, details: dict[str, Any],
                      event_key: str | None = None) -> None:
        key = event_key or f"{package_id}:{event_type}:{uuid.uuid4().hex}"
        con.execute(
            "INSERT INTO events(event_key,package_id,event_type,actor_id,details_json,created_at) VALUES(?,?,?,?,?,?)",
            (key, package_id, event_type, actor_id,
             json.dumps(details, sort_keys=True), utc_now())
        )

    def create_package(self, package_type: str, payload: dict[str, Any],
                       qa_map: dict[str, str], package_id: str | None = None) -> str:
        pipeline = []
        for station in self.stations:
            qa_id = qa_map.get(station["station_id"]) or station.get("qa_supervisor_id")
            if not qa_id:
                raise ConfigurationError(
                    f"QA supervisor not assigned for {station['station_id']}. "
                    "Supply --qa-map or configure the station explicitly."
                )
            if qa_id == station["agent_id"]:
                raise ConfigurationError("A production agent cannot QA its own work.")
            pipeline.append({**station, "qa_supervisor_id": qa_id})
        pid = package_id or f"HC-PKG-{uuid.uuid4().hex[:10].upper()}"
        now = utc_now()
        with self._connect() as con:
            try:
                con.execute("BEGIN IMMEDIATE")
                con.execute(
                    "INSERT INTO packages VALUES(?,?,?,?,?,?,?,?,?,?)",
                    (pid, self.config.get("project", "Hustle City"), package_type, 1,
                     "ready", pipeline[0]["station_id"], json.dumps(pipeline),
                     json.dumps(payload, sort_keys=True), now, now)
                )
                first = pipeline[0]
                con.execute(
                    """INSERT INTO station_runs(run_id,package_id,station_id,agent_id,
                    qa_supervisor_id,status) VALUES(?,?,?,?,?,?)""",
                    (uuid.uuid4().hex, pid, first["station_id"], first["agent_id"],
                     first["qa_supervisor_id"], "ready")
                )
                self._record_event(con, pid, "package_created", "creator",
                                   {"package_type": package_type, "first_station": first["station_id"]})
                con.commit()
            except sqlite3.IntegrityError:
                con.rollback()
                raise RuntimeErrorBase(f"Package ID already exists: {pid}")
        return pid

    def claim(self, package_id: str, station_id: str, agent_id: str) -> None:
        with self._connect() as con:
            con.execute("BEGIN IMMEDIATE")
            run = con.execute(
                """SELECT * FROM station_runs WHERE package_id=? AND station_id=?
                AND status IN ('ready','rework') ORDER BY attempt DESC LIMIT 1""",
                (package_id, station_id)
            ).fetchone()
            if not run:
                con.rollback()
                raise InvalidTransition("No ready or rework station task exists.")
            if run["agent_id"] != agent_id:
                con.rollback()
                raise InvalidTransition("Only the assigned station agent may claim this work.")
            con.execute(
                "UPDATE station_runs SET status='in_progress',started_at=? WHERE run_id=?",
                (utc_now(), run["run_id"])
            )
            con.execute("UPDATE packages SET status='in_progress',updated_at=? WHERE package_id=?",
                        (utc_now(), package_id))
            self._record_event(con, package_id, "station_claimed", agent_id,
                               {"station_id": station_id, "attempt": run["attempt"]})
            con.commit()

    def release_failed_claim(self, run_id: str, agent_id: str, reason: str) -> bool:
        """Return a failed in-progress run to the ready queue without losing it."""
        with self._connect() as con:
            con.execute("BEGIN IMMEDIATE")
            run = con.execute(
                "SELECT package_id,station_id,agent_id,status FROM station_runs WHERE run_id=?",
                (run_id,)
            ).fetchone()
            if not run or run["agent_id"] != agent_id or run["status"] != "in_progress":
                con.rollback()
                return False
            now = utc_now()
            con.execute(
                "UPDATE station_runs SET status='ready',started_at=NULL WHERE run_id=?",
                (run_id,)
            )
            con.execute(
                "UPDATE packages SET status='ready',updated_at=? WHERE package_id=?",
                (now, run["package_id"])
            )
            self._record_event(
                con, run["package_id"], "station_claim_released", agent_id,
                {"run_id": run_id, "station_id": run["station_id"], "reason": reason}
            )
            con.commit()
            return True

    def submit(self, package_id: str, station_id: str, agent_id: str,
               output_text: str, event_key: str | None = None) -> None:
        if not output_text.strip():
            raise RuntimeErrorBase("A station cannot submit an empty deliverable.")
        with self._connect() as con:
            con.execute("BEGIN IMMEDIATE")
            if event_key and con.execute("SELECT 1 FROM events WHERE event_key=?", (event_key,)).fetchone():
                con.rollback()
                return
            run = con.execute(
                """SELECT * FROM station_runs WHERE package_id=? AND station_id=?
                AND status='in_progress' ORDER BY attempt DESC LIMIT 1""",
                (package_id, station_id)
            ).fetchone()
            if not run or run["agent_id"] != agent_id:
                con.rollback()
                raise InvalidTransition("No in-progress task owned by this agent.")
            con.execute(
                "UPDATE station_runs SET status='qa_pending',output_text=?,submitted_at=? WHERE run_id=?",
                (output_text, utc_now(), run["run_id"])
            )
            con.execute("UPDATE packages SET status='qa_pending',updated_at=? WHERE package_id=?",
                        (utc_now(), package_id))
            self._record_event(con, package_id, "deliverable_submitted", agent_id,
                               {"station_id": station_id, "run_id": run["run_id"]}, event_key)
            con.commit()

    def review(self, package_id: str, station_id: str, reviewer_id: str,
               decision: str, feedback: str = "", event_key: str | None = None) -> str:
        if decision not in ("approve", "reject"):
            raise RuntimeErrorBase("Decision must be approve or reject.")
        with self._connect() as con:
            con.execute("BEGIN IMMEDIATE")
            if event_key and con.execute("SELECT 1 FROM events WHERE event_key=?", (event_key,)).fetchone():
                con.rollback()
                return "duplicate_ignored"
            run = con.execute(
                """SELECT * FROM station_runs WHERE package_id=? AND station_id=?
                AND status='qa_pending' ORDER BY attempt DESC LIMIT 1""",
                (package_id, station_id)
            ).fetchone()
            if not run:
                con.rollback()
                raise InvalidTransition("No deliverable is waiting for QA at this station.")
            if reviewer_id != run["qa_supervisor_id"]:
                con.rollback()
                raise InvalidTransition("Only the assigned QA supervisor may review this station.")
            if reviewer_id == run["agent_id"]:
                con.rollback()
                raise InvalidTransition("Self-approval is prohibited.")
            now = utc_now()
            if decision == "reject":
                correction = feedback or "QA requested corrections."
                con.execute(
                    "UPDATE station_runs SET status='rejected',qa_feedback=?,reviewed_at=? WHERE run_id=?",
                    (correction, now, run["run_id"])
                )
                # Keep the rejected attempt immutable and create a fresh correction run.
                con.execute(
                    """INSERT INTO station_runs(run_id,package_id,station_id,agent_id,
                    qa_supervisor_id,status,attempt,qa_feedback) VALUES(?,?,?,?,?,?,?,?)""",
                    (uuid.uuid4().hex, package_id, run["station_id"], run["agent_id"],
                     run["qa_supervisor_id"], "ready", run["attempt"] + 1, correction)
                )
                con.execute("UPDATE packages SET status='rework',updated_at=? WHERE package_id=?",
                            (now, package_id))
                result = "rework"
            else:
                con.execute("UPDATE station_runs SET status='approved',qa_feedback=?,reviewed_at=? WHERE run_id=?",
                            (feedback, now, run["run_id"]))
                package = con.execute("SELECT pipeline_json FROM packages WHERE package_id=?",
                                      (package_id,)).fetchone()
                pipeline = json.loads(package["pipeline_json"])
                index = next(i for i, item in enumerate(pipeline) if item["station_id"] == station_id)
                if index + 1 >= len(pipeline):
                    con.execute("UPDATE packages SET status='complete',current_station=NULL,updated_at=? WHERE package_id=?",
                                (now, package_id))
                    result = "complete"
                else:
                    next_station = pipeline[index + 1]
                    con.execute(
                        """INSERT INTO station_runs(run_id,package_id,station_id,agent_id,
                        qa_supervisor_id,status) VALUES(?,?,?,?,?,?)""",
                        (uuid.uuid4().hex, package_id, next_station["station_id"],
                         next_station["agent_id"], next_station["qa_supervisor_id"], "ready")
                    )
                    con.execute(
                        "UPDATE packages SET status='ready',current_station=?,updated_at=? WHERE package_id=?",
                        (next_station["station_id"], now, package_id)
                    )
                    result = f"released:{next_station['station_id']}"
            self._record_event(con, package_id, f"qa_{decision}", reviewer_id,
                               {"station_id": station_id, "feedback": feedback}, event_key)
            con.commit()
            return result

    def status(self, package_id: str | None = None) -> list[dict[str, Any]]:
        with self._connect() as con:
            if package_id:
                packages = con.execute("SELECT * FROM packages WHERE package_id=?", (package_id,)).fetchall()
            else:
                packages = con.execute("SELECT * FROM packages ORDER BY created_at DESC").fetchall()
            result = []
            for p in packages:
                runs = con.execute(
                    "SELECT station_id,agent_id,qa_supervisor_id,status,attempt,qa_feedback FROM station_runs WHERE package_id=? ORDER BY rowid",
                    (p["package_id"],)
                ).fetchall()
                result.append({
                    "package_id": p["package_id"], "type": p["package_type"],
                    "version": p["version"], "status": p["status"],
                    "current_station": p["current_station"],
                    "stations": [dict(r) for r in runs],
                    "updated_at": p["updated_at"]
                })
            return result

    def recover(self) -> dict[str, Any]:
        """Return restart-recovery snapshot; persisted work is not reset."""
        with self._connect() as con:
            counts = {row["status"]: row["n"] for row in con.execute(
                "SELECT status,COUNT(*) AS n FROM packages GROUP BY status")}
            queued = con.execute("SELECT COUNT(*) FROM station_runs WHERE status='ready'").fetchone()[0]
            qa = con.execute("SELECT COUNT(*) FROM station_runs WHERE status='qa_pending'").fetchone()[0]
            rework = con.execute("SELECT COUNT(*) FROM station_runs WHERE status='rework'").fetchone()[0]
        return {"packages_by_status": counts, "ready_station_runs": queued,
                "awaiting_qa": qa, "rework_station_runs": rework}


def _parse_qa_map(raw: str) -> dict[str, str]:
    result: dict[str, str] = {}
    if not raw:
        return result
    for pair in raw.split(","):
        if "=" not in pair:
            raise argparse.ArgumentTypeError("QA map entries must be station=supervisor.")
        station, qa = pair.split("=", 1)
        result[station.strip()] = qa.strip()
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Hustle City IntelliSync package relay")
    parser.add_argument("--db", default=str(DEFAULT_DB))
    parser.add_argument("--config", default=str(DEFAULT_CONFIG))
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("init")
    create = sub.add_parser("create")
    create.add_argument("--type", required=True)
    create.add_argument("--payload", default="{}")
    create.add_argument("--qa-map", type=_parse_qa_map, default={})
    create.add_argument("--package-id")
    claim = sub.add_parser("claim")
    claim.add_argument("--package", required=True)
    claim.add_argument("--station", required=True)
    claim.add_argument("--agent", required=True)
    submit = sub.add_parser("submit")
    submit.add_argument("--package", required=True)
    submit.add_argument("--station", required=True)
    submit.add_argument("--agent", required=True)
    submit.add_argument("--output-file", required=True)
    submit.add_argument("--event-key")
    review = sub.add_parser("review")
    review.add_argument("--package", required=True)
    review.add_argument("--station", required=True)
    review.add_argument("--reviewer", required=True)
    review.add_argument("--decision", choices=["approve", "reject"], required=True)
    review.add_argument("--feedback", default="")
    review.add_argument("--event-key")
    status = sub.add_parser("status")
    status.add_argument("--package")
    sub.add_parser("recover")
    args = parser.parse_args(argv)
    try:
        app = IntelliSync(args.db, args.config)
        if args.command == "init":
            print(f"IntelliSync database ready: {args.db}")
        elif args.command == "create":
            pid = app.create_package(args.type, json.loads(args.payload), args.qa_map, args.package_id)
            print(pid)
        elif args.command == "claim":
            app.claim(args.package, args.station, args.agent)
            print("claimed")
        elif args.command == "submit":
            output = Path(args.output_file).read_text(encoding="utf-8")
            app.submit(args.package, args.station, args.agent, output, args.event_key)
            print("submitted_for_qa")
        elif args.command == "review":
            print(app.review(args.package, args.station, args.reviewer,
                             args.decision, args.feedback, args.event_key))
        elif args.command == "status":
            print(json.dumps(app.status(args.package), indent=2))
        elif args.command == "recover":
            print(json.dumps(app.recover(), indent=2))
        return 0
    except (RuntimeErrorBase, sqlite3.Error, ValueError, OSError) as exc:
        print(f"intellisync: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
