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

## Creator-approved requirements to carry into schema design

### Sim identity and durable memory
- Design durable records for each named Sim's stable identity and supported profile/self-model data, with a target population of up to 100,000 named Sims. Use tiered simulation; database identity persistence does not imply full real-time AI for every Sim.
- Each Sim has an individual memory library for people they meaningfully communicate with or personally encounter. Store the remembering Sim and remembered person as separate references, with event-grounded memory content. Do not share personal memories across Sims.
- Store directional pair-specific relationship state. Familiarity and trust are separate values, and neither is reciprocal by default. Preserve event history separately from current relationship values.
- Persist through sessions, reconnects, restarts and population expansion. Use sparse indexed access, not an all-to-all precomputed relationship matrix.
- Persist valet/concierge service events with player, individual attendant, vehicle, service point, timestamp and outcome. Operational shift handoff data must remain separate from an attendant's personal memory/trust.

### Economy, consumables and profiles
- The approved economy has four distinct currency types: Hustle Money (also called Hustle Cash in some food/drink discussion), Diamonds, Poker Chips and Wings. The existing SQL draft currently lists only Hustle Money, Diamonds and Poker Chips; add Wings to the reviewed wallet contract before any migration.
- Food and drinks at bars, restaurants and poker tables are paid with Hustle Money/Cash, never directly with Poker Chips. They may restore health/condition; exact health model, item effects, prices and balancing remain open.
- Poker Chip → Hustle Money exchange is a separate cashier/kiosk conversion. The approved nominal in-game rate is 1:1; atomic debit/credit, audit history, idempotency and legal/platform review remain required.
- Player profile balances, progression, owned-card counts, trade listings and shared wishlists must be sourced from authoritative records and visibility permissions.
- Membership tier names/prices, no-card package rule, and allowed package currencies are already recorded in the economy membership/rewards specification. Preserve those rules; exact quantities and billing cadence remain unresolved.

### Schema questions that remain open
- Exact Sim identity/profile, personal-memory, encounter/event, directional relationship and valet-service table schemas; retention, indexing, deletion and access-control policy.
- Whether health is one value or a broader condition/energy model; exact food/drink effect definitions and item consumption semantics.
- Canonical ledger code/name for Hustle Money versus the player-facing phrase Hustle Cash; ensure one ordinary-currency wallet rather than duplicate balances.
- Four-wallet currency constraints, including Wings, and all wallet grant/spend/conversion transaction rules.
- Exact profile visibility, memory privacy, and server/Edge Function/RLS policies.
- Do not apply a migration or claim production tables exist until the target Hustle City Supabase project is explicitly confirmed and the reviewed migration is tested.
