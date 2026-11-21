#!/usr/bin/env python3
"""Engine-neutral IntelliSync dependency impact checker (Python standard library only)."""
from __future__ import annotations

import argparse
import json
import sys
from collections import deque
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_REGISTRY = ROOT / "SHARED_CORE/content/world-intelligence-registry.json"


class RegistryError(ValueError):
    pass


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RegistryError(f"Cannot read valid JSON from {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise RegistryError(f"{path} must contain a JSON object")
    return data


def build_graph(registry: dict[str, Any]) -> tuple[dict[str, dict[str, Any]], dict[str, set[str]]]:
    systems_list = registry.get("systems")
    if not isinstance(systems_list, list):
        raise RegistryError("Registry must contain a systems array")
    systems: dict[str, dict[str, Any]] = {}
    graph: dict[str, set[str]] = {}
    for item in systems_list:
        if not isinstance(item, dict) or not isinstance(item.get("id"), str):
            raise RegistryError("Every system must be an object with a string id")
        sid = item["id"]
        if sid in systems:
            raise RegistryError(f"Duplicate system id: {sid}")
        systems[sid] = item
        graph[sid] = set()
    for sid, item in systems.items():
        deps = item.get("depends_on", [])
        if not isinstance(deps, list):
            raise RegistryError(f"{sid}.depends_on must be an array")
        for dep in deps:
            if dep not in systems:
                raise RegistryError(f"{sid} depends on unknown system: {dep}")
            graph[sid].add(dep)
            graph[dep].add(sid)
    for rel in registry.get("relationships", []):
        if not isinstance(rel, dict):
            raise RegistryError("Every relationship must be an object")
        source, target = rel.get("from"), rel.get("to")
        if source not in systems or target not in systems:
            raise RegistryError(f"Relationship references unknown systems: {source} -> {target}")
        # Impact review is intentionally bidirectional: either side may be affected.
        graph[source].add(target)
        graph[target].add(source)
    return systems, graph


def analyze_change(registry: dict[str, Any], change: dict[str, Any]) -> dict[str, Any]:
    systems, graph = build_graph(registry)
    changed = change.get("changed_systems")
    if not isinstance(changed, list) or not changed or not all(isinstance(x, str) for x in changed):
        raise RegistryError("Change must provide a non-empty changed_systems array of system IDs")
    unknown = sorted(set(changed) - systems.keys())
    if unknown:
        raise RegistryError("Unknown changed system ID(s): " + ", ".join(unknown))

    depth_limit = change.get("max_dependency_depth", 1)
    if not isinstance(depth_limit, int) or isinstance(depth_limit, bool) or depth_limit < 1:
        raise RegistryError("max_dependency_depth must be a positive integer")

    distance = {sid: 0 for sid in set(changed)}
    queue = deque(sorted(set(changed)))
    while queue:
        current = queue.popleft()
        if distance[current] >= depth_limit:
            continue
        for neighbor in sorted(graph[current]):
            next_depth = distance[current] + 1
            if neighbor not in distance or next_depth < distance[neighbor]:
                distance[neighbor] = next_depth
                queue.append(neighbor)

    affected = sorted(distance, key=lambda sid: (distance[sid], sid))
    reviewers = []
    for sid in affected:
        owner = systems[sid].get("owner_agent")
        reviewers.append({
            "system_id": sid,
            "system_name": systems[sid].get("name", sid),
            "owner_agent": owner,
            "review_required": sid not in changed,
            "impact_depth": distance[sid]
        })

    return {
        "analysis_version": "1.0.0",
        "change_id": change.get("change_id", "unspecified-change"),
        "summary": change.get("summary", ""),
        "changed_systems": sorted(set(changed)),
        "affected_systems": affected,
        "reviewers": reviewers,
        "review_required_from": sorted({
            systems[sid].get("owner_agent") for sid in affected
            if sid not in changed and systems[sid].get("owner_agent")
        }),
        "approval": "pending_owner_review",
        "notes": [
            "Impact is a conservative dependency neighborhood, not proof of a runtime defect.",
            "Reviewers must inspect the actual diff and run applicable tests.",
            "No changes are applied or approved by this checker."
        ]
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("change_file", type=Path, help="JSON file describing the proposed change")
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--output", type=Path, help="Optional output JSON path")
    args = parser.parse_args()
    try:
        result = analyze_change(load_json(args.registry), load_json(args.change_file))
    except RegistryError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    rendered = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
