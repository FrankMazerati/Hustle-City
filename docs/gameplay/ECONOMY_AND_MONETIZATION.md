# Hustle City — Economy, Wallets and Monetization

## 1. Currency definitions
| Currency | Meaning | Primary uses | Must not be used for |
|---|---|---|---|
| Hustle Money | General in-game cash | Ordinary goods/services, eligible vehicle/property/business upgrades, basic rides where priced | Poker stakes unless explicitly configured; premium-only travel |
| Diamonds | Premium currency | Premium travel choices and approved premium store goods | Mandatory basic travel or essential social access |
| Hustle City Poker Chips | Virtual game chips | Poker and approved chip-based table activities | General retail, cash-out or real-world redemption |

No implicit conversion. If conversion is later approved, it needs an explicit exchange screen, rate, limits, cooldown, server transaction and audit record.

## 2. Wallet rules
Each player wallet has separate integer balances (or fixed-precision values if the economy later requires fractional units), lifetime earned/spent totals, pending platform grants, transaction history and fraud/risk flags. The server is authoritative. A balance update and its ledger entry are one atomic operation.

Every transaction records: transaction_id, player_id, currency, signed amount, reason_code, source_system, reference_id, idempotency_key, timestamp, status and audit metadata. Never store payment card details.

## 3. Sources and sinks
Create a creator-approved economy table for every earn/spend source. Candidate sources requiring balancing include gameplay rewards, approved missions/events, referrals, business revenue and platform packages. Candidate sinks include clothing/accessories, ordinary services, eligible upgrades, card packs and premium travel. These are categories, not final reward rates or prices.

## 4. Basic and premium travel
- Basic public transit and ordinary rideshare remain available without Diamonds.
- Basic services may be free or use Hustle Money, according to the specific service.
- Premium travel options may use Diamonds.
- Before confirmation show origin, destination, service tier, currency, fare, party/seat constraints and refund/cancellation rule.
- Never charge until the server reserves the travel service and confirms the quoted fare.
- If travel fails before departure, refund or release the reservation automatically. If interrupted after departure, apply the published service-specific policy; never silently consume a premium fare.
- Exact Diamond fares, tiers and routes are unresolved.

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
