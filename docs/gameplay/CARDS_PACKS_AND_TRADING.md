# Hustle City — Collectible Cards, Packs and Trading

## 1. Purpose
Cards are collectible game items with at least two distinct roles: collection/progression and configured five-card building unlock sets. Do not assume every card is an ownership key; card metadata states its function.

## 2. Card catalogue
Each card definition needs: card_definition_id, display_name, artwork_asset_id, collection_id, set_id, rarity_tier (only after tiers are approved), card_number, description/lore, acquisition_sources, trade_policy, duplicate_policy, building_unlock_target (nullable), release_window, version and creator approval. Each owned instance has a unique instance_id, owner_player_id, acquisition_source, acquired_at, bound/locked state and trade history.

## 3. Standard five-card ranked ownership collection

**Recommended standard:** five ranked cards per eligible building, boat/yacht collection and car/dealership collection. This preserves the creator's earlier five-card progression decision and avoids making every ownership collection unnecessarily grind-heavy. The beach is explicitly excluded from this card-collection ownership requirement.

Each asset collection is a five-step rank ladder, ordered from entry level to the highest rank. The five cards are not five unrelated collectibles: each card represents the next rank in that asset's themed progression. Completing all five ranks completes the collection and unlocks the corresponding ownership claim. The fifth/top-rank card is part of the five; do not add a separate sixth ownership card.

Draft examples only; rank names require creator approval:
- Yacht/boat: Deck Hand → Yacht Crew Member → First Mate → Captain → Yacht Master.
- Car dealership: Lot Attendant → Sales Associate → Sales Consultant → Sales Manager → Dealership Owner.
- Music Studio precedent from earlier design: Runner → Artist → Music Producer → Record Label Owner → building ownership. The exact fifth-card label should be authored consistently with the chosen card-rank presentation.

Every other eligible building gets its own five-card ladder with role/title names appropriate to that venue or business. Do not reuse yacht or dealership titles indiscriminately. The beach is excluded. The creator may later approve special ten-card prestige collections, but ten cards are not the baseline and must not be silently substituted.

**Asset scope to confirm in content authoring:** distinguish collecting a card set to own the car dealership/building from collecting a separate set to unlock an individual car or boat. Do not assume one collection grants both the venue and every vehicle sold there.

## 3. Five-card building collection
For each configured building, author exactly five explicit card slots and map the completed set to one stable building_id. UI displays 0/5 through 5/5, card artwork, missing slots, eligible sources and target building. On completion, server verifies ownership and set membership before issuing the configured unlock entitlement.

**Critical unresolved rule:** whether the five cards are consumed, remain in the collection, or become locked as an ownership proof. The implementation must support a configurable policy but must not choose one without creator approval. Ownership claim can also have separate eligibility or capacity rules; completion must not silently override them.

A set completion is not automatically a building deed if the creator defines it as an unlock/eligibility key. The exact sequence (complete set → unlock claim → claim/activate ownership) must be shown clearly.


## 3A. Venue-specific completion rewards (creator direction)

The five-card collection standard applies to each configured building/venue collection, including the casino experience. Completion rewards are venue-specific and must not be interpreted as automatic ownership of the entire venue.

- **Hustle Towers:** a new player may begin by renting an apartment. Completing the five-card collection for that apartment permanently unlocks ownership of that specific apartment, subject to the configured claim/eligibility flow. The exact rent terms, apartment inventory and card rank titles remain TBD.
- **Shuffle Club / casino:** players do not own the Shuffle Club or its casino. Completing the relevant five-card collection may unlock a private room inside the Shuffle Club. The private-room entitlement is distinct from venue ownership and casino operation. Confirm whether the casino experience uses its own five-card set or shares the Shuffle Club set before implementation.
- **Velvet Lounge:** it receives its own five-card collection; the exact completion privilege is TBD. Do not assume venue ownership.
- **Hustle Club, Hustle City Marina and Yacht Club, American Swagger Clothing, the car dealership, Upper Level Entertainment Studios, Upper Level Films and Monster Beats:** create venue-specific five-card collections where configured; each completion reward must be explicitly authored. Do not infer ownership from the existence of a collection.
- **Beach:** excluded from the five-card building collection requirement.

The marina/yacht club venue collection is separate from individual boat/yacht collections. The car dealership collection is separate from individual car collections. Collecting a venue set never grants every vehicle sold, stored or hosted there.

Maintain a creator-approved building/venue registry with stable building_id, canonical display name, category, collection_id (nullable), five card slots, completion_reward_type, completion_entitlement_id, rental/ownership rules and approval status. Do not add brands, streets, districts, transport hubs or decorative background structures as owned buildings without explicit creator direction.
## 3B. Creator-approved ownership and production rewards

The five-card collection unlocks the player's specific asset or privilege, not necessarily the host building:
- **Monster Beats:** the player does not own the Monster Beats building or production company. The player owns a studio within the Monster Beats facility and can produce music there. The exact studio naming, production-company relationship, operating rights and upgrade catalogue remain to be authored.
- **Upper Level Films / Upper Level studio:** the player can establish and operate their own film crew and make movies, using the Upper Level studio/production facility. The player's crew/production operation is distinct from ownership of the studio building. Confirm the exact relationship between Upper Level Films and Upper Level Entertainment Studios in the content registry.
- **Car dealership:** completion can grant ownership of a car lot, not automatic ownership of the entire dealership group or every vehicle.
- **Clothing retail:** completion can grant ownership of a clothing store.
- **Yacht:** completion grants ownership of the specific yacht, never the Hustle City Marina and Yacht Club.
- **Hustle Club:** eligible collection can grant ownership of the Hustle Club venue/business.
- **Velvet Lounge:** eligible collection can grant ownership of the lounge venue/business.
- **Shuffle Club / casino:** collection grants a private room inside the casino/club only; no ownership of the Shuffle Club or casino.
- **Hustle Towers:** apartment collection grants permanent ownership of the specific apartment; rental is a separate starting/temporary state.

These are different entitlement types and must be represented separately in card-set configuration. Do not label a studio, car lot, clothing store, yacht, crew, private room or business as ownership of its host building unless the creator explicitly says so.

## 4. Card pack system
A pack definition includes pack_id, display_name, theme/set, price_currency, price_amount (TBD), guaranteed contents, random slots, odds table, duplicate protection policy, eligibility, repeatability, availability window and disclosure text. Pack opening is a server-authoritative operation:
1. Confirm pack is available and player is eligible.
2. Show cost, contents/odds and duplicate policy.
3. Confirm purchase.
4. Atomically debit currency and create a unique pack-opening record.
5. Server generates contents from the approved versioned odds table.
6. Grant card instances and record pack result.
7. Show reveal animation and collection progress.
8. Reconcile any failed response through idempotent request ID; never charge twice or grant twice.

Do not invent pack names, prices, odds, rarity tiers, guaranteed cards or limited-time schedules.

## 5. Daily login, poker and building-pack acquisition
Building card packs must be part of the daily engagement loop, not only a store product.
- The reward schedule should be able to grant a building-specific card pack or a selectable building pack as a daily login reward.
- Daily rewards can also include individual cards or card-pack fragments only if that reward type is explicitly configured.
- Playing poker can earn card rewards through approved gameplay milestones, session objectives, tournament/event placement or other defined achievements. Poker Chips remain the currency used to play poker; they are not a card-reward currency and are not automatically debited to award cards.
- Poker card rewards must be based on participation/achievement rules that are published and balanced; do not reward only high-stakes play or encourage wagering to obtain essential progression cards.
- The seven-day login streak may award a higher-value or selectable building pack as its special bonus. Exact pack tier, card count and selection rules remain TBD.
- The daily prize wheel may include approved building packs or card rewards, with the same server-authoritative odds disclosure and anti-duplication controls.
- Pack catalogue must support a pack associated with each eligible building/set, plus any approved general or event pack. Do not invent building names, card contents, rarity or odds.
- Rewarded packs use the same server-side pack-opening and inventory grant path as purchased packs; free does not mean client-authoritative.

## 6. Acquisition catalogue
The card catalogue should identify each permitted source separately: earned gameplay rewards, event rewards, referral rewards if approved, card packs, direct purchase of a specified missing card if approved, and player-to-player trade. The exact source list and eligibility are unresolved. Store listings must clearly distinguish randomized packs from guaranteed single-card offers.

## 7. In-game card discovery and social trading
The complete card-trading experience lives inside Hustle City. Players must not need a companion app, external website, Discord server, Facebook group or spreadsheet to find trading partners, negotiate or complete exchanges.

### Card Album and collection visibility
- Each player has a Card Album showing each building collection, the five required slots, cards owned, missing cards and duplicate counts.
- The album supports search/filter by building, set, card name/ID, owned/missing/duplicate status and trade eligibility.
- Players can choose whether their collection progress, duplicate inventory and wish list are visible to friends, eligible traders or nobody. Respect privacy settings and blocks.
- A player may mark missing cards as wanted and maintain a wish list. They can remove or change a request at any time.

### Friend discovery and relationships
- Players can search/add another player using approved in-game identifiers, send a friend request, accept/decline, remove friends, block and report.
- A trade can be initiated from a friend's profile, the Card Album, a card's detail screen, a wish-list match or the in-game Card Finder.
- Friend status and trade eligibility are checked by the server. Being friends does not override blocks, account restrictions or card binding.
- Provide optional in-game messaging or a trade conversation thread; keep private messages private and provide mute/report controls.

### In-game Card Finder and matching
- Players can search for a specific missing card and see eligible players who have a tradeable duplicate, subject to each player's visibility settings.
- Finder can show reciprocal matches (what I need / what they need), suggested fair swaps based on card metadata and duplicate availability, and filters for friends/available traders.
- Players can create a trade request with requested card(s) and offered card(s), set an expiry, edit/cancel before acceptance and receive in-game notifications.
- Finder must never expose hidden inventory, private account details or precise player location.
- No external trading communities or companion app are required for discovery or completion.

### Safe multi-card exchange
- Support one-for-one and multi-card-for-multi-card offers. Both sides see every card instance and the exact final terms before approval.
- Cards remain reserved/locked while an offer is pending; they cannot be offered in another trade, consumed, sold or used to complete another transaction.
- Either side may counter, decline or cancel while allowed by the trade state. A counteroffer creates a new version and requires both players to approve that exact version.
- The server revalidates ownership, duplicates, tradeability, friend/block state, account restrictions and offer version at final acceptance.
- The exchange is atomic: all items transfer together or none transfer. No partial completion, double spend, duplicate card, or one-sided loss.
- If an offer expires or is canceled, all reserved cards return to available inventory. A disconnected player can resume and see the authoritative trade state.
- Default design: card-for-card only. Any currency, real-money or off-platform consideration is disabled unless separately approved. Never allow real-money settlement through chat or trade notes.

### Trust, limits and moderation
- Provide trade history and receipts showing cards exchanged, participants, timestamps and final state.
- Establish configurable new-account safeguards, trade rate limits, daily limits if needed, suspicious-activity detection and cooldowns. Exact limits remain TBD.
- A reputation indicator may reflect verified completed trades and upheld moderation findings; do not allow users to buy reputation or publicly shame players based on unverified accusations.
- Report trade fraud, impersonation, harassment and coercion. Moderators need auditable tools to investigate without silently rewriting inventories.
- Support trade dispute review, but never promise automatic reversal after a completed valid exchange. Any administrative correction must be permissioned, logged and auditable.

## 8. Player-to-player trading
Trade flow:
1. Player A selects a friend/eligible player and offers one or more tradeable card instances.
2. Player B proposes counter-items or accepts the offer.
3. Both sides see exact cards, ownership, bound status and any currency component if such trades are ever approved.
4. Both players confirm the final immutable offer.
5. Server rechecks ownership, tradeability, account restrictions and offer version.
6. Atomic swap occurs; both inventories and trade ledger update together.
7. Both players receive a receipt/notification.

No card can be in two active trades simultaneously. Reject stale offers, missing items, bound cards, duplicate confirmations and attempts to transfer non-tradeable entitlements. Trade cancellation/expiry returns offered cards to available inventory. A currency-plus-card trade is disabled unless explicitly approved. Include block/report controls and scam warnings; no external payment or off-platform settlement.

## 9. Duplicate cards
Duplicate handling is unresolved. The system must support one or more creator-selected policies: keep duplicates for trading; allow duplicates toward separate sets only if the rules say so; convert duplicates to a defined reward only if approved; or mark duplicates as non-tradeable. Do not auto-convert duplicates by default.

## 10. In-game card trading acceptance
- A player can add another player as a friend and initiate a card trade entirely in Hustle City.
- A player can search for a missing card and discover eligible traders without leaving the game.
- Collection visibility and wish-list visibility obey player privacy settings.
- A player can make a multi-card offer, receive a counteroffer and approve the final terms.
- No card transfers until both sides approve the same offer version.
- Cards in pending offers are reserved and cannot be spent, reoffered or used to satisfy another transaction.
- Concurrent trade attempts, reconnects, retries and stale offers cannot duplicate or destroy cards.
- Decline, cancel and expiry release all reserved cards.
- Blocked users cannot contact or trade with the blocking player; reports are routed to moderation.
- Trade history and audit records are available to players and authorized support staff under role controls.
- The full experience works without external trading apps, websites or social groups.

## 11. Anti-abuse and QA
Test pack purchase retries, server timeout, duplicate grants, manipulated client odds, card duplication, concurrent trades, trade cancellation, blocked players, bound cards, set completion, ownership claim, refund/revocation, and version changes to card sets. Audit every acquisition and transfer.


## 12. Expandable catalogue and live progression

The master asset/entitlement catalogue and future expansion rules live in [Ownership Card Catalogue and Live Progression](OWNERSHIP_CARD_CATALOGUE_AND_LIVE_PROGRESSION.md). Treat that document as the source of truth for asset targets, host-building boundaries, future card-pack releases and progression tracks. New collections use stable IDs and versioned definitions; adding content must not require hard-coded schema changes or invalidate existing cards, trades, completed sets or entitlements. Five cards remain the standard ownership collection unless the creator approves another format. Player level, XP, stats, reputation, stars and achievements are separate expandable progression tracks, not synonyms for card collection completion.
