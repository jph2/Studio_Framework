---
arys_schema_version: "1.2"
id: "2676659c-8e69-4642-8dbf-b224e0319f84"
title: "STD_ARY — ARYS 1.2 Dual-Header Protocol"
type: STANDARD
status: active
trust_level: 3
created: "2026-03-21T18:31:01Z"
last_modified: "2026-03-21T18:31:01Z"
author: "TARS"
tags: [studio_framework, artifact_system, schema, arys, documentation_standards]
---

# STD_ARY — ARYS 1.2 Dual-Header Protocol

**Version**: 1.0.0 | **Date**: 21.03.2026 | **Time**: 19:31 | **GlobalID**: 20260321_1931_STD_ARY_v1

**Last Updated:** 21.03.2026 19:31  
**Framework:** Studio_Framework_Artifact_System  
**Status:** active

**Tag block:**
#studio_framework #artifact_system #schema #arys #documentation_standards

---

## Purpose

Defines the baseline ARYS 1.2 dual-header protocol for Studio Framework artifacts.

## Core rule

Every governed artifact should begin with:
1. machine-readable YAML frontmatter
2. a human-visible metadata header block immediately below it

This keeps artifacts readable in IDEs and still usable for indexing/retrieval.

## Required YAML fields

```yaml
---
arys_schema_version: "1.2"
id: "UUID-v4"
title: "Document Title"
type: STANDARD
status: active
trust_level: 3
created: "YYYY-MM-DDTHH:MM:SSZ"
last_modified: "YYYY-MM-DDTHH:MM:SSZ"
author: "TARS"
tags: [tag1, tag2]
---
```

## Required visible metadata block

```markdown
# [Document Title]

**Version**: [X.Y.Z] | **Date**: [DD.MM.YYYY] | **Time**: [HH:MM] | **GlobalID**: [YYYYMMDD_HHMM_PTR_vX]

**Last Updated:** [DD.MM.YYYY HH:MM]  
**Framework:** [Framework_Name]  
**Status:** [Status Label]

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

## Document type guidance

Recommended values:
- `README`
- `STANDARD`
- `TEMPLATE`
- `WORKFLOW`
- `REFERENCE`
- `CHECKLIST`
- `ARTIFACT`
