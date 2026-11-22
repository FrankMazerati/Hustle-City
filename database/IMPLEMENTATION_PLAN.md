# Hustle City Database Implementation Plan

## Confirmed target
Supabase project **Hustle City Shuffle Club** (`jtkbtogtxfbtammdlewv`), PostgreSQL 17.12, region `us-west-2`. The separate IntelliStack command-center project is not in scope.

## Safe baseline observed 2026-11-22
- No application tables in `public`.
- No application migrations recorded.
- A pre-existing `ensure_rls` DDL event trigger calls `public.rls_auto_enable()`.
- Security Advisor warns that this SECURITY DEFINER function is executable by `anon` and `authenticated`. It has not been modified by this project work.
- No performance advisor findings were returned.

## Implementation stages
1. **Reconcile historical decisions.** Recover original Command Center conversations and map references. Remove stale assumptions from the legacy draft before generating constraints.
2. **Canonical geography and transport.** Model six districts and the neighborhood boxes without hardcoding unapproved grid dimensions, neighborhood count, block subdivision, station count, or rail routes. Keep HIM and HCTA separate with explicit transfer relationships.
3. **Identity and social foundation.** Finalize account/profile/character cardinality, crews, residency, property, business, venue, presence, and communication rules.
4. **Economy and inventory.** Design append-only wallet ledger, idempotency, server-authoritative transaction functions, inventory grants, and card-pack rules.
5. **Security design.** Define least-privilege grants, per-table RLS, trusted-server operations, moderation, privacy, and deletion. Never enable client write access to balances or ownership.
6. **Migrations and verification.** Create small ordered migrations, test in a safe development environment, apply only to the confirmed Hustle City project after review, inspect schema and migration history, and run security/performance advisors.

## Deployment guardrails
- The existing `database/schema/001_core_schema_draft.sql` is historical review material, not a production migration. It encodes an unapproved 7×7 grid and 5×5 block assumptions and must not be applied as-is.
- Do not use a monolithic `apply_migration` call to iterate. Use a reviewable migration workflow and verify after each stage.
- Do not enable public Data API grants by default. Supabase grants and RLS are separate layers; expose only what the approved client/server architecture requires.
- RLS enabled without policies is deny-by-default for ordinary client roles, but it is not a finished access model.
- Keep SQL migrations and architecture in GitHub. Never store secrets or private player data in the repository.
- No paid APIs or optional paid features without explicit cost approval.
