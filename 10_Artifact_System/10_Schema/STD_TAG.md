---
arys_schema_version: "1.2"
id: "0d2db1c6-ac08-4b2f-afe2-925920908d54"
title: "STD_TAG — Tag System Operating Note"
type: STANDARD
status: active
trust_level: 3
created: "2026-03-21T18:31:01Z"
last_modified: "2026-03-23T21:42:00Z"
author: "TARS"
provenance:
  git_repo: "Studio_Framework"
  git_branch: "main"
  git_commit_short: null
  git_commit_full: null
  git_path: "10_Artifact_System/10_Schema/STD_TAG.md"
tags: [studio_framework, artifact_system, schema, tags, retrieval]
---

# STD_TAG — Tag System Operating Note

**Version**: 0.2.0 | **Date**: 23.03.2026 | **Time**: 22:42 | **GlobalID**: 20260323_2242_STD_TAG_v0

**Last Updated:** 23.03.2026 22:42  
**Framework:** Studio_Framework_Artifact_System  
**Status:** beta

**Git:** Repo: Studio_Framework | Branch: main | Path: 10_Artifact_System/10_Schema/STD_TAG.md | Commit: pending

**Tag block:**
#studio_framework #artifact_system #schema #tags #retrieval

---

## Purpose

This file explains how the Studio Framework should use the canonical tag system.

## Canonical sources

The canonical tag system now lives in:
- `master_tag_system.yml`
- `TAG_SEMANTIC_INDEX.md`

These two files should be treated as the primary source of truth for:
- tag inventory
- tag categories
- semantic meaning
- canonical naming
- topic-to-tag interpretation

## Core rule

When tagging a new document:
1. compare the document content against the existing canonical tags first
2. use existing tags wherever they already cover the meaning
3. only add a new tag when the content is genuinely not covered yet
4. when adding a new tag, update the semantic documentation as well

## Format rule

- use lowercase_with_underscores
- keep one visible tag block near the top
- use canonical tags, not ad hoc synonyms
- prefer deterministic validation over inference-only tag assignment

## Studio note

Within the Studio Framework, tags are expected to support:
- retrieval
- filtering
- future board/search views
- deterministic validation tooling
- cross-artifact traceability

This file is now an operating note, not a competing miniature tag standard.
