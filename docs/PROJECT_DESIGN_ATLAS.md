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
- Daily login rewards and weekly streak rewards are desired retention features. Meaningful poker, social, event and city activities can also grant Hustle Money and XP.
- The level/progress bar should advance in small, satisfying increments during normal play. Avoid excessive grind or making players spend hours or repeatedly log in each day just to preserve progress.
- Protect basic access: a missed login or missed streak must not cause eviction, loss of phone access, utility shutoff or exclusion from poker/social activities. Add reasonable streak grace/catch-up rules and a clear path to earn the basic lifestyle cost.
- Reward schedules should be transparent, capped and tested against economy inflation/exploitation. Do not reward idle AFK time as if it were meaningful play, and do not create uncapped playtime incentives.
- Design for healthy voluntary engagement: no coercive multiple-daily-check-in requirement, artificial urgency, deceptive near-miss mechanics or punitive streak resets. Include natural stopping points and monitor player feedback and wellbeing alongside retention.
- Exact bundle contents, names, prices, billing day, grace period, reward values, streak length, activity eligibility, XP curve, level rewards and anti-exploit controls remain unresolved and require creator approval plus playtesting.
