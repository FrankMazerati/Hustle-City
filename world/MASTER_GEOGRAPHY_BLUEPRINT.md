# Hustle City — Master Geography Blueprint

**Status:** Foundation draft based on creator-approved direction in the current planning conversation.  
**Branch:** `world/master-geography-transit-foundation`  
**Purpose:** Establish the spatial rules that every future world, district, neighborhood, road, rail, venue, and database workstream must follow.

## 1. Non-negotiable world identity

Hustle City is an original fictional American city. Its flagship environment uses selected Chicago-inspired urban character and Florida-inspired tropical/coastal atmosphere without copying either real city. The world must remain geographically coherent and expandable.

Unreal Engine 5 is the primary production target. Unity 6 is the secondary compatibility/migration target. Canonical geography and world data must remain engine-neutral.

## 2. City structure

The city is organized into two major geographic layers:

1. **Six central district boxes** — the core urban districts.
2. **Surrounding outer boxes** — reserved for individual neighborhoods and the city's expanding outer areas.

The six district concepts currently recorded in the project atlas are:

- Downtown District
- Financial District
- Diamond District
- Entertainment District
- Marina District
- Fashion / Swagger District — working label; final name remains open

The six districts are established as the central planning structure. Their exact boundaries, relative positions, dimensions, and final names where noted must be reconciled against the creator's original map references before being treated as final coordinates.

### Outer neighborhood boxes

- Every surrounding box is reserved for a neighborhood-scale area; do not silently repurpose one as an unrelated central district.
- Neighborhoods must be individually identifiable and capable of having their own visual identity, entrance, local destinations, community activity, and ownership/residency records.
- A neighborhood's existence, visual identity, player founding/ownership, crew leadership, property ownership, business ownership, and residency are separate systems.
- Neighborhoods may be visually populated and ambiently active even when only selected venues are fully interactive.
- Exact neighborhood count, numbering, grid dimensions, and block subdivision remain subject to reconciliation with the original map and conversation archive.

### Planning-envelope note

An earlier repository atlas records a 7×7 / 49-box planning envelope, six central boxes, 43 potential outer boxes, and a 5×5 block-planning concept inside each outer box. Treat those figures as a **previously recorded capacity model**, not a newly re-approved launch commitment. Do not create or number all 43 neighborhoods, or assume every block must be built, until the original map references are reviewed with the creator.

## 3. Spatial hierarchy

Use this hierarchy in documents, data, and future engine-neutral world definitions:

`World → City → District or Outer Neighborhood → Neighborhood (where applicable) → Block → Parcel / Lot → Building / Venue → Interior Space`

The six central districts and the surrounding neighborhood boxes are distinct top-level planning areas within Hustle City. A neighborhood may contain blocks, parcels, properties, businesses, public spaces, transit stops, and landmarks.

Do not confuse:
- district membership with neighborhood residency;
- neighborhood founding/ownership with crew membership;
- crew leadership with property or business ownership;
- a station's service area with the neighborhood's ownership boundary.

## 4. Macro infrastructure must be reserved first

Before detailed buildings are placed, reserve corridors and land for:

- primary and secondary streets, avenues, and connecting roads;
- the elevated Skyway and ground-level expressway systems;
- Hustle City Transit Authority rail corridors and stations;
- Hustle International Metro approaches, terminal, and interchange facilities;
- bus and pedestrian connections;
- bridges, waterways, shoreline access, marina and water-transport corridors where the geography supports them;
- parks, civic spaces, utilities, service access, and emergency access.

A corridor reservation is a spatial constraint, not a finished road or rail asset. Buildings must not consume a reserved corridor without an approved map revision.

## 5. Transportation relationship to geography

Two passenger railway authorities serve different trip scales:

- **Hustle International Metro (HIM):** intercity and regional passenger rail connecting Hustle City with other cities and destinations.
- **Hustle City Transit Authority (HCTA):** local transit connecting downtown, the six districts, outer neighborhoods, and surrounding city areas.

Every designated outer neighborhood must have a usable HCTA station connection. A player must be able to travel from their neighborhood through HCTA to an HIM interchange and then take HIM to another city. Selected outer locations may become direct HIM interchange/terminal stations if the final geography and route plan justify them; direct HIM service at every neighborhood is not assumed.

Detailed route alignment, station positions, route count, line colors, service patterns, and station names remain open until the map is reconciled.

## 6. Map conventions

When the map is authored, it should have separate toggleable layers:

- base geography / water / terrain;
- six central districts;
- outer neighborhood boxes and boundaries;
- blocks and major parcels;
- arterial roads and expressways;
- HIM intercity rail;
- HCTA local rail, differentiated by route and operating environment;
- stations, transfer points, terminals, and pedestrian access;
- major landmarks, venues, civic spaces, and utilities.

Use a consistent coordinate reference and stable IDs. Human-readable names may change; IDs should not.

## 7. Build order

1. Reconcile original map images and early design conversations.
2. Lock the master-map envelope and six district positions.
3. Confirm outer neighborhood box arrangement and naming convention.
4. Reserve water, shoreline, major road, Skyway, and expressway corridors.
5. Reserve HIM terminal, approaches, and intercity connections.
6. Reserve HCTA rail corridors, district stations, neighborhood stations, and transfers.
7. Define neighborhood boundaries and block structure.
8. Place major landmarks, venues, civic destinations, and transport-support facilities.
9. Only then progress into detailed parcels, buildings, interiors, props, and ambient population.

## 8. Acceptance checklist

- [ ] Six central district boxes are represented without inventing new districts.
- [ ] All surrounding boxes remain reserved for neighborhoods.
- [ ] The six district names and any working labels are clearly status-tagged.
- [ ] Exact box count and dimensions are reconciled with original references before final lock.
- [ ] HIM and HCTA are represented as separate passenger rail authorities.
- [ ] Every neighborhood has an HCTA access path.
- [ ] A neighborhood-to-HIM intercity journey is possible through a defined interchange.
- [ ] Major transport corridors are reserved before detailed building placement.
- [ ] All unresolved geography is visible as unresolved, not silently guessed.

## 9. Related canonical documents

- [World Identity Bible](WORLD_IDENTITY_BIBLE.md)
- [Transportation Network Specification](TRANSPORTATION_NETWORK_SPEC.md)
- [Consolidated Design Atlas](../docs/PROJECT_DESIGN_ATLAS.md)
- [Decision Log](../docs/DECISION_LOG.md)
- [Roadmap](../planning/ROADMAP.md)
