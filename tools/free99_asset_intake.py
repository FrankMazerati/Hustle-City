#!/usr/bin/env python3
"""Free 99 asset intake scanner.

Inventories local staged files, hashes them, and writes a provenance manifest.
It does NOT download assets, extract archives, determine license rights, or
import assets into Unreal Engine.

Example:
  python3 tools/free99_asset_intake.py --scan ./staging/Quaternius/CityKit \
    --creator Quaternius --pack DowntownCityMegaKit-Standard \
    --source-url https://quaternius.itch.io/downtown-city-megakit \
    --license CC0-1.0 --price-usd 0 --output ./manifests/quaternius-city.json
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from datetime import datetime, timezone

EXTENSIONS = {
    ".uasset", ".umap", ".fbx", ".obj", ".gltf", ".glb", ".blend",
    ".usd", ".usdz", ".abc", ".png", ".jpg", ".jpeg", ".tga", ".exr",
    ".hdr", ".tif", ".tiff", ".wav", ".mp3", ".ogg", ".zip", ".7z", ".rar"
}

def file_hash(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scan", required=True)
    parser.add_argument("--output", default="free99-asset-manifest.json")
    parser.add_argument("--creator", default="")
    parser.add_argument("--pack", default="")
    parser.add_argument("--source-url", default="")
    parser.add_argument("--license", default="UNVERIFIED")
    parser.add_argument("--price-usd", default="UNVERIFIED")
    args = parser.parse_args()

    root = Path(args.scan).expanduser().resolve()
    if not root.is_dir():
        parser.error(f"Not a directory: {root}")

    records = []
    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        ext = path.suffix.lower()
        if ext not in EXTENSIONS:
            continue
        records.append({
            "relative_path": str(path.relative_to(root)),
            "extension": ext,
            "size_bytes": path.stat().st_size,
            "sha256": file_hash(path),
            "classification": (
                "archive" if ext in {".zip", ".7z", ".rar"} else
                "unreal_asset" if ext in {".uasset", ".umap"} else
                "model_or_scene" if ext in {".fbx", ".obj", ".gltf", ".glb", ".blend", ".usd", ".usdz", ".abc"} else
                "texture_or_environment" if ext in {".png", ".jpg", ".jpeg", ".tga", ".exr", ".hdr", ".tif", ".tiff"} else
                "audio"
            )
        })

    manifest = {
        "schema_version": 1,
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "intake_status": "STAGED_NOT_IMPORTED",
        "root_folder_name": root.name,
        "creator": args.creator,
        "pack": args.pack,
        "source_url": args.source_url,
        "license": args.license,
        "price_usd": args.price_usd,
        "commercial_use_verified": False,
        "attribution_required": "UNVERIFIED",
        "engine_version_tested": None,
        "technical_validation": "NOT_RUN",
        "creator_approval": "PENDING",
        "files": records,
        "warnings": [
            "Scanner does not establish license, price, provenance, or commercial rights.",
            "Manually verify exact creator terms before importing or shipping.",
            "Keep untouched source packages separate from modified Hustle City assets.",
            "A checksum identifies file bytes; it does not prove authenticity."
        ]
    }
    output = Path(args.output).expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Scanned {len(records)} recognized files from {root}")
    print(f"Manifest: {output}")
    print("Status: STAGED_NOT_IMPORTED; license and UE validation remain required.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
