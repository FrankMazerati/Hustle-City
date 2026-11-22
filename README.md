# Hustle City

Hustle City is a cinematic, realistic 3D social-world/city-life game built primarily with **Unreal Engine 5**, with **Unity 6** as a secondary compatibility target. This repository is the durable source of truth for project vision, approved decisions, agent roles, architecture, workflows, assets and implementation.

## Start here
- [Project vision and game scope](docs/PROJECT_VISION.md)
- [World identity bible — original Chicago/Florida-inspired scenery](world/WORLD_IDENTITY_BIBLE.md)
- [Master geography blueprint](world/MASTER_GEOGRAPHY_BLUEPRINT.md)
- [Transportation network specification — HIM and HCTA](world/TRANSPORTATION_NETWORK_SPEC.md)
- [Fashion Hub and 100-floor Hustle Towers foundation](world/FASHION_HUB_AND_HUSTLE_TOWERS_SPEC.md)
- [World foundation workplan](planning/WORLD_FOUNDATION_WORKPLAN.md)
- [First Arrival, rail systems, and Fashion Hub build plan](planning/FIRST_ARRIVAL_AND_FASHION_HUB_BUILD_PLAN.md)
- [Interactive mobile browser preview](web-preview/README.md)
- [Open browser preview source](web-preview/index.html)
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
The world/transit foundation branch now contains an interactive Babylon.js browser blockout for HIM, HCTA, and the Fashion Hub, plus a creator-directed 100-floor Hustle Towers program specification. The browser preview is source code only until hosted/deployed; no public preview URL has been verified. The scene is an early geometry blockout, not final high-fidelity art or a playable game. No Unreal project has been compiled. Models remain unassigned, provider secrets are not confirmed, and no live agent cycle has been run from this repository. An initial database model and SQL schema draft exist, but no schema has been applied to Supabase. The active Supabase project currently visible has a general command-center name and has not been confirmed as the Hustle City project.
