# IntelliSync dependency checker

A first, engine-neutral dependency-impact tool for Hustle City's shared world registry. It uses only Python's standard library.

## Run it

From the repository root:

```bash
python SHARED_CORE/tools/intellisync_dependency_check.py SHARED_CORE/examples/traffic-signal-change.json
```

Save a report:

```bash
python SHARED_CORE/tools/intellisync_dependency_check.py SHARED_CORE/examples/traffic-signal-change.json --output /tmp/intellisync-impact.json
```

Run tests:

```bash
python -m unittest discover -s SHARED_CORE/tools/tests -v
```

## Impact behavior

The checker starts with the changed system IDs, then expands through the registry's declared dependencies and relationships. The default fixture uses depth 1, so a traffic-signal change identifies directly connected systems and their owners for review. Increase `max_dependency_depth` to explore a wider dependency neighborhood.

This is deliberately conservative: an affected system is a review candidate, not proof that it contains a defect. The tool never edits project files, approves a change, or silently applies a recommendation. Review and approval remain explicit.

The registry's `owner_agent` fields identify intended role ownership only; they do not prove that those agents are currently activated or running.
