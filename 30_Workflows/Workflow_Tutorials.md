---
arys_schema_version: "1.2"
id: "940973f8-adb8-4137-9cc2-994fa2507e6b"
title: "Workflow_Tutorials"
type: WORKFLOW
status: active
trust_level: 3
created: "2026-03-23T22:17:00Z"
last_modified: "2026-03-23T22:17:00Z"
author: "TARS"
provenance:
  git_repo: "Studio_Framework"
  git_branch: "main"
  git_commit_short: null
  git_commit_full: null
  git_path: "30_Workflows/Workflow_Tutorials.md"
tags: [studio_framework, workflows, tutorials, learning, artifact_system]
---

# Workflow_Tutorials

**Version**: 0.1.0 | **Date**: 23.03.2026 | **Time**: 23:17 | **GlobalID**: 20260323_2317_Workflow_Tutorials_v0

**Last Updated:** 23.03.2026 23:17  
**Framework:** Studio_Framework_Workflows  
**Status:** beta

**Git:** Repo: Studio_Framework | Branch: main | Path: 30_Workflows/Workflow_Tutorials.md | Commit: pending

**Tag block:**
#studio_framework #workflows #tutorials #learning #artifact_system

---

This workflow defines how work moves into Tutorial Prep inside the Studio Framework.

## Purpose

Tutorials are one of the main downstream directions from Discovery and Research.
They turn understanding into teachable structure.

## Entry rule

Work should move into:
- `00_Artifacts/20_tutorial-prep/`

when a Discovery/Research thread is being shaped into:
- a how-to
- a structured guided learning path
- a troubleshooting guide
- an integration walkthrough
- a best-practices or deep-dive tutorial output

## Workflow

### 1. Start from Discovery/Research
Tutorial Prep should normally be downstream of:
- `topic-name__DISCOVERY.md`
- `topic-name__RESEARCH.md`

### 2. Define the teaching objective
Before writing the tutorial, clarify:
- what the learner should understand or build
- who the learner is
- what prior knowledge is assumed
- what counts as success

### 3. Shape the tutorial structure
Then move into a suitable tutorial form such as:
- foundation
- how-to
- integration
- troubleshooting
- best-practices
- deep dive

### 4. Maintain traceability
Tutorial Prep artifacts should link back to the originating Discovery and Research.

## Human-in-the-loop rule

By default, the decision to move a workstream into Tutorial Prep is human-in-the-loop unless a future workflow explicitly automates it.

## Related areas
- `20_Templates/20_Tutorials/`
- `40_Quality_System/Quality_Tutorials.md`
