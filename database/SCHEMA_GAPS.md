# Database Questions and Deferred Design

These questions must be settled before production policies, RPCs, or live deployment. They are intentionally not guessed in the core schema draft.

## Identity and progression
- Can one account own multiple playable characters, or is launch limited to one?
- Can a player change home city, and are there cooldowns or costs?
- What exact rules unlock additional cities and create a character?

## Neighborhoods and crews
- Is neighborhood ownership permanent, transferable, inheritable, or relinquishable?
- Can one player found/own more than one neighborhood?
- What are residency admission and removal rules?
- What progression gates allow a player to create a crew?
- Which crew roles exist, who can appoint/remove leaders, and what happens when leadership changes?
- How are weekly crew dues calculated, authorized, and accounted for?
- Which assets can be owned by a crew versus an individual?

## Property and business
- Can properties have multiple co-owners or tenants?
- Can a business be owned separately from the property where it operates?
- Which businesses generate Hustle Money, and how are operating costs and payouts calculated?

## Economy and cards
- Confirm currency sources, sinks, limits, grants, refunds, and reversal rules.
- Confirm Poker Chips are strictly non-redeemable virtual chips for the initial release. No real-money cash-out or wagering should be implemented without separate legal review.
- Confirm card-pack acquisition, trading, duplicates, and whether every location always has five pack slots.
- Starter packages, subscriptions, and prices were discussed but not finalized; do not encode them as approved products.

## Venues, communication, and events
- Define seat reservation expiry, spectator rules, and concurrent presence behavior.
- Define consent and blocking rules for private chat, contact exchange, and card/item trading.
- Define event recurrence, NPC ownership, admin controls, and participation rewards.
- Define moderation, data retention, reporting, and privacy requirements.

## Transport
- Define ownership and rental rules for cars, motorcycles, boats, and yachts.
- Define driver/passenger permissions, crew convoy behavior, destination routing, cancellation, and safe recovery.
- Detailed train lines/stations, schedules, buses, taxis, aircraft, and water transport need their own schema after interface contracts are approved.

## Security and backend
- Define trusted server/Edge Function boundaries for wallet writes, purchases, inventory grants, ownership changes, table settlement, and event rewards.
- Define and test exact RLS policies for anonymous, authenticated, and privileged roles.
- Define Data API exposure and grants intentionally.
- Confirm the actual Hustle City Supabase project and region before applying any schema.