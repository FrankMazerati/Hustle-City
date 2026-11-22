# Hustle City — Core Data Model

This is the conceptual data model, not a claim that these tables have been deployed. The confirmed live Supabase project is Hustle City Shuffle Club; see [README](README.md) for its inspected baseline.

## Identity and player shell
- Supabase Auth owns authentication identity.
- `profiles` stores account-level profile data.
- `player_characters` stores in-world character identities and appearance.
- `player_city_unlocks` records city access.
- `player_home_cities` records selected home city independently of neighborhood ownership.
- Account-to-character cardinality and character creation/progression rules remain open.

## World geography
- `cities` contains reusable city systems with city-specific identity.
- `districts` represents the six central district boxes in Hustle City.
- `neighborhoods` represents the surrounding map boxes reserved for neighborhoods.
- `neighborhood_ownership` records founder/claimant ownership separately from residency.
- `neighborhood_residencies` records who lives in or is associated with a neighborhood.
- `city_blocks` is a possible lower-level geography entity, but its subdivision and count are not finalized.

Confirmed: six central district boxes; all surrounding boxes are reserved for neighborhoods. The total grid dimensions, number of neighborhood boxes, exact boundaries, block count/subdivision, and final district placements must be recovered from the original map and approved before schema constraints encode them. The earlier 7×7 / 43-neighborhood / 5×5-block proposal is historical capacity planning only, not approved canonical geography.

Working district concepts in prior planning include Downtown, Financial, Diamond, Entertainment, Marina, and Fashion/Swagger (working label). Final names, boundaries, and placements remain subject to creator approval.

## Crews
- `crews` represents player groups.
- `crew_memberships` records membership and status.
- `crew_leadership` records leadership appointments separately from membership and neighborhood ownership.
- Working names include Mazerati Boys, Billion Dollar Boys Club, and Million Dollar Row. Mazerati Boys currently uses a Z; names remain editable content.
- Crew eligibility, roles, appointments, dues, and asset ownership rules remain open.

## Property and businesses
- `properties` represents real-estate assets.
- `property_ownership` records player ownership separately.
- `businesses` represents operating businesses, optionally located at a property.
- `business_ownership` records ownership separately from property ownership and crew membership.
- A player can own a property in one neighborhood and belong to a crew headquartered elsewhere.
- Co-ownership, tenancy, leases, and crew-owned assets require rule decisions.

## Economy and inventory
- `wallet_accounts` supports player-owned or crew-owned currency accounts.
- `wallet_transactions` is the auditable transaction header.
- `wallet_entries` is the append-only balance-change ledger.
- Currency codes remain separate: `HUSTLE_MONEY`, `DIAMONDS`, and `POKER_CHIPS`.
- `inventory_items` and `player_inventory` track non-card items.
- `collectible_cards`, `player_cards`, `card_packs`, and `card_pack_placements` track collectible cards and packs. Five pack slots per location is the current design rule.
- The client must never set balances, grant items, authorize ownership, or settle competitive outcomes.
- Currency limits, grants, sinks, refunds, reversals, and card trading rules remain open.

## Venues and social activity
- `venues` are named interactive destinations.
- `venue_presence` records player presence.
- `venue_tables` and `table_seats` model activity tables and occupancy.
- `social_conversations`, `conversation_participants`, and `messages` model communication.
- `contact_exchange_requests` models consent-based contact-card exchange.
- Poker/card games are optional; the social world must stand on its own.
- Presence concurrency, seat expiry, moderation, blocking, and retention rules remain open.

## Events and transport
- `city_events` and `event_participants` establish persistent event and participation records.
- `vehicles`, `vehicle_ownership`, and `travel_trips` provide a foundation for owned transport and destination-based journeys.
- HIM and HCTA are distinct rail authorities/networks and should have separate operator, line, station, stop, route, service, and transfer concepts.
- HCTA provides local access to the six districts and every designated outer neighborhood. HIM provides intercity/regional passenger journeys, with transfers to HCTA at designated interchanges.
- Exact HIM terminal count/location, HCTA line count/colors/alignments, station locations, schedules, and neighborhood station placements are not finalized. Do not seed or constrain them as fixed facts.
- Detailed transit schema should follow the approved geography and transport contracts, not be guessed from the legacy draft.

## Security baseline
- RLS is required on every exposed application table.
- Table grants and RLS policies are separate controls and must be designed together.
- Policies must reflect ownership, membership, consent, and trusted-server rules; do not apply one generic `auth.uid()` policy to every table.
- Wallet, inventory grants, purchases, ownership changes, settlement, and rewards must be trusted-server operations.
- Never expose service-role credentials in a game client.
