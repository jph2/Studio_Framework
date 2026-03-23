---
arys_schema_version: '1.2'
id: 2edef726-ff3d-4950-a05b-1ffcc479842c
title: '[Finding Title]'
type: STRATEGIC
status: active
trust_level: 2
visibility: internal
created: '2026-02-18T05:33:26Z'
last_modified: '2026-02-18T05:33:26Z'
---

# [Finding Title]

**Version**: 0.0.0 | **Date**: 13.01.2026 | **Time**: 00:31 | **GlobalID**: 20260113_0031_GeneralResearch_Research_finding_template

**Purpose**: [1 sentence describing the document's purpose]
**Context**: [1 sentence providing context or scope]

#workflow_optimization #best_practices #case_study

> **Status**: [Draft/Final] | **Date**: [DD.MM.YYYY] | **Environment**: [inside_omniverse/outside_omniverse/hybrid/standalone]

> **Author**: [Author Name] | [Website] | [LinkedIn/Contact]

> **Additional Authors**: [Additional contributors]

> **Audience**: [Target audience, e.g., "Technical team, decision makers"]

> **Research Overview**: A single, actionable finding with evidence and next actions.

**Event ID:** EVT-YYYYMMDD-HHMM-[Component]-[SeqNum]  
**Origin Event:** [EVT-ID if evolved from discovery or another event]  
**Related Events:** [List Event IDs showing lifecycle/evolution]  
**Tags:** [Auto-generated based on content]
  - environment: [tag1, tag2]
  - functionality: [tag3, tag4]
  - use_case: [tag5]
  - research_type: [tag6]
  - complexity: [tag7]
  - [other relevant categories from master_tag_system.yml]

## 🤖 Agent Note (Discovery → Research workflow)

- **Discovery location**: `research/02_Research_WIP/`
- **Discovery naming**: filenames may contain `_DISCOVERY` **or** `__DISCOVERY` (both accepted)
- **Research naming**: Research filename MUST be derived from discovery filename by replacing `_DISCOVERY` or `__DISCOVERY` with `_RESEARCH` (e.g., `Blender_USD_FAKE_References_DISCOVERY.md` → `Blender_USD_FAKE_References_RESEARCH.md`)
- **Promotion script**: `scripts/generate_research_from_discovery.py` generates a `_RESEARCH` placeholder into `research/02_Research_WIP/`
- **Research structure rules (ruling contract)**: `Research_Definition/research_configuration_rules.yml`

## 📝 Template User Note (variant)

- **Ruling contract**: `Research_Definition/research_configuration_rules.yml`
- **This is a research variant** (YAML profile: `finding`).
- Use it when you want *one* lesson/decision captured cleanly.

## 📋 Template Traceability

**REQUIRED**: Every research document created from this template MUST include a "Template Traceability" section (typically in the document metadata or after the Template User Note) that clearly states:

- **Template Used**: `Research_finding_template.md`
- **Template Version**: [Version when document was created]
- **Template Profile**: `finding`
- **Template Location**: `🔬 General_Research (Research Library)/030_Proj_TEMPLATES/Research_finding_template.md`

This ensures traceability and helps maintain consistency across research documents.

## 🧾 Copy-paste prompt snippet (for a new agent)

Use `Research_Definition/research_configuration_rules.yml` as the ruling contract.  
Use this template (single finding) as the target structure.  
Extract one clear finding from the attached `*_DISCOVERY.md`, **preserving ALL links** (critical requirement), and complete Source Registry/Evidence Matrix.  
**Link Validation**: After completing the research, extract all URLs/links from the discovery file and verify every single link appears in either:
- Source Registry (Appendix A) for documentation/API references
- Additional Resources section (Appendix A) for community/tutorial links
- Documented in Appendix D if excluded (with justification)
**Important**: Missing links violate framework rules. Complete link validation checklist in Appendix D before finalizing. After completing the research, review the discovery file and add all aspects that were NOT included to **Appendix D — Discovery Content Not Included** to prevent information loss.  
Return the final document as Markdown.

---

<a id="tldr"></a>
## Too Long; Didn't Read (TLDR)

- **Finding**: [1 sentence]
- **Impact**: [1–3 bullets]
- **Action**: [what to do next]

---

## 🎯 What Was Found

- **Finding statement**: [clear description]
- **Context**: [where/when it applies]

---

## 🔍 Technical Details

- **Problem/Opportunity**: [details]
- **Approach/Solution**: [what worked]

---

## 📊 Evidence

### Source Registry

| ID | Source (Title+URL) | Type | Version/Date | Relevance | Quality (A/B/C/D) | Notes |
|---|---|---|---|---|---|---|
| S1 | [Title](URL) | [vendor/standards/academic/community/internal] | [date] | [H/M/L] | [A/B/C/D] | |

### Evidence Matrix

| Claim/Finding | Source IDs | Source Quality | Confidence (high/medium/low) | Evidence Notes |
|---|---|---|---|---|
| [claim] | S1 | [A/B/C/D] | [high/medium/low] | |

---

## 🛠️ Action Items

- [ ] [Action] — [owner] — [due]

---

## 🔗 Related Information

- Related docs: [links]

---

## Appendix — Terminology & Key Concepts

This glossary defines key terms, acronyms, and concepts used throughout this document. Terms are organized by domain for easier navigation.

### [Domain/Category]

**Term**
- **Definition**: [Clear definition]
- **Context**: [How it's used in this document]
- **Related Terms**: [Links to related terms if applicable]

---

## Appendix B — Version History & Raw Notes

### v1.0.0 - [Current Date]
- Template modernization with enhanced header structure, master tag system integration, and updated discovery location references
- Added Purpose, Context, Status, Author, Audience fields
- Added Master Tag System Integration section
- Added Discovery Paper Reference & Template Derivation section
- Updated discovery location from `01_Research_DISCOVERY` to `02_Research_WIP`

### v0.2.0 - 24.12.2025
- Template version update and date synchronization with configuration rules.

### v0.1.0 - 13.12.2025
- Initial finding.

---

## Appendix C — Tags

**ENVIRONMENT**: [inside_omniverse | outside_omniverse | hybrid | standalone]

best_practice | troubleshooting | ...

---

## Appendix D — Discovery Content Not Included

> **Purpose**: This appendix captures all aspects from the discovery file that were **not included** in this research document at the time of creation. This prevents information loss during the discovery → research conversion process and allows future expansion or separate research documents.
> 
> **Note**: More details on these topics can be found in the discovery file. **It is recommended to provide a link to the corresponding discovery file** (e.g., `[Discovery File Name](path/to/discovery_file.md)` or `[Discovery File Name](../02_Research_WIP/discovery_file.md)`).

### Source Discovery File

- **Discovery File**: [Link to discovery file] — [Brief description of what the discovery file contains]
  - Example: `[ComfyUI_ComposableBindings_DISCOVERY.md](../02_Research_WIP/ComfyUI_ComposableBindings_DISCOVERY.md)` — Comprehensive discovery document covering ComfyUI ComposableBindings integration patterns

### Content from Discovery Not Yet Implemented

- [ ] [Aspect/topic from discovery file that was not included]
  - [Brief description or reason why it was excluded]
  - [Link to relevant section in discovery file if applicable]

- [ ] [Another aspect/topic from discovery file]
  - [Brief description]
  - [Link to relevant section in discovery file if applicable]

### Notes on Exclusion

- **Reason for exclusion**: [Why this content was not included - e.g., out of scope, requires separate research, low priority, etc.]
- **Future consideration**: [When/if this should be addressed in future research]
- **Related documents**: [Links to other research documents that might cover this content]

### Link Validation Checklist

**CRITICAL**: Verify all links from discovery file are included in this research document.

#### Link Extraction & Verification

**Discovery File Links Found**: [Count] total links
- Documentation/API links: [Count]
- Community/Tutorial links: [Count]
- Other links: [Count]

**Research Document Links Included**: [Count] total links
- In Source Registry: [Count]
- In Additional Resources: [Count]
- Documented as excluded in Notes on Exclusion: [Count]

#### Validation Status

- [ ] All documentation/API links from discovery are in Source Registry
- [ ] All community/tutorial links from discovery are in Additional Resources
- [ ] Any excluded links are documented in "Notes on Exclusion" with justification
- [ ] Link count matches: Discovery links = Research links (or excluded links documented)

**Validation Result**: [✅ PASS / ❌ FAIL - Missing Links: [list]]

**Missing Links** (if any):
- [Link URL] — [Reason for exclusion / Action needed]

---

## ⚠️ Keyword System Status

**Current State**: We can use the Master Tag system (MasterTech system) to provide standardized taxonomy for cross-document discoverability. Master tag system integration is fully available.

**Master Tag System**: `🏗️ Master_Rules (Framework Foundation)/master_tag_system.yml`

**Tag Integration Guidelines**:
- Use master tag system for document tagging (see Appendix C — Tags section)
- Maintain local keyword index in appendix for document-specific terms
- Follow tag usage standards: max 12 tags, required categories, case sensitivity

**Local Keyword Management**: Continue using:
- Section-specific keywords for navigation and discoverability
- Document-specific keyword index in appendix
- Manual keyword curation per document based on content

**Cross-Document Discoverability**: Master Tag system provides standardized taxonomy enabling research documents to be discoverable across the entire framework through consistent tagging.

## 🔗 Discovery Paper Reference & Template Derivation

**Source Document**: `🔬 General_Research (Research Library)/070_Proj_RESEARCH/02_Research_WIP/[Discovery_File_Name]_DISCOVERY.md`

**Template Derivation Process**:
- **Base Template**: `MasterResearch_template.md` (master template)
- **Variant Template**: `Research_finding_template.md`
- **Purpose**: Single actionable finding variant for focused research outputs

**Sections Structure**:
- Header with metadata (Purpose, Context, Status, Author, Audience)
- Template traceability
- TLDR section
- Finding statement
- Technical details
- Evidence (Source Registry, Evidence Matrix)
- Action items
- Related information
- Appendices (Terminology, Version History, Tags, Discovery Content Not Included)

**Design Rationale**:
- **Focused scope**: Designed for single, actionable findings rather than comprehensive research
- **Quick read**: TLDR section for fast consumption
- **Evidence-backed**: Includes source registry and evidence matrix even for focused findings
- **Action-oriented**: Emphasizes action items and next steps
- **Discovery tracking**: Appendix D prevents information loss during conversion
- **Tag system integration**: Master tag system for cross-document discoverability

**Usage Context**: This template serves as a lightweight framework for documenting single findings, lessons learned, or focused research outputs that don't require comprehensive research document structure.
