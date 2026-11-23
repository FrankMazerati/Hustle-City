# Hustle City

Hustle City is a cinematic, realistic 3D social-world/city-life game built primarily with **Unreal Engine 5**, with **Unity 6** as a secondary compatibility target. This repository is the durable source of truth for project vision, approved decisions, agent roles, architecture, workflows, assets and implementation.

## Start here
- [Project vision and game scope](docs/PROJECT_VISION.md)
- [World identity bible — original Chicago/Florida-inspired scenery](world/WORLD_IDENTITY_BIBLE.md)
- [Master geography blueprint](world/MASTER_GEOGRAPHY_BLUEPRINT.md)
- [Transportation network specification — HIM and HCTA](world/TRANSPORTATION_NETWORK_SPEC.md)
- [World foundation workplan](planning/WORLD_FOUNDATION_WORKPLAN.md)
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
- [17-agent local workforce and coordinator structure](intellisync/config/coordination.json)
- [Library workstation and portable project handoff](planning/LIBRARY_WORKSTATION_QUICKSTART.md)
- [Opening cinematic and Bella Rose introduction brief](planning/OPENING_SEQUENCE_PRODUCTION_BRIEF.md)
- [Asset import manifest](ASSET_IMPORT/IMPORT_MANIFEST.md)
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
The active target workforce is 17 local agents: SCRIBE, LENS, three QA supervisors and twelve production specialists. ChatGPT is the external coordinator; there is no local Trinity model/agent. Fourteen Ollama models are user-reported as installed but have not been device-verified in this session; three additional pulls are planned, not confirmed. Model assignments and the scheduler remain disabled pending exact inventory, role mapping, QA ownership and hardware checks. The first Unreal visual milestone is the train-arrival opening and Bella Rose guided introduction. Asset manifests and import scripts are committed, but source binaries have not yet been downloaded or imported. The library workstation workflow is documented. The initial database model and SQL draft remain un-applied; no live agent cycle or Unreal build has been verified.
