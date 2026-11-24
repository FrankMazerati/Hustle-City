# Hustle City — Full-Day 17-Agent Production Schedule
**Prepared:** 2026-11-24 | **Execution target:** 2026-11-25  
**Status:** Creator-requested operating plan; planned work, not proof of activation. ChatGPT coordinating conversation is the overall coordinator; no local Trinity model is required.

## Mission and operating limits

Deliver tangible, reviewable Hustle City artifacts through a four-model/four-agent-at-a-time rotation. The 17 roles remain SCRIBE, LENS, QA-1–QA-3 and P01–P12. Success means at least one complete production → independent QA → correction → retest → accepted handoff, useful artifacts from all three production groups, and a verified next-day queue. Unreviewed output is not success.

**Concurrency:** Target up to four active local model sessions, only after a controlled memory/thermal test. Never exceed four. If four-way inference is unstable, use the largest stable number, even one-at-a-time. The roles can still rotate. A five-minute QA slot is for a small, pre-scoped package; if review needs longer, leave it pending rather than rubber-stamping it.

**Storage:** Reuse the workaround already established: tablet storage is exposed through Primitive FTPd and UserLAnd accesses it over the network using the configured SFTP service (historically port 1234). Verify current server address, account, port, permissions and read/write at startup. Do not revert to assuming UserLAnd must directly mount the USB drive. Do not assume the old IP remains valid. Keep the active Git working tree in its verified location unless Git operations on the SFTP-backed path are explicitly proven safe. SFTP file access is not automatically a native mounted filesystem; do not place a live Git working tree or Ollama model directory there without validating locking, rename and mount behavior.

## Roster and QA ownership

| Role | Mission / review ownership |
|---|---|
| SCRIBE | Story Director: narrative spine, opening sequence, Bella Rose voice, dialogue triggers, continuity |
| LENS | Cinematic Camera Director: shot language, choreography, transitions, travel/arrival, accessibility |
| QA-1 | Independent QA for P01–P04: geography, city plan, districts, architecture |
| QA-2 | Independent QA for P05–P08: interiors, transit, vehicles, characters |
| QA-3 | Independent QA for P09–P12: NPCs, gameplay, onboarding, Unreal integration |
| P01 | World Geography & Environment |
| P02 | City Masterplanning & Districts |
| P03 | District & Neighborhood Design |
| P04 | Architecture & Building Systems |
| P05 | Interiors, Venues & Environment Dressing |
| P06 | Rail, Transit & Transportation |
| P07 | Vehicles, Traffic & Simulation |
| P08 | Player Characters & Character Systems |
| P09 | NPC Intelligence & Navigation |
| P10 | Gameplay Interaction & Venue Systems |
| P11 | Onboarding & Story Progression |
| P12 | Unreal Integration & Asset Pipeline |

QA supervisors do not approve their own work. SCRIBE/LENS are peer creative leads, not substitutes for production QA. The creator remains final authority on product decisions and unresolved scope.

## Eight-hour day schedule (relative to T0)

T0 is the actual start time tomorrow; no clock-in time has been assumed.

| Block | Duration | Work | Exit condition |
|---|---:|---|---|
| 0. Startup | 30 min | Primitive FTPd/SFTP test; repo/branch; Ollama endpoint/model inventory; memory/thermal baseline; tests | Actual environment recorded; no guessed paths or duplicate downloads |
| 1. Creative brief | 30 min | SCRIBE/LENS briefs; package IDs, owners, acceptance criteria, dependencies | All tasks bounded and routed |
| 2. Group A | 90 min | P01–P04 with QA-1 | Four versioned world-foundation packages reviewed |
| 3. Group B | 90 min | P05–P08 with QA-2 | Four versioned spaces/mobility packages reviewed |
| 4. Group C | 90 min | P09–P12 with QA-3 | Four versioned living-city/gameplay packages reviewed |
| 5. Integration | 45 min | P12 and affected specialists; QA cross-boundary checks | Interfaces/conflicts/dependencies recorded |
| 6. Rework and second production pass | 60 min | Return failed packages to owners; run another 20/5/5 cycle on priority fixes or next bounded tasks | Priority defects retested; next packages advanced where ready |
| 7. Creative continuity/final QA | 30 min | SCRIBE, LENS and QA supervisors | Continuity review and defect disposition |
| 8. Commit/archive/next queue | 15 min | Package owners and coordinator | Accepted artifacts committed; logs backed up; next queue ready |
| **Total** | **8 hours** |  |  |

If startup overruns, protect QA and correction; shorten optional polish. If UE tooling is unavailable in UserLAnd, produce engine-neutral specifications, data contracts, validation scripts or source artifacts and clearly label what could not be built/imported.

## Four-agent rotation and 20/5/5

Each specialist cycle is 20 minutes production, 5 minutes independent QA, 5 minutes correction. Stagger the four workers' starts by five minutes where practical so QA submissions arrive in sequence. Pause/swap model sessions as needed to stay within the four-session ceiling. Each package is small enough to review; longer work remains pending. A downstream specialist may prepare a draft against existing approved inputs but may not call it integrated or consume an unapproved upstream artifact as final.

- Group A: P01, P02, P03, P04; QA-1.
- Group B: P05, P06, P07, P08; QA-2.
- Group C: P09, P10, P11, P12; QA-3.

SCRIBE and LENS work during the creative block and then consult with affected groups; they use model slots when available without displacing QA. Group members may work in parallel on separate bounded packages, but may not edit the same files or silently redefine shared contracts.

## Agent-specific assignments

### SCRIBE — Story Director
- Read approved vision, decision log and P09/P10/P11 contracts.
- Draft a launch story spine: arrival, city orientation, meaningful social/venue encounter, first poker/social activity and return-to-world loop.
- Define Bella Rose voice, personality, conversational boundaries and context-specific welcome/help lines.
- Build a dialogue trigger matrix: trigger, speaker, preconditions, intent, player options, state outcome.
- Write 2–3 short scene briefs for P08/P09/P11; coordinate beats with LENS.
- Mark new names/lore as proposed; do not invent unavailable features.
**Outputs:** launch story spine; Bella Rose voice/dialogue library; dialogue trigger matrix; review notes.  
**Pass criteria:** each beat has trigger, speaker, context, player outcome and dependencies; no canon conflict; downstream owners can implement it.

### LENS — Cinematic Camera Director
- Read SCRIBE beats and player/UE5 constraints.
- Define camera states, control ownership, framing/FOV intent, transition timing ranges and interruption behavior.
- Produce shot briefs for opening arrival, city reveal, venue entry and one travel/passenger sequence.
- Specify no-clipping/no-obscured-controls, multiplayer ownership, aspect-ratio and motion-sensitivity alternatives.
- Coordinate with P08, P10, P12, P06 and P07; do not invent geography.
**Outputs:** cinematic style guide; opening shot list; camera state/transition contract.  
**Pass criteria:** each shot has purpose, start/end state, framing, control handoff, recovery and test notes.

### QA-1 — World Foundation (P01–P04)
- Create checks for scale/coordinates, terrain/water, city connectivity, district canon, building access and provenance.
- Review exact versions from P01–P04; record PASS, FAIL or BLOCKED separately.
- Verify marina open-channel/ocean access, water continuity, road/rail continuity and district adjacency.
- Keep approved and proposed district colors separate; flag unresolved parcels/names/dimensions.
- Return evidence-based defects and independently retest corrections.
**Outputs:** four versioned QA records, defect log, Group A release recommendation.  
**Pass criteria:** no approval without artifact evidence; critical spatial/access defects block handoff.

### QA-2 — Spaces and Mobility (P05–P08)
- Check interior circulation, entrances/exits, service points, seating, accessibility and staff routes.
- Check transit continuity, station access, boarding/disembarking and transfers.
- Check vehicle envelopes, road fit, parking/garage access, automated travel and safety cases.
- Check character scale, rig, clothing fit, interaction reach and animation compatibility.
- Test building→interior, station→transit, vehicle→road and character→animation handoffs.
**Outputs:** four versioned QA records, cross-package defect list, Group B release recommendation.  
**Pass criteria:** no critical blocked circulation, unsafe movement, broken boarding, severe rig/clipping or missing evidence.

### QA-3 — Living City and Gameplay (P09–P12)
- Check stable NPC identity, schedules, memory boundaries, navigation and truthful state-aware dialogue.
- Test interaction preconditions, confirmation, authoritative outcomes, cancellation/recovery and anti-duplication.
- Review onboarding/story continuity, skip/revisit behavior and accurate currency/transport explanations.
- Inspect UE5 asset naming/import metadata, references, scale/collision expectations and validation steps.
- Require end-to-end evidence; return defects to original owners and retest independently.
**Outputs:** four versioned QA records, end-to-end scenario set, Group C release recommendation.  
**Pass criteria:** no identity reset, fabricated service/transaction state, onboarding blocker, safety bypass or unverified integration pass.

### P01 — World Geography & Environment
- Audit world identity/masterplan references; extract approved geography only.
- Produce coordinate/scale constraints: units, axes/orientation, shoreline/water boundaries, elevation assumptions and unknowns.
- Create water-access checklist: navigable access to waterfronts/islands; marina visibly open to ocean through a channel; no trapped basin; continuous bridges/causeways/water routes.
- Define climate/vegetation zones and reference provenance fields.
- Identify conflicts without relocating approved landmarks.
**Outputs:** geography constraints sheet; water/access checklist; provenance register; unresolved-geography list.  
**QA:** QA-1. **Downstream:** P02/P03/P04/P06/P07.

### P02 — City Masterplanning & Districts
- Convert approved seven-district and 7x7 references into a versioned city/district index.
- Record adjacency, known landmarks, access corridors and unresolved boundaries/parcels.
- Preserve approved colors: Entertainment electric/cobalt blue; Downtown Diamond black/gold; Trapper blue/white; Hustle red/white. Swagger purple/silver, Transportation slate gray/teal and Financial emerald/platinum-silver remain proposed.
- Keep Transportation and Financial distinct; Diamond is luxury/prestige, Financial is banking/corporate.
- Audit continuous road/rail connectivity and southwest outer-city train station; do not invent geometry.
**Outputs:** district index; adjacency/connectivity matrix; unresolved boundary register; map-layer schema.  
**QA:** QA-1. **Downstream:** P03/P04/P05/P06/P07.

### P03 — District & Neighborhood Design
- Create identity sheets for all seven districts; separate approved identity from proposed details.
- Index placements: Shuffle Club beside beach on right/east waterfront; Get Wild Beach distinct from Monster Beach; Monster Beach within Upper Level Entertainment Studios grounds.
- Record nearby but distinct Upper Level Entertainment Studios & Production (including Monster Beats) and Upper Level Films campuses.
- Preserve venue naming discrepancy for creator resolution; do not silently replace legacy names.
- Preserve nuanced Trapper/Hustle contrast without stereotypes.
**Outputs:** district identity matrix; landmark/venue register; name discrepancy register; unresolved placement questions.  
**QA:** QA-1. **Downstream:** P04/P05/P09/P10/SCRIBE/LENS.

### P04 — Architecture & Building Systems
- Define modular building brief: declared units, floors, footprint, entrances/exits, vertical circulation, access anchors, collision/navigation and exterior/interior handoff.
- Create archetype briefs for ordinary street building, entertainment venue and large landmark; do not invent final dimensions.
- Specify front/back/left/right elevation references and street context with consistent orientation/placement.
- Record parking/garage/service access, accessible routes, loading and egress.
- Define asset metadata/naming for P12.
**Outputs:** modular building spec; three archetype briefs; access/anchor checklist; metadata template.  
**QA:** QA-1. **Downstream:** P05/P09/P10/P12.

### P05 — Interiors, Venues & Environment Dressing
- Define interior layout contract: entrances, circulation, counters, seating, service points, exits and staff routes.
- Create one vertical-slice venue interior from already approved scope; if selection is unresolved, make a venue-neutral template.
- Define dressing layers and day/night lighting handoff.
- Coordinate Shuffle Club, Hustle Towers, beach and studio references without changing approved adjacency.
- Add accessibility, queue and NPC clearance checks.
**Outputs:** interior contract; venue/template package; furniture/service-point metadata; dressing checklist.  
**QA:** QA-2. **Dependencies:** P04. **Downstream:** P09/P10/P12.

### P06 — Rail, Transit & Transportation
- Build continuity register for elevated rail/L, subway, bus and station links.
- Define route/station/stop fields, transfers, passenger flow, boarding/disembarking and accessibility.
- Include southwest outer-city station; connect districts rather than isolated set pieces.
- Coordinate Transportation District airport/marina/car destination access with P01/P02/P07.
- Flag unapproved alignments and station parcels.
**Outputs:** transit schema; connectivity diagram; boarding/transfer state spec; unresolved alignment register.  
**QA:** QA-2. **Downstream:** P07/P09/P10/P12.

### P07 — Vehicles, Traffic & Simulation
- Define vehicle envelope/anchor metadata for cars, buses, trains, boats and aircraft; do not attempt every asset class without tools/assets.
- Specify automated destination travel, driver/passenger roles, boarding, arrival and disembarking.
- Define pedestrian/vehicle interactions, intersection conflicts, safe stopping and deadlock recovery.
- Check parking/garage entrances, valet handoff, marina docking and airport runway/taxiway separation.
- Produce test matrix for route continuity, blocked roads, occupied destinations and interrupted travel.
**Outputs:** mobility interface contract; vehicle anchor schema; traffic/travel state diagram; safety test matrix.  
**QA:** QA-2. **Dependencies:** P01/P02/P06. **Downstream:** P09/P10/P12.

### P08 — Player Characters & Character Systems
- Define character scale/rig/body customization slots, interaction reach and collision assumptions.
- Produce diverse, respectful character visual specification emphasizing Black representation and contemporary urban fashion/swagger without caricature or district stereotyping.
- Define wardrobe taxonomy for everyday, work, nightlife, beach/resort, athletic and weather-aware contexts.
- Specify animation/rig fit, camera framing and portrait/profile consistency.
- Keep age/romance safeguards explicit; never sexualize minors.
**Outputs:** scale/rig contract; visual representation/style guide; wardrobe taxonomy; character-sheet metadata and QA checklist.  
**QA:** QA-2. **Downstream:** P09/P10/P11/P12/SCRIBE/LENS.

### P09 — NPC Intelligence & Navigation
- Define stable NPC identity/profile, job/workplace/home anchors, schedules, shifts, routines and simulation tiers.
- Design a representative small cohort data contract that scales toward the population target without full-detail AI for every NPC.
- Specify person-specific memories grounded in actual interaction; no copying trust/memory between NPCs; exclude private data from public profile.
- Define role-aware valet/concierge/server/front desk/transit workflows; NPCs must check authoritative state before claiming completion.
- Produce commute/navigation state diagrams and stuck-route recovery.
**Outputs:** identity/profile contract; schedule/shift model; memory/privacy rules; service workflows; simulation-tier proposal; QA scenarios.  
**QA:** QA-3. **Dependencies:** P05–P08. **Downstream:** P10/P11/P12.

### P10 — Gameplay Interaction & Venue Systems
- Define interaction contract: prompt, range, preconditions, choices, confirmation, authoritative action, result, cancel and recovery.
- Specify one end-to-end interaction slice grounded in approved scope; do not invent launch rules.
- Preserve poker-first social lifestyle positioning and separate Hustle Money, Poker Chips, Diamonds and Wings.
- Include server-authoritative service/purchase state, idempotency and anti-duplication where relevant.
- Document NPC consent, social boundaries, accessibility and multiplayer ownership.
**Outputs:** interaction contract; one activity/service flow; state diagram; acceptance/edge-case tests.  
**QA:** QA-3. **Dependencies:** P05/P08/P09. **Downstream:** P11/P12/SCRIBE.

### P11 — Onboarding & Story Progression
- Map first-time journey: arrival, avatar/account setup, phone/HUD/map, transport, first venue/poker/social experience and return loop.
- Integrate SCRIBE's beats and Bella Rose voice; do not invent conflicting lore.
- Create optional tutorial prompts with skip/revisit and accessible pacing.
- Explain currencies/basic transport accurately; do not promise future features.
- Define persistent tutorial completion state and acceptance scenarios.
**Outputs:** onboarding journey map; tutorial trigger matrix; Bella Rose integration brief; skip/revisit model; QA scenarios.  
**QA:** QA-3. **Dependencies:** SCRIBE/P08/P09/P10. **Downstream:** P12.

### P12 — Unreal Integration & Asset Pipeline
- Audit UE5 scaffold and actual tool availability; do not claim a build if Unreal tooling is unavailable in UserLAnd.
- Define source folder/naming/version, asset metadata, import validation, scale/material/collision/rig checks and dependency manifests.
- Create a small validation script/schema validator runnable in the available environment; add tests where feasible.
- Manifest each accepted package with source, version, owner, QA record and downstream consumer.
- Preserve engine-neutral contracts; Unity 6 remains secondary.
- Do not integrate unapproved/failed packages or commit secrets/large unreviewed binaries.
**Outputs:** UE5 integration audit; asset metadata contract; package manifest; runnable validator/tests where feasible; build/tooling blocker report.  
**QA:** QA-3. **Dependencies:** all groups.

## Handoffs and repository rules

Every package includes a unique ID/version, owner, QA owner, scope/exclusions, approved inputs, assumptions/unknowns, changed paths, acceptance criteria, evidence/tests (or reason not run), defects, downstream owner and commit SHA. Suggested IDs: HC-1125-A-P01-001, HC-1125-B-P05-001 and HC-1125-C-P09-001. Corrections create a new version; preserve earlier QA evidence.

QA outcomes: PASS, FAIL—RETURN TO OWNER, or BLOCKED—DEPENDENCY/TOOLING/CREATOR DECISION. A pass releases only the exact reviewed version. "Agent says done" is not acceptance.

- Keep foundation documentation on knowledge-library-foundation / PR #11 until creator approves merge. Do not confuse this foundation PR with later production on shared main.
- No per-agent branches; avoid concurrent edits to the same file. Use task ownership/file claims and small commits.
- No paid providers/calls, credential exposure, Supabase changes, merges or deployments without explicit authorization.
- No database schema is deployed by this schedule.
- A concept image is not automatically a production-ready 3D asset.
- Do not claim workers, concurrency, builds, imports, tests, storage or deployment are live until verified.

## Day-end definition of done

- [ ] Primitive FTPd/SFTP verified from UserLAnd with safe read/write test; private credentials kept out of Git.
- [ ] Repository branch, status and remote verified.
- [ ] Model inventory captured; duplicates avoided; four-way concurrency tested or safely reduced.
- [ ] All 17 roles have a task status: queued, in progress, submitted, passed, rework, blocked or complete.
- [ ] P01–P12 each submit one bounded artifact or a documented blocker with evidence.
- [ ] QA-1/QA-2/QA-3 record independent reviews for their groups.
- [ ] SCRIBE and LENS submit creative packages and cross-check downstream consumers.
- [ ] At least one full production → QA → correction → retest cycle is evidenced.
- [ ] Accepted artifacts committed/backed up; unreviewed output not called approved.
- [ ] Next-day queue, open defects and resource limits recorded.

**Build something real tomorrow with the resources available now. Storage expansion and a larger model library improve throughput later; they are not prerequisites for beginning bounded, reviewable production.**
