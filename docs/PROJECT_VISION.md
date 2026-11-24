# Hustle City — Project Vision

## Product identity
Hustle City is an original, cinematic, realistic 3D social-world and open-world city-life game. Its first flagship environment blends selected Chicago-inspired urban character with Florida-inspired tropical/coastal atmosphere, but it is **not a literal recreation of Chicago, Miami, or any single real city**. The game owns its fictional geography, district identities, landmarks, architecture, street culture, names and visual language.

The world-building foundation must be capable of creating scenery beyond this initial blend: dense downtowns, historic neighborhoods, modern waterfronts, tropical islands, inland lakes, parks, wetlands, industrial corridors, suburban edges, rural routes and other distinct U.S. regional environments as the project expands.

## Visual identity and atmosphere
- Photorealistic/cinematic 3D presentation, with believable scale, materials, lighting, weather, crowds, traffic, water and environmental storytelling.
- Chicago inspiration: recognizable big-city density, downtown skyline composition, grid and arterial streets, brick and stone neighborhood architecture, bridges, river/canal moments, lakefront promenades, parks, elevated rail/L-train character and underground subway infrastructure.
- Florida inspiration: warm and humid weather, palm-lined streets, tropical planting, coastal light, beaches, marinas, yacht harbors, canals, lagoons, islands, causeways, waterfront homes, resort and nightlife districts, sudden rain and dramatic sunsets.
- Blend these influences intentionally. Do not simply paste Chicago landmarks into Miami scenery or reproduce either city block-for-block.
- Hustle City must have its own skyline, fictional landmarks, neighborhood identities, architecture families, street furniture, signage, waterfront shapes and district transitions.
- Environmental palette: electric blue, white, sunset pink, purple transitions and colorful sunrise/sunset gradients. Use black and gold selectively for luxury, premium brands and nighttime atmosphere. Neighborhoods may have distinct palettes that remain coherent with the larger world.
- Preserve established visual continuity: wet reflective streets when weather calls for them, cinematic luxury/crew vehicle imagery, expressive street culture, skyline and waterfront vistas.
- Mazerati Boys is spelled with a Z and uses black and gold.

## World and scenery design principles
1. Build a reusable world-generation foundation, not a one-city one-off.
2. Use a library of environment archetypes and mix them through authored design, procedural tools and hand-built landmarks.
3. Each district must have a readable identity, coherent street network, believable terrain/water edges, functional transportation and appropriate building typologies.
4. Water is a first-class world system: lakefronts, rivers, canals, bays, lagoons, ponds, marinas, beaches, islands, docks, bridges, causeways, water taxis and safe access rules.
5. Vegetation must be climate- and location-aware: palms in warm coastal/tropical settings, temperate street trees and parks in cooler/urban settings, marsh plants in wetlands, and appropriate native-inspired planting elsewhere.
6. Weather and lighting must respond to the environment: humid haze, bright coastal sun, cloud build-up, showers, thunderstorms, rain-slick roads, fog, clear nights, seasonal variation and smooth transitions.
7. Create distinctive scenery without copying protected real-world maps, landmarks, logos, or trade dress. Research references must carry source and license metadata.
8. The initial Chicago/Florida blend is the flagship setting; future U.S. cities and regions should be generated from the same reusable rules with different geography, climate, architecture and vegetation profiles.

## Player experience
- Persistent Player Shell above reusable game environments: profile/avatar, username, crew, Hustle Money, Diamonds, Poker Chips, level/XP, notifications, messages, map, navigation, settings and contextual actions.
- Players can walk together, socialize, visit venues and participate in activities.
- For vehicles, destination-based automated travel is preferred over manual driving. Players choose driver/passenger, board together, choose destinations and travel as a group; convoys arrive together.
- Basic transport should not consume premium Diamonds. Diamonds are for premium travel options. Basic rideshare/transit can use Hustle Money or be free according to the service design.
- NPCs are responsive and answer using actual game state, not invented event or transit information.

## Living city
Persistent automated events from launch, with NPCs driving much of the activity. Cars, traffic lights, pedestrians, buses, trains, weather, venues, waterways and NPC routines operate automatically. Players can discover, join, watch and interact with activities. An Operations Status Board should monitor live events, player participation, NPC activity, traffic/transit, venues and alerts.

## Transportation
Chicago-style elevated rail/L train and underground subway are important. Riders board, sit, see outside through windows and can change camera views (passenger, window, exterior, overhead/free camera); trains stop at stations and passengers disembark. Also plan buses, rideshare, water taxis, cars/motorcycles, helicopters, private aircraft, boats and yachts. Water and air transportation must fit the authored geography rather than appear arbitrarily.

## Safety
No player death. Build prevention, detection and safe recovery for vehicle contact, falls, water, train tracks, doors, collisions, restricted areas and stuck states. Preserve progress and possessions after accidental hazards.

## World planning
- Approved master planning grid: 7x7 = 49 large boxes.
- Six central boxes reserved for central districts; 43 potential outer neighborhood boxes.
- Each outer neighborhood planning box uses a 5x5 grid = 25 blocks; 43 boxes would represent 1,075 potential outer-neighborhood blocks.
- This is long-term capacity, not a launch build requirement.
- Six central district concepts: Diamond, Entertainment, Marina, Fashion/Swagger (working label), Financial and Downtown. Exact boundaries and some assignments remain open.
- Neighborhood founding/ownership, crew leadership, property/business ownership and residency/membership are distinct.
- Neighborhoods should look large and alive at launch but can have limited fully interactive destinations (roughly five per neighborhood was discussed as an initial concept). Remaining buildings can be ambient scenery and activated later.

## Social, economy and activities
Separate Hustle Money, Diamonds and Poker Chips. Plan crew/friend/private/group/nearby/table chat, social feeds, invitations/referrals, properties, businesses, events, venues and optional premium content. Avoid pay-to-win and keep essential social participation accessible. Real-money gambling requires legal review; initial poker should use non-redeemable virtual chips.

## Named places and brands
Velvet Club Lounge; Hustle Club; Hustle City Marina and Yacht Club; Hustle Towers; The Shuffle Club; Swagger Shop; American Swagger Clothing; Bella Rose Collection; We Fly High International Airport / We Fly Sky International Airport (final name unresolved); Mazerati Boys Automotive Group (working name); South Side Bar; East Side Bar; North Side Bar; West Side Bar; Casino (planned, district unresolved).

## Character and onboarding
Bella Rose is a confident, fashionable, street-smart guide with humor and attitude. She introduces new players to venues, clothing, card rooms and activities; players can call for help, skip or revisit guidance.

## Technology and engine decision
- **Unreal Engine 5 is the primary production engine.**
- **Unity 6 is the secondary compatibility/migration target**, not a parallel production runtime.
- Engine-neutral rules, data schemas, content definitions and source assets live in SHARED_CORE and SHARED_ASSETS. Engine-specific rendering, physics, animation, input, UI, networking and packaging live in ENGINE/unreal or ENGINE/unity.
- Godot is retired from the approved engine architecture. Existing Godot work and history are not to be destructively deleted; archive or remove active references only after preserving relevant assets and documenting disposition.
- Local development/testing and cloud-hosted live multiplayer are the intended direction; provider and detailed topology are undecided.


## Product rollout strategy — launch scope and expansion
The initial commercial/product objective is to attract and retain players with a polished **poker-first social activity game**: a welcoming, lively city where people meet, communicate, visit venues, play poker using non-redeemable virtual chips, attend social activities and build friendships/crew identity. The first release should prove the core social loop, player acquisition, retention and sustainable revenue before attempting a much broader open-world simulation.

### Initial release boundaries
- Prioritize multiplayer social presence, poker/card activities, venues, events, player identity, messaging, virtual economy and a convincing ambient city.
- The city may depict NPC-only street incidents and emergency activity as environmental storytelling, but these are not player crime systems.
- Initial players do not rob, steal, use weapons, commit player-directed crimes, get arrested, go to jail, die, or enter player medical/hospital consequence loops. Do not build player-targeted law-enforcement gameplay into the initial release.
- NPC police/fire/ambulance and NPC arrest/hospital/jail simulations may operate as ambient background systems, with player interaction limited to safe, friendly, non-punitive encounters (for example, officers asking a yacht party to lower its noise).
- Keep player movement and transport safe; no intentional random vehicle crashes. Preserve player assets and progress when simulation faults occur.
- Everyday lifestyle systems (housing, vehicles, insurance, fuel, phone service and maintenance) must remain lightweight and must not obstruct the core poker/social loop. A bundled/simple default is under consideration; exact costs and rules are not approved.

### Expansion strategy
- Design modular systems and clean data/content boundaries so the world can grow without rebuilding the foundation.
- After the initial game is established, has players and generates revenue, later phases may explore expanded open-world/crime-oriented gameplay, including player law-enforcement consequences, jail scenarios, weapons and drugs. These are future possibilities only—not launch requirements, not approved feature specifications, and not permission to implement them now.
- Any later expansion requires a separate creator-approved scope, product/business case, technical and safety review, platform-age-rating review, legal/compliance review where applicable, and explicit design of player protections and moderation.
- Growth may be supported by future investors, partners and additional development contributors. The architecture and documentation should make the product understandable, modular and extensible for those collaborators.
- Protect the original launch identity: a social-first poker and city-lifestyle game. Do not let speculative future features delay getting the initial experience into players' hands.


## Engagement, daily rewards and lifestyle package economy
- The creator's intended progression loop combines daily return rewards, meaningful play/activity rewards, gradual XP/level progress, weekly lifestyle packages and aspirational upgrades.
- Each player may select a lifestyle bundle (for example, Starter, Comfortable, Premium or Elite) with a clear recurring in-game price and included services such as housing tier, phone tier and utilities. These are illustrative tier names; exact names, contents, prices and billing cadence require balancing and creator approval.
- Prefer one understandable weekly lifestyle charge over many separate micro-bills. Players may upgrade individual bundle components or move to a higher tier. Bundle prices must be affordable relative to ordinary in-game earning opportunities and must not make poker/social participation inaccessible.
- Daily login rewards, weekly streak rewards, activity rewards and XP progression can encourage return visits. Reward meaningful play and varied social/game activities rather than raw idle time or repetitive check-ins.
- Do not require multiple logins per day to maintain basic housing, phone or utilities. Do not make essential services disappear because a player misses a day. Consider streak grace/repair options and catch-up paths so absences do not create punitive loss.
- Use transparent, predictable reward schedules and reasonable daily caps. Avoid infinite/uncapped playtime incentives, manipulative urgency, deceptive near-miss progress, or reward schedules designed to pressure unhealthy prolonged sessions.
- Progress bars should move in visible, satisfying increments through normal play, but advancement must be balanced and achievable without excessive grinding, spending or uninterrupted hours. The creator's "small progress each time" direction is a pacing/feedback goal, not approval for exploitative friction.
- Players should have meaningful ways to earn the lifestyle charge through normal gameplay; do not make real-money purchases necessary to keep a basic home, phone or utilities active. Exact reward amounts, XP curves, streak rules, caps, weekly charge timing, grace periods and economy sinks remain unresolved.
- Measure retention alongside player wellbeing indicators: session length distribution, voluntary return rate, churn, reward completion, reports of pressure/frustration and healthy stopping points. Optimize for a fun sustainable community, not maximum compulsion.
