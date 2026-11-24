# Hustle City — Complete Gameplay Script Library

This directory is the connected, engine-neutral gameplay specification library. It defines player-facing rules and the contracts Unreal Engine 5 gameplay systems must implement. Unity 6 remains a secondary compatibility target.

## Documents
1. [Master Gameplay Bible](MASTER_GAMEPLAY_BIBLE.md) — player lifecycle, system map, canon and cross-system rules.
2. [Currencies, Economy and Monetization](ECONOMY_AND_MONETIZATION.md) — Hustle Money, Diamonds, Poker Chips, Play Store purchases, pricing safeguards and transaction rules.
3. [Collectible Cards, Packs and Trading](CARDS_PACKS_AND_TRADING.md) — card catalog, packs, collection completion, five-card building keys, trading and anti-abuse.
4. [Property, Buildings and Business Ownership](PROPERTY_BUILDINGS_AND_BUSINESSES.md) — ownership unlocks, upgrades, operations, club hosting and party permissions.
5. [Social Network, Sharing and Referrals](SOCIAL_NETWORK_AND_SHARING.md) — feeds, invitations, external share links, referrals, chat, privacy and moderation.
6. [Cruising, Travel and Events](TRAVEL_CRUISING_AND_EVENTS.md) — destination travel, Diamonds, convoys, cruises, calendars and events.
7. [Player Commerce and Customization](PLAYER_COMMERCE_AND_CUSTOMIZATION.md) — clothing, accessories, vehicles, apartments and business upgrade flows.
9. [Gameplay State and Acceptance Tests](GAMEPLAY_STATE_AND_ACCEPTANCE.md) — shared state, transaction invariants, QA scenarios and release gates.

## Canon discipline
- **Established** means supported by existing creator-approved repository design.
- **Working specification** means a proposed implementation contract derived from established direction; creator review is still required where stated.
- **Unresolved** means no value, price, probability, cap, name or rule may be treated as final.
- Never silently convert a proposal into canon. Record creator decisions in `docs/DECISION_LOG.md` and update dependent documents.
- No real-money gambling or cash-out is specified. Poker Chips are non-redeemable virtual chips unless the creator obtains legal review and explicitly approves a different model.
- No exact Play Store prices, pack odds, card names, card rarity, five-card identity mapping, referral payout, Diamond travel rates or upgrade prices are invented here.
- Basic transportation must not require premium Diamonds. Diamonds are reserved for premium travel options and approved premium purchases.
- All balances and ownership are server-authoritative in multiplayer. Client UI is never the authority for currency, inventory, card transfer, property ownership or event attendance.

## Production use
Each system document includes player flow, game rules, state/data requirements, failure cases, UI/audio/UX hooks, dependencies and QA. Production agents should implement against the shared contracts, not independently invent economy or ownership rules.
