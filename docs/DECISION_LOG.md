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
- Rights for compositions and sound recordings, territories, platforms, term, interactive playback, marketing, player streams/clips and other uses must be reviewed and secured as applicable. Consumer music subscriptions are not game-use licenses.
- **Unresolved:** Specific artists, tracks, labels/publishers, rights agreements, licensing budget, venue names/locations/counts, radio/playback design, event schedules, fictional team/league identities, match simulation/broadcast details and implementation scope.
- Canonical specification: `docs/gameplay/LIVE_ENTERTAINMENT_SPORTS_AND_MUSIC.md`.

## 30-city food and beverage catalog foundation
- **Approved direction:** Build distinct local food and beverage menus for 30 major U.S. starter city markets, while keeping everyday affordability and shared price tiers reasonably comparable across markets.
- **Creator-provided price anchors:** basic meal around $5.00; hamburger-and-fries example $5.99; pop/soda around $2–$3; inexpensive liquor serving/example around $5; bottles and premium liquor cost more according to size/tier. These are reference anchors, not a complete or final price list.
- **Approved currency rule:** Food and drinks are purchased with Hustle Money, not Poker Chips. Keep Hustle Money, Diamonds, Poker Chips and Wings as separate wallets.
- **Working 30-market roster selected under creator direction:** Chicago; Manhattan, Brooklyn, Queens, The Bronx and Staten Island; Houston, Dallas, Austin and San Antonio; Boston; Philadelphia; Washington, D.C.; Atlanta; New Orleans; Miami, Tampa and Orlando; Los Angeles, San Francisco, San Diego and Sacramento; Las Vegas; Phoenix; Denver; Seattle; Portland; Detroit; Nashville; Honolulu.
- **Menu identity examples:** Chicago-style pizza and local comfort food; New York borough-specific menus; Texas regional food; Florida/Caribbean/seafood influences; California regional and international food; and distinct local specialties across the remaining markets. Hustle City's own broad menu direction includes soul food bowls, jerk chicken, shrimp dinners, rib tip dinners and seafood.
- **Unresolved:** final roster confirmation/substitutions; full item-level menus; final prices, portions and bottle sizes; venue-specific menus; food/health/energy effects; clothing prices; and daily reward amounts. Do not finalize daily rewards before the food/beverage and other major spending catalogs are modeled.
- **Canonical catalog foundation:** `docs/economy/30_CITY_FOOD_BEVERAGE_CATALOG.md`. The selected roster and menu examples are a working foundation; individual items and prices remain subject to research and creator approval.

## Initial item-level food and beverage menus
- **Working proposal, not yet creator-approved:** `docs/economy/ANCHOR_ITEM_LEVEL_MENUS_DRAFT.md` defines draft item-level menus for the flagship fictional Hustle City market and Chicago, including item IDs, serving descriptions and proposed Hustle Money prices.
- The draft preserves creator-provided anchors: basic meal around $5.00; hamburger and fries $5.99; pop/soda around $2–$3; inexpensive liquor serving around $5.00. All other draft prices require creator review.
- **Unresolved:** final item selection, names, prices, portion sizes, venue availability, food/health/energy effects and alcohol details. The draft does not authorize implementation or final daily-reward amounts.

## Social world, lifestyle, hospitality and conversational NPC requirements
- **Approved creator direction:** Hustle City is a 3D social-life world first; poker is one activity inside the larger persistent world, not the product's defining purpose.
- **Approved creator direction:** Expand character creation and identity with diverse body builds, facial hair, hairstyles, clothing, shoes, accessories and distinct men's/women's fashion catalogs. Creator-provided outfit images will guide visual direction when supplied.
- **Approved creator direction:** Players manage individual clothing items and saved outfits through physical wardrobes/closets at apartments, houses and designated locations including Hustle Towers; clothing choices should account for weather and seasons.
- **Approved creator direction:** Players can pack owned clothing into travel bags/suitcases for trips and access packed items at suitable destinations. Capacity and packing rules remain unresolved.
- **Approved creator direction:** Build broad, believable restaurant, food, non-alcoholic beverage, alcohol, cocktail, bottle, cigar and cigarette catalogs. Use real-world price research as reference evidence while preserving existing creator price anchors; final game prices remain subject to review.
- **Approved creator direction:** Provide contextual social-action buttons at poker tables, including drink pouring/consumption, cigar/cigarette interactions and shot offers, without displacing the primary poker interface.
- **Approved creator direction:** Full bottles are persistent possessions with tracked remaining pours; players can carry them between locations and retain them through vehicle entry/exit and travel.
- **Approved creator direction:** Players can gift food and drinks to other players through the in-game messaging/inbox. Recipients must accept before fulfillment. NPC servers can deliver accepted gifts. Refund/expiry edge cases remain unresolved.
- **Approved creator direction:** Include cigar bars, cigar lounges, private/executive boss-style cigar rooms and VIP social spaces for conversation, drinks, socializing and card trading.
- **Approved creator direction:** Character simulation should include expressive drinking, smoking and social animations and a nonessential, non-competitive bubbly/intoxication presentation. Exact effects and limits remain unresolved.
- **Approved creator direction:** Hotels and Hustle Towers should support staffed hospitality: doormen, circular-driveway drop-off, valet vehicle parking/retrieval, concierge/front desk, bellhops/luggage assistance and elevator attendants.
- **Approved creator direction:** NPCs must communicate proactively and conversationally with players, ask questions, accept player responses and react contextually. They should provide directions, local/service information and game-world guidance using authoritative state rather than inventing events or player information.
- **Implementation discipline:** These are required product directions, not claims that features are already implemented or included in the first playable release. Interaction details, content, capacities, economics, technical architecture and production phasing remain to be designed. The creator remains final design authority.
- **Canonical specification:** `docs/gameplay/SOCIAL_WORLD_LIFESTYLE_AND_PLAYER_INTERACTION_REQUIREMENTS.md`.

## Large poker rooms and proactive roaming service staff
- **Approved creator direction:** Poker rooms should be large, impressive multi-table spaces where a player can see other active tables, player groups, NPCs and venue activity from their own table.
- **Approved creator direction:** NPC waitstaff circulate through poker rooms and approach different tables/players rather than remaining stationary.
- **Approved creator direction:** Servers proactively offer food and drinks through audible, conversational dialogue; players can respond, order, decline or dismiss the offer.
- **Approved creator direction:** After an order is confirmed, the NPC obtains the selected item from the appropriate service point and visibly returns to deliver it; charges and inventory updates must be accurate.
- **Approved creator visual direction:** Hospitality staff should include predominantly adult female characters with glamorous, attractive, venue-appropriate fashionable/revealing uniforms, potentially lingerie-inspired where compatible with the game's rating, platform rules and setting. Final outfit references/designs remain to be reviewed.
- **Implementation details still open:** Room dimensions/table count/occupancy, NPC density and performance budget, pathfinding/service routes, spoken dialogue and localization, order/payment timing, animation coverage and staff scheduling.
- **Canonical specification:** `docs/gameplay/SOCIAL_WORLD_LIFESTYLE_AND_PLAYER_INTERACTION_REQUIREMENTS.md`.

## Flirting, playful banter and social chemistry
- **Approved creator direction:** Adult NPCs and players should be able to exchange playful, flirtatious banter; female characters can flirt with male players and male characters can flirt with female players.
- **Approved creator direction:** Social behavior includes smiles, laughter, eye contact, compliments, teasing and expressive conversational gestures.
- **Approved creator direction:** Light physical gestures such as a shoulder touch may be used when contextually appropriate and welcomed; interactions must respect refusal and social boundaries.
- **Implementation details still open:** Dialogue variation, personality/context systems, animation/gesture sets, player consent controls, voice and localization.
- **Canonical specification:** `docs/gameplay/SOCIAL_WORLD_LIFESTYLE_AND_PLAYER_INTERACTION_REQUIREMENTS.md`.

## Contextual quick replies and free-text NPC conversation
- **Approved creator direction:** NPC questions and service offers should present a few immediate, context-specific quick replies (for example, relevant drinks/food, another cigar, view options, ask a question, or decline).
- **Approved creator direction:** Players must also be able to type a custom natural-language response; the NPC should respond in context and maintain conversation continuity.
- **Approved creator direction:** Choices must match the NPC's role, venue inventory/services and current player/game state. NPCs cannot promise unavailable services or invent prices, stock or events.
- **Approved creator direction:** Purchases/services must be clearly selected and confirmed before fulfillment/charging; declines must be respected.
- **Implementation details still open:** Choice layout/count, touch UI, text entry, voice input, moderation, localization and dialogue orchestration.

## Universal role-based NPC interaction across the city
- **Approved creator direction:** The contextual quick-reply and custom free-text conversation system applies across the entire city and all appropriate NPC roles, not only hospitality servers or poker venues.
- **Approved creator direction:** Players can use role-specific quick replies and custom text to interact with valet attendants (park/retrieve vehicles), hotel front desks (room search/booking/check-in), concierges (directions and local information), bellhops (luggage), elevator attendants (floors/destinations), and other city staff.
- **Approved creator direction:** NPC interactions should support complete service conversations and workflows: ask, clarify, present valid choices, confirm, perform the requested action and report the verified outcome.
- **Approved creator direction:** Consequential actions such as bookings, reservations and purchases require authoritative availability/terms and player confirmation; NPCs must never claim a service or action is complete before the underlying game system confirms it.
- **Approved creator direction:** Custom typed requests must be handled in context; when an NPC cannot fulfill a request, it should clarify or explain supported alternatives instead of pretending.
- **Implementation details still open:** Role/service configuration, conversation continuity, booking and payment integrations, navigation data, error recovery, interaction layout and production phasing.
- **Canonical specification:** `docs/gameplay/SOCIAL_WORLD_LIFESTYLE_AND_PLAYER_INTERACTION_REQUIREMENTS.md`.
