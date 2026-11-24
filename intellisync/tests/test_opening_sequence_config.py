import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "opening_sequence_work_packages.json"


class OpeningSequenceConfigTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = json.loads(CONFIG.read_text(encoding="utf-8"))
        cls.tasks = cls.config["tasks"]
        cls.by_id = {task["task_id"]: task for task in cls.tasks}

    def test_cycle_matches_creator_approved_20_5_5(self):
        schedule = self.config["schedule"]
        self.assertEqual(schedule["production_seconds"], 1200)
        self.assertEqual(schedule["independent_qa_seconds"], 300)
        self.assertEqual(schedule["correction_seconds"], 300)
        self.assertEqual(schedule["optional_extension_seconds"], 600)
        self.assertEqual(schedule["mode"], "rolling_overlapping_per_agent_package_cycles")
        self.assertFalse(schedule["scheduler_enabled"])

    def test_fourteen_task_owners_cover_creative_and_production_roles(self):
        owners = {task["agent_id"] for task in self.tasks}
        expected = {"SCRIBE", "LENS"} | {
            f"P{i:02d}-{name}" for i, name in [
                (1, "GEOGRAPHY"), (2, "CITY-PLAN"), (3, "DISTRICTS"),
                (4, "ARCHITECTURE"), (5, "INTERIORS"), (6, "TRANSIT"),
                (7, "VEHICLES"), (8, "CHARACTERS"), (9, "NPC-NAV"),
                (10, "GAMEPLAY"), (11, "ONBOARDING"),
                (12, "UNREAL-INTEGRATION")
            ]
        }
        self.assertEqual(owners, expected)
        self.assertEqual(len(self.tasks), 14)

    def test_qa_supervisors_cover_twelve_specialists_once(self):
        qa = self.config["qa_ownership"]
        groups = [qa["QA-1"], qa["QA-2"], qa["QA-3"]]
        self.assertEqual([len(group) for group in groups], [4, 4, 4])
        flattened = [agent for group in groups for agent in group]
        self.assertEqual(len(flattened), 12)
        self.assertEqual(len(set(flattened)), 12)
        for task in self.tasks:
            if task["agent_id"].startswith("P"):
                self.assertIn(task["agent_id"], qa[task["qa_supervisor_id"]])
            else:
                self.assertEqual(task["review_policy"], "coordinator_assigns_independent_qa")

    def test_all_dependencies_exist_and_graph_is_acyclic(self):
        state = {}

        def visit(task_id):
            if state.get(task_id) == "visiting":
                self.fail(f"Dependency cycle detected at {task_id}")
            if state.get(task_id) == "done":
                return
            state[task_id] = "visiting"
            task = self.by_id[task_id]
            for dependency in task["hard_dependencies"]:
                self.assertIn(dependency, self.by_id)
                visit(dependency)
            state[task_id] = "done"

        for task_id in self.by_id:
            visit(task_id)

    def test_every_task_has_deliverables_and_acceptance_criteria(self):
        for task in self.tasks:
            with self.subTest(task=task["task_id"]):
                self.assertTrue(task["deliverables"])
                self.assertTrue(task["acceptance_criteria"])


if __name__ == "__main__":
    unittest.main()
