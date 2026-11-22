# Decision Log

Status labels: **Approved** = explicit creator direction. **Working direction** = strong preference with technical details open. **Proposed** = candidate. **Unresolved** = do not finalize without creator approval.

## Approved / established
- Project: Hustle City, an original cinematic realistic 3D social-world/open-world city-life game.
- **Engine decision:** Unreal Engine 5 is the primary production engine; Unity 6 is the secondary compatibility/migration target. Godot is retired as an active engine target. Preserve existing Godot history/assets unless disposition is reviewed; do not destructively delete history.
- The flagship environment combines selected Chicago-inspired urban character with Florida-inspired tropical/coastal atmosphere while remaining a fictional, original Hustle City setting—not a literal recreation of Chicago or Miami.
- The world-building foundation must support additional distinct scenery and regional environment archetypes, not only the Chicago/Florida blend.
- Core scenery includes dense downtown, varied neighborhoods, skyline, lakefront, river/canal elements, palms in warm areas, tropical planting, beaches, marinas, waterways, lagoons, islands, causeways, parks and climate-aware vegetation/weather.
- Environmental palette includes electric blue, white, sunset pink, purple transitions and colorful sunrise/sunset gradients; black and gold are selective luxury/brand accents. Mazerati Boys spelling uses Z and black/gold identity.
- Car-focused crew convoy visual direction; wet reflective streets where weather and scene conditions support them.
- Automated destination-based vehicle travel is preferred over manual driving. Players can travel as driver/passenger and travel together in crew convoys.
- City should feel alive with NPCs, traffic, transit and persistent automated events.
- Local rail is operated by the **Hustle City Transit Authority (HCTA)** and connects downtown, all six central districts, surrounding neighborhoods, and outer areas.
- HCTA is intended to support elevated rail, underground rail, and street-level rail. Individual route count, names, colors, and operating environments remain to be finalized.
- The **Hustle International Metro (HIM)** is a separate intercity/regional passenger railway connecting Hustle City with other cities and regions, with Chicago, Atlanta, New York, and Florida destinations given as examples.
- Every designated outer neighborhood must have HCTA station access. Neighborhoods must be able to reach HIM through a transfer; direct HIM service at every neighborhood is not assumed.
- The opening passenger-train arrival of Frank Maserati and his female companion belongs to HIM.
- NPCs must answer from authoritative game state, not hallucinate events.
- No player death; implement safe prevention/detection/recovery.
- Six central district boxes are established, with all surrounding boxes reserved for neighborhoods. An earlier repository plan records a 7x7 / 43-outer-box / 5x5-block capacity model; exact count, dimensions, and block subdivision require reconciliation with the creator's original map references before being treated as final.
- Persistent Player Shell is separate from individual world environments.
- Basic transport must not consume premium Diamonds.
- Neighborhood ownership/founding, crew leadership, property/business ownership and residency are separate concepts.
- Neighborhoods can be visually complete/ambient while only a small number of locations are fully interactive at launch.
- Existing SAM-led 10-person named Hustle City cohort and 48-role specialist catalog remain the canonical agent system; engine-specific role mappings must reflect Unreal primary / Unity secondary.
- **District separation correction (creator-confirmed):** The Fashion District / Swagger District and Diamond District are separate central districts. They must not be conflated.
- **Hustle Towers location (creator-confirmed):** Hustle Towers is in the **Diamond District**, not the Fashion / Swagger District.
- **Hustle Towers design (creator-confirmed):** 100 floors, vertical-first, rising straight up rather than sprawling horizontally.
- The Hustle Towers / Diamond District development brief includes malls, multiple casino areas, multiple food concierge lounges, multiple welcoming help desks, the Heavenly Hallway, and “kicking areas” (exact meaning unconfirmed).
- “Caesar's Palace” is a creator-specified name in the Hustle Towers context; its exact architectural relationship to the tower remains unresolved.
- A mobile browser-compatible development preview is a required companion review target alongside UE5 production. Browser preview is not a replacement for UE5.

## Working direction
- Fictional city draws from Chicago and Miami/Florida but has original geography, names, architecture, landmarks and district identities.
- Develop/test locally and host live multiplayer in the cloud.
- Build reusable world-building foundations and expand through validated layers.
- Use Unreal Engine 5 for primary implementation; keep Unity 6 compatibility contracts and adapters documented/testable without duplicating production effort.
- 8K is a cinematic capture/output ambition where hardware permits, not a minimum real-time gameplay resolution.
- The browser preview currently uses a lightweight Babylon.js geometry blockout for early spatial review. It is not final art or a compiled game.

## Unresolved
- Final city name and exact geography.
- Airport name: We Fly High International Airport vs We Fly Sky International Airport.
- Final boundaries, exact positions, and Fashion / Swagger District's distinct identity.
- Exact Diamond District boundary and location within the original master map.
- Exact outer neighborhood box count, arrangement, and block dimensions pending original-map review.
- HIM/HCTA terminal locations, route count, route names/colors, line alignments, station positions, and service patterns.
- Meaning and gameplay purpose of “kicking areas”.
- Exact floor-by-floor assignment and counts for mall areas, casino areas, food concierge lounges, and welcoming help desks.
- Heavenly Hallway's visual identity, exact location, and gameplay function.
- Whether Caesar's Palace is inside Hustle Towers, attached to it, or a separate Diamond District destination.
- Fashion / Swagger District's visual identity, venues, and gameplay purpose.
- Final list of five interactive neighborhood locations.
- Population milestones for neighborhood expansion.
- Backend/cloud/database/auth vendors and architecture details.
- AI model choices, laptop hardware, n8n version, credentials and workflow runtime.
- Real-world brand licensing and permitted use of map/transit/image data.
- Unspecified card-game rules and exact first-release scope.
