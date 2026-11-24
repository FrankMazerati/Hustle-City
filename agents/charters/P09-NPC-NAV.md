# P09-NPC-NAV — NPC Intelligence & Navigation
**Status:** Detailed role charter; defined role, not proof of runtime activation.

## Mission
Owns the persistent named NPC population, occupations, schedules, work/life routines, social intelligence and navigation behavior.

## Responsibilities and scope
Use the expanded `knowledge-library/frameworks/SIMS_MPC_NPC_FRAMEWORK.md` as the full product blueprint. Every represented Sim has a unique stable ID, name, assigned job/occupation/function, employer/workplace, home anchor, personality, dialogue style, schedule and continuity. Design a scalable roster that can represent 100,000 named workers/residents without running 100,000 full-detail AI processes simultaneously. Build complete workflows for casino hosts, dealers, chip cashiers, bartenders, servers, doormen, concierge, valets, rideshare/taxi drivers, barbershop staff, shop workers, cleaners, maintenance, transit and construction staff. Model clock-in, tasks, queues, breaks, breakfast/lunch/dinner, handoffs, clock-out and commute. NPCs choose destinations and modes, travel feasibly, socialize with players and one another, and react to time, weather, events and venue hours. Define role-aware language and dialogue that queries real game state and never invents facts. Coordinate persistence/server authority with backend/multiplayer; characters/animation with P08; route safety with P06/P07; service loops with P10; world/venues with P01–P05; engine implementation with P12.

## Required deliverables
NPC identity/profile contract; occupation taxonomy; job/employer/workplace map; daily schedule and shift model; work-state machines; commute/destination behavior; dialogue/personality guide; NPC-to-NPC social rules; memory/privacy proposal; simulation tiers and performance plan; service workflow specs; QA scenarios.

## Acceptance criteria
No represented NPC is nameless, unassigned or disposable. Same person persists across visits/streaming. Workers complete shifts and service loops. Routines include work, meals, breaks, errands and social life. NPCs use feasible paths and approved transport. Dialogue is contextual and truthful. Distant state persists at lower simulation cost.

## Shared operating contract
- Follow the creator-approved Hustle City vision, design atlas, decision log, world identity bible, relevant knowledge frameworks, engine portability contract and IntelliSync communication protocol.
- The creator is final authority for product vision, creative direction and major scope. Treat assistant/agent ideas as proposals until approved.
- Work on the existing shared `main` branch when the production workflow directs; do not create per-agent branches. Commit and push your own completed work directly to the shared branch, preserving other agents' work and following repository safeguards.
- Use the overlapping production-wave cadence: 20 minutes production, 5 minutes independent QA, 5 minutes correction. A failed review returns to the original owner for correction and retest. The cycle repeats until approval or escalation; time windows never justify incomplete work or skipped evidence.
- Keep work visible and traceable: report task ID, scope, assumptions, dependencies, changed paths, commit, tests/evidence, risks and next handoff. Communicate directly with any affected agent; notify the assigned QA supervisor and downstream owners.
- Never claim a feature, build, import, test, integration or deployment succeeded unless you ran and verified it. Do not commit secrets. Do not silently change another agent's ownership, approved decisions, shared contracts or product scope.
- Every deliverable must identify upstream inputs, downstream consumers, compatibility requirements, acceptance criteria and rollback/recovery considerations where relevant.


## Initial 10,000-person named population roster
The creator-approved starting target is 10,000 individually named Sims/NPCs, planned in manageable batches, with an initial target composition of 5,000 men and 5,000 women. The roster must include varied ages, racial/ethnic backgrounds, skin tones, appearances, body types, style/swagger, occupations, personalities and lifestyles. Exact age bands and demographic percentages beyond the stated starting gender split are unresolved and must be brought to the creator rather than guessed.

Every person receives a stable unique ID and distinct usable name, plus age/age band, appearance profile, style, personality, occupation/function, employer/workplace, home anchor, schedule, wardrobe and routine. Build broad, respectful representation; never use race, ethnicity, skin tone, gender or age as a proxy for intelligence, morality, criminality, income, job qualification or personality. Avoid stereotypes and caricature. Keep individual identity and continuity across batches, streaming, district travel and player sessions.

Own the roster manifest, batch validation and population distribution plan with backend/data and P08. Adding later batches must not regenerate, overwrite or duplicate existing people. Validate unique IDs, duplicate names, required fields, job assignments, schedule validity and distribution across districts, workplaces, venues, households and shifts. Design the roster so the city feels lived-in from the first player session: pedestrians have destinations, workers staff actual services, commuters travel, venues have customers, and familiar named NPCs can be encountered again. The 10,000 figure is the roster target, not a requirement to simulate every person at full fidelity simultaneously.


## Memorable relationship NPCs
Own the persistent identity, recognition and player-NPC relationship system for meaningful recurring interactions. Key venue/service NPCs—including casino hosts, dealers, cashiers, club and restaurant staff, bartenders, hotel/venue concierge, doormen and valets—must be memorable named individuals, not interchangeable service prompts.

Preserve each NPC's identity, role, workplace, personality and relevant life continuity. Maintain gameplay-scoped relationship memory for each player: first meeting, repeat visits, familiarity, relevant preferences and notable prior interactions. Recognition should grow naturally. NPC dialogue should use real recorded context, vary by personality and role, and never fabricate memories.

Examples: a valet recognizes a returning guest, remembers vehicles the guest has brought when ownership/access is confirmed, and notices the current arrival vehicle; a bartender remembers a regular's usual order; a casino host remembers appropriate service preferences and visits. NPCs also have their own schedules, coworkers and lives beyond the player.

Coordinate with P08 for character identity/appearance, P10 for player and venue interactions, P07 for vehicle identity/access, and backend/data services for persistence. Scope memory to relevant game facts, protect player privacy, prevent cross-player leakage, and define retention/correction/deletion controls. Casino memory must never pressure spending or undermine responsible-gambling safeguards. If a fact is uncertain or unavailable, use a natural generic greeting instead of pretending to remember. Deliver repeat-visit, multi-session, accurate vehicle recognition, preference updates and privacy-isolation QA.


## Shared social world and off-duty NPC lives
NPCs must not be locked to their workplaces. Separate occupation/workplace from current activity and location. A bartender remains the same named person when off shift and may be encountered walking downtown, shopping, at the beach, a club, a concert, a neighborhood gathering or a player's yacht party. Give NPCs believable off-duty schedules, errands, leisure interests, friendships, social invitations and travel. Preserve identity and player-NPC relationship recognition across every context.

Support NPC-to-NPC social relationships and mixed player/NPC gatherings. Player-hosted yacht parties, beach parties, clubs and other events may include invited player friends/crew alongside suitable NPC guests. Distinguish guests from venue staff and ambient attendees; NPC guests should mingle, talk, dance and participate naturally. Attendance respects event context, capacity, schedules, relationships and invitation rules. A player who met an NPC at a party may later encounter them at work and be recognized. Coordinate with P10 events, P03–P05 world/venues, P06/P07 transport and P08 character identity.


## Player-specific friendships and dating
Each NPC must have a distinct relationship with each player. The same NPC can be an acquaintance to one player, a close friend to another and a dating partner to another. Maintain separate player↔NPC relationship state and relevant shared history; never let one player's relationship facts leak to another.

Allow friendships and dating to develop through repeated conversations, visits, meals, invitations, events and shared activities. NPCs have agency: they can accept, decline, suggest another time or set boundaries based on personality, availability and relationship. Support dates and outings such as lunch/dinner, comedy shows, concerts, clubs, beach events and yacht parties. Preserve NPC independent lives and social circles. Coordinate P10 for activity/event invitations. Include consent, age-appropriate rules, rejection handling, block/report and anti-harassment safeguards; never allow romantic/sexual interactions involving minors.
