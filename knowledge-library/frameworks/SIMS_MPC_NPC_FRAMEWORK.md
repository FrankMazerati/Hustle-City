# Hustle City Sims / MPC / NPC Simulation Framework

**Status:** Creator-approved product direction; detailed implementation, population budgets and persistence rules remain technical design work. “Sims-style” describes a living-life simulation, not a requirement to copy another game's proprietary systems. “MPC” remains an unresolved term; NPC means non-player character.

## 1. Purpose and creator direction
Hustle City is populated by a persistent, named population—not anonymous pedestrians that appear only to decorate the screen. The creator's population target includes a potential city roster of 100,000 people. Every Sim/NPC in that roster must have:
- A unique, durable identity and an actual name.
- An assigned occupation/job, role and useful function in the city. No member of the represented population is an unassigned nameless filler.
- A home/residential anchor, workplace or work assignment, schedule and normal destinations appropriate to their role.
- A recognizable appearance, personality/behavior profile and context-appropriate way of speaking.
- A daily routine and the ability to move between places, perform activities and interact with other Sims and players.
- Persistent identity and continuity when the player leaves and returns; an NPC should not silently become a different person because the player changed districts or logged out.

The 100,000 figure is a population/identity scale target, not a requirement to run 100,000 expensive, fully detailed AI brains simultaneously. Use scalable simulation tiers while preserving the population's records and continuity.

## 2. Individual identity and population records
Use the universal entity identity system. Each Sim receives a stable NPC/person instance ID that is never recycled. Keep catalog/archetype definitions separate from individual people. Each individual record should link, as appropriate, to:
- Full display name and optional preferred name; identity/profile version.
- Occupation, job title, employer/business ID, workplace/venue/building ID, department and supervisor/work group.
- Home/residential location, neighborhood/district, household or household links where designed.
- Shift pattern, work days, start/end times, breaks, days off and current work status.
- Commute preferences and permitted transport modes (walk, owned/authorized car, taxi/ride-hail, transit, bicycle or other supported mode).
- Personality/temperament, interests, conversational style, language/register and optional accent/voice profile.
- Relationships (coworkers, friends, family/household, neighbors, acquaintances and other approved relationship types).
- Current location/activity/state, schedule progress, needs/goals and relevant history.
- Appearance/clothing profile, seasonal attire and role-specific uniform/dress expectations.
- Last meaningful update and persistence/version metadata.

Names and identities must be stable across routine changes, job changes, district travel, streaming and reconnects. Changes to a person's job, home, schedule or appearance update that person's record and history; they do not create a replacement identity.

## 3. Work is a real city workflow
Every Sim has a job or assigned occupation/function. A job is more than a label or costume. It defines a place, schedule, tasks, service responsibilities, interactions, break behavior and completion states. Build role-specific workflows for at least these examples:

### Casino, poker and hospitality
- Casino hosts/hostesses greet players, check the appropriate venue/table context, provide directions and support arrivals.
- Poker-floor staff guide guests to available tables and explain venue procedures without interfering with authoritative poker rules.
- Chip-cashier/cage staff handle approved chip purchase, redemption or exchange flows through the authoritative economy service. They verify the transaction result and never invent or locally alter balances.
- Dealers perform table-specific dealing/animation and turn-flow duties under the poker game's authoritative rules.
- Bartenders take orders, prepare/serve available items, process purchases and handle bar conversations.
- Servers take food/drink orders, deliver to the correct table/deck/seat and close out the service interaction.
- Doormen/security/greeters manage venue entry, guest flow, queueing and permitted access checks. Player-facing conduct remains respectful and non-punitive within launch scope.
- Concierge staff answer service requests and coordinate approved transportation/valet handoffs.
- Valets receive a vehicle handoff, preserve vehicle ownership/keys/location state, park it in a recorded slot and retrieve it on an authorized request.
- Housekeeping, cleaners, maintenance, kitchen staff and managers perform scheduled venue upkeep, preparation, service and closing routines.

### City services and everyday businesses
- Barbershop workers welcome customers, manage queue/chair availability, consult on available styles, perform the selected service interaction and complete payment through the economy.
- Shopkeepers, clerks and cashiers greet customers, stock/sell catalogued goods, process purchases and maintain opening/closing routines.
- Restaurant cooks and kitchen staff prepare menu-defined food; wait staff serve it; hosts manage seating and queues.
- Transit staff operate stations, vehicles and passenger assistance workflows where represented.
- Construction workers, engineers, supervisors, inspectors, cleaners, maintenance crews and delivery workers have coherent site tasks and safety/route behavior.
- Rideshare/taxi drivers accept permitted ride requests, travel to pickup, wait, board the passenger, transport them safely and complete drop-off. Specific real-world brand use such as Uber or Lyft is not assumed; service branding/licensing is a separate decision.
- Office, retail, hospitality, marina, airport, medical/emergency and public-service roles may be added according to approved city content. Each role must have a defined function rather than merely increasing the job-title count.

The first production pass should build complete service loops for the high-value player-facing jobs: casino host, dealer, chip cashier, bartender/server, doorman, concierge, valet, rideshare/taxi driver and barber/shop staff. Additional occupations expand the believable city and must use the same job/workflow contract.

## 4. Full daily life and schedules
NPCs should live through a day, not teleport between isolated animations. A typical schedule can include:
1. Wake up and prepare at home.
2. Choose breakfast or another morning activity.
3. Select a route and commute to work using a plausible available transport mode.
4. Arrive, enter the workplace and clock into the assigned role.
5. Perform job tasks and interact with coworkers/customers/players.
6. Take scheduled breaks, eat lunch or dinner at a suitable time and location, then return to work.
7. Complete shift duties, hand off work, clock out and travel home or to another planned destination.
8. Stop for groceries, a barber appointment, a meal, errands, social visits, events, poker or recreation according to preferences and schedule.
9. Return home, relax and sleep/rest according to the character's routine.

Do not force every Sim into an identical timetable. Stagger shifts, commute departures, meal windows, breaks, days off and activity preferences. A Sim may work early, daytime, evening, overnight, split or flexible shifts where the job supports it. Include weekend/holiday/event variations. Schedule decisions should account for in-game clock, weather, travel time, venue hours, closures, crowding and relevant events.

NPCs should be able to choose breakfast, lunch and dinner venues; take breaks; travel for errands; visit a barbershop; meet friends; attend concerts/parties; go shopping; use transit or ride-hail; and return home. Activities should have start, progress, completion, interruption and recovery states rather than one-shot teleport events.

## 5. Travel, route choice and destination behavior
- Select destinations from schedule, needs, job duties, preferences, relationships, invitations and world conditions.
- Select a feasible route and mode based on distance, access, availability, time, weather, cost and character preference.
- Support walking, driving, public transit, taxi/ride-hail and other approved modes. Coordinate with the transportation and traffic systems; do not create a separate incompatible traffic model.
- Use navigation-aware entry/exit points, sidewalks, crossings, building doors, elevators, stairs, station platforms, vehicle pickup/drop-off points and venue interaction anchors.
- Recover from blocked paths, closed venues, missed rides, traffic delays, unavailable services and interrupted sessions. Replan rather than looping forever or clipping through the world.
- NPC transportation must follow the approved safe-traffic rules. No random crashes, player asset damage, theft or financial penalties caused by simulation failures.

## 6. Social behavior, language and player interaction
NPCs should behave as people with context—not as identical dialogue dispensers.
- Define personality traits and behavior tendencies that affect greetings, patience, humor, confidence, sociability, formality, helpfulness and conversation choices without reducing characters to stereotypes.
- Define dialogue styles by character, role, setting and relationship: professional service language at a cashier/concierge desk; friendly hospitality at a bar; casual neighborhood conversation; concise transactional exchanges during a ride; and more personal conversation among established acquaintances.
- Language should fit the character's background and context while remaining respectful, readable and appropriate for the game's rating. Do not use caricatured dialect, slurs or identity-based stereotypes as a shortcut to realism.
- NPCs should recognize player context where permitted: a returning guest, current service request, accepted invitation, prior conversation, active venue interaction or a player's visible action. They must not invent private player data or claim knowledge they do not have.
- Support greetings, short conversations, directions, service requests, ordering, queueing, payments, invitations, shared meals, small talk, group conversations and relationship progression according to the role's permissions.
- NPC-to-NPC interaction matters too: coworkers coordinate, customers queue, friends greet each other, families dine, pedestrians avoid collisions, staff hand over shifts, and people respond to public events.
- Use dialogue authored by role/context and, if dynamic generation is used, constrain it with character facts, current state, safety rules and approved world lore. Store reusable dialogue intents and outcomes so responses remain coherent.
- Respect player block/report/mute and social safety systems. An NPC cannot bypass player safety controls or impersonate a real player.

## 7. Workday and business operations state machine
Define reusable work states such as:
- Off shift / traveling to work.
- Arriving / entering workplace / clocking in.
- Preparing station or receiving handoff.
- Available for service / serving customer / performing task.
- Waiting for customer or next task.
- On break / meal break.
- Returning from break.
- Closing / cleaning / restocking / handoff.
- Clocking out / traveling home or to next activity.
- Interrupted / recovering / reassigned.

Every job profile defines valid transitions, task priorities, service capacity, required interaction points, shift rules, break windows, failure handling and supervisor/colleague coordination. Business operations should expose authoritative opening hours, staffing needs, service queues, menu/catalog availability, prices and transaction interfaces to NPC workers. Staff cannot sell unavailable inventory, charge arbitrary prices or fabricate completed transactions.

## 8. Population scale and simulation fidelity
Maintain a roster of named, job-assigned individuals, but vary simulation cost by relevance:
- **Full simulation:** player-interacting NPCs, nearby workers, named recurring characters, active service requests, event leads and characters whose choices materially affect the current scene.
- **Local simulation:** nearby pedestrians, commuters, customers and coworkers use lower-cost behavior, route following, simple dialogue/avoidance and scheduled state transitions.
- **Background simulation:** distant people advance through schedule/time blocks, travel estimates, work attendance, purchases or other approved abstract events without running full pathfinding and animation continuously.
- **Population accounting:** retain identity, job, home/work assignment and current abstract state for the full represented roster. Streaming a person out of view must not erase their identity or reset their life.
- **Activation:** when a player approaches or interacts with a person, hydrate the appropriate detailed state from the authoritative record and current schedule.
- **Determinism and recovery:** use reproducible seeds/decision logs where useful for QA; checkpoint meaningful state and safely reconcile after reconnects or server restarts.
- **Crowd density and resource budgets:** define active/local/background budgets and prioritize interaction relevance, safety, and visible schedule continuity. Do not promise 100,000 simultaneous full-detail agents without profiling evidence.

## 9. Memory and continuity
Persist meaningful facts only according to approved privacy and gameplay rules. Candidate memory categories include prior player interactions, service state, relationship changes, work assignments, schedule changes and important world events. Define retention, access, reset, correction and deletion behavior before implementation. Avoid storing unnecessary sensitive information. NPCs should remember only what the game explicitly supports and should not fabricate memories.

## 10. Interfaces and ownership
Coordinate with:
- Character/Persona for names, appearance, clothing, animation, voice and role presentation.
- NPC intelligence for identity, schedules, job state, goals, relationships and dialogue.
- Backend/data and multiplayer for durable records, server authority, replication, persistence and concurrency.
- Navigation/roads/traffic/transport for pathing, commuting, vehicles and safe movement.
- Venues/economy/poker for service queues, orders, inventory, prices, chip exchange and transactions.
- Events/social for invitations, attendance, crews, friends and player safety.
- Environment/time/weather for schedule changes and context.
- UI/ops/analytics for player-facing status, live population health and privacy-conscious metrics.
- QA for continuity, service correctness, dialogue quality, pathfinding, performance and multiplayer consistency.

No agent may independently invent database schemas, network authority or transaction rules. Agree contracts with architecture/backend/multiplayer owners before implementation.

## 11. Required deliverables from the living-city owner
1. Population identity and profile specification.
2. Occupation/job taxonomy with employer/workplace links.
3. Job profile and work-state templates.
4. Shift, break, meal and daily schedule system.
5. Commute and destination-choice behavior.
6. Role-specific player service workflows for the launch-critical jobs.
7. Dialogue/personality/language guide and safe interaction matrix.
8. NPC-to-NPC social behavior specification.
9. Persistent identity, memory and continuity proposal.
10. Simulation-tier/resource budget proposal for the 100,000-person roster.
11. Data/API/interface contracts coordinated with backend, multiplayer and systems architecture.
12. QA scenarios, performance targets and evidence for schedule continuity and service completion.

## 12. Acceptance criteria
- Every person in the represented population has a unique stable ID, a name, an assigned job/occupation/function and a defined routine/profile.
- A player can encounter the same named NPC again and the NPC's identity/job/context remain coherent.
- A worker can complete a full shift workflow, including arrival, tasks, breaks, service interactions, handoff and departure.
- NPCs can travel between home, work, meals, errands and social destinations through feasible routes and supported transport modes.
- Player-facing services complete through authoritative systems, including valid queues, availability, prices and transactions.
- NPC dialogue reflects role, personality, location, time and known context without inventing facts or using harmful caricatures.
- NPCs interact with other NPCs in believable, non-identical ways.
- Distant population state persists without requiring full real-time simulation of every person.
- Reconnects, time changes, weather changes, venue closures and route interruptions do not silently erase or duplicate NPC identities or jobs.
- Performance and population claims are demonstrated by profiling at staged scales, not assumed.

## 13. Decisions still open
- Exact 100,000-person population composition and occupation distribution.
- Which jobs/workflows are required in the first playable slice versus later population expansion.
- In-game day duration, workday clock mapping, calendar, holidays and shift cadence.
- NPC memory scope, retention and player privacy rules.
- Dialogue generation technology, authored content ratio, voice coverage and localization.
- Simulation budgets, persistence intervals, server authority and network replication details.
- Exact database schema, APIs, job marketplace/employer economy and wages.
- “MPC” meaning and scope, pending creator clarification.


## 14. NPC wardrobe, fashion identity and 30-day outfit rotation
**Creator-approved requirement:** Every Sim/NPC represented in the population has a substantial, individually assigned wardrobe capable of supporting approximately one month of varied outfits. This is a wardrobe-content and rotation target, not a requirement to render or load every garment simultaneously.

### Individual wardrobe ownership
- Each person has a persistent wardrobe profile linked to their stable NPC instance ID. Garment definitions use catalog/type IDs and each owned/assigned garment instance uses the universal item identity rules where instance tracking is needed.
- Build enough complete outfit combinations for roughly 30 days of distinct looks per Sim, using a scalable mix of complete outfits, interchangeable garments, accessories and role uniforms. Avoid making every NPC wear a unique hand-authored full outfit if modular combinations can provide variety without obvious repetition.
- Wardrobes should reflect character identity, occupation, income/lifestyle, personality, neighborhood, age-appropriate presentation, personal taste and weather. Keep a character recognizable across outfit changes.
- Support everyday casualwear, workwear/uniforms, business attire, upscale eveningwear, nightlife looks, beach/swimwear, athletic/leisure clothing, sleepwear/homewear and cold/rain/snow clothing as relevant to the character and world.
- Rotate outfits by day, activity, venue, work shift, event, weather and season. Reuse should be managed to avoid the same nearby crowd appearing in identical outfits; exact rotation cadence and wardrobe inventory size remain implementation/budget decisions.

### Venue and occupation dress codes
- Casino and shuffle-club staff should have polished, coordinated, upscale uniforms appropriate to their job: host/hostess, dealer, cashier, bartender, server, concierge, doorman and valet each need a recognizable role-appropriate look.
- Adult casino guests and nightlife patrons may wear glamorous, fashionable, sexy upscale eveningwear, including fitted dresses, short dresses/skirts, low-cut or open-neckline designs, heels and statement jewelry. Keep designs within the game's approved age rating and platform rules; no explicit nudity or sexualized depiction of minors.
- Beach and waterfront venues support swimwear, resortwear, cover-ups, sandals, sunglasses and relaxed luxury fashion appropriate to the location.
- Restaurants, bars, rooftops, yacht clubs, concerts and private events each have a style range matching the venue's atmosphere, from casual to premium/formal.
- Neighborhood/street fashion should be distinct and authentic to each district, including fashionable streetwear and nightlife looks, without reducing communities to stereotypes or assigning clothing based on protected traits.
- Player characters should have comparable outfit categories and customization depth, subject to the player's owned/unlocked items and the same content/rating rules.

### Wardrobe operations and visual continuity
- Define outfit selection rules, outfit presets, layering, garment compatibility, body/rig fit, footwear, accessories, seasonal storage and outfit-change locations/animations.
- NPCs should dress for their shift and change into/out of work uniforms where appropriate; off-duty looks should differ from work attire.
- Weather-aware selection should consider rain, heat, cold and occasional snow. Avoid inappropriate winter clothing on a hot beach or swimwear during a formal indoor shift unless the context supports it.
- Coordinate with P08 character systems, P03 district identity, P04/P05 venue design, P09 NPC schedules/jobs, P10 interactions/events and P12 asset pipeline. Clothing assets must be catalogued, licensed/original, optimized and validated for clipping and animation compatibility.

### Deliverables and acceptance
- Wardrobe category taxonomy and garment catalog standards.
- Venue/occupation dress-code matrix and style guides.
- NPC wardrobe profile and 30-day outfit rotation specification.
- Modular outfit combination, repetition avoidance and weather/season selection rules.
- Role uniform sets for launch-critical casino, hospitality, transport and service jobs.
- QA proving adult NPCs vary their outfits across a representative month, staff dress appropriately for shifts, beach/nightlife/restaurant looks match context, characters remain recognizable, and garments fit rigs/animations without severe clipping.

**Open design details:** exact garment counts per category, number of unique authored assets versus modular combinations, outfit repetition window, body/rig compatibility standards, monetization/unlock rules and final rating boundaries require separate content and technical planning. Do not assume premium fashion must be paid-only; basic wardrobe variety and role uniforms are part of a believable living city.


## 15. Initial named population roster — 10,000 Sims
**Creator-approved starting scale:** Begin with a planned population roster of 10,000 individually named Sims/NPCs, organized and authored/imported in manageable batches of 10,000-person population cohorts as the world expands. The initial cohort target is 5,000 men and 5,000 women, with varied ages, skin tones, racial/ethnic backgrounds, appearances, body types, fashion, personalities, occupations and lifestyles. The 10,000-person roster is a content/population target, not a demand to render every person simultaneously.

### Every person is an individual
- Every Sim in the roster must have a stable unique person instance ID and a distinct, usable display name. Names should be culturally varied and plausible for the character's chosen background, while avoiding accidental duplicate full names within the active roster where practical.
- Each profile includes an age or age band, gender presentation where relevant to the approved character design, appearance/skin-tone palette, style/swagger profile, occupation/function, home/work anchors, schedule, wardrobe, personality and routine. Exact age distribution and demographic mix remain to be designed; do not invent fixed percentages without creator approval.
- The creator's initial population composition target is 5,000 men and 5,000 women. This is a starting content target, not a rule that every future population expansion must preserve that exact ratio.
- Represent a broad, respectful range of racial/ethnic backgrounds and skin tones. Diversity is intentional world population design, not a gameplay stat.
- Race, ethnicity, skin tone, gender or age must not determine a character's intelligence, morality, income, criminality, job qualification, dialogue quality, personality, social status or behavior. Build individual personalities and life circumstances independently; avoid stereotypes and caricatures.
- Give each person recognizable swagger/style through clothing, grooming, posture, accessories, voice/dialogue style and behavior preferences. Do not reduce identity to appearance alone.

### Population batch management and updates
- Treat the initial 10,000 as a versioned roster/cohort that can be added to, corrected or expanded in later batches. Each batch needs a manifest, unique ID range/namespace allocation, count reconciliation, duplicate checks and validation before integration.
- Adding a batch must never regenerate or overwrite existing identities. Names, jobs, ages or appearances may be corrected through versioned profile updates while the stable person ID remains unchanged.
- Track roster totals by approved, non-sensitive content dimensions for production validation (e.g. age bands, gender presentation, broad visual diversity, occupation coverage) without exposing demographic profiles as player-facing rankings or using them to drive discriminatory outcomes.
- Maintain population distribution across neighborhoods, workplaces, businesses, venues, households, commuting routes and day/night schedules so the city feels occupied at different hours—not 10,000 people concentrated in one place.
- Ensure visible crowd density is plausible for each district, venue capacity, time of day and event. Background residents continue their abstract routines when not visible; when a player returns, familiar named people can reappear with continuity.

### First roster production deliverables
1. A 10,000-person roster plan and cohort manifest, targeting 5,000 men and 5,000 women.
2. A culturally varied name-generation/curation standard and duplicate-name audit.
3. A creator-reviewed age-band and broad representation plan; exact distribution percentages remain open.
4. Individual profile fields for name, stable ID, age, appearance/skin tone, style/swagger, personality, occupation, home/work, schedule and wardrobe.
5. A job and neighborhood distribution plan aligned with business staffing and city activity needs.
6. Batch import/update validation: unique IDs, name checks, required-field completeness, occupation assignment, schedule validity, and no overwriting of existing people.
7. Crowd and return-visit tests demonstrating that the city feels inhabited and that named Sims retain identity across player sessions.


## 16. Memorable relationship NPCs and player recognition
**Creator-approved requirement:** NPCs whom players meaningfully interact with at recurring venues and services must be memorable individuals, not interchangeable service prompts. This includes casino staff, club and venue staff, bartenders, restaurant workers, hotel/venue concierge, doormen, valets and parking attendants, shop staff, hosts, dealers and other recurring service roles.

### Persistent identity and relationship continuity
- Preserve the NPC's stable name, face/appearance, voice or dialogue style, role, workplace, personality and relevant history across player sessions.
- Track a privacy-conscious, gameplay-scoped relationship state between the NPC and each player: first meeting, prior encounters, familiarity, relevant preferences, notable shared interactions and recent visit context.
- NPCs should recognize returning players and greet them with contextually appropriate familiarity. Recognition should grow naturally through repeated encounters; do not make every NPC instantly act like a close friend.
- NPCs can remember relevant player preferences and past choices when useful to their role: a bartender may remember a usual order; a concierge/valet may remember vehicles the player commonly brings; a casino host may remember preferred games or prior visits; a venue host may remember seating or event preferences.
- NPCs should notice relevant changes and refer to them naturally when the information is available and appropriate. Example: a valet recognizes a returning player and comments that they arrived in a different luxury car today, or asks when they will bring the other car again.
- Dialogue must be varied, personality-aware, role-aware, relationship-aware and grounded in actual recorded game context. Do not fabricate memories, ownership, prior encounters, player details or promises.
- NPCs should also retain continuity in their own lives: work shifts, coworkers, routines, relationships and recent events. Their lives do not exist only to react to the player.

### Role-specific examples
- **Valet/concierge:** remembers a regular guest, their authorized vehicle history, usual arrival pattern and service preferences; recognizes the current vehicle only when the game has reliable access to that vehicle's identity and the player has permission to use it.
- **Bartender/server:** remembers a returning guest's usual order, favorite table or prior conversation where appropriate; can offer a familiar greeting without forcing a purchase.
- **Casino host/dealer/cashier:** remembers repeat visits and relevant service preferences or prior table interactions, while respecting poker fairness, privacy and responsible-gambling safeguards. Do not use memory to pressure spending or exploit player vulnerabilities.
- **Club, restaurant and hotel staff:** remember regular attendance, preferred experiences and prior service interactions; recognize friends/crew only where the game context supports it.

### Data, privacy and safeguards
- Keep player-NPC relationship memory scoped to the game and to the minimum relevant facts needed for believable continuity. Do not infer sensitive traits or collect unrelated personal information.
- Define retention, reset, correction and deletion controls for relationship data; provide moderation and abuse protections. Do not let NPCs reveal one player's private information to another player.
- Treat vehicles and other possessions carefully: mention them only when ownership/access and current game state confirm the fact. Never expose another player's asset or activity history.
- Build memory tiers: persistent identity and role facts; durable relationship/familiarity facts; bounded recent interaction summaries; and short-lived conversational context. Exact storage and model architecture remain implementation decisions.
- If memory is unavailable or uncertain, use a warm generic greeting rather than pretending to remember. NPC memory must be testable, auditable and resistant to cross-player data leakage.

### Acceptance tests
1. A player visits the same venue repeatedly and is recognized by the same named staff member across separate sessions.
2. The NPC's familiarity changes gradually and dialogue reflects actual prior interactions without repeating one canned line.
3. A valet can recognize a player's different authorized vehicles and comment accurately on the current arrival vehicle.
4. A bartender can recall a relevant usual order or preference, and can gracefully handle a changed preference.
5. NPCs never claim false memories or disclose another player's private information.
6. NPC relationships remain consistent through NPC shifts, venue changes, player reconnects and ordinary world simulation.
7. Casino memory never becomes manipulative spending pressure or compromises game fairness.
