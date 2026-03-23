---
arys_schema_version: '1.2'
id: bd261e70-a134-4061-b9ee-7339acda02bd
title: Video Deep-Dive Tutorial Templates
type: PRACTICAL
status: active
trust_level: 2
visibility: internal
created: '2026-03-03T09:30:33Z'
last_modified: '2026-03-03T09:30:33Z'
---

# Video Deep-Dive Tutorial Templates

Canonical home for reusable OpenUSD video deep-dive authoring templates.

## Scope

These templates are used to generate:

- `__VIDEO_DEEP_DIVE_TUTORIAL.md` learning documents
- transcript-aligned chapter breakdowns
- key-moment screenshot maps
- beginner-safe code breakouts

## Files

- `VIDEO_DEEP_DIVE_TUTORIAL_TEMPLATE.md`
  - Main markdown skeleton
  - Includes narrative flow, chapter bridges, links section, appendices
- `VIDEO_DEEP_DIVE_TUTORIAL_PROMPT_PACK.md`
  - Trigger prompt
  - Master generation prompt
  - QA prompt
- `VIDEO_DEEP_DIVE_TUTORIAL_SKILL.md`
  - Execution skill workflow (transcript, capture, mapping, QA)
  - **Mandatory breakout audit:** every image with code must have a breakout; skill includes audit step
  - Keeps template docs lean and focused on output format

## Relationship to USD_GoodStart

Working tutorial instances can remain in `USD_GoodStart/WIP_Docs`.
Template maintenance lives here in `General_Tutorials`.
