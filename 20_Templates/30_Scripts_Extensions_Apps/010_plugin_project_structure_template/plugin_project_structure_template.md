---
arys_schema_version: '1.2'
id: 41f3d69e-3b33-469f-a719-76ffcb784461
title: Plugin Project Structure Template
type: TECHNICAL
status: active
trust_level: 2
visibility: internal
created: '2026-02-19T14:08:23Z'
last_modified: '2026-02-19T14:08:23Z'
---

# Plugin Project Structure Template

**Version**: 1.2.0 | **Date**: 18.02.2026 | **Time**: 20:20 | **GlobalID**: 20260218_2020_General_Scripts_Extensions_Apps_PluginTemplate

**Tag block:**
#best_practices #automation #framework_integration #openusd #usd_core #export #workflow_automation #extension_development

---

## Overview

This is the canonical structure for plugin development projects in this framework.

- Common documentation scaffold: `TEMPLATE_Plugin_Project_Common/`
- Platform overlays:
  - `platforms/Blender/` (Python addon)
  - `platforms/Rhino/` (C#/.NET RhinoCommon plugin)
- Generic option:
  - `--platform generic` for docs-only scaffolds (C4D, Maya, Houdini, etc.)

Bootstrap script:

- `General_Scripts_Extensions_Apps/040_Proj_TOOLS/utilities/bootstrap_plugin_project.py`

---

## Canonical Common Structure

Note on discovery naming:
- `00_Discovery.md` is the lifecycle/index entry.
- Canonical discovery artifacts should follow suffix naming: `*_DISCOVERY.md`.
- If both exist, `00_Discovery.md` must link to the canonical `*_DISCOVERY.md` file.

```text
PluginName/
|-- README.md
|-- LICENSE
|-- .gitignore
|-- 00_Discovery.md
|-- 01_Requirements_Questionnaire.md
|-- 02_Detailed_Requirements.md
|-- 02A_Requirements_Phase1.md
|-- 03_Module_Design.md
|-- 04_Implementation_Plan.md
|-- 04A_Implementation_Plan_Phase1.md
|-- 05_Testing_Plan.md
|-- 06_TROUBLESHOOTING.md
|-- 09_Roadmap.md
|-- 10_USER_GUIDE.md
|-- 11_BUILD_INSTRUCTIONS.md
|-- 80_WIP.md
|-- 99_HANDOFF.md
|-- 99_HANDOFF_SESSION.md
|-- OUTPUT_FOLDER.md
|-- docs/
`-- tests/
```

### Minimum testing scaffold (mandatory)

```text
tests/
|-- README.md
|-- pytest.ini
|-- unit/
|   `-- test_smoke.py
|-- integration/
|   `-- README.md
|-- scenarios/
|   |-- README.md
|   `-- scenario_primary_workflow.yml
`-- manual/
    `-- README.md
```

Master + sub-document pattern:

- Requirements master: `02_Detailed_Requirements.md`
- Requirements sub-docs: `02A_...`, `02B_...`, ...
- Implementation master: `04_Implementation_Plan.md`
- Implementation sub-docs: `04A_...`, `04B_...`, ...
- Handoff master: `99_HANDOFF.md`
- Session handoffs: `99A_Handoff_YYYYMMDD_[Topic].md`, ...

---

## Platform Overlay: Blender

Generated structure includes:

- `scripts/build_extension.py`
- `blender_addon/__init__.py`
- `blender_addon/operators/`
- `blender_addon/ui/`
- `blender_addon/utils/`
- `dist/` (build output)

Build:

```bash
python scripts/build_extension.py
```

---

## Platform Overlay: Rhino

Generated structure includes:

- `RhinoUSDMultiExport.csproj`
- `RhinoUSDMultiExportPlugin.cs`
- `Commands/UsdMultiExportExportAll.cs`
- `Core/ExportEngine.cs`
- `Models/ExportOptions.cs`
- `UI/UsdMultiExportPanel.cs`
- `Utils/PathResolver.cs`
- `Properties/AssemblyInfo.cs`
- `Scripts/build_release.ps1`
- `releases/` (build output)

Build:

```powershell
powershell -ExecutionPolicy Bypass -File Scripts/build_release.ps1
```

Expected release artifact:

- `releases/RhinoUSDMultiExport.rhp`

---

## Generic (Docs-Only) Mode

Use `--platform generic` for C4D/Maya/Houdini or other pipelines where code overlay should be added manually later.

Command:

```bash
python General_Scripts_Extensions_Apps/040_Proj_TOOLS/utilities/bootstrap_plugin_project.py --platform generic --dest "PATH_TO_NEW_REPO"
```

---

## What This Template Is Based On

Reference projects reviewed:

- `C4D_USD_MultiExport` (latest common-doc structure baseline)
- `Blender_USD_MultiExport` (Blender overlay reality)
- `Rhino_USD_MultiExport` (Rhino C#/.NET overlay reality)

---

## Decision Record (2026-02-18)

Context:
- Template audit found drift between Rhino template overlay and actual Rhino project reality.

Decision:
- Rhino overlay is standardized to C#/.NET RhinoCommon scaffold files.
- Bootstrap validation checks Rhino C# scaffold files instead of legacy Python/Yak template files.
- Bootstrap excludes template `archive/` files from generated projects.

Reason:
- Avoid generating outdated Rhino scaffolds.
- Keep template output aligned with current shipped Rhino project structure.
- Prevent legacy/deprecated template files from leaking into new projects.

Traceability:
- Execution workflow: `General_Scripts_Extensions_Apps/010_Proj_GUIDES/G008_Plugin_Project_Bootstrap_GUIDE.md`
- Historical handover: `Master_Rules/060_Framework_HANDOVERS/A039_Plugin_Template_Rhino_Overlay_Alignment_HANDOVER.md`
- Enforced by script: `General_Scripts_Extensions_Apps/040_Proj_TOOLS/utilities/bootstrap_plugin_project.py`

---

## Quality Rules

1. Do not invent structure manually; always bootstrap.
2. Keep `00/02/04/80/99` files as first-class lifecycle docs (index/entry docs).
3. Use canonical suffix artifacts for full content (`*_DISCOVERY.md`, `*_RESEARCH*.md`, `*_TUTORIAL*.md`, `*_IMPLEMENTATION_PLAN*.md`, `*_REQUIREMENTS*.md`).
4. If both lifecycle and canonical docs exist for the same kind, lifecycle docs must link to canonical docs instead of duplicating full narrative content.
5. Use sub-documents for phase scaling (`02A+`, `04A+`, `99A+`).
6. Keep template placeholders explicit: `[REPLACE_ME:...]`.
7. Avoid copying archived/deprecated template files into new projects.
8. Every generated project must include the testing scaffold and a concrete `05_Testing_Plan.md`.

---

## Related Files

- Bootstrap guide:
  - `General_Scripts_Extensions_Apps/010_Proj_GUIDES/G008_Plugin_Project_Bootstrap_GUIDE.md`
- Bootstrap script:
  - `General_Scripts_Extensions_Apps/040_Proj_TOOLS/utilities/bootstrap_plugin_project.py`
- Skill orchestration:
  - `.cursor/skills/bootstrap-plugin/SKILL.md`
  - `.cursor/skills/plugin-from-discovery/SKILL.md`
