# Shared Asset Library

Store source assets and portable manifests here, not engine-generated import caches.

## Suggested organization
- `source/characters`, `source/clothing`, `source/buildings`, `source/vehicles`, `source/roads`, `source/rail`, `source/props`, `source/animations`, `source/audio`, `source/environments`
- `interchange/`: approved exports such as glTF or FBX.
- `manifests/`: stable asset IDs, variants, scale, orientation, dependencies, and checksums.
- `licenses/`: provenance, license terms, attribution, and usage permissions.

Do not commit purchased or downloaded assets until their license permits repository storage and the intended distribution workflow. Keep source files where possible; engine imports are reproducible outputs.
