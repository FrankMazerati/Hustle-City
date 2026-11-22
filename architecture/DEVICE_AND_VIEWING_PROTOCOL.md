# Hustle City Device, Production, and Viewing Protocol

**Status:** Creator-confirmed operating protocol  
**Budget context:** Free 99 — $0 until investor funding  
**Primary engine:** Unreal Engine 5; Unity 6 remains secondary.

## Confirmed device hierarchy

### 1. Primary production environment — laptop (best-case scenario)
When a suitable laptop is available, it is the preferred authoring and production machine. Intended work includes:
- Unreal Engine project authoring and editor use.
- Importing and organizing approved assets.
- Building and editing levels, Blueprints, materials, lighting, animation, and environments.
- Running scripts, project validation, packaging, and performance tests.
- Full-quality visual and gameplay review.

Do not assume any particular laptop is capable until its CPU, GPU, RAM, storage, and OS are checked against the chosen UE5 version and target project settings. If the laptop is not available or does not meet requirements, queue heavy work for an appropriate workstation rather than forcing it onto mobile devices.

### 2. Secondary viewing protocol — library browser
The browser is the remote review and approval surface:
- Open lightweight, responsive previews of city blockouts and scene layouts.
- Inspect district identity, building massing, streets, rail alignments, stations, and landmark placement.
- Review screenshots, short captures, diagrams, and progress reports.
- Approve or request changes without needing the full Unreal Editor.

Browser previews are companion visualizations, not the production game and not proof that a UE5 build has compiled. Where possible, keep previews lightweight, touch-friendly, and compatible with ordinary browsers.

### 3. Third viewing protocol — tablet
The tablet is a viewing and creative-review device:
- Open the browser preview.
- Review images, diagrams, documentation, and recorded walkthroughs.
- Inspect and approve visual direction and layout changes.
- Avoid heavy local 3D editing, large asset imports, engine builds, or compilation.

### 4. Phone — command and coordination
The phone is for:
- GitHub and project coordination.
- Reading reports and specifications.
- Agent status and task approvals.
- Quick communication and lightweight browser checks.

Do not assign heavy game-engine, model-training, large asset-processing, or compilation workloads to the phone.

## Workload placement rules

| Workload | Preferred location |
|---|---|
| UE5 authoring, asset import, level editing | Capable laptop/workstation |
| UE5 compilation, packaging, performance profiling | Capable laptop/workstation |
| Large environment/asset processing | Capable laptop/workstation |
| Lightweight browser preview | Library browser, tablet, or phone |
| Visual approval and design direction | Browser/tablet |
| GitHub documentation and task coordination | Phone, tablet, or laptop |
| Local AI model inference | Only on hardware verified to handle the model; otherwise queue or use an explicitly verified free option |

## Production architecture implications

- Build the actual game for the selected UE5 production target, not for mobile-device compute limitations.
- Treat browser compatibility as a separate review deliverable. Keep the preview implementation decoupled from the UE5 project so it can be inspected without running the engine.
- Keep project assets, source, documentation, and configuration under version control where licensing and file-size constraints permit. Use Git LFS or an appropriate asset store for large binary assets; do not commit licensed source assets to a public repository without permission.
- Use source-controlled project settings, naming conventions, asset manifests, and reproducible import/build instructions so work can move between machines.
- Do not claim a scene is production-ready because a browser blockout looks correct. UE5 import, lighting, collision, animation, performance, and gameplay must be validated on production hardware.
- If a suitable laptop is not yet available, continue with documentation, resource research, architecture, browser preview improvements, and small code/configuration tasks. Queue heavy engine tasks.

## Confirmation and change control

This protocol reflects the creator's requested priority:
1. Laptop — primary production, best-case scenario.
2. Library browser — secondary viewing protocol.
3. Tablet — third viewing protocol.
4. Phone — lightweight command and coordination.

Do not silently reverse this hierarchy or assume that mobile devices should run the game-development workload.
