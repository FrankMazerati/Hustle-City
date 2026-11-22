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
