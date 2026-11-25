# Hustle City — Super Agent Memory Architecture

**Status:** Canonical design under the Super Agent Charter  
**Top-level sections:** 9  
**Design principle:** One Super Agent identity, selective retrieval, cross-linked records, persistent write-back.

## Memory map

| ID | Section | Primary contents |
|---|---|---|
| HC-MEM-01 | MASTER PROJECT | Global index, decisions, project state, dependencies, priorities, package queue, milestones and history |
| HC-MEM-02 | SCRIBE & LENS | Story, cinematics, camera, weather/climate/patterns, seasons, time, sky, lighting, atmosphere, sound/music and player experience |
| HC-MEM-03 | WORLD | City geography, districts, neighborhoods, terrain, roads, expressways, rail corridors, waterfront, plots, buildings and interiors |
| HC-MEM-04 | PEOPLE | Character identity, personality, behavior, schedules, animation, rigs and per-Sim encounter/recognition memories |
| HC-MEM-05 | TRANSPORTATION | Cars, trucks, taxis, buses, trains, subway, aircraft, helicopters, boats, yachts, stations, airport, marina and transport operations |
| HC-MEM-06 | SYSTEMS | Controls, HUD, interaction contracts, gameplay, physics, traffic, weather simulation implementation, economy, persistence and integration |
| HC-MEM-07 | QUALITY | Standards, test cases, inspection reports, defects, corrections, regression checks and approvals |
| HC-MEM-08 | ASSET LIBRARY | Original downloads/photos/videos, provenance, licenses, processed models, meshes, textures, materials, rigs and animations |
| HC-MEM-09 | SOCIAL & LIFESTYLE | Clothing/fashion/wardrobes, relationships, communication, messages/calls, events, invitations, notifications, calendars and everyday activities |

## Retrieval router

1. Read the compact Master Project index and current task record.
2. Identify the primary memory section and any cross-domain dependencies.
3. Retrieve only the relevant records from those sections.
4. Follow record links as needed; do not bulk-load all nine archives by default.
5. Build a concise active working brief with source IDs, constraints, open questions and acceptance criteria.
6. After production, update the owning section(s), linked records and Master Project index.
7. Add QA findings to QUALITY and update the package's status. Preserve prior versions and provenance.

## Cross-domain examples

- Rainy train-arrival cinematic: SCRIBE & LENS + WORLD + TRANSPORTATION + SYSTEMS + QUALITY.
- Car asset/handling task: TRANSPORTATION + ASSET LIBRARY + SYSTEMS + WORLD + QUALITY.
- Character outfit and party: SOCIAL & LIFESTYLE + PEOPLE + ASSET LIBRARY + SYSTEMS + QUALITY.
- NPC recognizes a returning person: PEOPLE (identity/encounter memory) + SOCIAL & LIFESTYLE (relationship/communication) + SYSTEMS (runtime persistence and retrieval) + QUALITY.
- A boat at the marina: TRANSPORTATION + WORLD + SYSTEMS + ASSET LIBRARY + QUALITY.

## Record conventions

Use stable IDs, for example:
- `HC-WORLD-ROAD-0001`
- `HC-PEOPLE-SIM-0042`
- `HC-TRANSPORT-BOAT-0012`
- `HC-SOCIAL-REL-0031`
- `HC-SL-EVENT-0018`
- `HC-QUALITY-DEFECT-0024`

Recommended record fields:

```yaml
record_id: HC-TRANSPORT-BOAT-0012
section: TRANSPORTATION
subcategory: Boats_Yachts
title: Example boat record
status: proposed
version: 1
updated_at: YYYY-MM-DD
source_refs: []
requirements: []
acceptance_criteria: []
asset_refs: []
related_records: []
dependencies: []
qa:
  status: not_reviewed
  evidence: []
open_items: []
change_history: []
```

## Physical storage layout

```text
HUSTLE_CITY/
├── 00_MASTER_PROJECT/
│   ├── Index/
│   ├── Decisions/
│   ├── Dependencies/
│   ├── Production_Status/
│   └── Package_Queue/
├── 01_SCRIBE_LENS_MEMORY/
│   ├── Story/
│   ├── Cinematics/
│   ├── Camera_Direction/
│   ├── Weather_Climate_Seasons/
│   ├── Time_Lighting_Atmosphere/
│   └── Audio_Direction/
├── 02_WORLD_MEMORY/
│   ├── Geography/
│   ├── Districts_Neighborhoods/
│   ├── Roads_Expressways/
│   ├── Transit_Corridors/
│   ├── Waterfront/
│   ├── Building_Plots/
│   ├── Buildings/
│   └── Interiors/
├── 03_PEOPLE_MEMORY/
│   ├── Characters/
│   ├── Personalities_Behavior/
│   ├── Schedules/
│   ├── Animation_Rigs/
│   └── Sim_Encounter_Memories/
├── 04_TRANSPORTATION_MEMORY/
│   ├── Cars_Trucks_Taxis/
│   ├── Buses/
│   ├── HIM_City_Train_Subway/
│   ├── Aircraft_Helicopters/
│   ├── Boats_Yachts/
│   └── Stations_Airport_Marina_Operations/
├── 05_SYSTEMS_MEMORY/
│   ├── Controls_HUD/
│   ├── Interactions/
│   ├── Traffic_Physics/
│   ├── Weather_Simulation/
│   ├── Economy/
│   ├── Persistence/
│   └── Gameplay_Integration/
├── 06_QUALITY_MEMORY/
│   ├── Standards/
│   ├── Test_Cases/
│   ├── Inspections/
│   ├── Defects/
│   ├── Corrections/
│   └── Approvals/
├── 07_ASSET_LIBRARY/
│   ├── Original_Downloads/
│   ├── Original_Photographs/
│   ├── Reference_Videos/
│   ├── Source_Provenance_Licenses/
│   ├── Models_Meshes/
│   ├── Textures_Materials/
│   └── Rigs_Animations/
└── 08_SOCIAL_LIFESTYLE_MEMORY/
    ├── Clothing_Fashion_Wardrobes/
    ├── Relationships/
    ├── Communication_Messages_Calls/
    ├── Events_Invitations/
    ├── Notifications_Reminders/
    ├── Social_Calendars/
    └── Everyday_Activities/
```

The folder numbering is storage organization; the logical memory IDs remain HC-MEM-01 through HC-MEM-09. Preserve all original source files and keep a second backup of essential project memory.
