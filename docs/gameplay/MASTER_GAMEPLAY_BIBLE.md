# Hustle City — Master Gameplay Bible

**Document role:** Top-level specification for everything a player can do, own, collect, share, attend, travel to, upgrade and purchase in Hustle City.

**Status:** Working specification grounded in approved project direction. Numerical balancing, detailed card rules, exact catalogues, prices and launch scope remain creator decisions.

## 1. Product experience
Hustle City is a persistent cinematic realistic 3D social-world / city-life game. The player is not limited to a linear story: they build an identity, meet people, cruise the city, collect cards, unlock and own locations, customize their appearance and possessions, participate in events, and develop properties and businesses.

The game must support both active play and social presence: a player can be at a venue, cruising with a crew, hosting an event, collecting cards, shopping, or simply checking feeds and responding to invitations.


## Property progression clarification: five-card collections and venue-specific rewards

Each configured building/venue collection uses five ranked cards. Completing a collection grants only its explicitly configured reward; it does not automatically grant ownership of the whole venue.

- Hustle Towers: players may begin by renting an apartment; completing that apartment's five-card collection unlocks permanent ownership of that specific apartment.
- Shuffle Club (with the casino inside): the club and casino are not player-owned. A five-card collection may unlock a private room inside the club. Whether the casino has a separate collection or shares the club set remains TBD.
- Velvet Lounge: five-card collection; completion privilege TBD.
- Other configured venues—including Hustle Club, Hustle City Marina and Yacht Club, American Swagger Clothing, the car dealership, Upper Level Entertainment Studios, Upper Level Films and Monster Beats—need their own five-card mappings and explicitly approved completion rewards.
- Venue collections are separate from individual car and boat collections. The beach is excluded.

Keep renting, permanent apartment ownership, private-room access, venue ownership, business operation and individual vehicle ownership as distinct game entitlements. Do not invent rent prices, card rank titles, collection contents or completion rewards.
## Creator-approved property, business and production distinctions

Five-card collections unlock the configured asset/privilege, which may be inside a building rather than ownership of the building itself:
- Monster Beats is a production company. Players can own a studio inside its facility and produce music; they do not own the Monster Beats building or company.
- Players can form their own film crew and make movies through the Upper Level studio/production facility. This does not itself grant ownership of the studio building. Confirm exact naming relationship between Upper Level Films and Upper Level Entertainment Studios.
- Players can own a car lot, a clothing store and an individual yacht. Yacht ownership does not include the Hustle City Marina and Yacht Club.
- Players can own the Hustle Club and the Velvet Lounge as venues/businesses.
- Players can unlock a private room inside the Shuffle Club casino, but cannot own the Shuffle Club or casino.
- Hustle Towers progression can begin with renting an apartment; completing that apartment's five-card collection grants permanent ownership of that specific apartment.

Keep the venue/building, business, studio unit, film crew, car lot, clothing store, individual yacht, private room and apartment as separate game entities and entitlements. A card collection must grant only the explicitly configured one.

## 2. Player lifecycle
1. **Discover and join:** player arrives through the opening experience, creates a character/profile and username, accepts terms and configures privacy.
2. **Establish identity:** profile, avatar, wardrobe, optional crew affiliation, friends and social preferences.
3. **Learn the economy:** clearly distinguish Hustle Money, Diamonds, Wings and Poker Chips; explain earn/spend sources before the first purchase.
4. **Explore:** use map and destination travel to visit districts, venues, shops, transit and social gatherings.
5. **Connect:** add friends, follow feeds, chat, join crews, accept invites and share a trackable invitation link externally.
6. **Collect:** obtain cards through defined packs, activities, rewards and approved offers; complete collections.
7. **Unlock and own:** complete the designated five-card collection for a specific building where that building's collection is configured as an ownership key; claim/activate ownership under that building's eligibility rules.
8. **Operate and host:** upgrade the property/business, set access and event details, invite crew/friends and host parties or activities at supported venues.
9. **Progress:** improve wardrobe, accessories, cars, apartments and businesses; build reputation and social reach.
10. **Return:** notifications, upcoming events, feed activity, daily/seasonal content and friend activity invite the player back without coercive mechanics.

## 3. Core systems and contracts
| System | Player-facing purpose | Authoritative state |
|---|---|---|
| Player identity | Character, profile, username, status | Account/profile service |
| Wallet | Four distinct currencies: Hustle Money, Diamonds, Wings and Poker Chips | Economy ledger |
| Card collection | Packs, cards, duplicates, collection progress | Inventory/collection service |
| Card trading | Player-to-player exchange | Atomic trade service |
| Building unlock | Five-card set unlocks configured building | Collection + ownership service |
| Property | Own, rent where enabled, upgrade, access | Property service |
| Business | Operate, staff, stock, events, upgrades | Business service |
| Social | Posts, feeds, chat, friends, crew, invites | Social service |
| Sharing/referrals | External invite links and attributable rewards | Referral service |
| Travel | Destinations, rides, transit, premium options | Mobility service |
| Events | Create, publish, invite, RSVP, attend | Event service |
| Commerce | Store catalog, purchases, entitlements | Platform purchase validation |
| Customization | Clothing, accessories, vehicle/apartment/business upgrades | Inventory + ownership services |

## 4. Currency separation
- **Hustle Money:** ordinary in-game purchases, goods, services and eligible upgrades.
- **Diamonds:** boats and cars, including approved purchase and upgrade flows.
- **Wings:** flying and air-travel services.
- **Poker Chips:** actually playing poker and other explicitly chip-denominated table activities. They are non-redeemable virtual chips under the baseline.

These are exactly four separate balances. There is no additional “poker money” currency. Never silently convert between them.

Never silently convert one currency into another. Any exchange feature requires a separately approved rate, limits, confirmation and ledger entries.

## 5. Social presence and events
The game has a live, location-aware Environment News Feed and wider social feeds. Feed content may include player arrivals, purchases, poker wins, reactions, table chat, posts, event notices, friend requests and crew invitations, subject to privacy and moderation settings. Venue feeds should feel lively and have local personality without exposing private location or activity against player settings.

External sharing supports a message such as **“I just joined Hustle City. Join me over here. Here's my link.”** The link is personal and attributable. Referral rewards may include credits, Diamonds, Poker Chips and Hustle Money; exact eligibility and payouts are unresolved. Launch bonuses may be higher initially and scale down later, but must be transparent and abuse-resistant.

## 6. Travel and cruising
Destination-based automated travel is the preferred baseline, not manual driving as the core loop. Players choose destination and travel mode; they may ride as driver/passenger, travel with friends and crew, and form visible convoys. Names or crew emblems can identify participants where privacy settings allow. Map views show destinations, nearby players and crew gatherings where visibility is permitted.

Boats and cars use Diamonds under their approved purchase/upgrade rules. Flying uses Wings. Hustle Money covers ordinary in-game goods and services. Poker Chips are used only for poker/table play. Exact prices, routes, fares and upgrade costs require approval.

## 7. Buildings and the five-card key
A configured building may have a five-card ownership collection. The five cards form a building-specific set/key; completion unlocks eligibility to claim or activate that building. The card set must map explicitly to one building ID. Completing the set must not grant an unrelated building. Whether a completed set is consumed, retained as a permanent collection achievement, or converted to an ownership entitlement is unresolved and must be decided before implementation. The UI must show all five slots, card identity, acquisition status, trade eligibility and the exact building unlocked.

A building unlock is not automatically the same as neighborhood ownership, crew leadership, residency or business operating permission. These are distinct systems.

## 8. Events and venue hosting
Supported player-owned venues can allow owners/managers to create events, set title/description/time/visibility/capacity/access rules, invite friends and crews, publish to approved feeds, accept RSVPs and manage attendance. Club owners can host parties where the venue tier and permissions support it. Event creation must validate ownership/manager rights, venue availability, moderation rules and schedule conflicts.

## 9. Player commerce and platform purchases
The in-game store can offer approved packages for currency, card packs, clothing, accessories, vehicle cosmetics/upgrades, apartment upgrades and business upgrades. Exact SKUs, prices, pack odds, regional availability, tax display and refund handling must be defined in a commerce catalogue and comply with Google Play billing policies. The server validates platform receipts before granting entitlements. Never grant paid goods based only on a client success screen.

## 10. Gambling boundaries
Poker and casino-style activities use Poker Chips as non-redeemable virtual currency under the current baseline. No real-money wagering, cash-out, transfer to real value or purchase-to-cash conversion is defined. Game rules, age/access controls, jurisdictional review, responsible-play messaging and platform-policy review are required before release. Do not assume every venue has a casino: the Shuffle Club and Hustle Towers activities must follow their individually approved venue layouts and activity scope.

## 11. Player protection and integrity
- Server-authoritative balances, card ownership, trades, building ownership, upgrades, event capacity and purchase entitlements.
- Atomic trades and purchases; no duplication on retries.
- Clear confirmation for irreversible trades, expensive purchases and ownership claims.
- Block, mute, report, privacy and invitation controls.
- Anti-spam, referral fraud detection, trade abuse detection and event moderation.
- No player death; safe prevention/detection/recovery remains a global game rule.
- Do not expose exact player location to feeds or external links unless explicitly allowed.

## 12. Unresolved creator decisions
1. Exact five-card building sets and card identities.
2. Whether a completed building set is consumed or remains in collection.
3. Card rarity, duplicate handling, pack odds, trade restrictions and any card-bound status.
4. Exact currency earn rates, balances, caps and sinks.
5. Google Play package names, prices, contents and purchase limits.
6. Diamond travel rates and which travel options are premium.
7. Whether Shuffle Club and Hustle Towers each have poker rooms, tables, casino games or other activities, and exact layout.
8. Which owned building tiers support party hosting, guest limits and ticketing (if any).
9. Exact referral milestones, payouts and launch-to-steady-state schedule.
10. First-release system scope and platform age/legal review.

## 13. Implementation rule
All systems share stable player, item, currency, building, venue, event and transaction IDs. Do not implement duplicate wallets or parallel ownership records. See the other documents in this folder for detailed flows and QA.


## Expandable world and lifelong progression

Hustle City is designed as a living game. Its launch buildings, businesses, assets, card collections and progression tracks are an initial catalogue, not a fixed limit. New approved content can add venues, districts, properties, studios, stores, car lots, vehicles, yachts, events, card collections, themed packs and progression rewards over time. The five-card collection is the standard ownership/unlock format for configured targets; it does not mean every new feature must use cards. Player XP/level, stats, reputation, stars/prestige, achievements, business/crew growth and collection milestones remain distinct progression systems. Exact scales, formulas, caps, pack odds, quantities and release cadence require creator approval. See [Ownership Card Catalogue and Live Progression](OWNERSHIP_CARD_CATALOGUE_AND_LIVE_PROGRESSION.md) as the living master register.
