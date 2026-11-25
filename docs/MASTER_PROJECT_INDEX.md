# Hustle City — Master Project Index

**Status:** Initial canonical index scaffold; populate from verified repository/project records  
**Project workforce:** One Hustle City Super Agent; ChatGPT is external Project Lead and independent QA  
**Creator authority:** Final authority on approved vision, scope and reserved decisions  
**Runtime:** Not active until the startup/activation gate passes

## Canonical operating documents

- [Super Agent Startup Guide](../agents/SUPER_AGENT_STARTUP_GUIDE.md)
- [Super Agent Charter](../agents/SUPER_AGENT_CHARTER.md)
- [Super Agent System Prompt](../agents/SUPER_AGENT_SYSTEM_PROMPT.md)
- [Memory Architecture](../agents/SUPER_AGENT_MEMORY_ARCHITECTURE.md)
- [Production and QA Cycle](../agents/SUPER_AGENT_PRODUCTION_CYCLE.md)
- [Batch Roadmap](../agents/SUPER_AGENT_BATCH_ROADMAP.md)
- [Package Handoff Template](../agents/templates/SUPER_AGENT_PACKAGE_HANDOFF_TEMPLATE.md)
- [Package Manifest Schema](../agents/schemas/super-agent-package-manifest.schema.json)
- Runtime target config: `intellisync/config/super_agent.json`

## Nine memory sections

| Section | ID | Current role |
|---|---|---|
| MASTER PROJECT | HC-MEM-01 | This index, decisions, project state, priorities, dependencies and queues |
| SCRIBE & LENS | HC-MEM-02 | Narrative, cinematics, camera, weather, climate, seasons, time, lighting, atmosphere, audio and player experience |
| WORLD | HC-MEM-03 | City geography, districts, streets, expressways, transit corridors, waterfront, plots, buildings and interiors |
| PEOPLE | HC-MEM-04 | Character identity, personality, behavior, routines, animation and individual Sim encounter memories |
| TRANSPORTATION | HC-MEM-05 | Vehicles, trains, subway, aircraft, boats, routes, stations, airport, marina and operations |
| SYSTEMS | HC-MEM-06 | Controls, gameplay, traffic, physics, weather implementation, economy, persistence and integration |
| QUALITY | HC-MEM-07 | Acceptance criteria, test plans, QA evidence, defects, corrections and approvals |
| ASSET LIBRARY | HC-MEM-08 | Original downloads/photos/videos, provenance, licenses and processed asset records |
| SOCIAL & LIFESTYLE | HC-MEM-09 | Clothing, wardrobes, relationships, communications, events, invitations, notifications and daily activities |

## Current operating decisions

- One production worker identity and one primary model at a time on the constrained local host.
- SCRIBE and LENS responsibilities are combined within the Super Agent; they are not separate agents.
- No separate local QA agents or Trinity model.
- ChatGPT reviews submitted immutable package versions while the Super Agent continues safe production.
- ChatGPT may fix only minor, isolated, unambiguous, low-risk items with access and verification; moderate/specialist corrections go to the Super Agent queue.
- Major/repeating/cross-domain/safety/data-loss issues trigger a Creator + ChatGPT + Super Agent review.
- Default 30-minute work blocks are checkpoints, not completion deadlines.
- Scheduler remains disabled until target-host inference, memory retrieval/write-back and end-to-end package workflow are tested.
- No paid fallback, spending or merge to `main` without explicit Creator approval.

## Immediate execution mode

- **Available now:** chat-assisted Batch 1 documentation and creative production; repository commits on the foundation branch; Creator review.
- **Not yet available/verified:** local autonomous Super Agent, background scheduling, local model inference, external-drive asset processing or independent QA of ChatGPT-authored outputs.
- **No Termux/UserLAnd/external-drive setup is required for the first creative and planning packages.** Do not block Batch 1 on local runtime readiness.

## Current batch status

| Batch | Name | Status | Exit gate |
|---|---|---|---|
| HC-B00 | Agent readiness and project intake | not verified / pending evidence | Actual host model inference, storage/backup, selective memory and handoff dry-run |
| HC-B01 | Creative and cinematic foundation | queued | Creator-approved creative brief and opening train-arrival cinematic requirements |
| HC-B02 | Hustle City master plan | queued | Creator-approved city footprint, orientation and spatial registry |
| HC-B03 | Expressway network | queued | Network fits approved master plan |
| HC-B04 | Street network and public realm | queued | Street/intersection registry and connectivity reviewed |
| HC-B05 | Rail, train and subway network | queued | Corridors/stations fit city plan; HIM acronym remains unresolved |
| HC-B06 | Marina and waterfront access | queued | Marina/access fits city and transport plan |
| HC-B07 | Districts and neighborhoods | queued | Boundaries/names trace to approved decisions |
| HC-B08 | Building plots and development framework | queued | Stable plots, envelopes and access requirements |
| HC-B09 | Building kits, landmarks and venues | queued | Detailed assets fit approved plots and pass provenance/QA |
| HC-B10 | People and character foundation | queued | Identity/rig/behavior/memory standards reviewed |
| HC-B11 | Transportation assets and operations | queued | Assets and operating contracts reviewed |
| HC-B12 | Social and lifestyle | queued | Social systems cross-link People, assets and runtime |
| HC-B13 | Core gameplay and simulation systems | queued | Functional contracts and tests pass |
| HC-B14 | Integration and playable vertical slice | queued | Creator-inspectable end-to-end slice |
| HC-B15+ | Expansion waves | future | Creator-prioritized expansion plan |

## Three live queues

### Agent production queue
1. HC-B00-P01 — Confirm current canonical startup documents and branch/PR state; record only verified facts.
2. HC-B00-P02 — Verify memory/asset roots and backup on the target host (only if not already supported by current evidence).
3. HC-B00-P03 — Verify actual model tag and bounded inference on the target host (only if not already supported by current evidence).
4. HC-B00-P04 — Run selective-memory and package/handoff/correction dry run.
5. HC-B01-P01 — Consolidate approved SCRIBE & LENS direction.

### Super Agent correction queue
- No active correction tickets registered in this index. Add only evidenced defects with severity, affected record, expected/observed result, owner and retest criteria.

### ChatGPT minor-fix log
- No new minor fixes recorded by this index commit. Record any later direct fix with exact before/after and verification.

## Current verification and blockers

- Repository documentation/configuration has been updated on `knowledge-library-foundation` under PR #11.
- The target-host model tag, bounded inference, runtime support, memory storage paths and end-to-end workflow have **not** been verified by this repository update.
- The configured `qwen2.5-coder:1.5b` remains a candidate only, not a verified active model.
- IntelliSync scheduler remains disabled.
- No claim is made that the Super Agent is currently running autonomously.

## Update rules

After each package checkpoint, update:
1. Batch/package status and exact artifact references.
2. Production queue, correction queue and ChatGPT minor-fix log.
3. Relevant memory records and cross-links.
4. QUALITY findings and evidence.
5. Dependencies, blockers and Creator decisions.
6. Next safe package and batch exit gate.

Preserve historical versions. Do not silently convert proposals into approved decisions.
