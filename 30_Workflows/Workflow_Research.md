---
arys_schema_version: "1.2"
id: "ff601d9b-3b70-47e3-8627-9f8df860ec34"
title: "Workflow_Research"
type: WORKFLOW
status: active
trust_level: 3
created: "2026-03-23T22:15:00Z"
last_modified: "2026-03-23T22:15:00Z"
author: "TARS"
provenance:
  git_repo: "Studio_Framework"
  git_branch: "main"
  git_commit_short: null
  git_commit_full: null
  git_path: "30_Workflows/Workflow_Research.md"
tags: [studio_framework, workflows, research, discovery, artifact_system]
---

# Workflow_Research

**Version**: 0.1.0 | **Date**: 23.03.2026 | **Time**: 23:15 | **GlobalID**: 20260323_2315_Workflow_Research_v0

**Last Updated:** 23.03.2026 23:15  
**Framework:** Studio_Framework_Workflows  
**Status:** beta

**Git:** Repo: Studio_Framework | Branch: main | Path: 30_Workflows/Workflow_Research.md | Commit: pending

**Tag block:**
#studio_framework #workflows #research #discovery #artifact_system

---

This workflow defines how Discovery and Research behave inside the Studio Framework.

## Purpose

Research in Studio is the first structured distillation of broad discovery work.
It is not yet a project and not yet automatically a tutorial, paper, or implementation plan.

## Base rule

The shared early work area is:
- `00_Artifacts/10_discovery-research/`

That folder may contain:
- Discovery only
- Discovery + Research pairs
- workstreams that never mature further
- workstreams that later branch into prep areas

## Workflow

### 1. Start as Discovery
A new topic begins as Discovery when:
- the problem is still broad or uncertain
- multiple directions need exploration
- the user wants a structured note before deciding the next move

### 2. Distill into Research
Move from Discovery to Research when:
- the topic has been explored enough to form a structured synthesis
- there is a meaningful first distillation, not just loose collection
- the user or workflow needs a clearer analytical frame

### 3. Preserve traceability
Research should always point back to its originating Discovery.
Discovery should indicate when a Research artifact exists.

### 4. Branch when maturity warrants it
Research may later branch into:
- `00_Artifacts/20_tutorial-prep/`
- `00_Artifacts/30_paper-prep/`
- `00_Artifacts/40_project-prep/`

Not every Research artifact must branch.
Some remain valuable as stable backlog or referenceable synthesis.

## Integrity rule

Discovery is a historical source artifact.
Do not casually delete it just because later artifacts exist.

## Naming rule

Use a shared workstream/topic stem plus suffixes, for example:
- `topic-name__DISCOVERY.md`
- `topic-name__RESEARCH.md`

## Human-in-the-loop rule

By default, promotion from Discovery to Research is human-in-the-loop unless a future workflow explicitly automates that decision.

## Related areas
- `20_Templates/10_Research/`
- `80_Project_Bridges/Bridge_Research_to_Project.md`
