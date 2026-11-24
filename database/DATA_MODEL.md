# Hustle City — Core Data Model

## Identity and player shell
- Supabase Auth owns authentication identity.
- profiles stores account-level profile data.
- player_characters stores in-world character identities and appearance.
- player_city_unlocks records city access.
- player_home_cities records the selected home city independently of neighborhood ownership.

## World geography
- cities contain reusable city systems with city-specific identity.
- districts represent major city districts.
- neighborhoods belong to a city and may be associated with a district.
- neighborhood_ownership records limited founder/claimant ownership.
- neighborhood_residencies records who lives in or is associated with a neighborhood. Residency does not confer ownership.
- city_blocks represent the 5×5 planning grid within a neighborhood.

Approved planning concept: 7×7 = 49 large boxes, six central districts and 43 potential outer neighborhood boxes. Each outer box contains 25 city blocks. This is long-term capacity, not a launch requirement. Six central district concepts include Diamond, Entertainment, Marina, Fashion/Swagger (working label), Financial, and Downtown. Exact boundaries and final assignments remain open.

## Crews
- crews represent player groups.
- crew_memberships records membership and status.
- crew_leadership records leadership appointments separately from membership and neighborhood ownership.
Working names include Mazerati Boys, Billion Dollar Boys Club, and Million Dollar Row. Mazerati Boys currently uses a Z; names remain editable content.

## Property and businesses
- properties represent real-estate assets.
- property_ownership records player ownership separately.
- businesses represent operating businesses, optionally located at a property.
- business_ownership records ownership separately from property ownership and crew membership.
A player can own a property in one neighborhood and belong to a crew headquartered elsewhere.

## Economy and inventory
- wallet_accounts supports player-owned or crew-owned currency accounts.
- wallet_transactions is the auditable transaction header.
- wallet_entries is the append-only balance-change ledger.
- Currency codes remain separate: HUSTLE_MONEY, DIAMONDS, POKER_CHIPS, and WINGS.
- inventory_items and player_inventory track non-card items.
- collectible_cards, player_cards, card_packs, and card_pack_placements track collectible cards and packs. Five pack slots per location is the current design rule.
The client must never set balances, grant items, authorize ownership, or settle competitive outcomes.

## Venues and social activity
- venues are named interactive destinations.
- venue_presence records player presence.
- venue_tables and table_seats model activity tables and occupancy.
- social_conversations, conversation_participants, and messages model communication.
- contact_exchange_requests models consent-based contact-card exchange.
Poker/card games are optional; the social world must stand on its own.

## Events and transport
- city_events and event_participants establish persistent event and participation records.
- vehicles, vehicle_ownership, and travel_trips provide a foundation for owned transport and destination-based journeys.
Detailed transit lines, stations, schedules, NPC routines, game rounds, and settlement rules are deferred until their contracts are specified.

## Security baseline
The draft enables RLS on every application table and defines no permissive policies. Access remains unavailable to ordinary client roles until table-specific policies and trusted server operations are designed and tested. Never expose service-role credentials in a game client.

## Lifestyle services and recurring costs (conceptual; schema not finalized)
- Candidate records may be needed for housing occupancy/tenancy, property ownership, vehicle financing obligations, insurance policies, fuel/service records, and recurring lifestyle charges.
- Do not assume each candidate needs a separate player-managed bill or table. A bundled recurring charge is under consideration to keep the simulation lightweight; itemized expense breakdown may be optional.
- Exact entities, payment cadence, prices, delinquency behavior, coverage/claims and whether fuel is separately tracked are unresolved. Do not implement financial penalties until the creator approves the rules.
- Vehicle simulation faults must not cause loss of player-owned assets or unfair insurance/repair charges.

## In-world phone and messaging
- Reuse the existing social_conversations, conversation_participants and messages foundation for phone-based player messaging rather than creating a disconnected duplicate messaging system.
- Phone UI/device state and message presentation are client/gameplay concerns unless persistent device ownership or settings become necessary.
- Enforce the same server-side authorization, privacy, blocking, reporting and moderation rules regardless of whether a message is opened from the phone UI or another social interface.


## Persistent Sims, relationships and service history
- Preserve stable NPC/Sim identity records for the named population, with profile/self-model attributes and links to home, work, schedule, possessions and supported history. The 100,000-person target is a roster/persistence scale, not a requirement to execute every Sim at full fidelity simultaneously.
- Add a sparse personal-memory model: a memory owner (the Sim doing the remembering), the person remembered, the actual encounter/conversation/event, and the facts/details legitimately retained. Do not share one Sim's personal memory with another.
- Add directional relationship state for each relevant pair. Familiarity, trust and current relationship state are separate mutable values; retain historical events separately. One person's trust or memory must not imply reciprocity.
- Persist these records through logout, reconnect, process/server restart and population expansion. Runtime caches may be used, but durable database records remain authoritative.
- Add valet/concierge service-event history keyed to the actual player, attendant, vehicle, service location/business, timestamp and outcome. Shared workplace service tickets may support retrieval and shift handoff, but must not transfer personal recognition/trust between attendants.
- Use sparse indexed queries for one Sim's known people, one relationship pair, or a player's service history. Do not create every possible Sim/player relationship in advance.

## Health, consumables and currency boundaries
- Player health/condition and any food/drink effects need authoritative state and item-effect definitions if the health system is retained in the playable design.
- Food and beverages purchased at venues use Hustle Money/Cash, not Poker Chips. Food and drinks at poker tables are specifically intended to restore table health; the wider distinction among health, energy/stamina, hunger and condition remains a design question. Store item identity, price charged, effect applied and transaction outcome so restoration can be audited and replay-safe.
- Keep four distinct wallets: Hustle Money/Cash, Diamonds, Poker Chips and Wings. The current SQL draft's three-currency constraint is incomplete relative to the approved four-currency economy and must be reconciled before migration.
- Poker Chip → Hustle Money conversion is a separate, explicit cashier/kiosk flow with atomic debit/credit and an auditable idempotent transaction. It is not direct Poker Chip payment for ordinary goods.

## Profile and collection records
- Player-visible balances, progression values, neighborhood/crew details, owned-card quantities, trade listings and shared wishlists must be derived from authoritative profile, wallet, progression and inventory records.
- Distinguish cards owned from cards listed for trade and from cards merely sought on a shared wishlist. Profile inspection is informational and must not reserve or transfer inventory.
- Apply visibility controls and never expose hidden inventory, unshared wishlists, private account/payment credentials or private NPC memory.

## Existing data-model status
These are requirements to reconcile into a reviewed schema migration. The current SQL draft does not yet implement the full Sim memory/relationship/service-event model or the complete four-wallet currency contract. Do not claim these tables or policies exist until designed, migrated and tested.
