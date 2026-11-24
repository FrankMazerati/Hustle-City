# Hustle City — Economy, Wallets and Monetization

## 1. Currency definitions
| Currency | Meaning | Primary uses | Must not be used for |
|---|---|---|---|
| Hustle Money | General in-game cash | Ordinary in-game purchases, services, clothing, jewelry and eligible property/business upgrades | Poker play, flying, and premium boat/car purchases reserved for Diamonds |
| Diamonds | Premium transport/vehicle currency | Boats and cars, including eligible purchase/upgrade transactions defined by the vehicle and marine catalogues | Poker play, flyer distribution or ordinary everyday in-game purchases |
| Wings | Flight currency | Flying and approved air-travel/flight services | Flyer promotion, poker/table play or boat/car purchases |
| Hustle City Poker Chips | Virtual game chips | Poker and approved chip-based table activities | General retail, cash-out or real-world redemption |

No implicit conversion. If conversion is later approved, it needs an explicit exchange screen, rate, limits, cooldown, server transaction and audit record.

## 2. Wallet rules
Each player wallet has separate integer balances (or fixed-precision values if the economy later requires fractional units), lifetime earned/spent totals, pending platform grants, transaction history and fraud/risk flags. The server is authoritative. A balance update and its ledger entry are one atomic operation.

Every transaction records: transaction_id, player_id, currency, signed amount, reason_code, source_system, reference_id, idempotency_key, timestamp, status and audit metadata. Never store payment card details.

## 3. Sources and sinks
Create a creator-approved economy table for every earn/spend source. Candidate sources requiring balancing include gameplay rewards, approved missions/events, referrals, business revenue and platform packages. Candidate sinks include clothing/accessories, ordinary services, eligible upgrades, card packs and premium travel. These are categories, not final reward rates or prices.

## 4. Transport, vehicles and flight
- **Diamonds** are used for boats and cars, including their approved purchase/upgrade transactions.
- **Wings** are used for flying / air-travel services.
- **Hustle Money** is for ordinary in-game purchases and services.
- Basic transport rules, if any, must be specified separately; do not silently charge Diamonds or Wings for ordinary everyday activity.
- Quote the exact currency and fare before confirmation; reserve then charge atomically.
- Exact vehicle/boat prices, flight fares, routes and upgrade costs remain unresolved.

## 4. Vehicle, boat and flight currency rules
- Boats and cars use Diamonds under their approved purchase and upgrade rules.
- Flying and air-travel services use Wings.
- Hustle Money is used for ordinary in-game purchases, goods, services and eligible upgrades.
- Poker Chips are used to actually play poker and other explicitly chip-denominated table activities.
- The exact fare, route, vehicle class, ownership and upgrade rules remain unresolved. The UI must show the required currency and exact price before confirmation.
- Do not charge a player until the server validates availability and reserves the transaction. Failed transactions must not debit a wallet.

## 5. Poker Chips
Poker Chips are separate from the other currencies. The initial policy is non-redeemable virtual chips with no cash-out. A table buy-in, ante, stake, payout and rake (if any) must be denominated in Poker Chips and recorded by the game server. The table must disclose limits before joining. No real-money wagering is specified.

## 6. Google Play packages and purchases
Build a server-validated product catalogue. Potential package categories:
- Starter / welcome packages.
- Hustle Money bundles.
- Diamond bundles.
- Poker Chip bundles, subject to platform and legal review.
- Card packs or a specific final missing card only if explicitly approved and odds/contents are disclosed as required.
- Clothing and accessory bundles.
- Vehicle cosmetic or upgrade packages.
- Apartment/property upgrade packages.
- Business upgrade packages.

For every SKU define product_id, display_name, description, platform_product_id, region availability, price supplied by the platform, contents, grant rules, repeatability, purchase limits, refund/revocation behavior, eligibility, disclosure and approval state. Do not hardcode regional prices; retrieve the platform price. The store must not imply a package guarantees a random item unless it truly does.

### Receipt flow
1. Client requests product catalogue from server.
2. Client initiates Google Play Billing purchase.
3. Client sends purchase token/receipt to backend.
4. Backend verifies with Google Play, checks product ID, package state, account binding and prior use.
5. Backend atomically records entitlement and grants contents with idempotency.
6. Client refreshes authoritative inventory/wallet.
7. Refund/revocation notifications trigger entitlement reconciliation under published rules.

Never grant an item solely because the client reports purchase success. Handle pending, canceled, failed, duplicate, refunded and revoked states.

## 7. Fairness and consumer protection
- Show currency and real-money price separately.
- Disclose randomized pack odds before purchase/opening where required.
- Avoid pay-to-win; essential social participation and basic transportation remain accessible.
- Provide purchase confirmation and platform refund/support route.
- Do not create deceptive countdowns, false scarcity or misleading discounts.
- Apply age, jurisdiction and platform rules, especially to poker/chip packs and randomized content.
- No monetization feature should sell a player's private location, messages or social graph.

## 8. Unresolved economy worksheet
All values intentionally TBD: starting Hustle Money, starting Diamonds, starting Poker Chips, daily earn rates, referral payouts, card pack prices, individual card purchase eligibility, upgrade prices, travel fares, limits, bundle contents, taxes/regions, refund rules and premium entitlements.


## 9. Login rewards and prize-wheel economy
- Daily login rewards and seven-day streak bonuses are server-issued economy grants.
- The standard reward pool includes Hustle Money, Diamonds and Poker Chips. Wings inclusion remains a creator decision; do not assume it is part of the routine daily grant.
- A separate seven-day completion bonus is granted in addition to the seventh daily reward.
- A proposed optional daily prize wheel may grant Hustle Money, Diamonds or Poker Chips; Wings only if explicitly approved.
- Exact quantities, wheel probabilities, reset boundary, missed-day/streak policy and reward calendar remain TBD.
- The wheel outcome must be server-selected, odds disclosed, and grant idempotent. No paid spin is authorized by this specification.
- Track daily and weekly currency issuance and compare it with sinks to control inflation.

## 9. Final creator-confirmed currency definitions
There are exactly four currencies: **Hustle Money, Diamonds, Wings and Poker Chips**. There is no separate “poker money” balance.
- Hustle Money: ordinary in-game purchases, goods, services and eligible upgrades.
- Diamonds: boats and cars, including approved purchase/upgrade flows.
- Wings: flying and air-travel services.
- Poker Chips: actually playing poker and chip-denominated table activities.

Never substitute one currency for another. The full In-App Store, memberships, rewards, ads and owner dashboard are specified in [Hustle Club Memberships and Package Store](HUSTLE_CLUB_MEMBERSHIPS_AND_PACKAGE_STORE.md).

The full Hustle City In-App Store, six candidate Hustle Club monthly price points, one-time currency/item packages, daily login rewards, bar recovery loop, advertising formats, revenue forecasting and owner dashboard are specified in [Hustle Club Memberships and Package Store](HUSTLE_CLUB_MEMBERSHIPS_AND_PACKAGE_STORE.md). Exact benefit quantities, package contents, reward amounts and prices remain subject to creator approval.
