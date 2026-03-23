---
arys_schema_version: '1.2'
id: a655cb7f-b230-440b-952d-75c14fe82f1f
title: 010 Plugin Project Structure Template
type: TECHNICAL
status: active
trust_level: 2
visibility: internal
created: '2026-02-18T18:08:39Z'
last_modified: '2026-02-18T18:08:39Z'
---

# 010 Plugin Project Structure Template

**Version**: 1.2.0 | **Date**: 18.02.2026 | **Time**: 21:20 | **GlobalID**: 20260218_2120_General_Scripts_Extensions_Apps_PluginTemplateReadme

**Purpose**: Entry file for the canonical plugin scaffold system.

## Canonical source files

- Structure contract:
  - `plugin_project_structure_template.md`
- Bootstrap workflow:
  - `../../010_Proj_GUIDES/G008_Plugin_Project_Bootstrap_GUIDE.md`
- Bootstrap script:
  - `../../040_Proj_TOOLS/utilities/bootstrap_plugin_project.py`

## Template layout

- `TEMPLATE_Plugin_Project_Common/`:
  - Common project docs and lifecycle files (`00/02/04/80/99`, `OUTPUT_FOLDER`, `README`, etc.)
- `platforms/Blender/`:
  - Blender addon overlay (`scripts/build_extension_TEMPLATE.py`, `blender_addon/...`)
- `platforms/Rhino/`:
  - Rhino C#/.NET overlay (`RhinoUSDMultiExport.csproj`, `Commands/`, `Core/`, `Models/`, `UI/`, `Utils/`, `Scripts/build_release.ps1`)

## Usage

Preferred (deterministic):

```bash
python 040_Proj_TOOLS/utilities/bootstrap_plugin_project.py --platform blender --dest "PATH_TO_NEW_REPO"
python 040_Proj_TOOLS/utilities/bootstrap_plugin_project.py --platform rhino --dest "PATH_TO_NEW_REPO"
python 040_Proj_TOOLS/utilities/bootstrap_plugin_project.py --platform generic --dest "PATH_TO_NEW_REPO"
```

Manual copying is supported but not recommended.

