# Hustle City

Hustle City is a cinematic, realistic 3D social-world/city-life game built with **Godot 4**. This repository is the durable source of truth for project vision, approved decisions, agent roles, architecture, workflows, assets and implementation.

## Start here
- [Project vision and game scope](docs/PROJECT_VISION.md)
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

## Current status
The ten-person named Hustle City cohort and five-role manual execution pilot are defined in GitHub. Models remain unassigned, provider secrets are not confirmed, and no live agent cycle has been run from this repository. The first pilot cycle is documentation/specification only. An initial database model and SQL schema draft now exist in the repository, but no schema has been applied to Supabase. The active Supabase project currently visible has a general command-center name and has not been confirmed as the Hustle City project. Godot implementation status must be tracked separately from design documentation.