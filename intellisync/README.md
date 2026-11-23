# Hustle City IntelliSync Runtime

IntelliSync is the durable work-package relay, agent execution and coordination foundation for Hustle City.

## Workforce configuration

The canonical 12-specialist roster is in [agents/hustle-city-core-roster.json](../agents/hustle-city-core-roster.json). Department collaboration, QA roles and continuous-worker behavior are documented in [agents/WORKFORCE_OPERATING_MODEL.md](../agents/WORKFORCE_OPERATING_MODEL.md). Active Directory-style application groups and permissions are specified in [agents/ACCESS_CONTROL_POLICY.json](../agents/ACCESS_CONTROL_POLICY.json).

Local Ollama is the configured default backend. Explicit model assignments for the 12 specialists and three QA supervisors are in `config/agents.json`. The shared mobile host is configured for one active model call at a time. Assignments do not prove that the model tags exist on the current device or that agents are running; the activation checklist requires a live inventory check and one bounded inference per assigned model.

## Implemented runtime capabilities

- SQLite persistence for packages, station runs, events and agent messages.
- Configurable station pipeline, station claims and deliverable submission.
- Independent QA review gate, correction loop and next-station release.
- Duplicate-event protection and restart recovery.
- Trinity status snapshot, QA oversight record and escalation services.
- Bounded scheduler and Ollama chat adapter.
- Gemini and OpenRouter adapters with environment-only credentials and fail-closed free-only eligibility gates.

## Not yet implemented or activated

- Group-aware task fan-out so all members of a department can be selected for work.
- Runtime enforcement of the application-level group/permission policy.
- The complete QA-1 intake → QA-2 routing → production correction → QA-3 independent verification workflow, including QA-3 returns to production or QA-1 reassessment.
- A verified local model inventory and inference test for every assignment on the target device.
- A continuous local service with heartbeat, graceful shutdown, resource-pressure handling and operational monitoring.
- A persistent hosted worker, 24/7 hosting or Supabase persistence.

For those reasons, `scheduler.enabled` remains false and production stations do not yet have a legacy single-stage QA owner configured. The scheduler must not be started until the missing workflow and group execution support are implemented and tested. The current one-cycle GitHub Actions workflow is manually gated and is not a continuous worker.

## Hosted providers

Gemini and OpenRouter remain disabled by default. They may be enabled only after the exact model's current zero-cost quota and data terms are verified. API keys belong in GitHub Secrets; model IDs belong in repository variables. If no verified free provider is available, work remains queued. Paid fallback is prohibited.

## Tests

```bash
python -m unittest discover -s intellisync/tests -v
```

## Safety and authority

- QA may not approve its own work.
- Low-confidence or malformed QA results remain pending for human review.
- Trinity coordinates and audits; it does not silently alter creator-approved canon.
- Agents may communicate across departments, but tool and write permissions remain least-privilege.
- No agent writes to `main`, merges pull requests, changes roster membership or spends money without explicit creator authorization.
- Do not connect or mutate Supabase until the dedicated IntelliSync database is confirmed.
