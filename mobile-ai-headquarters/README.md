# Hustle City Mobile AI Headquarters

> **Superseded blueprint — not the current command-center operating plan (2026-11-24).** This document describes an earlier Galaxy A17/12-specialist/remote-model/branch-per-task concept. Current direction prioritizes the tablet as the dedicated Hustle City command center, a 17-role local workforce target, one shared `main` branch and no per-agent branches. ChatGPT is the external coordinator. Preserve this file as historical design context; do not use its older roster, device hierarchy or branch workflow as current instructions. See [the conversation-to-repository audit](../docs/CONVERSATION_TO_REPOSITORY_AUDIT_2026-11-24.md).


Status: architecture and configuration blueprint; not yet deployed or running.

Working branch: `agents/mobile-ai-headquarters-v1`

## Purpose

Use the Galaxy A17 as a lightweight mobile headquarters for managing a 12-agent specialist workforce. AI reasoning runs through remote model APIs. The phone stores agent definitions, project instructions, lightweight controller/relay code, task metadata, and working copies. GitHub is the shared version-control source of truth. A tablet is the primary review/display station. USB-attached 1 TB storage is for large assets and backups.

## Command structure

- **Trinity** — central coordinator; routes work, maintains project-wide context, resolves conflicts, and reports to the creator. Trinity is outside the 12 specialist seats.
- **12 specialist agents** — see [agent-roster.json](agent-roster.json) and [agent-personas.md](agent-personas.md).
- **Four logical AI engine groups** — three agent seats per group. Agents share a configurable model pool; tasks route to the strongest suitable model under capability, privacy, latency, quota and budget rules. See [model strategy](model-strategy.md).
- **Nexus** — shared backend/multiplayer engineering support role already described in the wider project; not counted among the 12 seats and not assumed to be a running agent.

## Initial AI budget policy

The creator selected **100% free initially; no paid API calls**. The router enforces a hard zero-dollar ceiling. If no verified free hosted model or verified local endpoint is available, tasks are queued rather than sent to a paid fallback. Free app/chat access is not assumed to provide free API access. Provider configuration remains disabled until current quotas, terms, model IDs and compatibility are verified.

The first router implementation is in `runtime/model_router.py`, with a fail-closed configuration in `runtime/model-router.config.json` and policy tests in `runtime/tests/`.

## First implementation milestones

1. Confirm this blueprint against the existing repository standards.
2. Add individual agent prompt files and structured task contracts.
3. Implement a lightweight remote-model relay with secure secret handling.
4. Add task queue, run records, retries, and agent health reporting.
5. Add branch-per-task GitHub workflow and automated validation.
6. Test USB storage access and backup/restore on the actual Galaxy A17.
7. Build a tablet-friendly status/review dashboard.

## Safety and reliability rules

- No API keys, access tokens, passwords, or private credentials in Git.
- Never let agents push directly to the protected main branch.
- Each task uses an isolated branch or worktree and a declared file scope.
- Require tests and QA before a pull request is marked ready.
- Human approval is required before merging into the main project.
- Keep phone storage for active work; put large source assets and versioned archives on external storage.
- Remote execution must be resumable if the phone goes offline. Do not depend on Android keeping a long-running process alive.
- Agent configurations are not the same thing as AI models: the phone stores the former; remote services provide the latter.

## Current status

This branch contains design/configuration documents only. Creating these files does not install Android applications, configure API credentials, deploy a server, or activate autonomous agents. Those are later, separately verified steps.
