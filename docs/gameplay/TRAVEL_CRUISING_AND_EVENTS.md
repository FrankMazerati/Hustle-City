# Hustle City — Travel, Cruising and Events

## 1. Travel philosophy
Destination-based automated travel is the preferred player experience. Manual driving is not the core direction. Players remain visible in vehicles during travel; friends and crew can board together, travel as driver/passenger, and arrive in coordinated convoys. Names or crew emblems may appear when privacy settings permit.

## 2. Travel modes
The mobility catalogue can include HCTA local rail (elevated, underground and street-level), HIM intercity/regional rail, buses, NPC rideshare, player-operated rides where supported, cars/motorcycles, boats/yachts, water taxis, helicopters and private aircraft. Availability is determined by actual authored geography and route data. Do not invent routes, times or fares.

HCTA connects downtown, all six central districts, neighborhoods and outer areas. HIM connects Hustle City with other cities/regions. Outer neighborhoods need HCTA station access and a transfer path to HIM; direct HIM service to every neighborhood is not assumed.

## 3. Fare rules
- Boats and cars use Diamonds under the approved vehicle/marine catalogue, including eligible purchase and upgrade transactions.
- Flying / air-travel services use Wings.
- Hustle Money is for ordinary in-game purchases and services, not the default currency for boats, cars or flying.
- Poker Chips are reserved for poker/table play.
- Before booking, show destination, service, currency, price, group/seat details, ETA if authoritative, cancellation and failure policy.
- Reserve then charge atomically. Failed pre-departure service releases/refunds the reservation.
- Exact Diamond costs, premium tiers, Hustle Money fares and travel catalogue remain TBD.

## 4. Cruising
Cruising is a social destination activity, not merely a loading screen. A player can initiate a cruise, select a vehicle/service, choose destination or route preset where approved, invite friends/crew, assign driver/passenger roles if supported, and depart once requirements are met. Participants see convoy status and privacy-respecting identities. The arrival can trigger venue presence, crew gathering display and optional feed post.

Cruise states: draft → invited → assembling → ready → in_transit → arrived → completed/canceled. Support late join only where safe, disconnect recovery, participant leave, host transfer and cancellation. Never strand a player or charge twice on reconnect.

## 5. Map and presence
Map can show destinations, transit layers, nearby players and crew gatherings such as a crew meeting in the Entertainment District, only according to each player's visibility settings. Use HCTA/HIM route layers separately. Do not expose hidden/private player location.

## 6. Events and parties
Event types may include club parties, crew meetups, cruises, poker sessions, venue events, community gatherings and official city events. Event record: event_id, host_id, venue_id or route_id, title, description, start/end, timezone, visibility, capacity, RSVP policy, invitation policy, status, moderation state and created_at.

Flow: create → validate rights/availability → publish → invite/share → RSVP → reminder → check-in/attend → live event interactions → close → optional recap/feed. Host can manage attendance within policy. Venue owner/authorized manager permissions are required for private venue events.

## 7. Event discovery and calendar
Provide upcoming, nearby/visible, friends, crew and venue event views. Filters by date, district, venue and event type. Calendar time zone must be explicit. Notifications respect user settings. Event cancellations or changes notify invitees.

## 7A. City travel as card-collection progression

Travel between cities is a core progression loop, not just transportation convenience. Each city owns its own card catalogue and City Key track.

- A player must physically travel to a city to earn/collect cards assigned to that city.
- Hustle City cards are earned in Hustle City; Chicago cards in Chicago; Miami cards in Miami; Texas cards in the relevant Texas city; and likewise for every approved destination.
- Playing poker, visiting businesses, completing activities, attending events, opening eligible packs and claiming card rewards in a city may award cards for that current city only.
- Cards from another city cannot be earned remotely while the player remains elsewhere.
- Players can view their Card Album and trade eligible cards from anywhere. Trading is the explicit exception to the presence requirement.
- City Keys are city-specific major milestones with significant bonus/surprise rewards and configured city-business unlocks. Exact key requirements and reward contents are defined per city and remain subject to creator approval.
- The city progression loop should make each destination worth visiting again: explore, play, complete activities, collect local cards, complete local collections, pursue that city's key and unlock its configured opportunities.
- Do not make travel costs, fares or card reward rates up. Basic transportation rules and currency constraints remain governed by this document's existing fare rules and the economy specification.

## 8. QA
Test fare quote mismatch, insufficient currency, service outage, group boarding, convoy split, disconnect/rejoin, privacy opt-out, blocked invite, schedule overlap, venue closure, capacity overflow, event cancellation and refund/idempotency behavior.
