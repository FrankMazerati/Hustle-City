# Hustle City — City Identity and Local Business Catalogue

**Status:** Living expansion specification. The creator approved the principle that each city may have distinct local business names, character casts, card titles, style and language. Specific names and examples below are proposals unless marked approved. The complete 30-city roster and all local names remain to be populated and approved.

## 1. Design goal

Make every city feel like its own place rather than a reskinned copy of another city. A city's identity should be recognizable through its businesses, venues, characters, card titles, fashion, vehicles, music, sports culture, architecture, local expressions and social atmosphere.

The game uses a consistent underlying content structure, while local presentation is authored city by city.

## 2. Approved design principles

- The initial expansion plan targets 30 cities. The exact canonical roster must come from the creator's approved city list; do not invent or silently finalize the roster.
- The same business category may have a different local business/dealership/venue name in every city.
- Each city can have its own character cast, including different names, ages, genders, personalities, backgrounds, biographies and artwork.
- For five-card collections, the five positions retain a recognizable low-to-high progression, but the actual character titles/roles may differ by city and local theme.
- Titles should sound memorable, stylish and game-worthy—not unnecessarily corporate or technical.
- Local identity should be researched and authored with care. Avoid reducing a city to stereotypes or forcing slang that residents would not naturally use.
- A shared parent company may operate differently named local businesses. A local storefront name does not need to repeat the parent company's name.
- The collection's completion reward must remain precisely scoped. A dealership character collection does not automatically grant every car or ownership of a parent company.

## 3. Automotive group and dealership naming

**Creator-approved parent group name:** Hustle Boys Automotive Group.

The group may operate local dealerships with distinct names in each city. The following are working examples, not a finalized list of five dealership names:

| City example | Local dealership name | Status |
|---|---|---|
| Chicago | Hustle Boys Motor House | Proposed |
| Los Angeles | West Coast Motor Society | Proposed |
| Miami | South Beach Exotic Motors | Proposed |
| Dallas, Texas | Lone Star Motor Exchange | Proposed |

The creator also approved the broader direction that dealership names can vary by city. Do not assume Dallas is the final Texas city in the 30-city roster; confirm the roster before assigning local brands.

### 3.1 Dealership five-card progression

Each dealership collection has five distinct characters in a low-to-high ladder. The structure is five cards; titles are city-specific.

Chicago-style working sequence:
1. Lot Runner
2. Car Plug
3. Sales Boss
4. Motor Mogul (confirm exact wording if a different phrase was intended)
5. Auto King

Other title concepts the creator liked or called out:
- Lot Scout
- Luxury Car Broker
- Showroom Boss
- Exotic Car Lot Hustler
- Exotic Car Plug
- Showroom Chief

These titles are a reusable idea pool, not an instruction to use the same sequence in every city. Assign each title to a city only when its progression, local flavor and character fit have been reviewed. Card 1 should clearly be the entry-level person working the lot; Card 5 should clearly communicate the top position/ownership or the collection's approved top-rank fantasy. The middle roles should show increasing influence and responsibility.

Each character card should support:
- Character name
- Age
- Gender
- City and local dealership
- Character title/role and collection slot
- Personality and short biography
- Character artwork/visual identity
- Optional voice, wardrobe and dialogue profile
- Stable card and character IDs

Do not invent card rarity, odds, prices, stat bonuses or a specific reward without approval.

## 4. Other categories for city-specific naming

The city identity catalogue should cover, where present in the city's world:

| Category | Localized content |
|---|---|
| Yacht clubs and marinas | Club/marina names, yacht culture, crew and five-card character titles |
| Nightclubs | Club names, music identity, promoters, DJs, hosts and VIP culture |
| Hotels and hotel chains | Hotel brands, individual properties, hospitality cast and guest experience |
| Bars and lounges | Venue names, atmosphere, bartenders, DJs and regulars |
| Sports venues and teams | Arena/stadium names, team identities, mascots and sports personalities |
| Clothing stores and fashion brands | Store names, local designers, streetwear and fashion characters |
| Barber shops and salons | Shop names, barbers/stylists and local personalities |
| Restaurants and food venues | Restaurant names, cuisine identity, chefs and staff |
| Radio and media | Station names, DJs, hosts and local programming |
| Recording/music businesses | Studio/label names, producers, artists and music scenes |
| Film/entertainment businesses | Production company/studio names, crews and filmmakers |
| Other local businesses | Names and characters appropriate to each city's approved content |

Not every category must appear in every city. Add categories where they make sense for the city's world and gameplay.

## 5. City-by-city authoring workflow

For each approved city:
1. Confirm the city's name, region and creator-approved identity direction.
2. Establish its visual, cultural, architectural and neighborhood references.
3. Create a local business and venue inventory from approved world content.
4. Name each local business/venue; track any parent company separately.
5. Author each five-card collection with five distinct city-appropriate titles in a clear low-to-high progression.
6. Create each character's name, age, gender, personality, background, biography and artwork brief.
7. Map the collection to one exact gameplay reward/entitlement.
8. Review authenticity, originality, tone, stereotypes, naming conflicts and trademark concerns.
9. Record creator approval and publish versioned content.
10. Preserve existing player collections and earned rewards when new cities or businesses are added.

## 5A. Strict city-presence rule for card collection

**Creator-approved strict rule:** A player may acquire/collect a new card only while physically present in the in-game city to which that card belongs. City identity is attached to every card definition and every acquisition grant.

- Chicago cards can be earned only while the player is in Chicago.
- Los Angeles cards can be earned only while the player is in Los Angeles.
- Miami cards can be earned only while the player is in Miami.
- Texas-city cards can be earned only while the player is in the relevant Texas city.
- Apply the same rule to all cities in the approved 30-city expansion roster.
- The rule covers card packs, poker/activity rewards, daily login rewards, prize-wheel rewards, events, achievements, direct card grants and any other new-card acquisition route. A reward may be claimed/opened only when the player is present in the card's city. A reward earned in one city must not silently grant a card belonging to another city.
- A pack that contains cards from multiple cities may be opened only if every card in its eligible pool belongs to the player's current city; otherwise it must be unavailable or clearly separated into city-specific packs.
- **Trading is the exception:** players may trade eligible cards with other players anywhere, regardless of the cities those cards belong to. Trading does not count as collecting through a city activity and does not bypass trade restrictions.
- City presence must be validated by authoritative server-side world/session state at the moment of acquisition. A client location claim, menu selection, remote purchase or spoofed city value is insufficient.
- If a player leaves the city before claiming/opening a pending card reward, preserve the unclaimed reward safely but require return to the card's city before granting/opening it. Exact pending-reward UX is an implementation detail; never lose a valid reward.
- A player may view their album and trade cards anywhere. Viewing or trading does not grant a new card.

This is a core progression rule, not an optional event modifier. Any exception requires an explicit creator decision and a versioned rule change.

## 6. Data model and expansion requirements

Use stable IDs and versioned data, never display names as database keys.

Minimum content entities:
- CityDefinition: city_id, canonical_name, region, identity_profile_id, roster_status, release_status.
- CityIdentityProfile: visual references, local themes, language guidance, music/fashion/vehicle direction, review status.
- ParentBusinessGroup: group_id, canonical_name, business_category.
- LocalBusiness: business_id, city_id, parent_group_id (nullable), local_display_name, category, location_id, status.
- CharacterDefinition: character_id, city_id, business_id, name, age, gender, personality, biography, artwork, voice/wardrobe references.
- CityCollection: collection_id, city_id, business_id/target_id, collection_type, ordered_card_ids, completion_entitlement_id.
- CardDefinition: card_id, collection_id, slot_number, character_id, city_specific_title, progression_position, release_version.

The model must allow more cities, businesses, characters and collections to be added without hard-coded caps, destructive migrations or resets. Existing city names and IDs must remain stable after publication; display names may be revised through versioned content changes with audit history.

## 7. Review and canon discipline

- **Approved:** Hustle Boys Automotive Group is the parent automotive group name; city-specific local dealership names and city-specific character titles are the intended design direction.
- **Proposed:** The individual dealership names and title examples in this document.
- **Unresolved:** Complete 30-city roster, final local business names, exact city-to-business assignments, final character identities, role ladders, artwork, biographies and rewards.
- Do not turn a brainstormed name into canon without creator approval.
- Do not force every city to use every venue category.
- Do not assume a local business is player-ownable merely because it has a card collection; use the ownership/entitlement catalogue to define its reward.
- Keep city identity grounded and distinctive without relying on caricature.

## 8. Relationship to other gameplay specifications

- `OWNERSHIP_CARD_CATALOGUE_AND_LIVE_PROGRESSION.md` defines collection/entitlement rules and lifelong expansion.
- `CARDS_PACKS_AND_TRADING.md` defines card acquisition, packs, album and trading.
- `PROPERTY_BUILDINGS_AND_BUSINESSES.md` defines business/property ownership and operations.
- `MASTER_GAMEPLAY_BIBLE.md` defines shared world and gameplay canon.

This document defines how local city identities, local business names and city-specific collectible characters are authored across the expanding world.
