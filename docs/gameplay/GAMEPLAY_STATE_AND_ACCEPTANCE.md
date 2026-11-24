# Hustle City — Gameplay State and Acceptance Criteria

## 1. Shared identifiers
All systems must use stable IDs for player, account, currency, transaction, card definition, card instance, collection, pack, building, ownership, property, business, vehicle, catalogue item, event, venue, travel booking, referral and social post. Avoid display-name joins and duplicate sources of truth.

## 2. Authority boundaries
Server-authoritative: balances, ledger, paid entitlements, card ownership, pack outcomes, trades, collection completion, building unlock/claim, property/business ownership, upgrade effects, travel charges, referral qualification, event capacity and moderation state. Clients request actions and display confirmed state.

## 3. Cross-system invariants
- Three currencies never merge or silently convert.
- Basic transportation never requires Diamonds.
- Poker Chips are non-redeemable virtual chips under the baseline.
- A five-card set unlocks only its configured building entitlement.
- Building ownership is distinct from neighborhood ownership, crew leadership and residency.
- Card trade is atomic and cannot duplicate or destroy cards.
- Platform purchase grants only after server receipt validation.
- Social privacy applies consistently to feeds, map, convoys and notifications.
- Private messages never leak into public feeds.
- Event hosting requires venue rights and respects capacity.
- Every paid/earned grant has an auditable transaction or entitlement record.
- All retries are idempotent.
- No player death; safety/recovery rules remain in force.

## 4. End-to-end acceptance scenarios
1. New player joins, creates profile, sees three separate wallet balances and understands their uses.
2. Player takes a basic ride using free/Hustle Money service without Diamonds.
3. Player selects premium travel, sees Diamond fare and confirms before debit.
4. Player opens a card pack; server records one debit and one unique result despite retry.
5. Player obtains four of five building cards; UI shows 4/5 and does not unlock building.
6. Player obtains the fifth required card; exact configured building unlocks; claim flow checks availability and eligibility.
7. Player claims the building; ownership appears in map/profile/dashboard after reconnect.
8. Owner upgrades the venue; wallet and upgrade state update atomically.
9. Owner schedules a party, invites crew, posts to permitted venue feed and receives RSVPs.
10. Player shares “I just joined Hustle City. Join me over here. Here's my link” externally; attribution is tracked without exposing private data.
11. Qualified referral grants only the approved rewards once.
12. Two players trade cards; concurrent attempts cannot duplicate or lose an instance.
13. Player hides location; feed/map/convoy presence respects the choice.
14. Google Play purchase is pending/canceled/refunded; no unauthorized grant remains.
15. Player buys clothing/accessory and equips it; ownership persists across sessions.
16. Vehicle/apartment/business upgrade validates prerequisites and shows only implemented effects.
17. Event reaches capacity; extra RSVP/entry is rejected gracefully and host sees accurate count.
18. Player disconnects during travel, trade, pack opening or purchase; state reconciles safely on return.

## 5. QA evidence required
For each feature, retain test ID, build/version, account fixtures, setup, action, expected result, actual result, server log/transaction reference, pass/fail and defect link. QA supervisors must independently verify economy, card/ownership and social privacy boundaries.

## 6. Not ready for production until approved
Exact pack odds/prices, card catalog, building-to-five-card mappings, card consumption policy, currency earn/spend table, Play Store SKUs/prices, Diamond travel fares, upgrade effects/prices, referral payouts, poker variants/stakes/venue layout and event capacity policies.
