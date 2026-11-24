# Hustle City — Complete Gameplay Script Library

This directory is the connected, engine-neutral gameplay specification library. It defines player-facing rules and the contracts Unreal Engine 5 gameplay systems must implement. Unity 6 remains a secondary compatibility target.

## Documents
1. [Master Gameplay Bible](MASTER_GAMEPLAY_BIBLE.md) — player lifecycle, system map, canon and cross-system rules.
2. [Currencies, Economy and Monetization](ECONOMY_AND_MONETIZATION.md) — Hustle Money, Diamonds, Poker Chips, Wings, wallets and economy rules.
3. [In-App Store, Memberships, Rewards, Ads and Revenue](HUSTLE_CLUB_MEMBERSHIPS_AND_PACKAGE_STORE.md) — Hustle Club monthly tiers, one-time packages, daily rewards, the bar recovery loop, banner/rewarded/interstitial ads, revenue forecasting and the professional owner dashboard.
4. [Collectible Cards, Packs and Trading](CARDS_PACKS_AND_TRADING.md) — card catalog, packs, five-card ownership keys, in-game trading and anti-abuse.
5. [Ownership Card Catalogue and Live Progression](OWNERSHIP_CARD_CATALOGUE_AND_LIVE_PROGRESSION.md) — asset/entitlement catalogue, expandable packs, player levels, stats, reputation, stars and live operations.
6. [City Identity and Local Business Catalogue](CITY_IDENTITY_AND_LOCAL_BUSINESS_CATALOGUE.md) — city-specific business/venue names, dealership brands, five-card character ladders and the 30-city expansion authoring system.
7. [Property, Buildings and Business Ownership](PROPERTY_BUILDINGS_AND_BUSINESSES.md) — ownership unlocks, upgrades, operations, club hosting and party permissions.
8. [Social Network, Sharing and Referrals](SOCIAL_NETWORK_AND_SHARING.md) — feeds, invitations, external share links, referrals, chat, privacy and moderation.
9. [Cruising, Travel and Events](TRAVEL_CRUISING_AND_EVENTS.md) — destination travel, Diamonds, convoys, cruises, calendars and events.
10. [Player Commerce and Customization](PLAYER_COMMERCE_AND_CUSTOMIZATION.md) — clothing, accessories, vehicles, apartments and business upgrade flows.
11. [Gameplay State and Acceptance Tests](GAMEPLAY_STATE_AND_ACCEPTANCE.md) — shared state, transaction invariants, QA scenarios and release gates.

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
