---
arys_schema_version: "1.2"
id: "2676659c-8e69-4642-8dbf-b224e0319f84"
title: "Standard_ARYS — ARYS 1.2 Dual-Header Protocol"
type: STANDARD
status: active
trust_level: 3
created: "2026-03-21T18:31:01Z"
last_modified: "2026-03-23T21:35:00Z"
author: "TARS"
provenance:
  git_repo: "Studio_Framework"
  git_branch: "main"
  git_commit_short: null
  git_commit_full: null
  git_path: "10_Artifact_System/10_Schema/Standard_ARYS.md"
tags: [studio_framework, artifact_system, schema, arys, documentation_standards]
---

# Standard_ARYS — ARYS 1.2 Dual-Header Protocol

**Version**: 0.2.0 | **Date**: 23.03.2026 | **Time**: 22:35 | **GlobalID**: 20260323_2235_Standard_ARYS_v0

**Last Updated:** 23.03.2026 22:35  
**Framework:** Studio_Framework_Artifact_System  
**Status:** beta

**Git:** Repo: Studio_Framework | Branch: main | Path: 10_Artifact_System/10_Schema/Standard_ARYS.md | Commit: pending

**Tag block:**
#studio_framework #artifact_system #schema #arys #documentation_standards

---

## Purpose

Defines the baseline ARYS 1.2 dual-header protocol for Studio Framework artifacts.

This standard adopts the ARYS 1.2 canonical logic from the legacy framework as the primary source, with only small Studio-specific adjustments.

## Core rule

Every governed artifact should begin with:
1. machine-readable YAML frontmatter
2. a human-visible metadata header block immediately below it

This keeps artifacts readable for humans in IDEs and editors while still supporting indexing, filtering, validation, and later automation.

## Header specification (the contract)

All framework-compliant Markdown files should contain a YAML frontmatter block following this schema.

### Required YAML fields

| Field | Type | Constraint | Description |
| :--- | :--- | :--- | :--- |
| `arys_schema_version` | String | Must be `"1.2"` | Identifies the contract version. |
| `id` | String | Strict UUID v4 | Persistent machine-indexable identifier. |
| `kanban_id` | String / null | Reserved | Reserved for later board/stage integration. May remain `null` until defined. |
| `title` | String | Max 120 chars | Human-readable title. |
| `type` | String | Enum-like | Artifact/document class. |
| `status` | String | Enum-like | Current lifecycle state. |
| `trust_level` | Integer | 1, 2, or 3 | Confidence weighting for retrieval and filtering. |
| `visibility` | String | internal, external, secret | Access control gate when relevant. |
| `created` | ISO-8601 | YYYY-MM-DDTHH:MM:SSZ | Original creation timestamp. |
| `last_modified` | ISO-8601 | YYYY-MM-DDTHH:MM:SSZ | Last significant change. |
| `author` | String | Free text | Human/agent author origin. |
| `provenance` | Object | Structured | Git/repo/path traceability. |
| `tags` | List[String] | Canonical tags | Tags from the master tag system. |

### Example YAML header

```yaml
---
arys_schema_version: "1.2"
id: "550e8400-e29b-41d4-a716-446655440000"
kanban_id: null
title: "Example Specification Document"
type: TECHNICAL
status: active
trust_level: 3
visibility: internal
created: "2026-03-14T12:00:00Z"
last_modified: "2026-03-14T12:00:00Z"
author: "TARS"
provenance:
  git_repo: "Studio_Framework"
  git_branch: "main"
  git_commit_short: null
  git_commit_full: null
  git_path: "relative/path.md"
tags: [example, spec]
---
```

`kanban_id` is reserved for later board/stage integration and may remain `null` until the board model is defined.

## Trust level mapping

The numeric `trust_level` allows later filtering based on reliability.

- **3** — framework governance, canonical rules, technical specs, mandatory policies
- **2** — verified research, domain-specific knowledge, validated workflows
- **1** — external or lossy material, raw notes, initial experiments, weakly validated input

## Provenance rule

Git provenance belongs in ARYS as traceability, not as artifact identity.

Meaning:
- ARYS identity stays stable across versions of the same artifact
- Git provenance records where that artifact lives in version control
- `git_commit_*` may be `null` or `pending` during drafting
- the path should still be filled because it is useful even before a clean commit snapshot exists

## Global rules

1. **Strict ID policy** — all governed documents should have a UUID in the `id` field.
2. **File-is-canonical** — the Markdown file remains the source of truth.
3. **ISO-8601 timestamps** — machine-readable dates should use UTC timestamps.
4. **Canonical tags only** — tags should come from the master tag system, not improvised local variants.
5. **One visible tag block** — keep one visible human-readable tag block near the top.
6. **Dual-header discipline** — machine-readable YAML plus human-readable summary block should stay aligned.

## Required visible metadata block

```markdown
# [Document Title]

**Version**: [X.Y.Z] | **Date**: [DD.MM.YYYY] | **Time**: [HH:MM] | **GlobalID**: [YYYYMMDD_HHMM_PTR_vX]

**Last Updated:** [DD.MM.YYYY HH:MM]  
**Framework:** [Framework_Name]  
**Status:** [Status Label]

**Git:** Repo: Studio_Framework | Branch: main | Path: relative/path.md | Commit: pending

**Tag block:**
#tag1 #tag2 #tag3

---
```

## Header freshness rule

On every substantive edit:
- increment version when appropriate
- update `last_modified`
- update visible date/time fields
- maintain coherent status values
- keep tags aligned with actual content

## Status guidance

Recommended values:
- `active`
- `draft`
- `deferred`
- `archived`
- `wip`
- `deprecated`

## Document type guidance

Recommended values include:
- `README`
- `STANDARD`
- `TEMPLATE`
- `WORKFLOW`
- `REFERENCE`
- `CHECKLIST`
- `ARTIFACT`
- `TECHNICAL`
- `STRATEGIC`
- `PRACTICAL`
- `GOVERNANCE`
- `MEMORY`

## Studio-specific note

Within the Studio Framework:
- `00_Artifacts` holds the real live work documents
- `10` through `90` define how those artifacts are structured, templated, reviewed, routed, matured, bridged, and archived

ARYS applies to both humans and agents.
It exists to reduce drift, improve traceability, and support deterministic validation later.
