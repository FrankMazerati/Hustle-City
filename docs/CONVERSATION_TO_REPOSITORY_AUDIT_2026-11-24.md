# Hustle City Conversation-to-Repository Audit

**Audit date:** 2026-11-24  
**Repository:** `FrankMazerati/Hustle-City`  
**Audited branch:** `knowledge-library-foundation`  
**Foundation PR:** [#11](https://github.com/FrankMazerati/Hustle-City/pull/11) — open, not merged to `main`.

## 1. Purpose and audit standard

This document compares creator-approved Hustle City directions available in the conversation history and project context with the current repository. It separates:
- **Documented:** a relevant requirement exists in a canonical project file.
- **Partial:** the idea exists, but important rules, edge cases, or authoritative data contracts are missing.
- **Conflict / stale:** repository files disagree with each other or preserve superseded instructions.
- **Missing:** no adequate canonical record or implementation contract was found in the inspected files.
- **Unresolved:** the direction is approved, but the creator has not finalized the detail.
- **Proposed:** an idea was exploratory and must not be treated as approved.

This is a repository-backed audit of the conversation history and summaries currently accessible to this session. It is not a claim that every message in every historical chat has been exported or exhaustively re-read. The audit should be extended if complete raw chat exports become available.

## 2. Repository and implementation status

- The canonical foundation branch is `knowledge-library-foundation`; PR #11 is open and unmerged. The default branch is `main`.
- The project has substantial design documentation, a database draft, an Unreal Engine 5 scaffold, IntelliSync code/configuration, shared schemas and agent documentation.
- Documentation does not prove a feature is implemented. The database SQL is explicitly a review draft and has not been applied to a confirmed Hustle City Supabase project.
- PR #11 states that the scheduler remains disabled pending group-aware execution, runtime-enforced permissions and the full QA-1 → QA-2 → production → QA-3 workflow. A fresh CI run and a real Unreal Editor build remain required.
- Do not label the game, live database, autonomous workforce or full feature set as production-ready based on the presence of documents or starter code.

## 3. Conversation-to-repository coverage

| Area | Repository evidence | Audit result | Required follow-through |
|---|---|---|---|
| Product identity and launch scope | `docs/PROJECT_VISION.md`, `docs/PROJECT_DESIGN_ATLAS.md`, social-world requirements | Documented, but launch and expansion boundaries must stay aligned | Keep poker-first multiplayer social activity game as launch identity; keep player-directed crime sandbox ideas post-launch/proposed |
| World geography, city grid and districts | `world/HUSTLE_CITY_TOP_DOWN_DISTRICT_AND_LANDMARK_PLAN.md`, Project Vision, Design Atlas | Broadly documented; map corrections are accumulated in the world plan | Run a named-landmark/district consistency pass across map, vision, atlas and agent briefs |
| Named places and signature launch destinations | World plan, social-world requirements, economy launch list | Documented, with exact playable launch requirements | Validate every required venue has a functional gameplay/service definition, not merely a rendered building |
| Trapper District vs upscale Hustle District | World plan and world identity documents | Partial; confirm all canonical contrast details are preserved consistently | Keep Trapper District gritty/distressed and Hustle District upscale; avoid flattening their identities |
| City population and living Sims | `SIMS_MPC_NPC_FRAMEWORK.md`, Project Vision, schemas | Documented at design level; data/runtime incomplete | Preserve named identity, 10,000 initial roster and expandable 100,000-person target with tiered simulation |
| NPC daily lives, work and schedules | Sims framework, Project Vision, NPC charters | Documented, implementation partial | Tie schedules, work, homes, transport and assets to authoritative Sim records and real event history |
| NPC profiles and self-knowledge | Sims framework sections 31–33, Design Atlas sections 31–33 | Documented in recent canonical sections | Keep public profile separate from private self-model, financial data and exact residential coordinates |
| Per-Sim person memory, familiarity and trust | Sims framework sections 19–24 and 34–35; Decision Register; database docs | Documented as approved requirements; schema missing | Design sparse directional memory/relationship/encounter records, privacy and retention |
| NPC-hosted parties, dating and social agency | Social-world requirements, Sims framework, Design Atlas | Broadly documented; interaction/state details partial | Preserve consent, adult-only romance, independent NPC schedules and relationship-specific decisions |
| Valet/concierge service memory | Social-world requirements, Sims framework section 36, database docs | Documented as requirement; schema missing | Persist individual attendant/player/vehicle/service-point/time/outcome; keep operational handoff separate from personal memory |
| Player profile, levels, stars, balances and cards | Social-world requirements, Design Atlas sections 25–29 and 37 | Documented; canonical economy/progression rules still need cross-file reconciliation | Separate authoritative balances, progression, owned cards, trade listings and wishlists |
| Card discovery and trading | Sims framework, social-world requirements, membership/economy docs | Partially inconsistent | Align approved poker achievement, daily-session and peer-trading channels; keep daily login currency grants card-free |
| Four-currency economy | Memberships & Rewards, database README/data model/schema gaps | Documented, but SQL draft was missing Wings | Keep four distinct wallets and one canonical Hustle Money ledger code; Hustle Cash is a player-facing alias, not a second wallet |
| Poker Chip → Hustle Money conversion | Memberships & Rewards and database docs | Conflict inside membership document | 1:1 nominal in-game conversion is approved; fees, limits, eligibility and launch remain unresolved |
| Food, drink and player condition | Food catalog, social-world requirements, database docs | Partial and wording conflict | Food/drink at poker tables uses Hustle Money and restores table health; broader health/energy/hunger model remains open |
| Membership ladder and package contents | Memberships & Rewards | Documented and approved | Preserve eight names/prices, currency-only packages, no cards/assets, and unresolved billing cadence/quantities |
| Daily free-player rewards | Memberships & Rewards, Social World requirements | Documented; exact reward schedule unresolved | Keep free-player daily rewards separate from memberships and card acquisition; define amounts/streak/catch-up/timezone/caps later |
| Transport, rail and city mobility | Transportation Framework, Project Vision, Design Atlas | Documented at planning level; service schema partial | Preserve separate HIM intercity and HCTA local authorities; specify lines/stations/fare/schedule and playable transport |
| Property, houses and business ownership | Economy docs, world plan, database model | Partial | Preserve stable parcel IDs, ownership/residency distinction, occupancy/availability and anti-double-purchase controls |
| Device-native phone/tablet/PC UX | Design Atlas section 38 | Documented direction; UI details unresolved | Tablet is primary design target; phone tap-driven navigation; PC expanded controls; same authoritative world and progression |
| Unreal Engine 5 foundation | `ENGINE/unreal`, Project Vision, PR #11 | Starter scaffold exists; build not verified | Require real Unreal Editor build and playable acceptance tests |
| Agent workforce and assembly line | `agents/`, `intellisync/`, PR #11 | Conflict / stale documents | Reconcile old 12+3 roster with current 17 local roles; correct Trinity authority, cadence, QA routing and branch policy |
| Local-first / zero-cost execution | IntelliSync config, mobile AI HQ docs, recent project context | Partially documented; older docs conflict | Enforce no paid calls, queue when no verified free capacity, one active local model call on shared device |
| Shared Git workflow | Newer workforce decisions vs older mobile AI HQ docs | Conflict | Current direction is one shared `main` branch and no per-agent branches; update stale branch-per-task and no-direct-push instructions only after canonical workflow review |

## 4. High-priority contradictions and stale records

### 4.1 Workforce identity and control plane

The repository contains multiple incompatible workforce descriptions:
- `agents/hustle-city-core-roster.json` and `intellisync/config/agents.json` describe 12 specialists plus 3 QA supervisors (15 local worker seats), with Trinity represented as a deterministic coordinator service.
- The current creator-approved target is 17 local agents: SCRIBE and LENS as parallel creative leads, QA-1 through QA-3, and P01–P12 production specialists. Trinity is ChatGPT in the coordinating conversation, not a locally running agent.
- `agents/agent-registry.json` contains a legacy 48-role catalog. `mobile-ai-headquarters/` still describes a 12-agent remote-model architecture and branch-per-task workflow.
- The current production cadence is 20 minutes production, 5 minutes independent QA, 5 minutes correction, with overlapping waves/resource scheduling. The existing runtime configuration does not implement this complete loop.
- The current shared Git direction is one shared `main` branch, with production agents committing/pushing their own scoped work subject to safeguards. Older documents prohibit direct pushes and require isolated branches.

**Action:** Treat the newer 17-role/Trinity/shared-main/20-5-5 direction as current canon. Reconcile the roster, prompts, charters, model assignments, QA group ownership, scheduler, branch policy, mobile HQ docs and PR description as one controlled workforce update. Do not infer that 17 model assignments are currently installed or running; local-device availability and heartbeats require verification.

### 4.2 Economy contradictions

- The membership document states the Poker Chip conversion ratio is unresolved in one section, but later states the creator-approved rate is 1:1. The 1:1 nominal in-game conversion is the approved direction; fees, limits, eligibility and policy review remain unresolved.
- The membership document previously treated all card-acquisition channels as unresolved, while the social-world requirements specify approved channels: qualifying poker hands/achievements, qualifying daily play sessions and player-to-player trading. **Corrected during this audit:** the membership document now records those channels; daily login currency rewards remain separate and do not award cards.
- Food/drink language sometimes says health/condition and sometimes implies energy. The creator specifically directed food/drinks at poker tables to restore table health. The broader relationship among health, energy/stamina, hunger and condition remains unresolved.
- Hustle Cash and Hustle Money refer to the ordinary wallet in different discussions. Use one canonical wallet/ledger code (`HUSTLE_MONEY`); treat Hustle Cash as a display-language alias unless a later creator decision changes it.

**Action remaining:** Check the flagship food catalog and any secondary economy references for the same wording, then preserve the aligned membership, social-world and database contracts through migration review.

### 4.3 Launch scope versus later ideas

The Design Atlas says Hustle City launches as a poker-first multiplayer social activity game, not a full crime sandbox. Player-directed robbery, weapons, jail, death and punitive police gameplay are not launch features; crime-oriented gameplay is a possible post-launch proposal requiring a separate creator decision and review. Signature destinations and core transport explicitly required for launch must not be pushed into later Coming Soon phases.

**Action:** Preserve launch requirements when phasing implementation. Do not promote assistant-generated ideas or old pilot tasks into creator-approved scope.

## 5. Database audit

### Present in the SQL draft

The current SQL draft contains foundational tables for:
- Accounts/player profiles and player characters.
- Cities, districts, neighborhoods, blocks, home-city selection, neighborhood ownership/residency.
- Crews, membership and leadership.
- Properties, property ownership, businesses and business ownership.
- Wallet accounts, wallet transaction headers and wallet ledger entries.
- Inventory, collectible cards, player cards, card packs and pack placements.
- Venues, presence, tables and seats.
- Social conversations, participants, messages and contact exchange requests.
- City events, event participants, vehicles, vehicle ownership and travel trips.

### Missing from the SQL draft relative to approved requirements

No dedicated durable schema was found for:
- Named Sim/NPC identity, profile/self-model, cohort provenance, home/work/schedule and supported ownership links at the required scale.
- Individual Sim memory libraries, remembered-person references, event-grounded memories and private retained facts.
- Directional pair-specific familiarity, trust and relationship state, separated from historical encounter/conversation events.
- Persistent valet/concierge service events keyed to player, individual attendant, vehicle, service point, timestamp and outcome.
- Player health/table-health state, consumable item effects and purchase/consumption outcomes.
- Daily reward claim state, membership purchase/entitlement state and card reward provenance/eligibility, if those systems are to be server-authoritative.
- Detailed transit routes, station schedules, bus services, passenger trips and other transport operations.
- Full progression ledger/state for unified player level, stars, rank/title and qualifying XP events.

These are schema gaps, not a mandate to create every table immediately. Define contracts and access patterns first; avoid over-normalizing or inventing unapproved mechanics.

### Database correctness and migration blockers

1. The wallet constraint previously listed only three currencies. The draft has now been corrected to include `WINGS`, making the four-wallet contract explicit.
2. Canonical wallet naming must remain `HUSTLE_MONEY`; do not create a second Hustle Cash wallet.
3. The 1:1 chip conversion needs an atomic two-entry ledger transaction with idempotency, audit metadata and server-side authorization.
4. Table-health restoration needs authoritative item/effect/consumption records; the broader condition model is not finalized.
5. Sim memories, relationships and service events need sparse indexed records, directional ownership, privacy boundaries and retention/deletion rules.
6. RLS is enabled in the draft with no permissive policies. This is a safe starting posture, not a finished authorization model; define and test policies and trusted server operations before client access.
7. The active Supabase project must be positively identified as the Hustle City database. Do not reuse the separate Command Center Supabase project.
8. No migration should be applied until schema review, project confirmation, migration generation, tests and explicit creator approval.

## 6. Changes made during this audit

- Added this audit register and linked it from the repository root README.
- Updated the SQL draft wallet constraint and database README/data model/schema-gap wording to include all four currency codes, including `WINGS`.
- Clarified that poker-table food/drinks are intended to restore table health while the broader health/energy/condition model remains open.
- Reconciled the membership document to the approved 1:1 nominal chip conversion and approved card-acquisition channels; daily login currency rewards remain card-free.
- Corrected stale root README and database data-model status text.
- Updated the decision log and added explicit current-workforce overlays/supersession notices to workforce, assembly-line, IntelliSync status and mobile-AI-HQ documentation.
- Updated PR #11's description to reflect the current 17-role target, legacy runtime configuration and actual verification gates.

## 7. Required update sequence

**P0 — Canon reconciliation**
1. Publish this audit as the current cross-project gap register.
2. Resolve the workforce roster/config/docs conflict (17 local roles, external ChatGPT coordinator, 20/5/5, shared `main`).
3. Align the 1:1 conversion, card-acquisition channels and poker-table health restoration language across economy/gameplay/database docs.
4. Maintain a single current source for approved vs unresolved decisions; mark legacy 12+3/48-role and remote/branch-per-task documents as superseded rather than silently deleting history.

**P1 — Database design**
1. Add a reviewed conceptual Sim identity/profile model.
2. Design sparse Sim memory, encounter history and directional relationship records.
3. Design valet/concierge service-event history without cross-attendant memory transfer.
4. Design authoritative health/consumable, daily-reward, card-reward provenance and unified progression records.
5. Reconcile all four wallet codes and the atomic 1:1 conversion contract.
6. Define RLS, server/Edge Function ownership, retention, deletion, indexing and migration tests.

**P2 — Feature contract and implementation**
1. Turn launch-required venues and transportation into acceptance-tested playable slices.
2. Close device UX specifications and responsive interaction contracts.
3. Reconcile the world map, district/landmark catalog and building identities.
4. Verify Unreal builds, gameplay acceptance tests, CI and runtime agent workflows before claiming activation.

## 8. What remains explicitly unresolved

Do not invent: membership billing cadence and currency quantities; daily reward amounts/streak/catch-up/reset/caps; card odds and exact thresholds; health versus energy/hunger meters and decay/recovery values; wages and living costs; property prices/caps/rental/resale; premium-versus-earned vehicle/yacht/aircraft access; detailed transit routes/fares/schedules; Sim memory retention/deletion policy; exact schema/indexing/partitioning; full RLS policy matrix; device orientation/camera/breakpoints; final 17-agent-to-specialist domain mapping and verified local model availability.

## 9. Audit maintenance rule

Every new creator-approved requirement should be added to its canonical domain document and reflected in this audit register when it changes coverage, status or an unresolved dependency. Keep proposal status explicit. A repository commit is evidence of documentation only; implementation status requires code, tests, deployment/build evidence and acceptance verification.


## 10. Follow-up diagnostic — visual blueprint, districts and live Supabase (2026-11-24)

### New creator direction captured
- The city visual-production workflow now has **seven official districts**: Entertainment, Downtown Diamond, Trapper, Hustle, Swagger, Transportation and Financial.
- Transportation District is explicitly an official district centered on the airport, car lot/automotive destination and marina/yacht facilities. It is not merely the citywide rail/transit corridor. Rail and road networks remain connected citywide.
- Financial District is a separate official banking, finance and corporate-business district, distinct from Diamond District's luxury/prestige identity.
- Current approved color directions: Entertainment electric/cobalt blue; Diamond black/gold; Trapper blue/white; Hustle red/white. Proposed pending approval: Swagger purple/silver; Transportation slate gray/teal; Financial emerald/platinum-silver.
- Shuffle Club stays directly beside the beach on the right/east waterfront. The visual brief requires ten coordinated images per blueprint push, progressive zoom from city to district/block/building/interior, consistent camera/location registers and functional-geography QA (including a navigable harbor opening).
- New consolidated manuscript: `docs/VISUAL_WORLD_BLUEPRINT_AND_META_AI_MANUSCRIPT.md`.
- Tomorrow handoff: `docs/IMPLEMENTATION_DAY_HANDOFF_2026-11-25.md`.

### Canonical conflicts discovered and retained for resolution
- Existing top-down plan section 8 still says Transportation is a continuous corridor/system, not a boxed district. This is superseded by the creator's latest direction; preserve the citywide transit corridor as infrastructure while treating Transportation District as the airport/car lot/marina destination district.
- Existing plan includes older district/venue naming and color details. This conversation reasserts Booker Cole Theater and Jokes on You Comedy Club, while the current repository spatial plan contains Book of Code Movie Theater and Ain't You Funny Comedy Club. Do not silently erase either historical record; the latest creator instruction governs the new visual manuscript, and the name conflict needs creator confirmation before changing all legacy assets.
- Existing plan has prior Entertainment campus color blue/black; current creator direction says Entertainment District electric/cobalt blue. Use the current district color register in new visuals; retain any black campus detail only as a possible architectural accent, not a competing district palette.
- Airport, car lot and marina grouping is approved; exact parcels, airport runway orientation, shoreline geometry and district boundaries remain unresolved. Do not invent final coordinates.

### Live Supabase diagnostic
- Queried the Supabase account explicitly labeled **Hustle City** and identified project **Hustle City Shuffle Club**, project ref `jtkbtogtxfbtammdlewv`, region `us-west-2`, database engine Postgres 17, status `ACTIVE_HEALTHY`.
- Read-only table inventory for schema `public` returned **zero tables**.
- Migration history contains one migration: `20261122193313_harden_rls_auto_enable_event_trigger`.
- This confirms the game schema draft has not been deployed into the public schema of this project. No SQL or schema writes were performed during this diagnostic.
- Keep the database SQL draft as review-only until schema design, project/environment confirmation, RLS policies, migration tests and creator approval are complete.

### Repository and implementation diagnostic
- Reconfirmed foundation PR #11 is open, draft and unmerged; head `knowledge-library-foundation`, base `main`. Do not claim it is merged.
- Reconfirmed current 17-role target remains unreconciled with older runtime configs. Scheduler remains disabled pending group-aware execution, runtime permissions, full independent QA/correction workflow and tests.
- The existing `scripts/hustle-city-ai-relay.sh` is a legacy 14-slot provider relay, not the current 17-local-agent scheduler. It has hosted-provider paths and paid-provider branches guarded by `ALLOW_PAID_AI`; keep paid providers disabled. The expected `scripts/hustle-city-status.sh` and `intellisync/worker.py` paths were not found in this branch.
- Existing UserLAnd/USB/Ollama details conflict across prior sessions. The implementation handoff records known paths, commands and hard limits; verify the actual drive mount and Ollama host before moving or downloading models.

### Audit coverage limitation
This is an incremental diagnostic against repository files and connected live Supabase metadata, plus the conversation history/summaries available to this session. It is not a byte-for-byte audit of every raw historical chat message. No claim of complete transcript export is made.
