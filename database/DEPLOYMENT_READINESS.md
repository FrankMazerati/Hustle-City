# Hustle City Database Deployment Readiness

**Review date:** 2026-11-23  
**Status:** Schema draft only. No live game schema has been deployed.

## 1. What exists in the repository

- `DATA_MODEL.md` defines the proposed player, character, city, district, neighborhood, crew, property, economy, inventory, venue, social, event, and transport domains.
- `SCHEMA_GAPS.md` records decisions that remain open and must not be guessed.
- `schema/001_core_schema_draft.sql` contains 39 application-table definitions.
- The draft enables Row Level Security on all 39 tables.
- The draft creates zero client-facing RLS policies. This is intentionally deny-by-default; it is not yet a usable application API.
- IntelliSync currently persists its work queue in local SQLite. A Supabase persistence adapter is not implemented.

## 2. Live project inspection

The connected Supabase account link labelled **Hustle City** currently exposes a healthy project named **Hustle City Shuffle Club** (project ref `jtkbtogtxfbtammdlewv`, region `us-west-2`). The `public` schema currently reports zero tables.

The repository's `database/README.md` explicitly says the connected project must not be assumed to be the dedicated Hustle City game database. Therefore this inspection made no schema changes, grants, policies, migrations, or data writes. The project identity must be confirmed before any deployment.

## 3. Required work before deployment

1. Confirm the exact Supabase project intended for the Hustle City game backend. Do not infer identity from the account-link label or similar project name.
2. Resolve the open decisions in `SCHEMA_GAPS.md`, especially player/character cardinality, city unlock/home-city rules, crew and neighborhood ownership rules, economy sources/sinks, card-pack rules, moderation/privacy, transport, and server-authoritative operations.
3. Review the 39-table SQL draft for constraints, indexes, foreign-key behavior, uniqueness rules, and ownership invariants.
4. Design table-specific RLS policies for each client-accessible operation. Do not add broad authenticated-user policies. Ownership checks must be row-specific; UPDATE policies need both `USING` and `WITH CHECK`.
5. Define trusted server-side operations for wallet transactions, purchases, inventory grants, ownership changes, event rewards, and competitive settlement. Clients must never write balances or authorize ownership directly.
6. Decide which tables, if any, should be exposed through the Supabase Data API. New tables are not automatically exposed by default under current Supabase behavior; exposure and grants must be deliberate. Enable RLS before granting client access.
7. Generate a proper migration using the Supabase CLI's migration workflow only after the project and schema are approved. Review advisors, apply to the confirmed target, and verify the resulting schema and policies.
8. Add integration tests for anonymous, authenticated, owner, non-owner, and trusted-server access paths before connecting the game client.

## 4. Security and deployment guardrails

- Keep service-role/secret keys and database credentials outside Git and outside all local model prompts.
- Do not disable RLS to make an API call work.
- Do not expose wallet ledger writes or privileged ownership operations to the game client.
- Do not use user-editable Auth metadata for authorization.
- Do not deploy the draft simply because a Supabase project is available.
- Keep the game database and IntelliSync orchestration persistence conceptually separate unless a later approved architecture explicitly integrates them.

## 5. Current conclusion

The repository has a substantial database design draft, but the live Supabase project is not confirmed as the target and has no public application tables. The correct next step is design/security completion and project identification—not applying the draft to the currently connected project.
