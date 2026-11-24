# Building Identity and Interaction Catalog
Version: 1.0
Status: Initial production catalog; creator approval required for final names, district placement, interiors, and gameplay scope.

## 1. Core rule

Most visible buildings in Hustle City must have an authored identity. Buildings should use fictional names that fit their business, residents, architecture, district, and world history. Do not fill major streets with anonymous repeated boxes or generic placeholder signage.

Not every building needs a bespoke interior or full gameplay loop. Each building must, however, have a deliberate classification:
- **Signature interactive destination:** authored identity, prominent exterior, enterable space, and one or more meaningful gameplay systems.
- **Standard interactive business:** named exterior and a focused interaction, service, shop, or interior.
- **Named ambient building:** named and visually authored; may be closed, private, inaccessible, or non-enterable.
- **Residential building:** named apartment/condo/tower/property identity; entry and resident interactions depend on its gameplay tier.
- **Restricted / closed / abandoned / under construction:** intentionally unavailable, with believable signage and world-state reasons. These are not accidental missing content.
- **Unlabeled background structure:** allowed sparingly for distant skyline silhouettes, low-visibility industrial massing, or tightly controlled background dressing; never use as the default for street-level buildings.

## 2. Building interaction tiers

| Tier | Meaning | Expected player experience |
|---|---|---|
| A — Full destination | Major signature location | Enter, explore designed interior, interact with staff/NPCs, use core activities/services, attend events, and return through persistent systems |
| B — Functional venue | Regular business or public venue | Enter or approach a service point; use a focused activity, purchase, service, or social interaction |
| C — Limited interaction | Named building with a small gameplay footprint | Doorbell, lobby, reception, ATM, service window, directory, mission trigger, or contextual interaction |
| D — Ambient / restricted | Named but not generally enterable | Exterior storytelling, signage, windows, deliveries, NPC activity, locked/private/closed state, or future expansion hook |
| E — Background | Distant or low-priority scenery | Visual city density only; no implied gameplay access |

Every building record must state its tier. Never let a locked door or inaccessible interior appear to be a broken interaction: communicate the state through signage, prompts, schedule, security, or world context.

## 3. Initial signature-building inventory

These names are drawn from established Hustle City concepts. They are working canon entries, not permission to invent unresolved final names.

| Building / destination | Intended identity and gameplay | Initial tier |
|---|---|---|
| Hustle Towers | Major skyline landmark; lobby, reception, elevators, social/business access, and future floors or suites as approved | A |
| Velvet Club Lounge | Upscale nightlife, social gathering, hosted events, music, VIP areas and venue operations | A |
| Hustle Club | Major club destination; nightlife, events, social play and venue interactions | A |
| Hustle City Marina & Yacht Club | Marina promenade, docks, yacht access, boating services, waterfront social activities and water transport connections | A |
| The Shuffle Club | Social entertainment destination; club activities and event programming to be defined | A |
| Swagger Shop | Fashion retail, browsing, fitting, purchasing and player style interaction | B |
| American Swagger Clothing | Flagship fashion retail / clothing brand destination; fitting and purchase flow | B |
| Bella Rose Collection | Fashion and retail destination; collection-specific presentation and shopping | B |
| Mazerati Boys Automotive Group | Automotive showroom / dealership identity, vehicle browsing, purchase or approved vehicle services | A |
| South Side Bar | Neighborhood bar and social meeting point | B |
| East Side Bar | Neighborhood bar and social meeting point | B |
| North Side Bar | Neighborhood bar and social meeting point | B |
| West Side Bar | Neighborhood bar and social meeting point | B |
| Casino — working concept | Major casino entertainment destination; final name, district, and approved activity scope remain unresolved | A |
| Airport — name unresolved | Major airport and travel hub; use either “We Fly High International Airport” or “We Fly Sky International Airport” only after creator approval | A |

## 3A. Creator-directed district identity and placement refinements

- **Diamond District is downtown.** Its identity includes the central downtown skyline, Diamond Row, Velvet Lounge, cigar bars/lounges, upscale jewelry stores, upscale clothing boutiques and related luxury/nightlife businesses.
- **Swagger District** is specifically the hip-hop/streetwear fashion area: urban clothing stores, sneaker/shoe shops and streetwear boutiques. Do not merge this identity with Diamond District luxury retail.
- **Entertainment District** must include several additional entertainment-appropriate buildings beyond the co-located Upper Level Entertainment Studios, Upper Level Films and Monster Beats campus. These buildings should be given distinct names and meaningful interactions as their concepts are approved. Potential building roles can include media, production, performance, screening, event and live-entertainment functions; names and final venue selection remain creator-approved, not auto-generated canon.
- **Get Wild Beach** is a distinct beach-party destination/area in the coastal plan, with its own visual identity and beach gathering/event function.
- **Hustle Towers** is a major downtown landmark and may host the gambling experience within its own building/interior.
- **Hustle Club** is a separate nightlife/club destination and is not to be placed in the downtown/Diamond District cluster by default. Its district assignment is unresolved. Do not assume Hustle Club is the casino or that gambling must happen there.
- The blue-and-black coordinated visual identity applies to Upper Level Entertainment Studios, Upper Level Films and Monster Beats as their shared campus identity. Do not automatically apply it to every Entertainment District building.

## 4. How to decide what is enterable

For every named building, record:
1. Is the player allowed inside?
2. Is the interior fully authored, modular, or represented by a focused service interaction?
3. What can the player actually do there?
4. Which NPC roles operate there?
5. Does it have opening hours, event schedules, or changing business states?
6. Is there a public lobby, private area, VIP area, staff-only area, or restricted floor?
7. Does the location support player-owned or crew-related activity?
8. Does it connect to transport, parking, pedestrian routes, docks, or transit?
9. What happens when it is closed, full, under maintenance, or unavailable?
10. What is the minimum launch implementation and what is deferred?

A building is not meaningfully interactive just because the player can open its door. It needs a purposeful activity, service, social loop, information interaction, or other designed response.

## 5. Naming system for the wider city

Create a reusable naming library by district and building type:
- Residential: apartment houses, condominium towers, lofts, residential courts and waterfront residences.
- Commercial: offices, professional buildings, banks, agencies and business centers.
- Retail: boutiques, shopping arcades, markets, salons, barbers, electronics, furniture and specialty stores.
- Food and hospitality: restaurants, cafés, diners, bakeries, hotels and resorts.
- Nightlife: lounges, clubs, bars, event halls and entertainment venues.
- Civic and community: libraries, recreation centers, schools, clinics, fire stations and public service buildings.
- Industrial and logistics: warehouses, workshops, depots, factories and distribution buildings.
- Waterfront: marinas, yacht services, ferry terminals, boat clubs, beach facilities and waterfront restaurants.

Names should be varied, believable, memorable, and original. Avoid repetitive filler such as “Building 01” or the same generic business name across multiple blocks. Use a consistent naming grammar without making every name sound like the same brand.

## 6. Engine-neutral building data

Canonical building identity and gameplay metadata belongs in SHARED_CORE, not exclusively in Unreal or Unity scene files. Each authored building should have a stable ID and fields equivalent to:

- building_id: immutable unique identifier
- display_name: approved in-world name
- short_name: optional map/UI label
- building_type: residential, retail, nightlife, civic, office, industrial, transport, waterfront, hospitality, or other approved category
- district_id and block_id: canonical world placement
- interaction_tier: A, B, C, D, or E
- access_state: public, scheduled, private, restricted, closed, abandoned, construction, or background
- enterable: explicit boolean
- interior_profile_id: optional reusable interior template or bespoke interior reference
- interaction_tags: approved gameplay interaction identifiers
- services: services actually supported by gameplay
- npc_roles: staff, residents, visitors, security, vendors, or other relevant roles
- schedule_id: optional opening/event schedule
- signage_profile_id: visual signage and branding reference
- exterior_asset_ids and interior_asset_ids: asset manifest references
- transport_links: nearby entrances, parking, transit, docks, or route nodes
- launch_scope: launch, post-launch, or ambient-only
- provenance / approval: creator approval and asset provenance metadata

Use schema validation and stable references. Engine adapters may render and implement these records differently, but must not silently change the canonical identity or access rules.

## 7. World Builder generation rules

- Generate a high proportion of named street-level buildings; prioritize authored names around player routes, commercial streets, transit stations, waterfronts and landmarks.
- Use district-specific naming pools and prevent accidental duplicate names within the same city.
- Assign building type, architecture family, materials, height, frontage, signage, access tier and district identity together so the result feels coherent.
- Place a deliberate mix of open businesses, residences, private properties, closed storefronts, vacant lots, construction sites and ambient structures.
- Do not mark a building enterable unless a valid interior or supported interaction endpoint exists.
- Do not create a visible “Press to Enter” prompt without a working destination or explicit unavailable-state response.
- Preserve navigation, collision, accessibility, performance and streaming requirements for all tiers.
- Support later upgrades: an ambient or limited-interaction building may become a full destination without changing its stable building_id.

## 8. Department ownership

- SAM: approve signature-building canon, names, priorities and launch scope.
- ATLAS: building records, stable IDs, schema contracts and engine-neutral data.
- URBAN: district placement, building types, architecture families, street frontage, signage and generated naming rules.
- VIBE: venue identity, activity design, events and social loops.
- PERSONA: staff, residents, visitors, fashion and character presentation.
- PULSE: NPC schedules, crowd behavior, business activity and open/closed world states.
- MOTION: parking, curb access, transit entrances, docks, pedestrian links and route connectivity.
- VECTOR: Unreal implementation and Unity adapter parity for interaction, interiors, streaming and prompts.
- NEXUS: persistent business/player state where required.
- SENTINEL: test that names, access states, prompts, interiors, services and interactions agree and never imply unsupported functionality.

## 9. Next production pass

1. Creator reviews the initial signature-building inventory and resolves the airport and casino names.
2. Assign each signature building to a district and block.
3. Define the exact player actions and services for each Tier A and Tier B destination.
4. Select reusable interior families and identify which destinations need bespoke interiors.
5. Build the engine-neutral building registry and validation schema.
6. Extend World Builder rules to generate named ordinary buildings around the signature destinations.
7. QA every displayed name and interaction prompt against the actual building record and implemented gameplay.


## 3B. Hustle Club placement refinement

Creator direction places Hustle Club in the waterfront cluster as a beachfront casino/nightlife destination. It is not a downtown Diamond District venue. Keep it distinct from Get Wild Beach, which is a separate beach-party destination in the broader coastal area. Hustle Towers remains a separate downtown landmark. Exact waterfront parcel adjacency and access are unresolved.


## 3C. Creator-approved Entertainment District additions and interaction direction

### Circular glass automotive tower — approved concept
- A major circular, glass-dominant automotive tower with a current creator-directed planning target of approximately **30–40 levels**.
- Display vehicles around the structure on every level. The most expensive and exclusive vehicles belong toward the top; other vehicle categories descend through the lower levels.
- It must be a visitable, explorable automotive destination with meaningful browsing and vehicle inspection, not merely a decorative tower.
- Exact building name, operator/brand association, final height, floor taxonomy, circulation, vehicle access, sales flow and launch scope remain unresolved.

### Walk-through automotive marketplace / car lot — approved concept
- A separate ground-oriented automotive marketplace, distinct from the circular tower.
- Organize it into recognizable sections, including expensive vehicles and regular vehicles; additional categories can be determined during detailed design.
- Players can walk through the lot, look at and inspect vehicles, interact with NPC salespeople and other visitors, and choose a vehicle through a supported selection/purchase interaction.
- The lot should feel socially active, not like a static vehicle menu.
- Whether it is operated by Mazerati Boys Automotive Group or another approved entity remains unresolved.

### Book of Code Movie Theater — confirmed name
- **Book of Code** is the creator-confirmed movie theater name.
- Preserve the exact title. It is a distinct Entertainment District destination.
- Screening catalog, schedules, ticketing, premieres and other event functions remain to be specified.

### Other approved Entertainment District destinations
- Outdoor concert amphitheater.
- Comedy club.
- Film and television production campus containing Upper Level Entertainment Studios, Upper Level Films and Monster Beats, co-located under their shared blue-and-black visual identity.
- The district must contain additional entertainment destinations beyond the media campus.

### Venue interaction standard: NPC-led activity and group outings
Entertainment venues should support purposeful social sessions and NPC activity. The creator's comedy-club example establishes this design direction:
- Players can go with friends or a group, enter together, and pay admission where applicable.
- Inside, players can socialize and use supported activities such as drinks, smoking interactions and card trading where enabled and appropriate to the venue.
- NPC performers should carry out actual venue roles; at the comedy club, an NPC comedian can stand on stage and perform for an audience.
- NPC staff, performers and visitors should make venues feel active even when players are not hosting an event.
- Future systems should support creator-designed events, missions and automated NPC-interactive sequences. These are a planned extension of the venue framework; no specific event, mission, schedule, reward or automation behavior is locked by this entry.

Implementation must distinguish a visible prop from a functioning interaction. Admission, party/group arrival, NPC performance, social activities and any consumable/card interactions must be connected to real game state and validated systems when implemented. Exact mechanics, schedules, pricing and launch scope remain TBD.


## 3E. Creator clarification — Monster Beats vs. Monster Beach

These are separate, creator-directed identities and must not be conflated:
- **Monster Beats** is part of the **Upper Level Entertainment Studios** campus in the Entertainment District.
- **Monster Beach** is a separate waterfront destination located by the **Hustle Club beachfront casino**.
- Do not move Monster Beach into the studios grounds, rename Monster Beats, or treat the names as interchangeable.
- **Ain't You Funny Comedy Club** is the confirmed comedy-club name.


## 3F. Creator correction — Monster Beach vs. Get Wild Beach

This section supersedes the previous section 3E placement of Monster Beach:
- **Get Wild Beach** is beside the **Hustle Club beachfront casino** in the waterfront cluster.
- **Monster Beach** is inside the grounds of **Upper Level Entertainment Studios** in the Entertainment District.
- These are distinct beach destinations with distinct locations. Never conflate their names or move one into the other's area.
- **Monster Beats** remains an established separate name; do not assume it is a synonym for Monster Beach or invent a relationship between them.
- Upper Level Films / Television / Production remains a separate, nearby major campus.
- Ain't You Funny Comedy Club remains the creator-confirmed comedy-club name.
