# Decision Log

Status labels: **Approved** = explicit user direction. **Working direction** = strong preference with technical details open. **Proposed** = candidate. **Unresolved** = do not finalize without creator approval.

## Approved / established
- Project: Hustle City. Engine: Godot 4.
- Cinematic realistic 3D city; car-focused crew convoy visual direction.
- Mazerati Boys spelling uses Z; black-and-gold identity.
- Automated destination-based vehicle travel is preferred over manual driving.
- Players can travel as driver/passenger and travel together in crew convoys.
- City should feel alive with NPCs, traffic, transit and persistent automated events.
- Chicago-style elevated rail and underground subway are important.
- NPCs must answer from authoritative game state, not hallucinate events.
- No player death; implement safe prevention/detection/recovery.
- Master grid 7x7; six central boxes and 43 potential outer neighborhood boxes; each outer box planned as 5x5 blocks.
- Persistent Player Shell is separate from individual world environments.
- Basic transport must not consume premium Diamonds.
- Neighborhood ownership/founding, crew leadership, property/business ownership and residency are separate concepts.
- Neighborhoods can be visually complete/ambient while only a small number of locations are fully interactive at launch.
- Existing SAM concept supervised World & City Architect, Character & Style Architect, Gameplay & World Simulation Architect, and Poker & Table Games Architect. Expand this structure, do not discard it.

## Working direction
- Fictional city draws from Chicago and Miami/Florida.
- Develop/test locally and host live multiplayer in the cloud.
- Build the AI studio, agent coordination and shared documentation before scaling game production.
- Start with a small playable vertical slice, then expand.

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
