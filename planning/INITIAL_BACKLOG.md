# Initial Backlog

## P0 — Studio foundation
- [ ] Confirm repository as canonical Hustle City source of truth.
- [ ] Review/approve agent catalog and communication protocol.
- [ ] Capture any existing SAM/n8n workflow exports and preserve current versions.
- [ ] Confirm n8n version, hosting and installed nodes.
- [ ] Define Godot version and project conventions.
- [ ] Define world coordinate system, scale and asset naming.
- [ ] Create model registry and evaluate hardware when available.

## P1 — Shared interfaces
- [ ] Character rig/scale contract.
- [ ] Building/door/interaction anchor contract.
- [ ] Vehicle/seat/boarding contract.
- [ ] Road/lane/intersection contract.
- [ ] Transit station/platform contract.
- [ ] NPC live-state query contract.
- [ ] QA scenario and bug report format.
- [ ] Define player status/rank presentation interfaces and progression data contract from the creator-approved 100-level rank framework.
- [ ] Define separate career-progression and star/social-recognition data contracts.

## P2 — First vertical slice
- [ ] One city block with roads, sidewalks and one building.
- [ ] One player character with walking and interaction.
- [ ] One enterable venue with usable interior.
- [ ] NPCs with safe navigation and simple schedules.
- [ ] One automated vehicle route with safe stops.
- [ ] Player Shell prototype.
- [ ] Automated tests for stuck state, doors, collisions and recovery.

## P3 — Player progression and recognition
- [ ] Implement and validate the creator-approved 100-level player status ladder and its ten prestige families.
- [ ] Finalize the exact ten descriptor labels and their level mapping.
- [ ] Design post-Level-100 career prestige/reset progression, beginning with the proposed Hustler Platinum I naming direction.
- [ ] Build activity-based career progression that can recognize daily logins, poker wins, casino wins, other game victories, and eligible world/social activities.
- [ ] Design a separate star-points/star-rank system earned through eligible NPC and real-player interactions and other qualifying city activities.
- [ ] Establish configurable star-point awards for individual actions, including initiating street conversations, meaningful NPC/player interactions, adding friends, trading cards, and eligible poker-table chip purchases/transactions.
- [ ] Implement the proposed first 100 street-oriented star-rank titles as a working naming ladder, with a progression architecture expandable beyond Rank 100 to 1,000+.
- [ ] Define XP and star-point thresholds, pacing, rewards, daily limits, anti-exploit protections, and any unlock behavior separately from the approved rank-name structure.


## P4 — Lifestyle services, vehicles and in-world phone
- [ ] Specify a low-friction cost-of-living model covering housing, vehicle ownership/financing, insurance, fuel, phone service and optional maintenance; explicitly prevent routine bills from becoming a second job.
- [ ] Evaluate a bundled recurring lifestyle payment as the default, with itemized expense detail as an optional design path; creator approval required before prices, cadence or consequences are locked.
- [ ] Define rent-versus-own housing states and outright-purchase-versus-financing vehicle states without making either mandatory for core social/poker participation.
- [ ] Define vehicle insurance scope and protect players from financial/asset penalties caused by simulation defects.
- [ ] Specify safe NPC traffic behavior, collision avoidance, collision recovery and regression tests for intersections, lane changes, pedestrian crossings and congestion.
- [ ] Design an in-world cellphone prop and pull-out/look-at interaction that opens a diegetic phone UI while the player remains in the world.
- [ ] Connect phone messaging to player contacts/conversations, notifications, delivery state and social privacy/block/report enforcement.
- [ ] Define optional voice/calling capability separately; do not assume it is part of the first phone implementation.


## P5 — Launch product focus and expansion readiness
- [ ] Define and protect the initial product as a poker-first multiplayer social activity game; prioritize player acquisition, retention, community and sustainable revenue.
- [ ] Lock launch exclusions: no player robbery/theft, player-directed crime, weapons, player arrests/jail, player death or player hospital/medical consequence loops; no punitive player-targeted law-enforcement gameplay.
- [ ] Keep police, fire, ambulance, arrests, jail and medical emergencies as NPC-only ambient simulation at launch, with only safe/friendly contextual authority interactions for players (for example, a yacht-party noise reminder).
- [ ] Ensure NPC ambient incidents never silently turn into player crime, arrest, death or medical systems.
- [ ] Build modular activation boundaries and documentation so later systems can be introduced without rebuilding the social/poker foundation.
- [ ] Treat crime-oriented player gameplay, jail scenarios, weapons and drugs as possible post-launch proposals only; require separate creator approval plus legal, platform-rating, safety, moderation and technical review before specification or implementation.
- [ ] Prepare concise architecture/product documentation that future investors, partners and development contributors can understand without changing the approved launch scope.


## P6 — Lifestyle package economy and healthy engagement loop
- [ ] Design a single recurring Lifestyle Package that can bundle housing, phone service and utilities, with transparent weekly pricing as the leading candidate.
- [ ] Prototype candidate Starter, Comfortable, Premium and Elite package tiers; define contents and allow component-by-component upgrades as a design option.
- [ ] Balance every package against realistic in-game earning opportunities; basic housing/phone/utilities must not require real-money purchases.
- [ ] Define billing UI with package contents, price, due date, payment status and clear earning options.
- [ ] Define daily login rewards and weekly streak rewards with transparent schedules, reasonable safeguards, grace/catch-up rules and no punitive loss of essential services.
- [ ] Design optional repeat-session and sustained-meaningful-play milestones so players who choose to return multiple times in one day or play for several hours feel recognized, without requiring uninterrupted sessions, rewarding idle AFK time or making shorter sessions feel pointless.
- [ ] Award XP and in-game currency for meaningful poker, social, event and city activities; avoid idle-time farming and repetitive check-in exploits.
- [ ] Tune incremental progress-bar feedback and level pacing to feel rewarding without excessive grinding, forced multiple-daily logins or prolonged sessions.
- [ ] Add economy simulations for income, weekly package costs, upgrades, sinks, inflation and new-player affordability.
- [ ] Add healthy-engagement metrics and player-feedback checks alongside retention metrics; prohibit deceptive urgency, coercive streak loss and uncapped playtime incentives.
- [ ] Obtain creator approval for package tiers/prices, weekly billing rules, rewards, streak policy, XP curves and upgrade costs before implementation.

- [ ] Design reversible offline/away-state apartment neglect visuals (e.g. dust, flies/roaches) and vehicle maintenance-due states after creator-approved absence thresholds; never evict players or permanently damage/remove assets due to inactivity.
- [ ] Define clear, affordable return-to-care actions for cleaning/restoring an apartment and servicing a vehicle, without blocking poker/social access.
- [ ] Add onboarding opt-ins for email and SMS/text updates, with separate explicit consent, disclosed purpose/frequency, editable preferences and straightforward unsubscribe/STOP handling.
- [ ] Treat social login (including Facebook) as authentication only; require separate supported permission/consent for any social-platform notifications.
- [ ] Build a low-frequency re-engagement notification service with quiet hours, frequency caps, deduplication, privacy-safe message previews, delivery audit and channel preference enforcement.
- [ ] Define absence thresholds, deterioration stages, maintenance timing, restoration costs, reminder cadence and approved message templates with the creator before implementation.


## P7 — May 2027 MVP delivery and advertising revenue
- [ ] Build a critical-path milestone plan targeting a focused, playable Hustle City launch by May 2027; separate MVP blockers from post-launch world expansion.
- [ ] Create a $10,000/month revenue model with explicit assumptions for DAU/MAU, impressions, rewarded-video opt-in/completion, eCPM, payer conversion, average payer spend, store/ad fees and taxes.
- [ ] Implement a persistent, unobtrusive bottom banner for every player, including all paid membership tiers; it is never removed by membership and helps fund in-game content/operations. Ensure it does not cover gameplay or controls and respects provider policy.
- [ ] Validate banner refresh rules with the selected ad provider. Do not implement the proposed 10–15-second refresh unless explicitly permitted; AdMob's documented custom refresh range is 30–150 seconds and it recommends optimized refresh.
- [ ] Design an optional rewarded-video chip recovery offer at the bar when a player runs out of poker chips, with a clear reward, frequency cap and non-ad earning alternative.
- [ ] Design predictable short non-rewarded in-app ad breaks at 15, 30, 45 and 60 minutes of active play, then every 15 active minutes (maximum four per hour); show only at safe natural transitions and skip missed opportunities rather than stacking them.
- [ ] Verify whether the selected ad format/provider supports a close option after approximately five seconds, as requested by the creator.
- [ ] Validate the desired close-after-about-five-seconds behavior against actual provider/creative capabilities; do not promise or implement it unless the selected format supports it.
- [ ] Design occasional opt-in double-reward videos for selected activities/claims, with cooldowns and no prompt on every action.
- [ ] Review any casino-context advertising for age-rating, gambling-advertising, legal and platform compliance; do not imply virtual chips have cash value or are redeemable.
- [ ] Prevent forced ads during poker hands, critical decisions, conversations or other key gameplay.
- [ ] Instrument ad impressions, viewability, fill, opt-in/completion, eCPM, revenue per DAU, retention and player complaints; compare actual results with the revenue model.
- [ ] Ensure no membership tier removes the persistent bottom banner; all tiers retain it as a permanent revenue placement.
- [ ] Obtain creator approval for ad provider, placements, refresh timing, reward amounts, cooldowns, frequency caps and monetization mix before production rollout.


## P8 — Three-to-four-hour daily destination and monetization loop
- [ ] Design toward the creator's target of an average of 3–4 hours of active daily play per active user; validate by cohort analytics rather than assuming every player will reach it.
- [ ] Build a connected activity portfolio around poker: chip earning/recovery, bar socializing, card trading, player conversations/meeting people, travel between venues/districts, events, home/apartment furnishing and upgrades, vehicle/lifestyle progression, and city discovery.
- [ ] Map several natural player journeys that move between poker, social venues, card trading, travel, events and property progression without making any one activity mandatory.
- [ ] Design the regular-user chip-shortage journey: clearly show available non-ad chip earning/recovery options and an optional rewarded-video offer at the bar for a disclosed, capped virtual-chip reward.
- [ ] Add optional rewarded-video doubling for selected eligible activity rewards/claims; disclose the base and doubled reward before opt-in, and apply transparent eligibility, frequency caps and cooldowns.
- [ ] Keep rewarded-video chip recovery and reward doubling separate from the four scheduled non-rewarded interstitial opportunities per active hour and the persistent bottom banner.
- [ ] Explore a longer rewarded-video placement only if supported by the chosen ad provider; do not assume longer viewing automatically means higher payout. Balance reward value against realized ad revenue and virtual-economy inflation.
- [ ] Never make ads the only route to poker chips, progression or social participation; preserve fair ordinary gameplay earning paths and ensure virtual chips/currency are non-redeemable.
- [ ] Do not require forced 30-minute waits, idle AFK farming or ad-viewing loops; offer meaningful activities during any genuine cooldown and never trap a player waiting to play.
- [ ] Instrument average daily active hours, session distribution, activity diversity, social participation, progression, chip recovery source, rewarded-ad opt-in/completion, retention, complaints and healthy stopping behavior.
- [ ] Review whether the 3–4-hour target is being achieved through enjoyment and activity variety rather than excessive interruptions, coercive rewards or unhealthy play pressure.


## P9 — Daily return, home/garage upkeep, bills and live event calendar
- [ ] Create a daily return/check-in surface that summarizes true pending home-care, vehicle-maintenance, weekly-bill, daily-reward and upcoming-event items.
- [ ] Add state-aware apartment reminders and reversible home-care actions; never send a dirty-home alert if the player's home state does not warrant it.
- [ ] Add garage reminders for owned vehicles that are actually due for routine maintenance, with clear service actions and reasonably affordable costs.
- [ ] Show weekly lifestyle package amount, due date, inclusions and fair in-game earning/payment options in a transparent bill reminder.
- [ ] Preserve ownership and core access: no eviction, car confiscation, permanent asset damage, punitive shutoff or poker/social lockout due to absence or missed bill.
- [ ] Add daily reward claim and streak/milestone progress to the return surface, with transparent rules and reasonable grace/catch-up.
- [ ] Draft and test friendly reminder copy such as “Hustle City is missing you. Your garage could use a little attention, and your apartment is ready for a quick refresh. Your weekly lifestyle package is coming due. Come back, collect your rewards, and see what's happening around the city.”
- [ ] Ensure every reminder is based on actual account state; do not fabricate urgency, maintenance needs, overdue balances or available rewards.
- [ ] Design a central event calendar for stadium-scale parties/headline events and smaller venue concerts, club nights and social gatherings.
- [ ] Support event schedules, venue/time details, hosts/performers, RSVP/attendance, friend/crew attendance and recurring/special event programming.
- [ ] Build event activities for dancing, socializing, conversations, networking, group attendance and card trading where appropriate.
- [ ] Apply privacy, mutual-consent, moderation, block/report and safety controls to networking; off-platform contact exchange must be voluntary and mutually authorized.
- [ ] Connect event reminders to in-game inbox and separately consented supported notification channels, with quiet hours, frequency caps, deduplication and unsubscribe controls.
- [ ] Test the daily return loop for usefulness and enjoyment; ensure reminders invite players back rather than shame or pressure them.


## P10 — Crew presence, event invitations and external sharing
- [ ] Add a friends/crew “Who's online” surface to the in-game phone, respecting each player's presence visibility settings.
- [ ] Add appear-offline/limited-presence controls and define who can see online status, current activity and venue/location.
- [ ] Add opt-in alerts for selected friends/crew coming online and for crew/neighborhood event announcements.
- [ ] Build an event invitation composer with event/venue/time/message, audience selection (specific friends, crew or authorized group), preview and send.
- [ ] Support in-game direct messages and event invitations with accepted/declined/maybe responses and event update/cancellation messages.
- [ ] Add optional SMS/text and email share actions initiated by the player, with recipient selection, preview and explicit send confirmation.
- [ ] Do not silently scan, upload or message address-book contacts; any optional contact access requires explicit OS permission and must remain optional.
- [ ] Keep phone numbers and email addresses private; expose only in-game identity/profile information the recipient's settings permit.
- [ ] Add controls for who can message or invite a player, plus mute, block, report and moderation actions across messages and invitations.
- [ ] Implement anti-spam safeguards: rate limits, cooldowns, duplicate detection, abuse monitoring and recipient opt-out; prohibit unsolicited bulk external messaging.
- [ ] Separate player-initiated event shares from platform-generated marketing/re-engagement alerts; require appropriate channel-specific consent for platform email/SMS.
- [ ] Define presence defaults, audience permissions, invitation limits, notification cadence, retention, provider costs and consent language with creator approval and privacy/security review.


## P11 — In-game phone transportation and automated passenger travel
- [ ] Add a Transportation section to the in-game phone as the player's city mobility control center.
- [ ] Implement “Call my car” for owned/authorized vehicles, with vehicle selection and delivery to the player's current location.
- [ ] Design and implement in-world taxi/cab pickup requests.
- [ ] Design and implement an in-world ride-hailing request flow.
- [ ] Add premium concierge vehicle/chauffeur requests.
- [ ] Design private-aircraft staging: request an owned/authorized plane, have it ready at the airport and confirm fuel/departure readiness.
- [ ] Enforce ownership, keys and access permissions when retrieving/summoning vehicles; do not let players summon vehicles they do not own or have permission to use.
- [ ] Implement automated passenger travel for initial launch; no direct manual steering/acceleration in the initial release.
- [ ] Build safe, predictable route following, traffic handling and collision avoidance for automated vehicle travel.
- [ ] Add passenger-perspective camera controls so players can rotate/orbit the view and enjoy city scenery while being transported.
- [ ] Display pickup/destination, service status, arrival/travel estimate and cost where applicable; provide cancel/exit and interruption recovery.
- [ ] Protect player assets and balances from simulation defects; no random crashes, vehicle loss, damage fees or financial penalties caused by automated pathing.
- [ ] Define service costs, staging rules, aircraft access/fuel state, routing, travel times, camera behavior and airport flow for creator review.
- [ ] Keep manual driving out of launch scope unless separately approved after technical, safety and accessibility review.


## P12 — Parking garages and valet/concierge arrival
- [ ] Design standard self-parking at relevant destinations with clear designated spaces for owned/authorized vehicles.
- [ ] Add indoor/covered garages to appropriate residential properties, upscale venues, hotels/clubs and major destinations; define slot capacity and availability.
- [ ] Design a premium valet/concierge drop-off point at eligible destinations.
- [ ] Allow qualifying players to exit at the entrance and have an NPC valet/concierge move the vehicle to secure parking.
- [ ] Allow premium valet convenience to be accessed through an eligible paid service tier OR earned in-game wealth, with exact eligibility and costs requiring creator approval.
- [ ] Keep basic vehicle ownership and standard parking available to non-subscribers.
- [ ] Persist authoritative vehicle location and state (owner, keys/authorized users, garage/slot, condition, availability) during and after valet handoff.
- [ ] Add phone/valet retrieval so players can request their parked vehicle at an approved pickup point.
- [ ] Enforce ownership/key/permission checks for valet drop-off, storage and retrieval.
- [ ] Implement safe NPC valet routing or a safe parking transition; prevent collisions, damage, theft, vehicle loss and penalties caused by simulation errors.
- [ ] Define overflow parking for full garages, service coverage, fees, retrieval timing and disconnect/session recovery.

 
## P13 — Universal IDs, entity registry and inventory traceability
- [ ] Design a universal entity-ID strategy for every trackable game object and record: clothing, individual garments, vehicle models and individual cars, motorcycles, trucks, helicopters, private jets, boats, yachts, buildings, apartments, garages, businesses, venues, property, furniture, cards, food, drinks, cigars, cigarettes, menus, menu versions, menu entries, products, services and other inventory.
- [ ] Define the distinction between catalog/type IDs and unique instance IDs; one catalog definition may have many individually tracked instances.
- [ ] Define typed entity namespaces, immutable/non-recycled identifiers, uniqueness constraints and opaque internal IDs that do not expose sensitive account/business data.
- [ ] Define shared entity metadata and typed extensions for ownership, custody, access permissions, location/container, condition, lifecycle status, source/creation and timestamps.
- [ ] Preserve the distinction between ownership, possession/custody and permission/access; integrate the existing vehicle key/authorization model.
- [ ] Create auditable lifecycle events for creation, acquisition, sale, transfer, lending, reservation, use/consumption, location change, maintenance, retirement and administrative correction as appropriate.
- [ ] Define business/venue records and their relationships to independently identified menus, menu versions, menu entries, products and services; identify buildings/properties independently from businesses occupying them, and model trackable sub-assets such as rooms, parking spaces and garage slots where needed.
- [ ] Catalogue food, drinks, cigars and cigarettes as explicit item definitions with category, price, availability and applicable age/content/regulatory metadata.
- [ ] Choose unit-level instance tracking for unique assets/collectibles and quantity/lot/batch tracking for fungible stock where appropriate.
- [ ] Ensure transactions reference player/account, item/catalog or instance ID, quantity, counterparty/business, timestamp, currency/price and resulting inventory state.
- [ ] Design concurrency-safe issuance, idempotent transactions, duplicate prevention, audit logging and inventory reconciliation.
- [ ] Define card catalog IDs separately from individual card instance IDs; new card copies must receive new unique instance IDs.
- [ ] Design configurable card-supply policies for population growth, including initial pool, reserve, issuance triggers, batch size, distribution/value/rarity rules, duplicate policy, replacement policy and circulation targets.
- [ ] Track card counts across created, unissued/available, reserved, in-circulation, player-held, system/business-held, consumed/retired and invalidated states.
- [ ] Model player population and card supply as separate metrics; do not assume one card per player unless a specific creator-approved rule says so.
- [ ] Simulate supply and economy behavior at 1,000, 10,000, 100,000 and higher player populations; test simultaneous issuance/trading and ensure no duplicate ownership or count drift.
- [ ] Require creator approval for card-to-player ratios, issuance thresholds, new values/variants/sets, rarity distributions and any supply inflation rules.
- [ ] Select database schema, ID encoding, indexes/partitioning, retention and operational admin tools after the domain model is reviewed.


## P14 — In-game clock, day/night cycle and weather
- [ ] Design a server-authoritative shared world clock for each multiplayer world instance.
- [ ] Add a persistent HUD display of in-game time and current local weather; clearly distinguish game time from the player's real-world device time.
- [ ] Implement smooth dawn, sunrise, morning, noon, afternoon, golden hour, sunset, dusk and night transitions.
- [ ] Coordinate sun position, sky, ambient lighting, shadows, reflections and artificial lights with the world clock.
- [ ] Design and implement changing climate-appropriate weather: sunny/clear, cloudy, humid/hazy, rain/showers, thunderstorms and fog.
- [ ] Support district/region-aware weather where appropriate, with smooth transitions across boundaries.
- [ ] Display concise weather conditions and determine whether temperature, wind, precipitation intensity and forecast details belong in the initial HUD or phone.
- [ ] Connect time/weather state to NPC schedules, traffic, venue ambience, event presentation, ambient audio and environmental effects where appropriate.
- [ ] Preserve safe predictable transportation; weather must not create random crashes, player-asset damage, loss or unfair financial penalties.
- [ ] Define in-game day length/time acceleration, calendar/date behavior, synchronization across clients/world instances, weather-region boundaries, transition rates, forecast horizon and seasonal rules before implementation.
- [ ] Test clock/weather consistency across multiple players, reconnects, server restarts and travel between districts.


## P15 — Neighborhood lifestyle spaces, landmarks and ambient city life
- [ ] Define distinct neighborhood visual identities, including architecture, landscaping, amenities and social atmosphere.
- [ ] Add rooftop terraces/lounges, private balconies, residential back porches, patios and waterfront decks to appropriate properties and venues.
- [ ] Create intimate private/semi-private waterfront dining decks with tables, seating, lighting and water views.
- [ ] Add player interactions for sitting, dining, eating together, relaxing, talking, socializing and inviting friends into permitted spaces.
- [ ] Add suitable rooftop social amenities such as skyline-view lounges and pools where appropriate to the location.
- [ ] Model access rules for private decks, porches, rooftops and shared spaces using ownership, tenancy, venue access and invitation permissions.
- [ ] Add palm trees and deliberate landscaping to appropriate neighborhoods, streets and waterfront locations.
- [ ] Give important buildings, towers, clubs, restaurants and landmarks recognizable names and world signage.
- [ ] Display the player's current district and, where useful, named building, venue or nearby landmark in the HUD/map.
- [ ] Populate appropriate districts with premium vehicles and visible fashion/jewelry, consistent with character customization, NPC identity and the game's economy.
- [ ] Add occasional ambient commercial/private plane and helicopter flybys with varied routes, altitude, direction and timing; keep ambient aircraft distinct from player-owned or interactive aircraft.
- [ ] Extend the world calendar/weather design to include cold-weather periods and the possibility of occasional snow.
- [ ] Define snow coverage, frequency, accumulation, seasonal behavior and NPC/environment response without locking dates or frequency before creator review.
- [ ] Preserve safe pedestrian and automated vehicle behavior in rain, cold and snow; no random crashes, asset damage, loss or financial penalties caused by weather simulation.


## P16 — Expanded agent charters and complete ownership briefs
- [ ] Reconcile the repository's legacy 48-role capability catalog, named cohort identities and creator-approved 17-agent operating roster; do not infer or silently replace the canonical roster or QA assignments.
- [ ] Create a dedicated, detailed charter file for every approved production agent and QA supervisor, with mission, ownership, explicit responsibilities, interfaces, inputs, outputs, permissions, dependencies, non-goals, acceptance criteria and handoff rules.
- [ ] Expand SCRIBE and LENS creative-lead responsibilities and define how creative direction, canon, visual references and implementation packages flow to production specialists.
- [ ] Expand QA-1 through QA-3 charters with their four-worker review assignments, independent test expectations, evidence requirements, correction loops and escalation rules.
- [ ] Expand all P01–P12 production-specialist charters to cover the full approved product blueprint in their assigned domains, not just isolated task summaries.
- [ ] Ensure every charter references the same current project canon and shared interfaces; cross-link relevant frameworks and prohibit contradictory duplicate sources of truth.
- [ ] Give each agent a substantial role-specific knowledge pack and task checklist, sized to its actual domain; avoid generic one-paragraph prompts.
- [ ] Define a shared deliverable template: scope, canon references, assumptions, dependencies, interface impact, design/implementation, artifact paths/version, tests/evidence, risks and next handoff.
- [ ] Preserve the 20-minute production, 5-minute independent QA, 5-minute correction cadence and overlapping wave/resource schedule; time targets must not replace evidence or QA approval.
- [ ] Verify that role files, registry IDs, cohort mapping, permissions and QA ownership agree before activating or assigning production work.

## P17 — Persistent named NPC population and full work/life simulation
- [ ] Implement the creator-approved NPC requirement: every represented Sim has a stable unique ID, actual name, assigned job/occupation/function, profile, schedule and persistent continuity.
- [ ] Design a scalable population roster capable of representing 100,000 named/job-assigned people without requiring 100,000 simultaneous full-detail AI processes.
- [ ] Build occupation taxonomy and employer/workplace mapping, including casino hosts, dealers, chip cashiers, bartenders, servers, doormen, concierge, valets, rideshare/taxi drivers, barbershop staff, shop workers, cleaners, maintenance, transit and construction staff.
- [ ] Specify full job workflows: arrival, clock-in, station preparation, service/task execution, queues, breaks, meals, coworker handoffs, closing and clock-out.
- [ ] Build varied daily routines: home preparation, breakfast, commute, work, breaks, lunch, errands, barber visits, dinner, social visits, events, return home and rest.
- [ ] Implement feasible destination choice and integration with walking, vehicles, public transit, taxi/ride-hail and approved travel systems.
- [ ] Define personality, dialogue style, language/register, player interaction and NPC-to-NPC social behavior by role and context; prevent fabricated facts and harmful caricatures.
- [ ] Integrate time, weather, venue hours, event schedules, crowding, route closures and transport availability into NPC decisions.
- [ ] Define identity continuity, persistence, memory scope, privacy/retention and reconnect/restart recovery with backend and multiplayer owners.
- [ ] Implement detailed/local/background simulation tiers and profile performance at staged population scales; retain identity and abstract state when people are outside active streaming range.
- [ ] Deliver role-specific service workflows for launch-critical staff and test each end-to-end against authoritative venue/economy systems.
- [ ] Independently QA identity continuity, job completion, breaks, commuting, meals, dialogue, service queues, transaction integrity, pathfinding recovery, multiplayer consistency and performance.


## P18 — 30-day Sim wardrobes and contextual fashion
- [ ] Define a wardrobe profile for every represented Sim, linked to their persistent person identity and universal item catalog.
- [ ] Design enough modular garments, accessories and complete outfit combinations to support approximately 30 days of varied looks per Sim without loading all garments at once.
- [ ] Define outfit rotation and repetition avoidance across time, districts, crowds, shifts, venues, events and weather.
- [ ] Create venue/occupation dress-code matrices for casino hosts, dealers, cashiers, bartenders, servers, concierge, doormen, valets, rideshare/taxi drivers, barbershop staff and other workers.
- [ ] Create upscale casino and nightlife guest fashion styles, including glamorous/sexy adult eveningwear; define coordinated staff uniforms separately.
- [ ] Create beach/resort, restaurant, bar, rooftop, yacht-club, concert, private-event, neighborhood streetwear, everyday and leisure categories.
- [ ] Support work-uniform changes at shift start/end and distinguish off-duty clothing.
- [ ] Integrate weather/season-aware clothing for heat, rain, cold and occasional snow.
- [ ] Validate garments against body rigs, animation, seating, dining, vehicle entry and interaction poses; track clipping and performance budgets.
- [ ] Apply content-rating and platform constraints; never sexualize minors or include explicit nudity. Avoid stereotype-based clothing assignments.
- [ ] Independently QA month-scale outfit variety, contextual dress, uniform correctness, continuity, fit and rendering performance.


## P19 — Initial 10,000 individually named Sim population
- [ ] Plan the initial 10,000-person named NPC roster, managed as a versioned cohort and validated in batches.
- [ ] Target 5,000 men and 5,000 women in the initial roster; preserve this as the creator's starting composition target, not a rule for every future expansion.
- [ ] Define varied age bands, broad racial/ethnic representation, skin-tone and appearance palettes, body types, style/swagger profiles and personality variation; exact demographic percentages beyond the stated gender target require creator review.
- [ ] Give every person a stable unique ID and distinct usable name; define cultural naming guidance and duplicate-name checks.
- [ ] Require each profile to include age/age band, appearance, style, personality, job/function, employer/workplace, home anchor, schedule, wardrobe and daily routine.
- [ ] Distribute population across districts, households, businesses, shifts, commutes, public spaces, venues and events to make the city feel lived-in throughout the day.
- [ ] Build batch manifests, ID allocation, import validation, duplicate detection, required-field checks, roster count reconciliation and safe update rules.
- [ ] Ensure later population batches and profile corrections never regenerate or overwrite existing identities.
- [ ] Prohibit demographic stereotyping: race, ethnicity, skin tone, gender and age must not determine intelligence, morality, criminality, income, job qualification or personality.
- [ ] QA return visits, familiar NPC recognition/continuity, city crowd distribution, staffing coverage, schedule realism and scalable simulation at the 10,000-person roster target.


## P20 — Memorable relationship NPCs and player recognition
- [ ] Make meaningful recurring service/venue NPCs named, persistent individuals rather than interchangeable service prompts.
- [ ] Cover casino hosts/dealers/cashiers, club and venue staff, bartenders, servers, restaurant/hotel/venue concierge, doormen, valets/parking attendants and other recurring service roles.
- [ ] Persist NPC identity, role, workplace, personality and relevant life continuity across player sessions.
- [ ] Implement player-scoped relationship memory: first meeting, repeat visits, familiarity, relevant preferences and notable prior interactions.
- [ ] Make familiarity grow naturally with repeat encounters; vary greetings and dialogue by personality, role, relationship and actual context.
- [ ] Support role-specific memories: bartender's usual order; concierge/valet's verified vehicle history; casino host's appropriate visit/service preferences; venue host's seating/event preferences.
- [ ] Allow NPCs to notice relevant changes, such as a regular arriving in a different authorized car, without inventing facts.
- [ ] Ensure NPCs retain their own schedules, coworkers, routines and relationships independent of player presence.
- [ ] Define privacy-scoped memory, data minimization, retention/correction/deletion controls and strict isolation between players.
- [ ] Prevent NPCs from fabricating memories, exposing another player's information, pressuring casino spending or compromising poker fairness.
- [ ] QA recurring NPC recognition across separate sessions, familiarity progression, varied accurate dialogue, vehicle authorization checks, preference changes and memory-unavailable fallback behavior.


## P21 — Shared social world and off-duty NPC lives
- [ ] Separate NPC occupation/workplace identity from current activity and location so staff remain the same people when off duty.
- [ ] Give named NPCs believable off-duty routines, errands, leisure interests, friendships, social invitations and destinations across the city.
- [ ] Allow recurring NPCs to appear naturally in public spaces and social venues outside their workplace: streets, shops, beaches, clubs, concerts, restaurants, neighborhood gatherings and parties.
- [ ] Preserve recognition and relationship memory across contexts; NPCs can remember where they met the player and refer to shared events when relevant.
- [ ] Build NPC-to-NPC social connections and group outings so their social lives do not revolve exclusively around players.
- [ ] Support mixed player/NPC gatherings, including player-hosted yacht parties and beach parties with invited player friends/crew and suitable NPC guests.
- [ ] Distinguish invited NPC guests, ambient attendees and venue staff; guests should socialize and participate as guests, not all act as employees.
- [ ] Make NPC event attendance schedule-, relationship-, capacity- and context-aware; do not force attendance when unavailable.
- [ ] QA cross-location identity continuity, off-duty encounters, party participation, NPC-to-NPC social behavior and later recognition of shared encounters.


## P22 — Player-specific relationships, social outings and dating
- [ ] Maintain separate NPC relationship states and shared histories for each player.
- [ ] Support gradual friendship and dating development through repeated interactions.
- [ ] Let players invite NPCs to lunch/dinner, comedy shows, concerts, clubs, beach events, yacht parties and other activities.
- [ ] Give NPCs agency to accept, decline, suggest another time and set boundaries.
- [ ] Protect relationship privacy between players; include consent, age-appropriate rules, rejection handling, blocking and reporting.

## P23 — Jokes on You Comedy Club (proposed name)
- [ ] Design a paid-admission comedy/date-night venue with scheduled shows, varied tables/seating, food/drink service, NPC/player guests and a cigar-lounge concept.
- [ ] Confirm final venue name, layout, capacity, schedule, ticket pricing and rating/platform requirements with creator before locking implementation.

## P24 — Expandable multi-floor casino architecture
- [ ] Design Shuffle Club as a large multi-floor flagship with multiple poker rooms, tables and supporting social/service spaces.
- [ ] Include Hustle Towers as the second initial casino destination.
- [ ] Architect expandable floors/rooms, table instances, concurrent capacity, staff coverage, wayfinding, room discovery and overflow handling.
- [ ] Determine building dimensions, floor count, poker-room count and capacity targets through performance and concurrency planning; do not guess these values.
- [ ] Support distinct casino brands for future cities rather than cloning the initial two names.

## P25 — Procedural naming and automated venue population
- [ ] Define naming principles and configurable name-generation rules for cities, casinos and other businesses, including local flavor and distinctiveness.
- [ ] Ensure generated names are stable, non-duplicate within relevant scopes, suitable, and free of avoidable trademark confusion; allow creator review and override.
- [ ] Provision generated venues with stable IDs, venue type, city/district placement, brand/name metadata, staffing needs and NPC population/activity schedules.
- [ ] Make generation repeatable, seedable, auditable and safe to rerun without duplicating or overwriting existing venues or NPC identities.
