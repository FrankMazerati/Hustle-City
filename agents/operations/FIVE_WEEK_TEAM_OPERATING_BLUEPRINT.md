# Hustle City — Five-Week Agent Mission & Execution Blueprint

**Horizon:** Five consecutive weeks, seven daily work blocks per week (35 workdays). **Authority:** Creator / Visual Director & Game Architect → Trinity → assigned QA supervisor → specialist. **Cost ceiling:** $0.

## Creator and project context
Hustle City is a premium, realistic, cinematic 3D urban/social open-world city-life game with an original fictional identity informed by Chicago's urban character and Florida's tropical/coastal atmosphere. The creator is the Visual Director and Game Architect, responsible for visual direction, aesthetics, world design and overall architecture, and retains final creative authority. The team turns that vision into coherent, buildable, integrated work. Use only creator biography actually supplied; never invent personal history or motivations. Approved repository decisions are authoritative. Label proposals, assumptions and unresolved facts.

## Complete organization directory, mottos and model identity

The authoritative full roster, domain responsibilities, QA coverage, reporting chain, three communication feeds, runtime communication hub, breadcrumb standard and rolling package relay are defined in [AGENT_COMMUNICATION_AND_BREADCRUMB_STANDARD.md](./AGENT_COMMUNICATION_AND_BREADCRUMB_STANDARD.md). Every agent must read it. No agent may operate with only its own role description. All agents must know every teammate's name, role, responsibilities, QA owner and contact route.

Individual mottos are **NOT YET RECORDED** unless an approved agent profile supplies one. Do not invent mottos. Read assigned model IDs and availability from the live registry; requests for another agent's expertise use the communication feeds, while model-inference requests use the approved model router and queue/owner rules.

## Authority and chain of command
Creator / Visual Director & Game Architect (final creative authority) → Trinity (overall coordinator/task dispatcher) → QA-1/QA-2/QA-3 (independent QA supervisors) → their assigned specialists for review and reporting. Specialists retain their domain ownership and may directly contact any relevant peer through the cross-department feed. SCRIBE, LENS and Nexus are specialist leads/support roles coordinated by Trinity. Trinity audits QA; QA does not report to a production worker. QA labels remain placeholders until runtime identities are verified.

## Three communication feeds and shared room
All messages use the shared IntelliSync runtime communication hub after its health is verified:
1. **Department Communication Feed** — same-department coordination.
2. **Cross-Department Communication Feed** — direct peer-to-peer requests, questions, expertise sharing and dependency coordination.
3. **Command Communication Feed** — Trinity and QA supervisors coordinate tasks, priorities, reviews, blockers and escalations; creator decisions are escalated here when required.
The hub preserves task-linked message history, timestamps, delivery/unread state and acknowledgements. Every message includes sender, recipient/feed, task ID, timestamp, priority, type, context/source, request/deliverable, dependencies, status and acknowledgement requirement. If relay health is not verified, do not claim delivery; route the request to Trinity and continue safe independent work.

## Breadcrumbs and rolling assembly-line handoffs
Every agent maintains a persistent breadcrumb trail recording what changed, exact paths/asset IDs and versions, current status, how the work was designed, why key decisions were made, source references, interfaces/units/contracts, upstream inputs consumed, downstream dependencies, assumptions, unresolved questions, defects, QA state, evidence and named next owner. The next agent must read and acknowledge the upstream breadcrumb, cite its version, record deviations and leave its own continuation breadcrumb. Breadcrumbs explain work; the versioned artifact is the deliverable; the formal package relay is the controlled transfer.

The geography-to-city opening dependency is Atlas → Brick → street/road construction → Blueprint. The street/road station owner must be resolved from the approved task graph; Route owns traffic, signals and navigation, but must not automatically be treated as the owner of every street-geometry task. Trinity coordinates the rolling assembly-line package relay: producer → assigned QA → approved downstream receiver, with exact paths, commit/version, evidence, assumptions, open issues and receiving acknowledgement. Do not consume unreviewed drafts as accepted production inputs unless Trinity explicitly authorizes parallel draft use.

## Model and second-opinion rules
Each agent has exactly one assigned local Ollama model at a time. Read actual model IDs from the live registry; this blueprint does not guess assignments. An agent may request another agent's expertise or model inference through the approved router, identifying task, purpose, context, expected output and urgency. Respect model ownership, active workload, queue and shared memory limits. Never seize another session or change another agent's assignment. Second opinions should be sequential/queued when hardware is constrained. Gemini/OpenRouter are backup only with approved credentials and verified free quota. No paid calls; if free capacity is unavailable, queue or decompose the request.

## Production assembly line
Trinity issues a task package → specialist acknowledges and produces a versioned artifact → specialist submits evidence to its QA supervisor → QA passes, passes with actions, requests revision, blocks or rejects → accepted package is handed to downstream agent(s) → Trinity audits cross-team consistency. No self-approval. A package includes task ID, owner, QA owner, objective, source versions, allowed paths, dependencies, deliverables, acceptance criteria, risk and status. Handoffs include exact paths, branch/commit, changes, assumptions, open questions, QA evidence and next owner. Statuses: PROPOSED, READY, IN_PROGRESS, BLOCKED, REVIEW, ACCEPTED, REVISE, REJECTED. DONE requires evidence. GitHub is durable project record; use branches and PRs. Never claim merged, deployed, running or tested unless verified.

## Five-week role-by-role milestone matrix

**Week 1 is the foundation-design completion sprint.** It is not a week spent only researching or making inventories. Every domain must deliver its first-pass design package by Day 7. Week 2 converts approved designs into detailed specifications; Week 3 produces representative implementation/vertical slices; Week 4 integrates and validates; Week 5 closes acceptance and prepares the next expansion phase.

### Atlas — World Architect
**Week 1 — Foundation design complete:** Complete the first-pass world design: six central district concepts, surrounding-neighborhood framework, district identities, spatial relationships, landmarks and source-linked map blueprint; explicitly leave unsupported grid dimensions/counts unresolved.

**Week 2 — Detailed specifications and contracts:** Convert the approved world into build-ready spatial specs, coordinate/scale conventions, district briefs and terrain/environment zones.

**Week 3 — First production/vertical slice:** Deliver prioritized region layouts, block/parcel guidance, landmark briefs and representative world prototype specs.

**Week 4 — Integrated system validation:** Integrate city, architecture, roads and HIM/HCTA proposals; resolve spatial conflicts and validate circulation and district identity.

**Week 5 — Acceptance and expansion handoff:** Publish accepted World Foundation v1, map/district packages, QA evidence and expansion backlog.

### Brick — City Builder
**Week 1 — Foundation design complete:** Complete first-pass city design: street hierarchy, block logic, parcels, land-use patterns, civic/commercial/residential placement, public spaces and corridors for the approved framework; do not invent counts.

**Week 2 — Detailed specifications and contracts:** Convert plan into street/block templates, parcel/land-use rules, sidewalk/public-realm specs, service access and district kits.

**Week 3 — First production/vertical slice:** Produce representative streets, blocks, parcels and public-space modules with asset lists.

**Week 4 — Integrated system validation:** Integrate buildings, signals, stations, pedestrian routes and venues; validate circulation.

**Week 5 — Acceptance and expansion handoff:** Publish accepted City Foundation v1, district kits, construction specs, QA evidence and build-out backlog.

### Blueprint — Building Architect
**Week 1 — Foundation design complete:** Complete architectural foundation: typology catalog, district-specific language, massing/height guidance where approved, facade/material direction, entrances, accessibility and hero-building shortlist.

**Week 2 — Detailed specifications and contracts:** Turn typologies into modular floor-plan, structural, facade, material, component and performance specifications.

**Week 3 — First production/vertical slice:** Deliver representative building packages and implementation-ready breakdowns for priority residential, retail, civic, transit and landmark types.

**Week 4 — Integrated system validation:** Integrate footprints/entrances with blocks, roads, stations and venue use; validate circulation and visual coherence.

**Week 5 — Acceptance and expansion handoff:** Publish accepted architecture foundation v1, typology library, packages, QA evidence and expansion backlog.

### Vibe — Sims Creator
**Week 1 — Foundation design complete:** Complete character/NPC design: core named-character roster, profiles, motivations, relationships, archetypes, daily routine concepts and social behavior matrix; coordinate canon with SCRIBE.

**Week 2 — Detailed specifications and contracts:** Translate character bible into schedules, needs, relationships, crowd tiers, venue behaviors and data interfaces.

**Week 3 — First production/vertical slice:** Produce representative character/NPC packages, schedules, interaction sets and behavior specs.

**Week 4 — Integrated system validation:** Integrate Stitch wardrobe, Motion animation, Ace gameplay, Spark events and Nexus backend; validate believable city life.

**Week 5 — Acceptance and expansion handoff:** Publish accepted character/NPC foundation v1, relationship/routine libraries, QA evidence and backlog.

### Stitch — Fashion Director
**Week 1 — Foundation design complete:** Complete fashion foundation and design the majority of scoped clothing: taxonomy, style identities, outfit capsules, core catalog, materials, colorways, fit, accessories and priority garments. Track designed versus remaining.

**Week 2 — Detailed specifications and contracts:** Convert designs into garment production specs, PBR materials, texture/colorway sheets, rig compatibility, layering and naming rules.

**Week 3 — First production/vertical slice:** Produce first major clothing asset batch or implementation-ready garment packages for player/core characters.

**Week 4 — Integrated system validation:** Integrate with Motion rigs/animations and Vibe character profiles; test clipping, fit, layering and customization.

**Week 5 — Acceptance and expansion handoff:** Publish accepted fashion foundation v1, evidenced majority-design tracker, asset queue, QA results and wardrobe remainder backlog.

### Motion — Animation Director
**Week 1 — Foundation design complete:** Complete animation design foundation: movement-state architecture, locomotion catalog, core player/NPC actions, interaction list, vehicle/transit movement needs and priority matrix.

**Week 2 — Detailed specifications and contracts:** Specify transitions, timing, root-motion policy, rigs, blend logic, interruption/recovery and event hooks.

**Week 3 — First production/vertical slice:** Produce representative animation sets or implementation-ready locomotion, interaction and social packages.

**Week 4 — Integrated system validation:** Integrate wardrobe/rigs, NPCs, gameplay, vehicles, transit and camera; run compatibility checks.

**Week 5 — Acceptance and expansion handoff:** Publish accepted animation foundation v1, matrix, representative sets, QA evidence and backlog.

### Torque — Vehicle Director
**Week 1 — Foundation design complete:** Complete vehicle foundation: classes, initial roster, design direction, use cases, ownership/access assumptions, visual identity, capacity categories, customization priorities and high-level handling.

**Week 2 — Detailed specifications and contracts:** Specify dimensions envelopes, tunable handling, entry/exit, seats, damage/repair, storage, ownership and garage interfaces.

**Week 3 — First production/vertical slice:** Produce representative vehicle design packages and implementation-ready specs/assets for priority classes.

**Week 4 — Integrated system validation:** Integrate traffic/navigation, animation, gameplay, streets/parking and transit interfaces; validate compatibility.

**Week 5 — Acceptance and expansion handoff:** Publish accepted vehicle foundation v1, roster, design/handling specs, QA evidence and expansion backlog.

### Tracks — Transportation Director
**Week 1 — Foundation design complete:** Complete rail/transit design: HIM intercity/regional role, HCTA local network concept, service purpose, station typologies, interchange logic, train categories and passenger journey. Do not invent station counts/alignments.

**Week 2 — Detailed specifications and contracts:** Specify track/mode options, station access, platform/train interfaces, passenger flow, signaling dependencies, accessibility and safety.

**Week 3 — First production/vertical slice:** Produce representative station/train design packages and implementation-ready network interfaces.

**Week 4 — Integrated system validation:** Integrate geography, city, roads, vehicles, gameplay and backend; validate transfers and access.

**Week 5 — Acceptance and expansion handoff:** Publish accepted HIM/HCTA foundation v1, network concept, station/train package, QA evidence and unresolved alignment register.

### Route — Traffic & Navigation Director
**Week 1 — Foundation design complete:** Complete road/traffic foundation: hierarchy, intersections, traffic-light/signaling concepts, pedestrian crossings, traffic behavior, parking/loading, emergency access, navigation and multimodal circulation.

**Week 2 — Detailed specifications and contracts:** Specify signal phases/logic, lane/intersection rules, traffic states, routing graph, pedestrian/transit priority and safety constraints.

**Week 3 — First production/vertical slice:** Produce representative road/intersection/signal packages and implementation-ready traffic/navigation specs.

**Week 4 — Integrated system validation:** Integrate blocks, stations, vehicles, pedestrian paths and gameplay; validate routes and edge cases.

**Week 5 — Acceptance and expansion handoff:** Publish accepted traffic/navigation foundation v1, signal/intersection library, QA evidence and backlog.

### Ace — Gameplay Director
**Week 1 — Foundation design complete:** Complete gameplay foundation: player fantasy, core loops, player actions, interaction categories, progression pillars, social/economic activities and system dependency map; align narrative boundaries with SCRIBE/creator.

**Week 2 — Detailed specifications and contracts:** Specify loop flows, interaction contracts, progression data, state changes, rewards/costs and interfaces with simulation, vehicles, transit, events and backend.

**Week 3 — First production/vertical slice:** Produce representative playable-slice specification or working prototype plan for the priority loop.

**Week 4 — Integrated system validation:** Integrate characters, events, animation, vehicles, transit, traffic and backend; run end-to-end scenarios.

**Week 5 — Acceptance and expansion handoff:** Publish accepted gameplay foundation v1, core-loop spec, contracts, QA evidence and feature backlog.

### Spark — Events & Social Director
**Week 1 — Foundation design complete:** Complete events/social foundation: venue/gathering categories, event taxonomy, concepts/calendar, activity loops, crowd needs, lifecycle and priority launch event concepts.

**Week 2 — Detailed specifications and contracts:** Specify lifecycle, scheduling, participant selection, venue capacity assumptions, rewards/interactions, crowd behavior and service interfaces.

**Week 3 — First production/vertical slice:** Produce representative event packages with setup, roles, flow, environment/wardrobe/animation needs and gameplay hooks.

**Week 4 — Integrated system validation:** Integrate venues, NPC routines, clothing, animation, gameplay, vehicles and transit; validate attendance journeys.

**Week 5 — Acceptance and expansion handoff:** Publish accepted event/social foundation v1, representative packages, QA evidence and future backlog.

### Lockdown — QA & Integration Director
**Week 1 — Foundation design complete:** Complete QA foundation while enabling Week 1 design completion: acceptance checklists for all major domains; review completeness and traceability without authoring their designs.

**Week 2 — Detailed specifications and contracts:** Establish domain validation suites, interface checks, traceability and risk-based review procedures.

**Week 3 — First production/vertical slice:** Run structured integration reviews on representative packages; publish defect/decision reports.

**Week 4 — Integrated system validation:** Coordinate cross-system integration/regression; verify high-priority defects fixed or explicitly accepted.

**Week 5 — Acceptance and expansion handoff:** Publish integrated QA foundation v1, acceptance matrix, evidence and residual-risk backlog.

### QA-1 — QA Supervisor 1
**Week 1 — Foundation design complete:** Verify Atlas world, Brick city, Blueprint architecture and Vibe character/NPC foundations are complete, traceable and coherent; surface findings fast.

**Week 2 — Detailed specifications and contracts:** Validate detailed specs/interfaces for geography, city construction, buildings and NPC/social simulation.

**Week 3 — First production/vertical slice:** Review representative packages and trace requirements to outputs.

**Week 4 — Integrated system validation:** Review spatial layouts, building/venue use and character circulation across domains.

**Week 5 — Acceptance and expansion handoff:** Publish accepted/revise matrix, evidence, residual risks and next backlog for all four agents.

### QA-2 — QA Supervisor 2
**Week 1 — Foundation design complete:** Verify Stitch's majority clothing design, Motion animation foundation, Torque vehicle foundation and Tracks HIM/HCTA train/transit concept; measure wardrobe coverage and flag unsupported transit counts.

**Week 2 — Detailed specifications and contracts:** Validate garment specs, animation/rig contracts, vehicle specs and transit interfaces.

**Week 3 — First production/vertical slice:** Review representative garment, animation, vehicle and station/train packages.

**Week 4 — Integrated system validation:** Run fit, movement, vehicle/road and train/station interface reviews.

**Week 5 — Acceptance and expansion handoff:** Publish dispositions, wardrobe evidence, transit uncertainties, risks and next backlog.

### QA-3 — QA Supervisor 3
**Week 1 — Foundation design complete:** Verify Route road/traffic-light/navigation design, Ace gameplay foundation, Spark events/social foundation and Lockdown QA framework are buildable and coherent.

**Week 2 — Detailed specifications and contracts:** Validate signal/routing specs, gameplay contracts, event lifecycle and QA traceability.

**Week 3 — First production/vertical slice:** Review representative intersection/signal, gameplay, event and QA packages.

**Week 4 — Integrated system validation:** Run navigation, gameplay, event attendance and traffic/transit scenarios.

**Week 5 — Acceptance and expansion handoff:** Publish dispositions, evidence, risks and next backlog for all four agents.

### Trinity — Overall Coordinator
**Week 1 — Foundation design complete:** Drive all Week 1 foundations to completion: world, city, buildings, characters, majority wardrobe, animation, vehicles, trains/HIM-HCTA, traffic lights/navigation, gameplay, events and QA. Unblock dependencies and escalate creator decisions.

**Week 2 — Detailed specifications and contracts:** Freeze approved baselines and coordinate detailed build specs/interfaces; Week 2 is specification, not another discovery week.

**Week 3 — First production/vertical slice:** Coordinate representative implementation/prototype packages and dependency sequencing.

**Week 4 — Integrated system validation:** Manage cross-system integration and defect closure across all domains.

**Week 5 — Acceptance and expansion handoff:** Audit acceptance, handoffs, version consistency and Week 6+ backlog; report five-week outcomes to creator.

### SCRIBE — Story Director
**Week 1 — Foundation design complete:** Complete narrative foundation: premise, tone, themes, core character motivations, relationship conflicts, opening situation and narrative guardrails; coordinate Vibe's character bible; never invent creator biography.

**Week 2 — Detailed specifications and contracts:** Expand approved foundation into story/character arcs, mission structure, dialogue principles and continuity rules.

**Week 3 — First production/vertical slice:** Produce representative opening sequences, mission briefs, dialogue samples and narrative packages.

**Week 4 — Integrated system validation:** Integrate story with gameplay, NPC schedules, events, camera and wardrobe; validate continuity.

**Week 5 — Acceptance and expansion handoff:** Publish narrative foundation v1, story/character arc bible, opening package, continuity QA and backlog.

### LENS — Cinematic Camera Director
**Week 1 — Foundation design complete:** Complete camera foundation: camera language, perspective rules, gameplay camera modes, shot vocabulary, movement principles, transition grammar and visual storytelling for opening/key city experiences.

**Week 2 — Detailed specifications and contracts:** Specify camera rigs, framing, transitions, input handoff, collision/occlusion and animation/story integration.

**Week 3 — First production/vertical slice:** Produce representative shot lists, scene boards and implementation-ready camera behavior packages.

**Week 4 — Integrated system validation:** Integrate with story, animation, gameplay, events and landmarks; validate readability and player control.

**Week 5 — Acceptance and expansion handoff:** Publish camera foundation v1, opening shot package, camera specs, QA evidence and backlog.

### Nexus — Backend & Multiplayer Support
**Week 1 — Foundation design complete:** Complete backend/multiplayer architecture foundation: system boundary, identity/session, persistence, multiplayer assumptions, authoritative state, service map, security/privacy and $0 constraints. No paid resources or unapproved deployment.

**Week 2 — Detailed specifications and contracts:** Specify API/event contracts, data ownership, persistence schemas, realtime flows, failure handling, access controls and local integration.

**Week 3 — First production/vertical slice:** Produce representative backend package or validated local prototype plan with schemas/API contracts and fixtures.

**Week 4 — Integrated system validation:** Integrate gameplay, NPC/social, events and QA; validate data flow, failure modes, privacy and cost.

**Week 5 — Acceptance and expansion handoff:** Publish backend foundation v1, interface specs, validation evidence and $0-bounded deployment backlog.

## Seven-day execution rhythm

Each agent's individual blueprint contains seven daily tasks for every week. The daily work must directly produce that agent's role-specific Week 1–5 exit outcome above. Day 7 is an evidence-backed milestone review and handoff, not a routine status message. If an agent is blocked, Trinity must re-sequence safe parallel work and escalate the exact missing decision/input.

## Non-negotiables
- Creator approval governs canonical changes.
- No invented geography dimensions, station/neighborhood counts, route alignments, QA names, model IDs, runtime status or test results.
- Preserve six central district boxes and surrounding neighborhood-box rule; total grid dimensions and neighborhood count remain unresolved unless approved source settles them.
- HIM is intercity/regional passenger rail; HCTA is local transit.
- Preserve approved Trapper District / Hustle District contrast.
- Premium realistic quality with performance awareness; no toy-like downgrade.
- $0 spend; no paid APIs/services/tiers.
- No secrets in repository; no self-approval; no silent edits to another agent's domain.

## Reporting contract
Daily report: task IDs; progress; exact paths/commit; evidence/checks; status; partner requests/acks; blockers; next action. Weekly report: milestone against acceptance criteria; deliverable version; QA disposition; unresolved decisions; receiving agents and handoff acknowledgement; next-week backlog. A week is not complete merely because seven days elapsed.
