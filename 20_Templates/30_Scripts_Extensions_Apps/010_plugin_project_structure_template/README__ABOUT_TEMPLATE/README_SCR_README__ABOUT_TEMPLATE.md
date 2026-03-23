---
arys_schema_version: '1.2'
id: fcc17b63-b880-4020-bc9e-e9df0468201a
title: About this folder-based template
type: TECHNICAL
status: active
trust_level: 2
visibility: internal
created: '2026-02-18T05:33:28Z'
last_modified: '2026-02-18T05:33:28Z'
---

# About this folder-based template

**Version**: 1.0.0 | **Date**: 18.01.2026 | **Time**: 12:00 | **GlobalID**: 20260118_1200_General_Scripts_Extensions_Apps_PluginTemplate_About

**Tag block:**
#best_practices #automation #framework_integration #workflow_automation #extension_development #analysis #quality_assurance #validation

## Why this exists

This plugin-project template is **folder-based** to remove ambiguity:

- You can **see the final structure** immediately in a file tree.
- An LLM (or human) does not need to “mentally reconstruct” folders from a description.
- It reduces drift and prevents “missing files” mistakes.

## Design choice: Common template + platform overlays

Most project structure is **platform-agnostic** (documentation conventions, numbering, README responsibilities).

Only a small subset is **platform-deterministic**:
- Blender: ZIP packaging + `bl_info` + operators/panels
- Rhino: Yak packaging + `manifest.yml` + commands/modules

So we keep:

- `TEMPLATE_Plugin_Project_Common/` (single source of truth for docs + structure)
- `platforms/Blender/` overlay (only Blender-specific files)
- `platforms/Rhino/` overlay (only Rhino-specific files)

This avoids maintaining two nearly-identical full templates.

## How to use

1. Copy `TEMPLATE_Plugin_Project_Common/` to a new repo folder name.
2. Choose a platform overlay:
   - Copy `platforms/Blender/*` into the repo root (merge directories).
   - OR copy `platforms/Rhino/*` into the repo root (merge directories).
3. Replace all `[REPLACE_ME:…]` placeholders.
4. Rename files by removing `_TEMPLATE` once you start “real” work.

