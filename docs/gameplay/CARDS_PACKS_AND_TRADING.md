# Hustle City — Collectible Cards, Packs and Trading

## 1. Purpose
Cards are collectible game items with at least two distinct roles: collection/progression and configured five-card building unlock sets. Do not assume every card is an ownership key; card metadata states its function.

## 2. Card catalogue
Each card definition needs: card_definition_id, display_name, artwork_asset_id, collection_id, set_id, rarity_tier (only after tiers are approved), card_number, description/lore, acquisition_sources, trade_policy, duplicate_policy, building_unlock_target (nullable), release_window, version and creator approval. Each owned instance has a unique instance_id, owner_player_id, acquisition_source, acquired_at, bound/locked state and trade history.

## 3. Five-card building collection
For each configured building, author exactly five explicit card slots and map the completed set to one stable building_id. UI displays 0/5 through 5/5, card artwork, missing slots, eligible sources and target building. On completion, server verifies ownership and set membership before issuing the configured unlock entitlement.

**Critical unresolved rule:** whether the five cards are consumed, remain in the collection, or become locked as an ownership proof. The implementation must support a configurable policy but must not choose one without creator approval. Ownership claim can also have separate eligibility or capacity rules; completion must not silently override them.

A set completion is not automatically a building deed if the creator defines it as an unlock/eligibility key. The exact sequence (complete set → unlock claim → claim/activate ownership) must be shown clearly.

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

## 5. Acquisition catalogue
The card catalogue should identify each permitted source separately: earned gameplay rewards, event rewards, referral rewards if approved, card packs, direct purchase of a specified missing card if approved, and player-to-player trade. The exact source list and eligibility are unresolved. Store listings must clearly distinguish randomized packs from guaranteed single-card offers.

## 6. Player-to-player trading
Trade flow:
1. Player A selects a friend/eligible player and offers one or more tradeable card instances.
2. Player B proposes counter-items or accepts the offer.
3. Both sides see exact cards, ownership, bound status and any currency component if such trades are ever approved.
4. Both players confirm the final immutable offer.
5. Server rechecks ownership, tradeability, account restrictions and offer version.
6. Atomic swap occurs; both inventories and trade ledger update together.
7. Both players receive a receipt/notification.

No card can be in two active trades simultaneously. Reject stale offers, missing items, bound cards, duplicate confirmations and attempts to transfer non-tradeable entitlements. Trade cancellation/expiry returns offered cards to available inventory. A currency-plus-card trade is disabled unless explicitly approved. Include block/report controls and scam warnings; no external payment or off-platform settlement.

## 7. Duplicate cards
Duplicate handling is unresolved. The system must support one or more creator-selected policies: keep duplicates for trading; allow duplicates toward separate sets only if the rules say so; convert duplicates to a defined reward only if approved; or mark duplicates as non-tradeable. Do not auto-convert duplicates by default.

## 8. Anti-abuse and QA
Test pack purchase retries, server timeout, duplicate grants, manipulated client odds, card duplication, concurrent trades, trade cancellation, blocked players, bound cards, set completion, ownership claim, refund/revocation, and version changes to card sets. Audit every acquisition and transfer.
