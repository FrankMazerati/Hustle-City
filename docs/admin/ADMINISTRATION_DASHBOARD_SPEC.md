# Hustle City — Administration Dashboard Functional Specification

**Status:** Product/technical specification. This does not claim a dashboard is implemented, connected to live data or deployed.

## 1. Purpose

The Administration Dashboard is the secure operational control center for Hustle City. It gives authorized staff a truthful global view of the game, players, sessions, economy, rewards, missions, districts, businesses, live events, NPC simulation, moderation, support and service health.

It works across all supported cities and districts. It is not the player-facing Hustle City Fund and must not expose private player information to unauthorized staff.

## 2. Main navigation

1. Overview
2. Players
3. Live Sessions
4. Rewards & Economy
5. Missions & Progression
6. Cities & Districts
7. Businesses & Properties
8. Live Events & Activities
9. NPC & World Operations
10. Social & Community
11. Reports & Analytics
12. Support & Moderation
13. System Health
14. Admin Users, Roles & Audit Log
15. Configuration & Content Operations

## 3. Global overview

Show with clear timestamps and data freshness:
- Players online now (global concurrent online players).
- Players online by city, district, venue and platform.
- Active sessions, new sessions and session duration distribution.
- Daily active users, weekly active users and monthly active users.
- New registrations, returning players and retention cohorts.
- Server/region health and capacity.
- Active world events and participation.
- Active missions and progression distribution.
- Economy transaction volume and currency issuance/sinks.
- Reward campaigns currently running.
- Open support/moderation queues and high-priority alerts.
- NPC simulation, traffic, transit and venue service health.

Every metric needs a definition, time window, last-updated timestamp and source service. “Online” must distinguish connected, authenticated, in-world and actively interacting states where backend support exists. A stale heartbeat must not count as a live player.

## 4. Player directory and player detail

### Directory
Authorized staff can search and filter players by:
- Stable player ID and exact username.
- Registration date and last active date.
- Current online/session state.
- Current city, district and venue, where privacy/permissions allow.
- Platform, client version and server region.
- Level/progression and selected mission milestones.
- Account status, support flags and moderation status.
- Crew membership or event participation where access is justified.

Avoid broad access to real-world personal information. Display only the minimum data needed for the admin's role. Credentials, payment details, authentication secrets and private message contents are never shown in ordinary player views.

### Player detail
A player record may include:
- Player ID, username, avatar/profile summary and account creation date.
- Current session status, platform, client build and last heartbeat.
- Current city/district/venue if online.
- Progression level and relevant unlocked content.
- Four player currency balances: Hustle Money, Poker Chips, Wings and Diamonds.
- Inventory/collection summary and property/business ownership summary.
- Mission completion and branch outcome history.
- Relationship/reputation summary at a safe abstraction level.
- Reward history and economy ledger references.
- Support cases, moderation actions and account restrictions.
- Consent/privacy settings summary where operationally required.

Do not expose hidden canonical story state or future unrevealed content to players through admin-driven exports or ordinary support tooling. Staff access to narrative debug state requires a separate permission and audit trail.

## 5. Live sessions and global online players

- Real-time global online count with last-updated timestamp.
- Breakdown by city, district, venue, server region and platform.
- Session detail: session ID, player ID, connection state, join time, last heartbeat, latency and client version.
- Presence transitions: authenticated, loading, in-world, background/idle, disconnected.
- Capacity, queue and reconnect metrics.
- Filters for suspicious duplicate sessions, repeated reconnects or abnormal connection patterns.
- Operational ability to message, move to safe lobby, disconnect or flag a session only with explicit permissions and recorded reason.

Do not display a player as online solely because the account exists or the last session did not close cleanly.

## 6. Rewards and economy operations

### Player currencies
Keep the four player currencies distinct:
- Hustle Money
- Poker Chips
- Wings
- Diamonds

District-specific mission funds, business accounts and city operating budgets are separate ledgers and never appear as a fifth player currency.

### Reward console
Authorized staff can:
- Grant a configured reward to one player.
- Grant a reward to a validated cohort/segment.
- Run a scheduled campaign or event reward.
- Issue a correction/compensation after a verified incident.
- Preview the exact eligible audience and reward payload before execution.
- Set a reason, internal ticket/reference and optional expiry.
- Require second-person approval above configurable thresholds.
- Cancel a pending reward before execution.
- Inspect delivery status and per-player results.
- Retry failed deliveries idempotently without duplicate grants.

Reward types may include the four currencies, approved cards/packs, cosmetics, event rewards, access entitlements, XP/progression items and configured content. Every reward uses a versioned reward definition and validates eligibility.

### Ledger and fraud protection
- Every grant, spend, reversal and adjustment writes an immutable ledger event.
- Record actor, target, reason, amount, currency/item, before/after balance, source campaign, timestamp, correlation ID and approval.
- Use idempotency keys to prevent duplicate grants.
- Require explicit reversal entries; never silently rewrite historical ledger rows.
- Apply per-role limits, rate limits, anomaly detection and approval thresholds.
- Separate test/staging rewards from production rewards.
- Never use a direct balance edit when a ledger transaction is required.

## 7. Missions, story and progression operations

Staff with appropriate permissions can inspect:
- Mission catalog/version and publication state.
- Mission availability, prerequisites and active player counts.
- Completion, abandonment, failure and retry rates.
- Objective-level drop-off and branch selection.
- Reward definitions and delivery status.
- District-specific fund allocations and outcomes.
- Business and district outcome distributions.
- Character-card/story progression separate from five-card building/venue collections.
- Ambient narrative event eligibility and content version health.

A restricted narrative QA/debug view may inspect player knowledge flags, rumor status, source records and conversation eligibility. It must distinguish canonical truth from player-discovered knowledge. Ordinary admin views should not reveal future story spoilers unnecessarily.

Admin tools must not grant mission completion or reveal secrets to players without a documented support/QA action, reason, authorization and audit record.

## 8. City, district, business and property operations

### City/district view
- Current population and online distribution.
- District activity, active missions and event attendance.
- District-specific mission funds, allocations, spend, remaining balance and outcome.
- District financial condition indicators and trends.
- Business status, service disruptions and key relationships at aggregate level.
- Public-space, venue and transportation utilization.

### Business/property view
- Business identity, owner/operator and status.
- Revenue, operating costs, liabilities and recent transactions.
- Staff/service status, inventory and supply condition where supported.
- Mission-related losses/recoveries and player decisions.
- Venue open/closed state, capacity and active events.
- Property access, maintenance and upgrade status.

Keep player-owned business accounts, district mission funds and player wallet balances separate.

## 9. Live events and activities

- Event calendar and live event map/list.
- Event owner, district, venue, start/end, capacity and status.
- NPC-driven versus player-hosted event classification.
- Attendance, join/leave rate, completion and reward delivery.
- Moderation/safety flags and operational incidents.
- Pause/cancel/reschedule controls with role permission and reason.
- Event templates, versioning and approval workflow.

## 10. NPC and world operations

Operational visibility for:
- NPC population by simulation tier and region.
- NPC schedule and routine service health.
- Navigation failures, stuck NPCs and pathfinding load.
- Ambient conversation/event delivery volume and error rate.
- Conversation eligibility decisions and content version.
- Venue occupancy and crowd behavior.
- Traffic density, signal service, transit schedule and boarding status.
- Weather/world event state and district transitions.

NPC dialogue uses authoritative world state and bounded knowledge. The dashboard may support authorized QA inspection of why a line played, but must not convert internal canonical truth into player-facing dialogue.

## 11. Social, support and moderation

- Account reports and moderation queue.
- Player safety flags, block/report workflow and appeal status.
- Chat abuse metadata and authorized review tooling, with privacy controls and strict access.
- Crew and event administration.
- Support cases, account recovery workflow and compensation requests.
- Warning, temporary restriction, suspension and ban actions according to policy.
- Clear evidence, reason codes, expiry and appeal history.
- No unrestricted browsing of private conversations.

## 12. Analytics and reporting

Provide configurable date ranges, comparisons, exports and scheduled reports for:
- DAU/WAU/MAU, retention and session behavior.
- City/district population and travel patterns.
- Mission funnel and branch analytics.
- Card collection and building unlock progression.
- Business/property adoption and operation.
- Currency sources/sinks, inflation and reward campaign cost.
- Event discovery and participation.
- Social activity and referral conversion.
- Stability, performance, latency and support workload.

Exports must be permissioned, minimized, logged and protected against unnecessary personal data disclosure.

## 13. Admin roles and permission model

Use least privilege and explicit role-based access control. Suggested roles:
- **Platform Super Admin:** account/role management and emergency system controls.
- **Live Operations:** events, world health and operational controls.
- **Player Support:** player lookup, support cases and limited compensation workflow.
- **Economy Admin:** reward definitions, economy monitoring and approved grants.
- **Narrative/Content Admin:** mission, NPC, dialogue and content version inspection/publication.
- **Community Moderator:** reports, moderation actions and appeals.
- **Analytics Viewer:** aggregate dashboards and approved exports.
- **QA/Developer:** test environments, debug state and reproducible player/session inspection.
- **Read-only Executive:** aggregate global performance and alerts.

High-risk actions require step-up authentication and/or dual approval. No role can grant itself broader permissions through the dashboard.

## 14. Audit and security

Every privileged action records admin identity and role, action and target, before/after state or immutable transaction reference, reason/ticket, timestamp, request/correlation ID and environment, approval identity where required, and outcome/error details.

Security requirements:
- Server-side authorization for every action.
- No client-trusted currency or reward writes.
- MFA/step-up authentication for sensitive operations.
- Session timeout and secure admin access.
- Immutable audit retention policy.
- Rate limits, abuse monitoring and alerting.
- Redaction of secrets and sensitive personal data.
- Separate development, staging and production environments.
- Emergency actions with break-glass approval and post-action review.

## 15. Technical data sources and service contracts

The dashboard consumes authoritative APIs/events rather than arbitrary client state. Expected domains:
- Identity/account service.
- Presence/session service.
- Economy ledger and reward service.
- Inventory/collection service.
- Mission/progression service.
- City/district/business/property service.
- Event/world simulation service.
- NPC/ambient narrative service.
- Social/moderation/support service.
- Analytics/telemetry pipeline.
- Admin RBAC and audit service.

Use server-side pagination, filters, scoped queries, stable IDs, schema versioning, idempotent mutation endpoints and event-driven updates. Real-time counts should be sourced from presence/session heartbeats and reconciled against durable session records.

## 16. Initial release phases

**Phase 1 — Operational visibility:** global overview, online count, player directory, session view, service health, audit log and read-only mission/economy summaries.

**Phase 2 — Safe operations:** reward console with ledger, support cases, moderation queue, event operations and limited account actions with approvals.

**Phase 3 — Content and simulation operations:** mission/content versioning, district/business views, NPC/ambient narrative diagnostics, live event controls and world health.

**Phase 4 — Analytics and automation:** cohort campaigns, scheduled reporting, anomaly detection, economy balancing support and controlled operational automations.

## 17. Acceptance criteria

- Global online counts reconcile with authoritative presence/session records and show freshness.
- Admins can find a player by stable ID or username without broad access to sensitive account data.
- Reward grants are permissioned, previewed, reasoned, auditable and idempotent.
- Player wallet currencies are distinct from district funds and business accounts.
- Story mission cards and five-card building collections are separate in all admin views.
- Mission outcomes do not imply the player knows the hidden freight conspiracy.
- Ambient intelligence diagnostics show why a conversation was eligible without exposing spoilers to ordinary staff.
- Every privileged action is audited.
- Role restrictions are enforced server-side and covered by tests.
- Dashboard states distinguish live, stale, unavailable and estimated metrics.
