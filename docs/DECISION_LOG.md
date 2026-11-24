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


## Hustle City memberships and currency economy
- **Approved:** Eight membership tiers and USD price points: Hustle City Starter ($9.99), Hustle City Connect ($19.99), Hustle City Boss ($29.99), Hustle City Mogul ($39.99), Hustle City Elite ($49.99), Hustle City Royalty ($59.99), Hustle City Legend ($79.99), Hustle City Empire ($99.99). There is no $69.99 tier.
- **Approved:** Membership packages contain only Hustle Money, Diamonds, Poker Chips and Wings. No membership includes cards, card packs or card drops.
- **Approved:** Cards are earned through a separate gameplay system; specific activities and award rules are unresolved. Daily login, poker participation and other activities are candidates only, not finalized card sources.
- **Approved design goal:** Balance membership value against gameplay earning and optional individual purchases. Do not over-grant currency or make paid membership necessary for core progression.
- **Unresolved:** Billing cadence, exact currency quantities and tier allocations, daily reward amounts/streak rules, card acquisition methods, store catalog/prices and Poker Chip monetization.
- Canonical specification: `docs/economy/MEMBERSHIPS_AND_REWARDS.md`.

## Live entertainment, sports and music
- **Approved direction:** Hustle City should support social entertainment as part of the living world, including venues where players can gather, socialize and enjoy events.
- **Approved direction:** Build fictional sports broadcasts and shared in-world watch parties first, using original Hustle City basketball/football content. Real-world NBA, NFL and other sports broadcasts are a later phase, after the game is built and has an active player base, and only after the required rights and distribution agreements are secured.
- **Approved direction:** Real-world music by real artists is intended from the outset; music is part of the world experience (for example, clubs, lounges, bars, vehicles and events), not only a separate menu player. Use only music with the appropriate rights cleared for the intended game uses.
- **Approved experience direction:** DJ sets/music events, nightclubs/lounges, sports bars with screens and watch parties, and potential concert/performance venues.
- **Unresolved:** Specific artists, tracks, labels/publishers, rights agreements, licensing budget, venue names/locations/counts, radio/playback design, event schedules, fictional team/league identities, match simulation/broadcast details and implementation scope.
- Rights for compositions and sound recordings, territories, platforms, term, interactive playback, marketing, player streams/clips and other uses must be reviewed and secured as applicable. Consumer music subscriptions are not game-use licenses.
- Canonical specification: `docs/gameplay/LIVE_ENTERTAINMENT_SPORTS_AND_MUSIC.md`.


## 30-city food and beverage catalog foundation
- **Approved direction:** Build distinct local food and beverage menus for 30 major U.S. starter city markets, while keeping everyday affordability and shared price tiers reasonably comparable across markets.
- **Creator-provided price anchors:** basic meal around $5.00; hamburger-and-fries example $5.99; pop/soda around $2–$3; inexpensive liquor serving/example around $5; bottles and premium liquor cost more according to size/tier. These are reference anchors, not a complete or final price list.
- **Approved currency rule:** Food and drinks are purchased with Hustle Money, not Poker Chips. Keep Hustle Money, Diamonds, Poker Chips and Wings as separate wallets.
- **Working 30-market roster selected under creator direction:** Chicago; Manhattan, Brooklyn, Queens, The Bronx and Staten Island; Houston, Dallas, Austin and San Antonio; Boston; Philadelphia; Washington, D.C.; Atlanta; New Orleans; Miami, Tampa and Orlando; Los Angeles, San Francisco, San Diego and Sacramento; Las Vegas; Phoenix; Denver; Seattle; Portland; Detroit; Nashville; Honolulu.
- **Menu identity examples:** Chicago-style pizza and local comfort food; New York borough-specific menus; Texas regional food; Florida/Caribbean/seafood influences; California regional and international food; and distinct local specialties across the remaining markets. Hustle City's own broad menu direction includes soul food bowls, jerk chicken, shrimp dinners, rib tip dinners and seafood.
- **Unresolved:** final roster confirmation/substitutions; full item-level menus; final prices, portions and bottle sizes; venue-specific menus; food/health/energy effects; clothing prices; and daily reward amounts. Do not finalize daily rewards before the food/beverage and other major spending catalogs are modeled.
- **Canonical catalog foundation:** `docs/economy/30_CITY_FOOD_BEVERAGE_CATALOG.md`. The selected roster and menu examples are a working foundation; individual items and prices remain subject to research and creator approval.
