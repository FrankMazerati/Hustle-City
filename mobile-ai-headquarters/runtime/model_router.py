"""Free-only model router for Hustle City Trinity.

Fail-closed: paid providers are never eligible under the initial zero-dollar
policy. A provider is callable only after explicit free/local verification.
"""
from __future__ import annotations
import json, os, time, urllib.error, urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any

class RouteBlocked(RuntimeError):
    """No policy-compliant model is available; task must be queued."""

@dataclass(frozen=True)
class Route:
    provider_id: str
    model: str
    endpoint: str
    api_key_env: str | None
    is_local: bool
    max_output_tokens: int

class ModelRouter:
    def __init__(self, config: dict[str, Any], environ: dict[str, str] | None = None):
        self.config = config
        self.environ = os.environ if environ is None else environ
        policy = config.get("budget_policy", {})
        self.zero_dollar = policy.get("mode") == "zero_dollar"
        self.paid_calls_allowed = policy.get("paid_calls_allowed", False)
        self.providers = config.get("providers", [])

    @classmethod
    def from_file(cls, path: str | Path) -> "ModelRouter":
        return cls(json.loads(Path(path).read_text(encoding="utf-8")))

    def select(self, task: dict[str, Any]) -> Route:
        if not self.zero_dollar or self.paid_calls_allowed:
            raise RouteBlocked("Only the initial zero-dollar policy is supported; paid routing is disabled.")
        required = set(task.get("capabilities", []))
        local_preferred = bool(task.get("local_only") or task.get("privacy_sensitive"))
        candidates = []
        for p in self.providers:
            if not p.get("enabled", False) or p.get("cost_class") == "paid":
                continue
            local = p.get("kind") == "local"
            if local:
                if not p.get("verified_local", False): continue
            else:
                if p.get("cost_class") != "free" or not p.get("verified_free", False): continue
                if not p.get("quota_available", False) or not p.get("data_terms_approved", False): continue
            if local_preferred and not local: continue
            if not required.issubset(set(p.get("capabilities", []))): continue
            if not p.get("endpoint") or not p.get("model"): continue
            key_env = p.get("api_key_env")
            if key_env and not self.environ.get(key_env): continue
            candidates.append(p)
        if not candidates:
            raise RouteBlocked("No configured, verified, zero-cost model fits. Queue task; never call a paid fallback.")
        candidates.sort(key=lambda p: (0 if local_preferred and p.get("kind") == "local" else 1,
                                       -int(p.get("quality_score", 0)), int(p.get("latency_ms", 10**9))))
        p = candidates[0]
        return Route(p["id"], p["model"], p["endpoint"], p.get("api_key_env"),
                     p.get("kind") == "local",
                     min(int(task.get("max_output_tokens", 2048)), int(p.get("max_output_tokens", 2048))))

    def invoke(self, task: dict[str, Any], messages: list[dict[str, str]], timeout_s: int = 60) -> dict[str, Any]:
        """Call a configured OpenAI-compatible endpoint; 402/429 queues task."""
        route = self.select(task)
        payload = json.dumps({"model": route.model, "messages": messages,
                              "max_tokens": route.max_output_tokens,
                              "temperature": float(task.get("temperature", 0.2))}).encode()
        headers = {"Content-Type": "application/json"}
        if route.api_key_env:
            headers["Authorization"] = f"Bearer {self.environ[route.api_key_env]}"
        request = urllib.request.Request(route.endpoint, data=payload, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(request, timeout=timeout_s) as response:
                data = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            if exc.code in (402, 429):
                raise RouteBlocked(f"Provider quota/billing gate HTTP {exc.code}; task queued, no paid fallback.") from exc
            raise
        choices = data.get("choices") or []
        if not choices: raise RuntimeError("Model endpoint returned no choices.")
        return {"provider_id": route.provider_id, "model": route.model,
                "content": choices[0].get("message", {}).get("content", ""),
                "usage": data.get("usage", {}), "timestamp": int(time.time()),
                "cost_usd": 0, "budget_policy": "zero_dollar"}
