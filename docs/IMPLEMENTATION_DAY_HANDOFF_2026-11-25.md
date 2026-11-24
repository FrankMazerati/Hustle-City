# Hustle City — Implementation Day Handoff (2026-11-25)

**Mode:** Implementation, not more open-ended planning.  
**Environment:** Android tablet, UserLAnd Kali Linux.  
**Repository:** `~/ai-hq/repos/Hustle-City` (known prior workspace; verify it exists).  
**Home:** `/home/userland`.  
**Engine:** Unreal Engine 5 primary; Unity 6 secondary.  
**Workforce target:** 17 roles — SCRIBE, LENS, QA-1–QA-3, P01–P12. ChatGPT conversation is coordinator; no local Trinity agent.  
**Cycle:** 20 min production → 5 min independent QA → 5 min correction; overlapping waves.  
**Git:** one shared `main` workflow is the current creator direction, but foundation work currently remains on `knowledge-library-foundation` under PR #11. Do not merge or switch the foundation PR to main without approval.

## 1. Known device/storage facts — do not assume the USB mount

- External USB storage is physically attached to the tablet; last reported free space was about 899 GB.
- UserLAnd Kali previously exposed `/storage/internal` (backed by `/storage/emulated/0/Android/data/tech.ula/files/storage`) and sometimes `/sdcard`, but did **not** have a verified external-SSD mount. Access to `/dev/bus/usb` and `/mnt/media_rw` was denied in prior checks.
- Termux previously could read/write the external drive, but the creator has specified UserLAnd as the operating environment. Do not switch the workflow to Termux as a workaround without asking.
- Primitive FTPd was reported running on the tablet; SFTP port 1234, with a prior connection example `sftp -P 1234 user@192.168.1.9`. Treat the host/IP and anonymous/no-password behavior as historical and re-check before use.
- Prior notes conflict about Ollama location: some sessions reported Ollama in UserLAnd, other checks found `ollama` missing there and the server/models in Termux. One earlier inventory reported 14 model tags; another later report said six models were already on USB. Do not redownload models until the actual runtime endpoint and storage inventory are checked.
- The previously used Ollama endpoint was `http://127.0.0.1:11434`; a prior tmux session name was `HUSTLE-CITY`, window `0 OLLAMA`. Verify rather than assuming the session/server still exists.
- Do not invent an external mount path. Discover it first. Keep model data on the external drive only after UserLAnd can demonstrably read/write the actual mount.

## 2. First terminal diagnostic — run in UserLAnd Kali

```bash
printf '\n=== HOST ===\n'; uname -a; id; pwd
printf '\n=== STORAGE VIEWS ===\n'
ls -la /storage 2>&1
ls -la /storage/internal 2>&1
ls -la /sdcard 2>&1
printf '\n=== MOUNTS ===\n'
findmnt 2>&1 | head -100
printf '\n=== DISKS ===\n'
lsblk -f 2>&1
printf '\n=== CAPACITY ===\n'
df -hT 2>&1
printf '\n=== USB VISIBILITY ===\n'
ls -la /dev/bus/usb 2>&1
printf '\n=== PROJECT ===\n'
ls -ld ~/ai-hq/repos/Hustle-City 2>&1
printf '\n=== OLLAMA PROCESS / COMMAND ===\n'
command -v ollama || true
pgrep -af ollama || true
printf '\n=== OLLAMA ENDPOINT ===\n'
curl -fsS --max-time 3 http://127.0.0.1:11434/api/tags || true
printf '\n=== TMUX ===\n'
tmux ls 2>&1 || true
```

This is a diagnostic only. If the external disk is not visible, stop before changing `OLLAMA_MODELS`, copying model blobs, or claiming the drive is mounted. Use Android's supported storage access/permission path and verify read/write from UserLAnd; do not try to bypass Android permissions or guess a path.

## 3. Repository and environment startup checks

```bash
cd ~/ai-hq/repos/Hustle-City
git status --short --branch
git remote -v
git branch --show-current
python3 --version
git --version
tmux -V
```

Run the previously recorded unit-test command:

```bash
cd ~/ai-hq/repos/Hustle-City
python3 -m unittest discover -s intellisync/tests -v
```

This test command was previously reported as usable. Capture the actual result tomorrow; do not report tests passing until they run successfully.

Check Ollama only if the endpoint responds:

```bash
curl -fsS http://127.0.0.1:11434/api/tags
```

If Ollama is confirmed, save the actual inventory before downloading anything. Do not assume old 14-model inventory is current.

## 4. External-drive target layout (create only after mount is verified)

Use a clear project-owned directory on the verified external volume, for example:

```text
HUSTLE-CITY/
  repo-mirror/
  models/ollama/
  agents/prompts/
  agents/config/
  agents/logs/
  artifacts/
  visual-references/
  backups/
```

The example is a directory layout, not a claim that the mount path is known. Keep Git's active working tree in the existing UserLAnd workspace until external-drive read/write and Git behavior are proven reliable. Large Ollama model storage and large visual/build artifacts are the first candidates for external storage. Agent prompt/config files are small; copy them after inventory. Never put credentials or API keys in Git or plain-text agent folders.

## 5. Ollama model storage and downloads

Do not redownload models already present. First determine:
- Which process serves port 11434.
- Which OS environment owns that process.
- The actual `OLLAMA_MODELS` path.
- Whether the existing model blobs are already on the external disk.
- Which of the 17 roles need distinct model capability assignments.

If the Ollama server is confirmed to run in UserLAnd and the external disk is mounted read/write there, then and only then configure its model directory to the verified external path and restart the server using the installed service/session method. Preserve existing model data and verify `/api/tags` after restart. Do not move a live model directory.

If UserLAnd cannot access the drive, do not pretend the external-drive model plan is complete. Keep the already-working model host in place for the first pipeline test, and record the storage-access blocker for a separate resolution. Do not switch to Termux without creator approval.

Model target is “as many useful models as safely fit,” historically 50–60 was an aspiration, not a verified compatible set. Prioritize the approved 17-role workforce's actual model needs, available storage, RAM/thermal limits and model licenses. Models are not agent processes; one local inference at a time is the known shared-device constraint. Do not attempt to load 17 models simultaneously.

## 6. Agent files and pipeline activation

Current creator-approved roster:
- SCRIBE and LENS — parallel creative leads.
- QA-1, QA-2, QA-3 — independent QA supervisors.
- P01–P12 — production specialists, three groups of four; one QA supervisor per group.

Before starting workers:
1. Inventory the actual agent prompt, roster, model config and task-contract files in the repository.
2. Mark old 12-specialist/3-QA and legacy 48-role configuration as stale; do not launch it as if it were the 17-role roster.
3. Create/verify the 17 role prompt/config entries without inventing the final P01–P12 domain mapping.
4. Validate each configured model tag against the live Ollama inventory.
5. Confirm one active inference at a time on the shared tablet.
6. Run one bounded test task for one production agent.
7. Run independent QA and a correction pass.
8. Only after the single-package test passes, expand to the three groups with overlapping production waves and resource scheduling.
9. Keep scheduler disabled if group-aware execution, runtime permissions, QA routing, heartbeat/recovery and safe stop are missing.

Required cycle: 20-minute production, 5-minute independent QA, 5-minute correction. Repeat until approved or escalated. No worker approves its own work. Keep durable logs and task/artifact version IDs.

The existing `scripts/hustle-city-ai-relay.sh` is a legacy 14-slot provider relay and must not be mistaken for the current 17-local-agent production scheduler. It can call hosted providers and contains paid-provider branches guarded by `ALLOW_PAID_AI`; do not enable paid calls. Inspect it before use. The repository currently does not expose `scripts/hustle-city-status.sh` or `intellisync/worker.py` at the expected paths.

## 7. Exact startup prompt for the UserLAnd assistant/terminal session

Paste this as the operating instruction when resuming:

> IMPLEMENTATION MODE — HUSTLE CITY. Use UserLAnd Kali Linux as the command environment. Do not switch to Termux. Start by running the storage, repository, Ollama endpoint, process and tmux diagnostics in docs/IMPLEMENTATION_DAY_HANDOFF_2026-11-25.md. Do not assume the USB drive is mounted or that Ollama is running in UserLAnd. Preserve existing models and files; do not redownload anything until inventory proves it is missing. Verify the external drive is mounted read/write before moving model storage. Confirm the actual repository branch and working tree before editing. Reconcile the live roster to SCRIBE, LENS, QA-1–QA-3 and P01–P12; do not launch stale 12+3 or 48-role configs. First get one production → independent QA → correction package passing, then implement the group-aware scheduler and overlapping 20/5/5 cycles with safe resource limits. Do not enable paid providers, do not expose credentials, do not merge PR #11, and do not claim agents are online until heartbeat and task execution are verified. Report commands, outputs, blockers and evidence; proceed with implementation rather than more speculative planning.

## 8. Completion checklist for tomorrow

- [ ] UserLAnd diagnostic captured.
- [ ] External drive mount path positively identified and read/write test passed, or blocker explicitly recorded.
- [ ] Existing model inventory captured; duplicates avoided.
- [ ] Repository status/branch confirmed.
- [ ] IntelliSync tests executed and results saved.
- [ ] Current 17-role roster/prompts/config audited.
- [ ] At least one bounded local model inference verified.
- [ ] One production → independent QA → correction cycle completed with evidence.
- [ ] Group-aware 20/5/5 pipeline implemented/tested before scheduler activation.
- [ ] Agent logs and project artifacts placed on verified persistent storage.
- [ ] No paid calls, no credentials committed, no unsupported “online” claims.

**Definition of tomorrow's first success:** one real local production agent completes a scoped Hustle City task, an independent QA role tests it, the production agent corrects any defect, and the accepted artifact is committed with evidence. Then scale the pipeline.
