# Hustle City — Property, Building and Business Ownership

## 1. Separate concepts
Do not conflate: building unlock eligibility, property ownership, business ownership, business operating permission, residency/tenancy, neighborhood founding/ownership, crew leadership and crew membership. A player may hold some without holding all.

## 2. Five-card unlock to building ownership
For buildings configured with a five-card key:
1. Player views the target building's collection and five required card slots.
2. Player obtains cards through approved acquisition paths.
3. Server validates all five required card definitions/instances.
4. UI marks the collection complete and reveals the building's claim/ownership action.
5. Server validates availability, eligibility, any approved claim cost and capacity.
6. Player confirms the claim.
7. Server writes a unique ownership record and entitlement atomically.
8. Building access, owner dashboard and upgrade options become available.

Whether the five cards are consumed, retained or locked is deliberately unresolved. The building-specific mapping and claim conditions must be data-driven. Never assume every city building requires cards or that one set unlocks multiple buildings.

## 3. Ownership record
Minimum fields: ownership_id, player_id, building_id, ownership_type, acquired_from, acquired_at, status, co_owners/managers if supported, access_policy, upgrade_level, transaction_reference and audit metadata. Enforce one authoritative ownership state and explicit transfer/sale/inheritance policy (TBD).

## 4. Building interaction tiers
Use the existing A–E building interaction tiers. Tier A signature destinations may have full interiors and management systems; lower tiers may offer focused interactions or ambient presence. A named exterior must not imply an enterable interior or unsupported feature.

## 5. Property and apartment operations
Apartment/property features may include furnishing, decor, layout packages, storage, garage/parking, guest permissions and access settings only where the selected property tier supports them. Upgrade catalogue must distinguish visual-only cosmetics from functional capacity/feature upgrades. Exact upgrade paths, prices, capacities and item catalogue are TBD.


## 5A. Renting first, permanent apartment ownership, and venue privileges

### Hustle Towers apartments
- A new player may start as a tenant renting an apartment in Hustle Towers.
- Each apartment's five-card collection is tied to that specific apartment or explicitly defined apartment entitlement.
- Completing all five required cards unlocks the permanent ownership claim for that apartment, subject to availability and any creator-approved eligibility rules.
- Renting and permanent ownership are different states. The UI must show the current tenancy, rent terms/renewal rules (TBD), collection progress, and the permanent-ownership unlock path.
- Do not silently convert rent payments into ownership or imply that renting alone completes the card collection.
- Decide whether the five cards are retained, locked or consumed only through an explicit creator-approved card policy.

### Shuffle Club and casino
- The Shuffle Club remains a shared venue; players cannot own the Shuffle Club or the casino inside it.
- A configured five-card collection may unlock a private room inside the Shuffle Club. This is a room/access entitlement, not ownership of the venue, casino, gaming operation or surrounding property.
- The casino is an experience inside the Shuffle Club, not a separate building by default. Whether it receives a separate five-card set or shares the club collection is TBD.

### Other venues
- Velvet Lounge has a five-card collection, but its completion reward is TBD; do not presume ownership.
- Hustle Club, Hustle City Marina and Yacht Club, American Swagger Clothing, the car dealership, Upper Level Entertainment Studios, Upper Level Films and Monster Beats may each have venue-specific collections. Their completion rewards require explicit creator approval.
- The marina/yacht-club venue collection does not grant ownership of every boat. The dealership collection does not grant ownership of every car. Individual vehicle collections remain separate.
- The beach is excluded from the five-card building collection requirement.

The building registry must distinguish venue ownership, private-room access, apartment tenancy, permanent apartment ownership, business operating rights and individual vehicle ownership as separate entitlement types.
## 5B. Creator-approved asset ownership versus host-building ownership

The following distinctions are approved direction:

- **Monster Beats:** Monster Beats is a production company. The player does not own its building or the company; the player can own a studio located inside the Monster Beats facility and produce music there.
- **Upper Level Films / Upper Level studio:** the player can form and operate their own film crew and make movies using the Upper Level studio/production facility. This does not automatically grant ownership of the Upper Level studio building. The exact brand/facility relationship between Upper Level Films and Upper Level Entertainment Studios needs canonical naming confirmation.
- **Car dealership:** the player can own an individual car lot. Do not conflate the lot with ownership of the entire dealership group or all cars on sale.
- **Clothing store:** the player can own an individual clothing store.
- **Yacht:** the player can own an individual yacht. The Hustle City Marina and Yacht Club remains a separate venue and is not granted with yacht ownership.
- **Hustle Club:** the player can own the Hustle Club venue/business.
- **Velvet Lounge:** the player can own the lounge venue/business.
- **Shuffle Club / casino:** the player can earn a private room inside the casino/club, but cannot own the Shuffle Club or casino.
- **Hustle Towers:** a player may begin as a renter; the five-card collection for a specific apartment unlocks permanent ownership of that apartment.

The entitlement catalogue must distinguish at least: host_building_ownership, studio_unit_ownership, film_crew_operation, car_lot_ownership, clothing_store_ownership, yacht_ownership, venue_business_ownership, private_room_access and apartment_tenancy/apartment_ownership. The five-card reward must point to the correct entitlement ID. Ownership of an asset inside a building never implies ownership of the building itself.

## 6. Business operations
A business record should define business_id, building_id, owner_id, managers, business_type, operating_state, hours, staff roles, service catalogue, inventory/stock, upgrade_level, revenue ledger, expenses, event capability and moderation/access policy. Revenue must come from simulated, auditable game activity; do not promise passive income rates until balanced.

## 7. Club ownership and party hosting
A club or venue may support owner-hosted parties when its interaction tier and permissions allow it. Owner/authorized manager can:
- Create event title, description, start/end time and time zone.
- Select public, friends-only, crew-only or invitation-only visibility.
- Configure guest capacity and entry/access rules supported by venue.
- Publish to permitted social feeds and send invitations.
- Review RSVPs, manage guest list and remove/report disruptive guests.
- Start, pause, end or cancel the event.
- View attendance and permitted event statistics.

Hosting permissions are venue-specific. A card collection does not automatically grant unlimited guest capacity, staff control, casino operation or ownership of surrounding land. Party tools must check ownership/manager role, venue schedule, safety capacity, moderation and service availability.

## 8. Upgrade model
Potential upgrade families: visual presentation, interior/furnishing, capacity, amenities, staff/service capability, business efficiency and event capability. Each upgrade has prerequisites, cost currency, price, duration if applicable, resulting attributes, reversible status and entitlement. Exact tiers, costs, effects and time gates are creator/balance decisions. Do not make paid upgrades mandatory for social participation.

## 9. QA
Test competing claims, unavailable building, duplicate set claims, partial card set, ownership revoke/refund policy, manager permission changes, party scheduling conflicts, full capacity, closed venue, player ban/block, upgrade rollback and cross-device state consistency.
