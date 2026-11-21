# Interactive IntelliSync dialogue prototype

From the repository root, run:

```bash
python SHARED_CORE/tools/intellisync_dialogue_chat.py
```

The first run copies the example conversation into a local session file under `~/.hustle-city/sessions/`. Type a response at the `You:` prompt. The dialogue coordinator records the player turn, selects one registered speaker, appends one authored local response, and saves the session after each exchange.

Useful commands:

- Type `/quit` to leave; the session is saved.
- Run the same command again to resume the saved conversation.
- Add `--reset` to restart from the original example.
- Add `--session-file /path/to/session.json` to choose a different save location.

Example:

```bash
python SHARED_CORE/tools/intellisync_dialogue_chat.py --reset
```

This is an interactive local turn-taking and persistence prototype. Responses are selected from a small authored set using simple keyword rules. It is not generative AI, a live NPC service, multiplayer networking, or Unreal Engine integration.
