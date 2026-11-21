import json
import tempfile
import unittest
from pathlib import Path

from intellisync.runtime import IntelliSync
from intellisync.services import AgentServices, Scheduler, ServiceConfigurationError


class FakeOllama:
    def __init__(self, replies):
        self.replies = list(replies)
        self.calls = []

    def chat(self, model, messages, temperature=0.2):
        self.calls.append((model, messages, temperature))
        return self.replies.pop(0)


class ServiceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.pipeline = self.root / "pipeline.json"
        self.pipeline.write_text(json.dumps({
            "project": "Hustle City",
            "stations": [
                {"station_id": "world-builder", "role": "World Builder", "agent_id": "world-builder", "qa_supervisor_id": "QA-1"},
                {"station_id": "city-builder", "role": "City Builder", "agent_id": "city-builder", "qa_supervisor_id": "QA-1"}
            ]
        }), encoding="utf-8")
        self.agent_config = self.root / "agents.json"
        self.agent_config.write_text(json.dumps({
            "ollama": {"endpoint": "http://127.0.0.1:11434"},
            "models": {"world-builder": "fake-model", "city-builder": "fake-model", "QA-1": "fake-model"},
            "qa": {"minimum_auto_approval_confidence": 0.85,
                   "require_nonempty_checks": True, "require_feedback": True}
        }), encoding="utf-8")
        self.db = self.root / "test.sqlite3"
        self.runtime = IntelliSync(self.db, self.pipeline)

    def tearDown(self):
        self.temp.cleanup()

    def create(self):
        return self.runtime.create_package("test_package", {"objective": "Test"}, {}, "HC-SERVICE-TEST")

    def test_worker_submission_and_qa_approval_releases_next_station(self):
        replies = [
            "World Builder deliverable: terrain, elevation and water boundaries.",
            json.dumps({"decision": "approve", "feedback": "All required terrain checks passed.",
                        "checks": ["terrain", "elevation", "water boundaries"], "confidence": 0.96})
        ]
        fake = FakeOllama(replies)
        services = AgentServices(self.runtime, self.agent_config, fake)
        scheduler = Scheduler(services, max_workers=1)
        self.create()
        first = scheduler.tick()
        self.assertEqual(first["outcomes"][0]["result"], "submitted_for_qa")
        second = scheduler.tick()
        self.assertEqual(second["outcomes"][0]["qa"]["result"], "released:city-builder")
        self.assertEqual(self.runtime.status("HC-SERVICE-TEST")[0]["current_station"], "city-builder")

    def test_low_confidence_approval_is_held_for_human_review(self):
        replies = [
            "Draft deliverable.",
            json.dumps({"decision": "approve", "feedback": "Possibly complete.",
                        "checks": ["some checks"], "confidence": 0.40})
        ]
        services = AgentServices(self.runtime, self.agent_config, FakeOllama(replies))
        scheduler = Scheduler(services)
        self.create()
        scheduler.tick()
        result = scheduler.tick()
        self.assertEqual(result["outcomes"][0]["qa"]["result"], "human_review_required")
        self.assertEqual(self.runtime.status("HC-SERVICE-TEST")[0]["status"], "qa_pending")

    def test_scheduler_refuses_missing_model_mapping(self):
        config = json.loads(self.agent_config.read_text(encoding="utf-8"))
        config["models"] = {}
        self.agent_config.write_text(json.dumps(config), encoding="utf-8")
        services = AgentServices(self.runtime, self.agent_config, FakeOllama([]))
        with self.assertRaises(ServiceConfigurationError):
            Scheduler(services)

    def test_invalid_qa_json_fails_closed_and_leaves_qa_pending(self):
        replies = ["Draft deliverable.", "not-json"]
        services = AgentServices(self.runtime, self.agent_config, FakeOllama(replies))
        scheduler = Scheduler(services)
        self.create()
        scheduler.tick()
        result = scheduler.tick()
        self.assertIn("not valid JSON", result["outcomes"][0]["error"])
        self.assertEqual(self.runtime.status("HC-SERVICE-TEST")[0]["status"], "qa_pending")


if __name__ == "__main__":
    unittest.main()
