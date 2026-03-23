---
arys_schema_version: "1.2"
id: "18ddc6e3-36ef-47ef-8d5f-03f2c08cae60"
title: "NOTE_Template_Families_Preservation"
type: NOTE
status: active
trust_level: 3
created: "2026-03-23T22:16:00Z"
last_modified: "2026-03-23T22:16:00Z"
author: "TARS"
provenance:
  git_repo: "Studio_Framework"
  git_branch: "main"
  git_commit_short: null
  git_commit_full: null
  git_path: "20_Templates/NOTE_Template_Families_Preservation.md"
tags: [studio_framework, templates, migration, preservation]
---

# NOTE_Template_Families_Preservation

**Version**: 0.1.0 | **Date**: 23.03.2026 | **Time**: 23:16 | **GlobalID**: 20260323_2316_NOTE_Template_Families_Preservation_v0

**Last Updated:** 23.03.2026 23:16  
**Framework:** Studio_Framework_Templates  
**Status:** beta

**Git:** Repo: Studio_Framework | Branch: main | Path: 20_Templates/NOTE_Template_Families_Preservation.md | Commit: pending

**Tag block:**
#studio_framework #templates #migration #preservation

---

All imported template families are intentionally being kept for now.

## Reason

The current priority is preservation-first migration.
The user explicitly does not want the existing good template sets reinvented or prematurely reduced before they are safely present inside the new Studio Framework.

## Current rule

For now:
- keep the imported Research templates
- keep the imported Tutorial templates
- keep the imported Scripts / Extensions / Apps templates
- do not aggressively prune variants, legacy copies, or alternate forms yet

## Later rule

A later hardening / canonicalization pass should:
- identify canonical templates
- identify variants
- identify archive-only legacy templates
- remove duplicate authority
- keep the strongest set while preserving provenance

## Important boundary

This note does not mean all current templates are final.
It means they are intentionally preserved first so cleanup can happen with lower risk later.
