# Shared Core — Engine-Neutral Foundation

This directory owns portable definitions and rules for Hustle City. It must not depend on Unreal Engine or Unity APIs.

## Contents
- `schemas/`: versioned JSON Schemas and example payloads.
- `rules/`: engine-neutral gameplay and simulation rules.
- `interfaces/`: contracts between systems.
- `content/`: data-driven city, character, interaction, and event definitions.

## Portability rules
- Use stable IDs, explicit schema versions, documented units, and deterministic enum values.
- Prefer JSON for authored definitions and interchange. Use binary formats only with a documented versioned contract.
- Never store engine object pointers, scene paths, Blueprint class names, Unity component types, or engine-specific resource handles in canonical shared data.
- Engine adapters may cache or transform shared data but must not silently change its meaning.
- Validate all authored data before runtime use.
- Keep secrets and private player information out of source-controlled content.
