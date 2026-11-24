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
Hustle City requires a universal identity and traceability layer across the game economy and world. Every trackable entity receives a stable unique ID, including individual clothing pieces, cars, businesses, food and drink products, cigars, cigarettes, cards, furniture, property, venues, menus and menu entries.

### Identity model
- Use separate IDs for a catalog definition/type and for an individually tracked instance. A clothing style or car model is a catalog entity; each individually owned garment or vehicle is an instance. A menu item definition is distinct from each stock/transaction/consumption record.
- IDs are immutable, unique, durable and never reassigned to another entity. Display names, descriptions, prices, owners, locations and other attributes are mutable metadata, not identity.
- Use typed entity namespaces or equivalent schema constraints to prevent collisions and preserve clear entity categories.
- Track ownership separately from possession/custody and access permission. A player may own a vehicle while another player has authorized keys; transfers must not accidentally change ownership.
- Keep current state plus auditable event history for creation, acquisition, sale, transfer, lending, reservation, use/consumption, location change, maintenance, retirement and administrative correction, as applicable.
- Businesses/venues have their own entity IDs. Their menus, menu versions, products, services and individual menu entries have their own IDs and relationships to the business. Food, drinks, cigars and cigarettes must be represented as explicit catalog records with relevant category, availability, price and regulatory/content metadata.
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
