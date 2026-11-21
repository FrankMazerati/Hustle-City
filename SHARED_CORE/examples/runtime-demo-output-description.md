# IntelliSync local runtime demonstration

Run from the repository root:

```bash
python SHARED_CORE/tools/intellisync_runtime_demo.py
```

The demonstration reads `frank-companion-event-dialogue-flow.json`, routes its sample discoverable event to the sample online player when the player is in the event audience, and validates that the conversation has contiguous turns spoken only by registered participants.

The output includes event discovery/invitation records and the ordered conversation turns, including Frank's Companion's response. Her permanent character name remains undecided.

This is a deterministic local prototype. It does not yet provide live multiplayer delivery, server persistence, actual AI-generated dialogue, voice, or Unreal Engine integration. Those are separate implementation steps.
