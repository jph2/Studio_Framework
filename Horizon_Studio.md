---
arys_schema_version: "1.2"
id: "0ff7f0d1-e72e-4343-ab16-ecc86a00f8dc"
title: "Horizon_Studio"
type: GOVERNANCE
status: active
trust_level: 3
created: "2026-03-23T22:37:00Z"
last_modified: "2026-03-23T22:37:00Z"
author: "TARS"
provenance:
  git_repo: "Studio_Framework"
  git_branch: "main"
  git_commit_short: null
  git_commit_full: null
  git_path: "Horizon_Studio.md"
tags: [studio_framework, orientation, governance, horizon]
---

# Horizon_Studio

**Version**: 0.1.0 | **Date**: 23.03.2026 | **Time**: 23:37 | **GlobalID**: 20260323_2337_Horizon_Studio_v0

**Last Updated:** 23.03.2026 23:37  
**Framework:** Studio_Framework  
**Status:** beta

**Git:** Repo: Studio_Framework | Branch: main | Path: Horizon_Studio.md | Commit: pending

**Tag block:**
#studio_framework #orientation #governance #horizon

---

Horizon_Studio is the quick orientation map for the Studio Framework.

## Purpose

Use this file to understand, at a glance:
- what Studio is for
- where live work lives
- how artifacts move
- how Studio relates to OpenClaw and separate project repos

This is not a task board.
This is not a duplicate README.
This is a lean operating map.

---

## 1. Role of Studio

Studio Framework sits **beside** OpenClaw.

- **OpenClaw** governs, routes, remembers, and orchestrates
- **Studio Framework** holds the production/incubation structure and the live evolving artifacts
- **Project repos** hold implementation truth when work gains enough project gravity

---

## 2. Main split inside Studio

## Live work
- `00_Artifacts/`

This is where the actual working documents live.

## Structural / governing layers
- `10_Artifact_System/`
- `20_Templates/`
- `30_Workflows/`
- `40_Quality_System/`
- `50_Tool_Surfaces/`
- `60_Connectors/`
- `70_Domain_Playbooks/`
- `80_Project_Bridges/`
- `90_Reference_Archive/`

These folders do not primarily hold the live work itself.
They define how work is structured, templated, reviewed, routed, matured, bridged, and archived.

---

## 3. Artifact flow

The base phase is:
- `00_Artifacts/10_discovery-research/`

This is where:
- broad Discovery begins
- Research becomes the first distillation

From there, work may branch into:
- `00_Artifacts/20_tutorial-prep/`
- `00_Artifacts/30_paper-prep/`
- `00_Artifacts/40_project-prep/`

Additional artifact areas:
- `00_Artifacts/50_admin-ops/`
- `00_Artifacts/60_social-content/`

Important:
Studio itself already behaves like a backlog / kanban field.
A separate markdown task board is intentionally not the primary structure.

---

## 4. Core artifact rules

- Discovery and Research stay together in the shared base phase
- Requirements are the default mandatory structured continuation artifact for project-oriented work
- Specs are optional and used only when deeper design detail is genuinely needed
- all important artifacts should preserve traceability upstream/downstream
- tags should use the canonical tag system first, and only expand when coverage is genuinely missing

---

## 5. Key orientation files

### Studio overview
- `README_Studio_Framework.md`

### Artifact system / schema
- `10_Artifact_System/README_Artifact_System.md`
- `10_Artifact_System/10_Schema/Standard_ARYS.md`
- `10_Artifact_System/10_Schema/master_tag_system.yml`
- `10_Artifact_System/10_Schema/TAG_SEMANTIC_INDEX.md`
- `10_Artifact_System/10_Schema/TOPIC_TO_TAG_MAPPING.md`

### Template families
- `20_Templates/10_Research/`
- `20_Templates/20_Tutorials/`
- `20_Templates/30_Scripts_Extensions_Apps/`
- `20_Templates/NOTE_Template_Families_Preservation.md`

### Workflow guidance
- `30_Workflows/Workflow_Artifacts.md`
- `30_Workflows/Workflow_Research.md`
- `30_Workflows/Workflow_Tutorials.md`
- `30_Workflows/Workflow_Project_Promotion.md`
- `30_Workflows/Workflow_Tag_Sync.md`

### Quality guidance
- `40_Quality_System/README_Quality_System.md`
- `40_Quality_System/Quality_Tutorials.md`

### Bridge guidance
- `80_Project_Bridges/README_Project_Bridges.md`
- `80_Project_Bridges/Bridge_Research_to_Project.md`

---

## 6. Current architectural stance

- preserve good legacy structure, but do not replicate old clutter
- keep templates preserved first; canonical hardening comes later
- rely on deterministic support where metadata/tagging drift matters
- do not treat domains as WIP dumping grounds
- do not trap mature projects in Studio forever; Studio incubates, projects eventually leave

---

## 7. Current weak spots still being sharpened

These areas are still in active clarification:
- Domain Playbooks
- later canonicalization of template families
- final deterministic metadata/link enforcement
- future board/filter/UI layer over the artifact system

---

## 8. Reading order for fast orientation

If you are new to the Studio repo, read in this order:
1. `README_Studio_Framework.md`
2. `Horizon_Studio.md`
3. `00_Artifacts/README_Artifacts.md`
4. `10_Artifact_System/10_Schema/Standard_ARYS.md`
5. `20_Templates/NOTE_Template_Families_Preservation.md`
6. the relevant workflow or quality file for the task at hand
