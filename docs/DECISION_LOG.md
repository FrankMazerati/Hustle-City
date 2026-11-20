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
- Chicago-style elevated rail and underground subway are important.
- NPCs must answer from authoritative game state, not hallucinate events.
- No player death; implement safe prevention/detection/recovery.
- Master grid 7x7; six central boxes and 43 potential outer neighborhood boxes; each outer box planned as 5x5 blocks.
- Persistent Player Shell is separate from individual world environments.
- Basic transport must not consume premium Diamonds.
- Neighborhood ownership/founding, crew leadership, property/business ownership and residency are separate concepts.
- Neighborhoods can be visually complete/ambient while only a small number of locations are fully interactive at launch.
- Existing SAM-led 10-person named Hustle City cohort and 48-role specialist catalog remain the canonical agent system; engine-specific role mappings must reflect Unreal primary / Unity secondary.
 
## Working direction
- Fictional city draws from Chicago and Miami/Florida but has original geography, names, architecture, landmarks and district identities.
- Develop/test locally and host live multiplayer in the cloud.
- Build reusable world-building foundations and expand through validated layers.
- Use Unreal Engine 5 for primary implementation; keep Unity 6 compatibility contracts and adapters documented/testable without duplicating production effort.
- 8K is a cinematic capture/output ambition where hardware permits, not a minimum real-time gameplay resolution.

## Unresolved
- Final city name and exact geography.
- Airport name: We Fly High International Airport vs We Fly Sky International Airport.
- Final district boundaries and Fashion/Swagger District name.
- Casino placement.
- Final list of five interactive neighborhood locations.
- Population milestones for neighborhood expansion.
- Backend/cloud/database/auth vendors and architecture details.
- AI model choices, laptop hardware, n8n version, credentials and workflow runtime.
- Real-world brand licensing and permitted use of map/transit/image data.
- Unspecified card-game rules and exact first-release scope.
