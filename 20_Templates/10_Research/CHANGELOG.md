---
arys_schema_version: '1.2'
id: dce940f3-be46-4398-b03f-b9bcbac77ba1
title: CHANGELOG — `General_Research/030_Proj_TEMPLATES/`
type: STRATEGIC
status: active
trust_level: 2
visibility: internal
created: '2026-02-18T05:33:26Z'
last_modified: '2026-02-18T05:33:26Z'
---

# CHANGELOG — `General_Research/030_Proj_TEMPLATES/`

**Version**: N/A | **Date**: 13.01.2026 | **Time**: 00:20 | **GlobalID**: 20260113_0020_General_Research_AUTO

**Tag block:**
#workflow_optimization #best_practices #case_study #workflow_automation #deterministic_workflows #analysis #framework_integration #quality_assurance

## Scope & rules

- **Scope**: This changelog tracks changes to files under `General_Research/030_Proj_TEMPLATES/` only (including moves into `archive/`).
- **Out of scope**: Changes to framework tooling/rules outside this folder (e.g., `Master_Rules/`) must be logged elsewhere.
- **Entry requirements (mandatory)**:
  - **What changed** (including an explicit **Files touched** list)
  - **Why** (specific failure mode(s) / risk(s) addressed)
  - **How** (the concrete pattern/mechanism applied)

---

## 12.01.2026  — Template standardization: drift controls + evidence/link governance

**What changed**

- Standardized discovery-derived templates to reduce research drift and improve traceability:
  - Evidence matrices appear before Source Registry sections.
  - Source Registry uses deterministic `SRC-###` IDs for referencing in text and matrices.
  - Appendix X is used as a preserved “all-links captured” audit registry and kept as the **final appendix**.
- Made these elements mandatory across active templates:
  - **Tags (Keywords)** line tied to the master tag system (`Master_Rules/master_tag_system.yml`) and tag-sync workflow.
  - Short **copy/paste prompt snippet** near the top that points to a full prompt appendix.
  - A required **Deviation Log** section/appendix (allowing “N/A” when not discovery-derived).
- Archived the deviations comparison doc after capturing the key decisions in this changelog.

**Why**

- Prevent “research drift” when discovery framing/scope is incomplete or ignored.
- Prevent silent loss of early software-development architecture/spec/definition discoveries.
- Improve auditability: claims → evidence → sources, with stable source identifiers.
- Preserve source completeness by separating:
  - **Appendix X** (canonical capture / completeness)
  - **Source Registry** (working registry / usability)

**How**

- Applied consistent section ordering and wording patterns across templates:
  - **Evidence Matrix → Source Registry**
  - **SRC-IDs** (`SRC-001`, `SRC-002`, …) referenced by ID (not raw URLs)
  - **Appendix X** renamed/standardized and positioned as **last appendix** with a “redundant once Source Registry is complete” note
  - Added mandatory **Tags**, **Prompt snippet pattern**, and **Deviation Log** blocks

**Files touched**

- `Documentation_HowTo_template.md`
- `Documentation_WhatWeDid_template.md`
- `External_Decision_Support_template.md`
- `External_Implementation_Planning_template.md`
- `External_Requirements_Engineering_template.md`
- `External_Research_Analysis_template.md`
- `External_Strategic_Guidance_template.md`
- `Internal_Decision_Support_template.md`
- `Internal_Implementation_Planning_template.md`
- `Internal_Requirements_Engineering_template.md`
- `Internal_Research_Analysis_template.md`
- `Internal_Strategic_Guidance_template.md`
- `Research_3D_ConversionPipeline_Evaluation_template.md`
- `Research_Strategic_Findings_light_template.md`
- `Internal_Research_Analysis_template__deviations.md` → moved to `archive/` (see next entry)

---

## 12.01.2026 — Archive: `Internal_Research_Analysis_template__deviations.md`

**What changed**

- Moved `Internal_Research_Analysis_template__deviations.md` into `archive/` to keep a single active change log.

**Why**

- Reduce “meta-doc sprawl” by keeping **one** authoritative place for template change history.

**How**

- Archived the deviations document with a small “ARCHIVED” header; original content preserved below. Going forward, use this `CHANGELOG.md` for template-change tracking.

**Files touched**

- `Internal_Research_Analysis_template__deviations.md` (moved to `archive/Internal_Research_Analysis_template__deviations.md`)

