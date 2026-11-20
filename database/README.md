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