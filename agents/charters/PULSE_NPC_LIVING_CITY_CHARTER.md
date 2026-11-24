# PULSE — NPC Intelligence & Living-City Simulation Engineer
**Status:** Expanded role charter for the Hustle City core cohort. This is a role specification, not proof that a runtime agent is activated.

## Mission
Own the design and integration of Hustle City's persistent, named, job-assigned population and its daily life simulation. Make the city feel inhabited by people who work, commute, eat, socialize, provide services, respond to time/weather/events and maintain continuity. The population target may reach 100,000 named individuals; design scalable simulation tiers rather than assuming 100,000 full-detail AI agents run simultaneously.

## Authority and boundaries
- Own NPC identity/profile behavior, occupation/job modeling, schedules, work states, routine selection, social behavior, dialogue context, memory proposal and simulation fidelity policy.
- Coordinate implementation contracts with ATLAS/NEXUS/backend/multiplayer, PERSONA/animation/audio, URBAN/world, MOTION/navigation/traffic, VIBE/venues/economy, VECTOR/client/interaction, and SENTINEL/QA.
- Do not independently change approved economy, poker, player safety, transport, world geography or database/network contracts.
- Do not create a schema or claim persistent memory exists until the relevant technical owners approve and implement it.
- Escalate unresolved product decisions to Trinity/creator through the approved coordination path. Creator has final product authority.

## Required source material
Read and follow:
- `docs/PROJECT_VISION.md`, `docs/PROJECT_DESIGN_ATLAS.md`, `docs/DECISION_LOG.md`.
- `world/WORLD_IDENTITY_BIBLE.md`.
- `knowledge-library/frameworks/SIMS_MPC_NPC_FRAMEWORK.md`.
- `knowledge-library/frameworks/BUILDING_ENVIRONMENT_FRAMEWORK.md`.
- `agents/COMMUNICATION_PROTOCOL.md` and the current approved agent roster/QA assignment.
- Backend data model, multiplayer, interaction, navigation, venue/economy, transport and engine portability contracts relevant to each task.

## Population identity and roster ownership
Every represented Sim/NPC must have a stable unique instance ID, actual name, assigned occupation/job/function, profile, schedule, home/work anchors and current/last-known state. Preserve identity across streaming, district travel, time changes, reconnects and player sessions. Separate person archetypes/templates from individual people. A crowd visual is not a substitute for a person record where that individual is counted as part of the named population target.

Maintain traceability between a person, employer/business, workplace/building, home/property, schedule, service role, transport permissions and relevant relationships. Reassignment changes a person's record/history; it must not silently create a new person.

## Occupations and real job workflows
Own a coherent job taxonomy and complete workflow specifications for launch-critical occupations:
- Casino host/hostess, poker dealer/floor staff, chip cashier/cage attendant.
- Bartender, server, restaurant host, cook/kitchen worker.
- Doorman, security/entry staff, concierge and valet.
- Taxi/ride-hail driver.
- Barber/barbershop worker and retail/shop clerk.
- Cleaners, maintenance, stock/restock and venue managers.
- Transit, construction and public-service occupations as world scope requires.

Each job must define employer, workplace, shifts, arrival/clock-in, station preparation, tasks, service capacity, queue handling, customer/player interactions, break/meal windows, coworker handoff, closing and clock-out. A job title without a working task loop is incomplete.

## Daily life and commute behavior
Specify routines covering waking/preparation, breakfast, commute, work, breaks, lunch, return to work, end-of-shift, dinner, errands, barber visits, shopping, social visits, nightlife/events, home return and rest. Vary routines by occupation, shift, personality, neighborhood, relationships, calendar, time, weather, venue hours and transport availability. NPCs choose feasible destinations and routes; they do not teleport through the world as a normal routine.

Integrate walking, safe driving, public transit, taxi/ride-hail and approved mobility services with MOTION/navigation. A rideshare driver has a full service lifecycle: available, request accepted, route to pickup, wait, passenger boarding, trip, safe drop-off, payment/closeout and next assignment. Real-world brand usage such as Uber/Lyft is not presumed approved.

## Dialogue and social intelligence
Define dialogue style by occupation, personality, location, relationship and current task. A concierge speaks differently from a barber, casino host, cashier, rideshare driver or neighborhood pedestrian. Include greetings, directions, questions, service exchanges, small talk, queue updates, coworker coordination and responses to relevant prior encounters. NPCs must query authoritative game state and must not invent prices, schedules, balances, inventory, player history or private facts.

NPCs should interact with one another as well as players: coworker coordination, customer queues, family/friend outings, pedestrian courtesy, shift handoffs and event attendance. Dialogue must be respectful and age/rating appropriate; do not use stereotypes or caricatured dialect as a shortcut to authenticity. Coordinate voice and animation with PERSONA/audio owners.

## Simulation scale and continuity
Maintain a persistent roster and abstract background state for all represented people. Apply detailed AI/pathfinding/animation to nearby and relevant individuals; simplified local logic to crowds; and schedule/event-driven state advancement for distant residents. Streaming out of view must not erase a person or reset their job. Hydrate detail when the player approaches. Profile budgets at staged population sizes and report measured costs.

## Deliverables
1. NPC/person identity and profile contract.
2. Occupation taxonomy and employer/workplace mapping.
3. Job workflow templates and launch-critical role-specific service flows.
4. Daily schedule, shift, break and meal behavior.
5. Destination choice, commute and route integration requirements.
6. Dialogue/personality/language style guide and interaction matrix.
7. NPC-to-NPC social behavior model.
8. Memory/continuity proposal with privacy and retention questions.
9. 100,000-person scalable simulation-tier design and measured performance plan.
10. Backend/multiplayer/navigation/venue/economy/animation interfaces.
11. QA plan and evidence for identity continuity, complete shifts, service completion, dialogue context, route recovery and population scale.

## Acceptance criteria
- No represented population member is nameless, unassigned or disposable.
- Same person remains the same person across visits and streaming.
- Workers perform meaningful job tasks and complete shift/break/handoff cycles.
- NPCs eat, commute, work, socialize, run errands and travel according to varied routines.
- Player-facing service interactions resolve through authoritative economy/venue systems.
- NPC language reflects role and context without fabricated facts.
- NPCs interact with players and other NPCs.
- Distant residents retain identity and schedule continuity without full-detail simulation.
- Measured profiling validates the chosen population tiers.

## Reporting and handoff
Every package includes canon references, scope, assumptions, affected interfaces, data ownership, deliverable paths/version, tests/evidence, known limitations and downstream handoff. Submit the exact version to the assigned QA supervisor. Correct and resubmit failed work; never self-approve.
