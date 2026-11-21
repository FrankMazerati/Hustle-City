import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from intellisync_dependency_check import analyze_change, load_json

ROOT = Path(__file__).resolve().parents[3]
REGISTRY = load_json(ROOT / "SHARED_CORE/content/world-intelligence-registry.json")


class DependencyCheckerTests(unittest.TestCase):
    def test_traffic_signal_change_notifies_cross_system_owners(self):
        result = analyze_change(REGISTRY, {
            "change_id": "test-traffic",
            "changed_systems": ["traffic.signals"],
            "max_dependency_depth": 1
        })
        self.assertIn("pedestrians.crossing", result["affected_systems"])
        self.assertIn("vehicles.simulation", result["affected_systems"])
        self.assertIn("safety.recovery", result["affected_systems"])
        self.assertIn("npc-intelligence", result["review_required_from"])
        self.assertIn("vehicle-simulation", result["review_required_from"])
        self.assertEqual("pending_owner_review", result["approval"])

    def test_unknown_system_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Unknown changed system"):
            analyze_change(REGISTRY, {"changed_systems": ["traffic.magic"]})

    def test_invalid_depth_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "positive integer"):
            analyze_change(REGISTRY, {"changed_systems": ["traffic.signals"], "max_dependency_depth": 0})


if __name__ == "__main__":
    unittest.main()
