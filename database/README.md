# Hustle City Database

## Status
- Design baseline is being established from creator-approved decisions.
- Initial SQL draft: schema/001_core_schema_draft.sql.
- No schema has been applied to a live database by this draft.
- The active Supabase project currently visible has a general command-center name; it is not assumed to be the Hustle City database.

## Non-negotiable data boundaries
1. A player account/profile is not the same thing as a playable character.
2. Neighborhood ownership, neighborhood residency, crew membership, crew leadership, property ownership, and business ownership are separate relationships.
3. Hustle Money, Diamonds, and Poker Chips are separate currencies.
4. Currency and ownership changes must be server-authoritative, auditable, and idempotent.
5. Home-city selection is separate from neighborhood ownership.
6. Geography is hierarchical: city → districts/neighborhoods → neighborhood planning box → 5×5 city blocks.
7. Five card-pack slots per location is the current design rule; this does not mean five character cards.
8. Every application table must use Row Level Security (RLS). No broad client policies are included in the draft.

## Deployment procedure
This SQL is a reviewable schema draft, not an applied migration. After the target Supabase project is confirmed and the schema is approved, create a proper migration using the Supabase CLI command supabase migration new with a descriptive name, move the reviewed SQL into that generated migration, apply it to the intended project, verify tables, and run security/performance advisors.

Never commit service-role keys, secret keys, database passwords, or private player data.

## Newly consolidated creator-approved data requirements
- The game economy has four distinct currency wallets: Hustle Money (also referred to in some player-facing discussion as Hustle Cash), Diamonds, Poker Chips, and Wings. Do not merge balances or silently convert currencies. Canonical naming/ledger codes must be normalized before migration.
- Food and drinks at bars, restaurants and poker tables are purchased with the ordinary Hustle Money/Cash wallet, never directly with Poker Chips. Food/drink items may restore health or affect player condition; item prices and effects remain configurable design data.
- Poker Chips → Hustle Money conversion is a separate explicit cashier/kiosk transaction, not direct payment with Poker Chips. The approved nominal in-game conversion is 1:1, subject to the existing legal/platform review and server-authoritative ledger safeguards.
- Every named Sim/NPC needs durable identity and self/profile records. The intended population scale is up to 100,000 named Sims, with tiered simulation and sparse records rather than a fully materialized all-to-all relationship matrix.
- Sim person-memory libraries and directional per-pair relationship records must persist across logout, reconnect and server restart. Historical encounters/conversations are distinct from current familiarity, trust and relationship state.
- Valet/concierge service history must preserve player, individual attendant, vehicle, service point, timestamp and outcome. Shared operational handoff data must not merge attendants' personal memories or trust.
- These are data-model requirements, not a claim that the SQL draft has been migrated or applied to a live database. See DATA_MODEL.md and SCHEMA_GAPS.md for the pending schema work.
