# Hustle City Database

## Confirmed Supabase target
- Project: **Hustle City Shuffle Club**
- Project ref: `jtkbtogtxfbtammdlewv`
- Region: `us-west-2`
- PostgreSQL: `17.12`
- Project status at last inspection: `ACTIVE_HEALTHY`
- This is the confirmed game database. The separate IntelliStack command-center project is not the game database.

## Live database baseline (2026-11-22)
- No application tables exist in the `public` schema.
- No application migrations are recorded in Supabase migration history.
- No game schema has been deployed by this repository's draft.
- A pre-existing event trigger named `ensure_rls` invokes `public.rls_auto_enable()` after DDL. The function is SECURITY DEFINER and the Supabase Security Advisor currently warns that anon and authenticated can execute it. It was not created or changed as part of this work; review and harden it before production use.
- Security Advisor also returned no performance findings at baseline.

## Repository design status
- Initial SQL draft: [schema/001_core_schema_draft.sql](schema/001_core_schema_draft.sql). This is a historical review draft, **not approved for deployment**.
- Core model: [DATA_MODEL.md](DATA_MODEL.md).
- Open decisions: [SCHEMA_GAPS.md](SCHEMA_GAPS.md).
- Implementation sequence: [IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md).

## Important design boundaries
1. A player account/profile is not the same thing as a playable character.
2. Neighborhood ownership, neighborhood residency, crew membership, crew leadership, property ownership, and business ownership are separate relationships.
3. Hustle Money, Diamonds, and Poker Chips are separate currencies.
4. Currency and ownership changes must be server-authoritative, auditable, and idempotent.
5. Home-city selection is separate from neighborhood ownership.
6. Hustle City has six central district boxes. All surrounding map boxes are reserved for neighborhoods. The total map grid, neighborhood count, exact boundaries, and block subdivision are **not finalized**.
7. HIM (Hustle International Metro) is intercity/regional rail; HCTA (Hustle City Transit Authority) is local rail. Their networks and transfers need distinct data models.
8. Five card-pack slots per location is a current design rule; it does not mean five character cards.
9. Every exposed application table must use Row Level Security (RLS), with table-specific policies and least-privilege grants. RLS enabled with no policies intentionally denies ordinary client access; it is not a complete production access design.

## Deployment and security procedure
1. Reconcile the design against recovered Command Center conversations and approved map references.
2. Split the historical monolithic SQL draft into small, reviewed, ordered migrations.
3. Define trusted server/Edge Function boundaries, table grants, and table-specific RLS policies before exposing client access.
4. Test migrations and policies in a safe development environment; do not rely on the phone's UserLAnd environment to run Docker.
5. Apply migrations only to the confirmed Hustle City Shuffle Club project, verify tables/constraints/policies, and run Supabase security and performance advisors.
6. Keep migration SQL in GitHub and never commit service-role keys, secret keys, database passwords, or private player data.

No paid services or paid API fallbacks are authorized. Confirm any plan/usage implications before enabling optional Supabase features.
