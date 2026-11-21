"""Fail-closed Gemini/OpenRouter adapter for IntelliSync.

Hosted providers are eligible only when explicitly enabled and verified as
zero-cost, with quota and data terms approved. API keys are read from env only.
"""
from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from typing import Any, Callable


class ProviderUnavailable(RuntimeError):
    pass


class HostedModelClient:
    def __init__(self, config: dict[str, Any], environ: dict[str, str] | None = None,
                 urlopen: Callable[..., Any] | None = None):
        self.config = config
        self.environ = os.environ if environ is None else environ
        self.urlopen = urlopen or urllib.request.urlopen

    def eligible(self) -> list[dict[str, Any]]:
        providers = self.config.get("providers", {})
        chain = self.config.get("provider_chain", ["gemini", "openrouter"])
        eligible = []
        for provider_id in chain:
            item = providers.get(provider_id, {})
            if not all(item.get(flag, False) for flag in (
                "enabled", "verified_free", "quota_available", "data_terms_approved"
            )):
                continue
            key_env = item.get("api_key_env")
            api_key = self.environ.get(key_env, "") if key_env else ""
            model = self.environ.get(item.get("model_env", ""), "") or item.get("model", "")
            if api_key and model and item.get("endpoint"):
                eligible.append({**item, "id": provider_id, "api_key": api_key, "model": model})
        return eligible

    def validate(self) -> None:
        if not self.eligible():
            raise ProviderUnavailable(
                "No hosted provider is eligible. Enable only verified free models with "
                "available quota and approved data terms; ensure the matching GitHub Secret "
                "and model ID are supplied. No paid fallback is permitted."
            )

    def chat(self, model: str, messages: list[dict[str, str]],
             temperature: float = 0.2) -> str:
        del model  # Per-provider model IDs are configured independently.
        providers = self.eligible()
        if not providers:
            self.validate()
        failures = []
        for provider in providers:
            try:
                if provider["id"] == "gemini":
                    return self._gemini(provider, messages, temperature)
                if provider["id"] == "openrouter":
                    return self._openrouter(provider, messages, temperature)
                failures.append(f'{provider["id"]}: unsupported provider adapter')
            except urllib.error.HTTPError as exc:
                # Quota/rate limits and transient server failures may try the
                # next explicitly verified-free provider; other errors fail closed.
                if exc.code in (402, 429, 500, 502, 503, 504):
                    failures.append(f'{provider["id"]}: HTTP {exc.code}')
                    continue
                raise ProviderUnavailable(
                    f'{provider["id"]} rejected the request (HTTP {exc.code}); no paid fallback.'
                ) from exc
            except (urllib.error.URLError, TimeoutError) as exc:
                failures.append(f'{provider["id"]}: connection failure')
                continue
        raise ProviderUnavailable(
            "All configured free providers are unavailable; task must remain queued. "
            + "; ".join(failures)
        )

    def _post(self, provider: dict[str, Any], payload: dict[str, Any],
              headers: dict[str, str]) -> dict[str, Any]:
        request = urllib.request.Request(
            provider["endpoint"], data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json", **headers}, method="POST"
        )
        with self.urlopen(request, timeout=int(provider.get("timeout_seconds", 90))) as response:
            return json.loads(response.read().decode("utf-8"))

    def _gemini(self, provider: dict[str, Any], messages: list[dict[str, str]],
                temperature: float) -> str:
        system_parts = [m["content"] for m in messages if m.get("role") == "system"]
        contents = []
        for message in messages:
            role = message.get("role")
            if role == "system":
                continue
            contents.append({
                "role": "model" if role == "assistant" else "user",
                "parts": [{"text": message.get("content", "")}]
            })
        payload: dict[str, Any] = {
            "contents": contents,
            "generationConfig": {"temperature": temperature}
        }
        if system_parts:
            payload["systemInstruction"] = {"parts": [{"text": "\n\n".join(system_parts)}]}
        data = self._post(provider, payload, {"x-goog-api-key": provider["api_key"]})
        candidates = data.get("candidates") or []
        parts = (candidates[0].get("content") or {}).get("parts", []) if candidates else []
        result = "\n".join(p.get("text", "") for p in parts if p.get("text"))
        if not result.strip():
            raise ProviderUnavailable("Gemini returned an empty response.")
        return result.strip()

    def _openrouter(self, provider: dict[str, Any], messages: list[dict[str, str]],
                    temperature: float) -> str:
        payload = {
            "model": provider["model"],
            "messages": messages,
            "temperature": temperature,
            "max_tokens": int(provider.get("max_output_tokens", 4096))
        }
        headers = {"Authorization": f'Bearer {provider["api_key"]}'}
        if provider.get("site_url"):
            headers["HTTP-Referer"] = provider["site_url"]
        headers["X-Title"] = provider.get("app_name", "Hustle City IntelliSync")
        data = self._post(provider, payload, headers)
        choices = data.get("choices") or []
        content = (choices[0].get("message") or {}).get("content", "") if choices else ""
        if not isinstance(content, str) or not content.strip():
            raise ProviderUnavailable("OpenRouter returned an empty response.")
        return content.strip()
