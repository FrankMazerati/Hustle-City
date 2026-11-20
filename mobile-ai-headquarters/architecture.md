# Mobile AI Headquarters Architecture

## Device and service responsibilities

| Component | Responsibility | Does not do |
|---|---|---|
| Galaxy A17 | Mobile control surface, local agent/config files, task review, lightweight relay client | Run four large language models concurrently |
| Remote AI APIs | Model inference for assigned agent tasks | Own the only copy of project state |
| GitHub | Canonical source history, issues/tasks, branches, pull requests, CI | Store large binary asset libraries as the default |
| USB 1 TB drive(s) | Large assets, exports, archives, backup snapshots | Act as the only copy of important work |
| Tablet | Project dashboard, code review, visual inspection, approval | Become a separate competing source of truth |

## Logical topology

Creator -> mobile dashboard -> Trinity coordinator -> task queue -> specialist agent runner -> remote AI engine -> scoped workspace -> validation/QA -> pull request -> creator review on tablet -> approved merge.

The tablet can inspect the same GitHub repository and CI results. The phone is the portable command surface, not a single point of failure for long-running work.

## Twelve specialist seats

1. Atlas — World Architect
2. Brick — City Builder
3. Blueprint — Building Architect
4. Vibe — Sims Creator
5. Stitch — Fashion Director
6. Motion — Animation Director
7. Torque — Vehicle Director
8. Tracks — Transportation Director
9. Route — Traffic and Navigation Director
10. Ace — Gameplay Director
11. Spark — Events and Social Director
12. Lockdown — Quality Assurance and Integration Director

Trinity is the central coordinator and is not counted in the twelve. Nexus remains a separate shared backend/multiplayer engineering support role as defined by the existing project plan.

## Four logical AI engine groups

- Engine 1: Atlas, Brick, Blueprint — world and construction.
- Engine 2: Vibe, Stitch, Motion — people and appearance.
- Engine 3: Torque, Tracks, Route — vehicles and transportation.
- Engine 4: Ace, Spark, Lockdown — gameplay and quality.

These are routing groups, not a commitment to four downloaded models or four vendors. A group may use one provider/model initially, but each agent retains its own system prompt, tools, permissions, context package, and task contract. The router may later select a different model per task based on capability, latency, cost, and availability.

## Execution model

- Agent configurations are stored in the repository and a local phone working copy.
- Inference is remote through authenticated APIs.
- A server-side runner or reliable hosted worker should execute long jobs. A phone-only background process is not a dependable always-on scheduler on Android.
- The phone can create tasks, inspect status, send approvals, and receive notifications.
- Agent work is asynchronous and resumable. Persist task state, inputs, outputs, model/provider metadata, and checkpoints.
- No real-world autonomy or external publishing without explicit permissions.

## Integration principles

Every task declares:
- objective and acceptance criteria;
- input specifications and dependencies;
- permitted repository paths;
- expected output format;
- interfaces/contracts affected;
- validation commands;
- rollback/recovery notes.

Agents must read shared project specifications and relevant integration contracts before producing work. Cross-domain changes trigger review from affected specialists. Lockdown performs independent QA, while Trinity owns final coordination and conflict resolution.
