# Hustle City — Transportation Network Specification

**Status:** Foundational system direction; detailed routes, station locations, line count, and schedules are not yet approved.  
**Scope:** Passenger rail authorities and their relationship to the city master map.

## 1. Two separate passenger rail authorities

Hustle City has two distinct passenger railway systems. They must not be collapsed into one service or treated as interchangeable.

### 1.1 Hustle International Metro (HIM)

**Role:** Intercity and regional passenger railway.

HIM connects Hustle City to other cities and regions. Creator-provided examples include:

- Chicago
- Atlanta
- New York
- Florida destinations
- Additional destinations as the game world expands

These are destination examples, not a finalized route timetable or a claim that every destination is in the first release.

**Core gameplay role**
- Bring characters into Hustle City from outside the city.
- Provide departures from Hustle City to other cities.
- Support visitors, travel, story arrivals, and future multi-city expansion.
- Provide an intercity passenger experience with boarding, seating, window views, station stops, and disembarking.

The opening arrival of Frank Maserati and his female travel companion by intercity passenger train belongs to HIM. The arrival terminal is therefore a major story and world landmark.

### 1.2 Hustle City Transit Authority (HCTA)

**Role:** Local city and surrounding-area passenger transit.

HCTA connects:
- Downtown;
- all six central districts;
- surrounding neighborhood boxes;
- outer areas and designated local destinations.

HCTA is the network a player uses to move between their neighborhood and the central city.

## 2. HCTA operating environments

HCTA is designed to support three rail environments:

1. **Elevated rail** — guideways above streets or other infrastructure.
2. **Underground rail** — subway tunnels and underground stations.
3. **Street-level rail** — surface-running tracks, including dedicated transit corridors and suitable street-running sections.

A route may change operating environment along its journey when its vehicle, track, station, clearance, signaling, and safety design support that transition. This is a system capability, not a requirement that every route use all three environments.

Chicago's color-coded line approach is a useful naming and navigation inspiration. Final route count, line names, colors, and which routes use which environments remain unapproved. Red and Blue are examples only, not locked line assignments.

### Engineering rule

Do not assume every rail vehicle can use every track type. Heavy metro/subway and street-running light rail can have different vehicle, platform, power, signaling, and right-of-way requirements. Select compatible vehicle and infrastructure families before finalizing mixed-environment routes. Where a continuous route changes mode, define the engineering transition and operating rules explicitly.

## 3. HIM ↔ HCTA passenger transfers

The systems are separate authorities but must provide convenient passenger transfers.

**Required player journey:**

`Neighborhood HCTA station → HCTA local route → HIM interchange / central terminal → HIM intercity train → destination city`

The reverse journey must also work.

- A major HIM terminal in Hustle City is a recommended anchor and a key arrival location.
- HCTA must connect to the HIM terminal or designated interchange stations.
- Every designated outer neighborhood must have an HCTA station connection.
- Selected outer locations may host a direct HIM interchange where geography and route demand justify it.
- A direct HIM platform at every neighborhood is not a requirement unless the creator later approves that expansion.

This arrangement gives every neighborhood access to intercity travel without requiring every intercity train to stop at every neighborhood.

## 4. Station and neighborhood requirements

Every outer neighborhood box must reserve space for an HCTA station or a clearly defined HCTA station access point.

Station planning must include:
- safe pedestrian approaches and crossings;
- accessible boarding paths;
- passenger waiting and circulation space;
- connections to local streets and neighborhood destinations;
- clear signage and route information;
- lighting, weather protection, and safety systems;
- service access and emergency egress;
- room for future upgrades where practical.

District stations should support transfers, higher passenger volumes, and access to major venues and civic destinations. The central HIM terminal should support intercity passenger flows, luggage, arrivals/departures, ticketing or equivalent game interaction, and HCTA transfers.

## 5. Passenger experience

Train travel should feel like part of the living city rather than an invisible teleport by default.

Supported experience goals:
- choose a destination and route;
- approach and enter the station;
- board the correct train;
- sit or stand as appropriate;
- view the city through train windows;
- optionally switch between passenger, window, exterior, and overhead camera views;
- stop at stations and allow passengers to board/disembark;
- arrive and continue on foot or transfer to another service.

Fast-travel convenience may be offered as an option, but it must not erase the immersive train experience.

## 6. Supporting transportation layers

Rail is one part of a wider transportation plan. Coordinate rail with:
- elevated Skyway;
- ground-level expressway;
- local streets and arterial roads;
- buses and pedestrian routes;
- destination-based vehicle travel and rideshare;
- water taxis, boats, and marina access where geographically appropriate.

Road and rail corridors must be coordinated at the master-map stage to prevent accidental conflicts. Rail crossings, bridges, tunnels, station approaches, and highway interchanges require explicit spatial reservations.

## 7. World simulation and gameplay integration

The transit system should eventually support:
- scheduled and/or frequency-based services;
- NPC passengers and station activity;
- train arrivals, departures, dwell time, and platform occupancy;
- route choice and transfers;
- service status and disruption handling;
- player and NPC boarding/alighting states;
- authoritative trip state for multiplayer;
- safe recovery if a character becomes stuck or a service is interrupted.

Do not invent travel times, service frequency, fares, or exact station coordinates before route geometry and gameplay requirements are approved.

Basic transport must remain accessible and must not consume premium Diamonds. Any fare or economy design must follow the project's economy rules.

## 8. Data and integration requirements

The eventual engine-neutral data model should be able to represent:
- transport authority;
- network;
- route / line and public-facing route color;
- service mode and permitted operating environments;
- track segments and their geometry/elevation class;
- station and platform;
- station-to-district/neighborhood relationships;
- transfer connections between networks;
- stop sequence and service pattern;
- vehicle family and compatibility constraints;
- trip, passenger journey, and service status.

The Unreal Engine 5 implementation is primary. Shared route, station, and authority definitions should remain engine-neutral so Unity 6 can consume the same canonical data through its adapter.

## 9. Open decisions — do not silently finalize

- Exact HIM central terminal location and architectural design.
- Whether there are additional HIM terminals beyond the primary terminal.
- Which outer neighborhoods, if any, receive direct HIM service.
- Number of HCTA lines.
- Final route names, colors, and line maps.
- Which lines use elevated, underground, street-level, or mixed operation.
- Vehicle family and infrastructure standard for each route.
- Station locations, spacing, schedules, capacity, and fares.
- Whether local transit includes additional dedicated commuter/light-rail services beyond HCTA.

## 10. Acceptance checklist

- [ ] HIM is documented as intercity/regional.
- [ ] HCTA is documented as local city/neighborhood transit.
- [ ] Elevated, underground, and street-level rail are supported HCTA environments.
- [ ] Mixed-environment routes require explicit compatibility design.
- [ ] Every outer neighborhood has HCTA access.
- [ ] Every neighborhood can reach HIM through a transfer.
- [ ] The Frank Maserati opening arrival is assigned to HIM.
- [ ] Route count, line names, colors, stations, and schedules remain open until approved.
- [ ] Rail, road, pedestrian, and waterfront corridors are coordinated in the master map.



## 11. Visual fidelity and real-world infrastructure standard

**Creator requirement:** All HIM and HCTA trains, stations, platforms, tunnels, elevated structures, rail yards, entrances, concourses, signage, and surrounding environments must meet a premium, realistic, high-quality 3D standard. They must read as believable modern urban infrastructure, not generic low-detail game props.

### 11.1 Reference and design method
- Use carefully selected real-world railway and urban-architecture references to study engineering logic, proportions, passenger circulation, construction methods, materials, signage systems, lighting, accessibility, and maintenance infrastructure.
- References inform realism; Hustle City must retain original station names, architecture, logos, route identity, and fictional geography. Do not copy protected branding or reproduce a real station one-for-one.
- Create a distinct architectural identity for major terminals, district stations, neighborhood stations, elevated stops, subway stations, and surface platforms while maintaining a coherent HCTA/HIM design language.
- No train or station concept image is approved as a final asset merely because it appeared in a planning conversation.

### 11.2 Modeling and material requirements
- Believable full-scale proportions, track gauge consistency, platform-to-vehicle clearances, door positions, bogies/wheel assemblies, couplers where visible, undercarriage, roof equipment, windows, lighting, safety markings, and operational details.
- Physically based materials with convincing response: brushed and painted metals, stainless steel, glass, concrete, stone, brick, asphalt, ceramic tile, rubber, weather seals, plastics, acoustic panels, tactile paving, and weathered surfaces.
- High-quality geometry and silhouettes at expected gameplay viewing distances. Use detailed hero assets for close inspection and optimized LODs/impostors only at appropriate distances; optimization must not make close-up assets visibly crude.
- High-resolution texture work with consistent texel density, clean UVs, normal/roughness/metallic/ambient-occlusion intent, and appropriate decals. Use 4K-class source textures for hero assets where justified, with efficient lower-resolution variants for secondary assets; do not make 8K real-time textures a blanket requirement.
- Realistic glass, interior visibility, reflections, emissive lighting, grime, rain streaks, puddles, track wear, wheel/rail contact detail, and environmental aging where appropriate.
- No stretched textures, blurry signage, visibly pixelated close-up surfaces, floating rails, unsupported track geometry, repeated obvious tiling, or toy-like vehicle proportions.

### 11.3 Station architecture and public realm
- Major HIM terminal: architecturally significant city landmark with a convincing exterior, large-scale concourse, train hall/platform arrangement, passenger circulation, ticketing or game-equivalent service areas, luggage/arrival logic, accessible routes, clear wayfinding, retail/amenities where appropriate, and direct HCTA interchange.
- HCTA district stations: designed for urban passenger throughput, with coherent entrances, platform canopies or enclosed structures as appropriate, fare/access-control concept if used, signage, lighting, vertical circulation, emergency exits, and street integration.
- Underground stations: believable tunnel bores/cut-and-cover spaces, structural columns, waterproofing/drainage cues, ventilation, emergency egress, lighting, platform edge safety, tactile warning surfaces, service rooms, and coherent transitions to surface entrances.
- Elevated stations: credible piers, beams, spans, vibration/noise mitigation where appropriate, drainage, maintenance access, structural supports, stair/elevator connections, and believable integration with streets and adjacent buildings.
- Street-level stations: clear right-of-way, safe crossings, platform edges, signals, traffic coordination, pedestrian access, curb and sidewalk integration, and realistic separation from road traffic where required.
- Neighborhood stations must feel like designed civic infrastructure, not a small generic shelter pasted beside a track. Their scale may vary, but materials, access, signage, safety, and architectural finish remain intentional.

### 11.4 Lighting, atmosphere, and environmental integration
- Day/night lighting must be physically plausible and legible; interior and exterior lighting should work together without flat, overbright, or uniformly glowing surfaces.
- Stations and trains must respond convincingly to rain, wet surfaces, humid haze, sun angle, cloud cover, nighttime city light, and seasonal environment profiles.
- Ambient context should include believable street frontage, adjacent buildings, sidewalks, roads, bridges, retaining walls, utilities, landscaping, drainage, service access, and pedestrian activity.
- Audio design should eventually support rail rumble, wheel squeal where appropriate, brakes, door chimes, ventilation, announcements, crowd ambience, traffic, and environment-specific reverberation.

### 11.5 Quality gates — visual and functional
A rail asset or station is not accepted as production-ready until it passes:
1. **Reference review:** documented real-world reference study and original Hustle City design approval.
2. **Scale review:** measured dimensions, platform heights, vehicle clearances, track geometry, stairs, doors, and accessibility paths are coherent.
3. **Material review:** PBR response, texture resolution, UV quality, signage sharpness, weathering, and close-up inspection pass.
4. **Lighting review:** day, night, interior, exterior, and wet-weather conditions remain credible.
5. **Context review:** asset integrates into a complete urban environment and does not float, clip, or terminate implausibly.
6. **Performance review:** LODs, instancing, streaming, collision, draw calls, and texture budgets are appropriate for the target hardware and viewing distance.
7. **Gameplay review:** boarding, alighting, passenger circulation, route access, emergency egress, and safety systems function as designed.
8. **Creator approval:** visual reference or rendered review is explicitly approved before an asset is called final.

**Rejection criteria:** cartoon/toy styling, generic placeholder stations presented as finished work, low-poly close-up geometry, blurry or stretched textures, inaccurate train proportions, implausible structural supports, incomplete platforms, nonsensical passenger paths, or unconvincing integration with the surrounding city.
