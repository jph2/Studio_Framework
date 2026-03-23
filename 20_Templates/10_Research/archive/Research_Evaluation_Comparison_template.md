---
arys_schema_version: '1.2'
id: 81fff1c0-701a-4e46-9369-4355fc126838
title: '[Evaluation Title] — Research'
type: STRATEGIC
status: active
trust_level: 2
visibility: internal
created: '2026-02-18T05:33:26Z'
last_modified: '2026-02-18T05:33:26Z'
---

# [Evaluation Title] — Research

**Version**: 0.0.0 | **Date**: 13.01.2026 | **Time**: 00:31 | **GlobalID**: 20260113_0031_GeneralResearch_Research_Evaluation_Comparison_t

**Purpose**: [1 sentence describing the document's purpose]
**Context**: [1 sentence providing context or scope]

#workflow_optimization #best_practices #case_study

> **Status**: [Draft/Final] | **Date**: [DD.MM.YYYY] | **Environment**: [inside_omniverse/outside_omniverse/hybrid/standalone]

> **Author**: [Author Name] | [Website] | [LinkedIn/Contact]

> **Additional Authors**: [Additional contributors]

> **Audience**: [Target audience, e.g., "Technical evaluators, decision makers, implementation teams"]

> **Research Overview**: Evaluation and comparison of [technology/approach] for [use case]. Includes methodology, findings, comparisons, and implementation recommendations.

## 🤖 Agent Note (Discovery → Research workflow)

- **Discovery location**: `research/02_Research_WIP/`
- **Discovery naming**: filenames may contain `_DISCOVERY` **or** `__DISCOVERY` (both accepted)
- **Research naming**: Research filename MUST be derived from discovery filename by replacing `_DISCOVERY` or `__DISCOVERY` with `_RESEARCH` (e.g., `ComfyUI_AI_Support_DISCOVERY.md` → `ComfyUI_AI_Support_RESEARCH.md`)
- **Promotion script**: `scripts/generate_research_from_discovery.py` generates a `_RESEARCH` placeholder into `research/02_Research_WIP/`
- **Research structure rules (ruling contract)**: `Research_Definition/research_configuration_rules.yml`

## 📝 Template User Note

- **Ruling contract**: `Research_Definition/research_configuration_rules.yml`
- **This is a simplified evaluation/comparison research template** (YAML profile: `evaluation_comparison`).
- Use it when evaluating technologies, frameworks, or approaches with clear comparisons and implementation focus.
- Simpler than MasterResearch, more structured than Finding template.

## 📋 Template Traceability

**REQUIRED**: Every research document created from this template MUST include a "Template Traceability" section (typically in the document metadata or after the Template User Note) that clearly states:

- **Template Used**: `Research_Evaluation_Comparison_template.md`
- **Template Version**: [Version when document was created]
- **Template Profile**: `evaluation_comparison`
- **Template Location**: `🔬 General_Research (Research Library)/030_Proj_TEMPLATES/Research_Evaluation_Comparison_template.md`

This ensures traceability and helps maintain consistency across research documents.

## 🧾 Copy-paste prompt snippet (for a new agent)

Use `Research_Definition/research_configuration_rules.yml` as the ruling contract.  
Use this template (evaluation/comparison) as the target structure.  
Transform the attached `*_DISCOVERY.md` into a clean research document, **preserving ALL links** (critical requirement), organizing by: Overview → Methodology → Findings → Comparisons → Recommendations → Implementation → Evidence.  
**Link Validation**: After completing the research, extract all URLs/links from the discovery file and verify every single link appears in either:
- Source Registry (Appendix A) for documentation/API references
- Additional Resources section (Appendix A) for community/tutorial links
- Documented in Appendix D if excluded (with justification)
**Important**: Missing links violate framework rules. Complete link validation checklist in Appendix D before finalizing. After completing the research, review the discovery file and add all aspects that were NOT included to **Appendix D — Discovery Content Not Included** to prevent information loss.  
Return the final document as Markdown.

**Quick Navigation**: [Executive Summary](#executive-summary) | [Key Conclusions](#key-conclusions) | [Methodology](#goals--methodology) | [Comparisons](#comparisons) | [Recommendations](#recommendations) | [Implementation](#implementation-approach) | [Evidence](#appendix-a--evidence--references)

---

## Purpose & Audience

- **Purpose**: [1 sentence describing what this evaluation accomplishes]
- **Audience**: [roles: e.g., developers, architects, decision-makers]
- **Decision this document supports**: [e.g., adopt framework / choose approach / proceed with implementation]

---

## Executive Summary

[4–7 short paragraphs answering: what was evaluated, why it matters, what works, what doesn't, what we recommend, and what the next steps are. Keep narrative style, no action list here.]

---

## Key Conclusions

- [3–7 bullets in plain language: what works, what doesn't/assumptions, what we recommend]

---

## Problem Framing & Scope

[1–3 short paragraphs: what question we're answering, what's in/out of scope, what "good" looks like for stakeholders.]

---

## Goals & Methodology

### Primary research questions

1. [Question 1: e.g., "Is ComfyUI suitable for AI-assisted Composable Bindings?"]
2. [Question 2: e.g., "How does ComfyUI compare to alternative frameworks?"]
3. [Question 3: e.g., "What are the implementation requirements?"]

### Approach

[How you investigated: e.g., "Analyzed commercial platform (EXP 'explore'), compared frameworks (ComfyUI vs N8N), evaluated architecture patterns, reviewed documentation and standards."]

### Tools and sources used

- [Tool/Source 1]: [purpose] — [how used]
- [Tool/Source 2]: [purpose] — [how used]

---

## What Was Evaluated

### [Technology/Framework/Approach 1]

**Description**: [Brief description]

**Key Characteristics**:
- [Characteristic 1]
- [Characteristic 2]
- [Characteristic 3]

**Use Cases**: [When/where it's used]

### [Technology/Framework/Approach 2] (if applicable)

**Description**: [Brief description]

**Key Characteristics**:
- [Characteristic 1]
- [Characteristic 2]

**Use Cases**: [When/where it's used]

---

## Findings

### What Works

- **[Finding 1]**: [Description and evidence]
- **[Finding 2]**: [Description and evidence]
- **[Finding 3]**: [Description and evidence]

### What Doesn't Work / Assumptions

- **[Limitation 1]**: [Description and context]
- **[Limitation 2]**: [Description and context]
- **[Assumption 1]**: [What we're assuming and why]

### Key Advantages

- **[Advantage 1]**: [Description]
- **[Advantage 2]**: [Description]

### Key Disadvantages

- **[Disadvantage 1]**: [Description]
- **[Disadvantage 2]**: [Description]

---

## Comparisons

### [Technology A] vs [Technology B]

| Aspect | [Technology A] | [Technology B] |
|--------|----------------|----------------|
| **Code Access** | [Description] | [Description] |
| **Debugging** | [Description] | [Description] |
| **AI Integration** | [Description] | [Description] |
| **Transparency** | [Description] | [Description] |
| **Ease of Use** | [Description] | [Description] |
| **Performance** | [Description] | [Description] |

### When to Use Each

- **Use [Technology A] when**: [scenarios]
- **Use [Technology B] when**: [scenarios]

---

## Recommendations

### Primary Recommendation

**[Recommendation]**: [Clear statement of what to do]

**Rationale**: [Why this recommendation]

**Success Criteria**: 
- [Criterion 1]
- [Criterion 2]
- [Criterion 3]

### Alternative Approaches (if applicable)

- **Option A**: [Description] — [Pros/Cons]
- **Option B**: [Description] — [Pros/Cons]

---

## Implementation Approach

### High-Level Architecture

[Brief description or diagram of the recommended architecture]

### Implementation Phases

**Phase 1: Foundation** (Weeks 1–4)
- [Task 1]
- [Task 2]
- **Deliverables**: [What's produced]

**Phase 2: Core Capabilities** (Weeks 5–8)
- [Task 1]
- [Task 2]
- **Deliverables**: [What's produced]

**Phase 3: Integration** (Weeks 9–12)
- [Task 1]
- [Task 2]
- **Deliverables**: [What's produced]

### Prerequisites

- [Prerequisite 1]
- [Prerequisite 2]
- [Prerequisite 3]

---

## Common Pitfalls and Solutions

| Pitfall | Impact | Solution |
|---------|--------|----------|
| [Pitfall 1] | [Impact description] | [How to avoid/solve] |
| [Pitfall 2] | [Impact description] | [How to avoid/solve] |

---

## Decisions & Rationale

### Decision 1: [Decision Name]

**Decision**: [What was decided]

**Rationale**: [Why this decision]

**Alternatives Considered**: [What else was considered and why it wasn't chosen]

### Decision 2: [Decision Name]

**Decision**: [What was decided]

**Rationale**: [Why this decision]

---

## Appendix A — Evidence & References

### Source Registry

| ID | Source (Title+URL) | Type | Version/Date | Relevance | Quality (A/B/C/D) | Notes |
|---|---|---|---|---|---|---|
| S1 | [Title](URL) | [vendor/standards/academic/community/internal] | [date] | [H/M/L] | [A/B/C/D] | |
| S2 | [Title](URL) | [type] | [date] | [H/M/L] | [A/B/C/D] | |

### Evidence Matrix

| Claim/Finding | Source IDs | Source Quality | Confidence (high/medium/low) | Evidence Notes |
|---|---|---|---|---|
| [Claim 1] | S1, S2 | [A/B/C/D] | [high/medium/low] | |
| [Claim 2] | S1 | [A/B/C/D] | [high/medium/low] | |

### External Resources

- [Resource 1](URL) — [Description]
- [Resource 2](URL) — [Description]

---

## 🔄 Next Steps

1. [Next step 1] — [Owner] — [Timeline]
2. [Next step 2] — [Owner] — [Timeline]
3. [Next step 3] — [Owner] — [Timeline]

---

## Appendix B — Version History & Raw Notes

### v1.0.0 - [Current Date]
- Template modernization with enhanced header structure, master tag system integration, and updated discovery location references
- Added Status, Author, Audience fields
- Added Master Tag System Integration section
- Added Discovery Paper Reference & Template Derivation section
- Updated discovery location from `01_Research_DISCOVERY` to `02_Research_WIP`

### v0.1.0 - [DD.MM.YYYY]
- Initial research document created from discovery.

---

## Appendix C — Tags

**ENVIRONMENT**: [inside_omniverse | outside_omniverse | hybrid | standalone]

[tag1] | [tag2] | [tag3] | [tag4] | [tag5]

---

## Appendix D — Discovery Content Not Included

> **Purpose**: This appendix captures all aspects from the discovery file that were **not included** in this research document at the time of creation. This prevents information loss during the discovery → research conversion process and allows future expansion or separate research documents.
> 
> **Note**: More details on these topics can be found in the discovery file. **It is recommended to provide a link to the corresponding discovery file** (e.g., `[Discovery File Name](path/to/discovery_file.md)` or `[Discovery File Name](../02_Research_WIP/discovery_file.md)`).

### Source Discovery File

- **Discovery File**: [Link to discovery file] — [Brief description of what the discovery file contains]
  - Example: `[ComfyUI_AI_Support_DISCOVERY.md](../02_Research_WIP/ComfyUI_AI_Support_DISCOVERY.md)` — Comprehensive discovery document covering ComfyUI AI integration, debugging capabilities, and Composable Bindings implementation

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
- **Variant Template**: `Research_Evaluation_Comparison_template.md`
- **Purpose**: Simplified evaluation/comparison variant for technology/approach evaluation

**Sections Structure**:
- Header with metadata (Purpose, Context, Status, Author, Audience)
- Template traceability
- Purpose & audience
- Executive summary
- Key conclusions
- Goals & methodology
- Findings & analysis
- Comparisons
- Recommendations
- Implementation approach
- Evidence & references
- Appendices (Version History, Tags, Discovery Content Not Included)

**Design Rationale**:
- **Simplified structure**: Streamlined for evaluation/comparison focus
- **Comparison emphasis**: Structured for clear technology/approach comparisons
- **Implementation focus**: Includes implementation approach section
- **Evidence-driven**: Includes source registry and evidence matrix
- **Discovery tracking**: Appendix D prevents information loss during conversion
- **Tag system integration**: Master tag system for cross-document discoverability

**Usage Context**: This template serves as a simplified framework for evaluating technologies, frameworks, or approaches with clear comparisons and implementation focus, positioned between comprehensive research (MasterResearch) and single findings (Finding template).

