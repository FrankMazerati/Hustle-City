# Unity 6 — Secondary Compatibility Target

Unity 6 is the approved secondary engine compatibility target. It is not the primary production runtime and should not receive parallel feature development by default.

## Purpose
Maintain a clear migration path so engine-neutral game rules, schemas, content definitions, and source assets can be adapted to Unity without redesigning the entire game.

## Rules
- Implement Unity equivalents in C#; Unreal C++ and Blueprints are not directly portable.
- Read the canonical definitions from `SHARED_CORE/`.
- Preserve schema IDs, field meanings, units, enum values, and validation rules.
- Keep Unity-specific rendering, physics, animation, input, UI, and networking code inside this adapter.
- Record every feature's migration status: Not Started, Spec Mapped, Adapter Implemented, Tested, or Deferred.
- Do not claim parity until behavior and data compatibility tests pass.

## Rendering
Evaluate Unity 6 render-pipeline choice against the actual target platforms before implementation. Keep rendering-specific materials and shaders separate from source textures and material intent metadata.
