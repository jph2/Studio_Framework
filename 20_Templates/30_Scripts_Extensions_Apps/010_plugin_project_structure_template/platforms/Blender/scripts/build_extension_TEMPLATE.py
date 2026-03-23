#!/usr/bin/env python3
"""
⚠️ TEMPLATE FILE — DO NOT SHIP AS-IS

Blender platform overlay — build ZIP.
Copy this file into your repo root at: scripts/build_extension.py
"""

import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
ADDON_DIR = REPO_ROOT / "blender_addon"
OUTPUT_DIR = REPO_ROOT / "dist"
ZIP_NAME = "REPLACE_ME_addon.zip"


def build_zip() -> Path:
    if not ADDON_DIR.exists():
        raise FileNotFoundError(f"Addon directory not found: {ADDON_DIR}")

    init_file = ADDON_DIR / "__init__.py"
    if not init_file.exists():
        raise FileNotFoundError(f"Missing __init__.py in: {ADDON_DIR}")

    OUTPUT_DIR.mkdir(exist_ok=True)
    zip_path = OUTPUT_DIR / ZIP_NAME
    if zip_path.exists():
        zip_path.unlink()

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file_path in ADDON_DIR.rglob("*"):
            if file_path.is_file():
                arcname = file_path.relative_to(ADDON_DIR.parent)
                zipf.write(file_path, arcname)

    return zip_path


if __name__ == "__main__":
    out = build_zip()
    print("[SUCCESS] Built ZIP:", out)

