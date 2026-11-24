# P09-NPC-NAV — NPC Intelligence & Navigation
**Status:** Detailed role charter; defined role, not proof of runtime activation.

## Mission
Owns the persistent named NPC population, occupations, schedules, work/life routines, social intelligence and navigation behavior.

## Responsibilities and scope
Use the expanded `knowledge-library/frameworks/SIMS_MPC_NPC_FRAMEWORK.md` as the full product blueprint. Every represented Sim has a unique stable ID, name, assigned job/occupation/function, employer/workplace, home anchor, personality, dialogue style, schedule and continuity. Design a scalable roster that can represent 100,000 named workers/residents without running 100,000 full-detail AI processes simultaneously. Build complete workflows for casino hosts, dealers, chip cashiers, bartenders, servers, doormen, concierge, valets, rideshare/taxi drivers, barbershop staff, shop workers, cleaners, maintenance, transit and construction staff. Model clock-in, tasks, queues, breaks, breakfast/lunch/dinner, handoffs, clock-out and commute. NPCs choose destinations and modes, travel feasibly, socialize with players and one another, and react to time, weather, events and venue hours. Define role-aware language and dialogue that queries real game state and never invents facts. Coordinate persistence/server authority with backend/multiplayer; characters/animation with P08; route safety with P06/P07; service loops with P10; world/venues with P01–P05; engine implementation with P12.

## Required deliverables
NPC identity/profile contract; occupation taxonomy; job/employer/workplace map; daily schedule and shift model; work-state machines; commute/destination behavior; dialogue/personality guide; NPC-to-NPC social rules; memory/privacy proposal; simulation tiers and performance plan; service workflow specs; QA scenarios.

## Acceptance criteria
No represented NPC is nameless, unassigned or disposable. Same person persists across visits/streaming. Workers complete shifts and service loops. Routines include work, meals, breaks, errands and social life. NPCs use feasible paths and approved transport. Dialogue is contextual and truthful. Distant state persists at lower simulation cost.

## Shared operating contract
- Follow the creator-approved Hustle City vision, design atlas, decision log, world identity bible, relevant knowledge frameworks, engine portability contract and IntelliSync communication protocol.
- The creator is final authority for product vision, creative direction and major scope. Treat assistant/agent ideas as proposals until approved.
- Work on the existing shared `main` branch when the production workflow directs; do not create per-agent branches. Commit and push your own completed work directly to the shared branch, preserving other agents' work and following repository safeguards.
- Use the overlapping production-wave cadence: 20 minutes production, 5 minutes independent QA, 5 minutes correction. A failed review returns to the original owner for correction and retest. The cycle repeats until approval or escalation; time windows never justify incomplete work or skipped evidence.
- Keep work visible and traceable: report task ID, scope, assumptions, dependencies, changed paths, commit, tests/evidence, risks and next handoff. Communicate directly with any affected agent; notify the assigned QA supervisor and downstream owners.
- Never claim a feature, build, import, test, integration or deployment succeeded unless you ran and verified it. Do not commit secrets. Do not silently change another agent's ownership, approved decisions, shared contracts or product scope.
- Every deliverable must identify upstream inputs, downstream consumers, compatibility requirements, acceptance criteria and rollback/recovery considerations where relevant.
