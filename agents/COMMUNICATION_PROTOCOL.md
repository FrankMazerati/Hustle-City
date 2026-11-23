# Hustle City IntelliSync Communication Protocol

## Purpose and authority

Hustle City agents operate as one coordinated production team, not isolated chatbots or sealed departments. Every agent must be able to discover the team, understand who owns each responsibility, communicate directly with relevant colleagues, and coordinate work across specialties.

The approved target structure is **ChatGPT as the external overall coordinator** (not a local Ollama agent), with **17 local agents**: two creative leads (SCRIBE and LENS), three QA supervisors, and twelve production specialists. The QA supervisors report to ChatGPT and each owns quality review for a designated group of four production specialists. There is no local coordinator agent or coordinator model. QA ownership determines review responsibility; it does **not** restrict who may communicate with whom.

This document describes the intended IntelliSync operating rules. Repository instructions do not, by themselves, prove that a live messaging service, agent runtime, model connection, or automatic repository synchronization is active. Runtime implementation must provide the channels, delivery, persistence, and notifications described here.

## Communication is open; authority remains structured

- All 12 production specialists, both creative leads, and all three QA supervisors are members of the same communication network. ChatGPT participates as the external coordinator.
- Any agent may initiate a relevant direct conversation with any other agent, including across departments and QA groups. Agents do not need the creator's or ChatGPT's advance permission merely to ask a question, share information, coordinate a dependency, request a review, or resolve a routine working issue.
- Agents may join relevant department and cross-department discussions, share progress, flag risks, and propose solutions.
- An agent must not take over another agent's assigned deliverable, change another role's ownership, or silently alter approved project canon.
- Open communication is not open authority. Product-direction changes, scope changes, priority overrides, permission changes, irreversible actions, and changes to approved shared contracts follow the appropriate approval path.
- When uncertain, ask and document; do not silently assume.

## Required communication feeds

### 1. Department communication feed

Each four-specialist department has a shared working feed for its members and assigned QA supervisor. Use it for:
- day-to-day coordination and progress updates;
- questions, clarifications, design discussion, and peer assistance;
- identifying shared dependencies and resolving routine conflicts;
- posting work-in-progress references and requesting early feedback;
- preparing deliverables for QA review.

Department feeds are collaboration spaces, not communication barriers. A member may contact any other department directly whenever work overlaps.

### 2. Cross-department communication feed

Provide a team-wide cross-department feed and direct agent-to-agent messaging. Any specialist may contact any other specialist, any QA supervisor, or ChatGPT when a task crosses ownership boundaries or requires expertise elsewhere.

Use cross-department communication for:
- interface and asset dependencies;
- world-to-gameplay, character-to-animation, vehicle-to-transit, NPC-to-venue, and other connected systems;
- handoffs, integration questions, shared risks, and compatibility reviews;
- early warnings when a change may affect another team's work.

Notify the agents who are affected; do not spam the entire team for an isolated issue. Use a broad broadcast when the information genuinely affects everyone.

### 3. Command communication feed

The command feed connects the external coordinator (ChatGPT) and all three QA supervisors. It supports coordination, workload and risk visibility, QA escalations, cross-QA assistance, review disputes, and project-wide broadcasts.

Production specialists must be able to:
- contact their assigned QA supervisor directly about reviews, findings, evidence, and corrections;
- contact another QA supervisor when a cross-department issue requires that supervisor's expertise or the assigned reviewer is unavailable;
- contact ChatGPT directly for blockers, conflicting direction, priority or ownership disputes, urgent risks, or matters that cannot be resolved at working level.

QA supervisors may communicate directly with one another and with every production specialist. ChatGPT coordinates and audits QA decisions; QA supervisors report to ChatGPT; the creator remains final authority.

## Team directory and shared context

The runtime should expose a current team directory to every agent, containing each agent's stable ID, display name, role, department, expertise, assigned QA supervisor, current task/status, and permitted contact routes.

All agents share access to approved project canon, decisions, relevant contracts, and task context according to their permissions. Department-specific knowledge may be emphasized for relevance, but must not be used to hide information needed by another department. Respect least-privilege access for tools, credentials, and write permissions.

## Message format and conversation hygiene

Messages should be structured enough to be actionable without making ordinary conversation cumbersome. When relevant, include:
- sender and intended recipient(s);
- department/channel and related task or issue ID;
- concise subject and message;
- linked repository paths, artifact versions, or evidence;
- priority and needed-by time, if applicable;
- whether a reply, review, decision, or approval is requested.

Use stable task and artifact references so conversations can be traced. Keep decisions and accepted changes in canonical repository artifacts or the decision log; chat alone is not the source of truth. Preserve message history, timestamps, delivery status, unread state, and task-linked discussion in the runtime communication hub.

## Rolling assembly-line package relay
All specialists follow [INTELLISYNC_ASSEMBLY_LINE.md](INTELLISYNC_ASSEMBLY_LINE.md): each specialist is a defined production station; versioned packages move to the next dependent station only after the assigned QA supervisor approves that station's output. A station may begin its next eligible package once the current package is safely handed off, while earlier packages continue downstream. Use event-driven review and handoff notifications; do not wait for a full upstream project to finish, skip required stations, or bypass QA. The World Builder → City Builder → Roads & Infrastructure → Building / Architecture sequence is the opening geography-to-city pipeline. Other workstreams use configured dependency-based station sequences.

## Continuous QA communication and handoffs

- All 12 specialists may work in parallel when their dependencies allow.
- A specialist signals completion and submits a versioned deliverable with acceptance evidence. That completion event should place the deliverable in the assigned QA supervisor's review queue without waiting for a polling interval.
- The assigned QA supervisor reviews the actual artifact against its acceptance criteria, project canon, relevant contracts, and applicable tests. A creator's self-report is not QA evidence.
- If work fails, QA sends actionable findings, evidence, severity, and correction instructions to the original owner. The owner corrects and resubmits; QA retests the new version.
- QA tracks the exact artifact version under review. Do not approve a stale version or allow conflicting reviewers to review different versions unknowingly.
- Once QA passes a deliverable, notify the owner, relevant downstream agents, and ChatGPT as appropriate. The approved artifact becomes eligible for dependent handoff.
- Independent work continues when another task fails. Block only work that genuinely depends on the unapproved output; use an explicitly agreed interface or mock when appropriate.
- QA supervisors may help one another during overload while preserving the designated supervisor's ownership and recording who performed each review.
- No QA supervisor may approve their own work. QA-supervisor deliverables require independent review coordinated by ChatGPT.
- Repeated failures, unresolved disagreements, missed critical reviews, or conflicts between QA supervisors escalate to ChatGPT.
- Time targets and review service levels are alerts and planning aids, never permission to stop unfinished work or approve work without evidence.

## Change proposals and dependency notifications

When an agent changes a shared interface, scale, coordinate system, schema, asset format, movement rule, interaction anchor, or event contract:
1. Create a change proposal with rationale, scope, affected artifacts, compatibility impact, and rollback considerations.
2. Identify and notify affected agents across all departments.
3. Request the relevant technical and QA reviews.
4. Wait for required approvals before changing the canonical contract.
5. Update the canonical artifact and decision/changelog record, then notify downstream consumers.

Agents may discuss and develop proposals autonomously. Approval is required only for decisions that cross the defined authority boundary, not for ordinary communication.

## Critical dependency examples

- Character ↔ Architecture: scale, doors, stairs, elevators, seats, collision, and interaction anchors.
- Character ↔ Clothing ↔ Motion: rig, body shape, clothing slots, clipping, gestures, and animation.
- Character ↔ Vehicles ↔ Transit: seat anchors, boarding/exiting, capacity, camera, and travel states.
- City ↔ Roads ↔ Traffic ↔ Pedestrians: coordinates, lanes, crossings, signals, and safe stops.
- City ↔ Transit ↔ Architecture: station footprint, platform, entrances, accessibility, and passenger flows.
- World ↔ Environment ↔ City: terrain, water, weather, lighting, and transitions.
- Venue ↔ Interior ↔ NPC ↔ Interaction: circulation, seating, service points, and live activity.
- Events ↔ NPC ↔ Social ↔ Operations: authoritative event state, discovery, and participation.
- Economy ↔ Backend ↔ Multiplayer ↔ Security: authoritative transactions, idempotency, balances, and audit.
- Asset agents ↔ Creator Studio ↔ Build: file formats, metadata, licensing, validation, and publication.
- Story direction ↔ Cinematic direction ↔ Gameplay: narrative continuity, shot design, camera constraints, player agency, and transition timing.

## Conflict resolution and approval boundaries

Agents first check approved canon, decisions, and contracts. Resolve routine misunderstandings directly and record the outcome when it affects work. Technical owners document interface impact; QA documents quality and risk impact; ChatGPT coordinates competing priorities, cross-team conflicts, and QA escalations.

The creator retains final authority over product vision, creative direction, and major scope decisions. ChatGPT may coordinate and recommend but must not silently replace the creator's decision. No agent may silently overwrite another department's approved decision.

## Task envelope

Use this envelope for formal assignments and handoffs; omit fields that do not apply.

```yaml
task_id: stable-id
requester: agent-id
owner: agent-id
qa_owner: assigned-qa-agent-id
goal: measurable outcome
context_refs: [repository paths, decision IDs]
inputs: [required artifacts and versions]
constraints: [approved decisions and contracts]
dependencies: [agent IDs and artifact versions]
deliverables: [paths, schemas, code, evidence]
acceptance_criteria: [testable checks]
reviewers: [affected agent IDs]
risk: low|medium|high
approval_required: none|ChatGPT|creator
status: proposed|ready|in_progress|blocked|review|accepted|rejected
```

A task's owner, QA owner, reviewers, approval requirements, and status must be visible to the agents who need them. Never treat a message as an approval unless the authorized person or role explicitly gives that approval.
