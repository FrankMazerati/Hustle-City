import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "intellisync_daily_sync.py"
SPEC = importlib.util.spec_from_file_location("intellisync_daily_sync", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class DailySyncTests(unittest.TestCase):
    def setUp(self):
        self.data = {
            "snapshot_date": "2026-11-20",
            "roster": [
                {"agent_id": "alpha", "role": "Roads"},
                {"agent_id": "beta", "role": "Traffic"},
                {"agent_id": "gamma", "role": "Dialogue"}
            ],
            "reports": [
                {"agent_id": "alpha", "report_date": "2026-11-20",
                 "completed": ["finished fixture"], "in_progress": ["next task"],
                 "blockers": [], "reviews_pending": []},
                {"agent_id": "beta", "report_date": "2026-11-19",
                 "completed": [], "in_progress": [], "blockers": ["waiting"],
                 "reviews_pending": ["alpha"]}
            ]
        }

    def test_counts_missing_stale_blockers_and_reviews(self):
        result = MODULE.build_daily_snapshot(self.data)
        self.assertEqual(result["totals"]["reports_missing"], 1)
        self.assertEqual(result["totals"]["reports_stale"], 1)
        self.assertEqual(result["totals"]["blockers"], 1)
        self.assertEqual(result["totals"]["reviews_pending"], 1)
        self.assertEqual(result["totals"]["completed_items"], 1)
        self.assertEqual(
            [item["agent_id"] for item in result["actions_required"]],
            ["beta", "gamma"]
        )

    def test_unknown_report_agent_is_rejected(self):
        self.data["reports"].append({"agent_id": "outsider", "report_date": "2026-11-20"})
        with self.assertRaisesRegex(ValueError, "unknown agent"):
            MODULE.build_daily_snapshot(self.data)

    def test_duplicate_reports_are_rejected(self):
        self.data["reports"].append(self.data["reports"][0])
        with self.assertRaisesRegex(ValueError, "duplicate daily report"):
            MODULE.build_daily_snapshot(self.data)


if __name__ == "__main__":
    unittest.main()
