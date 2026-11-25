# Hustle City Super Agent — Startup and First-Run Guide

**Canonical entry point:** This guide  
**Worker:** One Hustle City Super Agent identity / one configured primary model  
**Project Lead and independent QA:** ChatGPT coordinating conversation  
**Final authority:** Creator  
**Current runtime status:** Disabled pending target-host and workflow verification

## 1. What starts the worker

The Super Agent is not activated merely by adding a prompt or model name to the repository. A working start requires:
- A verified model tag and a successful bounded inference on the actual host.
- A runtime/launcher that loads the system prompt and project configuration.
- Readable/writable project memory and asset roots, with backup.
- Selective memory retrieval and write-back.
- Persistent package/checkpoint records.
- A handoff path that lets ChatGPT inspect submitted outputs and return findings.
- A tested correction/version path.

Until these are verified, run packages manually through the verified model interface. Do not enable the scheduler or claim autonomous operation.

## 2. Startup sequence

1. Confirm repository branch `knowledge-library-foundation` and PR #11. Keep changes in that PR; do not merge to `main`.
2. Read, in order:
   - `agents/SUPER_AGENT_CHARTER.md`
   - `agents/SUPER_AGENT_SYSTEM_PROMPT.md`
   - `agents/SUPER_AGENT_MEMORY_ARCHITECTURE.md`
   - `agents/SUPER_AGENT_PRODUCTION_CYCLE.md`
   - `agents/SUPER_AGENT_BATCH_ROADMAP.md`
   - `intellisync/config/super_agent.json`
3. Read the Master Project index and current queue.
4. Verify the actual active model tag on the host and run one small inference. Record exact model tag, host, available memory, inference result and date. Do not use an unverified candidate.
5. Verify memory root, asset root and backup location are readable/writable. Keep original asset files immutable.
6. Load only the records needed for Batch 0 / the active package. Do not load all nine memory archives into every prompt.
7. Run the package dry-run and test checkpoint → handoff → QA return → correction version → memory write-back.
8. Keep scheduler disabled until all activation requirements in the config pass.

## 3. First work to execute

Use the batch roadmap:
- Batch 0 is readiness and dry-run. Do not repeat checks already evidenced as passed; inspect the current verification record and perform only missing or stale checks.
- Batch 1 is the first actual game-production batch: creative direction and opening train-arrival cinematic.
- Batch 2 is the Hustle City master plan.
- Then proceed through expressways, streets, transit, waterfront, districts and building plots.

Do not start detailed building production before the relevant plot and city constraints are approved. Do not build the entire outer world first.

## 4. How a batch runs

A batch is a group of packages. A package is the smallest reviewable unit.

For each package:
1. Read Master Project first, then relevant memory sections and linked records.
2. Write a compact work brief: objective, approved requirements, scope, exclusions, dependencies, open decisions and acceptance criteria.
3. Produce for a default 30-minute block. If unfinished, checkpoint partial progress; continue in another block.
4. Save an immutable version and complete the handoff template.
5. Start the next independent safe package if available. Never rely on unapproved upstream work as final.
6. ChatGPT reviews the submitted package while the Super Agent continues safe production.
7. Route defects by severity:
   - Minor: ChatGPT may fix if isolated, clear, low-risk and verifiable; log it.
   - Moderate/specialist: add a correction ticket for the Super Agent; the worker can finish its current safe block first.
   - Major/recurring/cross-domain/safety/data-loss: stop starting new packages and hold a Creator + ChatGPT + Super Agent review.
8. Correct in a new version. Re-run relevant checks and hand off for independent verification.
9. Update owning memory records, QUALITY, Master Project index and all three queues.

## 5. Required checkpoint and handoff

Use `agents/templates/SUPER_AGENT_PACKAGE_HANDOFF_TEMPLATE.md`. Never submit only a conversational summary. Include exact paths, versions, requirements checklist, test commands/results, screenshots/logs where relevant, incomplete work, risks, memory write-back and next dependencies.

## 6. Three queues

Master Project must always show:
- **Production queue:** packages the Super Agent should build.
- **Correction queue:** moderate/specialist issues assigned back to the Super Agent.
- **ChatGPT minor-fix log:** small direct fixes with before/after and verification.

## 7. Stop conditions

Stop starting new packages and call a group review when:
- Core direction or architecture is wrong.
- A critical dependency is broken.
- The same major defect recurs after correction.
- Multiple domains are affected.
- A safety, security or data-loss risk appears.
- Three or more related moderate/high-severity defects accumulate in one package, or the correction backlog grows faster than it can be resolved.

Do not stop for every small preference or typo. Do not conceal defects to protect the schedule.

## 8. Activation checklist

- [ ] Correct branch and PR confirmed
- [ ] Canonical prompt/charter/config loaded
- [ ] Master Project index loaded
- [ ] Model tag verified on target host
- [ ] Bounded inference passed
- [ ] Memory and asset paths read/write verified
- [ ] Backup verified
- [ ] Selective retrieval/write-back dry run passed
- [ ] Versioned package/handoff dry run passed
- [ ] QA return and correction version tested
- [ ] Required tests passed
- [ ] Creator informed of any remaining limitations

Only after all required checks pass may runtime activation be considered. Creator approval is still required for any paid service, spending or merge to main.
