#!/usr/bin/env bash
# Hustle City 14-slot free-first relay, adapted from the Command Center relay.
# Usage: ./scripts/hustle-city-ai-relay.sh <agent-prompt-file>
set -uo pipefail
AGENT_FILE="${1:-}"
if [[ -z "$AGENT_FILE" || ! -f "$AGENT_FILE" ]]; then echo "Usage: $0 <agent-prompt-file>" >&2; exit 2; fi
REPORT_FILE="automation/HUSTLE_CITY_RELAY_LOG.md"
PROMPT="Read and execute $AGENT_FILE for the assigned Hustle City task only. Follow project canon and do not claim unverified work."
PAID_AI_ENABLED="${ALLOW_PAID_AI:-false}"
record_success() {
  local relay="$1" model="$2"
  mkdir -p "$(dirname "$REPORT_FILE")"; touch "$REPORT_FILE"
  { printf '\n### Relay success — %s\n' "$(date -u '+%Y-%m-%d %H:%M:%S UTC')"
    printf -- '- Prompt: %s\n- Relay: %s\n- Model: %s\n- Actions run: %s\n' "$AGENT_FILE" "$relay" "$model" "${GITHUB_RUN_ID:-manual/local}"; } >> "$REPORT_FILE"
  echo "Relay $relay succeeded: $model"
}
try_aider() {
  local relay="$1" model="$2" model_arg="$3"
  echo "Trying relay $relay: $model"
  if aider --model "$model_arg" --yes --message "$PROMPT"; then record_success "$relay" "$model"; return 0; fi
  echo "Relay $relay failed; trying next configured relay." >&2; return 1
}
try_gemini() {
  local relay="$1" key_name="$2" key_value="$3"
  echo "Trying relay $relay: Gemini 2.5 Flash ($key_name)"
  if GEMINI_API_KEY="$key_value" gemini --model gemini-2.5-flash --yolo -p "$PROMPT"; then record_success "$relay" "gemini-2.5-flash ($key_name)"; return 0; fi
  echo "Relay $relay failed; trying next configured relay." >&2; return 1
}
command -v aider >/dev/null 2>&1 || echo "Aider unavailable; Aider relays skipped."
if command -v gemini >/dev/null 2>&1; then
  [[ -n "${GEMINI_API_KEY:-}" ]] && try_gemini 1 GEMINI_API_KEY "$GEMINI_API_KEY" && exit 0
  [[ -n "${GEMINI_API_KEY_2:-}" ]] && try_gemini 2 GEMINI_API_KEY_2 "$GEMINI_API_KEY_2" && exit 0
  [[ -n "${GEMINI_API_KEY_3:-}" ]] && try_gemini 3 GEMINI_API_KEY_3 "$GEMINI_API_KEY_3" && exit 0
else echo "Relays 1-3 skipped: Gemini CLI unavailable."; fi
echo "Relays 4-5 skipped: GitHub Models retired; GitHub token is not an inference key."
if [[ -n "${GROQ_API_KEY:-}" ]] && command -v aider >/dev/null 2>&1; then GROQ_API_KEY="$GROQ_API_KEY" try_aider 6 "Groq / llama-3.3-70b-versatile" "groq/llama-3.3-70b-versatile" && exit 0; fi
if [[ -n "${CEREBRAS_API_KEY:-}" ]] && command -v aider >/dev/null 2>&1; then OPENAI_API_BASE="https://api.cerebras.ai/v1" OPENAI_API_KEY="$CEREBRAS_API_KEY" try_aider 7 "Cerebras / llama-3.3-70b" "openai/llama-3.3-70b" && exit 0; fi
if [[ -n "${SAMBANOVA_API_KEY:-}" ]] && command -v aider >/dev/null 2>&1; then OPENAI_API_BASE="https://api.sambanova.ai/v1" OPENAI_API_KEY="$SAMBANOVA_API_KEY" try_aider 8 "SambaNova / Meta-Llama-3.3-70B-Instruct" "openai/Meta-Llama-3.3-70B-Instruct" && exit 0; fi
if [[ "$PAID_AI_ENABLED" == "true" ]] && [[ -n "${MISTRAL_API_KEY:-}" ]] && command -v aider >/dev/null 2>&1; then MISTRAL_API_KEY="$MISTRAL_API_KEY" try_aider 9 "Mistral / codestral-latest" "mistral/codestral-latest" && exit 0; fi
if [[ "$PAID_AI_ENABLED" == "true" ]] && [[ -n "${CLOUDFLARE_API_TOKEN:-}" && -n "${CLOUDFLARE_ACCOUNT_ID:-}" ]] && command -v aider >/dev/null 2>&1; then OPENAI_API_BASE="https://api.cloudflare.com/client/v4/accounts/${CLOUDFLARE_ACCOUNT_ID}/ai/v1" OPENAI_API_KEY="$CLOUDFLARE_API_TOKEN" try_aider 10 "Cloudflare Workers AI" "openai/@cf/meta/llama-3.3-70b-instruct-fp8-fast" && exit 0; fi
if [[ "$PAID_AI_ENABLED" == "true" ]] && [[ -n "${HF_TOKEN:-}" ]] && command -v aider >/dev/null 2>&1; then OPENAI_API_BASE="https://router.huggingface.co/v1" OPENAI_API_KEY="$HF_TOKEN" try_aider 11 "Hugging Face Router" "openai/Qwen/Qwen2.5-Coder-32B-Instruct" && exit 0; fi
if [[ "$PAID_AI_ENABLED" == "true" ]] && [[ -n "${COHERE_API_KEY:-}" ]] && command -v aider >/dev/null 2>&1; then COHERE_API_KEY="$COHERE_API_KEY" try_aider 12 "Cohere / command-r-plus" "command-r-plus-08-2024" && exit 0; fi
if [[ "$PAID_AI_ENABLED" == "true" ]] && [[ -n "${NVIDIA_API_KEY:-}" ]] && command -v aider >/dev/null 2>&1; then OPENAI_API_BASE="https://integrate.api.nvidia.com/v1" OPENAI_API_KEY="$NVIDIA_API_KEY" try_aider 13 "NVIDIA NIM" "openai/meta/llama-3.3-70b-instruct" && exit 0; fi
if [[ -n "${OPENROUTER_API_KEY:-}" ]] && command -v aider >/dev/null 2>&1; then
  OPENROUTER_API_KEY="$OPENROUTER_API_KEY" try_aider 14 "OpenRouter / DeepSeek R1 Free" "openrouter/deepseek/deepseek-r1:free" && exit 0
  OPENROUTER_API_KEY="$OPENROUTER_API_KEY" try_aider 14 "OpenRouter / Llama 3.3 Free" "openrouter/meta-llama/llama-3.3-70b-instruct:free" && exit 0
  OPENROUTER_API_KEY="$OPENROUTER_API_KEY" try_aider 14 "OpenRouter / Qwen Coder Free" "openrouter/qwen/qwen-2.5-coder-32b-instruct:free" && exit 0
fi
echo "All configured Hustle City relay attempts failed for $AGENT_FILE." >&2
exit 1
