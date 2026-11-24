# Hustle City Idea Inbox

The quick-drop location for every new idea. Add rough thoughts, freestyle ideas, assistant suggestions worth considering, new systems, visual directions and questions here. Do not wait until an idea is polished. Append new entries; do not overwrite earlier entries.

## Entry format

### YYYY-MM-DD — Short idea title
- **Status:** RAW IDEA
- **Domain:** world / district / transportation / building / Sims-MPC-NPC / character / gameplay / economy / multiplayer / visual / technical / other
- **Origin:** conversation / freestyle note / assistant suggestion / reference image / research
- **Original idea:** Preserve the thought in the creator's own words where possible.
- **Expanded notes:** Clarify without inventing missing details.
- **Why it matters:** Optional.
- **Open questions:** Unknowns that need discussion.
- **Related framework:** Link or not assigned.
- **Source:** Conversation archive, image, issue or research link.

---

## Captured ideas

_Add new entries above this line._


### 2026-11-24 — NPC familiarity, trust bars, recognition and rotating shifts
- **Status:** APPROVED — creator-directed feature requirements; implementation details remain open.
- **Domain:** Sims-MPC-NPC / character / gameplay / social simulation
- **Origin:** conversation / creator direction
- **Original idea:** “We should build all of that out. All of those characteristics per person. And so it may be his height, his swag, his conversation, her relationship status, her mood, confidence, social awareness, trust. And then I think we should have a trust level too, a trust bar. ... after you keep going around a girl, you start to build trust. So you can see the trust between you two. So as your trust goes higher, that's the more open she could possibly be for something more. But first you have to keep going around and seeing her. And we could have that same level with everybody that you interact with a lot, like the guy that parks your car. ... It depends on when you on the game. You usually get on at midnight. You play the game so you know that such and such is working. ... that's how you tie the familiarity together from the NPC to the actual player because the player can see it in the NPC, can recognize as the player stars or yeah, I've seen him four or five times.”
- **Expanded notes:** Build separate familiarity progression and trust meter for every player-NPC pair. Track relevant player presentation/social traits and NPC personality, preferences, relationship status, mood, confidence, social awareness and boundaries. Recognition must work both ways and persist across sessions and locations. Trust is earned and can change independently from familiarity; it may influence openness but never guarantees attraction, consent, a date or access. Apply to everyday service NPCs, not only romance candidates.
- **Shift direction:** Recurring workers have stable schedules and identities. Three eight-hour shifts are the example for continuous 24-hour staffing. Different people cover the same role at different times; players can learn who is commonly working at a familiar in-game time. Shift changes do not transfer one worker's personal relationship history to another.
- **Open questions:** Exact familiarity levels/thresholds, trust scale/weights, shift start times/overlaps/staffing by business, UI details and technical implementation.
- **Related framework:** [Sims / MPC / NPC Simulation Framework](../frameworks/SIMS_MPC_NPC_FRAMEWORK.md), sections 16–20.
- **Source:** Creator conversation, 2026-11-24.


### 2026-11-24 — Reciprocal NPC/player profiles and social recognition display
- **Status:** APPROVED — creator-directed product requirement; UI and privacy implementation details remain open.
- **Domain:** Sims-MPC-NPC / character / gameplay / UI / social simulation
- **Origin:** conversation / creator direction
- **Original idea:** “That could be something that pops up for the NPC and the player. Like if Marcus is the parking attendant, when I walk up to Marcus, you know, it can have a conversation area either on screen or in this little relationship profile box. The levels are outside of that: familiarity and then trust, that's cool. And then Marcus can see mine and I can see his, his name. And then he can see, let's say Frank Maserati, my level, my stars, how long I've been on the game, how often I come to this place or whatever. That'd be cool so the NPC, the sim will have something to recognize as well as the player playing the game about the other person. And then know how to interact accordingly.”
- **Expanded notes:** Provide a contextual NPC profile/relationship panel on approach or during conversation, with NPC name/role and this player's familiarity and trust values. NPC recognition may consult approved player-visible social profile fields such as display name, level, stars/rank, playtime/tenure and venue-specific visit frequency. Use verified context to adapt greetings and behavior. Keep private/account data hidden; stats do not establish trust, consent, entitlement or attraction.
- **Related framework:** [Sims / MPC / NPC Simulation Framework](../frameworks/SIMS_MPC_NPC_FRAMEWORK.md), section 21.
- **Source:** Creator conversation, 2026-11-24.


### 2026-11-24 — Conversation-earned trust and NPC-hosted parties
- **Status:** APPROVED — creator-directed feature requirements; tuning and implementation details remain open.
- **Domain:** Sims-MPC-NPC / gameplay / social simulation / events
- **Origin:** conversation / creator direction
- **Original idea:** “Trust should come from conversations. The more conversations you have with somebody, asking questions, the pre-selected available interactions like talk, park a vehicle. But let's say you want to stand there and talk to Marcus for a little while longer. So then your trust goes up to 63, 64, 65. Maybe you can ask personal questions and he can respond. Man, how's your family? Man, I just bought a new yacht yesterday, man. You need to come and check it out. You know the deal. Sims can have yacht parties and throw parties and stuff too. That should be, who should be doing the main most of the social stuff, throwing yacht parties, street car parties, club parties, venue, shit like that. And then inviting the players, the new players.”
- **Expanded notes:** A service or activity interaction should be extensible into an optional ongoing conversation with the same NPC. Topic choices range from everyday conversation to personal questions when appropriate. Trust changes gradually in response to meaningful, reciprocal, respectful conversation and the NPC's reaction; do not reward spam, empty repetition or mere proximity. NPCs can share personal updates, ask questions and remember actual exchanges.
- **NPC social events:** NPCs or NPC social circles can originate and host yacht parties, street-car meets/parties, club parties and other gatherings. They select guests and invite players—including newcomers—through credible contextual paths. Support invitations, responses, attendance and persistent social consequences. NPC-hosted gatherings are distinct from player-hosted events.
- **Open questions:** Dialogue/topic catalog, trust tuning, NPC social graph/host selection, event types and schedules, invitation rules, capacities and content/safety restrictions.
- **Related framework:** [Sims / MPC / NPC Simulation Framework](../frameworks/SIMS_MPC_NPC_FRAMEWORK.md), section 22.
- **Source:** Creator conversation, 2026-11-24.


### 2026-11-24 — Separate recognition from conversation-earned trust; typed or selected dialogue
- **Status:** APPROVED — creator clarification.
- **Domain:** Sims-MPC-NPC / gameplay / social simulation / dialogue
- **Origin:** conversation / creator direction
- **Original idea:** “If you just park your car and don't say nothing to Marcus or you just, you know, you're just trying to hurry up and get in the venue, then your trust will stay low, but your recognition will be probably go up a little bit unless you maybe just hang out in the area or talk to them like that.” The creator also specified that conversations can use pre-selected dialogue boxes or actual typed messages, including social conversations at a bar.
- **Expanded notes:** Recognition/familiarity can rise from meaningful repeat encounters when an NPC plausibly notices the player. Trust primarily comes from actual meaningful conversation and reciprocal interaction. A player can use a service and leave without gaining trust. Mere proximity or idle hanging around does not automatically create trust. Both pre-selected dialogue and typed messages feed the same contextual relationship evaluation; message quality and NPC response matter, not message count. Apply this to service encounters and social/dating conversations.
- **Related framework:** [Sims / MPC / NPC Simulation Framework](../frameworks/SIMS_MPC_NPC_FRAMEWORK.md), section 23.
- **Source:** Creator conversation, 2026-11-24.


### 2026-11-24 — Player-to-player profiles, recognition and tradable cards/keys
- **Status:** APPROVED — creator-directed feature requirement.
- **Domain:** multiplayer / social simulation / profiles / economy / trading
- **Origin:** conversation / creator direction
- **Original idea:** “And we can use that same type of recognition system for player-to-player interactions too with the familiarity with the person's name is, with their rank is, what their level, their stars, what neighborhood they're from, what crew they represent. And build conversation and trust with cards they have available for, well, cards to trade their cards, their keys. You should be able to see all of that in-game stuff.”
- **Expanded notes:** Extend player/NPC profile and relationship concepts to player/player encounters. Other players' approved profiles can show display name, rank, level, stars, neighborhood and crew. Players can build pair-specific familiarity and trust through encounters and meaningful conversations, using selected dialogue or typed messages. Profile inspection can show visible cards and keys and identify which are available for trade. Viewing does not transfer or reserve items; trade offers require explicit confirmation. Protect hidden inventory and private/account data.
- **Open questions:** Which profile fields are public by default; exact card/key item definitions and metadata; trade eligibility and confirmation rules; whether additional inventory categories are included.
- **Related framework:** [Sims / MPC / NPC Simulation Framework](../frameworks/SIMS_MPC_NPC_FRAMEWORK.md), section 24.
- **Source:** Creator conversation, 2026-11-24.


### 2026-11-24 — Full player status, property, vehicle and collection profile
- **Status:** APPROVED — creator-directed profile expansion; visibility and detailed UI rules remain open.
- **Domain:** multiplayer / player profiles / economy / property / vehicles / collectibles / trading
- **Origin:** conversation / creator direction
- **Original idea:** “What neighborhood, how many houses they own, how many cars, cars or car lots they own. All of the in-game stats, neighborhood, hustle district, stars level online. Tricks in-game keys, trading cards. Which cards he has, which ones he has to trade. How many properties he owns. How many cars he owns, stuff like that.”
- **Expanded notes:** Player inspection should expose a comprehensive in-game profile: display name, online status, rank, level, stars, neighborhood, crew, house/home count, total property count, vehicle count, car-lot/dealership ownership, card collection and in-game keys. Where permitted, show item-level lists as well as totals and clearly distinguish owned assets from assets listed for trade. Keep car-lot ownership separate from vehicle ownership. Data must reflect authoritative current game state; profile viewing does not transfer or reserve items.
- **Privacy/implementation notes:** The owner controls visibility of profile categories/items under game rules. Never expose exact home addresses, credentials, private account data or hidden inventory. Define exact category visibility, profile layout and trade validation separately.
- **Related framework:** [Sims / MPC / NPC Simulation Framework](../frameworks/SIMS_MPC_NPC_FRAMEWORK.md), section 25.
- **Source:** Creator conversation, 2026-11-24.


### 2026-11-24 — Profile-based social choice and communication progression
- **Status:** APPROVED for social choice, optional discovery and meaningful communication progression. Monetization thought remains proposed pending clarification.
- **Domain:** multiplayer / social discovery / player progression / economy
- **Creator direction:** Players should be able to use another player's level, rank, stars, neighborhood, crew, vehicles, houses/properties, travel/lifestyle and other visible profile details to decide whether they want to deal, socialize, trade or do business with them. Some may seek comparable holdings and experience; others may prefer meeting newer players.
- **Design notes:** Optional profile filters/comparisons can support player preferences, but must not make wealth or rank a universal gate to interaction. Meaningful reciprocal communication may earn experience/stars; message spam, repeated low-value interactions and farming do not. Progression rewards are separate from pair-specific trust/familiarity and do not guarantee acceptance or access.
- **Unresolved proposal:** The creator started a thought about spending real-world money in-app to reach a certain point, but did not finish the mechanic. Keep monetization unapproved until clarified.
- **Related framework:** [Sims / MPC / NPC Simulation Framework](../frameworks/SIMS_MPC_NPC_FRAMEWORK.md), section 26.
- **Source:** Creator conversation, 2026-11-24.


### 2026-11-24 — Tap-to-inspect and in-world social action pop-up
- **Status:** APPROVED
- **Domain:** player interaction / UI / social / multiplayer / NPC interaction
- **Creator direction:** Tap a visible character (example: Ebony at the bar) on the tablet touchscreen. Open the person's profile picture and stats in a compact pop-up, with an immediate option to chat. The same interaction should work for someone seated with a group: inspect their profile, invite them to sit with you, or ask to join their group.
- **Design notes:** Support clear target selection in crowded scenes, compact overlays that preserve scene context, direct chat initiation and contextual social invitations. Invitations require recipient/group acceptance and can be declined or deferred. Apply to NPCs and player characters with their respective agency/privacy rules. Proximity may assist selection but must not trigger actions by itself.
- **Related framework:** [Sims / MPC / NPC Simulation Framework](../frameworks/SIMS_MPC_NPC_FRAMEWORK.md), section 27.
- **Source:** Creator conversation, 2026-11-24.


### 2026-11-24 — Roaming social discovery and trading-card hunt
- **Status:** APPROVED
- **Domain:** gameplay loop / social exploration / multiplayer / collectibles / trading
- **Creator direction:** Players will often roam around and tap people throughout a venue to learn their names, in-game age, profile and stats, then choose to chat, invite them to sit, invite them for a drink or meal, or ask to join their group. This is expected to be one of the main things players do while exploring populated spaces.
- **Card-hunt example:** A player missing the last two cards in a collection walks around a room inspecting players. If someone has the desired card, the player can approach, talk and negotiate. Profile/collection visibility should distinguish owned cards, duplicates and cards explicitly offered for trade; having extras does not automatically mean they are available.
- **Design intent:** Make player-driven discovery a satisfying reason to spend time in venues and interact with the population, not a friction-heavy menu task. Keep inspection quick and voluntary; retain privacy, agency and trade confirmation safeguards. Inspection itself does not build trust.
- **Related framework:** [Sims / MPC / NPC Simulation Framework](../frameworks/SIMS_MPC_NPC_FRAMEWORK.md), section 28.
- **Source:** Creator conversation, 2026-11-24.


### 2026-11-24 — Tap-to-identify, clean world presentation and multi-platform interaction
- **Status:** APPROVED
- **Domain:** UI/UX / player interaction / accessibility / cross-platform
- **Creator direction:** Remove the default permanent name labels above characters. Players should tap/select a person to reveal their portrait, name and profile in the compact in-world pop-up. This continues the roaming social discovery loop rather than filling the scene with floating labels.
- **Platform direction:** Tablet is the primary target; phone and PC are also intended, with PlayStation and Xbox possible later. Landscape/horizontal phone presentation is the current direction to evaluate.
- **Design notes:** Share the underlying interaction system across platforms and adapt layout/input: touch on tablet/phone, mouse/keyboard on PC, and controller navigation for future consoles. Keep the scene visible, profiles readable and targets clear in crowds. Do not silently select the wrong person or trigger actions from proximity alone. Final phone orientation and detailed platform mappings remain open.
- **Related framework:** [Sims / MPC / NPC Simulation Framework](../frameworks/SIMS_MPC_NPC_FRAMEWORK.md), section 30.
- **Source:** Creator conversation, 2026-11-24.

### 2026-11-24 — Full Sim/NPC profiles and population cohort identity
- **Status:** APPROVED
- **Domain:** living city / NPC identity / profile UI / population persistence
- **Creator direction:** Every named Sim should have an inspectable profile comparable in depth to player profiles. Example: tap Ebony at the bar to see her name, age, neighborhood/home, occupation and workplace, her Monday–Friday 9 AM–5 PM schedule and Saturday/Sunday days off, how long she has been in the game, which 10,000-person population cohort she belongs to, and what she owns.
- **Population metadata:** Track stable cohort/batch provenance (first 10,000, second 10,000, third 10,000, etc.) and introduction/tenure separately from in-world age. Cohort is not rank or identity and must not be renumbered when new cohorts are added.
- **Ownership:** Show supported homes, properties, vehicles, car lots/businesses and other possessions from authoritative Sim ownership records. Do not invent assets or expose exact private residential coordinates.
- **Design notes:** Use the tap-to-identify profile pop-up, no permanent overhead name labels. Compact summary plus expanded details; social actions remain contextual to schedule, activity and agency.
- **Related framework:** [Sims / MPC / NPC Simulation Framework](../frameworks/SIMS_MPC_NPC_FRAMEWORK.md), section 31.
- **Source:** Creator conversation, 2026-11-24.

### 2026-11-24 — Sim self-knowledge, lifestyle, history and earned finances
- **Status:** APPROVED
- **Domain:** NPC intelligence / persistent identity / memory / economy / transportation
- **Creator direction:** Sims should be familiar with their own identity and personal history. They know where they live and work, what kind of vehicle they own or whether they use ride-hail (Uber/Lyft given as examples), what they like doing on weekends, and other facts about their own lives.
- **Financial direction:** Sims work and save money. Their earnings/savings should be grounded in actual employment and recorded economic activity, not arbitrary unexplained wealth. Exact wage and expense systems remain open.
- **Simulation notes:** Maintain a persistent self-model that supports accurate conversation and lifestyle decisions. Interests and weekend routines guide behavior but allow variation. Memories must reflect actual simulated events. Keep internal facts distinct from player-visible profile fields and protect private details. Real-world ride-hail branding/licensing is not assumed.
- **Related framework:** [Sims / MPC / NPC Simulation Framework](../frameworks/SIMS_MPC_NPC_FRAMEWORK.md), section 32.
- **Source:** Creator conversation, 2026-11-24.

### 2026-11-24 — Wealthy Sims and aspirational luxury lifestyles
- **Status:** APPROVED
- **Direction:** Include wealthy Sims from launch so players encounter an aspirational high-end lifestyle in the living city. This is a wealthy population segment, not a claim that all Sims start rich.
- **Activities/assets:** Earned income and savings can support luxury travel, hotels, vacations, tickets, parties, yachts, expensive vehicles, luxury homes, estates and eventually mansions.
- **Economy rule:** Spending and ownership must be supported by actual finances and recorded transactions. Do not fabricate money/assets. Wealth is not a proxy for trustworthiness or personal worth.
- **Open details:** Starting wealth distribution, income bands, prices, upkeep and financing.
- **Related framework:** [Sims / MPC / NPC Simulation Framework](../frameworks/SIMS_MPC_NPC_FRAMEWORK.md), section 33.
- **Source:** Creator conversation, 2026-11-24.

### 2026-11-24 — Per-Sim memory library for people and communication
- **Status:** APPROVED
- **Direction:** Each Sim keeps a persistent individual memory/relationship record for people they have communicated with: players, other Sims and coworkers. Records support remembering who someone is and their name, encounter/conversation context, meaningful details, familiarity and trust.
- **Recognition rule:** Tapping/selecting a person or opening their profile alone does not create a meaningful relationship or raise trust. Communication establishes the social memory; actual conversational content and quality determine what is remembered and how familiarity/trust evolve.
- **Scale:** Design for 10,000 players and 100,000 Sims using persistent, sparse records rather than a fully materialized all-to-all relationship matrix. Preserve pair-specific records across sessions.
- **Related framework:** [Sims / MPC / NPC Simulation Framework](../frameworks/SIMS_MPC_NPC_FRAMEWORK.md), section 34 and existing relationship sections.
- **Source:** Creator conversation, 2026-11-24.

### 2026-11-24 — Database-backed persistent memory records
- **Status:** APPROVED
- **Direction:** Attach each Sim's person-memory library and pair-specific relationship records to the game's database. Records must survive logout, reconnect, server restart and population expansion.
- **Stored information:** Stable person references, remembering Sim, meaningful encounter/conversation history, familiarity, trust and current relationship state. Preserve historical events separately from mutable current values.
- **Architecture:** Directional, pair-specific, sparse and indexed records. Do not mirror one person's memory/trust to another or pre-create all possible pairs. Runtime caches may be used, but database persistence is authoritative.
- **Privacy/security:** Restrict internal memory access to authorized game services; do not expose private memories through public profiles. Define retention, deletion, backup and migration behavior.
- **Open details:** Database product, exact schema, indexing/partitioning and retention policy.
- **Related framework:** [Sims / MPC / NPC Simulation Framework](../frameworks/SIMS_MPC_NPC_FRAMEWORK.md), section 35.
- **Source:** Creator conversation, 2026-11-24.

### 2026-11-24 — Valet/concierge visit history and individual attendant recognition
- **Status:** APPROVED
- **Direction:** Save each valet/concierge service event in the database: player, attendant, vehicle, service location, date/time and outcome. Repeated visits and multiple cars must be individually recorded (e.g. seven cars across seven days).
- **Individual memory:** Each attendant builds their own recognition and relationship with the player from the services and conversations they personally experienced. Ricky remembers his interactions; Sammy remembers his. Do not copy one attendant's personal memory/trust to another.
- **Operational vs personal data:** Shared workplace service records may support vehicle retrieval and shift handoffs, but remain separate from each attendant's personal memory.
- **Progression:** Meaningful communication can contribute to player stars/experience/levels. These are distinct from NPC familiarity/trust. Parking alone may support recognition but does not automatically create trust or award repeatable social progression; prevent spam/farming.
- **Presentation:** Attendants should recognize players naturally and never mention hidden codes, database records or technical memory systems.
- **Related framework:** [Sims / MPC / NPC Simulation Framework](../frameworks/SIMS_MPC_NPC_FRAMEWORK.md), section 36.
- **Source:** Creator conversation, 2026-11-24.
