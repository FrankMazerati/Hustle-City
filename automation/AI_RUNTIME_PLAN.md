# AI Runtime and Workflow Plan

## Agent definition versus running agent
An agent role is a prompt plus scope, tools, knowledge and permissions. Running workers additionally require an orchestration runtime, model endpoints/local model servers, credentials, storage, monitoring and scheduler/queue. The 48 roles in the catalog are defined roles, not 48 live instances.

## Runtime layers
1. Agent registry: stable ID, prompt version, department, model profile, permissions.
2. Task orchestrator: queues, assignments, dependencies, retries, timeouts and escalation.
3. Model router: local/cloud model selection by task, quality, latency and cost.
4. Shared knowledge: repository documents, decision log, asset registry and retrieval index.
5. Tool gateway: scoped GitHub, Godot, asset, test and approved research tools.
6. Review service: peer review, QA gates, creator approval and audit trail.
7. Observability: run IDs, inputs/outputs, duration, compute/tokens, errors and status.

## Dedicated Hustle City execution pilot
A separate five-role manual pilot is stored under agents/runtime/hustle-city/:
- SAM game orchestrator
- NEXUS game backend
- VECTOR game developer
- URBAN world designer
- SENTINEL independent QA

The wider ten-person named cohort is under agents/cohorts/hustle-city-core/. The pilot uses its own task queue (automation/HUSTLE_CITY_TASK_QUEUE.json), relay log and 14-slot free-first provider fallback script. It does not share Command Center agent instances or the Command Center Supabase project.

The workflow at .github/workflows/hustle-city-agent-pilot.yml is manual-dispatch only and requires the input RUN. No schedule is enabled. It runs temporary sequential model sessions; it does not create persistent always-on agents. The workflow installs Gemini CLI and Aider, grants the worker session repository write access on an isolated run branch, and opens a pull request for review. Review prompts before dispatch and keep the first cycle documentation-only.

Provider credentials must be added as repository Actions secrets in Hustle City; secrets in the Command Center repository are not automatically shared. Paid relay slots remain disabled unless ALLOW_PAID_AI=true. Provider availability, model names, free quotas and billing can change; a relay slot is not a guarantee of free capacity.

## Backend isolation
The Command Center Supabase project must not be reused for Hustle City. NEXUS first produces a backend blueprint. A dedicated game Supabase project is a separate provisioning step requiring an organization selection and review of any quoted cost. Do not deploy schema or functions until the creator approves the architecture and project.

## Offline and hybrid models
Do not require a unique model per agent. Multiple roles can share a small model pool with different prompts and permissions. Capability groups: general reasoning/planning, coding, vision, image generation, embeddings/retrieval and optional 3D/motion tools. Hardware choice depends on RAM, GPU/VRAM, operating system, model size and quantization. Local models do not automatically provide current web research or cloud connectivity.

## Workflow candidates
- Task intake → canon retrieval → dependency check → assignment.
- Deliverable submission → peer review → QA → creator approval.
- Change notification → affected-agent review requests.
- Scheduled geographic research → source/license capture → atlas update proposal.
- Nightly regression/build check → report.
- Agent health, queue and resource monitoring.

## n8n safety
Confirm n8n version and installed nodes before creating importable workflows. New schedules/webhooks must be inactive by default. Use durable idempotency for external writes; an in-memory Set only catches duplicates within one execution. Never put credentials in workflow JSON or code. Do not activate production workflows without explicit approval.

## Permissions
Default read-only. Restrict write access to designated paths/branches. Publishing, production deployment, spending, account changes and external messages require explicit approval. Keep secrets in runtime secret storage, never Git.