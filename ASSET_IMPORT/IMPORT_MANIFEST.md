# Hustle City — Asset Import Manifest

**Status:** Intake manifest; no source asset binaries have been imported yet.
**Primary engine:** Unreal Engine 5.
**Budget rule:** Free 99 — $0 acquisition, commercial use permitted, no subscriptions or paid dependencies. Preserve attribution when required.
**Import policy:** Verify the exact listing's license, supported engine version, download size, dependencies, and redistribution restrictions before adding files to the production project. Do not commit large binary packs to Git; store originals in the user's asset library/external drive and commit manifests, scripts, and project references.

## Priority 1 — first visual prototype

| Package | Intended use | Source | Current intake status |
|---|---|---|---|
| Epic City Sample | City environment, buildings, vehicles, crowd/traffic systems, Mass AI, ZoneGraph, Chaos Vehicles, Niagara, audio | https://www.fab.com/listings/4898e707-7855-404b-af0e-a505ee690e68 | Free; Unreal-only sample. Confirm compatible UE version and Fab/Epic terms in account before import. Large project; assess disk/RAM first. |
| City Sample Buildings | Modular building components for station, towers, streets | https://www.fab.com/listings/008fe959-5511-428e-93bd-f99b1179f6d5 | Free; UE-only content. |
| City Sample Vehicles | Traffic vehicle assets | City Sample related content | Candidate; verify separate listing and requirements before import. |
| City Sample Crowd | Crowd/NPC assets | City Sample related content | Candidate; verify separate listing, MetaHuman dependencies and terms. |
| Quaternius Downtown City MegaKit | Modular city blocks, storefronts, street pieces | https://quaternius.com/packs/downtowncitymegakit.html | CC0; standard download is free/name-your-price and includes FBX/OBJ/glTF. Source project tier is paid—do not select it. |
| Kenney City Kit | Roads, sidewalks, city props | https://kenney.nl/assets/city-kit | CC0 candidate; verify current package contents and formats before intake. |
| Kenney Train Kit | Train, tram, trolley, tracks and rail props | https://kenney.nl/assets/train-kit | CC0; 100 files listed. |
| Kenney Prototype Kit | Placeholder buildings, vehicles, characters and props | https://kenney.nl/assets/prototype-kit | CC0; 145 files listed. |
| Poly Haven | PBR materials, HDRIs, environment props | https://polyhaven.com/ | CC0; commercial use permitted; attribution not required (appreciated). |

## Priority 2 — sample projects and reusable systems

| Package | Intended use | Source | Current intake status |
|---|---|---|---|
| Electric Dreams | UE5 environment/PCG techniques and environment assets | https://www.unrealengine.com/ | Catalogued candidate; exact Fab listing, engine compatibility and terms to verify. |
| Lyra Starter Game | UE gameplay framework, input, multiplayer patterns | https://www.fab.com/ | Catalogued candidate; verify current UE version and terms. |
| Stack O Bot | Small UE sample project and gameplay examples | https://www.fab.com/ | Catalogued candidate; verify current listing and terms. |
| Content Examples | UE feature examples and reusable learning references | https://www.fab.com/ | Catalogued candidate; verify version and terms. |
| Cropout | UE sample game, gameplay and PCG patterns | https://www.fab.com/ | Catalogued candidate; verify version and terms. |
| Valley of the Ancient | UE environment/character sample | https://www.fab.com/ | Catalogued candidate; verify version and terms. |
| Game Animation Sample | Character locomotion and animation systems | https://www.fab.com/ | Catalogued candidate; verify version and terms. |
| A-COM Animation Sample | Animation workflow reference | https://www.fab.com/ | Catalogued candidate; exact listing and terms to verify. |
| Niagara Examples | VFX examples for rain, weather, water and ambience | https://www.fab.com/ | Catalogued candidate; verify version and terms. |
| MetaHumans | Character creation and sample characters | https://www.metahuman.com/ | Candidate; check current MetaHuman licensing, UE version and required services before use. |

## Additional systems to source

- Rail station, platform, track spline and train Blueprint templates.
- Traffic signal, lane-following, intersection reservation and pedestrian crossing templates.
- NPC pedestrian schedules, crowd behavior and ambient life.
- Vehicle traffic spawners and vehicle Blueprint examples.
- Train arrival/departure, door, boarding, disembarking and camera-sequence examples.
- Interior interaction, elevator, doors, room booking, dialogue and guided-tour systems.
- Hood character / neighborhood-life simulation templates. The phrase “Sim Hood” appeared in the planning discussion, but an exact verified package/source has not yet been identified. Do not substitute an unrelated product or assume a package was downloaded.

## Import sequence

1. Confirm the installed Unreal Engine version and target project version.
2. Download the small CC0 kits first (Kenney Train Kit, Kenney City Kit, Kenney Prototype Kit, Quaternius standard pack, selected Poly Haven assets).
3. Add the Epic City Sample and its extracted content through Fab/Epic Launcher, using the compatible engine version.
4. Create a clean staging project for each large sample; never migrate an entire sample blindly into the production project.
5. Inspect dependencies, plugins, redirectors, shaders, texture sizes, collision, LODs, Nanite use and runtime performance.
6. Migrate only the approved assets and Blueprints into the Hustle City UE project.
7. Record package version, source URL, license, attribution, import date, engine version, dependencies, and destination folder in the asset register.
8. QA each import in a test map before production use.

## First prototype asset targets

The opening sequence needs:
- Rainy passenger train exterior and rail track environment.
- Train interior/window and camera positions.
- Arrival platform and station exterior.
- Grand concierge hall.
- Hustle Towers exterior, interior lobby and enclosed courtyard.
- Bella Rose character and animation set.
- Room/interior dressing.
- Dialogue, guided-tour and room-booking interaction systems.

**Important:** The catalogued packages are not yet installed. This manifest is the controlled intake plan, not evidence of a completed download or Unreal import.
