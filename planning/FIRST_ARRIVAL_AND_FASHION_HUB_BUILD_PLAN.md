# Hustle City — First Build Workplan: Rail Systems + Central Districts

**Status:** Active foundation package on `world/master-geography-transit-foundation`.  
**Primary runtime:** Unreal Engine 5.  
**Mobile review path:** Browser preview in `web-preview/`.  
**No claim:** No UE5 project has been compiled and no public browser deployment has been verified.

## Workstream 1 — Hustle International Metro (HIM)
- Build the intercity passenger railway as a distinct authority and network.
- Establish the flagship central terminal and arrival/departure passenger flows.
- Support the opening arrival of Frank Maserati and his female companion.
- Design intercity rolling stock, platforms, concourses, luggage/arrival logic, wayfinding, and HIM/HCTA transfer.
- Keep origin city, exact terminal location, line geometry, station names, destinations in launch scope, and schedules unresolved until creator review.

## Workstream 2 — Hustle City Transit Authority (HCTA)
- Build local city and neighborhood passenger transit separately from HIM.
- Support elevated, underground, and street-level rail environments.
- Connect downtown, all six central districts, and every designated outer neighborhood.
- Design stations, platforms, access paths, vehicle/track compatibility, transfers, local service behavior, and passenger flows.
- Do not lock line count, route colors/names, alignment, station positions, fares, or schedules without map review.

## Workstream 3 — Diamond District / Hustle Towers
- Hustle Towers belongs in the **Diamond District**.
- The Fashion / Swagger District is separate and must not be used as the tower's location.
- Represent Hustle Towers as a 100-floor, vertical-first landmark.
- Avoid horizontal resort/campus sprawl.
- Reserve program for malls, multiple casino areas, multiple food concierge lounges, multiple welcoming help desks, Heavenly Hallway, and “kicking areas”.
- Retain Caesar's Palace as a creator-named element, with its relationship to Hustle Towers unresolved.
- Do not allocate exact floor numbers until a 100-floor program is reviewed and approved.

## Workstream 4 — Fashion / Swagger District
- Keep it as a distinct central district, separate from Diamond District.
- Develop its own visual identity, geography, streetscape, buildings, venues, and gameplay purpose from creator direction.
- Do not automatically place Hustle Towers or the Diamond District program here.

## Workstream 5 — Browser preview
- Provide mobile touch-friendly scene switching for HIM, HCTA, Fashion / Swagger District, and Diamond District / Hustle Towers.
- Use the browser as a review surface while UE5 remains the primary production runtime.
- Use low-cost static hosting if/when GitHub Pages is enabled.
- Keep the blockout clearly labeled and do not present primitive geometry as final high-fidelity assets.

## Build sequence
1. Validate and refine the interactive browser blockout on phone/tablet.
2. Creator review of rail separation, district separation, tower silhouette, and destination labels.
3. Recover original city map and locate Fashion and Diamond districts and transit corridors without inventing geography.
4. Produce measured rail/station and 100-floor architectural briefs.
5. Create UE5 module and content skeleton on a compatible workstation.
6. Implement HIM and HCTA data-driven rail infrastructure and initial passenger flows.
7. Implement Diamond District Hustle Towers floor registry, vertical circulation, and venue modules.
8. Develop Fashion / Swagger District as its own independent district.
9. Integrate lighting, materials, character movement, and cinematic First Arrival sequence.
10. Validate mobile browser preview and UE5 performance separately.

## Acceptance gates
- HIM and HCTA remain separate systems with an explicit transfer contract.
- HCTA has access coverage for every designated neighborhood.
- Six central districts remain distinct; Fashion and Diamond are never conflated.
- Hustle Towers has exactly 100 floors and is in Diamond District.
- Tower massing remains vertical-first.
- Every requested venue type appears in the program register.
- Browser scene switching works on touch devices and is honestly labeled as an early blockout.
- UE5 remains primary; Unity 6 remains secondary; no Godot work is added.
