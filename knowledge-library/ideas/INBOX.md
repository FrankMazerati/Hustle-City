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
