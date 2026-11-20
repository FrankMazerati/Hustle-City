# Hustle City Engine Workspace

**Primary production engine:** Unreal Engine 5  
**Secondary compatibility target:** Unity 6  
**Godot:** Removed from the approved engine architecture and no longer an active development target.

This repository keeps engine-neutral game specifications and data separate from engine-specific implementations. Unreal Engine 5 is the authoritative runtime for production. Unity 6 is maintained as a documented adapter/migration target; do not build parallel gameplay features in Unity unless the project owner authorizes a migration or compatibility task.

## Workspace
- `unreal/README.md`: UE5 project conventions and implementation boundary.
- `unity/README.md`: Unity 6 adapter and migration conventions.
- `../SHARED_CORE/`: portable specifications, schemas, and engine-neutral rules.
- `../SHARED_ASSETS/`: source assets and interchange guidance.

## Important
This documentation establishes the repository architecture. It does not mean Unreal or Unity has been installed, an editor project generated, assets converted, or a game build compiled. Those steps require a compatible development computer and verified tooling.
