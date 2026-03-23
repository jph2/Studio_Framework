---
arys_schema_version: "1.2"
id: "fbe4f145-9a9c-43a2-bf0c-42ddf4898b96"
title: "README_ART — 00_Artifacts"
type: README
status: active
trust_level: 3
created: "2026-03-23T17:10:00Z"
last_modified: "2026-03-23T17:10:00Z"
author: "TARS"
provenance:
  git_repo: "Studio_Framework"
  git_branch: "main"
  git_commit_short: null
  git_commit_full: null
  git_path: "00_Artifacts/README_ART.md"
tags: [studio_framework, artifacts]
---

# README_ART — 00_Artifacts

**Version**: 0.1.0 | **Date**: 23.03.2026 | **Time**: 18:10 | **GlobalID**: 20260323_1810_README_ART_v0

**Last Updated:** 23.03.2026 18:10  
**Framework:** Studio_Framework_Artifacts  
**Status:** beta

**Git:** Repo: Studio_Framework | Branch: main | Path: 00_Artifacts/README_ART.md | Commit: pending

**Tag block:**
#studio_framework #artifacts

---

00_Artifacts is the live storage area for the actual working documents of the Studio Framework.

## Purpose

This folder holds the real evolving artifacts such as:
- Discovery
- Research
- Tutorial preparation
- Paper preparation
- Project preparation
- Admin / Ops artifacts
- Social / Content artifacts

## Important boundary

`00_Artifacts` contains the live work products.

The folders `10` through `90` do **not** hold the primary live artifacts.
They define how artifacts are created, structured, reviewed, routed, matured, and archived.

That means:
- `00_Artifacts` = actual documents
- `10–90` = governing / structural / workflow / quality / bridge layers

## Current structure

- `discovery-research/`
- `tutorial-prep/`
- `paper-prep/`
- `project-prep/`
- `admin-ops/`
- `social-content/`

## Working model

The default early workstream starts in:
- `discovery-research/`

Later, work may branch into:
- `tutorial-prep/`
- `paper-prep/`
- `project-prep/`

`admin-ops/` and `social-content/` may use deeper substructure when needed.

## Naming rule

Use a stable topic/workstream stem plus artifact suffixes, for example:
- `topic-name__DISCOVERY.md`
- `topic-name__RESEARCH.md`
- `topic-name__REQUIREMENTS.md`
- `topic-name__SPEC.md`
- `topic-name__IMPLEMENTATION-PLAN.md`
- `topic-name__TUTORIAL.md`

## Linking rule

- Discovery should point to downstream artifacts when they exist.
- Research should point back to Discovery and forward to prep artifacts when they exist.
- Prep artifacts should point back to their Discovery and Research origins.
