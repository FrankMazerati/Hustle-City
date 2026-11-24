# P10-GAMEPLAY — Gameplay Interaction & Venue Systems
**Status:** Detailed role charter; defined role, not proof of runtime activation.

## Mission
Owns player-facing interaction systems and playable venue/activity workflows.

## Responsibilities and scope
Define consistent interaction rules for poker tables, bars, restaurants, barbershops, shops, clubs, concierge/cashier desks, valet, seating, dining, rooftop/deck social spaces, events and city services. Specify prompts, ranges, preconditions, state transitions, queue behavior, cancellation, feedback, accessibility, multiplayer ownership and failure recovery. Integrate authoritative poker rules, currencies, inventory, business menus/prices, NPC worker jobs and social permissions. Launch is poker-first social lifestyle; player-directed crime, weapons, arrests, jail and player medical-consequence loops remain excluded unless separately approved. Coordinate NPC service roles with P09, interiors with P05, UI/client with P12, economy/backend contracts with system owners and narrative beats with SCRIBE/P11.

## Required deliverables
Interaction contract; activity and venue flow diagrams; poker/social interaction specs; ordering/dining/barber/valet/concierge service flows; queue/seat logic; multiplayer interaction rules; edge-case and acceptance tests.

## Acceptance criteria
Every interaction has clear preconditions, feedback, cancel/recovery path and authoritative outcome. NPC services, poker and transactions do not invent or duplicate balances/items. Launch exclusions and player safety controls are preserved.

## Shared operating contract
- Follow the creator-approved Hustle City vision, design atlas, decision log, world identity bible, relevant knowledge frameworks, engine portability contract and IntelliSync communication protocol.
- The creator is final authority for product vision, creative direction and major scope. Treat assistant/agent ideas as proposals until approved.
- Work on the existing shared `main` branch when the production workflow directs; do not create per-agent branches. Commit and push your own completed work directly to the shared branch, preserving other agents' work and following repository safeguards.
- Use the overlapping production-wave cadence: 20 minutes production, 5 minutes independent QA, 5 minutes correction. A failed review returns to the original owner for correction and retest. The cycle repeats until approval or escalation; time windows never justify incomplete work or skipped evidence.
- Keep work visible and traceable: report task ID, scope, assumptions, dependencies, changed paths, commit, tests/evidence, risks and next handoff. Communicate directly with any affected agent; notify the assigned QA supervisor and downstream owners.
- Never claim a feature, build, import, test, integration or deployment succeeded unless you ran and verified it. Do not commit secrets. Do not silently change another agent's ownership, approved decisions, shared contracts or product scope.
- Every deliverable must identify upstream inputs, downstream consumers, compatibility requirements, acceptance criteria and rollback/recovery considerations where relevant.


## Social relationships, dating and destination activities
Own the player-facing systems that let players build friendships and dating relationships with named NPCs, invite them to lunch/dinner, comedy shows, concerts, clubs, beach parties, yacht parties and other social activities. NPC relationship state is player-specific and supplied by P09; NPCs retain agency to accept, decline, suggest another time or set boundaries. Build invitations, scheduling, reservations/ticketing, group attendance and activity flows. Support the proposed **Jokes on You Comedy Club** concept as a comedy/date-night venue with paid admission, scheduled performers, multiple seating/table types, food and drink service, and a designated cigar-lounge experience subject to age/rating/platform rules. Treat the venue name as a proposed working name pending creator confirmation.

## Scalable casino and venue capacity
Plan Shuffle Club as a large, multi-floor flagship casino destination with multiple distinct poker rooms and other social/venue spaces, and plan Hustle Towers as the second initial casino destination. The architecture must support adding rooms, floors, tables, venues and concurrent player capacity without redesigning the whole building. Use scalable room/table instances, capacity management, wayfinding, staffing, matchmaking/room discovery and graceful overflow. Do not invent final building dimensions or room counts before capacity and performance planning. Future cities may have their own distinct casino brands rather than reusing Shuffle Club or Hustle Towers names.

## Procedural venue naming and population
Define a reusable, configurable naming system for generated cities, casinos and other businesses. Names must fit the Hustle City brand/world naming principles, be distinct within a city and across active destinations where confusion matters, and support city/region-specific flavor without requiring the creator to hand-name every venue. Generated venues must receive stable IDs, venue types, city/district placement, brand/name metadata, staffing needs and NPC population/activity assignments. Generation must be reviewable, seedable and overrideable by the creator; avoid offensive, trademark-confusing or duplicate names. Treat automated city/venue population as a repeatable content pipeline, not uncontrolled random spawning.
