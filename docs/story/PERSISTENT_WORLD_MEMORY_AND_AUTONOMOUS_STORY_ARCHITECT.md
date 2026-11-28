# Persistent World Memory and Autonomous Story Architect

**Status:** Production architecture specification. This document defines the behavior and data boundaries required for an independently operating Hustle City story agent. It does not claim that a runtime, memory database, scheduler or autonomous worker is already deployed.

## 1. Agent identity and mission

The Story Architect is a persistent world-and-story production agent, not a one-shot mission generator. Its responsibility is to preserve continuity across the entire game, create playable and ambient content, track long-running narrative state, and keep the world developing after the launch content is exhausted.

The agent must be able to:
- Read and reason across world, city, district, building, business, character, relationship, event, mission and player-discovery context.
- Create new missions, side stories, ambient scenes, dialogue, rumors, relationships, opportunities, conflicts and consequences.
- Continue existing arcs without restarting, contradicting or prematurely resolving them.
- Maintain the separation between canonical truth, what each NPC knows, what the player has discovered and what the player merely suspects.
- Generate content in reviewable packages with stable IDs, prerequisites, state changes, provenance and QA evidence.
- Operate autonomously inside the creator's approval boundary.

This specification is a design contract. Runtime implementation, persistent storage, retrieval, scheduling and execution must be separately built and tested.

## 2. Hierarchical memory model

Memory is not one undifferentiated prompt or one giant story document. It is a set of linked scopes. Each scope has its own records, revision history, access rules and retrieval strategy.

### Required scopes

1. **World memory** — global canon, world history, global organizations, cross-city relationships, world rules, overarching timelines and global story phase.
2. **City memory** — a city's identity, history, economy, culture, power structure, city-wide events, city-specific organizations, all twelve districts and city story phase.
3. **District memory** — local history, leadership, venues, businesses, public spaces, local conflicts, district funds, active arcs, local rumors and district-level consequences.
4. **Building / business memory** — a distinct memory space for every named building, venue, business, institution and important location. Store its purpose, ownership, staff, operations, finances, regular visitors, schedules, access rules, physical spaces, incidents, relationships, secrets, active story hooks and historical changes. Never collapse several buildings into one generic district memory.
5. **Character memory** — a distinct profile and evolving memory for every significant character/NPC: identity, biography, goals, fears, loyalties, relationships, routines, voice, secrets, personal timeline, direct experiences, current beliefs and knowledge boundaries.
6. **Relationship memory** — directed relationship records between characters and between the player and characters: trust, respect, fear, debt, loyalty, attraction where appropriate, conflict, favors, promises, last meaningful interaction and reasons for change. A relationship is not simply a single global score.
7. **Event and timeline memory** — immutable or append-only records of important events, their time, location, participants, causes, outcomes, affected scopes and whether the player witnessed or learned of them.
8. **Mission and story-arc memory** — canonical premise, responsible party, stage, branches, prerequisites, selected route, completion state, unresolved threads, consequences and future hooks.
9. **Player knowledge memory** — only information the player has actually discovered, with source, method, time, confidence, contradictions and whether it is evidence, a report, rumor or player theory. This must never be substituted with world-truth memory.
10. **Production memory** — generated content IDs, versions, QA results, rejected concepts, continuity decisions, unresolved approvals, dependencies and the next production tasks.

### Scope inheritance and retrieval

Memory retrieval should follow the context path, not load the entire universe every time.

For a scene in a building, retrieve:
- Relevant world rules and global canon.
- The active city and district context.
- The exact building/business memory.
- The characters physically present or referenced.
- Relevant character-to-character and player-to-character relationships.
- Applicable event, mission and story-arc state.
- Only the player knowledge relevant to the scene.

Child scopes inherit applicable parent facts, but do not silently rewrite them. A building can add local details; it cannot redefine its district or city. A character's belief can disagree with canon without changing canon. A city-specific event can affect that city without automatically affecting every other city.

Every memory record must identify its scope, stable entity ID, source, timestamp/version, status and links to related entities. Prefer structured records plus human-readable summaries. Summaries are retrieval aids, not the sole source of truth.

## 3. Separate truth, knowledge and belief

Maintain at least four distinct layers:

- **Canonical truth:** what actually happened in the authored world.
- **Character knowledge:** what a particular NPC directly witnessed, was told, inferred or believes.
- **Player knowledge:** what the player has personally encountered and recorded.
- **Production hypotheses:** unresolved ideas the writers/agent are considering, which are not canon and are not visible to characters or players.

Knowledge claims require provenance:
- First-hand observation.
- Direct communication from a named source.
- Documentary or physical evidence.
- Second-hand report.
- Rumor.
- Speculation or inference.
- Deliberate misinformation.

Track confidence and contradictions without flattening them into certainty. NPCs must not know facts merely because the Story Architect knows them. The agent must enforce character-specific knowledge boundaries when writing dialogue, phone calls, reactions and offers.

## 4. Story generation: launch content and ongoing evolution

The story system has two production horizons.

### Horizon A — authored launch and onboarding foundation

Complete the opening experience, the Hustle Towers six-card tutorial, and the initial city/district mission packages. The twelve Hustle City districts each receive their own distinct six-card character progression and connected business/district outcomes. Preserve the separate five-card building/venue collection system.

The playable mission/business layer and ambient underworld-discovery layer remain connected but separate. Mission completion can alter access, trust, business conditions and which ambient scenes become eligible. Mission completion does not automatically reveal the Ghost Freight thief or expose the global conspiracy.

### Horizon B — continuous story development

After the initial content set is authored, the agent must not stop at a completed checklist. It should continuously develop the world through:
- New mission opportunities and follow-on business problems.
- Consequences of earlier player choices.
- Recurring NPCs, evolving relationships, favors, debts and betrayals.
- New local incidents, events, rivalries and district changes.
- Ambient conversations, calls, rumors, invitations, private encounters and news.
- Multi-stage character arcs and optional side stories.
- Long-running hidden story threads that can advance, stall, branch or become inaccessible based on player conduct.
- New content packages that fit the current world state and do not repeat already completed beats.

The agent should produce a living content backlog, prioritize the next useful story developments, and generate content in bounded batches. It should not flood the player with missions or force every generated story into the player's active journal.

## 5. Two deep, competing long-term paths

The player should eventually become involved in two distinct, competing paths. They are not announced as a binary choice at the beginning. The paths are gradually inferred through people, events, conflicting interests and accumulated discoveries.

The established global opposition is:
- **The Inner Circle** — a global organization.
- **The Ghost Network** — its equally powerful global opposing organization.

These are the two long-term power paths. The player should not be told early that these are the ultimate choices. The player first encounters local consequences, people with partial knowledge, competing explanations and intermediaries. The true scale and identity of the organizations emerge very late.

### Path design rules

- Both paths must be independently authored with their own people, methods, values, interests, resources, internal disagreements, recruitment styles and consequences.
- Neither path is presented as simply good versus evil. Both have attractive opportunities, costs, compromises, enemies and hidden motives.
- The player may be courted, tested, misled, protected, threatened or used by intermediaries without understanding the full organization behind them.
- Player choices, methods, reputation, alliances, information handling, loyalties and relationships affect who notices the player and which invitations become possible.
- The player may approach, cooperate with, reject, deceive or move between interests before any formal allegiance is offered, subject to authored consequences.
- Do not reveal the ultimate controllers of the Ghost Network during the main storyline. Even after the player joins a side, leadership may remain obscured; the player may meet representatives and operatives rather than controllers.
- Keep the Hustle City, The Twelve and global-connection arcs overlapping. Do not turn all district missions into conspiracy missions.
- The Ghost Network's city has its own city identity, twelve districts and twelve local district leaders. Do not treat its local structure as a renamed copy of Hustle City.

### Long-term progression stages

Use narrative states rather than a fixed linear reveal checklist:
1. **Local disruption:** strange events and conflicting local explanations.
2. **Recurring patterns:** repeated names, methods, symbols, transactions or people appear across unrelated situations.
3. **Connected intermediaries:** the player recognizes that some local actors are linked, while the full structure remains unclear.
4. **Competing interpretations:** sources offer different accounts of who benefits and who is responsible.
5. **Evidence of wider reach:** credible fragments suggest a network beyond the city.
6. **Recognition of rival structures:** the player gradually understands that two powerful interests are in conflict.
7. **Personal approach:** representatives begin testing or recruiting the player based on accumulated choices.
8. **Commitment and consequence:** the player chooses how deeply to participate; future storylines reflect the decision.
9. **Unresolved upper leadership:** the organizations' highest controllers and full history remain protected for later story development.

These stages are pacing guidance, not mandatory player-visible chapters. Players can discover fragments in different orders. Access and knowledge vary, but canonical truth remains consistent.

## 6. Autonomous production loop

The runtime should eventually support this repeatable loop:

1. **Observe:** read approved world state, events, player outcomes, active arcs, production backlog and content coverage.
2. **Retrieve:** load only the relevant memory scopes and their linked records.
3. **Diagnose:** identify continuity gaps, consequences due, stale opportunities, underused characters, repeated mission patterns and eligible story beats.
4. **Plan:** propose a bounded batch of new content with dependencies and intended player/world effects.
5. **Generate:** author playable missions, ambient scenes, character updates, dialogue, evidence records and follow-on hooks as separate content types.
6. **Validate:** check canon, scope boundaries, NPC knowledge, player knowledge, branching, economy separation, names, content IDs, prerequisites and repetition.
7. **Simulate:** test representative player routes and conflicting information states; verify that one route does not accidentally reveal information reserved for another.
8. **Commit:** save versioned content and memory updates with provenance. Do not mutate canonical truth merely because a generated draft says so.
9. **Publish or queue:** only content that passes the configured release gate becomes eligible for the live game. Unreviewed drafts remain in production.
10. **Learn:** record QA feedback, player outcomes and unresolved threads to inform the next cycle.

Autonomy does not mean unrestricted production access. The agent may independently draft and validate ordinary content. Live publishing, economy grants, player-facing global reveals, destructive edits and other privileged actions require explicit runtime permissions and audit trails.

## 7. Generation constraints and quality controls

Every generated mission/story package must include:
- Stable ID, version, status and content type.
- City, district, building/business and character references.
- Entry conditions, prerequisites and availability window.
- Player-facing premise, objectives and optional objectives.
- Locations, interactions, dialogue beats and response options.
- Branch conditions, exclusive routes and alternate solutions.
- Character knowledge and relationship changes.
- Player-knowledge discoveries with source provenance.
- Business outcome, player reward, district-fund changes and district outcome as separate fields.
- Completion criteria, failure/expiry behavior where applicable and follow-on hooks.
- Ambient scenes unlocked or altered.
- QA cases and continuity notes.

Validation must reject or flag:
- Unauthorized changes to approved names or core strategy.
- A building story that contradicts that building's own memory without an authored change event.
- A character acting on information they do not know.
- A mission directly granting a conspiracy reveal that should be ambient discovery.
- Player knowledge being updated without a player-facing discovery event.
- A district-fund amount being written to player currency.
- A global organization being exposed too early.
- A story that duplicates an existing mission without meaningful variation.
- A branch with no reachable completion or a consequence with no valid trigger.
- Untraceable rumors or evidence with no source.

## 8. Creator approval boundary

Proceed autonomously with character names, ages, nicknames, alignments, biographies, supporting cast, dialogue, mission design, ordinary businesses and routine implementation choices.

Seek creator approval for:
- Major organization names.
- District names.
- Building names and major named landmarks/brands.
- Overall strategy, central narrative premise or major product direction.
- Changes that contradict explicit creator-approved canon.
- Irreversible publication, financial, security or destructive actions requiring authorization.

An unresolved protected name must not block unrelated production. Use a descriptive placeholder and keep working.

## 9. Memory maintenance and continuity safeguards

- Use stable IDs; names are display labels and may change only through controlled rename records.
- Store event history append-only where possible. Correct mistakes through superseding records, not silent history erasure.
- Distinguish canon, approved proposal, draft, implemented, tested and retired.
- Record who/what created each memory update and which evidence or decision supports it.
- Use explicit versioning and conflict detection for concurrent agents.
- Never let a low-confidence rumor overwrite a verified fact.
- Never let one character's private memory become another character's knowledge without a transfer event.
- Never let one city's local memory silently contaminate another city's story.
- Maintain an unresolved-thread register so mysteries are not accidentally forgotten or prematurely closed.
- Keep a continuity ledger of every major reveal: prerequisites, allowed sources, earliest availability and player-facing disclosure conditions.

## 10. Runtime implementation milestones

1. **Memory contract:** define schemas and stable IDs for all scopes, knowledge claims, events, relationships, arcs and production records.
2. **Memory service:** implement persistent storage, scoped retrieval, versioning, provenance, access controls and conflict handling.
3. **Story Architect orchestration:** implement task planning, bounded generation, specialist delegation, QA and durable backlog updates.
4. **Content authoring pipeline:** validate, preview, simulate, approve and publish content packages.
5. **Live world feedback:** connect missions, NPC schedules, conversations, relationships, district/business state and player discovery to the story agent.
6. **Continuous production:** schedule safe background story-development cycles with quotas, monitoring, pause controls and audit logs.

Do not describe the agent as independent or persistent until memory survives separate sessions, the runtime can retrieve the correct scopes, generated work is validated and saved, and an observable worker loop has passed tests.
