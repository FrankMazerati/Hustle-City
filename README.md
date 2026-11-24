# Hustle City

Hustle City is a cinematic, realistic 3D social-world/city-life game built primarily with **Unreal Engine 5**, with **Unity 6** as a secondary compatibility target. This repository is the durable source of truth for project vision, approved decisions, agent roles, architecture, workflows, assets and implementation.

## Project knowledge library
- [Hustle City Knowledge Library](knowledge-library/README.md) — permanent home for new ideas, approved decisions and reusable frameworks.
- [Idea inbox](knowledge-library/ideas/INBOX.md) — drop freestyle ideas here immediately.
- [Knowledge index](knowledge-library/INDEX.md) — browse transportation, building, Sims/MPC/NPC and other frameworks.
- [Decision register](knowledge-library/DECISION_REGISTER.md) — current captured decisions and unresolved questions.
- [Conversation-to-repository audit](docs/CONVERSATION_TO_REPOSITORY_AUDIT_2026-11-24.md) — cross-project coverage, conflicts, database gaps and update priorities.

## Start here
- [Project vision and game scope](docs/PROJECT_VISION.md)
- [World identity bible — original Chicago/Florida-inspired scenery](world/WORLD_IDENTITY_BIBLE.md)
- [Portable engine architecture](architecture/PORTABILITY_CONTRACT.md)
- [Decision log and unresolved items](docs/DECISION_LOG.md)
- [Database foundation and deployment status](database/README.md)
- [Core data model](database/DATA_MODEL.md)
- [Database questions and deferred design](database/SCHEMA_GAPS.md)
- [Initial SQL schema draft — review only](database/schema/001_core_schema_draft.sql)
- [AI agent studio catalog](agents/AGENT_CATALOG.md)
- [Agent prompts](agents/AGENT_PROMPTS.md)
- [Machine-readable agent registry](agents/agent-registry.json)
- [Dedicated Hustle City cohort](agents/cohorts/hustle-city-core/README.md)
- [Dedicated runtime pilot and activation steps](agents/runtime/hustle-city/README.md)
- [IntelliSync package-relay runtime](intellisync/README.md)
- [Rolling assembly-line production standard](agents/INTELLISYNC_ASSEMBLY_LINE.md)
- [Agent communication protocol](agents/COMMUNICATION_PROTOCOL.md)
- [Cross-system integration contracts](architecture/INTEGRATION_CONTRACTS.md)
- [QA and glitch prevention](quality/QUALITY_SYSTEM.md)
- [AI runtime and workflow plan](automation/AI_RUNTIME_PLAN.md)
- [Roadmap](planning/ROADMAP.md)

## Operating principles
1. Preserve creator-approved decisions; label ideas as proposed until approved.
2. Do not silently invent unresolved names, rules, dimensions, licensing or implementation status.
3. Agents work as one coordinated network through shared contracts and targeted reviews.
4. A generated image is a concept reference, not automatically a production-ready 3D asset.
5. Never commit API keys, credentials, private player data or secrets.
6. Do not claim a feature, workflow, build or agent is running unless it has actually been activated and verified.

## Engine direction
Unreal Engine 5 is the primary production engine. Unity 6 is the secondary compatibility/migration target. Godot is retired as an active target; existing work/history is preserved pending review. The flagship fictional world blends Chicago-inspired urban character with Florida-inspired tropical/coastal atmosphere while retaining original Hustle City geography, landmarks and identity. Reusable environment profiles must support other distinct U.S. scenery types.

## Current status
The repository contains a substantial project design library, a starter Unreal Engine 5 scaffold, IntelliSync runtime/configuration, agent definitions and a review-only database SQL draft. The current creator-approved workforce target is 17 local roles (SCRIBE, LENS, QA-1–QA-3 and P01–P12), with ChatGPT serving as the external coordinator; existing repository workforce configs still contain older 12-specialist/3-QA and legacy 48-role descriptions and require reconciliation. The scheduler remains disabled, the full 20-minute production / 5-minute independent QA / 5-minute correction loop is not yet implemented and tested, and no live agent cycle is verified. The SQL draft now includes the four currency codes (HUSTLE_MONEY, DIAMONDS, POKER_CHIPS, WINGS), but it has not been applied to a confirmed Hustle City Supabase project. The current foundation work is on the open, unmerged [PR #11](https://github.com/FrankMazerati/Hustle-City/pull/11); commits to that branch are documentation/code changes, not proof of deployed or shipped features.
