# Hustle City — Master AI Context

**Purpose:** This is the shared project briefing for every AI model and agent assigned to Hustle City. The coordinator/runtime should load this document into each task's context. Ollama models do not automatically retain this information across independent sessions; the runtime must inject it when creating a task.

**Authority:** The creator is the Visual Director and Game Architect and retains final approval over creative direction, canon, scope and major architectural decisions. Treat proposals as proposals until approved.

## 1. Project identity

Hustle City is a cinematic, realistic 3D open-world social/city-life game. The long-term target includes an explorable city with districts, streets, transit, trains, vehicles, pedestrians, characters, businesses, interiors, social interactions and activities.

Target experiences:
- A packaged Windows desktop game built with Unreal Engine 5.
- An optimized browser-playable experience, including tablet touch controls.
- Unreal Pixel Streaming may be evaluated for streaming the full Unreal experience to browsers. A Windows executable does not run natively inside a browser.

## 2. Creative direction and world identity

The creator directs visual identity, aesthetics, city layout, neighborhood identities, gameplay vision and overall architecture. AI agents perform scoped research, implementation, integration, documentation, testing and coordination.

Preserve the distinction between the two established districts:

### Hustle District
- More upscale, polished and attractive in appearance.
- Higher-end businesses and clientele.
- Developed urban environments and premium destinations.
- Street-level hustling still exists; the district is not crime-free.

### Trapper District
- Distressed, lower-income, gritty urban environment.
- Includes liquor stores, churches, convenience stores, residential houses, trap houses, weed spots, dope spots and neighborhood businesses.
- Portray people facing addiction and economic hardship as part of the world's social reality, not as a caricature.
- Street-level trapping and hustling are part of the district's identity.

Do not flatten these districts into one generic city aesthetic.

## 3. Engine and platform direction

- **Primary production engine:** Unreal Engine 5.
- **Secondary compatibility/migration target:** Unity 6.
- **Godot:** retired as an active production target; preserve historical work but do not silently restart it.
- Use modular, maintainable systems and shared data contracts where practical.
- Keep the browser target in view without replacing Unreal as the primary production engine.
- Do not claim a Windows build, browser build, Pixel Streaming deployment or playable feature exists until it has been built and tested.

## 4. Tablet and keyboard controls

The intended browser controller supports touchscreens and physical keyboards.

### Movement
- Up arrow: move forward.
- Down arrow: move backward.
- Left arrow: move/turn left, according to the active camera/control scheme.
- Right arrow: move/turn right, according to the active camera/control scheme.

### Action buttons
- **A:** jump; contextual climb or vault where supported.
- **B:** run/sprint; support hold or toggle behavior as designed.
- **C:** interact, talk, open doors, enter/exit vehicles and activate nearby objects.
- **G:** contextual gestures such as greetings, waves, high-fives and other approved social animations.

Actions should be context-sensitive and eventually remappable. A proposed action is not an implemented feature until tested.

## 5. Assets and provenance

The creator has claimed a collection of free packages through the Epic Games/Fab ecosystem. Previously discussed categories include:
- City Sample / city-building environment assets.
- Train and railway assets.
- People / character creation assets.
- Character animation.
- Vehicles, props and environment assets.

Fab is the account/library source for claimed packages. The exact package list and local download/import state must be verified against the creator's Fab library and project asset register. Never state that an asset is downloaded, imported, licensed for a particular use or tested unless verified. Do not buy duplicate assets.

Large binary asset packages and packaged builds belong on the external SSD or another approved asset store, not in ordinary Git commits. Keep source code, manifests, metadata, import instructions and documentation in GitHub.

## 6. Workforce and authority

### Local Hustle City workforce target: 17
- 2 creative leads: **SCRIBE** (story/narrative direction) and **LENS** (cinematic camera direction).
- 3 QA supervisors.
- 12 production specialists.

### External coordinator
ChatGPT serves as the overall coordinator and is not a local Ollama agent/model. Trinity does not need to run as a local model.

### Command center
Maximus Optimus has a separate 7-agent command-center workforce. The combined target is 24 agents, but this is a target roster, not proof that 24 live workers are currently activated.

The canonical Hustle City roster and QA ownership are in `intellisync/config/coordination.json`. The 48-entry agent catalog is a reusable capability catalog, not 48 active workers.

## 7. Verified local Ollama inventory (2026-11-23)

The creator ran `ollama list` in Termux while the external SSD was connected. The following six models were visible in that Ollama instance:

| Model | Ollama-reported size |
|---|---:|
| `deepseek-r1:1.5b` | 1.1 GB |
| `gemma3:1b` | 806 MB |
| `qwen3:1.7b` | 1.4 GB |
| `llama3.2:3b` | 2.0 GB |
| `gemma2:2b` | 1.6 GB |
| `qwen2.5:1.5b` | 986 MB |

Earlier discussions mentioned 14 models, but only these six were visible in the current verified `ollama list`. Do not claim the other eight are installed or available until a later inventory confirms them.

The configured model directory is:
`/data/data/com.termux/files/home/ssd/ollama_models`

The external SSD was confirmed mounted at:
`/mnt/media_rw/34EE-8169`

The model directory reported 8.8 GB and the SSD reported 869 GB available at the time of the check. The six displayed model sizes total approximately 7.9 GB; directory size can differ because of shared layers, metadata and filesystem allocation.

### Initial model assignments — committed, not yet device-tested

The initial assignment registry is `intellisync/config/model_assignments.json`. It maps all 17 local roles across the six verified models using the capability profiles below. These are starting assignments, not benchmark-proven rankings; test task quality and revise based on evidence:
- `deepseek-r1:1.5b`: reasoning and technical analysis.
- `qwen3:1.7b`: coding and implementation support.
- `qwen2.5:1.5b`: structured code, scripts and data/configuration tasks.
- `llama3.2:3b`: general production, drafting and documentation.
- `gemma2:2b`: QA assistance and review checklists.
- `gemma3:1b`: lightweight classification, summaries and support.

Each agent may use one assigned local model at a time. Models may be shared by multiple agents through sequential scheduling. The initial on-demand worker runner is `intellisync/worker.py`; it serializes one local model request at a time and asks Ollama to unload the model after each task. Device execution remains unverified until tested in Termux. Do not assume all 24 agents can run simultaneously or that a background scheduler is active. Gemini and OpenRouter are cloud escalation options for larger tasks, alternate reasoning or work beyond local model capability; local models remain the default.

## 8. Production workflow

- All production agents work in the shared Git branch `main`.
- Agents are responsible for committing and pushing their own work, subject to repository permissions and safeguards.
- Standard cycle: 20 minutes production, 5 minutes independent QA, 5 minutes correction.
- Each QA supervisor reviews the four production specialists assigned to that supervisor in `intellisync/config/coordination.json`.
- Repeat until QA approves or escalates.
- Preserve existing files, inspect before editing, make scoped changes and report commit references and test evidence.

## 9. Current project status and honesty requirements

Known project direction includes an Unreal Engine 5 foundation. The first visual milestone is the train-arrival opening and Bella Rose guided introduction. Existing repository documentation describes project configuration and a greybox-building script.

Do not claim:
- The Unreal project has successfully built unless a build was run and verified.
- The greybox is a finished level or game.
- Fab packages have been downloaded/imported unless verified.
- The browser game or tablet controls are playable until tested in a browser/device.
- All 17 local agents or all 24 combined agents are running unless live runtime evidence confirms it.
- The model scheduler is active unless its process and job execution are verified.

For every task, report separately: **completed and verified**, **implemented but not tested**, **proposed**, and **blocked**.

## 10. Termux operator visibility

The creator wants to inspect the local model/runtime state from the Termux command prompt. Useful current checks are:

```bash
ollama list
ollama ps
echo "$OLLAMA_MODELS"
df -h ~/ssd
```

These commands report installed models, currently loaded Ollama models, the configured model path and SSD capacity. They do **not** prove that an AI agent is active. Agent status requires the agent runtime/scheduler to publish truthful status or heartbeat records. Do not label a configured role as online merely because its model is installed.

## 11. Required behavior for every model/agent

1. Read this master context and relevant linked project specifications before acting.
2. Respect creator-approved decisions and identify proposals clearly.
3. Inspect existing files and current branch state before editing.
4. Follow the canonical roster, role boundaries and QA ownership.
5. Do not duplicate completed work or overwrite unrelated changes.
6. Never expose credentials, API keys or private data.
7. Report blockers and assumptions.
8. Provide concrete deliverables, changed paths, commit IDs and test evidence.
9. Distinguish configured roles from instantiated, running and healthy agents.
10. Never claim unverified work is complete.
