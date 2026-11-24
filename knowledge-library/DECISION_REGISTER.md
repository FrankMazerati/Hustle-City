# Hustle City Knowledge Decision Register

This register captures decisions promoted through the knowledge library. The existing project decision log remains part of the historical record.

## 2026-11-22 — Transportation authority split
- **Status:** APPROVED — creator explicitly confirmed names and responsibilities.
- **Hustle International Metro (HIM):** Intercity passenger rail connecting Hustle City with other cities and regions. Examples discussed: Chicago, Atlanta, New York and Florida destinations. HIM is the intercity arrival system for the opening sequence.
- **Hustle City Transit Authority (HCTA):** Local passenger transit connecting the six central districts, neighborhoods and surrounding/outer areas.
- **HCTA rail environments:** Elevated, underground and street-level operation.
- **Outer neighborhood access:** Every designated outer neighborhood box gets an HCTA station or defined passenger connection. Selected locations may interchange with HIM; not every neighborhood requires a full intercity platform.
- **Player journey:** HIM arrival → terminal/interchange → HCTA → outer neighborhood → destination. The reverse journey must also work.
- **Open:** Exact line count, routes, colors, station locations/names, terminal count, train technology and construction phasing. Earlier suggestions of two mixed-mode lines are proposals, not locked decisions.

## 2026-11-22 — City composition and visual identity
- **Status:** APPROVED as the creator's stated creative direction.
- Hustle City blends Chicago-inspired urban character, Miami/Florida-inspired atmosphere and original Hustle City identity. “Half Chicago, half Miami, half Hustle City” is a creative blend, not literal mathematical proportions.
- Use real-world references for familiarity and believable urban design, but create original geography, landmarks, names and layouts; do not copy a real city map.
- Six central districts are established. Surrounding outer boxes are reserved for neighborhoods. Exact grid dimensions, outer-box count and boundaries must be reconciled with original map references.

## 2026-11-22 — Transportation visual quality and living construction
- **Status:** APPROVED as production direction.
- Stations, trains, tracks, tunnels, bridges, platforms and surroundings must be high-quality, realistic 3D urban environments with detailed architecture, materials, lighting, signage and credible engineering proportions.
- Avoid generic, toy-like, low-detail or cartoon train/station designs.
- Some stations and rail corridors should be under construction, with believable phases, workers, engineers, supervisors, inspectors, equipment, barriers, scaffolding, deliveries and temporary pedestrian/traffic arrangements.
- NPCs should perform context-appropriate jobs and routines, not act as static decoration.
- Naming should feel native to Hustle City while evoking familiar Chicago-style geographic naming and Miami/Florida place character. Brainstormed names are not approved until reviewed.

## 2026-11-22 — Persistent knowledge library
- **Status:** APPROVED — creator requested a repository-based idea library and consistent knowledge base.
- Capture new freestyle ideas, adopted assistant suggestions, frameworks and design conversations in the repository.
- Preserve source wording and context. Promote refined ideas into reusable frameworks; link sources and update the index.
- Assistant/agent suggestions remain proposals until creator approval.
- Superseded decisions remain in history.

## Pending questions
- Reconcile district names/placement and outer-box count against original map references.
- Design HCTA line count, colors, routes, station locations and naming.
- Design HIM terminal(s) and intercity route map.
- Define building framework details and confirm the intended meaning/scope of “MPC” in the Sims/MPC discussion.
- Recover and index original conversations and visual references.


## 2026-11-24 — Persistent NPC familiarity, recognition, trust and shift continuity
- **Status:** APPROVED — creator explicitly directed that this system be built out as a Hustle City requirement.
- Every meaningful recurring NPC interaction can build persistent, player-specific familiarity, including dating/social NPCs and everyday workers such as valets, parking attendants, bartenders, servers, shop staff, mechanics, hosts and other service NPCs.
- Familiarity and trust are separate measurements. Familiarity tracks recognition built through meaningful repeat encounters; trust is a distinct visible meter/bar that reflects earned comfort and confidence. Familiarity may rise while trust remains low.
- Trust develops through behavior and shared experiences, can change in either direction, and is not equivalent to attraction, friendship, relationship status, consent or guaranteed access.
- Player characteristics such as height, appearance, style/swagger and conversation approach, alongside NPC personality, preferences, relationship status, mood, confidence, social awareness and boundaries, inform contextual social reactions without deterministic stereotypes or overriding NPC agency.
- NPCs and players should recognize recurring people using stable identity and verified encounter history. Each player↔NPC relationship is separate; one player's familiarity/trust must not leak to another.
- Recurring workplaces use persistent shift rosters. Three staggered eight-hour shifts are an approved example pattern for 24-hour coverage; business-specific shift start times, staffing levels, overlaps, days off and opening hours remain configurable.
- Different named workers can cover the same role at different times. Players can learn who is commonly on duty at familiar in-game times. Incoming workers retain their own independent familiarity/trust records; they do not inherit another worker's personal relationship.
- **Open implementation details:** familiarity level count and thresholds; trust scale and change weights; exact shift hours and staffing per business; UI presentation; persistence schema; recognition implementation and performance budgets.
- **Canonical specification:** [Sims / MPC / NPC Simulation Framework](knowledge-library/frameworks/SIMS_MPC_NPC_FRAMEWORK.md), sections 16–20.


## 2026-11-24 — Reciprocal NPC/player profiles and contextual recognition UI
- **Status:** APPROVED — creator explicitly requested visible NPC profiles and reciprocal player recognition information.
- When a player approaches or interacts with a named NPC, a compact profile/relationship area can appear alongside the conversation or be opened as a fuller profile.
- The player can see the NPC's stable name and role, plus the player-specific familiarity level and trust bar.
- The NPC recognition system can consult approved in-game player profile fields such as display name (example: Frank Maserati), player level, visible stars/rank, playtime/tenure and visit frequency at the relevant venue.
- NPC greetings and behavior should adapt to verified context: first-time visitor, returning guest, venue regular, recognized player, prior service or conversation history.
- Venue visit frequency must be distinguished from total playtime/tenure. NPCs may only use fields approved as visible in that context; private/account data must not be exposed.
- Level, stars and playtime are context cues, not proof of trustworthiness, wealth, consent, authority, romantic compatibility or entitlement. They do not replace player-specific familiarity/trust or NPC agency.
- **Open implementation details:** final panel layout, profile visibility defaults/settings, exact public/social fields, UI behavior on different screens, data contracts and dialogue-selection rules.
- **Canonical specification:** [Sims / MPC / NPC Simulation Framework](knowledge-library/frameworks/SIMS_MPC_NPC_FRAMEWORK.md), section 21.


## 2026-11-24 — Conversation-earned trust and NPC-hosted social life
- **Status:** APPROVED — creator explicitly directed that trust should grow through conversations and that NPCs should host and invite players to social gatherings.
- Trust is primarily earned through meaningful conversation and interaction. After completing a practical interaction (for example, “park a vehicle” with Marcus the valet/parking attendant), the player can choose to remain and talk with that same NPC.
- Conversation choices can include ordinary topics, questions about family or work, shared interests, personal updates from the player, and more personal questions when context and boundaries support them. NPCs can answer, decline, deflect or redirect naturally.
- A sustained positive conversation can raise trust gradually (illustratively, 63→64→65). Trust changes depend on conversation quality and the NPC's response, not elapsed time, repetitive prompts or button-spamming. Listening, empathy, relevant follow-ups and respectful reciprocal sharing can help; intrusive, dismissive or boundary-violating behavior can stall or reduce trust.
- NPCs can initiate conversation, ask questions and share appropriate personal updates grounded in their own lives and recorded shared history. Trust remains separate from familiarity, attraction, relationship status and consent.
- NPCs and NPC social circles can host city social events, including yacht parties, street-car meets/parties and club parties. Hosts select guests and can invite players, including new players, through contextual social pathways; invitations are not restricted to high-trust relationships or established crews.
- Support the full event lifecycle: host and event selection, location/time, guest list, invitations/responses, attendance, social interactions and persistent outcomes. NPCs retain agency to accept, decline, defer, attend, leave and interact independently.
- Player-hosted parties remain supported; NPC-hosted events are a separate capability in which NPCs have genuine social agency rather than acting as decoration.
- **Open implementation details:** conversation topic catalog and scoring/decay model; trust increment sizes and thresholds; NPC memory representation; social graph and host selection; event scheduling, capacity, invitation discovery and safety/content rules.
- **Canonical specification:** [Sims / MPC / NPC Simulation Framework](knowledge-library/frameworks/SIMS_MPC_NPC_FRAMEWORK.md), section 22.


## 2026-11-24 — Recognition through encounters; trust through conversation
- **Status:** APPROVED — creator clarified that recognition and trust must progress through different signals.
- Recognition/familiarity may increase when an NPC meaningfully sees or encounters a returning player, including repeat service visits. Trust should primarily come from actual, meaningful conversation and reciprocal interaction.
- A player who parks a vehicle with Marcus and leaves without talking may become more recognizable to Marcus over time, but should not automatically gain meaningful trust from the service transaction alone.
- Repeated venue visits or standing nearby are not substitutes for conversation. Passive proximity does not automatically build trust; recognition only changes when the NPC plausibly notices a meaningful encounter.
- Players can converse using either pre-selected dialogue boxes or player-typed messages. Both routes use the same contextual evaluation of relevance, respect, reciprocity, NPC personality, response and boundaries.
- This applies to social conversations such as talking with someone at a bar as well as conversations with service NPCs. Trust gains are not guaranteed for every message and need not be symmetrical between player and NPC.
- **Canonical specification:** [Sims / MPC / NPC Simulation Framework](knowledge-library/frameworks/SIMS_MPC_NPC_FRAMEWORK.md), section 23.
