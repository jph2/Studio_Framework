---
arys_schema_version: "1.2"
id: "7acf2281-d463-4206-8f35-74657e1cc248"
title: "STD_DOC — Documentation Standards"
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
  git_path: "40_Quality_System/STD_DOC.md"
tags: [studio_framework, quality_system, documentation_standards, artifact_quality]
---

# STD_DOC — Documentation Standards

**Version**: 1.0.0 | **Date**: 21.03.2026 | **Time**: 19:31 | **GlobalID**: 20260321_1931_STD_DOC_v1

**Last Updated:** 21.03.2026 19:31  
**Framework:** Studio_Framework_Quality_System  
**Status:** active

**Git:** Repo: Studio_Framework | Branch: main | Path: 40_Quality_System/STD_DOC.md | Commit: pending


**Tag block:**
#studio_framework #quality_system #documentation_standards #artifact_quality

---

## Purpose

Defines the baseline documentation standards for Studio Framework artifacts.

## Core rule

Documentation should be:
- structured
- scannable
- explicit about status and intent
- readable by humans in IDEs
- retrievable by agents later

## Required qualities

### Clarity
- title says what the artifact is
- sections have concrete names
- avoid vague prose when a rule/list/decision is better

### Traceability
- artifacts should point back to upstream material when relevant
- decisions should not appear without context
- implementation work should not float free of its requirements/spec/plan context

### Version and status awareness
- status must be visible
- edits should refresh header metadata
- when a document changes meaningfully, the visible metadata should reflect that

### Separation of artifact types
Do not collapse these into one muddy document when they serve different functions:
- Discovery
- Research
- Tutorial
- Requirements
- Specification
- Implementation Plan

## Link and placeholder hygiene

Before treating a document as stable:
- remove placeholder tokens
- check links/paths where relevant
- make sure examples are not silently fake or stale

## Anti-patterns

- giant undifferentiated markdown blobs
- missing status/version/header metadata
- project-specific truth pretending to be universal law
- old template bureaucracy for its own sake
- headers that exist only in theory and are not actually applied
