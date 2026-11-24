"""On-demand Ollama worker for the 17-agent Hustle City local workforce.

This runner executes one explicitly requested task. It does not create a scheduler,
grant repository write access, or claim that persistent agents are running.
"""
from __future__ import annotations

import argparse
import fcntl
import json
import os
import sys
import time
import urllib.error
import urllib.request
import uuid
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSIGNMENTS = ROOT / "intellisync" / "config" / "model_assignments.json"
WORKFORCE = ROOT / "intellisync" / "config" / "coordination.json"
MASTER_CONTEXT = ROOT / "AI" / "KNOWLEDGE" / "HUSTLE_CITY_MASTER_CONTEXT.md"
PROMPTS = ROOT / "agents" / "AGENT_PROMPTS.md"
RUNS = ROOT / "data" / "agent_runs"
LOCK = ROOT / "data" / "agent-runtime.lock"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_agent(agent_id: str):
    cfg = read_json(ASSIGNMENTS)
    workforce = read_json(WORKFORCE)["local_workforce"]
    roster = []
    roster.extend(workforce.get("creative_leads", []))
    roster.extend(workforce.get("qa_supervisors", []))
    roster.extend(workforce.get("production_specialists", []))
    role = next((a for a in roster if a.get("id") == agent_id), None)
    assignment = next((a for a in cfg["agents"] if a["agent_id"] == agent_id), None)
    if role is None or assignment is None:
        raise ValueError(f"Unknown or unassigned local agent: {agent_id}")
    if not assignment.get("enabled", False):
        raise ValueError(f"Agent is disabled: {agent_id}")
    return role, assignment, cfg


def build_prompt(agent_id: str, role: dict, assignment: dict, task: str) -> str:
    context = MASTER_CONTEXT.read_text(encoding="utf-8") if MASTER_CONTEXT.exists() else ""
    prompt_pack = PROMPTS.read_text(encoding="utf-8") if PROMPTS.exists() else ""
    responsibilities = role.get("responsibilities", [])
    if isinstance(responsibilities, list):
        responsibilities = "\n".join(f"- {item}" for item in responsibilities)
    qa_scope = ""
    if role.get("specialist_ids"):
        qa_scope = "\nQA ownership: " + ", ".join(role["specialist_ids"])
    return f"""You are {agent_id}, a local specialist in the Hustle City production workforce.
Role: {role.get('role', 'QA Supervisor')}
Assigned model profile: {assignment.get('profile')}
Responsibilities:
{responsibilities}{qa_scope}

Operating rules:
- ChatGPT is the external overall coordinator; there is no local Trinity worker.
- The creator retains final authority over vision, canon, scope and irreversible decisions.
- Work only within this agent's role. Do not invent approvals, facts, assets, tests or completed work.
- Distinguish confirmed project decisions from proposals and assumptions.
- Identify dependencies, risks, acceptance criteria and the QA reviewer.
- Do not claim to have edited files, run tests, browsed the web or committed code. You have no tools in this session.
- Produce a useful, structured deliverable for the requested task. State open questions rather than silently guessing.

PROJECT MASTER CONTEXT:
{context}

SHARED AGENT PROMPT REFERENCE:
{prompt_pack}

ASSIGNED TASK:
{task}

Return the deliverable in Markdown with: task understanding, assumptions, proposed work, dependencies, risks, acceptance criteria, and next handoff."""


def ollama_generate(cfg: dict, model: str, prompt: str) -> str:
    endpoint = cfg.get("endpoint", {})
    base = endpoint.get("base_url", "http://127.0.0.1:11434").rstrip("/")
    url = base + endpoint.get("generate_path", "/api/generate")
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "keep_alive": 0
    }
    request = urllib.request.Request(
        url, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST"
    )
    timeout = int(endpoint.get("timeout_seconds", 900))
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.URLError as exc:
        reason = getattr(exc, "reason", exc)
        raise RuntimeError(
            f"Cannot reach Ollama at {url}. Confirm the Ollama server is running in Termux. Details: {reason}"
        ) from exc
    text = data.get("response", "").strip()
    if not text:
        raise RuntimeError("Ollama returned an empty response.")
    return text


def command_list():
    cfg = read_json(ASSIGNMENTS)
    workforce = read_json(WORKFORCE)["local_workforce"]
    roster = workforce.get("creative_leads", []) + workforce.get("qa_supervisors", []) + workforce.get("production_specialists", [])
    by_id = {a["agent_id"]: a for a in cfg["agents"]}
    print("AGENT                 MODEL                  PROFILE")
    print("-" * 88)
    for role in roster:
        a = by_id.get(role["id"])
        if a:
            print(f"{role['id']:<21} {a['model']:<22} {a['profile']}")
        else:
            print(f"{role['id']:<21} UNASSIGNED")


def command_run(agent_id: str, task: str):
    role, assignment, cfg = load_agent(agent_id)
    RUNS.mkdir(parents=True, exist_ok=True)
    LOCK.parent.mkdir(parents=True, exist_ok=True)
    with LOCK.open("w", encoding="utf-8") as lock_handle:
        print("Waiting for the shared local-model slot...")
        fcntl.flock(lock_handle.fileno(), fcntl.LOCK_EX)
        print(f"Starting {agent_id} with {assignment['model']} (single task; serialized).")
        prompt = build_prompt(agent_id, role, assignment, task)
        started = time.monotonic()
        output = ollama_generate(cfg, assignment["model"], prompt)
        elapsed = round(time.monotonic() - started, 2)
        run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:6]
        out_dir = RUNS / agent_id
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{run_id}.md"
        metadata = (
            f"<!-- agent_id: {agent_id}\nmodel: {assignment['model']}\n"
            f"run_id: {run_id}\nelapsed_seconds: {elapsed}\n"
            f"created_at: {datetime.now(timezone.utc).isoformat()} -->\n\n"
        )
        out_path.write_text(metadata + output + "\n", encoding="utf-8")
        record = {
            "run_id": run_id, "agent_id": agent_id, "model": assignment["model"],
            "status": "completed", "elapsed_seconds": elapsed,
            "output_path": str(out_path.relative_to(ROOT)),
            "created_at": datetime.now(timezone.utc).isoformat()
        }
        with (RUNS / "runs.jsonl").open("a", encoding="utf-8") as log:
            log.write(json.dumps(record) + "\n")
        print(f"Completed in {elapsed}s")
        print(f"Deliverable: {out_path.relative_to(ROOT)}")
        print(output)


def main():
    parser = argparse.ArgumentParser(description="Hustle City on-demand local Ollama worker")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("list", help="show all 17 agent-to-model assignments")
    run = sub.add_parser("run", help="run one task with one assigned local model")
    run.add_argument("--agent", required=True, help="agent ID from the 17-role roster")
    run.add_argument("--task", required=True, help="specific task instruction")
    args = parser.parse_args()
    try:
        if args.command == "list":
            command_list()
        elif args.command == "run":
            command_run(args.agent, args.task)
        return 0
    except (OSError, ValueError, RuntimeError, KeyError, json.JSONDecodeError) as exc:
        print(f"hustle-city-agent: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
