# Opening Sequence — 17-Agent Assignment Matrix

**Status:** Prepared work allocation for the opening vertical slice. This is a task plan, not proof that any local worker has been activated or has completed work.

## Command and creative direction

| Local agent | Assignment | Output |
|---|---|---|
| SCRIBE | Opening story beats, Bella Rose dialogue, scene continuity, short/full tour branching | Narrative beat sheet, dialogue draft, tour state outline |
| LENS | Train-window opening, train exterior/aerial approach, skyline reveal, station walk, Towers and tour camera language | Sequencer shot list, camera movement plan, transition and timing sheet |

SCRIBE and LENS are local creative leads. Their deliverables require independent review; neither approves its own work.

## Production specialists and QA ownership

| Specialist | QA owner | Opening-sequence responsibility |
|---|---|---|
| P01-GEOGRAPHY — World Geography & Environment Foundation | QA-1 | Rainy rail corridor, city approach geography, skyline sightlines, weather/environment profile |
| P02-CITY-PLAN — City Masterplanning & District Layout | QA-1 | Station-to-city placement, skyline composition, route from station to Hustle Towers |
| P03-DISTRICTS — District & Neighborhood Design | QA-1 | Arrival district identity, Hustle District context and contrast with Trapper District |
| P04-ARCHITECTURE — Architecture & Building Systems | QA-1 | Station exterior, Hustle Towers exterior, building scale, entrances and courtyard envelope |
| P05-INTERIORS — Interiors, Venues & Environment Dressing | QA-2 | Concierge hall, Towers lobby, courtyard dressing, Bella's room and player room |
| P06-TRANSIT — Rail, Transit & Transportation Infrastructure | QA-2 | Passenger train, track, platform, train stop, disembarking and station passenger flow |
| P07-VEHICLES — Vehicles, Traffic & Simulation | QA-2 | Station access traffic, vehicle/roadside ambience and future transport-system compatibility |
| P08-CHARACTERS — Player Characters, Character Art & Animation | QA-2 | Bella Rose character presentation, rig/animation requirements, player arrival group |
| P09-NPC-NAV — NPC Intelligence, Navigation & Crowd Behavior | QA-3 | Crowd movement, Bella's guided route, passenger navigation and escort behavior |
| P10-GAMEPLAY — Gameplay Interaction & Venue Systems | QA-3 | Room booking, dialogue interactions, tour controls, doors and amenity interactions |
| P11-ONBOARDING — Onboarding, Story Progression & Player Journey | QA-3 | Short/full tour, mandatory Towers stop, skip/revisit, persistence, start-location and control-lock rules |
| P12-UNREAL-INTEGRATION — Unreal Integration, Asset Pipeline & Performance | QA-3 | UE project structure, asset intake, Sequencer/Blueprint integration, test map, performance and packaging |

## QA responsibilities

- QA-1 independently reviews P01–P04.
- QA-2 independently reviews P05–P08.
- QA-3 independently reviews P09–P12.
- Creative-lead deliverables from SCRIBE and LENS require independent review, coordinated by ChatGPT; neither lead may self-approve.
- QA checks actual artifacts, requirements, source/license metadata, tests and evidence. No approval based only on a completion claim.

## First production package order

1. **Opening world/arrival foundation:** P01 + P02 define the rail approach, skyline, station location and arrival route. P01/P02 outputs pass QA-1.
2. **Rail arrival:** P06 defines train, tracks, platform, stopping and disembark flow. QA-2 reviews.
3. **Station and Towers shell:** P04 creates exterior/building requirements; P05 creates interior/courtyard requirements. Each receives its assigned QA review.
4. **Bella and guided movement:** P08 specifies character/animation needs; P09 defines crowd and guided path behavior.
5. **Narrative/camera integration:** SCRIBE and LENS deliver story/dialogue and shot plans; integrate with environment and character outputs.
6. **Booking and tour logic:** P10 and P11 define room booking, tour state, persistent visit flags, no-control gating and return-home behavior.
7. **Unreal assembly:** P12 integrates approved assets and systems into a test map and produces a viewable prototype candidate.
8. **Final independent checks:** QA-1/2/3 review their assigned work; integration and cross-discipline checks are coordinated by ChatGPT. Creator approval is required for canon or major visual-direction changes.

## Work cadence

Use the approved 20-minute production, 5-minute QA, 5-minute correction cycle, with an optional 10-minute extension alternating correction and re-review. This cadence is a planning standard, not a reason to submit incomplete work. Initial local concurrency remains one model worker at a time until hardware capacity is verified.

## Activation gate

Do not start the scheduler until:
- exact Ollama model tags are verified on the actual target device;
- model assignments exist for every activated local role;
- QA ownership is valid;
- target device RAM, storage and concurrency limits are measured;
- automated tests pass;
- the creator approves any still-open roster or canon decisions.
