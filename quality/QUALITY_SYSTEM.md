# QA, Glitch Prevention and World Integrity

The objective is not only to make systems work on the happy path. The game must prevent, detect and recover from unusual states.

## Three layers
1. **Prevention:** constraints, validation, safe geometry, authoritative rules and robust state machines.
2. **Detection:** runtime assertions, telemetry, stuck-state detection, watchdogs and anomaly checks.
3. **Recovery:** safe repositioning, route replanning, state compensation and clear player feedback.

## Required test families
- Character: wall clipping, falling through floors, stairs, slopes and stuck navigation.
- Buildings: door state, simultaneous entry, elevators, seating, exits and inaccessible interiors.
- Vehicles: boarding while moving, full seats, door states, passenger desync and blocked paths.
- Traffic: deadlocks, red lights, protected turns, crossings, route conflicts and emergency braking.
- Transit: missed stops, blocked platforms, capacity, door timing and disembarking.
- Water/aviation: docks, swimming, inaccessible shore, boarding and safe return.
- Animation: interrupted transitions, rig mismatch, frozen states and overlapping gestures.
- Multiplayer: latency, disconnect/reconnect, duplicate entities, race conditions and event ordering.
- Economy: duplicate rewards, retries after timeout, replay and unauthorized balance changes.
- Events/NPCs: stale state, cancellation, hallucinated NPC answers and impossible schedules.
- Content pipeline: missing files, invalid metadata, unsupported formats and license gaps.

## Non-lethal player safety
No player death. Cars detect and stop for pedestrians; unexpected contact triggers safe stumble/reposition. Rooftop edges use barriers/warnings and safe recovery. Water can be intentionally swimmable in designated areas; if the player cannot exit safely, rescue/return. Train tracks and restricted areas require barriers or recovery. Preserve progress and possessions after accidental hazards.

## Quality gates
G0 requirements recorded and unknowns flagged.
G1 interfaces, scale, anchors, data ownership defined.
G2 unit tests pass.
G3 dependent-agent reviews and integration tests pass.
G4 end-to-end and failure-path scenarios pass.
G5 performance, security and accessibility checks pass where applicable.
G6 reproducible build, known issues documented and creator approval recorded.

Generated code or assets alone do not constitute completion.
