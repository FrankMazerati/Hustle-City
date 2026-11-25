# Hustle City — Super Agent Production & QA Cycle

**Status:** Canonical operating target; runtime automation pending  
**Production worker:** One Super Agent  
**Independent Project Lead / QA:** ChatGPT coordinating conversation  
**Final authority:** Creator  
**Default production checkpoint:** 30 minutes

## 1. Work hierarchy

- **Batch:** a coordinated phase of related packages with dependencies and an exit gate. See `agents/SUPER_AGENT_BATCH_ROADMAP.md`.
- **Package:** the smallest independently reviewable unit of production.
- **Work block:** a default 30-minute focused period. A package may take multiple blocks; 30 minutes is not a forced completion deadline.
- **Checkpoint:** an immutable, versioned submission with a completed handoff manifest.
- **Correction:** a new version or follow-up package; never overwrite a submitted version under active review.

The first active game-production batch is Batch 1 (creative/cinematic foundation). Batch 0 is readiness only and should not repeat checks already verified with current evidence.

## 2. Continuous production with overlapping review

The Creator's latest direction is to keep the Super Agent producing while ChatGPT reviews and fixes small issues. The two-build overlap is the default pattern, not a rigid stop/start loop.

| Window | Super Agent | ChatGPT Project Lead / QA |
|---|---|---|
| Block A | Build Package A; save immutable versioned checkpoint and manifest | Prepare review criteria from approved requirements |
| Block B | Start independent Package B if safe; do not modify submitted A | Independently inspect A, record defects/questions, make only eligible minor fixes |
| Checkpoint B | Submit B; continue another independent safe package when available | Return A findings and Creator feedback; route corrections by severity |
| Ongoing production | Continue production unless a major stop condition applies; take moderate corrections at a safe checkpoint | Review submitted packages, verify resubmissions, maintain queues and Master Project status |
| Correction handoff | Apply moderate/specialist corrections in a new version at a prioritized checkpoint | Recheck against original defect and regression criteria |

The worker does not need to stop for every small issue. A moderate correction may wait until the current safe package is checkpointed. If a correction invalidates the current work or a dependency, stop that affected work only.

ChatGPT review is external to the local model call. The constrained local host runs one local inference at a time unless a controlled capacity test proves a higher limit is safe.

## 3. Correction ownership

### Minor — ChatGPT may fix directly
Only when all are true:
- The issue is isolated, unambiguous and low-risk.
- ChatGPT has access to the exact file/record.
- The change does not require specialist production tools, local execution, asset editing or model inference.
- The change can be checked after editing.

Examples: typo, small documentation correction, metadata/label adjustment, isolated text/config correction.

Log each fix with package/version, file/record, before/after, reason and verification. This is a minor fix, not a substitute for independent QA.

### Moderate — Super Agent correction queue
Use for nontrivial implementation, technical/code changes, asset work, multi-file changes, domain-specific production or anything requiring the worker's environment/tools. Write a precise correction ticket with severity, expected/observed behavior, evidence, affected records and retest criteria. The worker may finish its current safe package before taking it.

### Major — group review
Stop starting new packages and hold a Creator + ChatGPT + Super Agent review when:
- Core direction or architecture is wrong.
- A critical dependency is broken.
- The same major defect recurs after correction.
- Multiple domains are affected.
- A safety, security or data-loss risk appears.
- Three or more related moderate/high-severity defects accumulate in one package, or the correction backlog grows faster than it can be resolved.

This is a governance trigger, not an automatic blame or rejection. Do not hide defects to protect the schedule.

## 4. Immutable versioning and handoff contract

Every package submission includes:
1. Batch ID, package ID, title, version and memory owner(s).
2. Exact files/records created or changed and paths.
3. Summary of completed and incomplete work.
4. Creator-approved requirements and acceptance checklist.
5. Dependencies, exclusions, assumptions and unresolved decisions.
6. Commands/checks actually run and exact results; checks not run and why.
7. Screenshots, logs, renders or other evidence where relevant.
8. Relevant memory records updated and cross-links.
9. Next safe package and why it is independent.
10. QA focus and retest criteria.

Use `agents/templates/SUPER_AGENT_PACKAGE_HANDOFF_TEMPLATE.md` and validate the manifest against `agents/schemas/super-agent-package-manifest.schema.json`.

A submitted version is immutable during QA. Corrections increment the version and include a change history. Do not treat unapproved upstream output as final or build dependent work on it.

## 5. QA states and acceptance

Recommended states:
`queued → ready → in_progress → partial/submitted → in_review → correction_required → correcting → resubmitted → accepted`

Other states:
- `blocked` — missing prerequisite, tool, asset or decision.
- `rejected` — fundamentally invalid or outside approved direction.
- `superseded` — replaced by a newer approved record/version.

Only ChatGPT's independent QA record may mark a package accepted, and acceptance requires evidence. Creator approval remains necessary for Creator-reserved decisions and batch gates.

ChatGPT reviews:
- Creator-canon and requirement compliance.
- Completeness, internal consistency and acceptance criteria.
- Interfaces, spatial consistency and cross-memory dependencies.
- Asset provenance, naming, scale and formats.
- Technical plausibility and actual test evidence.
- Regression risks and unresolved assumptions.

ChatGPT returns a defect packet containing severity, affected file/record, expected result, observed result, reproduction/evidence, exact correction request and retest criteria.

ChatGPT must not claim a test, Unreal build, binary asset inspection, local runtime verification or deployment unless it actually had the artifact and environment to perform it.

## 6. Batch sequencing and first production queue

Use `agents/SUPER_AGENT_BATCH_ROADMAP.md` as the canonical phase plan. It defines package groups, outputs, dependencies, memory ownership and exit gates.

Initial sequence:
- **Batch 0:** Agent readiness, repository/memory/asset access, model verification and end-to-end dry run. Perform only missing/stale checks.
- **Batch 1:** Creator-approved SCRIBE & LENS creative direction, opening train-arrival cinematic, camera, weather, time, lighting, atmosphere and sound.
- **Batch 2:** Hustle City master plan, geography, scale/orientation, boundaries, landmarks and spatial registry.
- **Batch 3:** Major/short expressways, interchanges, ramps, bridges and tunnels.
- **Batch 4:** Street network, permanent street-name registry, intersections, sidewalks and crossings.
- **Batch 5:** HIM train, city train, subway, corridors, stations, platforms, transfers and yards.
- **Batch 6:** Marina, waterfront, docks, slips, navigation and circulation.
- **Batch 7:** Districts, neighborhoods, boundaries and connections.
- **Batch 8:** Building plots, footprints, envelopes, parking and access.
- **Batch 9 onward:** Detailed buildings/venues, people, transportation assets, social/lifestyle, gameplay/systems and a playable vertical slice in dependency order.

Build Hustle City itself first. Do not build the entire surrounding world as a prerequisite. Preserve the name HIM; do not invent an acronym expansion. Reserve the opening cinematic station, route and camera staging early.

## 7. Memory and queue maintenance

After every package checkpoint:
- Update the owning memory section(s) and linked records.
- Add QA findings and evidence to QUALITY.
- Update the Master Project index and current batch/package state.
- Preserve source assets and prior package versions.
- Update three separate queues:
  1. **Agent production queue** — next safe packages.
  2. **Super Agent correction queue** — moderate/specialist corrections.
  3. **ChatGPT minor-fix log** — small direct fixes with before/after and verification.

At each checkpoint report what was built, what ChatGPT inspected, minor fixes, queued corrections, Creator feedback, blockers and whether production should continue or a group review is needed.

## 8. Startup and runtime gate

Use `agents/SUPER_AGENT_STARTUP_GUIDE.md`. Before autonomous activation:
- Confirm branch `knowledge-library-foundation` and PR #11; do not merge to `main`.
- Verify the actual model tag on the target host and complete one bounded inference.
- Verify memory/asset paths are readable and writable and a backup exists.
- Test selective retrieval and memory write-back.
- Test immutable package checkpointing, handoff, QA return and correction versioning.
- Verify required runtime tests pass.

The current config intentionally keeps the scheduler disabled. If the runtime is not ready, prepare and review Batch 1 manually through a verified model interface; do not describe that as autonomous scheduling. External storage does not remove model RAM requirements.

## 9. Resource, authority and integrity rules

- One Super Agent identity and one local model inference at a time by default.
- No separate local QA agents, separate SCRIBE/LENS agents or Trinity model.
- No paid fallback, paid service activation or spending without explicit Creator approval.
- No merge to `main` without explicit Creator approval.
- Creator-approved requirements are mandatory; proposed/unresolved details remain visibly unapproved.
- Never invent model availability, files, asset counts, measurements, tests, builds or successful integrations.
- If blocked, state the exact blocker and propose a materially different next step. Do not repeat diagnostics already completed without a new reason.
