---
arys_schema_version: '1.2'
id: 36fcdf2d-1899-4926-8852-d222d6a3fc79
title: TEMPLATE FILE - DO NOT SHIP AS-IS
type: TECHNICAL
status: active
trust_level: 2
visibility: internal
created: '2026-02-18T17:57:54Z'
last_modified: '2026-02-18T17:57:54Z'
---

# TEMPLATE FILE - DO NOT SHIP AS-IS

This file is a TEMPLATE.
Replace every `[REPLACE_ME:...]` placeholder before use.

---

# 11 Build Instructions - [REPLACE_ME:PROJECT_NAME]

**Version**: [REPLACE_ME:VERSION]  
**Date**: [REPLACE_ME:DD.MM.YYYY]  
**Purpose**: Build and package the plugin from source

**Tag block:**
#framework_integration #best_practices #construction #conversion #blender #rhino #workflow_automation #extension_development

## Choose the platform build script

This project uses a platform overlay. Use the appropriate build script:

- **Blender**: `scripts/build_extension.py`
- **Rhino**: `Scripts/build_release.ps1` (builds `.rhp` into `releases/`)

## Prerequisites

- **Blender path**: Python installed (`python --version`)
- **Rhino path**: .NET SDK and Rhino 8 installed

## Build

[REPLACE_ME:BUILD_COMMANDS]

## Output

See `OUTPUT_FOLDER.md`.
