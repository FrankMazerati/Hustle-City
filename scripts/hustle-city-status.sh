#!/data/data/com.termux/files/usr/bin/bash
# Hustle City local status dashboard (Termux / Bash + Python 3)
# Reports configured roster and Ollama state. It does not fabricate agent heartbeats.
set -u
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CONFIG="$ROOT/intellisync/config/coordination.json"

if ! command -v python >/dev/null 2>&1; then
  echo "Python is required. Install it with: pkg install python"
  exit 1
fi
if [ ! -f "$CONFIG" ]; then
  echo "ERROR: Missing workforce configuration: $CONFIG"
  exit 1
fi

export HUSTLE_CITY_ROOT="$ROOT"
export HUSTLE_CITY_CONFIG="$CONFIG"

python - <<'PY'
import json, os, shutil, subprocess, sys
from pathlib import Path

root = Path(os.environ["HUSTLE_CITY_ROOT"])
config_path = Path(os.environ["HUSTLE_CITY_CONFIG"])
cfg = json.loads(config_path.read_text(encoding="utf-8"))
workforce = cfg.get("local_workforce", {})
creatives = workforce.get("creative_leads", [])
qas = workforce.get("qa_supervisors", [])
specialists = workforce.get("production_specialists", [])

def run(args):
    try:
        p = subprocess.run(args, capture_output=True, text=True, timeout=8)
        return p.returncode, p.stdout.strip(), p.stderr.strip()
    except FileNotFoundError:
        return 127, "", f"{args[0]} not found"
    except subprocess.TimeoutExpired:
        return 124, "", "command timed out"

print("=" * 68)
print(" HUSTLE CITY — TERMUX OPERATIONS STATUS")
print("=" * 68)
print(f"Repository : {root}")
print(f"Roster     : {len(creatives) + len(qas) + len(specialists)} configured local roles / target {workforce.get('target_total', '?')}")
print("Coordinator: ChatGPT (external; not a local Ollama worker)")
print()

# Ollama installed models
print("OLLAMA — INSTALLED MODELS")
rc, out, err = run(["ollama", "list"]) if shutil.which("ollama") else (127, "", "ollama not found")
installed = []
if rc == 0 and out:
    lines = out.splitlines()
    for line in lines[1:]:
        parts = line.split()
        if parts:
            installed.append((parts[0], " ".join(parts[2:]) if len(parts) > 2 else ""))
    if installed:
        for name, size in installed:
            print(f"  [INSTALLED] {name:<25} {size}")
    else:
        print("  No models listed.")
else:
    print(f"  UNAVAILABLE: {err or 'ollama list failed'}")

print()
print("OLLAMA — CURRENTLY LOADED MODELS")
rc, out, err = run(["ollama", "ps"]) if shutil.which("ollama") else (127, "", "ollama not found")
if rc == 0 and out:
    rows = out.splitlines()
    if len(rows) > 1:
        for line in rows[1:]:
            print(f"  [LOADED] {line}")
    else:
        print("  No model currently loaded (Ollama is idle).")
else:
    print(f"  UNAVAILABLE: {err or 'ollama ps failed'}")

# Agent statuses: configuration is not runtime presence.
print()
print("HUSTLE CITY AGENT ROSTER")
print("-" * 68)
print(f"{'AGENT':<23} {'ROLE':<31} STATUS")
print("-" * 68)
agents = []
for a in creatives:
    agents.append((a.get("id", "?"), a.get("role", "Creative lead"), "CREATIVE"))
for a in qas:
    agents.append((a.get("id", "?"), "QA Supervisor", "QA"))
for a in specialists:
    agents.append((a.get("id", "?"), a.get("role", "Production specialist"), "PRODUCTION"))

for agent_id, role, group in agents:
    # No heartbeat/runtime status store is currently wired into this dashboard.
    short_role = role if len(role) <= 30 else role[:27] + "..."
    print(f"{agent_id:<23} {short_role:<31} DEFINED / NOT VERIFIED")

print("-" * 68)
print(f"Configured roles: {len(agents)}")
print("Live agents      : NOT VERIFIED — no agent heartbeat/status feed is connected.")
assignment_path = root / "intellisync" / "config" / "model_assignments.json"
if assignment_path.exists():
    try:
        assignment_cfg = json.loads(assignment_path.read_text(encoding="utf-8"))
        assignments = assignment_cfg.get("agents", [])
        print(f"Model assignments: {len(assignments)} configured / {len(agents)} roles")
        print("Assignment status : CONFIGURED / NOT YET BENCHMARKED")
    except Exception as exc:
        print(f"Model assignments: ERROR reading registry ({exc})")
else:
    print("Model assignments: NOT CONFIGURED")
print()
print("QUICK INTERPRETATION")
print("  INSTALLED = model is present in this Ollama model store.")
print("  LOADED    = model is currently resident in Ollama.")
print("  DEFINED   = role exists in the project roster; it is not proof of a running agent.")
print()
print("NEXT CHECKS")
print("  ollama list       # installed models")
print("  ollama ps         # currently loaded models")
print("  python -m intellisync.worker list   # show role-to-model assignments")
print("  python -m intellisync.worker run --agent P01-GEOGRAPHY --task \\"Describe a small test deliverable.\\"")
print()
PY
