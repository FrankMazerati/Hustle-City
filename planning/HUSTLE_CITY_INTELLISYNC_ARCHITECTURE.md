# Hustle City IntelliSync Architecture

**Status:** Architecture direction approved by the project owner; implementation and runtime integration are pending verification.  
**Repository:** Hustle City  
**Target branch:** prototype/unreal5-playable-foundation

## 1. Purpose

IntelliSync is the shared intelligence and coordination layer for Hustle City Main. It is more than a data synchronization bus: it gives agents and game systems a common, governed understanding of the world, the systems that affect one another, changes being made, and evidence from tests.

It supports two related operating contexts:

1. **Development IntelliSync** — helps AI agents and human contributors inspect changes, understand dependencies, review one another's work, identify integration risks, and coordinate improvements.
2. **Runtime City Intelligence** — helps the game simulation coordinate and evaluate interacting systems such as roads, traffic signals, vehicles, pedestrians, transit, weather, businesses, and safety.

The two contexts should share schemas, entity definitions, event contracts, and validation rules where appropriate. They do not have to run as one process or share unrestricted access.

## 2. Design principles

- **Shared understanding:** systems publish structured descriptions of their responsibilities, entities, state, and interfaces.
- **Parallel ownership:** agents can work simultaneously on separate systems under clear ownership and contracts.
- **Visible changes:** every proposed or accepted change records its author, scope, reason, affected systems, and evidence.
- **Dependency awareness:** changes are evaluated against connected systems, not only the component being edited.
- **Review before adoption:** recommendations are not silently applied. The owning agent or authorized human approves changes.
- **Testable behavior:** important interactions have deterministic scenarios and explicit acceptance criteria.
- **Safety by design:** collision and hazard scenarios test prevention, mitigation, and recovery. Player death is not a gameplay outcome.
- **Governed integration:** access, identity, ownership, audit, and data movement follow Command Center governance.
- **No assumed runtime:** existing Command Center IntelliSync concepts or services may be reused only after their interfaces, access, and runtime behavior are verified.

## 3. Core components

### A. Shared World Intelligence Model

A canonical, versioned registry describing:

- World entities: districts, blocks, roads, lanes, intersections, sidewalks, crossings, buildings, venues, vehicles, pedestrians, transit stops, and businesses.
- Systems: world generation, traffic, pedestrian AI, vehicles, transit, weather, interactions, player safety, economy, and presentation.
- Ownership: responsible agent/team, human reviewer, repository paths, and interface contracts.
- Relationships: which entities and systems depend on, influence, or constrain others.
- State contracts: what data each system owns and what data it may read or publish.

Each system remains authoritative for its own state. The shared model describes and links the state; it must not create competing sources of truth.

### B. Event and Change Bus

A typed event stream for development changes and runtime simulation events.

Every event should include, where applicable:

- event ID and schema version
- event type and timestamp
- source system and owner
- entity or component identifiers
- correlation/trace ID
- change summary and reason
- affected dependencies
- evidence or test references
- status: proposed, accepted, rejected, applied, or reverted

Events must be idempotent where retries are possible. Invalid or unknown schema versions must be rejected or quarantined rather than silently misinterpreted.

### C. Dependency Graph

A versioned graph connecting systems, entities, interfaces, and shared resources. It should answer:

- What depends on this component?
- Which systems could this change affect?
- Who owns those systems?
- Which tests should run after this change?
- Are two agents editing conflicting contracts or files?

### D. Rules and Simulation Engine

A deterministic rules/test layer evaluates cross-system behavior. It should support repeatable test fixtures, event sequences, expected outcomes, and regression checks.

### E. Agent Review and Recommendation Loop

1. An agent submits a change or recommendation.
2. IntelliSync identifies affected systems and owners.
3. Relevant agents inspect the change and return evidence-backed findings.
4. The owning agent or authorized human accepts, rejects, or requests revision.
5. Approved changes run required checks and integration tests.
6. The outcome is recorded for all contributors.

Agents may recommend changes across team boundaries, but they may not overwrite another system's authoritative work without approval.

### F. Observability and Audit

Provide a shared view of agent activity, change history, dependencies, open risks, test status, decisions, and integration health. Preserve enough information to reproduce why a change was accepted or rejected.


## 3A. Synchronization cadence and living-world services

IntelliSync must support three complementary synchronization modes:

1. **Daily development synchronization:** at a configured daily checkpoint, reconcile the Command Center and Hustle City development rosters, role ownership, assignments, progress reports, completed work, blockers, dependency changes, open reviews, and integration status. Produce a dated snapshot and carry unresolved work forward. This is a recurring reconciliation cycle, not a claim that a scheduled job is already deployed.
2. **Event-driven development synchronization:** publish relevant changes as they happen so dependent agents can see new work and review requests without waiting for the daily checkpoint.
3. **Real-time runtime synchronization:** coordinate live player presence, world events, NPC activity, dialogue, and relationship state using authoritative game services and event timestamps.

The daily cycle should detect stale assignments, missing owner reports, conflicting edits, newly introduced dependencies, and work awaiting review. It should not overwrite a contributor's work or silently change role assignments. Each team retains its own source of truth; IntelliSync reconciles references and reports discrepancies.

### Player and event synchronization

The runtime layer must connect player context to the living city. It should support:

- player presence, current location, party/crew context, and relevant activity state
- event discovery, eligibility, invitations, attendance, participation, outcomes, and follow-up
- event changes that reach affected players and NPCs in a timely, consistent way
- shared event state so participants see compatible status and outcomes
- reconnect/recovery behavior when a player disconnects or misses an update
- privacy and permission checks so players only receive information they are allowed to see

A player should be able to encounter an event naturally, receive a relevant invitation or notification, join with others where allowed, and see the event's consequences reflected in the world.

### Conversational synchronization

Dialogue is a first-class runtime system, not a collection of disconnected one-line NPC responses. IntelliSync should coordinate:

- speaker identity, conversation participants, and turn order
- conversation/session ID and dialogue history or a bounded context summary
- current topic, location, event context, relationship context, and conversation intent
- NPC personality, voice, age-appropriate language, and relationship boundaries
- player responses and NPC follow-up turns, including interruptions or topic changes where supported
- world events that can start, interrupt, or change a conversation
- durable outcomes such as a promise, invitation, rumor, relationship change, or event lead, subject to game rules

A conversation should remain coherent across back-and-forth turns. The system should not have two agents independently speak for the same character at once; a dialogue/session owner coordinates turns while other agents may provide reviewed context or suggestions.

### Story character continuity

Frank Maserati is a named story character. His female travel companion remains a canon character whose permanent name is intentionally undecided. Until the project owner chooses her name, use the stable temporary identifier `character.frank_companion_temporary` and the display label **Frank's Companion**. Do not invent a permanent name or infer her identity. Her dialogue, reactions, travel arrival, and relationship to Frank must remain consistent across opening scenes and later story references.

## 4. First vertical slice: intelligent downtown intersection

The first proof should connect five independently owned concerns:

- **Roads and crossings:** lanes, sidewalks, stop lines, crosswalk geometry.
- **Traffic signals:** signal phases, timing, and right-of-way.
- **Vehicle behavior:** approach speed, stopping distance, queueing, turning paths.
- **Pedestrian behavior:** routes, crossing intent, crossing occupancy, and safe waiting.
- **Safety and validation:** conflict detection, mitigation, recovery, and repeatable tests.

### Example scenario

A signal timing change allows a vehicle movement while a pedestrian is still occupying a crossing. IntelliSync should:

1. Read the signal, vehicle, and pedestrian events.
2. Resolve the shared intersection and crossing entities.
3. Detect the conflicting movement using explicit right-of-way and occupancy rules.
4. Identify the traffic, pedestrian, and safety owners.
5. Produce a finding that explains the conflict and its evidence.
6. Recommend a correction, such as revised phase timing or a protected crossing interval.
7. Require owner approval before adopting the change.
8. Re-run the scenario and record whether the conflict is resolved.

Tests should cover safe crossing, conflicting signal phases, a vehicle failing to yield, a pedestrian entering late, emergency-vehicle priority, and recovery from blocked or invalid states. These are simulation test cases, not claims that the feature already exists.

## 5. Initial event contract (illustrative)

```json
{
  "schema_version": "1.0",
  "event_id": "example-event-001",
  "event_type": "traffic.signal.phase_changed",
  "source_system": "traffic",
  "owner": "traffic-agent",
  "entity_id": "intersection-downtown-001",
  "correlation_id": "scenario-crossing-001",
  "payload": {
    "phase": "vehicle_green",
    "crossing_id": "crossing-north-001"
  },
  "status": "proposed"
}
```

This is an example contract only. Final field names, identifiers, validation, and transport are to be established during implementation.

## 6. Agent coordination standards

Every agent assignment should state:

- objective and acceptance criteria
- owned files, systems, and interfaces
- dependencies and affected agents
- inputs and outputs
- required tests
- evidence/report format
- integration and review owner

Agents should work in parallel wherever interfaces are stable. Integration checks, contract tests, and clear ownership protect that parallel throughput; they are not a reason to serialize independent work.

## 7. Command Center relationship

The Command Center's Synapse/IntelliSync intelligence is the intended source of reusable coordination patterns and, where verified, shared services. Hustle City Main owns its game-world model, runtime event contracts, and simulation behavior.

Before connecting services, verify authentication, permissions, data ownership, event schemas, health reporting, and actual end-to-end delivery. Existing tables or API foundations alone do not prove that operational synchronization is running.

## 8. Implementation sequence

1. Add the architecture and ownership contracts to the repository.
2. Define the initial world entity and system registry.
3. Define versioned event schemas and validation.
4. Define the dependency graph and change/review record.
5. Build the intersection scenario and deterministic test fixtures.
6. Connect agent review and approval workflow.
7. Add runtime adapters for the Unreal prototype after the contracts are validated.
8. Verify integration with Command Center services without assuming an existing live connection.\n9. Add daily development reconciliation and event-driven change notifications.\n10. Add runtime player/event synchronization and stateful dialogue sessions.

## 9. Definition of the first demonstration

The first IntelliSync demonstration is successful when contributors can see:

- the intersection's connected systems and owners
- a proposed change from one system
- the dependent systems identified by IntelliSync
- a cross-system risk finding with reproducible evidence
- recommendations from relevant agents
- an owner decision
- before/after test results and an audit record

**Current implementation status:** the architecture and initial registry/event contracts are committed, and a first dependency-impact checker exists in the repository. Daily scheduling, live player/event synchronization, stateful dialogue runtime, the event bus, agent review loop, simulation engine, and Command Center connection are not yet verified as deployed or operational.
