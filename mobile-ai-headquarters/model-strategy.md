# Model Strategy: strongest capability, maximum throughput, free-first

Status: active policy baseline; **100% free initial budget**. No paid API calls are permitted. Provider credentials and production models are not configured.

## Objective

Maximize useful Hustle City work per dollar while preserving output quality. Select models by measured task performance, not brand popularity or a fixed one-model-per-agent arrangement. Keep the twelve specialist identities and four logical engine groups, but route individual tasks through a shared model pool.

## Operating tiers

### Tier A — Frontier / hardest tasks (DISABLED under initial budget)
No paid frontier endpoint may be called under the current policy. When a task needs frontier capability, Trinity must queue it for creator review or perform a bounded best-effort attempt with an explicitly approved free endpoint. Do not silently downgrade a high-risk task.

Use the strongest model that is available and approved for:
- Trinity's difficult coordination and conflict resolution;
- architecture decisions and cross-system dependency analysis;
- complex Godot engineering, debugging and code review;
- security-sensitive design and difficult QA investigations.

This tier is disabled until the creator changes the budget policy in a future explicit decision. No paid candidate is configured.

### Tier B — Verified free hosted throughput
Use only a provider/model endpoint whose API free tier, current quota, data terms, model ID and tool compatibility have been checked. The router must require an explicit `verified_free` flag and a zero-cost policy classification. If no suitable verified endpoint is configured or its quota is exhausted, queue the task. Never treat a low-cost paid API as free.

Free chat access in an app does not imply free API access. Do not assume a user's Copilot, Gemini, Manus or DeepSeek app subscription/plan includes API credits.

### Tier C — Local / offline fallback
Use local models for private drafts, classification, simple extraction, prompt formatting, small summaries and offline assistance. Local inference has no per-token provider charge, but uses device memory, battery, storage and processing time.

On the Galaxy A17 configuration reported for this project (4 GB RAM), start with a small quantized GGUF model around 1B–2B parameters, only if the runtime reports it fits. Test a 3B-class model only if memory headroom and stability allow. Close other apps during tests. Do not expect phone-local models to match frontier reasoning or handle the full project context.

PocketPal supports on-device GGUF models on Android. Use it for local experiments and fallback, not as the central always-on agent server. The 1 TB USB drive increases storage capacity, not RAM or compute power.

## Routing rules

1. Classify each task by difficulty, risk, required context, tool use, vision, coding and privacy.
2. Use Tier C first only for low-risk tasks where a small local model is sufficient.
3. Use Tier B for ordinary production tasks when a suitable free quota is available.
4. Escalate to Tier A for complex/high-impact work, repeated failures, ambiguous architecture, cross-domain integration or independent final review.
5. If a free quota is exhausted, queue the task. There is no paid fallback under the initial budget.
6. Keep an independent QA pass for consequential outputs. A model must not approve its own high-impact work.
7. Cache shared project context where supported, deduplicate repeated requests, batch suitable background jobs and cap retries.
8. Preserve a human approval gate before merge, deployment, spending, account changes or external publication.

## Benchmark before selection

Run the same representative tasks against each candidate:
- understand the existing Hustle City architecture without contradicting its decision log;
- design a compatible feature contract across city, Sims/NPC, vehicles and transportation systems;
- implement a small Godot 4 change with tests;
- diagnose a deliberately seeded bug;
- produce valid JSON matching a supplied schema;
- identify uncertainty and refuse to invent missing project facts.

Score each run on correctness, completeness, repository consistency, tool-call reliability, latency, context handling, cost and retry rate. Use independent QA and retain the test prompts/results. Do not choose a provider based only on vendor benchmark claims.

## Privacy and data handling

- Treat free API tiers as potentially unsuitable for confidential or unreleased project material unless the provider's current terms explicitly meet project requirements.
- Google's Gemini API pricing page states that free-tier content may be used to improve products; paid-tier content is not used for that purpose under the stated terms. Verify current terms before sending private project data.
- Never send secrets, access tokens, personal player data or private credentials to model prompts.
- Use minimum necessary project context and redact sensitive material.
- Store provider credentials only in a protected runtime secret store, never in Git, phone notes, source files or task logs.

## Device and runtime boundary

The phone is the mobile command surface and local lightweight-model test device. It is not the dependable always-on worker. Long-running tasks belong on a controlled remote runner with persistent task state, bounded retries, logs and a hard zero-dollar cost limit. Tablet is for review and monitoring. GitHub remains the shared source of truth.

## Initial recommended posture

- Keep all provider/model fields configurable.
- Evaluate currently available free API tiers only after verifying model IDs, quota, privacy terms and tool compatibility. Do not hard-code unverified model names.
- Paid escalation is disabled. Do not configure paid fallbacks.
- Test one small GGUF model in PocketPal on the phone; do not download large models to the A17.
- Use the existing Manus, Perplexity, NotebookLM, Copilot, Gemini and DeepSeek apps as human-facing research/development tools where useful. Do not assume they are automatically callable by Trinity; integrations require supported APIs and credentials.

## Review cadence

Re-check provider model IDs, prices, free quotas, terms, context limits and tool support before activation and periodically thereafter. Record the date and evidence for each approved configuration.
