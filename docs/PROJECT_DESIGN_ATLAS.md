# Hustle City — Consolidated Design Atlas

## 1. World map and districts
- Master map: 7x7 large boxes = 49 total.
- Six central boxes reserved for central districts; 43 boxes are potential outer neighborhoods.
- Each outer neighborhood box contains a 5x5 planning grid = 25 blocks. Long-term capacity across all 43 is 1,075 blocks.
- This is a capacity plan, not a requirement to build every box at launch.
- Six central district concepts: Diamond District, Entertainment District, Marina District, Fashion/Swagger District (working label), Financial District and Downtown District.
- Casino is planned; its district is unresolved.
- Hamburger/map UI should show the full map, color-coded districts and neighborhoods, names, ownership/crew identity and destinations. A separate transit layer should show routes and stations.
- Neighborhood boundaries should be legible with connecting avenues/boundary roads, entrance signage and environmental transitions.

## 2. Neighborhood identity, ownership and activation
Keep separate: neighborhood founding/ownership; crew leadership; property/business ownership; neighborhood membership/residency. They may overlap but are not interchangeable.
- Eligible founders may claim an available neighborhood, name it, set identity/colors/emblem and establish an HQ. Not every player automatically owns a neighborhood.
- Other players can join existing neighborhoods/crews, own or rent property, or wait for future expansion opportunities.
- Neighborhoods have identity palettes (two primary colors plus optional accent), emblem, entrance signs and decorative accents. Do not paint every building entirely in crew colors; preserve realistic architecture.
- Neighborhood color and weather/sky are separate systems.
- Visual/environment existence, NPC traffic, transit, identity, ownership records, interactive businesses, events, management and customization should be independently activatable.
- Launch concept: neighborhoods look substantial and alive but have a limited set of fully interactive destinations; roughly five was discussed as an exploratory target. Candidate examples included starter apartment, modest starter property with one-car garage, small upgradeable office, used-car lot and possibly a community center. These are not a finalized list.
- Build activation hooks early so deeper neighborhood systems can be enabled later without rebuilding the map.

## 3. Transportation and mobility
- Automated destination travel is the preferred player experience; manual driving is not the core direction.
- Players choose driver or passenger, enter together, select destination and travel together. Crew convoy vehicles travel as a group and arrive together.
- NPC traffic, traffic lights, buses and trains operate automatically. Traffic signals coordinate protected turns, safe stopping distances, lane reservations and intersection occupancy.
- Rideshare should always be available through NPC drivers; players may optionally drive and earn Hustle Money. Basic rides use in-game Hustle Money or are free according to the service; Diamonds are for premium travel.
- Transit includes buses, Chicago-style elevated rail/L train, underground subway, water taxis, cars/motorcycles, helicopters, private aircraft, yachts and boats.
- Train ride is immersive: players board, sit, see the city through windows, switch passenger/window/exterior/overhead camera views, stop at stations and disembark.
- Do not invent route maps or travel metrics. Geographic and transit agents must record sources and licenses.

## 4. Traffic and pedestrians
Cars follow lanes and signals, stop predictably, avoid pedestrians and other vehicles, reserve intersections and safely stop if a route is blocked. Pedestrians use sidewalks/crossings, obey crossing phases, avoid vehicles, enter venues and interact with the city. QA must deliberately test crowded intersections, blocked lanes, simultaneous route requests and deadlocks.

## 5. Character movement and safety
Players should have useful 3D free movement to walk with friends through streets and venues, with customizable walk/swagger styles, hairstyles, clothing and appearance. Vehicle movement is automated/destination-based. No player death: prevent hazards and provide safe recovery for falls, water, vehicle contact, train tracks, closing doors, restricted areas and stuck states. Preserve progress and possessions.

## 6. Player Shell
Persistent UI layer across environments:
- Profile/avatar, username, crew identity/emblem, level/XP.
- Hustle Money, Diamonds and Poker Chips.
- Notifications, messages/email, friends/crew and settings.
- Expandable hamburger navigation and map.
- Context-sensitive actions; shortcuts such as Map, Crew, Inventory, Store, Poker, Settings, Events and Rewards.
- Chat can remain accessible while walking or traveling.
- Keep reserved ad space non-obstructive and configurable.
- Responsive layouts for tablet/phone/desktop; the world view remains primary.

## 7. Social, crews and feeds
Crew chat, group/travel chat, private 1:1, nearby chat and public venue/table chat. Friends, invites, profiles, contacts, block/report. World News Feed, Friends Feed, local Environment/Venue Feed and Official Admin Feed. Players may belong to multiple crews while maintaining a primary identity. Crews may have HQs, garages, clubs, vehicles, clothing, businesses, finances, dues, events and alliances.

## 8. Economy and business
Separate Hustle Money, Diamonds and Poker Chips. Properties and businesses are distinct from neighborhood ownership. Monetization candidates include subscriptions, ads, digital merchandise, properties/businesses and premium currency; avoid pay-to-win and keep essential participation accessible. Real-money gambling requires legal review; start with non-redeemable virtual chips.

## 9. City events and NPC activity
Persistent automated event system from the beginning. NPCs drive much of the ambient activity; players discover, join, watch and interact. Examples include car meets, marina/yacht parties, nightlife, basketball, park gatherings, vendors, fashion shows, concerts, celebrations and tournaments. NPCs answer “what's happening?” from authoritative event data. An operations status board tracks events, players, NPCs, traffic/transit, venues, automation and alerts.

## 10. Visual/environment systems
Time cycle: sunrise, morning, noon, afternoon, sunset, night. Weather: sun, clouds, rain, heat, cold, snow, fog, storms and seasonal variation. Effects include reflections, puddles, headlights, shadows, visibility, water, pedestrian clothing and outdoor activity. Smooth transitions between districts. Proposed system responsibilities: Time Manager, Weather Manager, Sky/Lighting Manager, District Appearance Manager, Crew Visual Influence and Transition Manager.

## 11. Card games
Multiple configurable variants, including six-card and nine-card 3x3 Tic-Tac-Toe. In the described nine-card mode: each player receives five private cards; shared board is three rows of three. Valid Tic-Tac-Toe lines are three rows, three columns and two diagonals. Hand construction described as exactly two private cards plus exactly three board cards to make a five-card hand. Optional three-card flop/side board depending on settings; some variants may allow discarding up to two private cards and drawing replacements. Dealer rotates; qualifiers/local rules are configurable. Preserve creator-defined rules; do not infer missing rules.

## 12. Named locations
Velvet Club Lounge; Hustle Club; Hustle City Marina and Yacht Club; Hustle Towers; The Shuffle Club; Swagger Shop; American Swagger Clothing; Bella Rose Collection; We Fly High International Airport / We Fly Sky International Airport (unresolved); Mazerati Boys Automotive Group (working name); South Side Bar; East Side Bar; North Side Bar; West Side Bar; Casino (planned, district unresolved).

## 13. Onboarding
Hustle City is the gateway into a broader expandable universe. Player obtains a Hustle City Key, chooses a home city and creates a character. Bella Rose is the confident, fashionable, street-smart guide who can introduce venues, clothing, card rooms and activities, and can be called for help or skipped/revisited.

## 14. Creator Studio and operations
Secure Creator Studio should manage vehicle packs, clothing, buildings, characters, crews, neighborhoods and events through create/import/preview/test/approve/publish. Global operations dashboard manages players, content, campaigns, staff roles, permissions, metrics and audit logs.


## 15. Everyday lifestyle costs and vehicle ownership (design direction)
- Hustle City should be able to represent ordinary lifestyle responsibilities such as housing, vehicle ownership, insurance, fuel, phone service and maintenance.
- Candidate vehicle paths include outright ownership and financing/car-note arrangements. Candidate housing paths include renting and owning.
- The creator raised the risk that separate recurring bills could make the experience feel like a second job. The design must therefore prioritize a low-friction, simplified default rather than requiring players to micromanage many bills.
- A bundled recurring lifestyle payment covering selected ordinary expenses is a candidate default. Optional itemized/detail management may be explored for players who want it. Neither the bundle contents, payment cadence, prices, missed-payment consequences nor final level of detail are approved.
- Gas/fuel may be represented as a lightweight ownership/use cost; decide whether it is automatically included, simplified, or separately managed before implementation.
- Vehicle insurance is a candidate ownership/service system. Avoid designing random crashes merely to create insurance claims.
- Traffic and vehicle simulation should prioritize predictable, safe behavior and collision avoidance. If a collision occurs because of a simulation or pathfinding fault, recovery must protect player-owned vehicles and possessions; do not punish players for system defects.
- Vehicle maintenance and insurance should not create pay-to-win advantages or block access to core social/poker experiences. Detailed costs, coverage, claim flows and ownership rules remain unresolved.

## 16. In-world mobile phone and communication
- Players should have a visible, usable in-world cellphone.
- A player can physically pull out/look at the phone while walking or standing, open a phone interface, select a contact and text/message another player.
- Phone interactions should support the established player-to-player communication system, with appropriate notification and conversation state.
- The phone is both a diegetic character prop/animation and an interface entry point; it should not require the player to leave the city world or permanently replace the main HUD.
- Exact calling/voice features, phone models, apps, contact permissions, message delivery rules, UI layout and animation scope remain to be designed.
- Phone communication must respect existing social safety requirements, including blocking, reporting, privacy and unwanted-contact protections.


## 17. Launch scope and long-term expansion boundary
- Initial release is a **poker-first multiplayer social activity game**, not a full crime sandbox. The immediate goal is to attract players, build an active community, validate retention and revenue, and establish a strong foundation.
- Launch priorities: multiplayer social presence, poker/card activities using non-redeemable virtual chips, venues, events, player identity/crew/friends, protected messaging, virtual economy and ambient city life.
- Initial player characters do not rob, steal, use guns/weapons, commit player-directed crimes, get arrested, go to jail, die, or enter player hospital/medical consequence loops. No player-targeted police enforcement or punitive law-enforcement gameplay at launch.
- NPC-only city incidents (including police activity, arrests, intoxicated NPCs, addiction/homelessness depiction, fires and medical emergencies) can provide ambient world life. Player-facing contact with authorities may be limited to friendly, non-punitive contextual interactions, such as a noise reminder at a yacht party.
- Avoid intentional random car crashes. Traffic should be predictable and safety-first; player assets/progress must be protected from simulation defects.
- Lifestyle realism must not overwhelm the core activity loop. Housing, vehicle ownership/financing, insurance, fuel, phone service and maintenance are candidate systems, but should use a low-friction default and must not become prerequisites for enjoying poker/social features.
- Later crime-oriented gameplay (including player crime, jail scenarios, weapons and drugs) is a possible post-launch expansion after the initial product has traction/revenue and potentially additional investors or partners. It is explicitly future/proposed scope, not approved launch scope. Each such expansion requires a separate creator decision and legal, platform-rating, safety, moderation and technical review.
- Keep systems modular, data-driven and independently activatable so future contributors can extend the game without forcing speculative features into the first release.


## 18. Lifestyle bundles, weekly bills and progression rewards
- Use a simple recurring **Lifestyle Package** rather than numerous separate player-managed bills. A package can bundle housing, phone service and utilities at a single transparent in-game price; vehicle/fuel/insurance may be separate optional services or later package components.
- Candidate package tiers: Starter (affordable apartment/basic phone/utilities), Comfortable (upgraded apartment/phone/utilities), Premium and Elite. These are examples for design exploration, not finalized names, contents or prices.
- Players can upgrade one component at a time or move to a higher package. The price of each tier must be balanced against reliable ordinary in-game earning opportunities.
- A weekly billing cadence is the current preferred concept, subject to economy testing. Clearly show the next due date, amount, included services and available balance.
- Daily login rewards and weekly streak rewards are desired retention features. The creator also wants active players recognized when they return for multiple play sessions in one day and when they spend several hours playing on a day they have free. Consider optional repeat-session milestones and sustained-play milestones for meaningful poker, social, event and city activity, not just app opens or idle time.
- The level/progress bar should advance in small, satisfying increments during normal play. Avoid excessive grind or making players spend hours or repeatedly log in each day just to preserve progress.
- Protect basic access: a missed login or missed streak must not cause eviction, loss of phone access, utility shutoff or exclusion from poker/social activities. Add reasonable streak grace/catch-up rules and a clear path to earn the basic lifestyle cost.
- Reward schedules should be transparent and tested against economy inflation/exploitation. Multiple sessions and longer play sessions can earn additional milestones, but do not require uninterrupted play, make rewards coercive or allow idle AFK farming. Players choosing shorter sessions must still make worthwhile progress, and the system should provide natural stopping points.
- Design for healthy voluntary engagement: no coercive multiple-daily-check-in requirement, artificial urgency, deceptive near-miss mechanics or punitive streak resets. Include natural stopping points and monitor player feedback and wellbeing alongside retention.
- Exact bundle contents, names, prices, billing day, grace period, reward values, streak length, activity eligibility, XP curve, level rewards and anti-exploit controls remain unresolved and require creator approval plus playtesting.


## 19. Away-state property care and return reminders
- The city may continue advancing an owned/rented player's home and vehicle care states while the player is offline. After a configurable period away, the apartment can visibly become neglected (dust, flies, roaches or other reversible signs of infestation/deterioration); a vehicle may become due for routine maintenance.
- This is an atmospheric re-engagement mechanic, not an asset-loss mechanic. No eviction, loss of apartment ownership, permanent vehicle damage, confiscation or lockout from poker/social play because of inactivity. Returning players need clear and reasonably affordable clean-up/maintenance actions.
- The creator wants players to want to return at least daily, but not to be forced to do so to protect essential possessions. Absence thresholds and deterioration stages are configurable and not yet finalized.
- At onboarding, offer optional email and SMS/text update subscriptions with clear channel-specific consent, purpose and expected frequency. Let players manage or withdraw preferences later.
- Social login (including Facebook login) is authentication, not notification consent. Only use social-platform notification features if separately supported by the platform and explicitly authorized by the player; linking a Facebook account alone does not authorize Facebook notifications.
- Send occasional, factual, friendly reminders such as an apartment-care notice or vehicle-maintenance reminder. Avoid alarmist/shaming copy and deceptive urgency.
- Notification delivery must support frequency caps, quiet hours, deduplication, channel preferences, unsubscribe/STOP handling for SMS, auditability and applicable privacy/messaging/carrier/platform requirements. Avoid revealing sensitive account/property details in lock-screen previews.
- Final thresholds, decay stages, restoration costs, reminder cadence, supported channels and consent language require creator approval and testing.


## 20. Advertising placements, monetization and delivery target
- Creator target: complete and launch a focused Hustle City release by **May 2027**, with a goal of at least **$10,000 monthly revenue**. Treat both as targets, not promises; create a milestone plan and forecast from actual audience, conversion and monetization assumptions.
- The release plan must prioritize a shippable poker-first social MVP; the full city vision remains modular follow-on scope.
- A small persistent bottom banner remains on for every player, including all paid membership tiers; the creator explicitly confirmed it is never removed and contributes ongoing revenue to fund in-game content and operations. Keep it unobtrusive and outside gameplay/controls. Refresh timing must follow the selected ad provider's policies and optimization. The proposed 10–15-second refresh is not approved; Google AdMob currently documents custom banner refresh at 30–150 seconds and recommends optimized refresh.
- Provide optional rewarded video at the bar when a player has depleted their poker chips, offering a disclosed, limited virtual-chip reward. Preserve non-ad ways to earn chips and return to play.
- Provide occasional opt-in reward doubling after selected activities/claims, not every action. Apply cooldowns, frequency caps and clear reward disclosure.
- Schedule short, non-rewarded in-app ad breaks at 15-minute active-session milestones: 15, 30, 45 and 60 minutes in the first hour, then every 15 active minutes thereafter (maximum four scheduled breaks per hour). These are predictable timing points. Show only at safe natural transitions; defer during poker hands, consequential table decisions, conversations, card trades, travel or other critical interactions. If an opportunity cannot be shown promptly, skip it rather than stacking missed ads. The creator wants dismissal available after approximately five seconds; verify selected provider/format support before implementation.
- Consider only sparse, context-appropriate casino ad opportunities (roughly one or two in a relevant visit/session was suggested), subject to legal, age-rating, gambling-advertising and platform review.
- Never interrupt a live poker hand or critical social interaction with forced advertising. Ads must not imply virtual chips are redeemable for cash.
- Do not create an ad-free membership entitlement for the bottom banner. It remains present for all membership tiers.
- Track impressions, fill, completion, eCPM, revenue per DAU, payer conversion, retention and complaints. Forecast gross and net revenue separately after ad-network share, store fees and taxes.
- Final provider, ad placement dimensions, refresh interval, chip reward, cooldowns, timed-ad triggers, the 15-minute milestone schedule and safe-transition/skip behavior, five-second dismissal support and eligibility rules remain unresolved. The bottom banner is confirmed permanent across all membership tiers.


## 21. Three-to-four-hour daily destination and cross-activity loop
- Creator target: design toward an average of **three to four hours of active daily play per active user**, validated through actual cohort analytics. This is a target, not a promise or mandatory minimum for individual players.
- Poker remains the core anchor, while the broader city gives players compelling reasons to stay and return: chip recovery/earning, bar hangouts, card trading, conversations, meeting friends, traveling between venues/districts, events, home/apartment furnishing and upgrades, vehicle/lifestyle progression, and ambient city discovery.
- Example regular-player journey: player runs low on poker chips; goes to the bar; trades cards, interacts with other players and socializes; continues other meaningful activities while waiting for a later eligible opportunity; chooses whether to watch a rewarded video for a disclosed virtual-chip reward or double an eligible activity reward; returns to poker when ready.
- Keep distinct ad formats and counters: persistent bottom banner (including paid members); up to four scheduled non-rewarded interstitial opportunities per active hour at 15-minute milestones; optional rewarded videos for chip recovery or selected reward doubling. Rewarded videos are opt-in and are not included in the four scheduled interstitial slots.
- The creator wants rewarded videos to provide attractive additional in-game earnings/rewards, including a longer rewarded-video option where supported. Actual reward amount, video duration, availability, caps, cooldowns and eligibility require provider review, economy balancing and creator approval. Do not promise a fixed duration, forced watch, or higher payout solely because an ad is longer; use only provider-served rewarded formats and clearly disclose the reward before opt-in.
- Chip recovery and progression must retain non-ad earning routes. Virtual chips and in-game currency are non-redeemable and must never be represented as cash.
- Do not create mandatory 30-minute waiting periods, idle farming, or ad-viewing loops. If a cooldown or timed opportunity is used, provide other meaningful activities and clear timing; no player should be trapped waiting to play poker.
- Measure average daily active hours alongside session-length distribution, activity diversity, social participation, progression, chip recovery source, rewarded-ad opt-in/completion, retention, complaints and healthy stopping behavior. Optimize for a compelling world and sustainable revenue—not maximum time-on-app at any cost.


## 22. Daily check-in, property/garage care, bills and event calendar
- Design a daily return dashboard/inbox that can surface four truthful, actionable categories: home/apartment care; garage and vehicle maintenance; weekly lifestyle package/bill status; and daily reward/progression claims.
- Reminder copy should be friendly and personal, e.g. “Hustle City is missing you. Your garage could use a little attention, and your apartment is ready for a quick refresh. Your weekly lifestyle package is coming due. Come back, collect your rewards, and see what's happening around the city.” Generate only notices supported by the player's current state; never fabricate an overdue bill, dirty home, maintenance need or unclaimed reward.
- A weekly bill reminder should state the actual amount, due date, package inclusions and fair ways to earn/pay. It is a prompt, not a threat. Missing a login or payment window must not evict a player, remove ownership, confiscate a car, permanently damage assets, shut off essential access or block poker/social play.
- Home upkeep and garage maintenance should be clear, low-friction and reasonably affordable. Offline deterioration is reversible; return care can restore the home/vehicle condition without punitive compounding costs.
- Daily rewards should be easy to understand and claim, with transparent progress toward weekly streaks/milestones and reasonable grace/catch-up. Do not make essential possessions dependent on daily attendance.
- Event calendar is a recurring community hub with stadium-scale parties/headline events and smaller venue concerts, club nights and gatherings. Include event details such as venue, start time, duration, activity type, host/performer, capacity/availability where relevant, RSVP/attendance and friend/crew attendance cues.
- Events should enable dancing, conversations, socializing, networking, group attendance and card trading where suitable. Provide appropriate player controls and moderation. Real-world contact exchange/off-platform networking must be mutual opt-in, privacy-aware and subject to block/report protections.
- Use push/email/SMS only when separately opted into and supported. Apply channel preferences, quiet hours, frequency caps, deduplication, unsubscribe and privacy-safe previews. In-game inbox reminders remain available as appropriate.


## 23. In-game phone: crew presence, invitations and social reach
- Add a “Who's online” view for friends and crew members, with presence controls (for example, visible to friends/crew, appear offline, or limited visibility). Show only information permitted by the target player's settings and relationship permissions.
- Add configurable crew/friend activity notifications, such as “Your crew is online,” “Your friend is available,” and “Your crew is hosting an event at the yacht club tonight.” Let players choose which people/groups trigger alerts and which channels receive them.
- Add an event invitation composer in the in-game phone. The host chooses an existing event or creates an invitation with venue, date/time and message; selects specific friends, a crew, or an authorized group; previews the invitation; and sends it through in-game messages.
- Add optional external share actions for SMS/text and email. The sender chooses the channel and recipient(s), reviews the message and confirms sending. Use only contact information already supplied/verified or explicitly selected with permission. Do not silently scan, upload or message the player's contacts.
- Support invitation status and responses (invited, accepted, declined, maybe), plus event updates/cancellations. Respect recipient notification preferences and invitation controls.
- Add contactability settings: who can send direct messages, invitations and crew/activity alerts. Blocking must prevent unwanted contact across supported channels; reporting and moderation must be accessible from messages/invitations.
- Apply spam controls: per-player send limits, duplicate detection, cooldowns, abuse monitoring and recipient opt-out. Do not allow bulk unsolicited SMS/email campaigns. Keep sender identity and event details clear, and do not expose phone numbers/email addresses to other players.
- Separate player-initiated event shares from Hustle City marketing/re-engagement notifications. Platform email/SMS notifications need channel-specific opt-in, quiet hours, frequency caps, unsubscribe and audit records; authentication/social login alone is not consent.
- Exact presence visibility defaults, audience rules, message retention, external delivery provider, SMS/email costs, consent wording and rate limits require creator approval and privacy/security review.


## 24. Phone-based transportation and automated scenic travel
- Add a Transportation area to the in-game phone, with service actions:
  - **Call my car:** choose an owned/authorized vehicle and request delivery to the player's location.
  - **Taxi/cab:** request an in-world cab pickup.
  - **Ride-hailing:** request an app-style in-world ride.
  - **Concierge:** arrange a premium car/chauffeur service.
  - **Private aircraft:** request an owned/authorized plane to be staged at the airport and prepared for departure, including fuel readiness.
- Show available service/vehicle, pickup and destination, estimated arrival/travel information where supported, price where applicable, and clear request/cancel/arrival states. Enforce ownership and permission distinctions: a player may only summon vehicles they own or have permission to use.
- Initial launch travel is **automated passenger mode**, not direct player steering. The selected car/cab/chauffeur vehicle follows a safe, predictable route using system-controlled navigation and traffic behavior.
- Make automated travel feel immersive: player is seated in/associated with the chosen vehicle, with a rotatable/orbit camera that can look around at city streets, districts, landmarks, skyline and passing scenery. Camera movement must not affect vehicle navigation.
- Use safe routing, traffic-aware movement and collision avoidance. Prevent random collisions and protect player-owned assets and balances from pathing/simulation defects. No damage charges or loss of a vehicle caused by an automated travel bug.
- Manual driving is outside initial launch scope unless the creator separately approves it after a dedicated feasibility and safety review. The automated travel approach is the approved initial direction.
- Define vehicle/aircraft staging, access permissions, airport/terminal flow, fuel state, service costs, travel duration, routing, camera controls, cancellation and recovery from interrupted sessions before implementation.


## 25. Parking, indoor garages and premium valet arrival
- Support two arrival paths:
  1. **Standard parking:** regular players arrive in their owned/authorized vehicle and park in an available designated space. Provide appropriate parking lots/structures and indoor or covered garages at destinations where the setting calls for them.
  2. **Valet/concierge arrival:** eligible players (through a qualifying paid service tier or earned in-game wealth) pull up to a designated drop-off point, exit at the entrance, and have an NPC valet/concierge take the vehicle to secure parking.
- Treat earned wealth and paid subscription/service eligibility as alternative possible routes to premium valet convenience; final thresholds, tier benefits and fees need creator approval. Basic ownership and standard parking must remain available without a subscription.
- Add indoor/covered parking garages to relevant properties and destinations: residential buildings, upscale venues, hotels/clubs and other suitable locations. Define parking slots, capacity and availability; handle full garages with a clear overflow/remote parking option.
- After valet handoff, maintain authoritative vehicle state: owner, authorized users/keys, current parking facility/slot, condition and availability. The car is not deleted or lost when the player enters the venue.
- Add phone/valet retrieval so the player can request the vehicle back at an approved pickup point. Enforce owner/key/permission checks for both valet drop-off and retrieval.
- NPC valet movement should follow safe controlled paths. No random collisions, vehicle damage, theft, loss or fees caused by valet/pathing simulation. A safe state transition may substitute for a fully simulated drive into the garage while retaining an appropriate arrival animation/feedback.
- Define parking/garage capacities, fees, eligibility, service coverage, retrieval time, vehicle state persistence and recovery from disconnects/session interruption before implementation.

 
## Universal entity IDs, catalog and inventory traceability
Hustle City requires a universal identity and traceability layer across the game economy and world. Every trackable entity receives a stable unique ID, including individual clothing pieces, cars, motorcycles, trucks, helicopters, private jets, boats, yachts, buildings, apartments, garages, businesses, food and drink products, cigars, cigarettes, cards, furniture, property, venues, menus and menu entries.

### Identity model
- Use separate IDs for a catalog definition/type and for an individually tracked instance. A clothing style or car, helicopter, private-jet, boat or yacht model is a catalog entity; each individually tracked garment, vehicle, aircraft or watercraft is an instance. A building/property is separately identified from each business operating inside it, and from its rooms, parking spaces or other trackable sub-assets where needed. A menu item definition is distinct from each stock/transaction/consumption record.
- IDs are immutable, unique, durable and never reassigned to another entity. Display names, descriptions, prices, owners, locations and other attributes are mutable metadata, not identity.
- Use typed entity namespaces or equivalent schema constraints to prevent collisions and preserve clear entity categories.
- Track ownership separately from possession/custody and access permission. A player may own a vehicle while another player has authorized keys; transfers must not accidentally change ownership.
- Keep current state plus auditable event history for creation, acquisition, sale, transfer, lending, reservation, use/consumption, location change, maintenance, retirement and administrative correction, as applicable.
- Businesses/venues have their own entity IDs. Buildings and properties have independent IDs, so ownership, tenancy and business occupancy can change without changing the building's identity. Their menus, menu versions, products, services and individual menu entries have their own IDs and relationships to the business. Food, drinks, cigars and cigarettes must be represented as explicit catalog records with relevant category, availability, price and regulatory/content metadata.
- Inventory records should support quantities and lot/batch tracking where individual unit identity is unnecessary, while unique assets and collectibles receive individual instance IDs. Do not create millions of unit records for fungible stock unless there is a real traceability requirement.
- Every transaction should reference the relevant player/account, item or catalog/instance ID, quantity, counterparty/business, timestamp, price/currency and resulting state. Use append-only or otherwise auditable transaction/event records with controlled correction paths.

### Population growth and card-supply management
- Player population and card inventory are distinct datasets with an explicit configurable relationship, not a hard-coded one-card-per-player assumption.
- The system must support growth from an initial card pool to 100,000+ players and beyond by issuing additional uniquely identified card instances and, if the creator approves, introducing additional values, variants, rarities or sets.
- Define supply policies per card family/game mode: initial print/issue quantity, reserve pool, issuance trigger, release batch size, rarity/value distribution, duplicate rules, replacement policy and maximum/target circulation.
- Maintain reconciled counts for total created, in circulation, unissued/available, reserved, held by players, held by businesses/system accounts, consumed/retired and invalidated. Card movement between players, tables, inventory, trades and system pools must update the ledger exactly once.
- Never silently alter the identity or value of an existing card to inflate supply. New supply should be new instances; new values/variants should be new catalog definitions and be introduced through an approved, versioned content/economy change.
- Add anti-duplication safeguards, idempotent transaction handling, concurrency-safe issuance, audit logs and reconciliation alerts. A card cannot be issued twice or simultaneously owned by multiple players.
- Exact supply ratios, issuance thresholds, new card values, rarity and distribution remain unresolved and require creator approval plus economy simulation.

### Implementation boundary
This is an approved product requirement for the architecture and backlog, not a claim that the registry or card issuance system is already implemented. The exact database schema, ID encoding, partitioning/indexing, public-facing reference format and operational tooling are technical design tasks.


## 26. World clock, day/night cycle and live weather
### Player-facing clock and conditions
- Provide a persistent HUD clock showing the current **in-game** time, with an unambiguous in-game label. Also expose current local in-game weather for the player's district/location.
- The clock and weather should be easy to check without opening a deep menu; the phone/map may provide expanded detail.
- In multiplayer, players sharing a world instance see the same authoritative world time and consistent weather state for the same location. Do not let each client independently invent a different time or weather condition.
### Time-of-day presentation
- Support dawn, sunrise, morning, noon, afternoon, golden hour, sunset, dusk and night, with smooth transitions to sun angle, sky, ambient light, shadows, reflections, street/building/vehicle lights and venue lighting.
- NPC routines, traffic patterns, venue activity, event schedules and city ambience may respond to the world clock. These responses should be coordinated with existing NPC schedules and event systems.
### Weather simulation
- Support climate-appropriate changing conditions including sunshine, cloud cover, humid haze, rain/showers, thunderstorms and fog. Conditions may vary by district or region where appropriate, rather than forcing one identical weather state across the entire map.
- Show a concise current-condition label/icon; optionally expose temperature, wind, precipitation intensity and forecast information if useful and supported.
- Weather can influence environmental presentation, visibility, ambient audio, wet-road reflections and NPC/venue behavior. It must not introduce unfair driving danger, random crashes, damage, asset loss or financial penalties.
### Decisions required before implementation
- Choose world-day duration and time acceleration, calendar/date rules, pause/maintenance behavior, server-authoritative synchronization and handling of players in different world instances.
- Define weather-region boundaries, transition rates, forecast horizon/accuracy, seasonal behavior and whether/when major weather events are scripted.
- Ensure clock, lighting and weather remain consistent across clients and recover correctly after reconnects or server restarts.


## 27. Neighborhood lifestyle spaces and ambient city activity
### Residential and waterfront social spaces
- Build distinct neighborhood identities with appropriate architecture, landscaping, amenities and social energy. Upscale neighborhoods should feel lived-in and aspirational rather than functioning only as backdrops.
- Include rooftop terraces, rooftop lounges, private balconies, back porches, patios and waterfront decks. Some waterfront homes, restaurants and venues should have intimate private/semi-private dining decks close to the water, with tables, comfortable seating, lighting and scenic views.
- Let players use these spaces to sit, eat meals, relax, talk, socialize, invite friends and host small gatherings. Support shared dining and conversation interactions; gate access through ownership, tenancy, venue access or invitations as appropriate.
- Include rooftop social spaces with skyline views and suitable amenities (for example, lounges or pools where the location calls for them). Preserve quieter residential spaces such as a back porch for dinner and conversation.
### Visual identity and ambient traffic
- Use palm trees and deliberate landscaping throughout appropriate districts. Give major buildings, towers, clubs, restaurants and landmarks recognizable names and legible world signage.
- Keep the player's location legible: display district name and, when useful, the named building, venue or nearby landmark in the HUD/map/location panel.
- Populate streets and venues with premium vehicles and visible fashion/jewelry as appropriate to the neighborhood, NPC, player character and venue. Expensive cars and jewelry contribute to the city's lifestyle identity but should remain coherent with district character and character customization/economy systems.
- Add occasional ambient aircraft flybys: distant commercial/private planes on believable routes and helicopters passing over the city. Vary timing, altitude, direction and frequency to avoid obvious loops. These ambient aircraft are distinct from player-owned aircraft, aircraft services and interactive flight systems.
### Seasonal and cold-weather presentation
- Expand weather beyond warm coastal conditions to include cold-weather periods and occasional snow where appropriate to the world calendar and district climate. The creator explicitly wants the possibility of snow at some point.
- Snow presentation may include accumulation, frosted surfaces, altered ambience and appropriate NPC clothing/behavior where supported. Define whether snow is citywide, district-specific or a rare special weather event.
- Maintain safe predictable automated transportation and pedestrian movement in cold/snow conditions. Weather must not cause random crashes, damage, asset loss or financial penalties.
- Decide season/calendar model, cold-weather duration, snow frequency and accumulation behavior during environment design; do not invent fixed dates or frequency yet.


## NPC and player wardrobe depth
Hustle City requires a substantial fashion system for the named Sim population and player avatars. Each Sim should have a wardrobe supporting approximately 30 days of varied outfits, using a scalable mix of modular garments, accessories, uniforms and outfit presets. Outfit selection reflects the individual's identity, job, income/lifestyle, personality, neighborhood, activity, venue, weather and season.

Venue styles must be distinct: casino/shuffle-club staff wear coordinated upscale role uniforms; adult casino and nightlife guests can wear glamorous, sexy evening fashion including fitted/short dresses and skirts, low-cut/open-neckline styles, heels and statement jewelry; beaches support swimwear and resortwear; restaurants, bars, rooftops, yacht clubs and concerts have appropriate casual-to-formal ranges; neighborhood streetwear reflects local style without stereotypes. Work uniforms differ from off-duty clothing. Rain, heat, cold and snow influence wardrobe choices. Keep all designs within the approved content rating and platform rules; never sexualize minors or depict explicit nudity. P08 owns the wardrobe system and coordinates with P03/P04/P05/P09/P10/P12. Exact catalog counts, asset budgets and repetition windows remain open.


## Initial 10,000-person named Sim population
The first planned population roster is 10,000 individually named Sims/NPCs, managed as a versioned cohort and expanded in additional batches as needed. The starting composition target is 5,000 men and 5,000 women, with broad variation in ages, racial/ethnic backgrounds, skin tones, body types, personal style/swagger, personalities, jobs and lifestyles. Every person must have a stable unique ID, name, occupation/function, profile, schedule, home/work anchors and wardrobe. Exact age bands and demographic percentages beyond the stated starting gender split require creator review. Population diversity must be respectful and individual: never infer personality, intelligence, morality, criminality, income or job qualification from race, ethnicity, skin tone, gender or age. Distribute people across districts, households, workplaces, shifts, routes and venues. Maintain continuity across roster updates and player sessions; new batches must not overwrite existing identities. The 10,000 roster is not 10,000 simultaneous full-detail AI processes.


## Memorable relationship NPCs
Meaningful recurring NPCs in casinos, clubs, restaurants, bars, hotels, venues and services must be recognizable individuals with persistent identities and player-specific relationship continuity. Examples include the valet who parks a regular guest's car, the bartender who remembers a usual order, and the casino host who remembers appropriate preferences and prior visits. Familiarity grows naturally over repeated encounters. NPCs can notice relevant changes—such as a different authorized vehicle arriving—and make accurate, personality-appropriate conversation. They must not fabricate memories or reveal another player's private information. NPCs also maintain their own lives, work shifts and relationships. Relationship memory is scoped to relevant gameplay facts, with retention/correction/deletion controls and responsible-gambling safeguards. Implementation details for storage and memory tiers remain open.


## Shared social world and off-duty NPC lives
Named NPCs are people across the entire city, not fixtures attached to their workplaces. A bartender remains the same recognizable person off shift and may be encountered on the street, at shops, beaches, clubs, concerts, neighborhood gatherings or player-hosted yacht parties. NPCs have off-duty schedules, interests, errands, friends and social lives, and they interact with one another independently of players. Player-hosted gatherings can include both invited player friends/crew and appropriate NPC guests, with guests distinguished from staff and ambient attendees. Recognition and relationship continuity follow the NPC across locations and shared events. Event attendance respects schedules, relationships, context and capacity.


## Player-specific relationships, dating and outings
NPC relationships are individual to each player. The same named NPC can be an acquaintance, friend or dating partner to different players, based on their separate histories. Friendships and dating develop through repeated visits, conversations, meals, events and invitations. NPCs retain agency and can accept, decline, suggest another time or set boundaries. Players can invite NPCs to lunch/dinner, comedy shows, concerts, clubs, beach parties, yacht parties and other social activities. Shared history is private to the relevant player-NPC relationship. Include consent, age-appropriate restrictions, rejection handling and anti-harassment safeguards.

## Jokes on You Comedy Club — proposed venue concept
Working name: **Jokes on You Comedy Club** (not yet locked as final brand). Envision a date-night/social destination with paid admission, scheduled comedy performances, multiple table and seating options, food and drink service, NPC and player guests, and a designated cigar-lounge area. Support couples, groups and solo visitors. Any alcohol/cigar representation must follow the approved content rating, age-gating, platform and regional rules.

## Scalable casino buildings and future city brands
The initial casino destinations are Shuffle Club and Hustle Towers. Shuffle Club is intended as a substantial multi-floor flagship with multiple poker rooms, tables and supporting social/service spaces; Hustle Towers is the second initial casino. Buildings must be architected for expandable floors/rooms, table instances, concurrent capacity, staffing, wayfinding, room discovery and overflow. Final dimensions, floor counts, poker-room counts and capacity targets remain unresolved pending performance/capacity planning. Future cities can have distinct casino names and identities; do not simply clone the two initial brands everywhere.

## Procedural naming and automated city population
Create a reusable naming framework for cities, casinos, venues and businesses. Generated names should fit the world's naming principles and local city/region flavor, remain distinguishable, avoid duplicates and unsuitable/offensive or trademark-confusing results, and be stable once assigned. Generated businesses/venues receive stable IDs, type, city/district location, brand/name metadata, staffing requirements and NPC population/activity schedules. The pipeline is repeatable, seedable, auditable and creator-overrideable, so expansion does not require manually naming and populating every new location. Exact name grammar, approval rules and generation mechanics remain open.


## 19. Persistent NPC familiarity, recognition and trust
- Every meaningful recurring NPC interaction can build persistent familiarity between that specific player and that specific NPC. This applies to everyday workers and service characters as well as social/dating characters.
- Familiarity progression and trust are separate: familiarity reflects repeated meaningful encounters and recognition; trust is a distinct visible meter/bar earned through behavior and shared experiences.
- NPC traits and player presentation/social traits (including height, style/swagger and conversation approach) influence contextual reactions. NPC mood, confidence, social awareness, preferences, relationship status and boundaries remain individual and authoritative.
- NPCs recognize returning players from verified game history, and players can recognize recurring NPCs through stable identity and schedule continuity. Relationship records are per player-NPC pair.
- Higher trust may support greater openness, but does not guarantee attraction, romance, consent, access or acceptance. Familiarity can increase without trust.
- See the canonical [Sims / MPC / NPC Simulation Framework](../knowledge-library/frameworks/SIMS_MPC_NPC_FRAMEWORK.md), sections 16–20.

## 20. Persistent shift rosters and recurring service staff
- Staff roles use stable named NPC rosters and predictable schedules. Three staggered eight-hour shifts are the creator-approved example for 24-hour coverage where needed; each business can configure hours, staffing, overlap, breaks and days off.
- Different named workers can cover the same valet, parking, bar, concierge or other service role at different times. Players can learn who is commonly on duty at familiar in-game times.
- Shift handoffs preserve active service records but do not transfer one worker's personal familiarity, trust or memories to another worker.
- NPCs retain their own identity and relationships across shift changes, off-duty activities, venues and player sessions.


## 21. Reciprocal NPC/player profiles and social recognition UI
- Approaching or interacting with a named NPC can surface a compact profile/relationship panel alongside conversation, with an optional fuller profile view.
- The player sees the NPC's stable name and role plus their own player-specific familiarity level and trust bar with that NPC.
- NPC recognition may use approved player-visible in-game fields: display name, level, stars/rank, playtime/tenure and visit frequency at the relevant venue.
- NPC greetings and interaction style adapt to verified context such as first visit, returning guest, venue regular and prior shared interactions.
- NPCs may only use information made visible to them by game rules. Private/account information and other players' relationship histories remain inaccessible.
- Level, stars and playtime are contextual cues only; they do not prove trustworthiness, wealth, consent, authority, attraction or entitlement.
- See [Sims / MPC / NPC Simulation Framework](../knowledge-library/frameworks/SIMS_MPC_NPC_FRAMEWORK.md), section 21.


## 22. Conversation-earned NPC trust and ongoing dialogue
- Trust should primarily grow through meaningful conversations and interactions, not passive proximity or repetitive button presses.
- After a practical interaction—such as asking Marcus the parking attendant to park a vehicle—the player can choose to continue talking with that same NPC.
- Available topics can include general conversation, family/work, shared interests, personal questions when appropriate, and player updates. NPCs respond according to personality, mood, workload, familiarity, trust, memory and boundaries; they may answer, decline or redirect.
- A meaningful positive conversation may gradually raise trust (illustratively 63, 64, 65). Listening, empathy, relevant follow-ups and respectful reciprocal sharing matter. Spam, empty repetition, intrusive questions or disrespect must not farm trust and may leave it unchanged or reduce it.
- NPCs can initiate conversations and share appropriate life updates grounded in their own persistent lives and actual shared history. Trust is not familiarity, attraction, romance, consent or entitlement.

## 23. NPC-originated social gatherings and invitations
- NPCs and NPC social circles should be active organizers/hosts of city social life, including yacht parties, street-car meets/parties, club parties and other gatherings.
- NPC hosts choose events and guests in ways consistent with their personality, interests, social network, resources, schedule and context. They can invite players, including new players, through credible social pathways; invitations are not reserved only for established high-trust players or existing crews.
- Support event planning, venue/time selection, guest lists, invitations and responses, attendance, in-event social interactions and persistent post-event relationship outcomes.
- NPCs have agency throughout: they can host, invite, accept, decline, defer, attend, socialize and leave according to their own state. Player-hosted parties remain a separate supported path.
- NPC-hosted events must feel like genuine social activity generated by the city's people, not merely player-owned instances populated with decorative NPCs. Event capacities, schedules, content restrictions and safety rules remain to be specified.
- See [Sims / MPC / NPC Simulation Framework](../knowledge-library/frameworks/SIMS_MPC_NPC_FRAMEWORK.md), section 22.


## 24. Recognition versus trust progression; flexible conversation input
- Recognition/familiarity may increase through meaningful repeated encounters when the NPC plausibly notices the player. Trust primarily grows through actual meaningful, reciprocal conversations.
- A player who uses valet parking and leaves without talking may become more recognizable to Marcus, but should not automatically gain trust from the service transaction.
- Repeated venue visits and idle proximity are not substitutes for conversation and do not automatically build trust.
- Conversations can use pre-selected dialogue boxes or player-typed messages. Both routes use the same contextual evaluation of meaning, relevance, respect, reciprocity, NPC response and boundaries.
- This applies to conversations with service NPCs and social interactions such as talking with someone at a bar. Message count alone never determines trust.
- Recognition and trust must remain independently tracked and may progress differently.
- See [Sims / MPC / NPC Simulation Framework](../knowledge-library/frameworks/SIMS_MPC_NPC_FRAMEWORK.md), section 23.


## 25. Player-to-player recognition, relationships and visible trade assets
- Extend the recognition/profile model to player-to-player encounters. An inspected player profile can show display name, rank, level, stars, neighborhood and crew representation.
- Players build pair-specific familiarity and trust. Recognition can grow through meaningful repeated encounters; trust primarily grows through actual conversation and reciprocal interaction. Repeated sightings alone do not automatically build trust.
- Player conversations support both pre-selected dialogue options and typed messages. Trust depends on interaction quality and both participants' responses; message count is not a progression shortcut.
- Profile inspection can show in-game cards and keys the owner makes visible, distinguishing owned assets from those explicitly available for trade. Players can initiate offers for eligible assets, but viewing does not reserve or transfer anything; transfers require explicit confirmation.
- Keep pair-specific relationship history private unless a defined game feature exposes a permitted summary. Do not expose hidden inventory, protected assets, private data or real account credentials.
- See [Sims / MPC / NPC Simulation Framework](../knowledge-library/frameworks/SIMS_MPC_NPC_FRAMEWORK.md), section 24.


## 26. Full player status, ownership and collection profile
- Player inspection should expose an expanded in-game profile with display name, online status, rank, level, stars, neighborhood/home district and crew affiliation.
- Include ownership counts for houses/homes, total properties, vehicles and car lots/dealerships. Keep house/property categories distinct and do not confuse car-lot ownership with vehicle ownership. Where permitted, let viewers inspect owned-item lists as well as totals.
- Show card collections and in-game keys, including item-level details the owner makes visible and a clear designation of items currently available for trade.
- Use authoritative live ownership/inventory records so counts and item lists stay accurate after transactions. Viewing a profile does not reserve or transfer an item; trades require explicit confirmation and eligibility/ownership validation.
- Provide a compact profile summary with expanded category views. Respect owner visibility settings and protect exact home addresses, private account data, credentials and hidden inventory. Status and wealth indicators do not automatically establish trust.
- See [Sims / MPC / NPC Simulation Framework](../knowledge-library/frameworks/SIMS_MPC_NPC_FRAMEWORK.md), section 25.


## 27. Profile-driven player choice and social progression
- Players can use visible profile details—level, rank, stars, neighborhood, crew, homes/properties, vehicles, travel/lifestyle and collections—to decide whom they want to approach, socialize with, trade with or do business with.
- Some players may seek peers with similar progression or assets; others may choose to meet, mentor or do business with newer players. Optional filters and comparisons support discovery but do not impose universal wealth/rank gates.
- Meaningful, reciprocal communication can contribute to experience/star progression. Do not reward spam, empty messages, repeated low-value exchanges or farming. Keep earned progression separate from pair-specific trust/familiarity, consent and trade acceptance.
- Real-money progression was mentioned only as an unfinished possibility; no paid status/level/star advancement or pay-to-win mechanic is approved until separately clarified.
- See [Sims / MPC / NPC Simulation Framework](../knowledge-library/frameworks/SIMS_MPC_NPC_FRAMEWORK.md), section 26.


## 28. Tap-to-inspect profiles and social actions in the live scene
- Players can tap a visible NPC or player character on the touchscreen to open a compact portrait/profile pop-up showing approved profile details and stats.
- Include a direct Chat action on the pop-up. Where the scene supports it, also offer **Invite to sit with me** and **Ask to join their group**.
- Use clear target selection in crowded scenes and keep the live scene visible where practical. Proximity can assist selection, but mere proximity must not trigger a social action.
- Invitations are requests: the recipient or relevant group can accept, decline or defer. Respect seating availability, current activity, group context, privacy, blocks, boundaries and moderation rules. No forced movement or automatic group entry.
- Support both NPC and player targets using their respective conversation and agency systems. See [Sims / MPC / NPC Simulation Framework](../knowledge-library/frameworks/SIMS_MPC_NPC_FRAMEWORK.md), section 27.


## 29. Roaming social discovery and collectible hunts
- Tapping and inspecting people while roaming populated venues is a core everyday gameplay loop. Players can rapidly inspect visible people, learn their permitted in-game identity/profile details (including game age), and choose whom to approach.
- Contextual profile actions include chat, invite to sit, invite for a drink, invite for a meal and ask to join a group, where the venue and social context support them. Recipients retain the ability to accept, decline or defer.
- Trading cards create a purposeful discovery loop: a player seeking a specific missing card can inspect people in the room to discover who owns it and, when disclosed, how many copies they have.
- Clearly distinguish owned cards, duplicates, cards listed for trade and cards not offered. An extra copy is not automatically tradable; the owner controls listings. Discovery can lead to chat and negotiation, but transfers require explicit trade confirmation and validation.
- Keep profile inspection quick and player-directed, without arbitrary friction. Respect privacy, blocks, moderation and recipient agency. Profile inspection alone does not increase trust/familiarity.
- See [Sims / MPC / NPC Simulation Framework](../knowledge-library/frameworks/SIMS_MPC_NPC_FRAMEWORK.md), section 28.


## 30. Tap-to-identify and cross-platform player interaction
- The default live scene should not display permanent floating name labels above every character. Players tap/select a person to reveal their portrait, name and permitted profile details in the compact in-world pop-up.
- Continue the same direct actions from the pop-up: chat, invite to sit, invite for a drink or meal, and ask to join a group when appropriate.
- Tablet is the primary design target, with phone and PC support and possible future PlayStation/Xbox support. Phone landscape/horizontal presentation is the current direction to evaluate.
- Use one shared interaction model with adaptive layouts and input: touch for tablet/phone, mouse/keyboard for PC, and controller navigation for future consoles.
- Preserve readable profiles, usable touch targets, clear selection feedback in crowds and the live scene context. Do not simply shrink the tablet UI or infer selection from proximity.
- Exact orientation rules, responsive breakpoints, accessibility settings and console control mapping remain open implementation details.
- See [Sims / MPC / NPC Simulation Framework](../knowledge-library/frameworks/SIMS_MPC_NPC_FRAMEWORK.md), section 30.

## 31. Full inspectable profiles for Sims/NPCs
- Named Sims/NPCs should have full tap-to-inspect profiles, parallel in depth to player profiles. Show name, in-world age, neighborhood/residential information, occupation/workplace, workdays, shift hours, days off and supported ownership/asset details.
- Example: Ebony works at the bar Monday–Friday, 9 AM–5 PM, with Saturday/Sunday off. Individual schedules are persistent and vary by person and employer.
- Track each Sim's city/game tenure and stable population cohort (first, second, third 10,000-person batch, etc.). Keep cohort provenance, introduction/tenure and in-world age as separate fields. Cohort does not define identity, rank or quality.
- Supported assets may include homes, properties, vehicles, car lots/businesses and other possessions, backed by authoritative ownership records rather than invented profile flavor.
- Use the tap-to-identify profile pop-up and expanded profile view; no permanent floating name tags. Keep private residential coordinates and internal simulation data out of the player-facing view.
- Profiles should reflect changes to work, schedule, residence and ownership while preserving the Sim's stable identity.
- See [Sims / MPC / NPC Simulation Framework](../knowledge-library/frameworks/SIMS_MPC_NPC_FRAMEWORK.md), section 31.
