import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = Path(__file__).resolve().parents[1] / "intellisync_dialogue_chat.py"
SPEC = importlib.util.spec_from_file_location("intellisync_dialogue_chat", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
FIXTURE = ROOT / "SHARED_CORE/examples/frank-companion-event-dialogue-flow.json"


class DialogueChatTests(unittest.TestCase):
    def setUp(self):
        self.session = MODULE.create_session(FIXTURE)

    def test_player_turn_is_followed_by_one_coordinated_vendor_turn(self):
        result = MODULE.process_player_turn(self.session, "Where is the plaza?")
        self.assertEqual(result["player_turn"]["turn_index"], 4)
        self.assertEqual(result["selected_speaker_id"], MODULE.VENDOR_ID)
        self.assertEqual(result["reply_turn"]["turn_index"], 5)
        self.assertEqual(self.session["turn_index"], 5)

    def test_acceptance_routes_companion_turn(self):
        result = MODULE.process_player_turn(self.session, "Yeah, let's go")
        self.assertEqual(result["selected_speaker_id"], MODULE.COMPANION_ID)
        self.assertEqual(result["reply_turn"]["speaker_id"], MODULE.COMPANION_ID)

    def test_empty_player_message_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "cannot be empty"):
            MODULE.process_player_turn(self.session, "   ")

    def test_session_save_and_resume_preserves_history(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nested" / "session.json"
            MODULE.save_session(self.session, path)
            resumed = MODULE.load_or_create_session(FIXTURE, path)
            self.assertEqual(len(resumed["turns"]), 4)
            self.assertEqual(resumed["session_id"], self.session["session_id"])

    def test_invalid_turn_index_is_rejected(self):
        self.session["turn_index"] = 99
        with self.assertRaisesRegex(ValueError, "turn_index"):
            MODULE.validate_session(self.session)

    def test_unknown_participant_is_not_selected(self):
        self.session["participants"] = [
            p for p in self.session["participants"] if p["speaker_id"] != MODULE.COMPANION_ID
        ]
        with self.assertRaisesRegex(ValueError, "outside this session"):
            MODULE.process_player_turn(self.session, "Yeah, let's go")


if __name__ == "__main__":
    unittest.main()
