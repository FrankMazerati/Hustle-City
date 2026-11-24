# Hustle City IntelliSync Runtime — starter implementation

This is the first executable orchestration layer for the rolling package relay. It is deliberately separate from the older six-role manual GitHub pilot and does not activate that workflow.

## What this version does

- Creates durable work packages in SQLite.
- Sends each package through the configured station sequence.
- Lets the assigned station agent claim and submit a deliverable.
- Moves each submission into its assigned QA supervisor's review queue.
- Releases the next station only after QA approval.
- Sends rejected work back to the same station for correction.
- Prevents self-approval and review by the wrong QA supervisor.
- Records event history and ignores repeated event keys.
- Preserves queue state across process restarts.
- Supports multiple packages in the same database; independent packages can be in progress at different stations.

## Local Ollama worker pilot (new)

The first local worker layer is now available:

- `intellisync/config/model_assignments.json` contains a provisional 17-role mapping to a six-model pool. It is not a verified device inventory or benchmark-proven assignment. `intellisync/config/agents.json` separately contains a user-reported inventory and an empty active model map. Reconcile both files against the live tablet `ollama list` before activation.
- `python -m intellisync.worker list` displays the mapping without calling a model.
- `python -m intellisync.worker run --agent P01-GEOGRAPHY --task "..." ` invokes one model for one task through the local Ollama HTTP API.
- Runs are serialized with a filesystem lock, and `keep_alive: 0` asks Ollama to unload the model after the task.
- Deliverables and a JSONL run record are saved under `data/agent_runs/`.

This is an on-demand single-task worker, not an always-on agent fleet. It has no repository write tools, does not commit code, and does not autonomously claim package-relay tasks. Ollama endpoint reachability and model performance must be tested on the tablet before any worker is treated as verified live.

## What it does not do yet

- It does not autonomously schedule or continuously invoke the 17 roles. Workers are started manually, one task at a time. The current local workforce target is SCRIBE, LENS, three QA supervisors and twelve production specialists; ChatGPT is external coordinator, not a local worker.
- The scheduler in `intellisync/services.py` now uses a rolling queue: QA-pending packages and unrelated ready production/correction packages can advance in the same tick. A single bounded executor caps simultaneous model calls; the safe configured default remains one. This removes the old global production → QA → correction phase barrier. Exact 20/5/5 wall-clock deadlines, correction expiry/escalation, and the optional 10-minute extension are still not enforced; the current worker is a one-shot model invocation, not a 20-minute autonomous checkpointing session. See `intellisync/OVERLAPPING_WORKFORCE_SPEC.md` and `intellisync/IMPLEMENTATION_STATUS.md`.
- It does not connect to Supabase. SQLite is a local starter adapter pending confirmation of the dedicated project.
- It does not change the existing model router or old manual GitHub pilot.
- It does not merge code, deploy services, spend money, or activate schedules.

The starter pipeline contains the geography-to-city opening stations: World Builder → City Builder → Roads & Infrastructure → Building & Architecture. The exact QA-supervisor-to-specialist ownership map is not guessed. Supply an explicit QA mapping for every station at package creation until the approved roster mapping is configured.

## Requirements

Python 3.10+; standard library only.

## Run

    python -m intellisync.runtime init
    python -m unittest discover -s intellisync/tests -v

Create a package and map every station to its approved QA supervisor:

    python -m intellisync.runtime create --type geography_to_city --payload '{"objective":"Build the approved world-to-city foundation"}' --qa-map world-builder=QA-1,city-builder=QA-1,roads-infrastructure=QA-2,building-architecture=QA-2

The QA IDs above are examples only; replace them with the actual approved ownership map. Do not copy the example as a permanent assignment.

Then use the package ID returned by create with the claim, submit, review, status and recover commands. A review decision must come from the configured QA supervisor.

## State model

ready → in_progress → qa_pending → approved → next station ready

A QA rejection creates a correction state for the same station:

qa_pending → rejected attempt + new ready correction attempt → in_progress → qa_pending

After the last station passes QA, the package becomes complete. Downstream work never starts from an unapproved station output.

## Safety and operating rules

- Configure QA ownership explicitly; no inferred roster mapping.
- Agent IDs in the starter pipeline are functional role IDs, not approved permanent agent names.
- SCRIBE and LENS remain separate creative leads and are not forced into this geography pipeline.
- Trinity remains the coordinator above the three QA supervisors; coordinator audit/assignment services are a later layer.
- Do not mark a model endpoint verified until it is tested on the actual device.
- Keep API keys outside Git.
- Do not connect or mutate a Supabase project until the creator confirms the dedicated IntelliSync database.
