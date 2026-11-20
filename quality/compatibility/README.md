# Cross-Engine Compatibility QA

This suite verifies that the Unreal Engine 5 and Unity 6 adapters interpret shared Hustle City contracts consistently.

## Required fixture categories
- Valid records.
- Missing required fields.
- Unknown enum values.
- Boundary numeric values.
- Unsupported schema versions.
- Unit/coordinate conversion cases.
- Save-data migration cases.

## Acceptance rule
A shared feature is not marked Parity Verified until both adapters pass equivalent tests against the same canonical fixtures. A documentation-only adapter is not an implemented adapter.
