import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = Path(__file__).resolve().parents[1] / "intellisync_runtime_demo.py"
SPEC = importlib.util.spec_from_file_location("intellisync_runtime_demo", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class RuntimeDemoTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(
            (ROOT / "SHARED_CORE/examples/frank-companion-event-dialogue-flow.json")
            .read_text(encoding="utf-8")
        )

    def test_eligible_online_player_receives_event(self):
        result = MODULE.route_event(self.data["player_context"], self.data["world_event"])
        self.assertTrue(result["delivered"])
        self.assertEqual(
            [n["event_type"] for n in result["notifications"]],
            ["world.event.discovered", "world.event.invited"]
        )

    def test_offline_player_does_not_receive_event(self):
        player = dict(self.data["player_context"], presence="offline")
        result = MODULE.route_event(player, self.data["world_event"])
        self.assertFalse(result["delivered"])
        self.assertEqual(result["reason"], "player_not_online")

    def test_player_outside_nearby_audience_is_not_routed(self):
        player = dict(self.data["player_context"], player_id="player.other")
        result = MODULE.route_event(player, self.data["world_event"])
        self.assertFalse(result["delivered"])
        self.assertEqual(result["reason"], "player_not_in_event_audience")

    def test_dialogue_turns_are_ordered_and_have_known_speakers(self):
        result = MODULE.validate_dialogue(self.data["dialogue_session"])
        self.assertEqual(result["turn_count"], 4)
        self.assertEqual(result["next_turn_index"], 4)
        self.assertEqual(result["turns"][3]["speaker_id"], "character.frank_companion_temporary")

    def test_unknown_dialogue_speaker_is_rejected(self):
        session = json.loads(json.dumps(self.data["dialogue_session"]))
        session["turns"][0]["speaker_id"] = "npc.unknown"
        with self.assertRaisesRegex(ValueError, "not in the session"):
            MODULE.validate_dialogue(session)

    def test_out_of_order_dialogue_turn_is_rejected(self):
        session = json.loads(json.dumps(self.data["dialogue_session"]))
        session["turns"][2]["turn_index"] = 9
        with self.assertRaisesRegex(ValueError, "contiguous"):
            MODULE.validate_dialogue(session)


if __name__ == "__main__":
    unittest.main()
