# Hustle City — Downtown City Blockout Foundation
Version: 0.1
Status: Working blockout proposal built from approved canon; creator approval required for unresolved geography and boundaries.
Owner: Trinity (coordination draft)
Primary engine: Unreal Engine 5
Secondary compatibility target: Unity 6

## 1. Purpose
Establish the first coherent, buildable piece of Hustle City while model downloads and the agent runtime are unavailable. This is a spatial foundation and production brief, not a claim that a 3D engine level has already been built.

The first build is the central intercity station and the surrounding downtown/Diamond District experience. It must support the opening arrival sequence and provide a convincing, living-city first impression. Keep the layout modular so the rest of the city can expand without rebuilding the first area.

## 2. Canon to preserve
- Hustle City is an original fictional American city, not a literal recreation of Chicago, Miami, or any other real place.
- Its flagship identity blends selected Chicago-inspired urban character with Florida-inspired tropical/coastal atmosphere.
- Unreal Engine 5 is the primary production engine; Unity 6 is the secondary compatibility target. Godot is retired as an active target.
- The long-term master planning framework is 7x7 (49 large planning boxes): six central district concepts and 43 potential outer neighborhood boxes. Each outer box may be planned as 5x5 blocks. This is long-term capacity, not a launch build requirement.
- The six central district concepts are Diamond, Entertainment, Marina, Fashion/Swagger (working label), Financial, and Downtown. Exact boundaries and some assignments remain unresolved.
- The central intercity passenger station is the opening arrival point. Future local rail, elevated rail/L-train character, underground subway and other transit should connect into a coherent network.
- The city should feel active through pedestrians, NPC routines, traffic, transit, venue activity and ambient sound.
- Water is a connected geography system. Do not place a shoreline, river, island, marina or canal until its relationship to the overall geography is coherent.
- Distinguish playable, enterable, ambient, restricted and decorative spaces.

## 3. First build target: Station-to-Diamond arrival district

### Required spatial sequence
1. **Intercity approach:** A passenger train approaches the central station through a believable rail corridor. The train and platform relationship must support passenger arrival and luggage.
2. **Central station:** A substantial, recognizable civic/transport building with platforms, passenger circulation, concourse, station shops and clear exits. The station is the player's first physical connection to the city.
3. **Station forecourt:** A public arrival space immediately outside the station with pedestrian paths, pickup/drop-off access, visible city traffic and a readable view toward downtown.
4. **First skyline reveal:** From the station exit/forecourt, frame the downtown skyline and the Diamond District landmarks. Hustle Towers should be a prominent visual anchor; avoid locking exact height or distance until scale studies are approved.
5. **Diamond District:** A walkable upscale urban district near Hustle Towers, including Diamond Row/luxury jewelry and premium storefronts, restaurants with outdoor dining, active sidewalks and The Shuffle Club (also referred to as Hudson City Shuffle Club in earlier planning; confirm canonical venue naming before asset production).
6. **Public gathering space:** A plaza or pedestrian-friendly street space that links the station approach to Diamond District destinations. Its final name and precise geometry remain open.
7. **Future connections:** Reserve logical connection opportunities for the other central districts, local rail/metro, road arterials and a future waterfront/marina route, without prematurely fixing their exact direction or boundary.

### Opening-sequence support
The blockout must stage the established cinematic arrival:
- Production credits and title sequence play over a moving intercity passenger train.
- The conductor announcement is: “Next stop, Downtown Hustle City.”
- Frank Maserati and his female companion arrive with luggage, leave the train and move through station platforms, shops and concourse.
- They exit into the city and receive the skyline/Diamond District reveal, with Hustle Towers readable in the composition.
- The music lowers as they leave the station; real station, street and pedestrian ambience becomes prominent.
- Player control begins naturally in the arrival area, without an intrusive tutorial/menu interrupting the cinematic handoff.
- Bella Rose is a local character who enters the story later and invites them to Hustle Towers. Do not place her into the opening as an unexplained greeter.

## 4. Conceptual adjacency map (not a surveyed or compass-locked layout)

```text
                FUTURE DOWNTOWN CONNECTIONS
                           |
              +-------------------------+
              |  DIAMOND DISTRICT       |
              |  Hustle Towers          |
              |  Diamond Row            |
              |  The Shuffle Club       |
              |  Restaurants / Dining  |
              +------------+------------+
                           |
                 Plaza / Pedestrian Link
                           |
              +------------+------------+
              | CENTRAL INTERCITY       |
              | STATION                 |
              | Platforms / Concourse   |
              | Shops / Main Exit       |
              +------------+------------+
                           |
                Forecourt / Arrival
                           |
              Rail corridor + city access
```

This diagram expresses adjacency and player flow only. It does not establish north, south, block dimensions, building heights, street widths, shoreline position, or district boundaries.

## 5. Blockout layers and production order

### Layer A — Spatial reference and scale study
- Define UE5 world units, origin, forward axis, grid/block dimensions, vertical convention and coordinate metadata through ATLAS before detailed asset production.
- Establish a human-scale reference using the player character, train carriage, platform, station doors, sidewalks and street crossings.
- Produce greybox primitives first; do not commit to final facade detail or decorative props.
- Record all dimensions as measured proposals until reviewed.

### Layer B — Rail and station envelope
- Reserve the intercity rail approach, track envelope, platforms, train stopping position, passenger circulation and accessible paths.
- Separate passenger paths from service/vehicle movements.
- Design station entrances/exits and concourse flow so the opening camera and player path remain unobstructed.
- Leave connection interfaces for future local rail and metro; do not invent their routes yet.

### Layer C — Street and pedestrian skeleton
- Create the station forecourt, primary pedestrian desire lines, street frontage, pickup/drop-off zone and initial road connections.
- Include sidewalks, safe crossings, curb geometry, lighting and street furniture placeholders.
- Keep pedestrian routes continuous and accessible. Prevent rail/road conflicts and unsafe platform access.

### Layer D — Landmark massing
- Establish greybox silhouettes for the station, Hustle Towers, Diamond Row storefronts, restaurant frontage and The Shuffle Club.
- Validate the skyline reveal from the station exit and the walking sequence toward the district.
- Use varied building heights and original architectural language. Do not copy a real skyline or protected landmark.

### Layer E — Public realm and city life
- Add plaza/street seating, planters, palms only where the warm-climate landscape profile supports them, shade, signage placeholders and outdoor dining zones.
- Populate with a small test crowd and NPC route loops only after walkable paths and collision are stable.
- Add ambient traffic and transit only when route logic and safe stopping states exist.

### Layer F — Visual identity pass
- Apply the established electric blue, white, sunset pink and purple transition palette with restrained black/gold luxury accents.
- Support bright coastal daylight, warm sunset and night variants. Wet reflective streets are weather-dependent, not permanently applied.
- Use original Hustle City signage, architecture and landmarks. Track asset provenance and licensing.

## 6. First playable blockout acceptance criteria
The first city blockout is ready for review when:
1. A player can travel from the arriving train/platform through the station concourse to the main exit without path obstruction.
2. The exit delivers a deliberate, readable view of the downtown skyline and Hustle Towers.
3. The player can walk from the station forecourt to the Diamond District through continuous, collision-safe pedestrian routes.
4. The station, Hustle Towers, Diamond Row, restaurant frontage and The Shuffle Club are distinct, readable greybox landmarks.
5. Rail, vehicle and pedestrian movement zones are separated and have safe stopping/crossing logic.
6. The scene can host ambient pedestrians and traffic without blocking the arrival path.
7. All spatial dimensions and coordinate conventions use the approved shared contract.
8. Every element is tagged as playable, enterable, ambient, restricted or decorative.
9. The layout does not imply unapproved district boundaries, shoreline placement, city compass orientation or final city scale.
10. The UE5 project/level is opened and tested in-engine before anyone claims a playable build exists.

## 7. Explicitly unresolved — do not silently decide
- Exact city geography, shoreline, river/canal placement and compass orientation.
- Exact station location within the six central planning boxes and its final architectural style.
- Master-grid box dimensions, block dimensions, street widths, rail elevations and all final scale values.
- Exact district boundaries and the formal placement of the six central district concepts.
- Whether “The Shuffle Club” and “Hudson City Shuffle Club” are one canonical venue name or separate naming variants.
- Exact Hustle Towers height, footprint, facade design and relationship to the station.
- Final name of the public plaza and final station name.
- Detailed local rail/metro routes and station locations.
- Final venue count and which spaces are enterable in the first playable release.

## 8. Handoffs
- **ATLAS:** approve coordinate/scale contract and spatial interfaces before detailed modeling.
- **URBAN:** own the geography, station-to-district blockout, district identity and city massing.
- **MOTION:** review intercity rail envelope, future transit interfaces, forecourt traffic and safe pedestrian/vehicle separation.
- **ARCHITECTURE / INTERIOR:** develop station and venue building modules after spatial envelopes are stable.
- **PULSE:** define initial pedestrian/NPC circulation and ambient activity after walkable routes are validated.
- **VECTOR:** implement the UE5 greybox level and player traversal after the spatial contract is approved.
- **SENTINEL / assigned QA supervisor:** independently review scale, navigation, collision, accessibility, visual readability, performance risks and opening-sequence continuity.
- **Creator:** approve unresolved geography, district boundaries, landmark scale and final visual direction.

## 9. Immediate next deliverable
Create a UE5 greybox scene for the station → forecourt → skyline reveal → Diamond District walking route. Use placeholder geometry only. The scene is a spatial testbed, not a final art pass. Do not begin detailed city-wide building production until the creator approves the first blockout and ATLAS validates the shared spatial contract.

## References
- `docs/PROJECT_VISION.md`
- `docs/DECISION_LOG.md`
- `world/WORLD_IDENTITY_BIBLE.md`
- `architecture/INTEGRATION_CONTRACTS.md`
- `architecture/PORTABILITY_CONTRACT.md`
- `agents/COMMUNICATION_PROTOCOL.md`

## Creator-approved district identity update — 2026-11-22

This section supersedes earlier tentative references to a Financial District, Marina District, and Fashion District. The earlier six-district list was a planning sketch, not a finalized canon.

### Current central district identities

1. **Downtown District** — the city's major destination and commercial core. It contains casinos, hotels, luxury dining, movie theaters, financial institutions, and major commercial buildings. There is no separate Financial District in the current plan.
2. **Diamond District** — the luxury and prestige district, including jewelry, high-end retail, upscale shopping, and established Diamond District destinations. Its exact venue mix and boundary with Downtown remain to be planned.
3. **Travel District** — replaces the former Marina District. It brings together the marina, yacht club, car club, airport, and intercity train station, with major transportation connections nearby. The Travel District should be directly adjacent to the Diamond District.
4. **Swagger District** — replaces the former Fashion District. Its identity includes fashion, clothing, sneaker culture, barber shops, beauty, personal style, and streetwear.
5. **Entertainment District** — nightlife, music, clubs, live performances, and entertainment venues.
6. **Hustle District** — a distinct, working commercial district focused on real-world money-making: independent businesses, street vendors, small shops, markets, entrepreneurs, and active street-level commerce. It should be close to Downtown, but remain its own district with a different economic character.

### Planning rules

- Do not create a separate Financial District unless the creator explicitly reintroduces one. Financial institutions belong in Downtown.
- Use **Travel District**, not Marina District; the marina is one of its anchors, not the whole district.
- Use **Swagger District**, not Fashion District.
- Keep the Diamond District and Travel District directly adjacent in the district plan.
- Keep the Hustle District close to Downtown, but do not collapse the two into one district: Downtown is the major destination/commercial core, while Hustle is everyday enterprise and street-level commerce.
- District boundaries, compass positions, exact grid cells, and the full 7×7 allocation remain unapproved. Do not assign geographic positions or water/shoreline geometry yet.
- The earlier opening-sequence plan remains valid as a proposed arrival experience, but the central train station's final district assignment must now be reconciled with the creator's Travel District definition. Treat the station as a Travel District anchor in the updated plan.

### District framework status

The six identities above are the current creator-directed central district framework. Any additional central planning boxes or districts are still open for creator discussion; do not invent three extra districts or assume the former six-box sketch defines the final count.
