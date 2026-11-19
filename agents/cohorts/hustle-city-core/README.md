# Hustle City dedicated core cohort

This cohort is a named, game-only working group within the existing Hustle City agent studio. It does not create duplicate canonical role IDs or replace the 48-role catalog. Each cohort identity maps to existing specialist role IDs in `agents/agent-registry.json`.

## Status

- Cohort definitions: recorded in this directory.
- Canonical specialist roles: already defined in `agents/AGENT_CATALOG.md` and `agents/AGENT_PROMPTS.md`.
- Models: unassigned.
- Runtime workers: not activated.
- Tool permissions/schedules: pending runtime configuration.
- First assignments: specification and planning deliverables only; no claim of implementation or execution.

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

## Shared rules

All agents follow the shared operating rules at the top of each individual instruction file, the project vision, decision log, communication protocol and integration contracts. SAM coordinates; ATLAS owns architecture and integration; SENTINEL independently verifies quality; the creator approves product-level decisions.

**Important:** committing these files records the agent identities, prompts and first assignments in GitHub. It does not instantiate workers, choose models, send runtime messages or start automation. Activation requires the runtime/model/tool configuration described in `automation/AI_RUNTIME_PLAN.md`.
