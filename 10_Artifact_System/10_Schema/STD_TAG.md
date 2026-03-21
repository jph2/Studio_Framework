---
arys_schema_version: "1.2"
id: "0d2db1c6-ac08-4b2f-afe2-925920908d54"
title: "STD_TAG — Tag System Starter Standard"
type: STANDARD
status: active
trust_level: 3
created: "2026-03-21T18:31:01Z"
last_modified: "2026-03-21T18:31:01Z"
author: "TARS"
provenance:
  git_repo: "Studio_Framework"
  git_branch: "main"
  git_commit_short: null
  git_commit_full: null
  git_path: "10_Artifact_System/10_Schema/STD_TAG.md"
tags: [studio_framework, artifact_system, schema, tags, retrieval]
---

# STD_TAG — Tag System Starter Standard

**Version**: 1.0.0 | **Date**: 21.03.2026 | **Time**: 19:31 | **GlobalID**: 20260321_1931_STD_TAG_v1

**Last Updated:** 21.03.2026 19:31  
**Framework:** Studio_Framework_Artifact_System  
**Status:** active

**Git:** Repo: Studio_Framework | Branch: main | Path: 10_Artifact_System/10_Schema/STD_TAG.md | Commit: pending


**Tag block:**
#studio_framework #artifact_system #schema #tags #retrieval

---

## Purpose

Defines the starter tag rules for Studio Framework.

## Core rule

Tags should help retrieval and classification.
They are not decorative noise.

## Format
- lowercase_with_underscores
- one tag block per document
- prefer canonical tags over ad hoc synonyms

## Minimum tagging guidance
Every governed artifact should usually include tags from at least these categories:
- artifact type
- domain or surface
- workflow/lifecycle stage

## Starter canonical tags

### Artifact tags
- `discovery`
- `research`
- `tutorial`
- `requirements`
- `specification`
- `implementation_plan`
- `checklist`
- `template`
- `workflow`
- `standard`

### System tags
- `studio_framework`
- `artifact_system`
- `quality_system`
- `tool_surfaces`
- `connectors`
- `project_bridges`
- `reference_archive`

### Surface tags
- `ide`
- `cad_dcc`
- `browser_terminal`
- `acp`
- `mcp`
- `openshell`

### Domain tags
- `software`
- `usd_dcc`
- `product_design`
- `marketing_content`

### Lifecycle tags
- `schema`
- `templates`
- `workflows`
- `validation`
- `incubation`
- `promotion`
- `archive`

## Quantity guidance
- short docs: 5–8 tags
- medium docs: 8–14 tags
- long/complex docs: 12–18 tags
- avoid tag spam

## Anti-patterns
- tags as prose
- person names as tags without reason
- giant topic phrases as tags
- duplicated synonyms when one canonical tag exists
