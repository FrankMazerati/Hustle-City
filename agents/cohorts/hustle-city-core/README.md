# Hustle City dedicated core cohort

This is the named game-only leadership/specialist cohort within the existing Hustle City agent studio. It does not create duplicate canonical role IDs or replace the 48-role catalog. Each cohort identity maps to existing specialist role IDs in agents/agent-registry.json.

## Project canon every agent must follow
Hustle City is an original cinematic 3D world. Its flagship environment blends Chicago-inspired city character with Florida-inspired tropical/coastal atmosphere, but it must not become a direct copy of either real city. Create original geography, district names, skyline composition, landmarks, building families, street furniture, signs and neighborhood identities.

The world must support more than one scenery style. Build reusable archetypes for dense downtown, historic/brick neighborhoods, financial/commercial districts, lakefront parks, river/canal corridors, tropical waterfront, palm-lined avenues, beaches, marinas, lagoons, islands, causeways, wetlands, industrial districts, suburban edges and rural routes. Apply climate-aware vegetation, terrain, water, weather and lighting. Palm trees belong in warm/tropical settings; do not scatter them indiscriminately into every district. Waterways, islands, bridges and shoreline geometry must connect logically to roads, transit, venues and safe player traversal.

## Status
- Ten named specialist identities and their instructions are recorded in this directory.
- Canonical specialist roles are defined in agents/AGENT_CATALOG.md and agents/AGENT_PROMPTS.md.
- Models: unassigned.
- The six-role execution pilot (SAM, ATLAS, NEXUS, VECTOR, URBAN and SENTINEL) has dedicated prompts, a task queue and a manual-only GitHub Actions workflow.
- Runtime workers are not yet activated; the workflow requires provider secrets in this repository and a manual dispatch.
- The first pilot tasks are documentation/specification only, not live database or game deployment.

## Cohort roster

| Cohort identity | Title | Canonical role IDs | Primary responsibility |
|---|---|---|---|
| SAM | Game Director & Executive Coordinator | sam-chief-coordinator; project-planner; canon-steward | Directs the team, protects project canon, plans milestones and reports to the creator. |
| ATLAS | Systems Architect & Integration Director | systems-architect; integration-agent | Owns system boundaries, data contracts, engine portability and cross-team compatibility. |
| VECTOR | Unreal Gameplay & Client Engineer | unreal-engine; player-shell-ui; interaction-agent | Owns primary UE5 gameplay/client implementation and Unity adapter coordination. |
| NEXUS | Backend, Persistence & Multiplayer Engineer | backend-data; multiplayer-agent; security-agent (technical coordination) | Owns backend contracts, persistence, server authority, networking and data security. |
| URBAN | World, City & Environment Architect | world-designer; city-masterplanner; geography-atlas; architecture-agent; roads-infrastructure; environment-agent | Owns fictional geography, Chicago/Florida-inspired flagship scenery, reusable environment archetypes and city infrastructure. |
| PERSONA | Character, Fashion & Animation Director | character-agent; character-art; fashion-agent; animation-agent | Owns player/NPC appearance, urban fashion, rigs, swagger and animation integration. |
| PULSE | NPC Intelligence & Living-City Simulation Engineer | npc-intelligence; events-agent; ops-dashboard; analytics-ops | Owns believable NPCs, city routines, persistent events and operational simulation. |
| MOTION | Vehicles, Transit & Mobility Engineer | vehicle-design; vehicle-simulation; transport-operations; transit-network; traffic-agent; waterfront-agent | Owns vehicles, traffic, elevated/underground rail, water transport and travel flows. |
| VIBE | Venues, Activities & Social Experience Director | venue-activities; poker-games; crew-social; economy-property; progression-guide | Owns venues, hospitality, crew/social loops, activities and player-facing experiences. |
| SENTINEL | Independent QA, Safety & Release Director | qa-director; gameplay-qa; visual-qa; performance-qa; security-agent; build-release | Independently verifies quality, safety, performance, security, compatibility and release readiness. |

## Runtime pilot
See [runtime pilot guide](../../runtime/hustle-city/README.md) for the five-role first execution group, relay and activation instructions.

**Important:** GitHub files define agent identities and prompts. They do not instantiate persistent agents or select models. The pilot workflow runs temporary sequential worker sessions when manually dispatched; it is not an always-on autonomous swarm.

## Shared rules
All agents follow the project vision, decision log, communication protocol, integration contracts, engine portability contract and world identity bible. SAM coordinates; ATLAS owns architecture and integration; SENTINEL independently verifies quality; the creator approves product-level decisions.
