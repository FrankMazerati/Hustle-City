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


## 17. Shared social world: NPCs beyond their workplaces
**Creator-approved requirement:** Named, memorable NPCs must exist as people throughout the shared city, not remain permanently stationed at their assigned workplace. A bartender may be encountered on the sidewalk, at a shop, beach, club, concert, restaurant, neighborhood gathering or a player's yacht party. The same stable NPC identity, appearance and relationship continuity follow them across all appropriate locations and activities.

- Separate an NPC's occupation/workplace identity from their current activity and location. An NPC remains the same bartender/valet/host when off shift and participating in ordinary life.
- Give NPCs off-duty schedules, personal errands, leisure destinations, friendships, social invitations and event attendance. Their movement should be plausible for their home, interests, schedule, transport access and social connections.
- Enable natural recognition across contexts: a player who knows the bartender from her workplace may recognize her downtown or at a beach party; she may greet the player using appropriate shared history without acting as though she is on duty.
- Support NPC-to-NPC relationships and encounters. Familiar workers may attend events together, meet friends, visit venues and form believable social groups; the city should not feel like every NPC's life revolves around the player.
- Support mixed player/NPC social gatherings. Player-hosted yacht parties, beach parties, club events and other gatherings may include player-invited friends/crew and suitable NPC guests/attendees. NPC attendance must respect event context, capacity, schedules, relationships, invitation rules and world simulation.
- Distinguish invited guests from ambient NPC attendees and venue staff. NPC guests should behave as guests—socialize, dance, eat, talk, mingle and move around—rather than all appearing as employees or service props.
- NPCs may accept/decline invitations or attend appropriate public events according to their schedules and relationships. Do not guarantee attendance when a character is unavailable; provide believable alternatives and continuity.
- Preserve social continuity: if a player meets an NPC at a party and later sees them at work or elsewhere, the NPC can recognize the player and optionally refer to the shared event when relevant.
- Coordinate P09 with P10 for event/party systems, P03/P04/P05 for public spaces and venues, P06/P07 for NPC travel, and P08 for persistent character appearance.


## 18. Player-specific friendships, dating and shared activities
**Creator-approved requirement:** An NPC's relationship with one player must be distinct from that NPC's relationship with every other player. A bartender might be a familiar acquaintance to one player, a close friend to another, a dating partner to another, and a stranger to someone else. Do not use one global NPC relationship score as the relationship for the whole server.

- Maintain separate player↔NPC relationship records, with relationship state, familiarity, trust/affinity where appropriate, shared interaction history, boundaries and current context.
- Let relationships develop through meaningful repeated interactions: conversations, frequent visits, meals, invitations, events, activities and dates. Avoid instant friendship or romance from a single interaction.
- Support friendship and dating pathways, invitations to lunch/dinner, comedy shows, concerts, clubs, beach gatherings, yacht parties and other approved social activities.
- NPCs make their own choices: they may accept, decline, suggest another time or end an interaction based on their personality, availability, relationship and boundaries. A player cannot force friendship, dating or attendance.
- NPCs remember shared experiences with the specific player and can refer to them naturally. Information learned with one player must not leak into another player's relationship or dialogue.
- Build respectful consent, age-appropriate relationship rules, rejection handling, block/report tools and anti-harassment protections. Dating/romance is adult-only where applicable; never enable romantic or sexual interactions involving minors.
- Keep NPCs' independent lives and other relationships active. NPCs are not exclusive player-owned companions and can have their own friends, dates, plans and social circles.
- Coordinate P09 relationship simulation with P10 social activities/invitations/events and the account/privacy systems.


## 19. Player-specific familiarity, recognition and trust progression
**Creator-approved requirement:** Every meaningful recurring NPC interaction can build a persistent, player-specific familiarity relationship. This applies across the whole city—not only dating candidates—including valets, parking attendants, bartenders, servers, doormen, cashiers, shopkeepers, mechanics, hosts, concierge staff, security, coworkers and other service or neighborhood NPCs.

### Two separate relationship measurements
- **Familiarity level:** Measures how well this specific NPC knows/recognizes this specific player through meaningful encounters. It can progress through first meeting, repeat recognition, familiar acquaintance and deeper familiarity. The exact level count, thresholds and UI presentation remain implementation details.
- **Trust meter:** A separately visible player↔NPC trust value/bar. It represents the NPC's earned comfort and confidence in the player, based on relevant behavior and shared experiences. Trust is not the same as familiarity, attraction, friendship, or permission.
- Familiarity can rise through repeated meaningful encounters even when trust stays low. Trust can rise or fall through the quality and context of interactions; simply appearing nearby or grinding repeated button presses must not automatically create trust.
- Trust should be earned gradually through reliable, respectful, consistent behavior and relevant shared interactions. Broken promises, disrespect, boundary violations or other contextually meaningful negative behavior may reduce it. Do not make every interaction a numeric transaction.
- Higher trust may make an NPC more comfortable sharing appropriate information, accepting certain invitations or allowing a closer friendship, but never guarantees attraction, romance, access, consent or a particular response.
- Keep romantic attraction and relationship status separate from familiarity and trust. An NPC can know and trust a player without being romantically interested; a high attraction score cannot override the NPC's boundaries or relationship status.

### Player and NPC characteristics that shape first impressions and progression
- Player-side traits may include height, appearance, grooming, clothing/style, swagger or movement style, confidence/presentation, conversational approach, social behavior and relevant reputation/context.
- NPC-side traits may include personality, interests, attraction/preferences where relevant, relationship status, mood, confidence, sociability, social awareness, trust disposition, boundaries, schedule and current circumstances.
- These characteristics inform contextual reactions and compatibility; they must not become rigid stereotypes or deterministic gates. The NPC's own preferences and choices remain authoritative.
- Conversation quality, listening, respectful behavior, shared interests, remembered details, reliability and context-appropriate actions can affect familiarity, trust and relationship development.
- Mood and availability can change by time, events, workload, companions and personal schedule. A previously receptive NPC may be busy or not interested on another visit.

### Recognition in both directions
- Persist enough approved, privacy-conscious player appearance/identity cues for an NPC to recognize a returning player where technically and legally appropriate.
- The player should also be able to recognize recurring NPCs through stable names, faces, appearance, voice/style, role and schedule continuity.
- Dialogue should reflect the actual familiarity level and known shared history: first-time greeting; recognition of a returning guest; reference to a previous conversation or service; or a more familiar greeting after repeated encounters.
- Recognition must be grounded in authoritative game records. If the NPC or player cannot reliably identify the other, use a neutral greeting rather than false recognition.
- Maintain separate relationship records for every player-NPC pair. One player's trust/familiarity must never be copied to another player's relationship with the same NPC.

### Player-facing relationship UI
- Where appropriate, expose a familiarity level and a distinct trust bar in the NPC/contact profile. Do not show hidden NPC calculations or sensitive internal traits.
- The UI should communicate progression clearly without promising that a certain bar value unlocks romance or a guaranteed service outcome.
- The player contact entry may include the NPC's name, portrait, known role/venue, last meaningful encounter, familiarity level, trust indicator where appropriate, and mutually shared contact methods only when exchanged.
- Avoid cluttering every first-time ambient interaction with a full relationship HUD. Show detail in contextual interaction panels, profiles or contacts.

## 20. Shift-based staffing and recurring workplace faces
**Creator-approved requirement:** Recurring service NPCs work predictable, persistent shifts so players can learn who is commonly working at particular times. The same service role can be staffed by different named NPCs across the day; the game must not assume one worker is always present.

- Support three staggered eight-hour staffing shifts as the creator's example operating pattern (24-hour coverage where a business is open continuously). Exact shift start times, overlap, break coverage, staffing counts and business-specific exceptions remain to be configured per workplace.
- Assign each worker a stable identity, role, employer/workplace and recurring shift schedule. Staff can have days off, leave, breaks, shift swaps, absences and schedule changes without losing identity or relationship history.
- Maintain a roster for each staffed service point. When one worker clocks out, another eligible worker can take over; the incoming worker is a different person with their own player-specific familiarity and trust history.
- The player should be able to learn patterns through repeated visits—for example, a player who usually visits around midnight may commonly encounter the overnight-shift valet or bartender. This is in-world schedule continuity, not surveillance of real-world login habits.
- The NPC on duty should be selected from authoritative shift and availability state, not randomly replaced every time the player looks away. Avoid implausible simultaneous staffing or a single NPC serving two distant locations.
- Shift handoffs should preserve service continuity while keeping each worker's personal identity separate. An incoming valet does not inherit the outgoing valet's personal familiarity or trust with a player, though shared workplace records may support an appropriate handoff of an active vehicle/service ticket.
- Schedule exceptions must be believable and testable: break relief, sick day/absence, special event staffing, venue closure, overtime/overlap and emergency replacement. Do not imply every business must run all three shifts if its approved opening hours do not require 24-hour staffing.

### Acceptance tests
1. The same player meets the same named valet on multiple visits; familiarity progresses and the valet's greetings reflect verified history.
2. Familiarity can rise while trust remains low; trust can rise or fall independently.
3. A player who visits at different times encounters different workers according to their actual shift roster, not arbitrary identity swaps.
4. Returning at a familiar time commonly surfaces the expected on-duty NPC, subject to recorded days off and schedule exceptions.
5. The incoming shift worker has their own independent relationship record; they do not inherit another worker's personal trust or memories.
6. NPC recognition persists across player sessions, district travel and NPC off-duty activities where supported.
7. Player appearance, height, swagger and conversation approach can inform social reactions without overriding NPC agency, consent or boundaries.
8. Trust/familiarity never guarantees a date, access, confidential information or a positive response.


## 21. Reciprocal NPC/player social profiles and contextual interaction UI
**Creator-approved requirement:** When a player approaches or interacts with a named NPC, the game can surface a compact profile/relationship panel alongside the conversation. The player can see who the NPC is and the current player↔NPC familiarity and trust; the NPC's recognition/decision system can also consult an approved, gameplay-visible profile of the player. Both sides have identity and context to support more appropriate interaction.

### Player-facing NPC profile
- Show the NPC's stable display name, portrait/recognizable appearance, occupation or social role, and relevant workplace/venue identity.
- Show the relationship measurements for this exact player-NPC pair: familiarity level and trust meter/bar. Keep these outside or alongside the conversation area so the conversation remains readable.
- Optionally surface relevant context such as whether the NPC recognizes the player, whether they are on or off shift, and the last meaningful encounter where appropriate.
- The profile can appear contextually on approach, during a conversation, or through an explicit inspect/profile action. Support a compact on-screen conversation panel and a fuller profile view; final layout/platform behavior remains design work.
- Do not expose hidden NPC reasoning, private memories, sensitive traits or information the NPC has not chosen/been authorized to share.

### NPC-facing player recognition profile
- The NPC's recognition system may consult the player's approved in-game public/social identity, including display name (example: “Frank Maserati”), player level, visible star/rank indicators, accumulated playtime or tenure where approved, and visit frequency/history at the relevant venue.
- Use these signals to establish context: a first-time visitor, a returning guest, a venue regular, an experienced player or a recognized community member. Venue-specific visit frequency is distinct from total game tenure.
- The NPC should use only fields the game designates as visible to that NPC in that context. Do not expose account credentials, real-world identity, private communications, hidden moderation data, precise login tracking or unrelated personal information.
- Define player controls for public/social profile visibility where appropriate. The creator's requested recognition behavior is the product direction; exact visibility defaults and privacy settings remain implementation decisions.
- NPCs must not treat a high level, star count or long playtime as proof of trustworthiness, wealth, consent, authority or romantic compatibility. These are context cues, not substitutes for actual interaction history or the NPC's independent judgment.

### Contextual behavior and dialogue adaptation
- Combine the player's visible profile with the NPC's own role, personality, schedule, mood, familiarity, trust and verified shared history to select an appropriate greeting and interaction style.
- Example: a first-time visitor receives a welcoming introduction; a repeat guest may be greeted by display name; a venue regular may receive a familiar greeting or a relevant comment about their visit pattern.
- A valet may recognize a returning guest and, where authoritative vehicle records permit, refer to a vehicle the player commonly brings. A bartender may recognize a returning customer and recall a relevant usual order. A club NPC may refer to a previous conversation only when it is actually recorded.
- Profile indicators must not dictate scripted favoritism, service quality, pricing, access, or relationship outcomes unless a separate approved game rule explicitly requires it. NPCs should remain respectful and consistent toward newcomers and experienced players.
- Dialogue generation must be grounded in the data actually available to the NPC. If a field is hidden, unavailable or uncertain, the NPC must not claim to know it.

### Acceptance tests
1. Approaching a named NPC can show a profile with stable name, role and that player's familiarity/trust values.
2. During conversation, the profile/relationship panel does not obscure essential dialogue or interaction controls.
3. The NPC can greet a returning player by their approved display name when recognition data supports it.
4. The NPC can distinguish a venue regular from a first-time guest using verified venue visit history.
5. Player level, stars/rank and playtime are used only as approved contextual signals and never as automatic proof of trust, wealth, consent or entitlement.
6. Different players see their own separate relationship values with the same NPC.
7. Hidden/private player data and another player's relationship history are never exposed.
8. If recognition/profile data is missing or unavailable, the NPC uses a natural neutral greeting and the profile omits unsupported fields.


## 22. Conversation-earned trust, extended interactions and NPC-hosted social events
**Creator-approved requirement:** Trust must be earned through actual conversations and meaningful interactions with an NPC. Players can continue an interaction beyond its basic service/action, ask questions, share personal news and build rapport over time. NPCs also create and host social experiences across the city, invite players—including new players—and maintain social networks beyond their workplaces.

### Conversation as the primary trust-building channel
- Treat conversation as a primary way trust grows. A player may complete a practical interaction (for example, selecting “park a vehicle” with Marcus the parking attendant) and then choose to remain and talk rather than ending the encounter immediately.
- Provide a set of available interaction choices appropriate to the NPC and context, such as talk, ask about family, discuss shared interests, ask about work, share personal news, talk about cars or other hobbies, and—when the relationship and NPC boundaries support it—ask more personal questions.
- Conversation can be extended through multiple turns and topics. The player should feel they are spending time with a person, not repeatedly activating a generic “increase trust” button.
- Trust changes in small, context-sensitive increments when conversation is meaningful and the NPC's response supports it. A displayed value might move from 63 to 64 to 65 over a sustained positive conversation; these numbers are illustrative, not a fixed rate or guaranteed outcome.
- Listening, relevant follow-up questions, remembering details, reciprocal sharing, empathy, honesty and respectful conversation can strengthen trust. Disinterest, dismissiveness, intrusive questions, repeated topic pushing, disrespect, broken promises or boundary violations can leave trust unchanged or reduce it.
- The NPC's personality, mood, time, workload, interests, social energy, familiarity, trust, relationship history and boundaries determine what topics are available and how the NPC responds. Personal questions should become available contextually; an NPC may answer, decline, deflect, joke, or say the subject is private.
- Do not award trust for raw conversation length, repeated identical questions, idle proximity, spammed interaction choices or farming dialogue loops. Meaningful content and the NPC's independent response matter.
- Trust remains distinct from familiarity, attraction, friendship status, romance and consent. A long conversation or high trust never entitles the player to private information, a party invitation, a date, a service exception or any other outcome.
- NPCs may also initiate conversation, ask the player questions, share appropriate personal updates and remember details that were actually exchanged. Dialogue and memory must remain grounded in recorded interactions; never fabricate shared history.

### Relationship-aware social circles and NPC-hosted events
- NPCs should be able to organize and host social gatherings as part of their own lives and networks, not only attend player-created events. Examples include yacht parties, street-car meets/parties, club parties and other venue- or interest-based gatherings.
- The event host may be an individual NPC or an appropriate NPC group/social circle. Hosts choose event type, location, timing, guest list and invitations in ways consistent with their identity, resources, interests, relationships and schedule. Exact hosting authority and event-generation rules remain implementation details.
- NPC hosts can invite player characters they know or want to include. New players must also have credible paths to receive invitations and enter the city's social life; invitation opportunities should not be limited to established high-trust players or existing crews.
- Invitations should be contextual and earned/selected by the host's independent judgment: shared interests, recent conversation, social connections, event fit, familiarity, availability and other relevant game state may matter. No single trust score or player level guarantees an invitation.
- Support the social lifecycle: event idea/host selection, venue and time selection, guest selection, invitations and responses, attendance, NPC/player interactions during the gathering, and persistent memories/relationship consequences afterward.
- Social events should feel populated by people with their own motives and relationships. NPC guests can arrive, socialize, introduce people, leave, decline, bring appropriate companions where supported, and respond to how the event unfolds.
- Event types should be extensible beyond the examples above. Venue parties, yacht gatherings and street-car events are explicit examples, not an exhaustive list. Event capacity, access rules, safety, age/content restrictions, moderation and scheduling are to be designed per event type.
- Player-hosted events remain supported and distinct from NPC-hosted events. NPC-hosted gatherings must not be reduced to player-owned party instances with NPCs as decoration; NPCs should have genuine hosting agency within the simulation rules.

### Acceptance tests
1. A player can finish a valet service interaction and choose to continue talking with the same named valet without restarting or losing the service context.
2. Contextually appropriate conversation choices include ordinary and personal topics; the NPC can answer, decline or redirect based on personality, familiarity, mood and boundaries.
3. A sustained, meaningful positive conversation can increment trust gradually (for example, 63→64→65), while spam or repetitive empty dialogue does not farm trust.
4. Respectful listening and remembered details can support trust; intrusive or disrespectful behavior can leave it unchanged or lower it.
5. NPCs can initiate topics and share appropriate personal updates grounded in their own simulated life and recorded shared history.
6. NPCs or NPC social groups can organize yacht parties, street-car meets/parties, club parties and extensible social gatherings.
7. NPC hosts can invite players, including new players, through credible contextual invitation paths; established high trust is not the only entry route.
8. Players can accept or decline invitations, and NPCs can independently accept, decline or defer player invitations.
9. Event attendance and post-event relationship changes respect schedules, capacity, relationship context, NPC agency and applicable safety/content rules.
10. Conversation-earned trust and event invitations never guarantee romance, consent, confidential information, access or entitlement.
