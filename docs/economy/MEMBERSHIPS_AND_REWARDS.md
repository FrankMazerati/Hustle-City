# Hustle City Memberships & Currency Economy

**Canon status:** Membership names, price points, currency-only contents and card exclusion are creator-approved. All quantities and unresolved mechanics below remain TBD.

## Approved membership ladder

| Price | Membership |
|---:|---|
| $9.99 | Hustle City Starter |
| $19.99 | Hustle City Connect |
| $29.99 | Hustle City Boss |
| $39.99 | Hustle City Mogul |
| $49.99 | Hustle City Elite |
| $59.99 | Hustle City Royalty |
| $79.99 | Hustle City Legend |
| $99.99 | Hustle City Empire |

There is no $69.99 tier. Do not change names, order or prices without creator approval.

**Billing cadence is unresolved.** Do not describe these as monthly subscriptions or one-time purchases until the creator decides.

## What membership packages contain

Membership packages may contain only these four established currencies:
- **Hustle Money** — general in-game money.
- **Diamonds** — premium/luxury currency.
- **Poker Chips** — poker activity currency.
- **Wings** — aviation/flying activity currency.

Exact quantities, tier allocations and whether every tier includes all four currencies are TBD.

### No cards in memberships
- No tier includes collectible cards, card packs, card draws, guaranteed card drops or card-collection progress.
- Membership does not grant City Keys, crowns, businesses, properties, vehicles or other ownership entitlements.
- Cards belong to a separate gameplay-earned progression system. The creator has not finalized which activities award cards, the amounts, frequency, eligibility or odds.
- Daily login, poker participation and other activities are candidate card-earning routes only; none is approved as a card source yet.

## Economy goals

Memberships should feel worthwhile while preserving reasons to play consistently, earn rewards through gameplay and make optional individual purchases. Avoid both negligible membership value and excessive currency grants that let players bypass progression or eliminate demand for ordinary purchases.

- Preserve meaningful progression for free players.
- Membership supplements gameplay; it does not replace gameplay.
- Do not make paid membership necessary for core progression.
- Keep all four wallets separate; never silently convert currencies.
- Show exact package contents and price before purchase.
- Balance currency sources against real in-game spending sinks and expected play patterns.

## Daily rewards — separate system

Daily login rewards are separate from membership contents. They should be available to free players and members. Member bonuses, if approved, should be clearly distinguished from the free daily reward.

Exact reward schedule, currency amounts, streak rules, catch-up rules, reset timezone and caps are TBD. Rewards should be modest enough to preserve the value of gameplay earning and optional purchases. Do not grant cards through daily login until the creator approves the card-acquisition system. Server-side claims must be idempotent so retries or reconnects cannot duplicate rewards.

## Card acquisition — unresolved

Potential sources for future consideration include daily login/daily objectives, poker participation or milestones, and other activities across the game. These are ideas, not approved mechanics. The creator will determine the actual card-earning activities and rules.

All card acquisition must respect the approved city-based collection rule: players may acquire cards for a city only while physically present in that in-game city; player-to-player trading is the explicit exception. Preserve pending valid rewards until the player returns to the relevant city.

## Optional individual in-app purchases

Memberships are distinct from the optional store. Players may be able to buy eligible individual items or currency packages without subscribing. Catalog, prices, bundle contents, exchange rates, discounts, limits and eligibility are TBD and require creator approval.

Purchases must display exact price and contents, use the applicable platform billing flow, be verified server-side, credit the correct wallet, be recorded in an auditable ledger and be idempotent against duplicate notifications or retries. Support entitlement restoration/reconciliation where required. Do not promise cash-out or real-world prize value without separate review.

Poker Chips remain a separate activity currency. Any paid Poker Chip purchase, wagering, prize, transfer or redemption feature requires separate product, platform-policy and legal review before implementation.

## Poker Chips → Hustle Money conversion

**Creator-approved feature direction:** A player who has Poker Chips but is short on Hustle Money should be able to exchange some Poker Chips for Hustle Money, then spend the received Hustle Money on eligible ordinary city-life purchases.

This is a conversion between separate wallets, not direct payment of food, drinks or retail purchases with Poker Chips:
- Debit Poker Chips and credit Hustle Money as one atomic, authoritative transaction.
- Record both sides in an auditable server-side ledger.
- Make requests idempotent and protect against replay, duplicate submission, concurrent-spend and rollback exploits.
- Show the exchange quote, amount debited, amount credited, any fee/limit and confirmation before committing.
- Food and beverages remain payable with Hustle Money, not Poker Chips.
- Do not create currency through conversion or bypass store purchase/refund controls.

**Unresolved — do not invent:** exchange ratio, fee, daily/weekly limits, minimum/maximum amount, eligibility of purchased chips versus gameplay winnings, cooldowns, venue/location restrictions, reversal rules, regional/platform restrictions and launch timing.

Because Poker Chips may be purchased, wagered, won or transferred, the conversion mechanic requires separate legal, platform-policy and economy-abuse review before implementation. Do not imply cash redemption or real-world monetary value.


## Poker winnings, lifestyle progression and premium access

**Creator-approved direction:** Connect poker success to the wider Hustle City lifestyle. A player can win Poker Chips at a poker table, visit a staffed cashier or self-service cash-out kiosk, and exchange eligible chips into Hustle Money for eligible in-game spending. The creator specified a **1:1, dollar-for-dollar nominal in-game conversion**: one eligible Poker Chip converts to one Hustle Money. This is an in-game denomination rule, not real-world cash value or cash redemption.

**Creator-approved direction:** Poker is one meaningful earning route, not the only way to participate in or progress through the city. Players should have reasons to socialize, add friends, communicate and share optional social posts. Any social-engagement rewards must encourage authentic participation without requiring public posting or creating spam, fake-account, referral or engagement-farming loops. Reward amounts and qualifying actions remain TBD.

**Creator-approved direction:** Free players retain access to core city life and practical transportation, including walking, public transportation and rideshare-style services (fictional in-world equivalents of services such as Uber/Lyft). The previously established rideable public bus and city L train direction remains relevant. Exact availability, fares and coverage remain TBD.

**Creator-approved premium-lifestyle direction:** Paid packages and/or premium progression may provide access to luxury ownership and services such as personal cars, yachts, private jets and private helicopters. Ordinary free play should not make yachts, private aviation or equivalent luxury access trivially available. The exact boundary between direct purchase, premium entitlement, earned progression, rental/charter access and ownership is not finalized. Preserve meaningful earned paths where directed; do not silently make every vehicle or lifestyle goal pay-only.

**Creator-approved property concept, with parcel details still proposed:** Neighborhood homes should be individually identifiable properties offered for sale when available/unoccupied. Each home needs a stable unique property/house ID and authoritative availability, occupancy and ownership state, so the game can distinguish a vacant listing from an occupied or already-owned home. Players may be able to acquire multiple homes on one block and potentially an entire block; five homes or a whole block are examples, not final ownership caps. A proposed density of roughly 5–10 houses per block is a planning range only, not a locked count.

**Existing world-grid context:** The accepted master layout is a 7×7 grid of 49 large boxes, with six central districts and 43 neighborhood boxes. Each neighborhood box was previously laid out as 5×5 city blocks (25 blocks), yielding 1,075 outer-neighborhood blocks across the 43 neighborhood boxes. This does not determine the number of houses on each individual city block; that remains open.

**Property-system requirements to design:** Unique parcel IDs; address/block/neighborhood linkage; for-sale, reserved, occupied and owned states; authoritative owner records; listing/price/terms; purchase confirmation; transaction history; transfer/resale rules if supported; concurrency protection so two players cannot buy the same parcel; and a clear distinction between owning a house, owning several houses on a block, owning a whole block, and founding/claiming a neighborhood. Neighborhood founding/claiming remains distinct from ordinary home ownership.

**Unresolved — do not invent:** Property prices, exact houses per block, player ownership caps, whole-block purchase rules, rental/resale mechanics, whether homes are bought with Hustle Money, Diamonds or platform purchases, package entitlements, social-reward amounts and limits, rideshare fares, vehicle eligibility, yacht/aircraft access rules, and the precise earned-versus-paid progression boundary. Model the economy and obtain creator approval before locking these details.

**Policy/economy guardrail:** Keep game-currency conversion separate from real-money cash-out. Any real-money purchase, paid currency, poker wagering/prizes, social rewards or premium property/vehicle sale requires platform-policy, legal, consumer-protection and anti-fraud review appropriate to the final design. Do not imply that Poker Chips or Hustle Money are redeemable for real-world money.

## Required balancing work before amounts are set

Do not guess currency quantities. Model:
- All sources: memberships, daily rewards, gameplay, events, achievements and approved purchases.
- All sinks: actual item prices, activity costs, upgrades and other approved spending.
- New/free-player progression and typical play frequency.
- Currency balances accumulated over 7, 30 and 90 days.
- Time-to-afford key purchases and purchase value versus normal gameplay earning.
- Inflation, hoarding, exploit loops and multi-account abuse.
- Poker Chip conversion as a currency sink/source pair, with simulations for arbitrage, farming and circular conversion.

Keep quantities, exchange rates, tier allocations, billing rules and unapproved mechanics marked TBD until creator approval.

## Implementation acceptance requirements

- Store canonical tier IDs, names, prices, billing cadence and entitlements in version-controlled configuration.
- Keep store display prices aligned with platform product configuration and regional pricing.
- Separate membership entitlements, daily rewards and one-time purchases.
- Maintain an authoritative server-side ledger for grants, spends, reversals and purchase receipts.
- Enforce idempotent purchase processing and reward grants.
- Define renewal, expiration, cancellation, refund and grace-period behavior before release.
- Show purchase history and entitlement status.
- Test free-player progression alongside every membership tier.
- Test that membership purchase/renewal never grants cards.
- Test that each currency credits only its correct wallet.
- For conversion, test atomic debit/credit, insufficient balance, stale quotes, retries, simultaneous requests, rollback, caps, fees and abuse detection.

## Decision summary

**Approved:** Eight tier names/prices; no $69.99 tier; membership contents limited to Hustle Money, Diamonds, Poker Chips and Wings; no cards in memberships; cards earned through a separate, not-yet-defined gameplay system; balanced value that preserves play and optional purchase incentives; players can convert Poker Chips into Hustle Money for eligible general city spending.

**Unresolved:** Billing cadence; exact currency quantities and tier allocations; daily reward schedule; card acquisition activities and rules; optional store catalog/prices; conversion ratio, fees, limits and eligibility; Poker Chip monetization and wagering-related features.
