# Agent Communication Protocol

## Principle
Agents share a coherent project context, but do not chatter indiscriminately. Use structured tasks, shared artifacts, dependency notifications and targeted review requests.

## Task envelope
```yaml
task_id: stable-id
requester: agent-id
owner: agent-id
goal: measurable outcome
context_refs: [repository paths, decision IDs]
inputs: [required artifacts and versions]
constraints: [approved decisions and contracts]
dependencies: [agent IDs and artifact versions]
deliverables: [paths, schemas, code, evidence]
acceptance_criteria: [testable checks]
reviewers: [affected agent IDs]
risk: low|medium|high
approval_required: none|SAM|QA|creator
status: proposed|ready|in_progress|blocked|review|accepted|rejected
```

## Cross-talk rules
- When an agent changes a shared interface, scale, coordinate system, schema, asset format, movement rule, interaction anchor or event contract, it must create a change proposal.
- Identify affected agents and notify only those dependencies.
- Request compatibility review and wait for required approvals.
- Update the canonical contract and changelog after approval.
- Agents may inspect one another's work; the Integration Agent verifies compatibility and QA verifies behavior.
- SAM coordinates and escalates; creator approves product-level trade-offs.

## Critical dependency examples
- Character ↔ Architecture: scale, doors, stairs, elevators, seats, collision and interaction anchors.
- Character ↔ Clothing ↔ Animation: rig, body shape, clothing slots, clipping and motion.
- Character ↔ Vehicles ↔ Transit: seat anchors, boarding/exiting, capacity, camera and travel states.
- City ↔ Roads ↔ Traffic ↔ Pedestrians: coordinates, lanes, crossings, signals and safe stops.
- City ↔ Transit ↔ Architecture: station footprint, platform, entrances and accessibility.
- World ↔ Environment ↔ City: terrain, water, weather, lighting and transitions.
- Venue ↔ Interior ↔ NPC ↔ Interaction: circulation, seating, service points and live activity.
- Events ↔ NPC ↔ Social ↔ Operations: authoritative event state, discovery and participation.
- Economy ↔ Backend ↔ Multiplayer ↔ Security: authoritative transactions, idempotency, balances and audit.
- Asset agents ↔ Creator Studio ↔ Build: file formats, metadata, licensing, validation and publication.

## Conflict resolution
Agents first check canon and contracts. Integration documents technical impact; QA documents quality/safety impact; SAM presents options. Creator decides product-level trade-offs. No agent may silently overwrite another department's approved decision.
