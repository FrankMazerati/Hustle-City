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
