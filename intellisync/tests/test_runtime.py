import json
import tempfile
import unittest
from pathlib import Path

from intellisync.runtime import IntelliSync, InvalidTransition, ConfigurationError


class RuntimeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.config = self.root / "pipeline.json"
        self.config.write_text(json.dumps({
            "project": "Hustle City",
            "stations": [
                {"station_id": "world-builder", "role": "World Builder", "agent_id": "world-builder"},
                {"station_id": "city-builder", "role": "City Builder", "agent_id": "city-builder"},
                {"station_id": "roads-infrastructure", "role": "Roads", "agent_id": "roads-infrastructure"}
            ]
        }), encoding="utf-8")
        self.db = self.root / "test.sqlite3"
        self.app = IntelliSync(self.db, self.config)
        self.qa = {s: "QA-1" for s in ("world-builder", "city-builder", "roads-infrastructure")}

    def tearDown(self):
        self.temp.cleanup()

    def make_package(self):
        return self.app.create_package("world_build", {"scope": "test"}, self.qa, "HC-PKG-TEST")

    def test_qa_approval_releases_next_station(self):
        pid = self.make_package()
        self.app.claim(pid, "world-builder", "world-builder")
        self.app.submit(pid, "world-builder", "world-builder", "Terrain specification")
        self.assertEqual(self.app.review(pid, "world-builder", "QA-1", "approve"), "released:city-builder")
        state = self.app.status(pid)[0]
        self.assertEqual(state["current_station"], "city-builder")
        self.assertEqual(state["stations"][-1]["status"], "ready")

    def test_rejection_routes_back_to_same_station(self):
        pid = self.make_package()
        self.app.claim(pid, "world-builder", "world-builder")
        self.app.submit(pid, "world-builder", "world-builder", "Draft")
        self.assertEqual(self.app.review(pid, "world-builder", "QA-1", "reject", "Add elevation data"), "rework")
        self.app.claim(pid, "world-builder", "world-builder")
        self.app.submit(pid, "world-builder", "world-builder", "Corrected draft")
        self.assertEqual(self.app.review(pid, "world-builder", "QA-1", "approve"), "released:city-builder")

    def test_wrong_reviewer_and_self_approval_are_blocked(self):
        pid = self.make_package()
        self.app.claim(pid, "world-builder", "world-builder")
        self.app.submit(pid, "world-builder", "world-builder", "Draft")
        with self.assertRaises(InvalidTransition):
            self.app.review(pid, "world-builder", "QA-2", "approve")
        with self.assertRaises(InvalidTransition):
            self.app.review(pid, "world-builder", "world-builder", "approve")

    def test_duplicate_submit_event_is_idempotent(self):
        pid = self.make_package()
        self.app.claim(pid, "world-builder", "world-builder")
        self.app.submit(pid, "world-builder", "world-builder", "Draft", "evt-1")
        self.app.submit(pid, "world-builder", "world-builder", "Different duplicate", "evt-1")
        self.assertEqual(self.app.status(pid)[0]["stations"][0]["status"], "qa_pending")

    def test_package_finishes_after_last_qa(self):
        pid = self.make_package()
        for station, agent in [
            ("world-builder", "world-builder"),
            ("city-builder", "city-builder"),
            ("roads-infrastructure", "roads-infrastructure")
        ]:
            self.app.claim(pid, station, agent)
            self.app.submit(pid, station, agent, f"{station} output")
            result = self.app.review(pid, station, "QA-1", "approve")
        self.assertEqual(result, "complete")
        self.assertEqual(self.app.status(pid)[0]["status"], "complete")

    def test_restart_preserves_qa_queue(self):
        pid = self.make_package()
        self.app.claim(pid, "world-builder", "world-builder")
        self.app.submit(pid, "world-builder", "world-builder", "Draft")
        restarted = IntelliSync(self.db, self.config)
        self.assertEqual(restarted.recover()["awaiting_qa"], 1)
        self.assertEqual(restarted.status(pid)[0]["status"], "qa_pending")

    def test_qa_mapping_is_required(self):
        with self.assertRaises(ConfigurationError):
            self.app.create_package("world_build", {}, {})


if __name__ == "__main__":
    unittest.main()
