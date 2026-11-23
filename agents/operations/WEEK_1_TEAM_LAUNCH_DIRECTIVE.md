# Hustle City — Week 1 Team Launch Directive

**Purpose:** Start execution from the approved five-week roadmaps. This is a launch directive, not proof that the runtime is already active.

## Creator authority
The creator is Visual Director and Game Architect and retains final creative authority. Trinity is the overall coordinator. Every agent must read the shared operating blueprint and its own five-week blueprint before accepting work.

## Boot and verification sequence
1. Start the existing Hustle City server/runtime using the creator's established launch procedure. Do not invent commands or change ports/services.
2. Verify server health, agent registry, message relay, model router and repository access. Report actual status and evidence for each; do not infer that a component is active because configuration files exist.
3. Read the live registry for each agent's assigned Ollama model, model availability, endpoint and queue state. Do not invent model IDs or reassign models. Preserve one assigned local model per agent at a time.
4. Verify the registered identities for QA-1, QA-2 and QA-3 and their four-agent groups. The intended groups are QA-1: Atlas, Brick, Blueprint, Vibe; QA-2: Stitch, Motion, Torque, Tracks; QA-3: Route, Ace, Spark, Lockdown.
5. If the relay or model router is unavailable, do not claim agents can message or borrow models. Record the blocker and route it to Trinity/creator while continuing work that does not require the missing service.
6. Confirm the GitHub repository is `FrankMazerati/Hustle-City`, default branch `main`; agents work in task branches and submit PRs.

## Required reading

Every agent must read the complete organization directory and communication/breadcrumb standard, not only its own role file. Before accepting a downstream package, read and acknowledge the upstream agent's breadcrumb and record the exact version consumed.
- `agents/operations/FIVE_WEEK_TEAM_OPERATING_BLUEPRINT.md`
- `agents/operations/AGENT_COMMUNICATION_AND_BREADCRUMB_STANDARD.md`
- `agents/blueprints/README.md`
- Each agent's own file under `agents/blueprints/`
- Existing specialist manuals under `agents/manuals/`
- Relevant approved source documents and `docs/DECISION_LOG.md`

## Week 1 — Foundation & discovery
All agents begin **Week 1, Day 1** of their own blueprint. Do not jump to Week 2 or invent downstream implementation work before prerequisites are verified.

### Trinity
- Acknowledge all roster members and confirm which agents actually started.
- Issue unique task IDs and load the Week 1 Day 1 instruction from each agent's own blueprint.
- Build the live dependency/blocked-work board and confirm QA coverage.
- Prioritize source-of-truth review and creator decision requests. Keep agents productive in parallel where safe.

### 12 production specialists
- Read the project canon and their own five-week blueprint.
- Verify existing source artifacts and record their starting state.
- Separate approved facts from proposals, assumptions and unknowns.
- Create a domain inventory and identify the highest-value Week 1 foundation work.
- Acknowledge partner dependencies and produce evidence-backed status reports.

### QA supervisors
- Confirm the four assigned specialists in their group.
- Establish independent review scope, acceptance criteria and evidence requirements.
- Review early baseline work without taking over production tasks.

### Lockdown
- Establish cross-system quality and integration risks, coordinate with QA supervisors and Trinity, and avoid self-approving any deliverable.

### SCRIBE, LENS and Nexus
- Read canon and their own roadmaps.
- Establish their domain baselines, identify upstream/downstream dependencies and report which Week 1 outputs can safely proceed in parallel.

## Week 1 exit gate
By the end of Day 7, each agent must submit:
- A verified inventory of relevant existing artifacts and source versions.
- A source-linked requirements/baseline document for its domain.
- An assumptions and unresolved-decisions register.
- A dependency/contact list with acknowledgements or explicit relay limitations.
- A prioritized Week 2 backlog.
- A status of ACCEPTED, ACCEPTED WITH ACTIONS, REVISE or BLOCKED, supported by evidence.

Trinity must publish an integrated Week 1 report, verify QA dispositions and present creator decisions needed to unlock Week 2.

## Communication feeds, breadcrumbs and model use

Use the three named feeds in the shared IntelliSync runtime communication hub: Department Communication Feed, Cross-Department Communication Feed and Command Communication Feed. Verify relay health first. Every agent leaves breadcrumbs documenting what changed, where it lives, current status, design method/rationale, upstream inputs, interfaces, assumptions, unresolved work, QA evidence and next owner. Downstream agents read/acknowledge the breadcrumb, cite its version and leave their own continuation breadcrumb. Transfer approved artifacts through the rolling assembly-line package relay (producer → assigned QA → downstream receiver). The breadcrumb explains; the artifact delivers; the relay controls handoff.


Use the registered IntelliSync relay and model router only after health is verified. Messages must include sender, recipient, task ID, timestamp, priority, type, source/context, request/deliverable, dependencies, status and acknowledgement requirement. Model borrowing/second opinions must be routed and queued under model-owner and hardware constraints. Never commandeer another agent's session. Gemini/OpenRouter are allowed only with approved credentials and verified free quota.

## Cost and integrity
Project spend is $0. No paid API calls, paid hosting or paid features. Do not expose credentials. Do not claim runtime activation, message delivery, model availability, test success, merge or deployment without direct evidence. Preserve six central district boxes and surrounding neighborhood-box rule; do not invent total grid dimensions, neighborhood counts, station counts or alignments. HIM remains intercity/regional rail; HCTA remains local transit.

## First coordinator status message
Trinity must report: server health; active agent count and names; verified model assignments and availability (without exposing secrets); relay status; model-router status; QA coverage; tasks issued; blockers; and first expected artifact/checkpoint. If any component fails, state the exact failure and continue safe independent work rather than declaring the launch complete.
