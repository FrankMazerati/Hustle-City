# IntelliSync Overlapping Workforce Operating Specification

**Authority:** Creator-approved operating decision, 2026-11-23  
**Status:** Normative scheduling target; runtime implementation and device capacity still require verification.  
**Coordinator:** ChatGPT in the coordinating conversation. There is no local Trinity model or agent.

## 1. Canonical workforce

The local target remains exactly 17 agents:

- Creative leads: SCRIBE and LENS.
- QA supervisors: QA-1, QA-2, QA-3.
- Production specialists: P01 through P12.

QA ownership is fixed:

| QA supervisor | Production specialists |
|---|---|
| QA-1 | P01-GEOGRAPHY, P02-CITY-PLAN, P03-DISTRICTS, P04-ARCHITECTURE |
| QA-2 | P05-INTERIORS, P06-TRANSIT, P07-VEHICLES, P08-CHARACTERS |
| QA-3 | P09-NPC-NAV, P10-GAMEPLAY, P11-ONBOARDING, P12-UNREAL-INTEGRATION |

SCRIBE and LENS remain parallel creative leads. Their deliverables require independent review; neither may approve their own work. ChatGPT coordinates priorities, dependencies, conflict resolution, and QA oversight but is not counted among the 17 local agents.

## 2. Rolling, overlapping production

The three groups are overlapping production waves, not a single-file sequence:

- Alpha: P01–P04, reviewed by QA-1.
- Bravo: P05–P08, reviewed by QA-2.
- Charlie: P09–P12, reviewed by QA-3.

A wave's start time is scheduler-controlled and may be staggered. A later wave may produce while an earlier wave has packages in independent QA or correction. A QA supervisor may review eligible submissions while unrelated production continues.

The waves are staffing and QA ownership groups, not mandatory dependency order. Actual package handoffs follow the configured workstream dependency graph. A downstream task may begin only when its required upstream package version is approved. Independent packages and unrelated tasks may proceed in parallel.

## 3. Required 20/5/5 cycle

Preserve this cycle for each agent/package work cycle:

1. **20 minutes — production:** the assigned worker advances its scoped package and records a checkpoint or submits a completed deliverable.
2. **5 minutes — independent QA:** the assigned QA supervisor reviews the submitted version against explicit acceptance criteria and records evidence.
3. **5 minutes — correction:** if QA rejects or requests changes, the originating worker patches that package version and resubmits it. An approved package is released to its next eligible dependency instead.

The 5-minute QA period is an independent review window, not permission for the producer to review its own work. QA can start as soon as a deliverable is submitted; the scheduler must not delay a ready review just to align it with a global clock.

If the correction/re-review work cannot be completed in the normal cycle, allow the existing optional 10-minute extension. The extension is for correction and independent re-review, not automatic approval. Unresolved work remains queued or escalated with its state preserved.

**Important:** 20/5/5 is a per-agent/package operating cadence, not three global phases that stop all production during QA. Production, QA, and correction windows for different packages must overlap.

## 4. Resource-aware execution

The scheduler separates logical agent availability from simultaneous model inference:

- All 17 roles remain configured and eligible for assignment.
- Each role has one assigned local Ollama model at a time. Model sharing is allowed when capacity requires it; an agent must not run two local models simultaneously for itself.
- The resource manager controls active inference calls, model loading/unloading, memory headroom, CPU pressure, queue priority, and timeouts.
- The tablet is the dedicated primary workstation. Do not require moving the external drive between devices.
- Start with a conservative measured inference limit, then raise concurrency one step at a time after device benchmarks. Do not treat swap as equivalent to RAM.
- Logical production/QA windows continue to overlap even when a single tablet must serialize some model calls through a shared inference slot.
- Never claim 17 models are simultaneously resident or 17 agents are simultaneously generating unless device telemetry proves it.

Model inventory and assignment configuration must be reconciled against the live `ollama list` output on the tablet before activation. Embedding-only models are not chat workers. Unverified or planned model tags must not be assigned as if installed.

## 5. Package and QA invariants

Every work package must carry a stable ID, version, owner, assigned QA supervisor, inputs and exact input versions, dependencies, deliverable paths, acceptance criteria, status, timestamps, review evidence, and handoff history.

- QA approval releases only the exact reviewed version.
- QA rejection returns the work to its originating specialist for correction.
- No self-approval and no review by the wrong QA supervisor.
- No downstream consumption of unapproved work.
- No silent overwrite of an approved package; publish a new version and assess downstream impact.
- Duplicate events must be idempotent.
- Queue and package state must survive process restarts.
- Unresolved QA, missing dependencies, model failures, or resource pressure must be visible as queued/blocked/escalated states, never silently dropped.

## 6. Repository and authority rules

- The shared Git branch is `main`; production agents work directly on that branch subject to repository safeguards.
- Agents must inspect current status and working-tree changes before editing, avoid overwriting another agent's work, and commit/push only their own scoped, reviewed changes.
- The repository is the durable source of truth for project decisions, role instructions, schemas, contracts, and handoffs.
- Chat messages are not the only record of a durable decision.
- The creator retains final authority over product vision, canon, visual direction, scope, and irreversible decisions.
- Never commit credentials, API keys, service-role keys, database passwords, or private player data.

## 7. Current implementation boundary

The repository contains a SQLite package relay, an on-demand serialized Ollama worker, a scheduler prototype, and tests. The current scheduler prototype's timed loop runs global production, QA, and correction phases in sequence. That is **not yet** the required per-agent overlapping-window scheduler described here. The scheduler remains unactivated until the rolling scheduler, resource controls, model assignments, and tests are implemented and verified on the tablet.

The live IntelliSync queue currently uses SQLite. Supabase persistence is not implemented. Do not apply the game database draft to a Supabase project until the dedicated Hustle City database is positively identified and the creator approves deployment.
