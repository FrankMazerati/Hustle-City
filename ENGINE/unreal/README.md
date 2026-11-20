# Unreal Engine 5 — Primary Production Target

Unreal Engine 5 is the primary and authoritative runtime for Hustle City.

## Responsibilities
- Own the production game project, world runtime, rendering, physics, animation runtime, input, UI, networking integration, and platform packaging.
- Implement engine-specific systems in C++ and use Blueprints for composition, tuning, and designer-facing workflows.
- Keep engine-neutral rules and content definitions in `SHARED_CORE/`; Unreal code adapts those definitions to runtime objects.
- Use modular plugins/modules and stable interfaces for major systems.
- Keep source assets outside generated/imported engine caches.

## Required engineering practices
1. Use source control for project source and text-based configuration; do not commit generated build/intermediate/cache folders.
2. Pin and document the exact Unreal Engine minor version when the development workstation is selected.
3. Document every Unreal-only dependency and provide a Unity migration note where relevant.
4. Avoid putting authoritative economy, inventory, mission, NPC schedule, or interaction rules only inside a Blueprint graph.
5. Use automated tests for portable rules and Unreal automation tests for engine integration.
6. Profile representative city scenes; do not assume cinematic settings are viable on every target device.
7. Treat 8K as a supported cinematic/render-output target where hardware permits, not a minimum real-time gameplay resolution.

## Initial implementation sequence
1. Confirm workstation OS, GPU, RAM, and storage.
2. Install a selected UE5 release and matching toolchain.
3. Create the UE project and source-controlled module/plugin skeleton.
4. Implement adapters for shared schemas.
5. Build a representative Chicago-inspired vertical slice and profile it.
