import json
import unittest
import urllib.error

from intellisync.providers import HostedModelClient, ProviderUnavailable


class FakeResponse:
    def __init__(self, payload):
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def read(self):
        return json.dumps(self.payload).encode("utf-8")


class ProviderTests(unittest.TestCase):
    def config(self):
        return {
            "provider_chain": ["gemini", "openrouter"],
            "providers": {
                "gemini": {
                    "enabled": True, "verified_free": True, "quota_available": True,
                    "data_terms_approved": True, "api_key_env": "GEMINI_API_KEY",
                    "model_env": "GEMINI_MODEL",
                    "endpoint": "https://example.test/models/{model}:generateContent"
                },
                "openrouter": {
                    "enabled": True, "verified_free": True, "quota_available": True,
                    "data_terms_approved": True, "api_key_env": "OPENROUTER_API_KEY",
                    "model_env": "OPENROUTER_MODEL",
                    "endpoint": "https://example.test/chat/completions"
                }
            }
        }

    def test_unverified_provider_is_never_called(self):
        config = self.config()
        config["providers"]["gemini"]["verified_free"] = False
        called = []
        client = HostedModelClient(config, {
            "GEMINI_API_KEY": "not-a-real-key", "GEMINI_MODEL": "test-model"
        }, urlopen=lambda *a, **k: called.append(True))
        with self.assertRaises(ProviderUnavailable):
            client.validate()
        self.assertEqual(called, [])

    def test_gemini_native_request_and_response(self):
        requests = []
        def fake_open(request, timeout):
            requests.append(request)
            return FakeResponse({"candidates": [{"content": {"parts": [{"text": "Gemini result"}]}}]})
        client = HostedModelClient(self.config(), {
            "GEMINI_API_KEY": "test-key", "GEMINI_MODEL": "gemini-test",
            "OPENROUTER_API_KEY": "router-key", "OPENROUTER_MODEL": "free/test"
        }, urlopen=fake_open)
        result = client.chat("hosted:auto", [
            {"role": "system", "content": "Be precise."},
            {"role": "user", "content": "Do the task."}
        ])
        self.assertEqual(result, "Gemini result")
        self.assertIn("gemini-test:generateContent", requests[0].full_url)
        self.assertEqual(requests[0].get_header("X-goog-api-key"), "test-key")

    def test_quota_error_fails_over_only_to_verified_free_openrouter(self):
        calls = []
        def fake_open(request, timeout):
            calls.append(request)
            if len(calls) == 1:
                raise urllib.error.HTTPError(request.full_url, 429, "quota", {}, None)
            return FakeResponse({"choices": [{"message": {"content": "OpenRouter result"}}]})
        client = HostedModelClient(self.config(), {
            "GEMINI_API_KEY": "gemini-key", "GEMINI_MODEL": "gemini-test",
            "OPENROUTER_API_KEY": "router-key", "OPENROUTER_MODEL": "free/test"
        }, urlopen=fake_open)
        result = client.chat("hosted:auto", [{"role": "user", "content": "hello"}])
        self.assertEqual(result, "OpenRouter result")
        self.assertEqual(len(calls), 2)
        self.assertEqual(calls[1].get_header("Authorization"), "Bearer router-key")

    def test_no_paid_fallback_when_all_free_providers_fail(self):
        def fake_open(request, timeout):
            raise urllib.error.HTTPError(request.full_url, 429, "quota", {}, None)
        client = HostedModelClient(self.config(), {
            "GEMINI_API_KEY": "gemini-key", "GEMINI_MODEL": "gemini-test",
            "OPENROUTER_API_KEY": "router-key", "OPENROUTER_MODEL": "free/test"
        }, urlopen=fake_open)
        with self.assertRaisesRegex(ProviderUnavailable, "no paid fallback"):
            client.chat("hosted:auto", [{"role": "user", "content": "hello"}])


if __name__ == "__main__":
    unittest.main()
