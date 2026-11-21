# IntelliSync dependency checker

A first, engine-neutral dependency-impact tool for Hustle City's shared world registry. It uses only Python's standard library.

## Run it

From the repository root:

```bash
python SHARED_CORE/tools/intellisync_dependency_check.py SHARED_CORE/examples/traffic-signal-change.json
```

Save a report:

```bash
python SHARED_CORE/tools/intellisync_dependency_check.py SHARED_CORE/examples/traffic-signal-change.json --output /tmp/intellisync-impact.json
```

Run tests:

```bash
python -m unittest discover -s SHARED_CORE/tools/tests -v
```

## Impact behavior

The checker starts with the changed system IDs, then expands through the registry's declared dependencies and relationships. The default fixture uses depth 1, so a traffic-signal change identifies directly connected systems and their owners for review. Increase `max_dependency_depth` to explore a wider dependency neighborhood.

This is deliberately conservative: an affected system is a review candidate, not proof that it contains a defect. The tool never edits project files, approves a change, or silently applies a recommendation. Review and approval remain explicit.

The registry's `owner_agent` fields identify intended role ownership only; they do not prove that those agents are currently activated or running.


## Daily IntelliSync reconciliation

Build a read-only daily team snapshot from the current roster and submitted reports:

```bash
python SHARED_CORE/tools/intellisync_daily_sync.py SHARED_CORE/examples/daily-sync-input.json
python SHARED_CORE/tools/intellisync_daily_sync.py SHARED_CORE/examples/daily-sync-input.json --output /tmp/hustle-city-daily-sync.json
```

The report identifies missing and stale updates, completed and in-progress work, blockers, and pending reviews. Replace the example roster/reports with the actual daily inputs before treating a snapshot as operational. This command does not contact agents or schedule itself; a recurring scheduler and authenticated report intake are separate deployment steps.

Run all tool tests:

```bash
python -m unittest discover -s SHARED_CORE/tools/tests -v
```


## Player, world-event, and dialogue contracts

The first runtime-facing contracts are now defined:

- `SHARED_CORE/schemas/player-event-context.schema.json` — player session, presence, location reference, party/crew context, and event-discovery preferences.
- `SHARED_CORE/schemas/world-event-lifecycle.schema.json` — event visibility, eligibility, invitations/participation state, lifecycle, and outcome.
- `SHARED_CORE/schemas/dialogue-session.schema.json` — participants, single session coordinator, ordered turns, continuity context, and interruptions.
- `SHARED_CORE/examples/frank-companion-event-dialogue-flow.json` — illustrative end-to-end example with Frank Maserati and **Frank's Companion**. Her permanent name remains undecided.

Validate that these files are syntactically valid JSON:

```bash
python -m json.tool SHARED_CORE/schemas/player-event-context.schema.json > /dev/null
python -m json.tool SHARED_CORE/schemas/world-event-lifecycle.schema.json > /dev/null
python -m json.tool SHARED_CORE/schemas/dialogue-session.schema.json > /dev/null
python -m json.tool SHARED_CORE/examples/frank-companion-event-dialogue-flow.json > /dev/null
```

These are data contracts and a sample sequence, not a deployed multiplayer event service or live conversational AI runtime. The next implementation step is a local event/session prototype that validates event routing and dialogue turn ownership before engine integration.
