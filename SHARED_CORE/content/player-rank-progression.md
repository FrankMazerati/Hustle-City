# Player Status, Career Level, and Star Progression

**Status:** Creator-approved core rank families and activity-based progression direction. Exact descriptor mapping, formulas, reward values, star-rank names, thresholds, and prestige mechanics remain open for later design.
**Scope:** Player-facing recognition and progression. This document defines the conceptual tracks and approved activity sources, not numerical balancing or implementation details.

## 1. Career level and rank

Hustle City uses a 100-level status ladder divided into ten consecutive prestige families. Each family contains ten levels. The family/status word advances every ten levels, while a rising descriptor communicates the player's standing within that family.

The ten families, in order, are:

1. Hustler — Levels 1–10
2. Boss — Levels 11–20
3. Playmaker — Levels 21–30
4. Game Changer — Levels 31–40
5. Big Mover — Levels 41–50
6. Mogul — Levels 51–60
7. Powerhouse — Levels 61–70
8. Heavyweight — Levels 71–80
9. Legend — Levels 81–90
10. Icon — Levels 91–100

### Ten-level descriptor ladder

The following is the current working descriptor sequence for each ten-level family:

1. Small-Time
2. Lightweight
3. Rising
4. Mid-Level
5. Established
6. Heavyweight
7. Big-Time
8. Elite
9. Master
10. Supreme

Combine the descriptor with the family title. Examples:

- Level 1: Small-Time Hustler
- Level 10: Supreme Hustler
- Level 11: Small-Time Boss
- Level 19: Master Boss
- Level 20: Supreme Boss
- Level 91: Small-Time Icon
- Level 100: Supreme Icon

The descriptor list is a working naming set. The creator has approved the ten-family progression and the overall rising-title concept; individual descriptor placement and alternatives such as "Big Boss" can be tuned without changing the ten-family structure.

## 2. Activity-based career progression

Career level should rise through meaningful participation in the game, not solely through one narrow activity. Approved progression sources include:

- Daily logins and consistent return play.
- Winning at the poker table.
- Winning at casinos.
- Winning other games and competitive activities.
- Participating in the wider game world and completing eligible activities.
- Interacting with NPCs and other real players.

These activities should contribute to career progression through a progression/experience system. The amount awarded, daily limits, anti-exploit rules, and exact eligibility criteria are implementation and balancing decisions still to be designed. A login reward should recognize consistent participation without making repeated logins or low-effort farming the dominant route to rank.

## 3. Separate star-points and star-rank system

In addition to the main career level and rank, Hustle City should have a distinct star-based recognition track. Stars represent social recognition and reputation earned through participation and meaningful interactions in the city.

### Star points accumulate from individual actions

Each eligible interaction or activity can award a defined amount of **star points**. Small actions may award a small amount; more meaningful, involved, or socially valuable actions may award more. Star points accumulate toward the player's next star rank. The player should be able to earn star points regularly, but the system should not hand out excessive rewards for repetitive or empty actions.

Creator-identified qualifying activities include:

- Initiating conversations with people encountered on the streets.
- Having meaningful conversations and interactions with NPCs.
- Having meaningful conversations and interactions with other real players.
- Adding friends.
- Trading cards with other players.
- Buying poker chips or making eligible purchases / transactions at the poker table.
- Other meaningful interactions with people, businesses, and activities around the city as the system is expanded.

These are intended as distinct activity/reward opportunities. The design should assign each eligible action its own configurable star-point value rather than treating every interaction as identical. The exact point values, caps, cooldowns, and thresholds are not yet defined.

### Star ranks

The accumulated star points should also have their own rank progression. As players earn and accumulate points, they advance through increasingly prestigious star ranks. This creates a second visible status measure alongside the career level/title.

The names and number of star ranks, star-point thresholds, visual treatment, rewards, and whether star ranks ever reset or decay remain open design decisions. Do not assume a five-star cap or invent numerical thresholds.

### Keep career and stars distinct

The star track is distinct from the 100-level career ladder:

- **Career level/rank** communicates overall game progression and the player's Hustler-to-Icon journey.
- **Star points/star rank** communicate social recognition and interaction-based standing.

Some actions may contribute to both tracks where explicitly balanced, but the systems must remain separately tracked and understandable.

### Integrity and anti-abuse

Reward meaningful play rather than raw interaction volume. Design safeguards against reciprocal farming, spam, harassment, scripted interactions, repeated low-effort conversations, fake friend-add cycles, and card-trading loops intended only to farm points. Consider diminishing returns, eligibility checks, cooldowns, and daily caps during balancing; exact controls remain to be designed.

## 4. Post-Level-100 prestige

After Level 100, the progression may cycle into a prestige/reset system rather than ending. The first proposed prestige naming direction is **Hustler Platinum I** (also expressible as Hustler Platinum 1). Further Platinum tiers and additional prestige names can be developed later.

This post-100 system is an approved direction to explore, but its exact tier names, reset rules, numbering, rewards, and progression mechanics are not yet defined.

## 5. Design rules

- Preserve the exact ten-family career-rank order listed above.
- Each career family occupies exactly ten levels.
- The descriptor rises within each family; the family title changes at the next ten-level boundary.
- Career progression must recognize multiple forms of play, including daily participation, poker/casino and other game wins, and eligible social interaction.
- Maintain a separate star-points and star-rank track, with NPC and real-player interactions as important earning paths.
- Assign configurable star-point values to individual eligible actions; do not award identical amounts automatically for every interaction.
- A single activity may contribute to both career XP and star points only when explicitly balanced and designed to do so.
- Use career titles and star rank in appropriate player-facing surfaces (for example, profile, player card, progression screen, and social displays), subject to later UX design.
- Do not invent XP thresholds, star-point values, star-rank thresholds, reward values, gameplay advantages, or unlocks from this specification.
- Keep the prestige-after-100 structure extensible; do not lock the project into only one prestige naming scheme yet.
