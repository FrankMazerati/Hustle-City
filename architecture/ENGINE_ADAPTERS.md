# Engine Adapter Contracts

## Unreal Engine 5 adapter (primary)
Owns production runtime execution. Implement canonical interfaces for:
- World/location registry and streamed world cells.
- Character identity, appearance, and outfit loading.
- NPC behavior and event scheduling.
- Vehicles, road navigation, and rail transit.
- Social interaction orchestration.
- Missions, activities, economy, inventory, and progression.
- Save/load and telemetry hooks.

Use C++ for core runtime modules and Blueprints for composition and tuning. Expose explicit data import/validation boundaries.

## Unity 6 adapter (secondary)
Implements equivalent interfaces in C#. It consumes the same canonical schemas and source assets. It must not redefine game rules or fork canonical content definitions.

## Shared interface rules
- Stable string IDs; never rely on engine object names as canonical identifiers.
- Explicit success/failure result types and error codes.
- Deterministic validation and documented defaults.
- Versioned contracts and backward-compatibility policy.
- No direct cross-engine API calls.
- All time, distance, currency, and quantity fields declare units.
- All asynchronous operations define cancellation and timeout behavior.

## Conformance testing
Every shared contract should have:
- Valid fixture.
- Invalid fixture.
- Boundary fixture.
- Expected normalized result.
- Tests in shared tooling where possible and adapter-specific tests in each engine.

## Status vocabulary
Not Started → Specified → Adapter Implemented → Tested → Parity Verified.
