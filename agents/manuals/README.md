# Hustle City Specialist Mission Manuals

These manuals are the deep onboarding and operating references for the first two tested World & Construction agents.

| Agent | Role | Manual |
|---|---|---|
| Atlas | World Architect | [Atlas Mission & Operating Protocol](ATLAS_MISSION_AND_OPERATING_PROTOCOL.md) |
| Brick | City Builder | [Brick Mission & Operating Protocol](BRICK_MISSION_AND_OPERATING_PROTOCOL.md) |

Each manual contains 24 page-separated sections covering welcome, mission, team position, chain of command, role boundaries, objectives, canonical world constraints, quality standards, work requirements, communication, agent/model routing, escalation, QA, handoffs, cost/safety rules, daily operations and a first mission.

## Runtime integration notes
- Treat these manuals as agent knowledge sources, not evidence that the agents or server are currently running.
- Primary and backup model IDs must be read from the live agent registry/runtime configuration. Do not invent assignments.
- Each agent uses one assigned local Ollama model at a time. Cloud providers are backup/escalation only when a verified free quota and approved credentials are available. Project spending remains $0.
- Contact other agents through the registered IntelliSync relay/coordinator. Do not assume direct model-to-model networking.
- The creator is final creative authority; Trinity is overall coordinator; assigned QA supervisors review their four-worker groups; Trinity audits QA decisions and escalations.
- The QA supervisor names and exact four-agent assignments must be resolved from the canonical live roster/registry before runtime activation.
