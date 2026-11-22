#!/usr/bin/env python3
"""Build a daily IntelliSync team snapshot from an explicit roster and reports.

This tool is deliberately read-only: it reports missing/stale updates, blockers,
pending reviews, and completed work. It does not contact agents, schedule itself,
change assignments, or modify source files.
"""
from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path
from typing import Any


def build_daily_snapshot(data: dict[str, Any]) -> dict[str, Any]:
    snapshot_date = date.fromisoformat(data["snapshot_date"])
    roster = data.get("roster", [])
    reports = data.get("reports", [])
    if not isinstance(roster, list) or not isinstance(reports, list):
        raise ValueError("roster and reports must be lists")

    roster_by_id: dict[str, dict[str, Any]] = {}
    for member in roster:
        agent_id = member.get("agent_id")
        if not isinstance(agent_id, str) or not agent_id.strip():
            raise ValueError("every roster member needs a non-empty agent_id")
        if agent_id in roster_by_id:
            raise ValueError(f"duplicate roster agent_id: {agent_id}")
        roster_by_id[agent_id] = member

    reports_by_id: dict[str, dict[str, Any]] = {}
    for report in reports:
        agent_id = report.get("agent_id")
        if agent_id not in roster_by_id:
            raise ValueError(f"report submitted by unknown agent: {agent_id}")
        if agent_id in reports_by_id:
            raise ValueError(f"duplicate daily report for agent: {agent_id}")
        report_date = date.fromisoformat(report["report_date"])
        if report_date > snapshot_date:
            raise ValueError(f"report date is after snapshot date for agent: {agent_id}")
        reports_by_id[agent_id] = report

    entries = []
    totals = {
        "roster_count": len(roster_by_id),
        "reports_received": len(reports_by_id),
        "reports_missing": 0,
        "reports_stale": 0,
        "blockers": 0,
        "reviews_pending": 0,
        "completed_items": 0,
        "in_progress_items": 0,
    }

    for agent_id, member in sorted(roster_by_id.items()):
        report = reports_by_id.get(agent_id)
        if report is None:
            status = "missing_report"
            report_date = None
            completed, in_progress, blockers, reviews = [], [], [], []
            if member.get("report_required", True):
                totals["reports_missing"] += 1
        else:
            report_date = report["report_date"]
            completed = report.get("completed", [])
            in_progress = report.get("in_progress", [])
            blockers = report.get("blockers", [])
            reviews = report.get("reviews_pending", [])
            status = "current" if report_date == snapshot_date.isoformat() else "stale_report"
            if status == "stale_report":
                totals["reports_stale"] += 1

        totals["blockers"] += len(blockers)
        totals["reviews_pending"] += len(reviews)
        totals["completed_items"] += len(completed)
        totals["in_progress_items"] += len(in_progress)
        entries.append({
            "agent_id": agent_id,
            "role": member.get("role", "unassigned"),
            "status": status,
            "report_date": report_date,
            "completed": completed,
            "in_progress": in_progress,
            "blockers": blockers,
            "reviews_pending": reviews,
        })

    return {
        "snapshot_version": "1.0.0",
        "snapshot_date": snapshot_date.isoformat(),
        "timezone": data.get("timezone", "not_specified"),
        "project": data.get("project", "Hustle City"),
        "totals": totals,
        "agents": entries,
        "actions_required": [
            {"agent_id": entry["agent_id"], "action": entry["status"]}
            for entry in entries if entry["status"] in ("missing_report", "stale_report")
        ],
        "governance_note": (
            "Read-only reconciliation. Missing or stale reports are flagged; "
            "assignments are not changed and no agent is contacted by this tool."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Daily roster and report JSON")
    parser.add_argument("--output", type=Path, help="Optional path for the snapshot JSON")
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
        result = build_daily_snapshot(data)
    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
        parser.error(str(exc))
    rendered = json.dumps(result, indent=2, ensure_ascii=False)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
