# Hustle City — Free 99 Modular Implementation Blueprint

**Branch:** world/master-geography-transit-foundation  
**Spend:** $0 only until investor funding. **Primary engine:** Unreal Engine 5. **Secondary:** Unity 6. **Review:** existing Babylon.js browser blockout.  
**Status:** integration architecture authored; third-party binary packages have NOT been downloaded or imported by this repository.

## Mission

Use free editable foundations to accelerate production, but create a distinctive Hustle City visual and technical blueprint. We will not merge sample projects wholesale or copy another game's identity. We will select suitable meshes, materials, procedural patterns, sample Blueprints and workflows, then rebuild around Hustle City's approved geography, style, gameplay and transport rules.

## Reusable foundation stack

| Foundation | Reuse | Limits |
|---|---|---|
| Epic City Sample UE 5.8 | PCG workflows, World Partition examples, building primitives, city organization, traffic/crowd/vehicle study | Do not inherit Matrix Awakens layout, brands, map or narrative |
| Epic City Sample Buildings | 2,000+ modular wall/corner/entrance/floor/pillar/rotunda modules | Recompose into original buildings |
| City Sample Vehicles and Crowd | Study and eligible sample components | Not automatically production-ready gameplay |
| Lyra Starter Game | Gameplay framework, input, modular architecture, multiplayer patterns | Do not wholesale-merge the sample game |
| Game Animation Sample | Locomotion and animation Blueprint patterns | Sample characters are not the final cast |
| Content Examples / Stack O Bot | Isolated Blueprint, material, physics and gameplay examples | Avoid monolithic sample merges |
| UNIBLOCKS FREE | Editor-side modular construction and its limited free templates | No PRO-only features; rectangular construction limitation |
| Quaternius Downtown City MegaKit Standard | FBX/OBJ/glTF pieces for massing and blockout | Free Standard only; stylized, not final realism; Source zip is paid |
| Kenney City Kit Roads | Roads, barriers, signs and traffic-control blockout | Low-poly, not final hero assets |
| Poly Haven | CC0 PBR surfaces, HDRIs and props | Apply Hustle City-authored material identity |
| ModKit / Lower Sector | Select CC0 modules after review | Only use parts appropriate to the district style |

Epic currently lists City Sample and City Sample Buildings as free; City Sample UE 5.8 uses PCG and includes building primitives. City Sample Buildings contains over 2,000 modules and is UE-only. Quaternius Standard is the free CC0 tier in FBX/OBJ/glTF; its Source tier is paid and excluded. Kenney Roads and Poly Haven assets are CC0. UNIBLOCKS FREE is distinct from PRO.

## Asset transformation pipeline

1. **Quarantine:** preserve untouched archive, creator/source, license, download date and hashes.
2. **Inventory:** list meshes, textures, materials, animations, Blueprints, plugins, sample maps and dependencies.
3. **Compatibility:** test in a clean UE project matching target engine; inspect plugins/settings before migration.
4. **Technical cleanup:** scale, pivots, normals, UVs, collision, LOD/Nanite suitability, material slots, texture sizes and naming.
5. **Visual conversion:** replace generic palette, materials, signage and branding; add original Hustle City wear, lighting, street furniture and identity.
6. **Modularization:** separate shells, interiors, entrances, service cores, roofs, props and variants.
7. **Gameplay integration:** interaction anchors, navigation, collision, doors/elevators, passenger paths, sockets, streaming and performance.
8. **Browser review:** produce lightweight proxy geometry. Do not claim Babylon.js is rendering UE assets unless a verified export pipeline exists.
9. **QA and creator approval:** visual, technical, licensing, performance and creator sign-off.
10. **Credit:** preserve provenance in project records and in-game credits where appropriate, even when optional.

Keep original third-party content separate from Hustle City modifications. Never overwrite the source.

## Reusable destination formulas

These are modular design contracts, not claims that the destinations or assets have already been built.

### 1. City block and street
**Kit:** road segments, curb, sidewalk, crosswalk, lane markings, streetlights, signals, hydrants, utility boxes, tree pits, transit furniture, storefront bays, corners, loading bays, alleys and props.

**Assembly:** road spline + sidewalk spline + intersection node + frontage bays + furniture sockets + pedestrian/traffic rules + district material/signage profile.

**Variants:** Downtown, Financial, Diamond, Entertainment, Marina, Fashion/Swagger and outer neighborhoods. Each has its own approved palette/frontage. Asset-kit dimensions do not define district boundaries.

**Sources:** City Sample PCG/building primitives, City Sample Buildings, Quaternius Standard and Kenney Roads for blockout, Poly Haven PBR.

### 2. Modular building shell
**Kit:** ground-floor entrance, repeatable wall/window/corner bays, floor slab, columns, roof/parapet, mechanical penthouse, fire/service core, loading dock, storefront, interior partitions, stairs and elevator core.

**Assembly:** footprint + grid-aligned façade bays + floor stack + vertical circulation core + service rules + roof silhouette + interior/exterior material profiles.

Keep entrance, loading, fire egress, accessibility and service access coherent. Separate exterior/interior shells where streaming benefits. Hero buildings need custom silhouettes and bespoke façade details.

**Sources:** City Sample Buildings, UNIBLOCKS FREE, Quaternius Standard and ModKit. Rework generic pieces visually.

### 3. HIM intercity terminal
**Program:** arrival/departure hall, ticketing/information, concourse, platforms, vertical circulation, accessible routes, staff/service rooms, wayfinding and city-facing arrival.

**Assembly:** terminal public spine + passenger circulation + platform modules + track approach + vertical access + service back-of-house + wayfinding.

Hustle International Metro (HIM) is intercity/regional. Frank Maserati and his female companion arrive via HIM from an unspecified other place. Do not invent origin city, terminal site, platform count or route alignment.

### 4. HCTA local rail stations
Build separate elevated, underground and street-level station variants.

- **Elevated:** platform/canopy, columns/foundations, vertical access, weather/noise protection, emergency egress and street interface.
- **Underground:** concourse, passenger zones, platform, ventilation/MEP zones, emergency exits, waterproofing and wayfinding.
- **Street-level:** platforms, safe crossings, signal interface, sidewalks and accessible boarding.

**Assembly:** station profile + parameterized platform length + verified track clearance envelope + passenger path graph + vertical access + safety/egress + signage + neighborhood skin.

HCTA is local. HIM and HCTA remain separate authorities, services, rolling stock and stations; connect only at designed transfer interfaces. No routes or station locations are invented here.

### 5. Rolling stock
Separate body shell, bogies/wheels, doors, interior seating, cab, lighting, passenger collision, boarding interface, animation/sound hooks, route/signal interface and LOD variants. Static train models are reference geometry, not functional railway systems.

### 6. Interiors and venues
Reusable interior shell, wall/floor/ceiling modules, lighting, doors, furnishing sockets, counters, seating groups, navigation graph, interaction anchors, audio zones and material profiles. Create variants for retail, restaurants, food concierge lounges, help desks, casinos, apartments, offices and entertainment. Do not assign Hustle Towers floors without approval.

### 7. Hustle Towers — Diamond District
100-floor vertical-first landmark, not a sprawling campus. Create custom silhouette, structural/service core, repeatable floor plates and façade systems. Requested program: malls, multiple casino areas, multiple food concierge lounges, multiple welcoming help desks, Heavenly Hallway, “kicking areas” (meaning unresolved), and Caesar's Palace (inside/attached/separate unresolved). Do not assign floors or invent definitions. Caesar's Palace is an original Hustle City destination name; do not reproduce the Las Vegas property's protected branding/trade dress.

### 8. Characters and social systems
Use Lyra for gameplay architecture patterns and Game Animation Sample for animation reference. Build original character rigs, clothing, hair, faces, locomotion, social behaviors, dialogue and interactions. Verify MetaHuman/plugin/platform requirements against target engine.

## Hustle City design conversion

Every adopted asset receives original layers:
- Architecture: district-specific proportions, façade rhythm, skyline silhouette, entrances, rooflines, signage and public realm.
- Materials: authored master materials/instances for concrete, stone, brick, glass, metal, asphalt, tile, rubber, wood and weathering.
- Identity: original typography, logos, wayfinding, street names and destination signs.
- Environmental storytelling: wear, maintenance, weather, lighting, props and neighborhood character.
- Gameplay: traversal, accessibility, interaction, navigation, social/commerce hooks and NPC behavior.
- Optimization: streaming, HLOD, Nanite/LOD policy, collision, texture budgets and browser proxy simplification.

The creator-approved world atlas takes precedence over any generic sample.

## Technical conventions — proposed test defaults, not locked decisions

- Unreal units are centimeters.
- Test a 100 cm review grid and 400 cm façade-bay increments; validate against actual source geometry.
- Parameterize station/platform dimensions against documented real-world references. Never estimate operating rail clearances from a visual asset.
- Naming: SM_ static mesh, SK_ skeletal mesh, M_ master material, MI_ material instance, T_ texture, BP_ Blueprint, DA_ data asset, PCG_ graph, LV_ level.
- Third-party content lives under Content/ThirdParty/Creator/Pack/. Modified Hustle City assets live under Content/HustleCity/SystemOrDistrict/. Do not overwrite third-party originals.
- Use data-driven profiles for district materials, station types, building footprints and variants.
- Profile full UE on capable target hardware; Android/browser review uses simplified proxy scenes, not full Nanite/Lumen expectations.

## Folder architecture

```
Content/
  ThirdParty/
    EpicGames/CitySample/
    EpicGames/CitySampleBuildings/
    EpicGames/CitySampleVehicles/
    EpicGames/CitySampleCrowd/
    Quaternius/DowntownCityMegaKit_Standard/
    Kenney/CityKitRoads/
    PolyHaven/<AssetName>/
    OtherCC0/<Creator>/<Pack>/
  HustleCity/
    Core/Materials/
    World/StreetModules/
    World/BuildingModules/
    Districts/Downtown/
    Districts/Financial/
    Districts/Diamond/
    Districts/Entertainment/
    Districts/Marina/
    Districts/FashionSwagger/
    Transportation/HIM/
    Transportation/HCTA/
    Transportation/Common/
    Landmarks/HustleTowers/
    Interiors/
    Characters/
    Gameplay/
    BrowserPreview/
```

## Acquisition and import procedure

1. Download only from the creator's official Fab/itch.io/site account or direct CC0 download.
2. Preserve the untouched archive in authorized local storage.
3. Stage by creator and pack.
4. Run the Free 99 intake scanner in tools/free99_asset_intake.py.
5. Manually verify exact license, $0 price and commercial-use permission; the scanner cannot establish legal rights.
6. Import Unreal-native Fab packages into a clean compatible UE project using the supported Epic workflow. Import FBX using UE tools; enable a glTF importer only if supported and approved in that engine build.
7. Validate scale, pivots, UVs, materials, collisions, LOD/Nanite, dependencies and performance.
8. Migrate only validated assets to the main project, preserving source folders and provenance.
9. Create browser proxies only for reviewed modules.
10. Mark ADOPTED only after validation and creator approval.

## Quality gates

License ($0 and commercial rights); visual (realistic proportions, topology, UVs, PBR and detail); engineering (scale, pivots, collision, LOD/Nanite, dependencies); environment (entrances, pedestrian circulation and service access); gameplay (interaction, navmesh, accessibility and safety); performance (draw calls, memory, streaming and HLOD); creator approval.

## Acquisition status

**Free candidates to add/download:** City Sample, City Sample Buildings, City Sample Vehicles, City Sample Crowd, Lyra, Content Examples, Stack O Bot, Game Animation Sample and UNIBLOCKS FREE (confirm current listing/version).

**Direct $0 files:** Quaternius Downtown City MegaKit Standard only; Kenney City Kit Roads; Poly Haven CC0.

**Selective candidates:** ModKit and Lower Sector after visual/technical review.

**Excluded:** paid train station packs, paid City Sample Source versions, paid Quaternius Source versions, paid plugins, trials and subscriptions.

**No third-party binaries are included in this commit.** This is the integration architecture and acquisition plan; downloads/imports require authorized asset-account access and a compatible Unreal workstation. The branch remains unmerged.
