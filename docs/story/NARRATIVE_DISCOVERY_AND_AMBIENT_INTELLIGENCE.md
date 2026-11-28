# Narrative Discovery & Ambient Intelligence System

## Purpose and design rule

This system delivers the hidden Hustle City story through NPCs and the living world. It is deliberately separate from mission completion.

**The player learns the underworld by living in the city, not by checking off mission objectives.**

A mission may change the conditions under which a conversation occurs, but the player does not receive the identity of the Ghost Freight thief simply for finishing a mission. No single NPC should know or explain the entire chain of responsibility.

## 1. Information layers

| Layer | Meaning | Example |
|---|---|---|
| Canonical truth | Actual authored world truth | Who arranged a freight interception |
| Direct evidence | Verifiable observation or record | A matching manifest entry |
| First-hand account | What an NPC personally saw or did | A worker saw an unfamiliar vehicle |
| Second-hand report | What someone was told | A driver heard a supervisor was paid |
| Rumor | Unverified community claim | A district leader is covering for someone |
| Interpretation | Player's inferred explanation | Two disruptions may be connected |
| Misinformation | Deliberately or accidentally false claim | A planted story blaming a rival crew |

Each item stores source, time, location, confidence, reliability, corroboration links, contradictions, visibility conditions and whether the player encountered it.

Do not label rumor as fact in the player UI. The Afterplay Library shows source and status.

## 2. Ambient delivery channels

### Overheard public conversation
NPCs converse in venue queues, sidewalks, train platforms, lobbies, restaurants, shops, parks, markets, work sites, bars and waiting areas. The player may hear only part of a conversation depending on proximity, crowd noise and timing.

### Phone conversations
NPCs speak on phones, listen to voice notes, argue quietly, confirm arrangements or react to a call. The player may hear one side only. Phone dialogue must not magically expose the other participant's identity unless the NPC says it.

### Approaches and interruptions
NPCs may approach the player because of reputation, prior interaction, relationship, opportunity, warning, debt, favor or a rumor about the player. The approach may be unsolicited, timed, conditional or interruptible. Respect player settings and avoid constant intrusive pop-ups.

### Repeat encounters
The same NPC can mention new information later, contradict an earlier statement, correct a rumor, become more guarded or reveal why they withheld something. Track what the player has already heard to avoid repetitive exposition.

### Social and private access
Invitations, private rooms, after-hours meetings, staff corridors, offices, VIP spaces and personal gatherings can expose different conversations. Access can depend on trust, status, favor, introduction, schedule or a discovered access method.

### Public information
News broadcasts, social posts, business notices, event chatter and public announcements provide partial context. Public sources may be incomplete or strategically framed.

## 3. Context selection

Ambient dialogue selection considers:
- Current city, district, neighborhood, venue and exact interaction zone.
- Time of day, day-of-week and event schedule.
- Nearby NPC identities, roles, relationships and current goals.
- NPC knowledge, secrets, fear, loyalty, confidence and willingness to speak.
- Player familiarity, trust, reputation, prior choices and known contacts.
- Relevant mission/business states as context only, not automatic conspiracy revelations.
- Prior rumors and evidence the player has encountered.
- Active world events and current public information.
- Whether the player is alone, in a group, accompanied by Bella or attending a private event.
- Accessibility, subtitles, audio range and player communication preferences.

Use authored content with controlled variation. Do not let a generative dialogue layer invent canonical facts or bypass knowledge boundaries.

## 4. NPC knowledge boundaries

Every NPC receives a bounded knowledge profile:
- What they personally know.
- What they suspect.
- What they heard from someone else.
- What they are hiding.
- What they misunderstand.
- What they would never plausibly know.
- What they are willing to tell this player, under these conditions.

A low-level worker might know a shift changed and a supervisor was nervous, but not who leads the Ghost Network. A business owner may know records disappeared and a contract was redirected. A district-connected figure may know about a private meeting but not its global sponsor.

Even senior local figures should not become omniscient narrators. Ultimate controllers remain hidden through the main storyline.

## 5. Rumor and evidence lifecycle

Recommended status values: unheard, heard_unverified, corroborated, disputed, disproven, confirmed.

A rumor can be heard from multiple sources. Corroboration should consider source independence; three NPCs repeating one original rumor is not automatically three independent confirmations.

The Afterplay Library records:
- Stable information ID.
- Content summary written without asserting more than the player knows.
- Source NPC or public source.
- Location and timestamp.
- Evidence type and status.
- Related people, businesses, districts and events.
- Contradictions and corroborating sources.
- Player's notes/theory, if supported.
- Whether the player can share or discuss the information.

The journal must not reveal a secret merely because the backend knows it.

## 6. Story pacing

1. Ordinary disruptions and missing appointments, deliveries or records.
2. Conflicting explanations and local rumors.
3. Repeated names, unusual access and patterns across businesses.
4. The player discovers the Twelve are coordinated and connected to Frank.
5. The player notices local events may be linked to a larger structure.
6. Late discoveries establish the Inner Circle and the Ghost Network as opposing global organizations.
7. The player encounters city-level counterparts and chooses whether to align with either side.
8. Ultimate Ghost Network controllers remain unknown through the main storyline.

Do not enforce a single linear sequence. District order, relationships and player curiosity alter when and how information is encountered. Use gates only where a prerequisite is necessary for comprehension or access.

## 7. Mission and ambient state integration

Mission outcomes can update business status, assets, revenue, liabilities, district mission funds, NPC trust, access, contact availability, ambient conversation eligibility, invitations and which rumors are contradicted or newly relevant.

Mission outcomes must not automatically:
- Set the player as knowing the freight thief.
- Reveal the Inner Circle or Ghost Network in an early business chapter.
- Mark a rumor as confirmed without evidence.
- Force a player to meet every supporting NPC.
- Make one NPC omniscient.

## 8. Example ambient scene

**Location:** After Hours venue lobby, late evening.

Two venue workers talk while checking a guest list. One says a regular executive has stopped arriving. The other says the executive's office has been asking about a shipment manifest that should have been archived weeks ago. A third person approaches, notices the player nearby and changes the subject.

The player may keep listening, walk away, ask one worker what they meant, or later contact a known venue employee. Another source may give a different version.

No one explains who stole the freight. The scene adds a lead and a human reaction. If the player later finds an independent record, the rumor may become corroborated.

## 9. Acceptance criteria

- A player can complete all required missions in a district without automatically receiving the hidden conspiracy answer.
- Ambient information respects NPC knowledge and player discovery state.
- The same rumor does not repeat as new information once heard unless status or context materially changes.
- Rumors and evidence remain distinguishable in storage and UI.
- Contradictory accounts are supported.
- NPCs can approach the player based on authored state and relationship rules.
- Player knowledge is not inferred from backend canonical truth.
- Story reveals can occur across districts and in flexible order.
- QA can replay a scenario and verify why a conversation was or was not eligible.
