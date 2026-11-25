> **SUPER AGENT CANON — 2026-11-25:** This file's earlier multi-agent workforce descriptions are historical and superseded wherever they conflict with [SUPER_AGENT_CHARTER.md](SUPER_AGENT_CHARTER.md), [SUPER_AGENT_MEMORY_ARCHITECTURE.md](SUPER_AGENT_MEMORY_ARCHITECTURE.md), and [SUPER_AGENT_PRODUCTION_CYCLE.md](SUPER_AGENT_PRODUCTION_CYCLE.md). Current target: one Super Agent production worker; ChatGPT is external Project Lead and independent QA; nine selective memory sections; 30-minute production blocks with the two-build review/correction handoff. The legacy role and model descriptions below are not an activation instruction.

# Hustle City Workforce Operating Model

> **Current creator-approved workforce overlay (2026-11-24):** This operating-model document contains earlier department/role descriptions. The current local workforce target is 17 agents: SCRIBE and LENS (parallel creative leads), QA-1 through QA-3, and P01–P12 (12 production specialists in three groups of four, each group owned by one QA supervisor). ChatGPT in the coordinating conversation is the overall coordinator; Trinity is not a locally running agent/model. Production uses overlapping waves with a 20-minute production window, 5-minute independent QA window and 5-minute correction window. The shared repository workflow is one shared `main` branch, not per-agent branches. The existing 12-specialist/3-QA configs and department mapping are legacy and must not be treated as the current roster or activated until reconciled. The 17-role target does not mean 17 workers are currently running.


**Status:** Roster, model assignments, department boundaries and policy are defined. Live workers are not yet activated. Runtime support and local-device verification remain required.

**Workforce governance:** The [WORKFORCE_AUTHORITY_CHARTER.md](WORKFORCE_AUTHORITY_CHARTER.md) is the controlling reference for authority hierarchy, decision rights, task lifecycle, role mandates, collaboration and escalation. The [AGENT_PROFILES.md](AGENT_PROFILES.md) contains detailed specialist instructions, required deliverables, acceptance expectations, handoff rules and model-aware evaluation. Read these together; neither changes model assignments or indicates live activation.

**Chain of authority:** Creator / Visual Director & Game Architect → Trinity (overall coordinator) → domain-owned production assignments. QA-1 → QA-2 → production owner → QA-3 is the independent defect-control path, audited by Trinity. QA stage authority is not a separate department command tier. Specialists report status to Trinity and retain authority only within their own defined domains.

## Leadership and departments

Trinity is the overall coordinator. Trinity assigns work, balances workloads, resolves cross-team dependencies, audits QA decisions, coordinates handoffs and escalates issues. Trinity does not silently rewrite creator-approved canon.

### Department 1 — World, City, Buildings & Streets
- **Atlas — World Architect:** world geography, terrain, scale, boundaries and world-to-city continuity.
- **Brick — City Builder:** city masterplan, district layout, blocks and urban circulation.
- **Blueprint — Building Architect:** building systems, architecture, interiors/exteriors, scale, structure and interaction anchors.
- **Route — Traffic & Navigation Director:** roads, intersections, signals, pedestrian/vehicle routes and navigation connectivity.

This is one integrated department because streets, buildings, city blocks and world geography must be designed against the same spatial rules. Its members coordinate directly before changing shared geometry, scale, coordinates or access.

### Department 2 — People, Appearance & Animation
- **Vibe — Sims Creator:** NPC behavior, social simulation, everyday life and contextual interactions.
- **Stitch — Fashion Director:** clothing, style, customization and character appearance.
- **Motion — Animation Director:** locomotion, gestures, interaction animations and motion continuity.

### Department 3 — Vehicles & Transportation
- **Torque — Vehicle Director:** vehicle design, behavior, physics requirements and integration.
- **Tracks — Transportation Director:** HIM, HCTA, stations, passenger circulation, transfers and transit operations.

### Department 4 — Gameplay, Events & Quality
- **Ace — Gameplay Director:** gameplay systems, activities, progression and player loops.
- **Spark — Events & Social Director:** city events, social experiences, player/NPC activities and event orchestration.
- **Lockdown — QA & Integration Director:** integration quality, regression planning, cross-system compatibility and release evidence. Lockdown does not replace the three independent QA supervisors.

SCRIBE (Story Director) and LENS (Cinematic Camera Director) remain separate peer creative leads under Trinity. Nexus remains the separate backend/multiplayer role. Their assignments are not silently folded into the 12-specialist roster.

## QA supervisor roles and routing

The three QA supervisors have distinct jobs. Their four-person supervisory scopes are retained as roster oversight assignments; the operational defect workflow is a separate three-stage process.

1. **QA-1 — Quality Intake & Evidence Analyst.** Finds and documents defects, missing requirements, bugs, visual/integration failures and reproducible steps. Records severity, expected versus actual behavior, evidence, affected systems and acceptance criteria. Sends a complete issue record to QA-2.
2. **QA-2 — Quality Triage & Routing Coordinator.** Reviews QA-1's report, identifies the responsible department and production owner, sets priority and dependencies, provides repair instructions, and tracks the assignment. Routes completed corrections to QA-3.
3. **QA-3 — Independent Verification & Release Analyst.** Tests the corrected artifact against the original issue and acceptance criteria. On pass, records evidence and releases that version. On failure, routes it to the responsible production agent. If the issue definition or evidence is unclear, sends it back to QA-1 for reassessment. The loop repeats until verified.

No QA supervisor may approve their own work. Trinity audits routing and QA records, resolves conflicts and handles escalations. A deadline never justifies unsupported approval.

**Implementation boundary:** the current IntelliSync scheduler performs a single configured QA review per station. The full QA-1 → QA-2 → production → QA-3 loop is specified here and in configuration but is not yet implemented in the runtime. Therefore scheduler activation remains disabled until the workflow is coded and tested.

## Model assignments and device limits

Each of the 12 specialists and three QA supervisors has one explicit local Ollama model assignment in `intellisync/config/agents.json`. The assignments use only models already reported as downloaded. A model assignment is a selection, not proof that a live agent process exists.

The mobile device is treated as a shared constrained host:
- one active local model inference at a time across the workforce;
- load the assigned model on demand and release it after idle where supported;
- never run two local models simultaneously for one agent;
- queue work rather than exceed memory or start competing workers;
- no more than one scheduler worker until measured device capacity justifies a change;
- Gemini/OpenRouter are disabled by default and may be used only after the exact model, zero-cost quota and data terms are verified; paid fallback is prohibited.

Trinity currently coordinates through deterministic runtime services and does not yet call an LLM. This avoids claiming an unconfigured coordinator model.

## Communication and collaboration

Every agent is part of one shared communication network. Department membership organizes work; it does not create silos.

Required routes:
- a department feed for each of the four departments;
- a team-wide feed for relevant shared announcements;
- a cross-department feed for shared interfaces, dependencies and integration;
- direct messages between any two agents, including between departments and QA supervisors;
- a command/escalation feed connecting Trinity and QA supervisors.

Agents may ask questions, share evidence, request expertise, flag risks and coordinate directly with any colleague. Notify only affected people unless a broadcast genuinely affects everyone. Keep decisions in canonical repository artifacts, not chat alone.

Every handoff should identify the task/package, artifact version, owner, status, dependencies, acceptance criteria, evidence, risks and requested next action. When changing shared geometry, coordinates, scale, schemas, APIs, asset formats, interaction anchors or simulation rules, notify affected teams before downstream consumers integrate the change.

### World-to-city-to-building-to-street collaboration

Atlas establishes world-scale and geography constraints. Brick translates those into city and district plans. Blueprint coordinates building footprints, height, entrances, circulation and interaction anchors against the city plan. Route coordinates road widths, sidewalks, crossings, intersections, traffic and pedestrian/vehicle navigation against both. They review shared spatial changes together; none may independently redefine the common coordinate system or move approved districts/roads/buildings without notifying affected owners and seeking required approval.

Other departments join when their work touches the shared world: Tracks for transit alignments and station access; Torque for vehicle envelopes and turning/boarding clearances; Vibe for pedestrian and NPC behavior; Stitch and Motion for character scale, clothing collision and animation clearance; Ace and Spark for gameplay and event spaces; Lockdown and QA supervisors for integration evidence.

## Continuous worker behavior

The intended continuous service is a persistent, supervised local worker loop, not a one-shot GitHub Action:
- start only after model endpoint, roster, access policy, group execution, QA routing and health checks pass;
- recover durable queued work after restart;
- claim work transactionally so two agents cannot own the same task;
- respect dependencies and QA gates;
- send heartbeats, progress, blockers and completion events;
- retry transient failures with bounded backoff; preserve tasks when providers or models are unavailable;
- pause safely on memory pressure, invalid configuration, repeated failure or missing approval;
- never bypass QA, alter approved canon, spend money or write to `main`;
- record every assignment, model, start/end, artifact version, QA result and handoff;
- continue checking independent eligible tasks while unrelated packages wait on blocked dependencies;
- support graceful stop and restart without losing queue state.

**Current state:** a bounded scheduler and one-cycle manual workflow exist, but the full group fan-out, permission enforcement and three-stage QA routing are not complete. No 24/7 service or phone-side daemon has been started from this repository connection. Keep the scheduler disabled until the activation checklist is satisfied.

## Active Directory-style group policy

See [ACCESS_CONTROL_POLICY.json](ACCESS_CONTROL_POLICY.json). It defines named security groups, explicit membership, scoped permissions, deny-by-default behavior, least privilege, audit requirements and restricted operations. This is an application-level RBAC policy specification; it is not a real Windows Active Directory domain and is not yet enforced by the current message hub.

## Activation gates

1. Validate all configured model tags against the live Ollama inventory and run one bounded inference per assigned model.
2. Implement group-aware task dispatch and message-feed access enforcement.
3. Implement the complete QA-1 → QA-2 → production → QA-3 loop, including rework to production or QA-1 reassessment.
4. Add queue recovery, heartbeat, health checks, graceful stop, logs and resource limits for continuous local operation.
5. Test permissions, cross-department collaboration, QA rejection/rework, duplicate events and restart recovery.
6. Confirm the local host has adequate memory/thermal headroom and that all model assignments resolve.
7. Only then enable the scheduler and report agents as online.
