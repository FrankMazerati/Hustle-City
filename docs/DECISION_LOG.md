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

## Distinct NPC personality, voice, look and swagger
- **Approved creator direction:** NPCs should have their own recognizable personalities, voices, visual looks, fashion/styles, swagger, mannerisms and conversational delivery rather than feeling interchangeable.
- **Approved creator direction:** Individual identity should be expressed through dialogue, voice tone/cadence, grooming, clothing, posture, movement, facial expressions and gestures, and should remain consistent across conversations and service interactions.
- **Implementation details still open:** Character archetypes/roster, voice production, visual style library, animation coverage, dialogue continuity and production budgets.
- **Canonical specification:** `docs/gameplay/SOCIAL_WORLD_LIFESTYLE_AND_PLAYER_INTERACTION_REQUIREMENTS.md`.


## Hustle City flagship master menu and economy spending direction
- **Approved creator direction:** Complete the flagship fictional Hustle City menu first. Current work scope is the Hustle City home-market menu only; Chicago and the other 29 city markets are deferred until this catalog is completed.
- **Approved catalog scope:** Broad real-world food menu; breakfast/brunch; burgers/sandwiches; chicken/wings; soul food/Southern/Caribbean; pizza/pasta; Mexican/Latin; seafood; salads/bowls; sides; snacks/appetizers; desserts/bakery; family meals; soda/pop; water; juice; sports/hydration/energy drinks; tea/coffee; milk/shakes/specialty non-alcoholic drinks; beer; wine; cocktails; liquor by the shot; liquor bottles; cigars; cigarettes and related accessories.
- **Approved creator price direction:** Keep the existing game-price anchors/draft values as they are for now. Complete the item catalog first; do not silently replace current proposed game prices or treat real-world retail/bar prices as in-game prices. Real-world price research is a separate evidence layer used for the later pricing pass.
- **Approved creator affordability direction:** Free players should be able to cover ordinary session consumption—food, shots and an occasional cigarette or cigar—without paying real money, and should be able to save for an outfit or two. Vehicles, flights, helicopters and similarly major aspirational purchases should be premium/paid-gated or require substantial progression, rather than being routine free-session purchases. Exact prices and earnings remain unresolved.
- **Bottle selection guardrail:** Aim to keep ordinary real-world bottle reference examples at or below approximately $150; this is a research/catalog ceiling direction, not a Hustle Money price. Exact products, sizes, regional availability and price snapshots must be verified.
- **Real-world brand references:** Brand examples may inform catalog completeness, but inclusion does not grant trademark, trade-dress, product-placement or packaging-art rights. Licensing and platform/rating review remain separate.
- **Canonical flagship catalog:** `docs/economy/HUSTLE_CITY_FLAGSHIP_MASTER_MENU.md`. The catalog contains items/brand families and research references; game prices remain a separate creator-approved pass. Existing draft game-price worksheet is preserved unchanged.
- **Approved creator direction — Poker Chip conversion:** Players should be able to exchange Poker Chips for Hustle Money when they need general spending money, then use Hustle Money for eligible city purchases. This is a conversion between separate wallets, not direct payment of food/drinks with Poker Chips.
- **Conversion implementation guardrails:** Atomic debit/credit; authoritative auditable ledger; idempotency and anti-replay/concurrency protections; show quote, fee and limits and obtain confirmation before conversion.
- **Unresolved:** Exchange ratio, fees, limits, eligibility of purchased chips versus winnings, cooldowns, restrictions, reversal rules and launch timing. Paid chips/wagering/prizes/transfer/redemption and conversion require legal/platform-policy review; do not imply cash-out or real-world value.
- Canonical economy specification: `docs/economy/MEMBERSHIPS_AND_REWARDS.md`.


## Poker-to-lifestyle economy, premium access and neighborhood property ownership
- **Approved creator direction:** Hustle City should connect poker success to the wider city lifestyle. Players can win Poker Chips at poker, then use a staffed cashier or self-service kiosk to exchange eligible chips into Hustle Money and spend it in the city.
- **Approved conversion rate:** 1 Poker Chip = 1 Hustle Money (dollar-for-dollar nominal in-game denomination). This is not real-world cash redemption or a representation of real-money value. Keep both wallets separate and use atomic, auditable, idempotent ledger transactions.
- **Approved creator direction:** Support additional earning/progression through social participation, including communicating with other players, adding friends and optional social posts. Exact reward actions/amounts are unresolved; social posting must remain optional and anti-spam/anti-fraud protected.
- **Approved creator direction:** Preserve practical access for free players through walking, public transportation and rideshare-style services; the established rideable bus and city L train concepts remain part of the transportation direction.
- **Approved premium-lifestyle direction:** Paid packages and/or premium progression may unlock luxury ownership/access such as personal cars, yachts, private jets and private helicopters. Do not make ordinary free play trivially provide yachts/private aviation. Exact earned-versus-paid boundaries, ownership versus rental/charter, and access rules remain unresolved; preserve meaningful gameplay earning where already directed.
- **Approved property direction:** Offer individually identifiable neighborhood houses for sale when vacant/unoccupied. Each property requires a unique house/parcel ID and authoritative availability, occupancy and ownership state. Players may be able to own multiple homes on a block and potentially a whole block.
- **Proposed, not finalized:** Five-to-seven-to-ten houses per block as a possible density range; five owned houses or a whole-block acquisition as examples, not fixed caps or final rules.
- **Existing map constraint:** Accepted 7×7 master grid = 49 large boxes; six central districts and 43 neighborhood boxes. Each neighborhood box contains 5×5 city blocks (25 each), or 1,075 outer-neighborhood blocks total. This does not set house count per city block.
- **Required distinction:** Individual home ownership, multiple-home ownership, whole-block ownership and neighborhood founding/claiming are separate concepts. Do not conflate owning a block with owning/founding a neighborhood.
- **Unresolved:** Home/whole-block prices and purchase currencies; exact house density; ownership limits; listing, rental, resale and transfer rules; social reward values/limits; rideshare pricing; vehicle/yacht/aircraft unlocks and premium package contents; detailed property-state and transaction implementation.
- **Guardrail:** No real-world cash-out is implied by Poker Chip conversion. Legal/platform/consumer-protection and anti-fraud review is required for paid chips, wagering/prizes, social rewards and premium property/vehicle transactions.
- Canonical economy specification: docs/economy/MEMBERSHIPS_AND_REWARDS.md.


## Neighborhood price identity and daily petty-cash rewards
- **Approved direction:** Comparable goods and services should have neighborhood-appropriate prices rather than one assumed universal citywide price. Neighborhoods need distinct identities spanning upscale/affluent, middle-income, working-class and lower-income/hood environments.
- **Approved direction:** NPC populations, fashion, vehicles, dialogue, behavior, local businesses and ambient activity should fit each neighborhood's identity while preserving individual character variation and avoiding caricature.
- **Proposed, not locked:** Daily login rewards and other modest petty-cash routes should let free players cover ordinary day-to-day spending without eliminating the value of memberships/kits, larger earning loops or premium activities.
- **Proposed values only:** Around $500 Hustle Money daily; around 5,000–10,000 Poker Chips daily; a possible seven-day progression adding roughly $100 cash; and a floated 100,000-chip starting example that the creator reconsidered. These are discussion values, not approved tuning.
- **Unresolved:** Neighborhood names/economic tiers; localized price lists and multipliers; NPC population distributions; exact daily reward amounts and schedule; streak/catch-up rules; petty-cash activity list and payouts; and balancing against Poker Chip conversion, kits and premium activity costs.
- Canonical specifications: docs/economy/MEMBERSHIPS_AND_REWARDS.md and docs/gameplay/SOCIAL_WORLD_LIFESTYLE_AND_PLAYER_INTERACTION_REQUIREMENTS.md.
