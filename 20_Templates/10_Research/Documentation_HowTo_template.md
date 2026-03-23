---
arys_schema_version: '1.2'
id: 80c66882-330d-4d39-bef7-7ece8da1e9d9
title: Documentation HowTo template
type: STRATEGIC
status: active
trust_level: 2
visibility: internal
created: '2026-02-18T17:03:31Z'
last_modified: '2026-02-18T17:03:31Z'
---

﻿# [Documentation Title]

**Version**: 0.0.0 | **Date**: 16.02.2026 | **Time**: 00:31 | **GlobalID**: 20260113_0031_GeneralResearch_Documentation_HowTo_template
**Tag block:**
#framework_integration #best_practices #conversion #inside_omniverse #outside_omniverse #hybrid #standalone #omniverse #analysis #case_study #workflow_optimization

**Purpose**: [1 sentence describing the document's purpose]
**Context**: [1 sentence providing context or scope]

> **Status**: [Draft/Final] | **Date**: [DD.MM.YYYY] | **Environment**: [inside_omniverse/outside_omniverse/hybrid/standalone]

> **Author**: [Author Name] | [Website] | [LinkedIn/Contact]

> **Additional Authors**: [Additional contributors]

> **Audience**: [Target audience, e.g., "Developers, technical users, implementers"]

> [Brief, factual description of what this document covers]


---

## Link and Citation Policy (Inherited)

Use `.cursor/rules/documentation-standards.mdc` as the single source of truth for in-text citations (`[[N]](#link-N)`) and `## Links` entry format (`N. <a id="link-N"></a>[Title](URL) - ...`).
If links are used in this document, add a dedicated `## Links` section and follow the canonical format from that rule file.

---


## ðŸ§¾ Copy-paste prompt snippet (for a new agent)

Use this template as the target structure.  
If a `*_DISCOVERY.md` is attached, extract only the actionable how-to, **preserve useful links**, and move background material into an Appendix section.  
Return the final document as Markdown.
For the full generation contract, see **Appendix D â€” Full Prompt Snippet**.

---

## Overview

**Purpose**: [What this document is for]

**Audience**: [Who should use this]

**Prerequisites**: [What you need before starting]

**Last Updated**: [DD.MM.YYYY]

**Status**: [Current/Deprecated/Under Review]

---

## Problem Statement

**What**: [Clear description]

**Why**: [Why it matters]

**When**: [When it applies]

---

## Solution

### Approach

[Step-by-step approach]

### Requirements

- **Hardware**: [requirements]
- **Software**: [versions]
- **Access**: [permissions]

### Implementation Steps

1. [Step]
2. [Step]
3. [Step]

---

## Verification

- [ ] [How to test]
- [ ] [Success criteria]

---

## Links

1. <a id="link-1"></a>[Resource Title](URL) - [1-2 sentences explaining what this source contains and why it matters for this document].

---

## Appendix â€” Terminology & Key Concepts

This glossary defines key terms, acronyms, and concepts used throughout this document. Terms are organized by domain for easier navigation.

### [Domain/Category]

**Term**
- **Definition**: [Clear definition]
- **Context**: [How it's used in this document]
- **Related Terms**: [Links to related terms if applicable]

---

## Appendix B â€” Version History & Raw Notes

### v1.0.0 - [Current Date]
- Template modernization with enhanced header structure, master tag system integration, and updated discovery location references
- Added Purpose, Context, Status, Author, Audience fields
- Added Master Tag System Integration section
- Updated discovery location from `01_Research_DISCOVERY` to `02_Research_WIP`

### v0.2.0 - 24.12.2025
- Template version update and date synchronization with configuration rules.

### v0.1.0 - 13.12.2025
- Initial template.

---

## Appendix C â€” Tags

**ENVIRONMENT**: [inside_omniverse | outside_omniverse | hybrid | standalone]

[tag1] | [tag2] | [tag3] | [tag4] | [tag5]

---

## âš ï¸ Keyword System Status

**Current State**: We can use the Master Tag system (MasterTech system) to provide standardized taxonomy for cross-document discoverability. Master tag system integration is fully available.

**Master Tag System**: `ðŸ—ï¸ Master_Rules (Framework Foundation)/master_tag_system.yml`

**Tag Integration Guidelines**:
- Use master tag system for document tagging (see Appendix C â€” Tags section)
- Maintain local keyword index in appendix for document-specific terms
- Follow tag usage standards: min 4 tags, sweet spot 12-15, max 25, required categories, case sensitivity

**Local Keyword Management**: Continue using:
- Section-specific keywords for navigation and discoverability
- Document-specific keyword index in appendix
- Manual keyword curation per document based on content

**Cross-Document Discoverability**: Master Tag system provides standardized taxonomy enabling documentation to be discoverable across the entire framework through consistent tagging.

---

## Appendix F â€” Framework Integration & Traceability

### ðŸ¤– Agent Usage Instructions

**Template**: `Documentation_HowTo_template.md` (Standalone documentation category)
**Audience**: Developers, technical users, implementers
**Focus**: How-to guides, implementation instructions, practical documentation
**Length**: 150-200 lines (focused, practical documentation)

**Usage Context**: This template is used for how-to documentation and implementation guides, not research synthesis. It provides practical, actionable instructions for technical users.

### ðŸ“‹ Template Traceability

**REQUIRED**: Every documentation document created from this template MUST include a "Template Traceability" section that clearly states:

- **Template Used**: `Documentation_HowTo_template.md`
- **Template Version**: v1.0.0
- **Template Profile**: `documentation`
- **Template Location**: `ðŸ”¬ General_Research (Research Library)/030_Proj_TEMPLATES/Documentation_HowTo_template.md`

This ensures traceability and helps maintain consistency across documentation documents.

### ðŸ”— Framework Integration Notes

**Standalone Category**: This template represents one of the two standalone documentation categories in the consolidated template system. It focuses on practical how-to guidance rather than research synthesis.

**Non-Research Documentation**: Unlike research templates, this template does not follow the discovery-to-research workflow but can incorporate research findings into practical implementation guides.

---

## Appendix D â€” Full Prompt Snippet (Contract)

Use `Documentation_HowTo_template.md` as the target structure.
If a `*_DISCOVERY.md` is attached, extract only the actionable how-to, preserve useful links, and move background material into an Appendix section.
Return the final document as Markdown.

---

## Appendix Y â€” Deviation Log (Required)

If this document is derived from discovery or another source document:
- Log any changes vs source that affect **steps**, **commands**, **parameters**, **links**, or **scope**.
- If no deviations exist, state: â€œNo deviations from source.â€

If this document is not derived from another source:
- State: â€œN/A (not derived from discovery/source).â€

| Item | Source | Document | Status (âœ…/âš ï¸) | Justification |
|------|--------|----------|----------------|---------------|
| [What changed] | [Source value] | [Doc value] | [âœ…/âš ï¸] | [Why] |
