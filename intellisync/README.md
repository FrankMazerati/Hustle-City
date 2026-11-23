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

## What it does not do yet

- It does not autonomously invoke all 17 local agents. The current local workforce target is SCRIBE, LENS, three QA supervisors and twelve production specialists; ChatGPT is external coordinator, not a local worker.
- It does not yet run continuous background workers or enforce a global concurrency semaphore.
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
