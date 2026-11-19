# Hustle City dedicated runtime pilot

This is the separate Hustle City execution team. It reuses the relay pattern from the Command Center repository, but has its own prompts, task queue, log and manual-only workflow.

## Pilot team

| Runtime role | Cohort identity | Purpose |
|---|---|---|
| Game Orchestrator | SAM | Assign, coordinate and audit |
| Game Backend | NEXUS | Backend/multiplayer blueprint |
| Game Developer | VECTOR | Godot gameplay vertical slice |
| World Designer | URBAN | City/world blockout |
| Independent QA | SENTINEL | Review and reject incomplete work |

The broader ten-person named cohort remains defined in agents/cohorts/hustle-city-core/. This five-role pilot activates only the minimum leadership, backend, gameplay, world and QA functions. ATLAS and other specialists remain available for later expansion.

## Relay

The 14-slot free-first relay is adapted from FrankMazerati/Maximus-Optimus-Global-Command-Center-. Gemini keys, Groq, Cerebras, SambaNova and OpenRouter are attempted when corresponding repository secrets exist. Slots 9–13 are disabled unless the repository variable ALLOW_PAID_AI=true. GitHub Models slots 4–5 are skipped because that service was retired. The relay is fallback infrastructure, not guaranteed free capacity or guaranteed availability.

## Safety and activation

- Workflow is manual dispatch only; no timer or automatic schedule is enabled.
- To run, open Actions → Hustle City — supervised agent pilot → Run workflow and enter RUN.
- The workflow runs agents sequentially and commits changes to main.
- It installs Gemini CLI and Aider and grants those tools write access to the checked-out repository during the run. Run only after reviewing prompts and adding provider secrets.
- No provider key is committed to Git.
- Initial tasks are documentation/specification only; no database deployment or production code is authorized.
- A successful relay means a provider call returned successfully, not that a deliverable passed QA.

## Required repository secrets

At least one working provider credential is required:
- GEMINI_API_KEY (optional GEMINI_API_KEY_2, GEMINI_API_KEY_3)
- GROQ_API_KEY
- CEREBRAS_API_KEY
- SAMBANOVA_API_KEY
- OPENROUTER_API_KEY

Optional paid providers (Mistral, Cloudflare, Hugging Face, Cohere, NVIDIA) remain disabled unless ALLOW_PAID_AI=true.

## Backend separation

The Command Center Supabase project is not reused. Supabase management access was unavailable during setup, so no database project was created or modified. NEXUS first prepares a backend blueprint. Provisioning a dedicated Hustle City Supabase project requires selecting an organization and reviewing any quoted cost.
