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

## Required balancing work before amounts are set

Do not guess currency quantities. Model:
- All sources: memberships, daily rewards, gameplay, events, achievements and approved purchases.
- All sinks: actual item prices, activity costs, upgrades and other approved spending.
- New/free-player progression and typical play frequency.
- Currency balances accumulated over 7, 30 and 90 days.
- Time-to-afford key purchases and purchase value versus normal gameplay earning.
- Inflation, hoarding, exploit loops and multi-account abuse.

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

## Decision summary

**Approved:** Eight tier names/prices; no $69.99 tier; membership contents limited to Hustle Money, Diamonds, Poker Chips and Wings; no cards in memberships; cards earned through a separate, not-yet-defined gameplay system; balanced value that preserves play and optional purchase incentives.

**Unresolved:** Billing cadence; exact currency quantities and tier allocations; daily reward schedule; card acquisition activities and rules; optional store catalog/prices; Poker Chip monetization and wagering-related features.
