# Hustle City dedicated core cohort

This cohort is a named, game-only working group within the existing Hustle City agent studio. It does not create duplicate canonical role IDs or replace the 48-role catalog. Each cohort identity maps to existing specialist role IDs in agents/agent-registry.json.

## Status

- Ten named specialist identities and their instructions are recorded in this directory.
- Canonical specialist roles are defined in agents/AGENT_CATALOG.md and agents/AGENT_PROMPTS.md.
- Models: unassigned.
- The six-role execution pilot (SAM, ATLAS, NEXUS, VECTOR, URBAN and SENTINEL) has dedicated prompts, a task queue and a manual-only GitHub Actions workflow.
- Runtime workers are not yet activated; the workflow requires provider secrets in this repository and a manual dispatch.
- The first pilot tasks are documentation/specification only, not live database or game deployment.

## Cohort roster

| Cohort identity | Function | Existing canonical role IDs | Initial instruction |
|---|---|---|---|
| SAM | Game Director | sam-chief-coordinator; project-planner; canon-steward | [SAM.md](SAM.md) |
| ATLAS | Systems & Integration Architect | systems-architect; integration-agent | [ATLAS.md](ATLAS.md) |
| VECTOR | Gameplay & Godot Engineer | godot-engine; player-shell-ui; interaction-agent | [VECTOR.md](VECTOR.md) |
| NEXUS | Backend & Multiplayer Engineer | backend-data; multiplayer-agent; security-agent (technical coordination) | [NEXUS.md](NEXUS.md) |
| URBAN | City & Environment Architect | world-designer; city-masterplanner; geography-atlas; architecture-agent; roads-infrastructure; environment-agent | [URBAN.md](URBAN.md) |
| PERSONA | Character, Fashion & Animation Designer | character-agent; character-art; fashion-agent; animation-agent | [PERSONA.md](PERSONA.md) |
| PULSE | NPC & Living-City Simulation Engineer | npc-intelligence; events-agent; ops-dashboard; analytics-ops | [PULSE.md](PULSE.md) |
| MOTION | Vehicles & Transportation Engineer | vehicle-design; vehicle-simulation; transport-operations; transit-network; traffic-agent; waterfront-agent | [MOTION.md](MOTION.md) |
| VIBE | Venues, Activities & Social Experience Designer | venue-activities; poker-games; crew-social; economy-property; progression-guide | [VIBE.md](VIBE.md) |
| SENTINEL | Independent QA & Safety Director | qa-director; gameplay-qa; visual-qa; performance-qa; security-agent; build-release | [SENTINEL.md](SENTINEL.md) |

## Runtime pilot

See [runtime pilot guide](../../runtime/hustle-city/README.md) for the five-role first execution group, relay and activation instructions.

**Important:** GitHub files define agent identities and prompts. They do not instantiate persistent agents or select models. The pilot workflow runs temporary sequential worker sessions when manually dispatched; it is not an always-on autonomous swarm.

## Shared rules

All agents follow the project vision, decision log, communication protocol and integration contracts. SAM coordinates; ATLAS owns architecture and integration; SENTINEL independently verifies quality; the creator approves product-level decisions.