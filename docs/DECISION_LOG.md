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
 
- **City identity system:** The initial expansion plan targets 30 cities. Each city may have distinct local business/venue names and its own character cast and five-card role/title ladder. The underlying five-card low-to-high progression remains recognizable while local names, characters, ages, genders, personalities, biographies and artwork vary by city.
- **Automotive parent group:** **Hustle Boys Automotive Group** is the creator-approved name. Individual dealerships may have different local names in each city.
- **Strict city-based card collection:** A player may earn/acquire a new card only while physically present in the in-game city assigned to that card. Activities, poker, packs, daily rewards, wheels, events and other acquisition sources are city-scoped. Eligible player-to-player card trading is permitted anywhere and is the explicit exception. City presence is server-validated.
- **City Keys:** Each city has its own major City Key milestone, earned by completing that city's configured card/collection requirements. Keys are intended to carry significant bonuses/surprises and unlock configured city-specific business opportunities. Exact thresholds, reward bundles and unlock maps remain to be authored.\n- **Universal social-sharing and growth system:** Creator-approved direction is that any meaningful gameplay activity/accomplishment—not only City Keys or major milestones—should be designed for optional social sharing and player acquisition. The shared architecture includes generated personalized share artifacts, supported share-sheet/platform destinations, unique share-event IDs, screenshot/photo proof submission where required, evidence-based verification with honest limits, anti-fraud controls, idempotent share rewards, referral attribution and milestone-qualified referral rewards. Exact reward amounts, currencies, caps, referral milestones, platform integrations and retention policies remain unresolved and require approval.

## Working direction
- City-to-city travel is a core repeatable progression loop: players visit each city to collect its local cards, complete its collections and pursue its City Key. Card trading remains available anywhere.
- Fictional city draws from Chicago and Miami/Florida but has original geography, names, architecture, landmarks and district identities.
- Develop/test locally and host live multiplayer in the cloud.
- Build reusable world-building foundations and expand through validated layers.
- Use Unreal Engine 5 for primary implementation; keep Unity 6 compatibility contracts and adapters documented/testable without duplicating production effort.
- 8K is a cinematic capture/output ambition where hardware permits, not a minimum real-time gameplay resolution.

- Final 30-city roster, local dealership/venue names and city-to-business assignments remain open; brainstormed examples are not automatically canon.

## Unresolved
- Final city name and exact geography.
- Airport name: We Fly High International Airport vs We Fly Sky International Airport.
- Final district boundaries, exact district positions, and Fashion/Swagger District name.
- Exact outer neighborhood box count, arrangement, and block dimensions pending original-map review.
- HIM/HCTA terminal locations, route count, route names/colors, line alignments, station positions, and service patterns.
- Casino placement.
- Final list of five interactive neighborhood locations.
- Population milestones for neighborhood expansion.
- Backend/cloud/database/auth vendors and architecture details.
- AI model choices, laptop hardware, n8n version, credentials and workflow runtime.
- Real-world brand licensing and permitted use of map/transit/image data.
- Unspecified card-game rules and exact first-release scope.


## Creator clarification — story architecture and administration (2026-11-28)

### Approved narrative structure
- Hustle City has two connected but separate narrative channels: (1) playable business/district missions and (2) ambient underworld discovery through NPCs and the living city.
- Completing missions does not reveal who stole the Ghost Freight and does not automatically explain the Inner Circle or Ghost Network. Missions resolve operational problems, business choices, district fund use, asset recovery/loss, business/district finances, relationships and standing.
- The hidden story is discovered through overheard conversations, NPC phone calls, rumors, people approaching the player, repeat encounters, private meetings, invitations, public news and accumulated evidence.
- NPCs have limited knowledge. Rumor, evidence, misinformation, player theories and canonical truth must remain distinct. No single NPC explains the entire conspiracy.
- The Inner Circle is global. The Ghost Network is its equally powerful global opponent. The Ghost Freight is the stolen shipment/opening incident. The Twelve are Hustle City's twelve district leaders, not a global organization. The Ghost Network has its own city and twelve district leaders.
- The player eventually learns that the Twelve have been working for Frank Maserati. This is an intermediate revelation. The player discovers the global organizations late and may eventually choose either. Ultimate Ghost Network controllers remain unknown through the main storyline.
- The twelve districts are Entertainment, Downtown, Hustle, Trappa, Transportation, Swagger, Diamond, Medical, After Hours, Financial, Industrial and Police. Police District is District 12, not an extra district.
- **Trappa District** is the approved spelling; older “Trapper District” wording is superseded and must be corrected in dependent documents when edited.
- The six-card character story chain (discover, investigate, choose, execute, business outcome, district outcome) is separate from five-card building/venue collections.
- Character names, ages, nicknames, alignments, supporting cast, ordinary dialogue and ordinary mission details are delegated to the creative team; they do not require individual creator approval.
- Creator approval remains required for major organization names, district names, building names/major landmarks and changes to overall strategy or central product direction.

### Administration dashboard direction
The repository must include a first-class Administration Dashboard covering global players online, player directory/detail, sessions, reward grants and economy ledger, mission/story progression, city/district/business operations, live events, NPC/world operations, support/moderation, analytics, admin roles/permissions and audit logs. Player currencies (Hustle Money, Poker Chips, Wings, Diamonds) remain distinct from district mission funds and business accounts. The dashboard specification is a product baseline, not evidence of implementation or live data connectivity.

See docs/story/ and docs/admin/ for the working specifications.
