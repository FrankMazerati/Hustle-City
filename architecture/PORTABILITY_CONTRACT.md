# Engine Portability Contract

**Decision:** Unreal Engine 5 is the primary production engine. Unity 6 is the secondary compatibility and migration target. Godot is not an approved engine target.

## Boundary
The canonical game rules, data schemas, content identifiers, system contracts, and source assets are engine-neutral. Unreal and Unity implementations are adapters that realize those contracts in their respective runtimes.

## Portable by design
- City/district/building metadata, stable IDs, tags, and transforms.
- Character profiles, outfit manifests, NPC personality/behavior definitions.
- Vehicle specifications and tuning intent.
- Rail, road, route, and station metadata.
- Mission, activity, economy, inventory, and progression definitions.
- Social interaction definitions and event schedules.
- Save-data contracts and versioned migrations.
- Source meshes, textures, audio, motion capture, and interchange-friendly animation sources where licensing permits.

## Engine-specific by design
- Rendering pipelines, shaders, materials, lighting setups, post-processing.
- Physics implementations and vehicle solver details.
- Animation graphs/state machines and runtime retargeting.
- Input mapping, UI widgets, scene/actor/component hierarchies.
- Networking transport, replication, streaming, and platform packaging.
- Engine plugins, editor tooling, and build configuration.

## Required adapter pattern
Each engine adapter must:
1. Load and validate canonical shared data.
2. Map stable IDs to engine resources through an explicit registry.
3. Convert shared transforms and units through documented conversion functions.
4. Implement runtime behavior behind stable system interfaces.
5. Emit equivalent observable outcomes for shared conformance tests.
6. Keep engine-only fields in adapter-owned files, never in canonical shared schemas.

## Units and coordinates
- Canonical linear distance: meters.
- Canonical time: seconds unless a field explicitly says otherwise.
- Canonical angles: degrees.
- Canonical orientation: right-handed coordinate convention documented by the shared world spec; each engine adapter must convert to its native convention.
- No implicit unit conversions. Every importer/exporter documents scale, axis, forward direction, and handedness.

## Asset interchange
- Preserve original authoring files and source textures.
- Use glTF 2.0 for suitable static scene/mesh interchange and FBX where rigged animation workflows require it.
- Preserve PBR texture maps and material intent metadata separately from engine shader graphs.
- Do not assume shader graphs, physics assets, animation controllers, or procedural systems transfer automatically.
- Track asset source, license, attribution, and permitted modifications.

## Compatibility definition
A feature is portable when its canonical data and behavior contract can be consumed by both adapters and both implementations pass the same conformance tests. Similar appearance alone is not parity.
