#!/usr/bin/env python3
"""Interactive local dialogue prototype with one coordinator and persistent turns.

This uses deliberately simple deterministic responses, not an LLM or live game
service. It is intended to test turn ownership, continuity, and session storage.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Any

DEFAULT_INPUT = Path("SHARED_CORE/examples/frank-companion-event-dialogue-flow.json")
DEFAULT_SESSION = Path.home() / ".hustle-city" / "sessions" / "downtown-welcome-dialogue.json"
PLAYER_ID = "player.demo.001"
VENDOR_ID = "npc.vendor.014"
COMPANION_ID = "character.frank_companion_temporary"


def now_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def create_session(input_path: Path) -> dict[str, Any]:
    data = json.loads(input_path.read_text(encoding="utf-8"))
    session = data["dialogue_session"]
    # Copy through JSON so the saved session is independent of the fixture.
    return json.loads(json.dumps(session))


def validate_session(session: dict[str, Any]) -> None:
    participants = session.get("participants", [])
    ids = [p.get("speaker_id") for p in participants]
    if len(ids) != len(set(ids)):
        raise ValueError("participant speaker_id values must be unique")
    if not session.get("coordinator_id"):
        raise ValueError("session requires one dialogue coordinator")
    if session.get("status") != "active":
        raise ValueError("only active dialogue sessions can accept turns")
    turns = session.get("turns", [])
    for index, turn in enumerate(turns):
        if turn.get("turn_index") != index:
            raise ValueError("turn indexes must be contiguous and zero-based")
        if turn.get("speaker_id") not in ids:
            raise ValueError(f"turn {index} has an unregistered speaker")
        if not isinstance(turn.get("text"), str) or not turn["text"].strip():
            raise ValueError(f"turn {index} has empty dialogue text")
    expected = len(turns) - 1 if turns else 0
    if session.get("turn_index") != expected:
        raise ValueError("turn_index must match the last recorded turn")


def choose_reply_speaker(player_text: str) -> str:
    """Coordinator policy: acceptance/companion references route to companion."""
    text = player_text.lower()
    companion_cues = (
        "let's go", "lets go", "we should go", "sounds good", "i'm in",
        "im in", "yeah", "sure", "tell her", "what do you think"
    )
    if any(cue in text for cue in companion_cues):
        return COMPANION_ID
    return VENDOR_ID


def generate_local_reply(speaker_id: str, player_text: str) -> tuple[str, str]:
    """Small authored response set used only to exercise the conversation loop."""
    text = player_text.lower()
    if speaker_id == COMPANION_ID:
        if any(word in text for word in ("what do you think", "you think", "her opinion")):
            return ("I'm curious. We just got here, so let's take a look around and get a feel for the city.", "share_opinion")
        return ("I'm with you. Let's head over to the plaza and see what's happening.", "accept_event_invitation")

    if any(word in text for word in ("where", "how do we get", "which way")):
        return ("Head straight down this street toward the plaza. You can't miss the music and the crowd.", "give_directions")
    if any(word in text for word in ("who", "people", "vendors")):
        return ("Local folks, small businesses, music, and people getting to know the neighborhood. It's a good first stop.", "describe_attendees")
    if any(word in text for word in ("thank", "appreciate")):
        return ("Anytime. Enjoy the city, and tell the folks at the plaza the vendor sent you.", "farewell")
    return ("It's a good place to get your bearings. There's music, local businesses, and plenty of people to meet.", "continue_event_explanation")


def append_turn(session: dict[str, Any], speaker_id: str, text: str, intent: str) -> None:
    session["turns"].append({
        "turn_index": len(session["turns"]),
        "speaker_id": speaker_id,
        "text": text,
        "occurred_at": now_iso(),
        "intent": intent,
        "triggered_event_ref": session.get("context", {}).get("event_ref")
    })
    session["turn_index"] = len(session["turns"]) - 1
    session["updated_at"] = now_iso()


def process_player_turn(session: dict[str, Any], player_text: str) -> dict[str, Any]:
    validate_session(session)
    clean_text = player_text.strip()
    if not clean_text:
        raise ValueError("player message cannot be empty")
    if len(clean_text) > 4000:
        raise ValueError("player message cannot exceed 4000 characters")
    participants = {p["speaker_id"] for p in session["participants"]}
    if PLAYER_ID not in participants:
        raise ValueError("demo player is not registered in this dialogue session")

    append_turn(session, PLAYER_ID, clean_text, "player_response")
    reply_speaker = choose_reply_speaker(clean_text)
    if reply_speaker not in participants:
        raise ValueError("coordinator selected a speaker outside this session")
    reply_text, reply_intent = generate_local_reply(reply_speaker, clean_text)
    append_turn(session, reply_speaker, reply_text, reply_intent)
    validate_session(session)
    return {
        "player_turn": session["turns"][-2],
        "coordinator_id": session["coordinator_id"],
        "selected_speaker_id": reply_speaker,
        "reply_turn": session["turns"][-1],
        "next_turn_index": len(session["turns"])
    }


def save_session(session: dict[str, Any], path: Path) -> None:
    validate_session(session)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(session, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    temporary.replace(path)


def load_or_create_session(input_path: Path, session_path: Path, reset: bool = False) -> dict[str, Any]:
    if session_path.exists() and not reset:
        session = json.loads(session_path.read_text(encoding="utf-8"))
        validate_session(session)
        return session
    session = create_session(input_path)
    validate_session(session)
    save_session(session, session_path)
    return session


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT, help="Dialogue fixture JSON")
    parser.add_argument("--session-file", type=Path, default=DEFAULT_SESSION, help="Persistent local session JSON")
    parser.add_argument("--reset", action="store_true", help="Start again from the example conversation")
    args = parser.parse_args()

    try:
        session = load_or_create_session(args.input, args.session_file, args.reset)
    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
        parser.error(str(exc))

    names = {p["speaker_id"]: p.get("display_name", p["speaker_id"]) for p in session["participants"]}
    print("HUSTLE CITY — DOWNTOWN CONVERSATION")
    print("Coordinator:", session["coordinator_id"])
    print("Session:", session["session_id"])
    print("Saved at:", args.session_file)
    print("Type /quit to leave. Your conversation will be saved.\n")
    last = session["turns"][-1] if session["turns"] else None
    if last:
        print(f'{names.get(last["speaker_id"], last["speaker_id"])}: {last["text"]}')

    while True:
        try:
            player_text = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nLeaving conversation.")
            break
        if player_text.lower() in ("/quit", "/exit"):
            break
        if not player_text:
            print("Type a response, or /quit to leave.")
            continue
        try:
            result = process_player_turn(session, player_text)
            save_session(session, args.session_file)
        except (OSError, ValueError) as exc:
            print("Could not process that turn:", exc)
            continue
        reply = result["reply_turn"]
        print(f'{names.get(reply["speaker_id"], reply["speaker_id"])}: {reply["text"]}')
        print(f'[{result["coordinator_id"]} assigned turn {reply["turn_index"]}; session saved]')
    save_session(session, args.session_file)
    print(f"Saved {len(session['turns'])} turns to {args.session_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
