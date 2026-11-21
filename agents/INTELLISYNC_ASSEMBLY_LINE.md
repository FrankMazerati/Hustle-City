# Hustle City IntelliSync — Rolling Assembly-Line Production Standard

**Status:** Operating model approved in principle by the creator; exact specialist station order beyond the confirmed foundation stages must follow the approved 12-specialist roster.  
**Applies to:** Trinity, all three QA supervisors, and all 12 production specialists.  
**Primary objective:** Keep production moving continuously through small, versioned, quality-checked packages instead of waiting for one agent or department to finish an entire project.

## 1. The factory-floor principle

Hustle City is produced like a coordinated factory assembly line:

- Every production specialist owns a defined station: a specific responsibility and transformation they perform on an incoming package.
- A package moves from station to station in the configured production order.
- Each station adds its contribution, publishes a new package version, and submits that version to its assigned QA supervisor.
- Only a QA-approved version is released to the next dependent station.
- As soon as a station has safely handed off Package 1, it may begin Package 2 while Package 1 continues downstream.
- The line therefore contains several packages at different stations at the same time.

The goal is **one continuous flow of work**, not twelve agents starting simultaneously without dependencies and not one agent completing the whole city before anyone else can begin.

## 2. Team structure and authority

### Trinity — overall production coordinator

Trinity coordinates the entire line and:
- maintains the production plan, station order, package queue, dependencies, and workload;
- makes sure each package has a clear owner, next station, QA owner, and acceptance criteria;
- coordinates handoffs and prevents packages from being lost, duplicated, or sent to the wrong station;
- monitors bottlenecks, blocked work, review queues, cross-team dependencies, and schedule coverage;
- resolves operational conflicts and escalates product-direction or major-scope decisions to the creator;
- audits QA decisions and ensures consistent quality standards across the three QA supervisors.

Trinity coordinates the QA supervisors; QA supervisors report to Trinity. Trinity does not replace the creator's final authority over product vision, approved creative direction, and major scope changes.

### Three QA supervisors

- QA-1 reviews the four production specialists assigned to QA-1.
- QA-2 reviews the four production specialists assigned to QA-2.
- QA-3 reviews the four production specialists assigned to QA-3.

The exact worker-to-QA mapping must come from the canonical roster/registry. QA ownership determines who is accountable for review; it does not create communication silos. QA supervisors may coordinate and assist one another, while the designated QA owner remains accountable for the recorded review.

### Twelve production specialists

Each specialist:
- owns its assigned station and does not silently take over another station's work;
- transforms the incoming package according to its role;
- communicates with upstream, downstream, peer, QA, and coordinator agents as needed;
- publishes versioned outputs with evidence and explicit handoff notes;
- begins the next package when the current package has been safely handed off and capacity permits.

The exact 12-role roster and names must be taken from the creator-approved roster. Do not promote legacy catalog entries or proposed names into approved assignments without confirmation.

## 3. Package flow: the moving assembly line

A package is a bounded, identifiable piece of the world or game that can be worked on, reviewed, and handed forward without waiting for the entire project to be complete. Examples include a terrain sector, district block, road corridor, station site, building group, venue, character set, or gameplay feature slice.

### Confirmed opening sequence for world construction

1. **World Builder — geographical foundation**
   - Defines the relevant terrain, geography, elevation, water/coastline where applicable, boundaries, coordinate reference, scale, and development-ready area.
   - Publishes a package with clear boundaries, dimensions/units, coordinate conventions, constraints, and known unfinished areas.
2. **Assigned QA supervisor — world package review**
   - Checks the actual package against its acceptance criteria and shared world standards.
   - Returns defects to the World Builder or approves the exact version.
3. **City Builder — city layout**
   - Receives only the approved World Builder package.
   - Establishes the city footprint, districts, neighborhoods, blocks, land use, and development zones within that package.
   - Publishes its transformed package for QA.
4. **Assigned QA supervisor — city package review**
   - Checks that the city layout fits the approved geography, scale, boundaries, and project canon.
5. **Roads and Infrastructure station**
   - Receives the approved city package and develops the streets, intersections, expressways, bridges, access routes, sidewalks, and infrastructure assigned to that package.
   - Coordinates with City Builder before changing block access or city layout.
6. **Assigned QA supervisor — infrastructure package review**
   - Checks connectivity, dimensions, access, safety logic, and compatibility with the approved city package.
7. **Building / Architecture station**
   - Receives the approved package and places/builds structures within approved development blocks.
   - Respects roads, access, building footprints, scale, entrances, and shared interface contracts.
8. **Assigned QA supervisor — building package review**
   - Checks fit, scale, placement, access, visual standards, and technical evidence.
9. **Remaining specialist stations**
   - Receive the package in the configured order and perform their defined contribution: for example environment dressing, transit, vehicles/traffic, NPC navigation and behavior, animation, audio, gameplay interactions, integration, or performance validation.
   - The exact station sequence depends on the package type and approved role roster. Not every station must modify every package; a station may record “not applicable” with a reason and route it onward.
10. **Final integration and package closure**
    - The final required station submits the integrated package and its QA evidence.
    - Trinity verifies that all required stations have completed or recorded an approved not-applicable disposition, dependencies are satisfied, and the package is indexed as integrated.
    - The package is not considered fully integrated merely because it passed one station's QA.

This sequence is the default for geography-to-city construction. Other workstreams (story, cinematics, characters, vehicles, gameplay, backend, audio, and live operations) use their own configured station sequence and dependency graph while following the same package and QA rules. SCRIBE (Story Director) and LENS (Cinematic Camera Director) are distinct peer creative leads under Trinity; their work should be packaged and routed to the specialists who consume narrative and cinematic direction, not forced into an unrelated terrain-only sequence.

## 4. The trickle-down / overlap rule

Stations do not wait for the upstream agent's entire assignment to finish.

Example:
- World Builder publishes World Package 001.
- QA reviews and approves World Package 001.
- City Builder starts City Package 001 using that approved input.
- World Builder continues producing World Package 002.
- Once City Builder has completed and passed QA for City Package 001, it hands that package downstream and may start City Package 002 as soon as World Package 002 is approved and available.
- Roads receives City Package 001 when it is approved, while City Builder works on Package 002.
- Building receives Package 001 after the roads contribution and QA are complete, while Roads works on the next eligible package.

At steady state, the line may look like this:

| Station | Package 001 | Package 002 | Package 003 |
|---|---|---|---|
| World Builder | Handed off | In production | Queued |
| World QA | Approved | Awaiting submission | Queued |
| City Builder | Handed off | In production | Queued |
| City QA | Approved | Awaiting submission | Queued |
| Roads | In production | Waiting for approved input | Queued |
| Building | Waiting for Roads approval | Queued | Queued |

This is an illustrative snapshot, not a fixed clock schedule. Real package states are determined by actual completion, QA, and dependencies.

## 5. QA is a gate at every station

Every production handoff follows this sequence:

1. **Submit:** The owner publishes an immutable/versioned deliverable and marks it ready for QA.
2. **Review:** The assigned QA supervisor reviews the exact version against measurable acceptance criteria, canon, relevant contracts, and applicable tests.
3. **Return or approve:**
   - If it fails, QA records actionable findings, evidence, severity, and the required correction. The package returns to its owner for repair and retest.
   - If it passes, QA records approval against that exact version.
4. **Release:** The approved version becomes available to the next dependent station. The runtime notifies the next owner and Trinity.
5. **Continue:** The prior station may start its next eligible package without waiting for the package to finish the entire line.

QA must never approve work solely from an agent's statement that it is complete. QA must inspect the actual artifact and evidence. No QA supervisor may approve their own deliverable; QA-supervisor outputs require independent review coordinated by Trinity. Trinity audits QA consistency and resolves escalations; it does not silently waive evidence requirements.

A failure in Package 002 must not invalidate an already approved Package 001 unless the failure reveals a shared defect or changed contract that materially affects Package 001. If that happens, Trinity coordinates impact analysis and targeted re-review.

## 6. Package identity, versions, and handoff contract

Every package must have:
- a stable package ID and workstream/area identifier;
- a package sequence or revision number;
- a defined scope and geographic/system boundaries;
- an owner station and assigned QA supervisor;
- input artifact IDs and exact versions;
- upstream dependencies and downstream consumers;
- shared scale, coordinate, naming, file-format, and interface conventions where relevant;
- deliverable paths or artifact references;
- measurable acceptance criteria and test/evidence requirements;
- status, timestamps, review findings, approvals, and handoff history.

A handoff must state:
- what was completed;
- what changed from the incoming version;
- what remains incomplete or intentionally out of scope;
- which constraints and interfaces downstream agents must preserve;
- known risks, assumptions, and open questions;
- the exact approved artifact version to consume;
- the next station and requested action.

Never overwrite an approved package in place. Publish a new version and identify affected downstream consumers. If an upstream revision changes a contract or geometry already used downstream, Trinity coordinates an impact assessment and targeted rework rather than silently replacing downstream work.

## 7. Scheduling, staggered starts, and 24-hour continuity

- Staggered starts are encouraged. Agents do not need to start at the same clock time.
- Start an agent's dependent work when its required input package is approved and available.
- A station may prepare tools, research, templates, reusable assets, tests, and non-dependent work before its first package arrives, but must not fabricate or finalize work that depends on missing upstream decisions.
- The suggested 10-minute production / 5-minute QA / 5-minute correction rhythm is a planning target and checkpoint, not a hard deadline. A package may take less or more time.
- Completion events should trigger QA immediately; do not wait for a 20- or 30-minute polling cycle.
- Checkpoints report throughput, package state, review backlog, blockers, workload, and next handoffs. They do not force agents to stop, submit unfinished work, or auto-approve.
- 24-hour continuity means the queue and handoff state persist across shifts and restarts. If an agent is unavailable, Trinity may route work to an approved backup or mark the station blocked; it must not silently skip a required station.
- Respect compute limits, model availability, and concurrency limits. Parallelism is allowed where dependencies and runtime capacity permit; do not assume every agent can execute simultaneously on one local device.

## 8. Communication rules for the whole line

All agents are members of one open communication network:
- department feeds support local coordination;
- cross-department feeds support direct collaboration across all specialists;
- the command feed connects Trinity and the three QA supervisors;
- every specialist can contact any other specialist, any QA supervisor, and Trinity when relevant.

Upstream and downstream stations should communicate directly about specifications, missing inputs, changes, and compatibility. QA may ask the producing agent for clarification and may consult affected downstream agents. Ordinary questions, progress sharing, coordination, and review requests do not require creator permission. Changes to approved canon, product scope, major priorities, permissions, or shared contracts follow the approval process.

Record durable decisions in canonical repository documents or the decision log; chat is not the sole source of truth. See [COMMUNICATION_PROTOCOL.md](COMMUNICATION_PROTOCOL.md).

## 9. Bottlenecks, blocked packages, and recovery

- Trinity monitors queue depth, time in station, QA turnaround, rework rate, blocked dependencies, and downstream idle time.
- Prioritize blocked packages that prevent several downstream stations from progressing.
- A station may continue independent work while one package is blocked.
- Never send an unapproved package downstream as if it were approved. If downstream preparation is useful, label it explicitly as provisional and prevent integration until approval.
- If QA is overloaded, another QA supervisor may assist; preserve the assigned QA owner's accountability and record the assisting reviewer.
- If a station repeatedly misses acceptance criteria, Trinity coordinates a corrective plan, clarification, or workload adjustment.
- If two agents modify overlapping artifacts, stop conflicting writes, establish one owner for the integration, reconcile changes, and record the result.
- On restart, recover the last durable package state and resume from the last verified handoff. Do not infer that an in-progress or unrecorded package passed QA.

## 10. Minimum runtime capabilities required

The runtime must support:
- persistent package/task registry and dependency graph;
- per-station queues and next-station routing;
- versioned artifact references and immutable QA decisions;
- event-driven QA notifications and handoff events;
- review findings, resubmission, retest, and approval records;
- team directory, direct messages, department feeds, cross-team feed, and command feed;
- workload, blocker, and queue monitoring for Trinity;
- audit trail, timestamps, notifications, and restart recovery;
- role-based tool/write permissions and secret protection.

These are requirements, not claims that the current runtime already implements them. Repository documentation alone does not activate agents, connect models, start a server, or prove that messages and handoffs work.

## 11. Daily production report

At each agreed checkpoint, Trinity publishes:
- packages completed, in production, in QA, rejected, blocked, and released;
- current station occupancy and next eligible package per specialist;
- QA backlog and oldest waiting review;
- downstream stations waiting for inputs;
- rework and recurring defect patterns;
- dependency changes and affected package versions;
- compute/runtime health and agent availability;
- decisions or creator approvals required.

The report should be concise, factual, and linked to package IDs and evidence.

## 12. Definition of success

The assembly line is operating correctly when:
- every package has a traceable route and accountable owner;
- every required station contributes or records a justified not-applicable result;
- each station's output passes its assigned QA gate before release;
- packages flow forward without unnecessary full-project waiting;
- multiple packages can occupy different stations at once without version conflicts;
- downstream work uses known, approved inputs;
- failures trigger targeted correction and retest, not silent bypass;
- Trinity can see and explain the state of the entire line;
- the creator retains authority over vision and major scope decisions.

**Operating motto:** One team. Defined stations. Small approved packages. Continuous handoffs. Quality at every station. Keep the line moving.
