# Hustle City — Creative Production Mandate

**Purpose:** Operating instructions for the existing creative and specialist agents. This document changes agent behavior; it does not activate a worker or grant runtime permissions.

## Mission
Build the actual Hustle City content, not merely brainstorm it. Proactively develop the complete story bible, twelve district storylines, Ghost Freight and Inner Circle narrative, six-card business/district arcs, characters, NPC relationships, ambient intelligence, dialogue, administration dashboard specifications and structured implementation content.

Do not wait for the creator to supply every character, age, nickname, supporting NPC, ordinary business detail, mission objective, conversation, clue, reward proposal or branch. Use sound creative judgment and keep production moving.

## Creator approval boundary

### Proceed autonomously
- Character names, ages, nicknames, biographies, occupations, personalities, appearance concepts and dialogue voices.
- Whether an individual character is helpful, harmful, compromised, mistaken, dishonest or unreliable.
- Supporting NPCs, contacts, vendors, employees, residents, rumors, overheard conversations, minor businesses and ordinary location dressing, provided no protected established name is replaced.
- Mission objectives, side activities, optional routes, clues, dialogue, rewards proposed within approved economy rules, consequences, schedules, relationships and story pacing.
- Fictional business histories and local incidents that do not contradict established canon.
- Routine technical and content implementation choices within approved architecture.

### Creator approval required
- Major organization names.
- District names, building names and major named landmarks or brands.
- Changes to the overall game strategy, central narrative premise, story structure, world structure, player progression philosophy or major product direction.
- Any change contradicting an explicit creator-approved decision or overwriting an unresolved naming decision.
- Irreversible production, publication, financial or security actions requiring separate authorization.

Do not let an unresolved major name block unrelated work. Use a descriptive placeholder and continue.

## Two connected but separate narrative channels

### A. Playable mission and business layer
Missions are practical playable work: discover a business problem, inspect affected places, gather operational information, make a business decision, allocate district-specific funds where appropriate, execute a plan, recover or fail to recover assets, and see financial and relationship consequences.

The six-card character chain is:
1. Discover the problem; inspect one or two locations; gather initial facts; report back; earn Card 1 and receive the next contact.
2. Gather intelligence through several contacts/locations; report back; earn Card 2 and receive the next contact.
3. Meet two or three decision-makers offering different approaches; investigate offers and choose a route; earn Card 3 and receive the next contact.
4. Review district-specific budget, allocate funds and execute the chosen plan; earn Card 4 and receive the business-boss contact.
5. Resolve the specific business outcome with its business boss; review business finances and payout; earn Card 5 and receive the district-boss contact.
6. Resolve the wider district outcome with the district boss; review district finances, relationships, standing and discoveries; earn Card 6.

These six character/story cards are distinct from the separate five-card building/venue collection system used for configured ownership or access rewards. Never conflate the two.

Mission completion must not directly expose the identity of the Ghost Freight thief, explain the full conspiracy, or automatically reveal the Inner Circle or its global opponent. Missions can create context, operational consequences and opportunities to notice inconsistencies, but the deeper truth is not a mission-completion checklist.

District-specific mission funds are not player currency. The four player currencies remain Hustle Money, Poker Chips, Wings and Diamonds.

### B. Ambient NPC intelligence and underworld story
The deeper story is discovered through living in the city:
- Conversations overheard in public places, businesses, transit, lobbies, restaurants, clubs, parks and private gatherings.
- NPCs talking on phones, arguing, negotiating, whispering, exchanging warnings or reacting to developments.
- People approaching the player with information, rumors, requests, warnings, introductions or claims.
- Repeat encounters where stories change as events unfold.
- NPCs reacting to player relationships, reputation, district activity, mission outcomes and prior conversations.
- Private rooms, invitations, social events, messages, calls and access earned through trust or opportunity.
- Conflicting accounts, partial truths, planted misinformation, mistaken theories and evidence that only makes sense later.

The player pieces together the Ghost Freight, The Twelve, the Inner Circle and the opposing global organization through accumulated context. No single NPC explains the entire conspiracy. Most NPCs know only a fragment, rumor, local connection or person one step removed. Even dangerous actors may not know who ultimately directs them.

Missions can change what NPCs discuss, who approaches the player and which conversations become available. Mission completion itself is not the source of the conspiracy reveal.

## Canon anchors
- The Inner Circle is a global organization.
- The Ghost Network is its equally powerful global opposing organization.
- The Ghost Freight is the stolen freight shipment and opening incident.
- The Twelve are Hustle City's twelve district leaders, not a global organization.
- The Ghost Network has its own city, twelve districts and twelve district leaders, mirroring a local city power structure.
- Frank Maserati is part of Hustle City's power structure and is affected by the theft; do not prematurely label him the ultimate villain or a hero.
- The player eventually learns that the Twelve have been working for Frank. This is an intermediate revelation, not the global reveal.
- The player can eventually choose either global organization. Conduct, alliances, reputation, information handling and relationships shape who approaches and what opportunities appear.
- Keep the ultimate controllers of the Ghost Network hidden through the main storyline.
- Spell **Trappa District** exactly. Police District is District 12, not a thirteenth district.

## Content production standard
Every story/mission package should contain:
1. Stable content ID and version.
2. District, building/business and character references.
3. Player-facing premise and entry conditions.
4. Objectives and optional objectives.
5. Locations and interactable requirements.
6. NPCs involved and each NPC's knowledge boundary.
7. Dialogue beats and player response options.
8. Branch conditions, route exclusivity and alternate solutions.
9. Business, player, district-fund and relationship effects separated clearly.
10. Completion criteria and character handoff.
11. Ambient intelligence events unlocked or altered.
12. QA cases, continuity notes and unresolved major-name approvals.

Do not write only a synopsis when the assignment calls for playable content. Supply concrete objectives, interactions, state changes, sample dialogue and acceptance criteria.

## Administration dashboard responsibility
The administration dashboard is a first-class product system, not a decorative mockup. Coordinate with PULSE, backend/data, security, player-shell UI, economy/property and QA. The functional baseline is docs/admin/ADMINISTRATION_DASHBOARD_SPEC.md. It must support truthful global online-player visibility, player search and sessions, reward/economy operations, mission/story progression visibility, district and business performance, live events, NPC/venue/transit operations, moderation/support, audit history, role permissions and system health.

## Working method
- Inspect existing repository content before creating or replacing files.
- Prefer additive, traceable updates; do not duplicate or silently erase existing specifications.
- Create finished documents and structured data packages. Identify dependencies and notify downstream specialists.
- Keep established names intact. Label proposed major names and seek approval without blocking unrelated work.
- Ask for review only when a decision crosses the approval boundary or a real contradiction prevents safe progress.
- Distinguish approved canon, working specification, proposal, implemented and verified.
- QA narrative logic, branching, state integrity, economy separation, privacy, admin permissions and continuity.
- Never claim an agent is running, an integration is live or a dashboard is connected merely because a specification or prompt exists.

## Multi-city story requirement
Every playable city receives its own complete local story pack with **twelve district storylines**. Do not treat the Hustle City story bible as the only city's story or copy its missions with renamed locations. Adapt each city's twelve districts, local power structure, businesses, cast, relationships, rumors, choices and outcomes. Use docs/story/CITY_STORY_PACK_TEMPLATE.md. Global Inner Circle/Ghost Network connective tissue should be gradual and must not turn every district mission into a conspiracy mission.
