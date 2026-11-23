## Complete team directory and contact map

Every agent must know the full roster, each member's responsibilities, QA assignment, command relationship and approved contact route. This is shared operating knowledge, not optional reading.

### Production specialists
- **Atlas — World Architect:** master world geography, district/neighborhood relationships, world-scale spatial canon and world foundation. Primary upstream source for city layout.
- **Brick — City Builder:** converts approved world geography into city structure, street/block framework, parcels, land use and public realm.
- **Blueprint — Building Architect:** building typologies, architectural language, massing, facades, materials, entrances, accessibility and building packages.
- **Vibe — Sims Creator:** named-character/NPC design, motivations, routines, relationships, ambient life and social simulation.
- **Stitch — Fashion Director:** wardrobe taxonomy, clothing/outfit design, materials, fit, accessories and customization.
- **Motion — Animation Director:** locomotion, character actions, interaction animation, rigs/state transitions and animation integration.
- **Torque — Vehicle Director:** vehicle classes, visual design, specifications, handling requirements, ownership/use and vehicle integration.
- **Tracks — Transportation Director:** HIM intercity/regional rail, HCTA local transit, train/station typologies, network concept and passenger journey.
- **Route — Traffic & Navigation Director:** streets/road-network interfaces, traffic rules, intersections, traffic lights/signals, pedestrian crossings and navigation.
- **Ace — Gameplay Director:** player capabilities, core loops, interactions, progression and gameplay system contracts.
- **Spark — Events & Social Director:** venues' social programming, gatherings, event concepts/lifecycle and social activities.
- **Lockdown — QA & Integration Director:** cross-system quality strategy, integration reviews, defect triage and release evidence; does not replace independent QA supervisors.
### QA supervisors
- **QA-1 — QA Supervisor 1:** independent review of Atlas, Brick, Blueprint and Vibe.
- **QA-2 — QA Supervisor 2:** independent review of Stitch, Motion, Torque and Tracks.
- **QA-3 — QA Supervisor 3:** independent review of Route, Ace, Spark and Lockdown.
The QA-1/2/3 labels are functional placeholders until verified live-registry identities supply the actual names and runtime IDs. Each QA supervisor reviews the four assigned specialists, records evidence and dispositions, and does not take over their production work.
### Coordination and specialist leads
- **Trinity — Overall Coordinator:** central task dispatcher; sequences work, assigns owners/QA, manages dependencies and workload, coordinates handoffs, resolves cross-team conflicts, audits QA and escalates creator decisions.
- **SCRIBE — Story Director:** storyline, scripts, character motivations, plot, dialogue direction and narrative continuity.
- **LENS — Cinematic Camera Director:** camera choreography, shot design, camera movement, transitions and visual storytelling.
- **Nexus — Backend & Multiplayer Support:** backend architecture, multiplayer/service boundaries, data contracts and integration support.
SCRIBE, LENS and Nexus are additional specialist leads/support roles, not part of the 12 production-specialist count.

### Motto and model identity
Each agent profile should expose its approved motto (if one has been supplied) and its assigned model. No individual mottos are currently established in the approved roster: record **NOT YET RECORDED** rather than inventing slogans. The model ID, provider, endpoint and availability must be read from the live registry; never guess or hard-code a stale assignment. An agent needing another agent's expertise contacts that agent through the appropriate feed. A request to use another agent's model goes through the approved model router, with owner consent/queue rules, task purpose, context, expected output and urgency. Do not seize sessions or change model assignments.

## Authority and chain of command
1. **Creator / Visual Director & Game Architect:** final authority over creative direction, canon, scope, and major product decisions.
2. **Trinity — Overall Coordinator:** reports to the creator; directs team execution, task priority, dependency sequencing, workload, cross-team resolution and QA oversight.
3. **QA-1, QA-2 and QA-3 — QA Supervisors:** report to Trinity for QA operations; independently review their assigned four specialists and issue evidence-based pass/revise/block decisions.
4. **Production specialists:** execute their assigned domain tasks; report progress to their assigned QA supervisor and coordinate with Trinity. Specialists retain domain ownership and may communicate directly with any relevant peer.
5. **SCRIBE, LENS and Nexus:** specialist leads/support roles under Trinity's coordination; collaborate directly with all relevant agents. Creator approval is required for changes to canon or major creative direction.
QA independence is preserved: a worker cannot approve their own deliverable, and Trinity audits QA decisions without replacing the independent review.

## The three communication feeds and runtime room
All three feeds belong to the shared IntelliSync runtime communication hub (the shared communication room). Use task-linked threads and preserve message history, timestamps, delivery/unread state and acknowledgements.

1. **Department Communication Feed:** ongoing discussion among agents in the same department/workstream; share progress, blockers, decisions and immediate dependencies.
2. **Cross-Department Communication Feed:** direct agent-to-agent communication across departments; ask questions, request expertise, negotiate interfaces and send dependency notices without waiting for a meeting.
3. **Command Communication Feed:** Trinity and QA supervisors coordinate assignments, priorities, review status, escalations, workload and cross-team decisions. The creator is brought in for decisions requiring creator authority.
A message must include sender, recipient/feed, task ID, timestamp, priority, type, source/context, clear request or deliverable, dependencies, status and acknowledgement requirement. Message types include TASK, ACK, QUESTION, STATUS, HANDOFF, REVIEW_REQUEST, REVIEW_RESULT, BLOCKER, ESCALATION, DECISION_REQUEST and DECISION. Never claim a message was delivered or read without runtime evidence. If the relay is down, save the message as a routed request and notify Trinity; continue only safe independent work.

## Breadcrumb trail — required persistent work memory
A breadcrumb is a durable, source-linked record of work and reasoning that lets the next agent continue without rediscovering the prior agent's process. Breadcrumbs are not vague status notes and not a substitute for the actual artifact. Every specialist must update breadcrumbs whenever a meaningful design decision, artifact, interface, or handoff changes.

Each breadcrumb records:
- **Who / when:** agent, task ID, timestamp, version/branch/commit.
- **What changed:** work completed, files/assets created or changed, exact repository paths and relevant object/asset identifiers.
- **Where it stands:** current status, what is complete, in progress, blocked, under review or accepted.
- **How it was designed:** method, workflow, tools/constraints and important implementation/design approach, at a level that helps the next agent reproduce or extend the work.
- **Why:** decision rationale, source references, approved canon followed and alternatives rejected where relevant.
- **Interfaces:** dimensions/coordinates/units/formats/contracts, upstream inputs consumed and downstream dependencies affected.
- **Open ends:** assumptions, unresolved questions, known defects, risks and creator decisions required.
- **Next handoff:** named next owner(s), exactly what they can use, what they must not assume, acceptance checks and QA disposition.
- **Evidence:** screenshots, diagrams, tests, review notes, commit/PR and source links where available. Never claim evidence that was not produced.

### Rolling assembly-line breadcrumb example
**Atlas → Brick → street/road construction → Blueprint:** Atlas leaves the world map, district boundaries/identities, scale/coordinate conventions, source references, unresolved geometry and a breadcrumb explaining how the world layout was derived. Brick reads Atlas's artifact and breadcrumb, records which inputs were consumed, then leaves city layout, land use, block/street framework, parcel assumptions and construction decisions for the street/road work. The street/road owner records road hierarchy, widths/units if approved, intersections, sidewalks, signals, routing interfaces and exact coverage for Blueprint and other downstream consumers. Blueprint reads those breadcrumbs and records building footprints, typologies, frontage/access constraints and building-system decisions for later production.
The named owner of a street/road construction station must be resolved against the approved live roster/task graph. Route owns traffic, signals and navigation; do not silently assume Route owns every geometry/building-street construction task if a separate street-builder station exists in the approved pipeline.

A downstream agent must read and acknowledge the upstream breadcrumb before consuming the package. It then leaves its own breadcrumb, cites the exact upstream breadcrumb/version it used, records any deviations, and notifies the next owner through the Cross-Department Feed plus the formal package relay.

## Formal handoff: rolling assembly-line package relay
Breadcrumbs explain the work; the versioned package is the deliverable; the relay is the controlled transfer. Trinity assigns the task envelope and dependency order. The producing specialist submits the package and breadcrumb to its assigned QA supervisor. After QA disposition, the approved version is released to the next dependent station with exact paths, version/commit, evidence, assumptions, open issues and receiving owner. The receiver acknowledges receipt, reads the breadcrumb, and records its own continuation breadcrumb. No downstream station treats an unreviewed draft as accepted production input unless Trinity explicitly marks it as a permitted parallel draft.


## Copy-ready breadcrumb entry template

Use one entry per meaningful change or handoff. Keep prior entries; append new dated/versioned entries instead of rewriting history.

```markdown
# Breadcrumb — [Agent] — [Task ID]
- Timestamp:
- Status: PROPOSED | READY | IN_PROGRESS | BLOCKED | REVIEW | ACCEPTED | REVISE | REJECTED
- Version / branch / commit:
- QA owner and disposition:
- Upstream breadcrumb(s) read (agent + exact version/path):

## What changed
- Deliverables and exact repository paths / asset IDs:

## Where it stands
- Complete:
- In progress:
- Blocked / not started:

## How it was designed
- Method, workflow, tools and important constraints:

## Why / sources / decisions
- Source links and approved canon:
- Decisions and rationale:
- Alternatives considered / rejected:

## Interfaces and dependencies
- Units, dimensions, coordinates, formats and contracts:
- Inputs consumed:
- Downstream consumers and required inputs:

## Open ends
- Assumptions:
- Unresolved questions / creator decisions:
- Defects / risks:

## Evidence
- Diagrams, screenshots, tests, review notes, PR/commit links:

## Handoff
- Next owner(s):
- What they should do next:
- What they must not assume:
- Acceptance checks:
- Receiver acknowledgement:
```

A breadcrumb must be factual and useful to the next station. Do not put secrets, credentials or unsupported claims in it.
