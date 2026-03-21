---
arys_schema_version: "1.2"
id: "a9bb73c3-1bbf-45b2-8064-818fb0415fea"
title: "README_STF — Studio Framework"
type: README
status: active
trust_level: 3
created: "2026-03-21T17:44:00Z"
last_modified: "2026-03-21T18:26:48Z"
author: "TARS"
tags: [studio_framework]
---

# README_STF — Studio Framework

**Version**: 1.0.0 | **Date**: 21.03.2026 | **Time**: 19:26 | **GlobalID**: 20260321_1926_README_STF_v1

**Last Updated:** 21.03.2026 19:26  
**Framework:** Studio_Framework  
**Status:** active

**Tag block:**
#studio_framework

---
Studio Framework is the rebuilt artifact/workflow layer that sits **beside** OpenClaw, not inside it.

## Pointer legend

Each directory-level README in this framework uses a three-letter pointer so the file identity is obvious even when seen out of context.

Examples:
- `README_STF` = Studio Framework
- `README_TSR` = Tool Surfaces
- `README_CNT` = Connectors
- `README_DPL` = Domain Playbooks
- `README_QLT` = Quality System

## Role

- OpenClaw = governing layer
- Studio Framework = artifact quality + workflow framework
- Project repos = implementation truth

## Purpose

This framework is broader than classic software development.
It exists to support building across:
- code
- documentation
- research
- tutorials
- requirements/specs/plans
- product design
- CAD / DCC / USD work
- marketing/content work

## Core rule

OpenClaw governs.
Studio Framework defines how high-quality artifacts are produced across different tools and surfaces.

## Structural model

### A. OpenClaw governance layer
Owns:
- soul / behavior / routing
- memory access policy
- automation control
- agent orchestration
- consistency across tools and machines

### B. Studio Framework layer
Owns:
- artifact schema
- templates
- documentation rules
- workflow definitions
- quality standards for producing artifacts across tools and surfaces

### C. Domain layer
Owns:
- domain-specific operating law
- validation/checklist logic
- reusable reasoning patterns for domains such as software, USD/DCC, product design, or marketing/content

### D. Tool / work surfaces
Owns the actual hands-on environments where work happens.
Examples:
- IDEs
- CAD tools
- DCC tools
- Omniverse
- browser/terminal surfaces
- future tools not yet known

### E. Project spaces
Owns:
- project truth
- implementation history
- concrete outputs
- code/assets/docs that clearly belong to a project lifecycle

## Connector note

ACP and MCP are **not** work surfaces.
They are connector/control layers.

- **ACP** = coding/session control layer for agentic coding work
- **MCP** = capability bridge into tools and services

OpenClaw governs above them.
The tools remain the surfaces.
Repos remain project truth.

## Documentation standards

Studio Framework uses explicit artifact metadata and heading standards so outputs remain searchable, readable, and structurally consistent across tools.

### ARYS 1.2 — Dual-Header Protocol

All framework documents should follow the **Dual-Header Protocol**:

1. a **machine-readable YAML block** for ingestion and retrieval
2. a **human-visible metadata block** immediately below it for readability in tools/IDEs that hide frontmatter

### 1. Machine-readable YAML block
Must be the first lines of the file, between `---` delimiters.

Required core fields:

```yaml
---
arys_schema_version: "1.2"
id: "UUID-v4"
title: "Document Title"
type: STRATEGIC
status: active
trust_level: 3
created: "YYYY-MM-DDTHH:MM:SSZ"
last_modified: "YYYY-MM-DDTHH:MM:SSZ"
author: "TARS"
tags: [tag1, tag2]
---
```

### 2. Human-visible header block
Must appear immediately below the YAML block.

```markdown
# [Document Title]

**Version**: [X.Y.Z] | **Date**: [DD.MM.YYYY] | **Time**: [HH:MM] | **GlobalID**: [YYYYMMDD_HHMM_SPS_Name_vX]

**Last Updated:** [DD.MM.YYYY HH:MM]  
**Framework:** [Domain_Name]  
**Status:** [Status Label]

**Tag block:**
#tag1 #tag2 #tag3

---
```

### Header freshness rule
On every substantive edit:
- increment the version
- update `last_modified`
- update visible date/time fields
- add/update short history/change notes where appropriate

## Naming standard

Use explicit pointer-based names rather than ambiguous generic names.

Examples:
- `README_STF.md`
- `README_TSR.md`
- `README_CNT.md`
- `Readme_TUT.md`

The point is simple:
- file identity should still be obvious when the file is seen out of context
- both human memory and agent retrieval benefit from explicit naming

## Immediate implication

Studio Framework is not just a folder tree.
It is the quality/workflow layer for producing structured artifacts that remain understandable, editable, and retrievable later across changing tools and domains.
