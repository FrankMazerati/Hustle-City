# Hustle City — Project Vision

## Product identity
Hustle City is an original, cinematic, realistic 3D social-world and open-world city-life game. Its first flagship environment blends selected Chicago-inspired urban character with Florida-inspired tropical/coastal atmosphere, but it is **not a literal recreation of Chicago, Miami, or any single real city**. The game owns its fictional geography, district identities, landmarks, architecture, street culture, names and visual language.

The world-building foundation must be capable of creating scenery beyond this initial blend: dense downtowns, historic neighborhoods, modern waterfronts, tropical islands, inland lakes, parks, wetlands, industrial corridors, suburban edges, rural routes and other distinct U.S. regional environments as the project expands.

## Product origin and identity evolution
The project began under the working title **Clover City Shuffle Club**, with a clover-centered visual identity built around the original shuffle-club/poker concept. As the creator developed the broader vision—drawing on real-life hood and neighborhood culture, city lifestyle, social identity and a much larger living urban world—the project evolved and was renamed **Hustle City**. The broader Hustle City identity is the current product direction; the original title and clover concepts are part of the project's creative history, not a requirement to preserve the old branding in the current product.

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
- Daily login rewards, weekly streak rewards, activity rewards and XP progression can encourage return visits. The creator specifically wants active players to feel recognized when they return for multiple play sessions in one day and when they spend several hours enjoying the game on a day they have free. Support optional repeat-session milestones and sustained-play milestones that reward meaningful poker, social, event and city activity—not merely opening the app repeatedly or remaining idle.
- Do not require multiple logins per day to maintain basic housing, phone or utilities. Do not make essential services disappear because a player misses a day. Consider streak grace/repair options and catch-up paths so absences do not create punitive loss.
- Use transparent, predictable reward schedules and reasonable safeguards against farming or runaway economy inflation. Longer sessions and multiple sessions may earn additional, clearly disclosed milestones, but rewards must not become coercive, uncapped or dependent on uninterrupted play. Provide natural stopping points; players who choose a shorter session should still make worthwhile progress. Avoid manipulative urgency, deceptive near-miss progress, and schedules designed to pressure unhealthy prolonged sessions.
- Progress bars should move in visible, satisfying increments through normal play, but advancement must be balanced and achievable without excessive grinding, spending or uninterrupted hours. The creator's "small progress each time" direction is a pacing/feedback goal, not approval for exploitative friction.
- Players should have meaningful ways to earn the lifestyle charge through normal gameplay; do not make real-money purchases necessary to keep a basic home, phone or utilities active. Exact reward amounts, XP curves, streak rules, caps, weekly charge timing, grace periods and economy sinks remain unresolved.
- Measure retention alongside player wellbeing indicators: session length distribution, voluntary return rate, churn, reward completion, reports of pressure/frustration and healthy stopping points. Optimize for a fun sustainable community, not maximum compulsion.


## Away-state property care and player re-engagement notifications
- Hustle City should continue to reflect the passage of time when a player is away. After a configurable absence period, owned/rented living spaces may show reversible signs of neglect (for example, dust, flies, roaches or general deterioration), and owned vehicles may show a maintenance-due state.
- These are world-state and maintenance prompts, not ownership penalties. Never evict a player, remove their apartment, permanently damage/confiscate their car, or block core poker/social play solely because they were away. Returning players must have a clear, reasonably affordable way to clean, repair and restore their property/vehicle.
- The creator wants the game to encourage at least a daily return where practical, while also respecting real-life schedules. Absence reminders and optional care systems should create a reason to return without making daily attendance mandatory to preserve essential assets.
- Offer optional email and SMS/text alerts during onboarding, with clear separate consent for each channel, the purpose of messages, expected frequency and an easy way to change preferences or unsubscribe. In-game notification preferences must remain accessible later.
- If a player uses Facebook or another social login, that authentication choice does not itself grant permission to send marketing or platform notifications. Use only notification channels and permissions the player explicitly authorized and that the provider/platform supports. Do not imply that Hustle City can send Facebook notifications merely because the account was linked.
- Example alert content may say that an apartment needs attention or a vehicle is due for maintenance, and invite the player to return. Keep messages factual, friendly, low-frequency and non-alarming; do not use deceptive urgency or shame.
- Implement frequency caps, quiet hours, deduplication, preference controls, unsubscribe/STOP handling for SMS, and delivery/audit records. Avoid exposing sensitive account or property details in lock-screen messages. Respect applicable privacy, electronic messaging, carrier and platform requirements.
- Exact absence thresholds, deterioration stages, restoration costs, notification cadence, channel availability and consent wording remain unresolved and require creator approval and implementation review.


## May 2027 delivery target and $10,000/month revenue objective
- The creator has set a target of completing and launching Hustle City by **May 2027**, with a business objective of reaching **at least $10,000 in monthly revenue**. These are planning targets, not a guarantee of delivery or earnings.
- Delivery planning must distinguish a focused, launchable MVP from the longer-term full Hustle City vision. Protect the poker-first social core and prioritize a playable, testable, monetizable release over attempting to finish every planned city system by the target date.
- Revenue planning should model monthly active users, ad impressions/completions, payer conversion, average revenue per paying user, platform/store fees, taxes, ad fill, geography and retention. Do not treat ad benchmark eCPMs or gross revenue as guaranteed net income.
- Monetization should be diversified and player-respecting: advertising, optional memberships and optional cosmetic/convenience purchases can contribute, while basic access to poker/social play and a fair non-paid path to earn virtual chips remain available.
- Track actual cohort and revenue performance after launch and revise forecasts from measured data. The $10,000 monthly target requires a defined revenue mix and audience size; it cannot be inferred from the existence of ad placements alone.

## In-game advertising and rewarded-ad placements
- A small, persistent bottom-of-screen banner is a permanent standard ad placement for all players, including every paid membership tier. The creator explicitly confirmed that membership does not remove the banner; it is a continuing revenue stream that helps fund in-game content and operations. Keep it compact and unobtrusive, outside controls and critical gameplay, with provider-compliant refresh behavior.
- The creator suggested refreshing bottom-banner ads approximately every 10–15 seconds. This interval is **not approved for implementation**: ad-network rules and user experience must be checked. For example, Google AdMob documents custom banner refresh intervals of 30–150 seconds and recommends its optimized refresh rate. Use a compliant/optimized interval rather than forcing a 10–15-second refresh.
- Add optional rewarded-video opportunities at contextual locations such as the bar when a player has run out of poker chips. A player may choose to watch an ad for a clearly disclosed, capped amount of non-redeemable virtual poker chips or another approved in-game reward. Watching must not be required to continue playing; retain a non-ad earning/recovery path.
- Schedule short, non-rewarded in-app ad breaks at 15-minute active-session milestones: 15, 30, 45 and 60 minutes in the first hour, then every 15 active minutes thereafter (a maximum of four scheduled breaks per hour). These are predictable timing points, not random interruptions. Present an ad only at a safe natural transition; defer while a player is in a live poker hand, making a consequential table decision, talking with friends, trading cards, traveling or completing another critical interaction. If the player is still busy when the opportunity expires, skip it rather than stacking missed ads. The creator wants the ad to become dismissible after approximately five seconds; verify that the selected provider/format supports this before implementation. Exact provider, close behavior and final UX require testing.
- Add occasional opt-in “double your reward” offers after selected eligible activities or reward claims. The player must see the exact reward and opt in before the video starts. Do not show the offer after every action; use contextual eligibility, frequency caps and cooldowns.
- Casino-context sponsored/rewarded placements may be considered sparingly (the creator suggested roughly one or two opportunities in a relevant visit/session), subject to age-rating, gambling-advertising, platform and legal review. Do not imply that virtual-chip rewards are cash or redeemable value.
- Do not force full-screen ads during a poker hand, table decision, social conversation, travel sequence or other critical interaction. Provide clear dismissal/decline paths and respect ad frequency limits.
- Measure banner viewability, fill rate, rewarded-ad opt-in/completion, retention, session quality, revenue per daily active user and complaints. Optimize total sustainable revenue and player experience rather than raw ad count.
- Exact ad network, banner size/placement, refresh policy, rewarded amounts, cooldowns, eligibility, timed-ad triggers, provider support for the five-second close behavior and final transition/deferral rules, five-second dismissal support and revenue mix remain unresolved and require implementation, provider-policy and creator review. The bottom banner is not an ad-free membership entitlement: it remains on for all tiers.


## Three-to-four-hour daily destination and activity loop
- The creator's target is an **average of three to four hours of active daily play per active user**. This is a product-design and business target to validate with real cohorts, not a guaranteed outcome or a requirement that every player must meet.
- Poker is the anchor activity, not the only reason to stay. Hustle City should offer a varied, connected set of worthwhile activities that make a longer visit feel natural: poker, chip earning/recovery, bar socializing, card trading, conversations and meeting people, traveling between districts/venues, attending events, furnishing/customizing/upgrading apartments and houses, vehicle/lifestyle upgrades, and discovering the living city.
- Design a regular player's return loop around meaningful choices. Example: a player runs low on poker chips, chooses to spend time at the bar trading cards and socializing, takes part in other activities while waiting for eligible opportunities, and may voluntarily watch a rewarded ad for a clearly disclosed virtual-chip reward or opt into doubling an eligible activity reward.
- The creator wants regular users to have opportunities to earn additional in-game currency/rewards by choosing longer rewarded-video experiences. These are voluntary rewarded placements, distinct from the four scheduled non-rewarded ad opportunities per active hour and the persistent bottom banner. The reward must be shown before opt-in and must be funded/balanced in the virtual economy.
- Do not make ad watching the only way to recover poker chips, progress, or participate. Preserve ordinary gameplay earning routes and a fair non-ad alternative. Never imply virtual chips or in-game currency are redeemable for cash.
- Track average daily active play, distribution of session lengths, meaningful activity mix, return frequency, social participation, progression, chip recovery routes, rewarded-ad opt-in/completion, purchases and retention. Do not optimize solely for longer sessions or ad volume; use player feedback and healthy-engagement indicators, preserve natural stopping points, and avoid forced waits or ad loops.
- The three-to-four-hour target must come from a genuinely engaging variety of activities—not repeated chores, artificial waiting, excessive ad interruptions, or pressure to stay online. Shorter sessions must still feel worthwhile.


## Daily return loop, personal upkeep and city events
- The creator wants a strong daily check-in loop that gives players personal, understandable reasons to return: home/apartment upkeep, garage and vehicle maintenance, weekly lifestyle bills, daily rewards/progression, and upcoming social events.
- The game may show an apartment-care reminder, garage notice that one or more owned vehicles are due for routine maintenance, a weekly lifestyle-package/bill reminder, and a prompt to collect available daily rewards. Example in-world tone: “Hustle City is missing you. Your garage could use a little attention, and your apartment is ready for a quick refresh. Your weekly lifestyle package is coming due. Come back, collect your rewards, and see what's happening around the city.”
- Reminders should be personalized to actual in-game state and timing. Do not claim a car needs service, a bill is due, or a reward is waiting unless that is true in the player's account.
- Use an event calendar as a central community heartbeat: stadium-scale parties and headline events; smaller venue concerts, club nights and social gatherings; recurring and special events that encourage players to meet up.
- Events should support player socializing, dancing, conversations, card trading where appropriate, networking, group attendance and shared experiences. The intended feeling is that Hustle City is a lively social destination and a place to build friendships and connections; any exchange of real-world contact details or off-platform networking must be voluntary, mutual-consent, privacy-aware and protected by block/report/safety controls.
- Daily reminders and events are invitations, not threats or obligations. Missing a day must not cause eviction, loss of home/car, confiscation, permanent deterioration, punitive service shutoff, or exclusion from poker/social play. Upkeep should be reversible and reasonably affordable, bills transparent with a fair earning path, and daily rewards/streaks should have reasonable grace/catch-up rules.
- Respect notification opt-ins, channel-specific consent, quiet hours, frequency caps, deduplication, preferences and unsubscribe requirements. Avoid shame, deceptive urgency or sensitive lock-screen disclosures.
