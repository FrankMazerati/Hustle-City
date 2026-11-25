> **CURRENT CANON — 2026-11-25:** The creator has replaced the prior multi-agent target with one Super Agent production worker and ChatGPT as external Project Lead/independent QA. The nine-section selective memory architecture and 30-minute two-build review/correction cycle are documented in `agents/SUPER_AGENT_*.md` and `intellisync/config/super_agent.json`. That config is a design target, not proof of runtime support. Existing multi-agent code/configuration is legacy; scheduler remains disabled. Model candidate, target-host inference, memory retrieval/write-back, versioned two-build handoff, and end-to-end tests remain unverified or unimplemented.

# IntelliSync implementation status

> **Current roster correction (2026-11-24):** The existing IntelliSync configuration and implementation notes describe an older 12-specialist + 3-QA setup. The current creator-approved target is 17 local roles (SCRIBE, LENS, QA-1–QA-3, P01–P12), with ChatGPT as the external coordinator. The 17-role roster has not yet been reconciled into runtime configuration. The scheduler remains disabled; do not treat old assignments as proof of current model availability or live agents.


## Consolidated foundation

- [x] PR #8 Unreal Engine 5 foundation work incorporated into canonical PR #11.
- [x] PR #10 IntelliSync runtime and hosted-provider work incorporated into canonical PR #11.
- [x] Both original branch heads preserved as additional parents in the consolidation commit.
- [x] No changes merged into `main`.

## Implemented

- [x] SQLite persistence for packages, station runs and event records.
- [x] Configurable station pipeline, station claims and deliverable submission.
- [x] Explicit QA assignment validation in the current single-stage scheduler.
- [x] Independent QA approval/rejection gate and correction loop.
- [x] Next-station release only after approval.
- [x] Duplicate event-key protection and restart recovery.
- [x] Trinity coordinator snapshot, QA oversight messages and escalation service.
- [x] Cross-agent message feed persistence.
- [x] Bounded scheduler and local Ollama chat adapter.
- [x] Gemini native API adapter and OpenRouter chat-completions adapter.
- [x] Environment-only API key access and fail-closed free-only provider eligibility.
- [x] Approved 12-specialist target roster and explicit local model assignments.
- [x] Three QA supervisor role descriptions and four-specialist oversight scopes.
- [x] Four department definitions, cross-department communication policy and Active Directory-style RBAC policy specification.
- [x] Three-stage QA workflow specified in configuration and documentation.

## Not yet verified or activated

- [ ] Current device confirms all 15 configured model tags exist and can complete bounded inference.
- [ ] Group-aware task fan-out implemented; current scheduler executes one configured station agent, not all members of a department.
- [ ] Application-level access-control policy enforced by the runtime message hub and tool layer.
- [ ] QA-1 intake → QA-2 triage/routing → production → QA-3 independent verification implemented in executable runtime code.
- [ ] QA-3 rework routing to production and QA-1 reassessment implemented and tested.
- [ ] Correct QA stages mapped into scheduler without weakening the independent-review gate.
- [ ] Continuous local worker service with health checks, heartbeat, graceful stop, resource monitoring and restart tested.
- [ ] End-to-end agent collaboration and permission tests pass.
- [ ] Exact Gemini/OpenRouter model IDs, free quotas and data terms verified; both providers remain disabled.
- [ ] Long-running hosted worker, persistent hosted database, Supabase adapter and 24/7 monitoring.
- [ ] Unreal project compiled and validated in Unreal Editor on a supported production computer.

The 12 specialists and three QA supervisors have model assignments in configuration, but these are not live agent instances. The scheduler remains disabled. Do not mark the workforce online until all activation gates above that apply to the chosen host have passed.
