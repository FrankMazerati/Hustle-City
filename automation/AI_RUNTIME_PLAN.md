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
