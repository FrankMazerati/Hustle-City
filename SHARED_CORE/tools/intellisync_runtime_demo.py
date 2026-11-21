#!/usr/bin/env python3
"""Run a local, deterministic IntelliSync player/event/dialogue demonstration.

This is a small engine-neutral prototype. It routes one sample event to one
player context and validates ordered dialogue turns. It does not connect to a
multiplayer server, generate AI dialogue, persist player state, or contact NPCs.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def route_event(player: dict[str, Any], event: dict[str, Any]) -> dict[str, Any]:
    player_id = player["player_id"]
    if player.get("presence") != "online":
        return {"delivered": False, "reason": "player_not_online", "event_id": event["event_id"]}

    status = event.get("status")
    if status not in ("discoverable", "invited", "in_progress"):
        return {"delivered": False, "reason": "event_not_available", "event_id": event["event_id"]}

    visibility = event.get("audience", {}).get("visibility")
    eligible = event.get("audience", {}).get("eligible_player_ids", [])
    if visibility in ("invitation_only", "party", "crew", "nearby") and player_id not in eligible:
        return {"delivered": False, "reason": "player_not_in_event_audience", "event_id": event["event_id"]}

    if visibility not in ("public", "nearby", "invitation_only", "party", "crew"):
        return {"delivered": False, "reason": "unsupported_visibility", "event_id": event["event_id"]}

    return {
        "delivered": True,
        "reason": "eligible_player",
        "player_id": player_id,
        "event_id": event["event_id"],
        "event_title": event["title"],
        "event_status": status,
        "event_location": event["location"]["area_id"],
        "notifications": [
            {"event_type": "world.event.discovered", "player_id": player_id, "event_id": event["event_id"]},
            {"event_type": "world.event.invited", "player_id": player_id, "event_id": event["event_id"]}
        ]
    }


def validate_dialogue(session: dict[str, Any]) -> dict[str, Any]:
    participants = session.get("participants", [])
    participant_ids = {p.get("speaker_id") for p in participants}
    if len(participant_ids) != len(participants):
        raise ValueError("dialogue participant speaker_id values must be unique")
    if not session.get("coordinator_id"):
        raise ValueError("dialogue session requires a coordinator_id")

    turns = session.get("turns", [])
    for expected_index, turn in enumerate(turns):
        if turn.get("turn_index") != expected_index:
            raise ValueError("dialogue turns must have contiguous zero-based turn_index values")
        if turn.get("speaker_id") not in participant_ids:
            raise ValueError(f"turn {expected_index} uses a speaker not in the session")
        if not isinstance(turn.get("text"), str) or not turn["text"].strip():
            raise ValueError(f"turn {expected_index} must contain non-empty dialogue text")

    declared_index = session.get("turn_index")
    if declared_index != (len(turns) - 1 if turns else 0):
        raise ValueError("session turn_index must match the last recorded turn")

    return {
        "session_id": session["session_id"],
        "status": session["status"],
        "coordinator_id": session["coordinator_id"],
        "turn_count": len(turns),
        "participants": [p["speaker_id"] for p in participants],
        "turns": [
            {
                "turn_index": turn["turn_index"],
                "speaker_id": turn["speaker_id"],
                "display_name": next(
                    p.get("display_name", p["speaker_id"])
                    for p in participants if p["speaker_id"] == turn["speaker_id"]
                ),
                "text": turn["text"],
                "intent": turn.get("intent")
            }
            for turn in turns
        ],
        "next_turn_index": len(turns)
    }


def run_demo(data: dict[str, Any]) -> dict[str, Any]:
    player = data["player_context"]
    event = data["world_event"]
    session = data["dialogue_session"]
    event_result = route_event(player, event)
    dialogue_result = validate_dialogue(session)
    return {
        "demo_version": "1.0.0",
        "player_event_routing": event_result,
        "dialogue": dialogue_result,
        "story_character_note": (
            "Frank's Companion is a temporary display label; her permanent name remains undecided."
        ),
        "runtime_boundary": (
            "Local deterministic demonstration only; no live multiplayer delivery, "
            "AI-generated responses, or persistent storage."
        )
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "input", nargs="?", type=Path,
        default=Path("SHARED_CORE/examples/frank-companion-event-dialogue-flow.json"),
        help="Player/event/dialogue example JSON"
    )
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
        result = run_demo(data)
    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
        parser.error(str(exc))
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
