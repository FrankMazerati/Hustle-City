# Hustle City — Super Agent Batch Roadmap

**Status:** Canonical production sequencing plan  
**Owner:** Hustle City Super Agent  
**Project Lead / independent QA:** ChatGPT coordinating conversation  
**Final authority:** Creator  
**Work branch:** `knowledge-library-foundation` (PR #11; do not merge to `main` without explicit approval)

## Purpose

This roadmap turns the nine memory sections and Super Agent charter into a start-to-finish production queue. A **batch** is a coordinated group of related packages with a clear entry condition, deliverables, dependencies and exit gate. A batch may contain several 30-minute work blocks and several package checkpoints. Thirty minutes is a default checkpoint, not a deadline.

Build Hustle City itself first. Do not build the entire surrounding world as a prerequisite. The opening train-arrival cinematic is an early creative requirement and must influence the station, route, camera staging, weather, lighting and atmosphere.

## Batch operating rules

1. Start each batch by reading the Master Project index, this roadmap, the relevant memory records and the current dependency state.
2. Work only from Creator-approved requirements. Mark assumptions as proposed or unresolved.
3. Break a batch into independently reviewable packages. Use stable IDs: `HC-B01-P01`, etc., while retaining existing package IDs such as `HC-000` through `HC-007` as aliases where already established.
4. Each package has a 30-minute target block, immutable versioned checkpoint, handoff manifest and acceptance checklist. Continue in additional blocks when necessary.
5. After Package A is submitted, begin Package B only when B is safe and does not depend on unapproved A. ChatGPT reviews A during B.
6. ChatGPT fixes only minor, isolated, unambiguous, low-risk issues when it has access and can verify the change. Moderate/specialist corrections go to the Super Agent correction queue. Major or accumulating defects trigger a Creator + ChatGPT + Super Agent review.
7. Do not edit a submitted version under active review. Corrections create a new version and preserve the prior artifact.
8. At each checkpoint update the owning memory section(s), QUALITY records, Master Project index, production queue, correction queue and ChatGPT minor-fix log.
9. Keep the local runtime scheduler disabled until model inference, memory retrieval/write-back, package versioning and review/correction handoffs pass tests on the actual host.
10. No paid services, paid fallback, spending, or merges to `main` without explicit Creator approval.

## Batch 0 — Agent readiness and project intake

**Purpose:** Make the Super Agent startable and safe before assigning game-production work.

**Packages**
- `HC-B00-P01` — Read charter, system prompt, memory architecture, production cycle, config and this roadmap; reconcile conflicts.
- `HC-B00-P02` — Confirm repository branch/PR, memory root, asset root, backup location and write permissions.
- `HC-B00-P03` — Verify the selected local model tag on the actual host and complete one bounded inference; record measured constraints. Do not assume a previously downloaded model is available.
- `HC-B00-P04` — Run a dry-run package through selective memory retrieval, immutable checkpoint, handoff, QA return, correction version and memory write-back.

**Outputs:** Startup report, verified environment facts, active model record (or explicit blocker), memory index, package queues and dry-run evidence.

**Exit gate:** Required files and storage are readable/writable; backup exists; one model inference passes; handoff/write-back dry run passes. If any host-dependent gate fails, report the blocker and keep scheduler disabled. Preparation can continue manually without claiming autonomy.

**Memory:** MASTER PROJECT, SYSTEMS, QUALITY, ASSET LIBRARY.

## Batch 1 — Creative and cinematic foundation

**Purpose:** Establish the approved creative identity before fixing city geometry.

**Packages**
- `HC-B01-P01` / legacy `HC-000` — Consolidate Creator-approved SCRIBE & LENS direction.
- `HC-B01-P02` — Opening train-arrival cinematic treatment: story beats, arrival sequence, camera positions/movement, shot continuity and player reveal.
- `HC-B01-P03` — Weather, climate, seasons, time-of-day, sky, lighting, atmosphere, environmental mood, sound/music and player-experience direction.
- `HC-B01-P04` — Convert creative requirements into spatial reservations and implementation dependencies for the station, rail route, sightlines and staging.

**Outputs:** Creative direction bible, cinematic beat/shot sheet, weather/lighting/atmosphere matrix, unresolved-decision register and city-planning constraints.

**Exit gate:** Creator-approved creative brief; no invented canon; opening cinematic requirements are traceable to later WORLD, TRANSPORTATION and SYSTEMS packages.

**Memory:** SCRIBE & LENS, MASTER PROJECT, QUALITY; cross-link WORLD and TRANSPORTATION.

## Batch 2 — Hustle City master plan

**Purpose:** Establish the city footprint and authoritative spatial framework, not detailed buildings.

**Packages**
- `HC-B02-P01` / legacy `HC-001` — City scale, orientation, boundaries and coordinate convention.
- `HC-B02-P02` — Waterfront, major landforms, city edges and primary landmarks.
- `HC-B02-P03` — Spatial registry, map layers, naming/ID rules and reserved corridors/plots.
- `HC-B02-P04` — Validate cinematic station/route/sightline reservations against the master plan.

**Outputs:** Master city plan, coordinate/orientation standard, geography registry, landmark and corridor reservations, open questions.

**Exit gate:** Creator approval of the master plan and spatial conventions before detailed network/building work treats them as final.

**Memory:** WORLD, MASTER PROJECT, QUALITY.

## Batch 3 — Expressway network

**Purpose:** Define the major and short expressways that shape city circulation.

**Packages**
- `HC-B03-P01` / legacy `HC-002` — Primary expressway alignments and city connections.
- `HC-B03-P02` — Secondary/short expressways and connectors.
- `HC-B03-P03` — Interchanges, ramps, bridges, tunnels, merge/diverge logic and access constraints.
- `HC-B03-P04` — Naming, IDs, junction registry and spatial consistency review.

**Outputs:** Expressway network map, corridor/segment registry, interchange schedule, bridge/tunnel list and dependency notes.

**Exit gate:** Network fits the approved master plan; junctions and corridors are uniquely identified; no unapproved conflict with rail, waterfront or reserved cinematic access.

**Memory:** WORLD, SYSTEMS, QUALITY.

## Batch 4 — Street network and addressable public realm

**Purpose:** Build the permanent street framework and naming registry.

**Packages**
- `HC-B04-P01` / legacy `HC-003` — Street hierarchy and local street network.
- `HC-B04-P02` — Permanent street names, IDs and naming validation.
- `HC-B04-P03` — Intersections, sidewalks, crossings, markings, traffic-control locations and pedestrian connections.
- `HC-B04-P04` — Connectivity and continuity audit against expressways and reserved transit corridors.

**Outputs:** Street map, street-name registry, intersection/crossing registry and pedestrian/public-realm standards.

**Exit gate:** No duplicate street IDs/names where uniqueness is required; street connections are continuous and traceable; Creator-reserved names/areas are preserved.

**Memory:** WORLD, SYSTEMS, QUALITY.

## Batch 5 — Rail, train and subway network

**Purpose:** Establish all transit corridors and station reservations, including the opening cinematic's train arrival.

**Packages**
- `HC-B05-P01` / legacy `HC-004` — HIM train corridor, operations and station plan.
- `HC-B05-P02` — City train corridor, stops and transfer relationships.
- `HC-B05-P03` — Subway corridors, stations, entrances and interchange relationships.
- `HC-B05-P04` — Platforms, yards, service access, passenger circulation and station spatial reservations.
- `HC-B05-P05` — Opening cinematic station/route fit check against Batch 1.

**Outputs:** Transit network map, station/route registry, platform and transfer requirements, operations assumptions and reserved cinematic staging.

**Exit gate:** Corridors and stations fit the approved city/street plan. Preserve the name **HIM**; do not invent an acronym expansion. Operational details remain proposed until approved.

**Memory:** TRANSPORTATION, WORLD, SYSTEMS, SCRIBE & LENS, QUALITY.

## Batch 6 — Marina and waterfront access

**Purpose:** Establish the marina and water-facing circulation as part of Hustle City.

**Packages**
- `HC-B06-P01` / legacy `HC-005` — Waterfront/marina footprint, docks, slips and vessel zones.
- `HC-B06-P02` — Navigation access, shoreline access and connections to roads/public spaces.
- `HC-B06-P03` — Service, pedestrian, parking and operational circulation.
- `HC-B06-P04` — Cross-check against city boundaries, transport corridors and waterfront landmarks.

**Outputs:** Marina/waterfront plan, dock/slip registry, access/circulation plan and unresolved operational requirements.

**Exit gate:** Marina fits the master plan and does not create unreviewed conflicts with transport or public access.

**Memory:** WORLD, TRANSPORTATION, SYSTEMS, QUALITY.

## Batch 7 — Districts and neighborhoods

**Purpose:** Organize the city into recognizable, connected districts and neighborhoods.

**Packages**
- `HC-B07-P01` / legacy `HC-006` — District boundaries and identities.
- `HC-B07-P02` — Neighborhood boundaries, character and internal organization.
- `HC-B07-P03` — District gateways, connectors, public spaces and transit/road access.
- `HC-B07-P04` — Verify continuity with Creator-approved district plans and visual references.

**Outputs:** District/neighborhood atlas, boundary registry, identity briefs and connectivity map.

**Exit gate:** Boundaries and names trace to approved decisions; proposed palettes/identities remain proposed until approved; all districts connect to the city network.

**Memory:** WORLD, SCRIBE & LENS, MASTER PROJECT, QUALITY.

## Batch 8 — Building plots and development framework

**Purpose:** Establish where buildings and venues belong before detailed asset production.

**Packages**
- `HC-B08-P01` / legacy `HC-007` — Building plots and footprints.
- `HC-B08-P02` — Height/massing envelopes, setbacks and frontage rules.
- `HC-B08-P03` — Parking, public space, service/loading, emergency and pedestrian access.
- `HC-B08-P04` — Landmark, venue and opening-cinematic location reservations.

**Outputs:** Plot/footprint registry, development envelopes, access requirements and prioritized building/venue queue.

**Exit gate:** Every plot has a stable ID, district assignment, access logic and dependencies; no detailed building package is treated as final without a valid plot.

**Memory:** WORLD, SYSTEMS, MASTER PROJECT, QUALITY.

## Batch 9 — Building kits, landmarks and venues

**Purpose:** Turn approved plots into detailed buildings and reusable modular kits.

**Package groups:** modular building systems; residential/commercial/industrial/civic buildings; stores and clubs; casino and entertainment venues; police/emergency/public facilities; transit and station interiors; interior circulation, service spaces and interaction-ready layouts.

**Rules:** Use existing source assets only after provenance/licensing review. Keep source downloads untouched. Trapper City building set and other collections remain separately inventoried and evaluated. Prioritize reusable kits and high-value city landmarks before low-priority decoration.

**Exit gate:** Each building/venue fits its plot and access requirements, has documented asset provenance, consistent scale/material standards and a QA handoff.

**Memory:** WORLD, ASSET LIBRARY, SYSTEMS, QUALITY.

## Batch 10 — People and character foundation

**Purpose:** Establish reusable people/character standards and the first city population.

**Package groups:** character identity/profile schema; body/face/hair standards; rigs and animation integration; personality/behavior/routines; recognition and per-Sim encounter memory design; population placement and schedule dependencies.

**Exit gate:** Character identities are stable, rigs/animations are traceable to sources, and Sim memory is distinguished from Super Agent project memory.

**Memory:** PEOPLE, ASSET LIBRARY, SYSTEMS, QUALITY.

## Batch 11 — Transportation assets and operations

**Purpose:** Populate the city with usable road, rail, air and water transportation.

**Package groups:** cars/trucks/taxis/buses; rail vehicles; aircraft/helicopters; boats/yachts; depots/stations/airport/marina support; routes, schedules, handling, parking, collision and service requirements.

**Exit gate:** Each transport asset has source/provenance, stable ID, scale/rig/collision requirements and an owning operational/system contract.

**Memory:** TRANSPORTATION, ASSET LIBRARY, SYSTEMS, WORLD, QUALITY.

## Batch 12 — Social and lifestyle

**Purpose:** Build the everyday life layer as a distinct production area.

**Package groups:** clothing/fashion/outfits/wardrobes/changing; friendships/family/dating/rivalries; conversations/calls/messages; parties/birthdays/concerts/events; invitations/notifications/reminders/social calendars; everyday routines and social activities.

**Exit gate:** Social features link correctly to people identity, gameplay/runtime systems and relevant assets. Clothing and social content are not buried in the People section.

**Memory:** SOCIAL & LIFESTYLE, PEOPLE, ASSET LIBRARY, SYSTEMS, QUALITY.

## Batch 13 — Core gameplay and simulation systems

**Purpose:** Implement the functional contracts that make the city playable and persistent.

**Package groups:** player controls/HUD; interactions; traffic and pedestrian simulation; weather implementation; physics/collision; economy and persistence; AI/runtime scheduling; communications/event delivery; save/load and data contracts.

**Exit gate:** Each system has explicit input/output contracts, deterministic tests where applicable, persistence behavior, failure handling and independent QA evidence.

**Memory:** SYSTEMS, QUALITY, with links to all owning content sections.

## Batch 14 — Integration and playable vertical slice

**Purpose:** Integrate one coherent, testable slice instead of attempting all content at once.

**Recommended slice:** opening train arrival → station/nearby streets → one connected district → a small set of buildings/venues → representative people → transport and social interactions → save/reload.

**Exit gate:** The Creator can inspect and experience the slice; core flow works end-to-end; critical defects are resolved or explicitly accepted; performance and asset budgets are documented. This gate does not imply the entire game is complete.

**Memory:** MASTER PROJECT, SYSTEMS, QUALITY, and all contributing content sections.

## Batch 15+ — Expansion waves

Expand the remaining city content and systems in Creator-approved priority order. Keep the same package, memory, provenance, QA, versioning and correction rules. New batches are added to this roadmap and Master Project index before work begins.

## Standard batch exit report

Every batch closes with:
- Completed package IDs and exact artifact paths/record IDs
- Creator-approved requirements covered
- Dependencies satisfied and remaining
- QA findings by severity, evidence and owner
- ChatGPT minor fixes with before/after and verification
- Super Agent correction queue
- Memory sections and Master Project index updated
- Open decisions reserved for Creator
- Next safe batch/package recommendation
- Honest runtime/build status; no unperformed checks claimed

## Initial active queue

1. Batch 0 readiness gate (only what is not already verified).
2. Batch 1 creative/cinematic foundation.
3. Batch 2 city master plan.
4. Batch 3 expressways.
5. Batch 4 street network.
6. Batch 5 transit.
7. Batch 6 waterfront.
8. Batch 7 districts/neighborhoods.
9. Batch 8 building plots.
10. Batches 9–14 in dependency and Creator-priority order.

The queue is a starting sequence, not permission to invent missing Creator decisions. Independent packages may overlap when their dependencies are safe.
