# Library Workstation Quickstart — Hustle City

**Purpose:** Use a public Windows workstation, if permitted and capable, to obtain the Unreal project, claim/download free assets, and create a portable handoff without putting large binaries into Git.

## First 10 minutes: qualify the workstation

Ask library staff whether the computer:
- runs 64-bit Windows 10/11;
- permits Epic Games Launcher and Unreal Engine installation or already has a compatible Unreal Engine 5 installation;
- has a dedicated GPU and enough RAM/storage for Unreal Editor;
- permits installing/running software, signing into Epic/Fab, browser downloads, USB external drives, and copying files to USB;
- allows a long enough reservation for downloads and installation.

If software installation, USB writing, or Epic sign-in is blocked, do not try to bypass library controls. Use the session for browser-based asset claiming, documentation, and downloading small standard-format packs only where permitted.

## Portable drive layout

Create this on the external drive:

```text
HUSTLE_CITY_PORTABLE/
├── PROJECT_SOURCE/          # Git clone/ZIP of Hustle-City source
├── ASSET_ARCHIVES/
│   ├── CITY/
│   ├── RAIL_AND_TRAINS/
│   ├── VEHICLES/
│   ├── CHARACTERS_ANIMATION/
│   ├── PROPS_INTERIORS/
│   ├── MATERIALS_TEXTURES/
│   └── EPIC_SAMPLE_PROJECTS/
├── UE_PROJECTS/
│   └── HustleCity/          # only if workstation can run Unreal
├── MODEL_ARCHIVES/          # only Ollama model files if safely exported
├── LICENSES_AND_RECEIPTS/
└── SESSION_NOTES/
```

## Project source: get the cloud copy

1. Open https://github.com/FrankMazerati/Hustle-City.
2. Download the repository ZIP or use Git if installed and permitted.
3. Extract/copy it to `PROJECT_SOURCE/Hustle-City`.
4. The GitHub repository is the source for code, scripts, manifests and documentation. Do not upload Unreal `.uasset` binaries, Fab sample projects, or large source archives into ordinary Git commits.

## Asset acquisition: use provider libraries first

1. Sign in to https://www.fab.com/ with the project owner's Epic account, only on a trusted session and only if library policy permits.
2. Add eligible free Unreal sample projects to the account library. This is account claiming, not a local install.
3. For regular interchange packs, download standard FBX/OBJ/glTF archives to the matching external-drive folder.
4. Start with smaller CC0 packs: Kenney Train Kit, Kenney City Kit, Kenney Prototype Kit, Quaternius Downtown City MegaKit standard/free tier, and selected Poly Haven materials.
5. Do not choose paid Source tiers or any item with a fee, subscription, unclear commercial rights, or required paid dependency. Save the exact license/readme/attribution file beside each pack.
6. Treat Epic City Sample and other large Unreal sample projects separately. Check compatible engine version, required plugins, disk space and GPU/RAM before downloading.

## If Unreal Engine is already installed or library staff approves installation

1. Install/launch the Epic Games Launcher and a compatible Unreal Engine 5 version only with permission.
2. Create a test project on the external drive only if the drive is fast enough and has adequate free space; otherwise use approved workstation storage during the session and copy the project back after closing Unreal.
3. Use Fab Library to create/add compatible sample projects.
4. Open the project and verify it reaches the editor before downloading more large packs.
5. For FBX/OBJ/glTF packs, copy extracted files into `Content/_Staging/<PackName>/`.
6. Run `Scripts/Unreal/import_staged_assets.py` from inside Unreal Editor with the Python Editor Script Plugin enabled. This script imports interchange formats only; it does not migrate `.uasset` sample projects.
7. For Unreal-native content, use the source project's Migrate command to move only selected assets and their dependencies into Hustle City. Never copy random `.uasset` files in File Explorer.
8. Save, close Unreal, then safely eject the drive.

## What makes a first viewable prototype

The first milestone is the opening arrival and guided introduction, not a generic city block:
- rainy passenger train window and exterior train approach;
- skyline reveal and station arrival;
- platform and grand concierge hall;
- Bella Rose introduction;
- Hustle Towers exterior, courtyard, lobby and room;
- room booking and Bella's narrated guided-tour sequence.

A library PC that cannot run Unreal can still claim assets and stage files, but it cannot produce a verified in-editor viewable game. A tablet running UserLAnd is not a substitute for the full Unreal Editor.

## Model downloads and transfer warning

Ollama models are not ordinary portable ZIP assets. Prefer pulling them directly on the device that will run Ollama. Moving model storage requires a supported Ollama model-store setup and sufficient disk space; do not assume copying an arbitrary cache folder to USB will make models portable. The planned additional pulls are qwen3.5:4b, gemma3:4b and qwen2.5-coder:3b, but they are not confirmed downloaded. Verify with `ollama list` on the actual target device before recording them as installed.

## Cloud vs external drive

- **GitHub:** source code, scripts, small text manifests and project decisions.
- **External drive:** large asset archives, local Unreal project copies and backups.
- **Fab/Epic account library:** claimable Unreal assets and sample projects.
- **Cloud file storage:** optional second backup for non-restricted archives; check provider limits and license terms before uploading.
- Do not put credentials, API keys, private account data or model secrets in GitHub.

## End-of-session checklist

- [ ] Repository source downloaded and commit noted.
- [ ] External drive folder structure created.
- [ ] Free assets claimed in Fab account where applicable.
- [ ] Downloaded archives have matching license/readme files.
- [ ] Asset names, source URLs, versions, sizes and status recorded.
- [ ] If Unreal was used, test project opened successfully and was closed cleanly.
- [ ] External drive safely ejected.
- [ ] No paid pack or unverified dependency added.
