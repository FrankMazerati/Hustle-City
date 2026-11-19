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
- Currency codes remain separate: HUSTLE_MONEY, DIAMONDS, and POKER_CHIPS.
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