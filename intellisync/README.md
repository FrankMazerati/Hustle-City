# Hustle City IntelliSync Runtime

IntelliSync is the durable package relay and worker execution layer for Hustle City. This runtime is separate from the older six-role manual GitHub pilot.

## Implemented

- SQLite persistence for work packages, station runs, events and agent messages.
- Station-to-station package relay with QA approval before downstream release.
- Rework loops that return rejected work to its original station.
- Restart recovery and bounded worker scheduling.
- Trinity coordinator snapshot, QA oversight record and escalation message services.
- Hosted model adapters for Google Gemini and OpenRouter.
- API keys read from environment variables only; no credentials are stored in the repository.
- Fail-closed provider eligibility: a hosted provider is callable only when enabled, verified as free, quota is available, data terms are approved, and its key/model are present.
- Quota/rate-limit fallback is limited to the next explicitly verified-free provider. If no free provider is available, work remains queued; paid fallback is prohibited.

## Gemini and OpenRouter connection

The GitHub Actions worker entrypoint supplies these existing repository secrets to the runtime:

- `GEMINI_API_KEY`
- `OPENROUTER_API_KEY`

Set model IDs as GitHub Actions repository variables (not secrets):

- `GEMINI_MODEL`
- `OPENROUTER_MODEL`

The provider definitions live in `config/agents.json`. Both providers are intentionally disabled until their current API pricing/free quota and data terms have been checked. Do not set `enabled`, `verified_free`, `quota_available`, or `data_terms_approved` to true without verifying each condition for the exact model. API keys by themselves do not prove an API call is free.

The manually dispatched `.github/workflows/intellisync-hosted-worker.yml` is gated by both the input `confirm_run=RUN` and repository variable `INTELLISYNC_ENABLE_HOSTED_WORKERS=true`. It processes one bounded queue cycle, not an overnight or continuous run. It is not dispatched automatically.

## Current activation blockers

- The starter geography pipeline still has no approved QA supervisor IDs. The scheduler refuses to start until each station has an explicit QA owner.
- The final specialist-to-QA ownership map has not yet been supplied.
- Provider model IDs, free quota and data terms still require explicit verification and configuration.
- No unattended overnight worker or 24/7 host is active.

The starter geography pipeline is World Builder → City Builder → Roads & Infrastructure → Building & Architecture. Functional role IDs are not approved permanent specialist names. SCRIBE and LENS remain separate creative leads and are not forced into this geography pipeline.

## Tests

```bash
python -m unittest discover -s intellisync/tests -v
```

## Safety

- Keep API keys in GitHub Secrets or another secret manager; never commit them.
- Do not infer QA assignments or final roster names.
- Do not connect or mutate a Supabase project until the dedicated IntelliSync database is confirmed.
- Do not merge or deploy generated work without review.
