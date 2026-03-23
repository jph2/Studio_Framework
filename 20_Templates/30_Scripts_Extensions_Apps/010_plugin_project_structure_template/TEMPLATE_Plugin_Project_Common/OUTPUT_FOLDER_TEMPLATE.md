---
arys_schema_version: '1.2'
id: 7f0c2d61-2dad-4905-b01c-87a3fb12e9a7
title: TEMPLATE FILE - DO NOT SHIP AS-IS
type: TECHNICAL
status: active
trust_level: 2
visibility: internal
created: '2026-02-18T17:58:25Z'
last_modified: '2026-02-18T17:58:25Z'
---

**Version**: 1.0.0 | **Date**: 16.02.2026 | **Time**: 12:00 | **GlobalID**: 20260216_1200_General_Dev_batch

**Tag block:**
#framework_integration #best_practices #blender #rhino #references #workflow_automation #extension_development

# TEMPLATE FILE - DO NOT SHIP AS-IS

This file is a TEMPLATE.
Replace every `[REPLACE_ME:...]` placeholder before use.

---

# Output folder - packaged builds

This project produces installable packages.

## Blender

- Output folder: `dist/` (usually generated, often gitignored)
- Package: `dist/[REPLACE_ME:ZIP_FILENAME].zip`

Build:

```bash
python scripts/build_extension.py
```

Install:
Blender -> Edit -> Preferences -> Extensions -> Install from Disk

## Rhino

- Output folder: `releases/`
- Package: `releases/[REPLACE_ME:RHP_FILENAME].rhp`

Build:

```powershell
powershell -ExecutionPolicy Bypass -File Scripts/build_release.ps1
```

Install:
Rhino -> Tools -> Options -> Plug-ins -> Install...
