# Hustle City — Living City Simulation, NPC, Traffic, Events & Safety Specification

**Branch:** world/master-geography-transit-foundation  
**Budget:** Free 99 — $0 spend until investor funding  
**Primary engine:** Unreal Engine 5  
**Status:** design specification and free-template shortlist; no runtime implementation or third-party binary integration claimed.

## 1. Design objective

Hustle City must behave like a living urban simulation, not a static collection of environments. People have routines and needs. Vehicles obey traffic rules. Public transport follows routes and operating plans. Venues and neighborhoods host scheduled and emergent events. Public safety, boundaries, accessibility, recovery and continuity are systemic.

**Core experience principle:** the objective is to live, explore, build relationships, travel, work, socialize and participate in city life while staying safe. Death is not the central objective or default gameplay loop. Risk and consequences may exist where the creator approves them, but safety, prevention, de-escalation, recovery and meaningful continuity are foundational.

This is a design specification, not a claim that these systems are already running.

## 2. Free reusable technical foundations

| Foundation | Relevant capabilities | Hustle City use | Decision |
|---|---|---|---|
| Epic City Sample UE 5.8 | Mass AI, ZoneGraph, crowds, vehicle traffic, MetaHuman crowds, Chaos vehicles, World Partition, PCG, Niagara and MetaSounds | Primary reference and reusable starting point for urban crowd/traffic architecture | PRIORITY 1 — free Epic sample; validate engine/version and terms |
| City Sample Crowd | MetaHuman-adapted crowd characters and wardrobe | NPC visual starting library and crowd archetypes | PRIORITY 1 — free extracted pack; check engine compatibility |
| City Sample Vehicles | Vehicle meshes and vehicle sample content | Traffic vehicle visual foundation and vehicle handling reference | PRIORITY 1 — free extracted pack; verify exact package/version |
| Lyra Starter Game | Gameplay framework, input, modular features, multiplayer architecture patterns | Player experience and modular gameplay architecture | PRIORITY 1 — free Epic sample |
| Game Animation Sample | Locomotion and animation Blueprint patterns | NPC/player locomotion and animation starting point | PRIORITY 2 — free Epic sample |
| Epic Gameplay Framework / AI docs | Behavior Trees, Mass Entity, StateTree, Navigation, Smart Objects, EQS, AI Perception | NPC behavior, schedules, world interactions and decisions | PRIORITY 1 — engine systems/documentation |
| Kenney Train Kit via Summer Engine | 103 CC0 train, tram, passenger train, subway, track and spline-track models | Early visual blockout for HIM/HCTA rolling stock and track only | PRIORITY 2 — CC0; not a functional rail system |
| UETrafficGame | UE 5.1 traffic playground with CC0 assets | Optional isolated study of repeated vehicle routes and traffic | PRIORITY 3 — old engine version; inspect repository and license |
| CityGenerator (MIT) | City Sample / OSM city-generation workflow, traffic and pedestrian crowds | Optional procedural geography experiment | HOLD — requires UE 5.8.2, Houdini 22, Houdini Engine and SideFX Labs; dependency may not fit $0 |
| ue5-ai-traffic plugin | Chaos vehicles and AIController traffic | Not adopted | EXCLUDED — modified CC BY-NC terms, unsuitable for commercial release without separate permission |

**License boundary:** the ue5-ai-traffic repository's included license restricts use to non-commercial purposes. Hustle City is intended to become commercial, so do not incorporate it without suitable written permission. A public GitHub repository is not automatically commercially reusable.

## 3. Simulation architecture

Use a layered, data-driven simulation with clear ownership. Avoid one giant AI controller or monolithic Blueprint.

### A. City Simulation Director
Owns simulation time, district activity profiles, event scheduling, population budgets, weather/time-of-day inputs, emergency state and world activity level. Reduces simulation detail for distant/off-screen districts.

### B. Agent identity and population
Each persistent NPC has a stable ID and authored profile. Crowd agents can be lightweight Mass entities; nearby/high-interaction characters can be promoted to full character actors.

NPC profile fields:
- identity/archetype and appearance/wardrobe references
- home/residential anchor and permitted living area
- work/study/venue role and schedule template
- relationships and social affiliations where applicable
- mobility/accessibility preferences
- needs, mood, current goal, activity and state
- permissions, boundaries and safety state
- persistence tier and last-known state

Do not use a transient crowd instance ID as a permanent identity.

### C. NPC life simulation
NPCs have schedules and context-sensitive decisions:
- rest, commute, work/study, errands, meals, shopping, leisure and social time
- enter/exit buildings through valid doors and navigable paths
- queue, wait, sit, stand, browse, purchase, ask for help, board transit and transfer
- greet, recognize, converse, form friendships, disagree, leave, apologize and de-escalate
- react to weather, delays, crowd density, event announcements, closed venues and emergencies
- adapt schedules without teleporting through blocked geometry

Use StateTree or Behavior Trees for decisions, Smart Objects for usable world interactions, Navigation for local movement and Mass Entity/ZoneGraph for scalable crowds. Promote nearby agents to full actors.

### D. Needs and well-being
Needs are gameplay signals, not punitive timers. Candidate dimensions:
- rest/energy
- food and hydration
- hygiene
- comfort/weather exposure
- social connection
- safety/security
- money/resources where the game loop requires it
- travel/time pressure

Needs change gradually and contextually. Provide understandable feedback, accessible options and recovery routes. Avoid sudden unavoidable death from an untelegraphed hidden meter. Any severe health/injury/death mechanics require explicit creator approval and fairness/accessibility review.

### E. Vehicle and road traffic
Separate vehicle simulation into:
1. vehicle data and visual model
2. physics/handling (Chaos Vehicles for drivable or close vehicles)
3. traffic AI (lane following, speed choice, gap acceptance, yielding, turns, stops)
4. road graph and lane semantics (ZoneGraph or equivalent)
5. traffic control (signals, signs, crossings, priority, closures)
6. parking, loading, pickup/drop-off and emergency access
7. pedestrian/vehicle conflict avoidance

Traffic protocols:
- stop at red lights and stop controls
- yield at crossings and intersections according to signal/right-of-way state
- remain within valid lanes and turn connectors
- keep emergency access clear
- obey speed zones and temporary closures
- avoid collisions, blocked intersections and impossible U-turns
- detect stalled/disabled vehicles and trigger safe response
- allow authored emergency-vehicle priority without making ordinary traffic lawless

Do not rely on the non-commercial AiTraffic plugin. Prefer City Sample's documented traffic/ZoneGraph implementation as the primary study.

### F. Public transportation
HIM and HCTA remain separate authorities and service systems.

**HIM — intercity/regional**
- intercity arrival/departure terminals
- regional routes and scheduled services
- passenger information, boarding/alighting, platform safety and service disruption
- accessibility and staff/service details as approved

**HCTA — local**
- elevated, underground and street-level services where approved
- local station access, platform circulation, transfers and neighborhood coverage
- station-specific accessibility, emergency egress and wayfinding

Shared transit simulation:
- route graph, track graph, station stops, platforms, timetables and vehicle assignment
- dwell times, boarding/alighting queues and passenger capacity
- doors/platform alignment, departure readiness and headway rules
- signals, blocks, switches and route reservations as appropriate
- delays, maintenance windows, temporary closures and service recovery
- transfer windows and passenger information

A free static train mesh is not a train system. Build functional rail logic as original code/Blueprints and validate physical dimensions against engineering references.

### G. Events and social activity
Events are data-driven, scheduled, location-aware activities:
- street fairs, neighborhood gatherings, markets and pop-ups
- concerts, nightlife, sports/watch parties and venue programming
- fashion shows, retail launches and district celebrations
- civic announcements, transit service events and seasonal activities
- player-created gatherings only if multiplayer design supports them

Each event record includes:
- event ID, name, type, organizer/NPC, venue/area and start/end window
- capacity, admission/eligibility, accessibility and safety plan
- schedule, setup/teardown, staff roles and crowd-flow routes
- NPC attendance profile
- traffic/transit impact, temporary signage and cleanup
- state: planned, announced, active, paused, completed or cancelled

Events must not spawn crowds inside blocked geometry or overload station exits. Events communicate closures and alternate routes to transit/traffic.

### H. Safety, boundaries and protocols
Safety is part of world simulation:
- safe pedestrian paths, crossing controls and platform edge protection
- clear fire/emergency egress and accessible routes
- venue capacity and crowd-density thresholds
- emergency response roles, dispatch, wayfinding and assembly areas
- de-escalation and conflict avoidance
- personal/social boundaries and consent-aware interactions
- protected areas and restricted-access rules
- multiplayer anti-harassment safeguards
- recovery/respawn/checkpoint rules if the game includes failure states

NPCs respect player refusal, personal space, venue rules and restricted areas. Repeated unwanted interaction stops rather than escalating by default. Player safety controls and reporting/blocking tools are required if online social features are introduced.

### I. World persistence and performance
Use simulation fidelity tiers:
- **Near player:** full character, interaction, animation, collision and decision detail.
- **Active district:** simplified agents, schedules, traffic and event attendance.
- **Distant district:** aggregate counts, schedule/state summaries and low-frequency updates.
- **Unloaded world:** persist essential state and deterministic schedule progression only.

Use data assets/data tables for population archetypes, vehicle types, route schedules, event definitions, safety rules and district profiles. Avoid saving every frame of every NPC. Persist meaningful changes and last-known schedule state.

## 4. How the systems connect

Example: a district fashion event starts at 18:00.
1. Event Director announces event and marks venue capacity.
2. NPC schedule planner assigns eligible attendees.
3. Attendees choose walking, driving or HCTA.
4. Transit Director estimates passenger demand and dispatches service within approved capacity.
5. Traffic Director adjusts curb pickup, parking and nearby signal/closure rules.
6. Pedestrian navigation routes attendees through safe entrances and crossings.
7. Venue Smart Objects handle ticketing, queues, seating and interactions.
8. Crowd-density monitors thresholds; event pauses entry or redirects flows when needed.
9. At event end, NPCs disperse through safe routes; traffic/transit returns to normal.
10. Event history records attendance and district activity.

Systems exchange explicit events/messages rather than tightly depending on each other's internals.

## 5. Shared event/protocol interfaces

Suggested event names:
- CityTime.Advanced
- NPC.GoalChanged
- NPC.NeedsThresholdReached
- NPC.InteractionRequested
- NPC.BoundaryRefused
- Traffic.SignalChanged
- Traffic.LaneClosed
- Traffic.VehicleDisabled
- Transit.ServiceDelayed
- Transit.PlatformBoarding
- Transit.TransferAvailable
- Event.Announced
- Event.Started
- Event.CapacityThresholdReached
- Event.Completed
- Safety.EmergencyDeclared
- Safety.RouteBlocked
- Safety.AreaCleared
- World.DistrictActivityChanged

Each payload includes a unique event ID, simulation timestamp, source system, subject/target IDs, district/location reference, severity/priority and schema version.

## 6. Free 3D model and template strategy

Use Epic City Sample's separate Buildings, Vehicles and Crowd packs as first visual foundations. City Sample documents Mass AI, ZoneGraph, MetaHuman crowds, Chaos vehicles, Niagara and MetaSounds. Its Crowd StateTree and Smart Objects examples are useful starting points. Confirm extracted-pack engine compatibility separately from the UE 5.8 main project.

Use Kenney's CC0 train kit for early visual prototypes only. It lists passenger locomotives, subway and tram variants, track and spline track. It does not provide signaling, schedules, doors, passenger flow or a working railway.

Use City Sample vehicles/crowds as visual and technical references, then create Hustle City-specific variation: fashion, archetypes, district roles, workwear, uniforms, vehicle identity, paint, interiors, audio and behavior. Preserve source and creator metadata.

## 7. Safety and experience rules

- The world should be challenging through decisions, not arbitrary unavoidable failure.
- Give warnings before significant risk or service disruption.
- Provide clear, accessible escape/recovery options.
- Make public transport legible: route, destination, platform, service state and transfer directions.
- Never trap the player or NPCs behind a closed door without an alternate exit.
- Keep accessible routes available when stairs/escalators are out of service.
- Emergency and event crowd flows must not share a single bottleneck without capacity controls.
- Use safe platform distances, crossing controls and road/rail separation.
- Online social boundaries and moderation are mandatory before public multiplayer.
- Do not add lethal mechanics, injury severity or permadeath without creator approval.

## 8. Acceptance tests

1. NPC leaves home, reaches a destination, enters through a valid entrance, completes an activity and returns without teleporting.
2. NPC recognizes a closed venue and selects an alternate valid activity.
3. Crowd queue stays within marked safe capacity; overflow is redirected.
4. Vehicle stops at a red signal, yields at a valid crossing, follows lane graph and clears intersection.
5. Disabled vehicle triggers safe response and does not permanently deadlock the road.
6. Train follows reserved route, stops at platform, opens doors only when aligned, dwells, closes and departs.
7. Passenger boards/alights without crossing platform edge or walking through a train.
8. HIM and HCTA use distinct service identities and operating data; transfer works only at a designated interchange.
9. Event announcement updates NPC plans, transit demand, traffic and venue capacity.
10. Emergency state redirects affected routes and preserves accessible egress.
11. Player boundary refusal is respected by NPC behavior.
12. Off-screen population updates at reduced fidelity without breaking schedule continuity.
13. Save/reload restores essential player, event, transit and NPC state without duplicating agents.

## 9. Unresolved creator decisions

Do not invent exact NPC population counts, demographic distributions, named NPC roster, vehicle counts/brands, HIM/HCTA routes or stations, fares, event calendar/rewards, player-created event permissions, crime/police/weapons/lethal combat/permadeath mechanics, or multiplayer moderation policy. These require creator direction and/or approved world map and gameplay foundation.

## 10. Implementation status

This document is a specification and integration plan. Free Epic sample and asset links are candidates, not evidence of downloaded packages. No NPC simulation, traffic AI, rail operations, event director, safety protocol or acceptance test is claimed to be running in a compiled Unreal project yet.
