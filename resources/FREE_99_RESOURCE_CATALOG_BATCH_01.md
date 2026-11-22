# Hustle City Free 99 Resource Catalog — Batch 01

**Policy:** $0 acquisition cost, no paid subscription or required paid dependency, and commercial-game rights must be checked before production adoption. Unreal Engine-only content is only considered for the UE5 production branch. Nothing in this catalog is automatically approved for final shipping until the exact asset license and engine compatibility are recorded.

**Catalog status:** Research shortlist. No external asset files have been downloaded into this repository. This file records discovery, intended use, constraints, and next checks.

## Batch 01 — 20 free resources

| # | Resource | Type / likely Hustle City use | Cost evidence | License / compatibility notes | Status |
|---:|---|---|---|---|---|
| 01 | [Epic City Sample](https://www.fab.com/listings/4898e707-7855-404b-af0e-a505ee690e68) | Large urban sample; city systems, roads, traffic, crowds, buildings, world streaming | Fab listing says Free | Unreal Engine project. Check current Fab/Epic license at acquisition. Very high hardware requirements; use as a reference/source project on a capable workstation, not on phone/tablet. | Priority research |
| 02 | [City Sample Buildings](https://www.fab.com/listings/008fe959-5511-428e-93bd-f99b1179f6d5) | Modular walls, floors, facades, architectural pieces for original district buildings | Epic extracted sample pack | UE compatibility and license to be checked on its own listing. | Priority research |
| 03 | City Sample Vehicles | Vehicle meshes and related sample content for traffic/vehicle study | Linked as extracted content from City Sample | Check separate listing/license and whether assets can be adapted in UE game. | Research |
| 04 | City Sample Crowd | Crowd characters and crowd-system reference | Linked as extracted content from City Sample | Check separate listing/license; MetaHuman/crowd technical requirements apply. | Research |
| 05 | [Electric Dreams Environment](https://www.fab.com/listings/d79688f5-29be-4fb2-a650-2d4a813f5306) | PCG environment workflows, splines, large assemblies, vegetation distribution | Fab listing says Free | UE-only content; PCG/Substrate features in this sample include experimental features. Study the workflow; don't make experimental dependencies production-critical. | Priority workflow study |
| 06 | [Lyra Starter Game](https://www.fab.com/category/tutorials-examples) | Gameplay framework, input, UI, modular gameplay, multiplayer architecture study | Epic/Fab category lists Free | UE sample; inspect version and project license before reuse. Not a ready-made open-world social game. | Priority systems study |
| 07 | [Stack O Bot](https://www.unrealengine.com/unreal-engine-5) | Small playable sandbox, Blueprints, basic interaction and learning workflow | Epic page lists Free | UE sample project. Useful for learning and extracting small patterns, not a city base. | Study |
| 08 | [Content Examples](https://dev.epicgames.com/documentation/en-us/unreal-engine/content-examples-sample-project-for-unreal-engine) | Animation, materials, Blueprints, physics, lighting, rendering techniques | Epic learning sample | Epic documentation says examples can be opened, edited, and used in own levels. Confirm matching engine version. | Priority reference |
| 09 | [Cropout Sample Project](https://www.fab.com/listings/bd733d81-7c29-44fe-b53f-65b14d06a9e2) | Cross-platform patterns, Common UI, Enhanced Input, Geometry Script, Blueprints | Fab listing says Free | UE-only content. Its top-down farming game is not our genre; extract reusable engineering patterns only. | Priority systems study |
| 10 | [Valley of the Ancient](https://www.fab.com/listings/0c19880e-21bd-42ba-8287-1caccc3951b1) | Photoreal environment, World Partition, animation, lighting, audio reference | Fab listing says Free | UE-only. Very large download (listing reports 205 GB storage) and high-end PC requirements; not a phone download priority. | Reference only |
| 11 | [Game Animation Sample](https://www.fab.com/listings/880e319a-a59e-4ed2-b268-b32dac7fa016) | Third-person locomotion, traversal, motion matching, animation retargeting | Fab listing says Free | Epic sample; listing describes 500+ animations and UE5 mannequin compatibility. Verify engine version and reuse terms. | Priority animation study |
| 12 | [Project Titan](https://www.fab.com/category/tutorials-examples) | Architecture/construction and large environment production reference | Fab tutorial/examples category lists Free | Exact project scope, engine version, and license to be checked before adoption. | Research |
| 13 | [MetaHumans](https://www.fab.com/category/tutorials-examples) | High-quality human character creation and NPC visual reference | Fab category lists Free | Character tooling and service requirements may change; check account/service terms and runtime costs. | Research |
| 14 | [Niagara Examples Pack](https://www.fab.com/category/tutorials-examples) | VFX patterns: smoke, rain, sparks, ambience, environmental effects | Fab category lists Free | Epic sample; check UE version and license. | Study |
| 15 | [Meerkat Demo](https://www.fab.com/category/tutorials-examples) | Character animation, cinematic and creature/rig workflow reference | Fab category lists Free | Not directly city-life content; use only applicable animation/lighting techniques. | Optional reference |
| 16 | [A-COM Animation Sample](https://www.fab.com/listings/7a019296-852d-47b8-86ed-ddcf2835a352) | Rigging, animation, modular props, Sequencer, cinematic lighting and FX workflows | Fab listing says Free | UE5.6/5.7 sample; includes stylized content, so use pipeline techniques rather than its art style. | Study |
| 17 | [Poly Haven](https://polyhaven.com/) | Photoreal PBR surfaces, HDRIs, and selected 3D models for streets/buildings/interiors | Free; no account required | CC0; commercial use allowed; attribution not required but appreciated. Record individual asset IDs and optional credits. | Approved source library |
| 18 | [Kenney Train Kit](https://kenney.nl/assets/train-kit) | Rail spline prototypes, train/track blockouts for HIM/HCTA planning | Free download | CC0. Stylized/low-poly; prototype geometry only, not final realistic rolling stock. | Approved for blockout only |
| 19 | [Kenney Prototype Kit](https://kenney.nl/assets/prototype-kit) | Placeholder people, vehicles, buildings, props for interaction and scale tests | Free download | CC0. Prototype-quality visuals; do not present as final art. | Approved for blockout only |
| 20 | [Kenney City Kit (Suburban)](https://kenney.nl/assets/city-kit-suburban) | Quick neighborhood street/blockout and scale studies | Free download | CC0. Stylized and suburban; use for layout tests only, not final city art. | Approved for blockout only |

### Batch 01 quality and legal gates

- **Free price is not the same as permission to ship.** The source listing and applicable license must be checked at the moment the asset is acquired.
- Fab sample projects may be restricted to Unreal Engine-based products. Do not convert them into a standalone asset pack or redistribute source files.
- Kenney and Poly Haven CC0 resources can be used commercially; preserve creator/source metadata anyway as a courtesy and for provenance.
- Low-poly/stylized kits are permitted only for greyboxing, scale, layout, and interaction tests unless the Visual Director explicitly approves a stylized use.
- Never use a real brand's logos, trade dress, or copied architectural identity to create Hustle City's original venues.
- Do not import/download large packages onto the Android phone/tablet. Keep the browser workshop light; stage large files for the future workstation or external storage.

## Reusable UE5 workflows to catalog and configure

These are engine capabilities or documented workflows, not third-party paid plugins. Availability and stability must be checked against the selected UE5 version.

| # | Workflow / system | Reusable use in Hustle City | First configuration target |
|---:|---|---|---|
| W01 | Procedural Content Generation (PCG) | Repeatable block dressing, vegetation, props, street furniture | A small test block with deterministic seed and editable density |
| W02 | World Partition | Stream a large city in manageable regions | District-sized cells and loading-distance test |
| W03 | Data Layers | Toggle construction stages, traffic, crowds, interiors, day/night sets | Separate layers for shell, streetscape, interiors, traffic, crowds |
| W04 | One File Per Actor (OFPA) | Reduce world-file conflicts during multi-person editing | Confirm source-control workflow with a small shared test map |
| W05 | Splines and spline meshes | Roads, sidewalks, curbs, rail guides, fences, utility runs | Editable road/track segment with width, banking, and junction rules |
| W06 | Mass Entity / Mass AI | Crowd and traffic population at scale | One street-corner pedestrian test before city-wide deployment |
| W07 | StateTree | NPC behavior state logic | Pedestrian idle / walk / cross / wait states |
| W08 | Smart Objects | Interactable seats, counters, kiosks, help desks, doors | One reusable interaction point with reservation/availability state |
| W09 | Enhanced Input + Common UI | Consistent controller, keyboard, touch-friendly UI patterns | Input mapping contexts and scalable HUD/menu shell |
| W10 | Chaos Vehicles | Road vehicle physics and handling | One test vehicle with measured mass, wheelbase, suspension and braking |
| W11 | Niagara | Rain, mist, sparks, exhaust, environmental effects | One optimized rain/splash effect with quality levels |
| W12 | Lumen / Nanite / TSR | High-fidelity lighting, geometry, and scaling | Performance comparison on target workstation; never assume mobile support |
| W13 | Animation Blueprints / IK Retargeter / Motion Matching | Character locomotion, interaction animations, NPC animation reuse | One character locomotion set and retarget test |
| W14 | Sequencer / Control Rig | Opening cinematic, train arrival, camera choreography | HIM arrival previs using placeholder assets |
| W15 | Geometry Script | Procedural mesh operations and configurable construction tools | Parametric sidewalk/curb or simple building-shell generator |

## Ten-step resource intake workflow

1. Discover a resource from an official creator/publisher page.
2. Confirm current price is exactly $0 without a trial or required purchase.
3. Open the license and verify commercial-game use.
4. Record creator, title, canonical URL, license, attribution requirement, and retrieval date.
5. Record supported engine version, formats, dependencies, and file size.
6. Check whether it contains source assets, scripts, Blueprints, plugins, or only a demo.
7. Classify it as **production candidate**, **workflow reference**, **blockout only**, or **reject**.
8. Run a clean-project compatibility test on the intended UE5 version when a workstation is available.
9. Review visual quality, scale, performance, accessibility, and originality against Hustle City standards.
10. Only after approval, integrate it; preserve provenance and creator credits in the asset manifest.

## Next batches

- **Batch 02 — urban architecture:** free modular high-rises, commercial buildings, storefronts, interiors, roads, sidewalks, street furniture.
- **Batch 03 — rail and transit:** free station environments, rail splines, rolling-stock prototypes, signage, platform modules, passenger-flow workflows.
- **Batch 04 — gameplay Blueprints:** doors, elevators, interaction prompts, inventory, save/load, dialogue, NPC schedules, vehicles, UI.
- **Batch 05 — characters and animation:** free human assets, clothing, hair, retargetable animations, crowds, facial animation.
- **Batch 06 — world production:** procedural roads, city zoning, PCG tools, environment workflows, lighting, optimization and testing.

## Project constraints

- Primary engine: Unreal Engine 5. Unity 6 remains secondary; do not introduce Godot.
- Budget: $0 until the project has investor funding.
- User review: browser-first, mobile-friendly preview for Android phone/tablet.
- Full UE5 authoring, import, compilation, and high-fidelity validation require a capable workstation or remote workstation.
- Hustle Towers is in Diamond District, not Fashion/Swagger District.
- HIM is intercity/regional rail; HCTA is local city transit. They remain separate systems with planned transfer logic.
- Catalog entries do not authorize changing approved geography, district identity, rail alignments, or unresolved tower floor assignments.
