# Building Asset Packages

This directory is the repository home for building-specific production packages.

## Structure

- `_template/` contains the starter manifest for a new building package.
- Add one subdirectory per approved building package, using its stable `building_id` as the directory name.
- Keep canonical building identity and gameplay metadata in the engine-neutral world inventory. This directory holds asset-package manifests and the assets they reference.
- Do not create final building packages, assign IDs, or treat working names as approved canon until the creator approves the building record.

## Package contents

A package may contain exterior assets, interior assets, signage, textures/materials, lighting references, audio references, and implementation notes as applicable. Only list assets that actually exist. Empty lists mean no assets have been supplied yet.

The starter manifest is a schema-shaped draft based on `world/BUILDING_IDENTITY_AND_INTERACTION_CATALOG.md`; it is not a completed building record.
