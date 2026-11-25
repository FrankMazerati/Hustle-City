# Hustle City — Super Agent Production & QA Cycle

**Status:** Canonical operating target; runtime automation pending  
**Production worker:** One Super Agent  
**Independent project lead / QA:** ChatGPT coordinating conversation  
**Default production block:** 30 minutes per bounded build package

## 1. What the 30-minute block means

Thirty minutes is the default focused production window for one bounded package or sub-package. It is not a promise that an entire memory department, large feature, or complex asset will be finished in 30 minutes. If work is not complete, the agent submits a truthful checkpoint and continues in another block. Never mark unfinished work complete to satisfy the clock.

Each package should have:
- Package ID, title, owning memory section and deliverable
- Creator-approved requirements and source records
- Scope boundaries and explicit exclusions
- Dependencies and files it may change
- Acceptance criteria and required evidence
- Expected output format and handoff location

## 2. Two-build overlap and correction handoff

The default cadence follows the Creator's requested two-build handoff:

| Window | Super Agent | ChatGPT Project Lead / QA |
|---|---|---|
| Block 1 — 0–30 min | Build Package A; save a versioned checkpoint and handoff manifest | Prepare review criteria from the task brief |
| Block 2 — 30–60 min | Start and build independent Package B; do not modify Package A's submitted files | Independently inspect Package A, compare it with requirements, record defects and questions |
| Handoff at ~60 min | Stop at a clean checkpoint for Package B | Return Package A's correction packet to the Super Agent |
| Block 3 — next 30 min | Correct Package A (or continue an explicitly prioritized correction package); do not overwrite Package B | Review Package B while correction work proceeds; verify Package A corrections when resubmitted |
| Following blocks | Continue the next independent package and resolve remaining corrections in priority order | Review each submitted package, track defects and approve only evidenced passes |

The Super Agent must not edit a package while ChatGPT is reviewing that same submitted version. Use immutable versioned submissions or separate working copies. A new version is submitted for each correction.

**Important:** ChatGPT's review is external to the local model call. The shared local host should still run only one local inference at a time unless a controlled capacity test proves more is safe. This workflow does not require two local models.

## 3. QA and correction handoff contract

Every submission includes:
1. Package ID and version
2. Files changed/created and exact repository or storage paths
3. Short summary of completed work
4. Requirements met and acceptance-criteria checklist
5. Tests/checks actually run, exact commands and results
6. Screenshots, logs, renders or other evidence where relevant
7. Known limitations, incomplete items and assumptions
8. Relevant memory records updated and cross-links
9. Dependencies and next recommended package

ChatGPT reviews:
- Requirement and creator-canon compliance
- Completeness and internal consistency
- Interfaces and cross-memory dependencies
- Asset provenance, format, scale and naming
- Technical plausibility and available test evidence
- Regression risks and acceptance criteria

ChatGPT returns a defect packet with severity, affected file/record, expected result, observed result, reproduction/evidence, precise correction request and retest criteria. The Super Agent applies corrections and submits a new version. ChatGPT verifies the new version against the original defect and relevant regression checks.

ChatGPT must not claim to have run a test, opened a binary asset, compiled the Unreal project or verified a local runtime unless the required artifact and test environment were actually available.

## 4. Package states

Use:
`queued → ready → in_progress → submitted → qa_review → changes_requested → correcting → resubmitted → accepted`

Other terminal/holding states:
- `blocked` — missing prerequisite, tool, asset or decision
- `partial` — useful work exists but acceptance criteria are not all met
- `rejected` — fundamentally invalid or outside approved direction
- `superseded` — replaced by a newer approved record/version

Only ChatGPT QA may mark a package accepted in the operating record, and acceptance requires evidence. Creator approval is still required for decisions reserved to the Creator.

## 5. Work selection and dependency safety

- Start the next package during QA only when it is independent of the unapproved output under review.
- Do not build downstream work on an unapproved upstream artifact as if it were final.
- Do not let the Super Agent and reviewer edit the same submitted version.
- Keep a single shared project history and task queue; avoid separate agent identities.
- Use small packages and explicit handoffs rather than trying to build an entire memory section at once.
- When a section is too broad, split it into sequential 30-minute packages.
- A correction block may be 15–30 minutes for small defects or multiple blocks for larger changes. Correctness takes priority over a fixed correction timer.

## 6. First production queue

The initial queue is proposed as the execution order under the approved direction to build Hustle City itself first:

1. `HC-000` — Read and consolidate creator-approved SCRIBE & LENS creative direction; opening train-arrival cinematic, camera, weather, time, lighting, atmosphere and sound requirements.
2. `HC-001` — Hustle City master plan: city scale/orientation, boundaries, waterfront, districts and major landmarks. No detailed building production.
3. `HC-002` — Major and short expressways, interchanges, ramps, bridges, tunnels and connections.
4. `HC-003` — Street network, street names/numbering, intersections, sidewalks, markings and permanent street-name registry.
5. `HC-004` — HIM train, city train, subway, rail corridors, stations, platforms, transfers and yards. Keep the meaning of HIM unresolved until Creator clarifies it.
6. `HC-005` — Marina/waterfront, docks, slips, navigation access and supporting circulation.
7. `HC-006` — Neighborhood and district layout, boundaries and connections.
8. `HC-007` — Building plots, footprints, parking, public space and service access.
9. Begin detailed building, venue, transit-interior, people, vehicle, social/lifestyle and gameplay packages in dependency order.

The train station, train route and camera staging for the opening cinematic must be reserved early. Do not build the entire surrounding world before Hustle City itself.

## 7. First-night startup gate

Before the first real production block:
- Confirm the active branch is `knowledge-library-foundation` and work remains inside PR #11; never merge to `main`.
- Confirm the actual model tag exists on the chosen host and completes one bounded inference. Do not infer availability from an old download report.
- Confirm available RAM/storage and that the chosen model fits; external storage does not remove model RAM requirements.
- Confirm project memory and asset paths are readable and writable, with a backup.
- Confirm the Super Agent prompt, nine-section memory index, package template and handoff manifest are accessible.
- Run a small dry-run package and validate output, versioning, memory write-back and QA return path.
- Keep the scheduler disabled until the runtime implements this operating model and its tests pass.

If the runtime is not yet ready, the Creator and ChatGPT can still prepare/QA the first package and run the Super Agent manually through the verified model interface; do not describe this as autonomous scheduling.


## 8. Revised continuous-production review policy (Creator direction, 2026-11-25)

The default is **keep the Super Agent producing while review happens**. ChatGPT should not interrupt the worker for every small defect or automatically send every issue back immediately.

### Normal flow

1. Super Agent builds Package A for a 30-minute block and submits an immutable checkpoint.
2. Super Agent starts Package B for another 30-minute block when B is independent and safe to build.
3. While B is underway, ChatGPT inspects A and records findings.
4. The Creator may inspect the submitted work and provide small changes or preferences. ChatGPT records these as creator feedback and routes each change to the safest owner.
5. ChatGPT handles a minor, isolated correction directly when it has the necessary file access, the change is unambiguous, low-risk, and does not require the Super Agent's specialist tools or local environment. Examples: a small documentation correction, metadata/label adjustment, typo, or straightforward isolated text/config edit.
6. If the change requires production tools, domain-specific implementation, asset editing, code execution, model inference, or risks breaking linked systems, ChatGPT records it as a correction task for the Super Agent. The worker may finish its current block/package before taking it.
7. The agent continues with subsequent packages while the correction queue remains small and safe. Corrections must be versioned; never mutate a submitted artifact that is actively being reviewed.

### Correction severity and ownership

- **Minor / ChatGPT may fix:** isolated, unambiguous, low-risk, easily verified changes with available access. Record before/after, file/record, reason and verification.
- **Moderate / Super Agent queue:** implementation changes, asset changes, nontrivial code, multi-file edits, domain-specific changes, or anything needing the agent's build environment. Add a precise ticket and let the agent finish its current safe work before returning to it.
- **Major / pause and group meeting:** stop starting new packages and convene the Creator, ChatGPT and Super Agent for a shared decision when the core direction or architecture is wrong, a critical dependency is broken, the same class of defect recurs after correction, multiple domains are affected, a safety/data-loss/security risk appears, or the defect backlog is growing faster than it can be resolved. A practical trigger is 3 or more related moderate/high-severity defects in one package or repeated recurrence of the same major issue. This is a trigger for discussion, not an automatic blame or rejection.

### Creator review loop

The Creator can review outputs at convenient checkpoints and say things such as "change this to that" or "move this there." ChatGPT records the exact requested change, checks whether it is a small safe edit or needs the Super Agent, and updates the task/QA record. Creator direction takes precedence over inferred preferences. Do not stop the agent for a minor preference change unless it affects work currently being edited or invalidates a dependency.

### Queue discipline

Maintain three visible queues in Master Project:
- **Agent production queue:** next packages the Super Agent should build.
- **Correction queue:** moderate issues the Super Agent must address, prioritized by severity and dependencies.
- **ChatGPT minor-fix log:** small changes made directly, with file/record, before/after and verification.

At each checkpoint, summarize: what the agent built, what ChatGPT inspected, what minor changes were made, what corrections are queued, what the Creator wants changed, and whether production should continue or pause for a meeting.

The 30-minute block remains a default checkpoint, not a hard completion deadline. ChatGPT should not make broad or speculative changes on the agent's behalf. Independent review remains independent even when ChatGPT makes a small correction.
