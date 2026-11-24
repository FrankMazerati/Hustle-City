# Hustle City — Ownership Card Catalogue and Expandable Live Progression

**Status:** Living master catalogue. Creator-approved reward distinctions are recorded below. Exact card titles, card art, quantities, prices, odds, eligibility, collection-consumption policy and launch order remain unresolved unless explicitly stated.

## 1. Design goal: expandable for the life of the game

Hustle City must not ship with a closed, hard-coded list of buildings, collections, card packs, levels, stats or progression rewards. The launch catalogue is the first release of a content system that can grow through new venues, properties, businesses, studios, vehicles, boats, districts, events, card sets and progression tracks.

The five-card collection is the standard ownership/unlock pattern for configured assets. It is not a requirement that every future game feature use cards. New content may use five-card collections, other explicitly approved collection formats, achievements, levels, events, direct gameplay unlocks or combinations. Do not silently change the standard five-card ownership set to ten cards.

No fixed maximum number of collections, cards, packs, levels, achievements, stats or future content releases should be built into the data model.

## 2. Core rule: collection target is not always the host building

Every collection must point to one exact target entitlement. The target may be a room, apartment, studio unit, crew operation, car lot, store, business/venue or individual vehicle. Owning an asset located inside a destination does not imply ownership of the destination.

Required entitlement distinctions include:
- apartment_tenancy
- apartment_ownership
- private_room_access
- studio_unit_ownership
- music_production_rights
- film_crew_operation
- car_lot_ownership
- clothing_store_ownership
- yacht_ownership
- venue_business_ownership
- host_building_ownership (only where explicitly approved)

The server grants only the entitlement configured for that collection.

## 3. Current ownership and privilege catalogue

Each row below represents a target for a five-card collection, unless the row says that the collection relationship or exact target remains to be confirmed. The five card titles are five ordered rank slots. Do not invent their final display names: author and approve them for the theme of each target.

| World location / category | Collectible target | Completion reward / privilege | Boundary |
|---|---|---|---|
| Hustle Towers | Specific apartment | Permanent ownership of that apartment | Player may begin as a renter; no ownership of all Hustle Towers |
| Shuffle Club / casino | Private room | Private-room access inside the casino/club | Never ownership of Shuffle Club or casino |
| Hustle Club | Venue/business | Player can own Hustle Club | Does not grant other venues |
| Velvet Lounge | Lounge venue/business | Player can own the lounge | Distinct from Shuffle Club |
| Monster Beats | Studio unit inside facility | Player owns a studio and can produce music | Monster Beats remains a production company; player does not own company/building |
| Upper Level studio / production facility | Film crew operation | Player can form a film crew and make movies | Does not grant ownership of the studio building |
| Car dealership / car lot | Individual car lot | Player can own a car lot | Dealership group identity/name remains unresolved; no automatic ownership of every car |
| American Swagger Clothing / clothing retail | Individual clothing store | Player can own a clothing store | Do not infer ownership of the entire district or brand |
| Hustle City Marina and Yacht Club | Individual yacht collection is separate | Yacht collection grants ownership of the specific yacht | Never grants marina or yacht club ownership |
| Individual car collection | Specific car | Ownership of that specific car | Separate from car lot/dealership ownership |

### 3.1 Additional named locations needing creator classification

These names exist in the world catalogue, but their five-card target and completion reward must not be guessed. Add them to the content registry only after deciding whether they are player-ownable, provide access/privileges, or remain shared destinations:
- Upper Level Films (relationship to Upper Level Entertainment Studios / Upper Level studio requires canonical clarification; film crew and movie-making capability are established).
- Upper Level Entertainment Studios (host facility; studio-building ownership is not established).
- Hustle City Marina and Yacht Club (shared destination; individual yacht ownership is established).
- Car Club (relationship to dealership/car-lot ownership and vehicle collections requires clarification).
- We Fly High International Airport (shared travel destination; no ownership entitlement established).
- Diamond Plaza and Restaurant Boulevard (public place/street; no ownership entitlement established).
- Other bars, public venues, shops and future buildings as they are approved.

The beach is excluded from the five-card building ownership system. A venue or building may still offer ordinary gameplay there without a collection.

## 4. Five-card set template

Every approved ownership/privilege collection has exactly five ordered card slots:

1. **Card 1 — Entry rank:** title and role appropriate to the target (TBD).
2. **Card 2 — Developing rank:** title and role appropriate to the target (TBD).
3. **Card 3 — Established rank:** title and role appropriate to the target (TBD).
4. **Card 4 — Advanced rank:** title and role appropriate to the target (TBD).
5. **Card 5 — Master/top rank:** title and role appropriate to the target (TBD).

The top card completes the five-card set; there is no sixth ownership card. A completed collection triggers the configured entitlement/claim flow, subject to approved availability and eligibility rules.

Previous yacht and dealership rank labels are draft concepts only until creator approval. Do not present them as final catalogue names.

## 5. Card packs and future catalogue growth

The pack system must be data-driven and support:
- A themed pack for each approved building, business, studio, vehicle, yacht or other collection.
- General packs that draw only from an explicitly configured eligible pool.
- Event, seasonal, anniversary, collaboration and expansion packs.
- New collection releases without changing old collection IDs or corrupting completed collections.
- Pack versioning, scheduled release/retirement, regional availability and rollback.
- Explicitly disclosed odds and contents for randomized packs; no invented probabilities.
- Guaranteed-content packs and individual-card offers if separately approved.
- Daily login, seven-day streak, prize wheel, poker gameplay, achievements and events as configured acquisition sources.
- In-game Card Album, wish lists, Card Finder and secure player-to-player trading; no external trading app or website required.

New buildings and assets added after launch receive new stable IDs, collection definitions, five card slots (when using the standard format), a completion entitlement, eligible pack definitions and QA coverage. They do not require rewriting the base system.

Retiring a pack must not erase cards already owned, invalidate a completed collection or revoke an entitlement. Reprints/re-releases must have explicit duplicate and trade rules.

## 6. Player progression beyond cards

Cards and asset ownership are only one progression track. The architecture must also allow separately configurable systems for:
- Player XP and overall player level.
- Skills and gameplay statistics.
- Reputation and social standing.
- Stars, ratings, prestige or status ranks (exact meaning and scale TBD).
- Achievements, milestones, badges and titles.
- Business/studio/crew progression and operational performance.
- Collection completion and collection milestones.
- Event, seasonal and limited-time progression.
- Vehicle, property, wardrobe and customization progression.

These tracks may interact through approved prerequisites or rewards, but must not be collapsed into one score. For example, player level, business level, reputation and collection completion should remain distinct concepts unless a later creator decision explicitly combines them.

Do not invent level caps, XP curves, stat formulas, star meanings, reward thresholds, currencies, prices or pay-to-win advantages. The data model must support future balancing and additional tracks without schema redesign.

## 7. Content data model

Minimum versioned entities:
- **AssetTarget:** target_id, target_type, canonical_name, host_location_id (nullable), ownership_scope, launch_status, creator_approval.
- **Collection:** collection_id, target_id, collection_type, card_count, ordered_card_ids, completion_entitlement_id, card_retention_policy, release_version, status.
- **CardDefinition:** card_id, collection_id, slot_number, title, role/rank, artwork, rarity (only if approved), trade_policy, duplicate_policy, release_version.
- **PackDefinition:** pack_id, eligible_collection_ids, eligible_card_pool, guaranteed_contents, random_slots, odds_version, acquisition_sources, price/currency (if paid), schedule, region, status.
- **EntitlementDefinition:** entitlement_id, entitlement_type, target_id, scope, conditions, grant/revoke policy.
- **ProgressionTrack:** track_id, track_type, display_name, version, progression rules, reward table, cap policy (nullable/unlimited), status.
- **ProgressionEvent:** event_id, player_id, track_id, source, amount/change, timestamp, idempotency key and audit reference.

Use stable IDs, not display names, as relationships. Store versioned configuration so balance changes affect future grants according to a clear policy and do not rewrite a player's earned history.

## 8. Live-operations publishing workflow

For each new release:
1. Creator defines the new asset, collection or progression feature.
2. Content team assigns stable IDs and records the host location versus collectible target.
3. Author five themed rank cards if using the standard collection.
4. Define the exact completion entitlement and what it does not grant.
5. Define acquisition sources and pack configuration; keep odds/prices TBD until approved.
6. Add daily reward, poker, event or other reward eligibility only when approved.
7. Prepare Card Album, Card Finder, inventory, trading and store presentation.
8. QA tests partial completion, final completion, duplicate cards, trading, reconnects, entitlement boundaries and rollback.
9. Publish a versioned release with audit history and monitoring.
10. Preserve prior collections, ownership and earned rewards after release or retirement.

## 9. Safety, economy and integrity invariants

- Server-authoritative card ownership, pack results, trades, progression values and entitlements.
- Idempotent rewards and transactions; no duplicate grants on retry.
- No card or entitlement may be transferred twice or destroyed by concurrent trades.
- No automatic conversion between Hustle Money, Diamonds, Wings and Poker Chips.
- Do not make essential progression dependent on high-stakes poker or paid randomized packs.
- Disclose randomized pack odds and applicable purchase rules before opening/purchase.
- Support parental/age, regional, platform and consumer-protection requirements.
- Preserve audit trails for grants, trades, adjustments, progression changes and live-ops configuration.
- Future expansion must not invalidate already-earned ownership or collection completion.

## 10. Open creator decisions

- Final five card titles for every target.
- Exact launch inventory of apartments, studios, stores, car lots, yachts and other eligible assets.
- Whether the Shuffle Club private-room set is a dedicated casino set or a shared club set.
- Exact Velvet Lounge collection identity (venue ownership is established; target scope needs final data mapping).
- Canonical relationship/name between Upper Level Films and Upper Level Entertainment Studios.
- Canonical car dealership group name and Car Club relationship.
- Whether the player owns the Hustle Club as a venue, operating business, or both (creator direction says can own the Hustle Club; exact entitlement scope to map).
- Card consumption/retention/locking policy after completion.
- Duplicate-card conversion policy, if any.
- Player level, XP, statistics, reputation and star definitions/scales.
- Pack odds, pack quantities, rarity tiers, prices and release schedule.
- Launch order, expansion cadence and any paid progression limits.

Do not silently resolve any item above. Record future approvals in the project decision log and update dependent documents.


## 11. City-specific dealership and venue collections

The five-card collection structure also supports a multi-city content catalogue. The creator approved city-specific business names and city-specific character titles/roles: a dealership collection in Chicago and one in another city may have different local dealership names, five character titles, characters and stories while retaining the same five-card low-to-high progression principle.

The approved parent automotive group name is **Hustle Boys Automotive Group**. Its local dealerships may use distinct city-specific names. The dealership title concepts currently in discussion include Lot Runner, Car Plug, Sales Boss, Motor Mogul (wording to confirm), Auto King, Lot Scout, Luxury Car Broker, Showroom Boss, Exotic Car Lot Hustler, Exotic Car Plug and Showroom Chief. These are working concepts, not a locked city-by-city mapping.

Apply the same city-specific naming and character approach to yacht clubs, nightclubs, hotels/hotel chains, bars and lounges, sports venues, clothing stores, restaurants, studios and other suitable local businesses. The complete 30-city roster and final local business names remain to be approved.

See [City Identity and Local Business Catalogue](CITY_IDENTITY_AND_LOCAL_BUSINESS_CATALOGUE.md) for the authoring workflow, data model and review rules. This localization layer does not change the exact-entitlement rule: a collection grants only its configured reward, not automatically the host building, parent company or unrelated assets.
