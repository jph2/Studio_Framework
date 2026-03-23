---
arys_schema_version: '1.2'
id: 43b7e453-8094-4b28-95ac-90602908f5d5
title: Internal Research Analysis template
type: STRATEGIC
status: active
trust_level: 2
visibility: internal
created: '2026-02-21T08:34:26Z'
last_modified: '2026-02-21T08:34:26Z'
---

﻿# [Research Title] â€” Internal Research Analysis

**Version**: 0.0.0 | **Date**: 13.01.2026 | **Time**: 00:31 | **GlobalID**: 20260113_0031_GeneralResearch_Internal_Research_Analysis_templ

**Tag block:**
#omniverse #analysis #case_study #workflow_optimization #framework_integration #workflow_automation #quality_assurance #best_practices

**Purpose**: Synthesize research findings for internal teams through storytelling and technical analysis

**Context**: Internal research synthesis document providing technical teams with narrative context, implementation details, and actionable insights

> **Status**: [Draft/Final] | **Date**: [DD.MM.YYYY] | **Environment**: [inside_omniverse/outside_omniverse/hybrid/standalone]

> **Author**: [Research Analyst/Technical Lead] | [Contact]
> **Technical Review**: [Subject Matter Experts, Senior Engineers]
> **Stakeholders**: [Development Teams, Architects, Product Owners]

**Discovery Source:** [REPLACE_ME_TOPIC_DISCOVERY.md](./REPLACE_ME_TOPIC_DISCOVERY.md)

## ðŸ§¾ Copy-paste prompt snippet (short)

Use `Internal_Research_Analysis_template.md` as the target structure and return the final document as Markdown.
For the full generation contract, see **Appendix H â€” Copy-Paste Prompt Snippet**.

> **Pre-flight (Discovery frame check)**: If this document is being generated from a `*_DISCOVERY.md` and the discoveryâ€™s **Initial Observations / Preliminary Findings** and/or **Research Scope** still contain placeholders (or markers like `<!-- FRAME_STATUS: UNSET -->` / `<!-- SCOPE_STATUS: UNSET -->`), include the Quality Note below near the top of the output and recommend filling those discovery sections before re-running.
>
> Tooling support (warn-only): `Master_Rules/040_Framework_TOOLS/discovery_frame_checker.py`
>
> **Quality Note (Scope/Frame)**: This research was generated even though the discoveryâ€™s Initial Observations / Preliminary Findings and/or Research Scope still contain placeholders or were not fully filled. Some drift may have occurred. If youâ€™re unhappy with the results, fill those discovery sections and re-run research generation.

---

## Link and Citation Policy (Inherited)

Use `.cursor/rules/documentation-standards.mdc` as the single source of truth for in-text citations (`[[N]](#link-N)`) and `## Links` entry format (`N. <a id="link-N"></a>[Title](URL) - ...`).
If links are used in this document, add a dedicated `## Links` section and follow the canonical format from that rule file.

---


**Quick Navigation**: [Executive Summary](#executive-summary) | [Deep Dive](#deep-dive) | [Building Blocks](#building-blocks--key-concepts) | [Technical Analysis](#technical-analysis) | [Implementation Specifications](#implementation-specifications) | [Evidence & Recommendations](#evidence--recommendations)

---

## Executive Summary (Short Story)

[Write 150-300 words as a narrative that hooks the reader. Start with the problem (why does this matter?), present the insight (what's the breakthrough?), and promise the outcome (what will readers gain?). This is the SHORT version of the story - make it compelling.]

**Example opening style:**
> "For years, we've struggled with [problem]. Despite our best efforts, [consequence]. But something fundamental has changed. [Insight]. This research reveals [promise]."

### Core Research Insight

[1-2 sentences capturing the fundamental discovery that drives all recommendations. This is the "aha moment" in one line.]

### What This Research Enables

[3-5 bullet points summarizing what readers will be able to do after reading this research. Focus on outcomes, not just findings.]

---

## Deep Dive (Long Story)

[Write 800-1500 words as a narrative journey through the discovery. This is the LONG version of the story - take readers through the full exploration, preserve the "aha moments", and explain the "why" behind each key decision. Use narrative prose with bullet points and subheadings for structure and navigation.]

### The Problem We're Solving

[Narrative prose explaining the problem in human terms. Why does this matter? What are the real-world consequences of not solving this?]

### What Changed

[Narrative explaining the shift, breakthrough, or new capability that makes a solution possible. This is often the "2026 moment" - what's different now?]

### The Core Loop / System Overview

[Narrative explaining how the solution works at a high level. Walk through the flow from start to finish. Use bullet points to structure the flow for navigation.]

### Key Decisions and Why They Matter

[Narrative explaining the major decisions made in the design. For each decision, explain the "why" - what problem does it solve? What alternative was rejected?]

### What It Feels Like When Working

[Narrative describing the experience of using the system successfully. This helps readers understand the goal state.]

---

## Building Blocks / Key Concepts

[If the source material contains numbered building blocks, key concepts, or core components, preserve them here as a numbered list with names and explanations. Use the original names and metaphors where possible.]

### [Number]. [Block Name] ([Technical Term])

**What it is**: [Brief description]
**Why it matters**: [Explanation of importance]
**How it works**: [Brief explanation]

[Repeat for each building block]

---

## Principles / Design Guidelines

[If the source material contains numbered principles, guidelines, or rules, preserve them here as a numbered list. Include the original phrasing and practical examples.]

1. **[Principle Name]** - [Brief explanation and example]
2. **[Principle Name]** - [Brief explanation and example]
3. [Continue for all principles]

---

## Technical Analysis

### 1. Architecture Overview

[Technical description of the system architecture, organized by layers or components.]

### 2. [Technical Domain 1] â€” [Analysis]

[Technical Domain 1] analysis reveals:

* **[Finding 1]**: [Detailed analysis]
* **[Finding 2]**: [Technical significance]
* **[Finding 3]**: [Integration considerations]

### 3. [Technical Domain 2] â€” [Analysis]

[Continue for additional technical domains]

### 4. Cross-Domain Integration

* **[Domain 1 + Domain 2]**: [How these interact]
* **[System-level Implications]**: [How everything works together]

### 5. Evidence Quality Assessment

**Research Rigor Evaluation:**
- **Data Quality**: [Assessment of sources and methodology]
- **Analysis Quality**: [Assessment of analytical methods]
- **Conclusion Confidence**: [Overall confidence level]

**Research Limitations:**
- **Scope Limitations**: [What was not covered]
- **Methodology Constraints**: [Limitations in approach]
- **External Validity**: [How well findings generalize]

---

## Implementation Specifications

**CRITICAL**: This section preserves exact specifications from the source material. Do not synthesize or abstract these details.

**Spec/Definition Preservation (Software-dev discoveries)**: If the source `*_DISCOVERY.md` already defines architecture/framework-fit, definitions, schemas, thresholds, interfaces, or evaluation criteria, preserve them verbatim. If you intentionally change them, log the change (with rationale + impact) in the **Deviation Log (Appendix E)**.

### Database / Schema Definitions

[Preserve exact field definitions, data structures, and schemas from source material]

**[Entity Type 1]:**
- Field 1: [description]
- Field 2: [description]
- [Continue for all fields]

**[Entity Type 2]:**
- [Continue for all entity types]

### Specific Numbers & Thresholds

[Preserve exact numbers, thresholds, and limits from source material]

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| [Parameter 1] | [Value] | [Why this number] |
| [Parameter 2] | [Value] | [Why this number] |

### Tech Stack / Tool Recommendations

[Preserve exact technology recommendations from source material]

- **[Layer 1]**: [Tool/Technology] - [Rationale]
- **[Layer 2]**: [Tool/Technology] - [Rationale]
- [Continue for all layers]

### Core Loop / MVP Definition

[Preserve the exact core loop or MVP definition from source material]

```
[Step 1] â†’ [Step 2] â†’ [Step 3] â†’ [Step 4] â†’ [back to Step 1]
```

---

## Portability & Anti-Lock-In

[If source material discusses portability, swappability, or vendor lock-in avoidance, preserve those details here]

### Swappability Matrix

| Layer | What Can Be Swapped | Hard Rule (Must Not Change) | How to Keep Swappable |
|-------|---------------------|---------------------------|----------------------|
| [Layer 1] | [Options] | [Constraint] | [Strategy] |
| [Layer 2] | [Options] | [Constraint] | [Strategy] |

### Portable Core Requirements

[Preserve exact requirements for portability: what must be backed up, restore strategy, replay strategy]

### Backup / Restore / Replay

- **What gets backed up**: [List]
- **Backup cadence**: [Frequency]
- **Restore verification**: [Strategy]
- **Replay capability**: [How projections can be rebuilt]

---

## Implementation Implications

### Technical Feasibility Assessment

**Implementation Readiness:**
- **Current Capabilities**: [What already exists]
- **Capability Gaps**: [What's missing]
- **Resource Requirements**: [What's needed]

### Development Approach Recommendations

**Recommended Strategy:**
- **Phased Implementation**: [Sequencing]
- **Technology Selection**: [Recommendations]
- **Team Structure**: [Roles needed]

### Risk Assessment & Mitigation

| Risk Category | Specific Risk | Probability | Impact | Mitigation Strategy |
|---------------|---------------|------------|--------|-------------------|
| [Category] | [Risk] | [P] | [I] | [Strategy] |

---

## Evidence & Recommendations

### Research Evidence Sources

### Evidence Matrix (Top claims only)

| Claim / Recommendation | Source IDs | Evidence Quality | Confidence | Notes |
|------------------------|------------|------------------|------------|-------|
| [Top claim or recommendation #1] | SRC-001, SRC-002 | [A/B/C/D] | [High/Med/Low] | [Why the evidence supports this] |
| [Top claim or recommendation #2] | SRC-003 | [A/B/C/D] | [High/Med/Low] | [Constraints, caveats, dependencies] |

**Source Registry:**

**Policy**: Source Registry must include **100% of canonical URLs** captured in **Appendix D** (or explicitly mark exclusion with rationale).

| SRC-ID | Source (Title+URL) | Type | Date/Version | Relevance | Quality (A/B/C/D) | Notes |
|--------|-------------------|------|--------------|-----------|------------------|-------|
| SRC-001 | [Source Name](URL) | [type] | [date] | [relevance] | A | [notes] |
| SRC-002 | [Source Name](URL) | [type] | [date] | [relevance] | A | [notes] |
| SRC-003 | [Source Name](URL) | [type] | [date] | [relevance] | A | [notes] |

### Technical Recommendations

#### Immediate Actions (0-3 Months)
- [ ] [Action item with specific detail]
- [ ] [Action item with specific detail]

#### Short-term Goals (3-6 Months)
- [ ] [Action item with specific detail]

#### Long-term Objectives (6-12 Months)
- [ ] [Action item with specific detail]

---

## Next Steps & Action Items

### Immediate (Next 2 Weeks)
- [ ] [Specific action]
- [ ] [Specific action]

### Short-term (1-2 Months)
- [ ] [Specific action]

### Long-term (3-6 Months)
- [ ] [Specific action]

---

## Appendix A â€” Research Methodology

### Data Sources & Collection
[Document primary data sources and collection methods]

### Analysis Framework
[Document analytical approach used]

### Research Quality Assurance
[Document validity and reliability measures]

---

## Appendix B â€” Version History

### v1.0.0 - [Date]
- Initial creation from [source discovery document]
- [Key changes and additions]

---

## Appendix C â€” Research Validation Checklist

**CRITICAL**: Verify research findings and content preservation.

#### Storytelling Validation
- [ ] Executive Summary tells a compelling short story (150-300 words)
- [ ] Deep Dive takes readers on a narrative journey (800-1500 words)
- [ ] Readers can understand "what this is about" in first 2 minutes

#### Content Preservation Validation
- [ ] All numbered blocks/concepts preserved in order with names
- [ ] All numbered principles preserved with examples
- [ ] All specific numbers and thresholds preserved
- [ ] All schemas and field definitions preserved
- [ ] Swappability/portability requirements preserved (if applicable)
- [ ] All source links preserved with URLs

#### Link Preservation Validation
- [ ] 100% of canonical links from discovery document preserved in Link Registry (Appendix D)
- [ ] All links have valid URLs (not just titles)
- [ ] Links organized by functional category
- [ ] Link Registry contains all URLs verbatim (no summarization or curation)
- [ ] Link preservation validation script confirms 100% preservation

#### Deviation Log Validation
- [ ] All numeric constraints and thresholds compared with discovery document
- [ ] All deviations documented in Deviation Log (Appendix E) with justification
- [ ] Preserved values marked with âœ…
- [ ] Deviations marked with âš ï¸ and explained

**Validation Result**: [âœ… VALIDATED / âŒ REQUIRES REVIEW - Issues: ]

---

## Appendix E â€” Deviation Log

**CRITICAL**: If any numeric constraints, schemas, thresholds, or specifications differ from the discovery document, they **must** be explicitly documented here with justification. This prevents silent drift while allowing intentional improvements.

**Instructions:**
- Compare all numeric values, thresholds, and specifications between discovery and research documents
- Document any differences with clear justification
- Mark preserved values with âœ…
- Mark deviations with âš ï¸ and provide explanation
- If no deviations exist, state "No deviations from discovery document"

**Example Format:**

| Specification | Discovery Value | Research Value | Status | Justification |
|--------------|----------------|---------------|--------|---------------|
| Confidence threshold | 0.6 | 0.6 | âœ… Preserved | Exact match |
| Daily digest word limit | 150 words | <150 words | âš ï¸ Minor deviation | Still acceptable, maintains intent |
| Number of categories | 4 | 4 | âœ… Preserved | Exact match |

**Numeric Constraints & Thresholds:**

[Document all numeric values, thresholds, limits from discovery]

**Schema Definitions:**

[Document any schema changes or field modifications]

**Specification Changes:**

[Document any other specification deviations]

**Validation:**
- All deviations documented: [Yes/No]
- Justifications provided: [Yes/No]
- Intentional improvements clearly marked: [Yes/No]

---

## Appendix F â€” Discovery Document Reference

**Source Discovery Document**: `[DISCOVERY_FILENAME]_DISCOVERY.md`

**Location**: `ðŸ”¬ General_Research (Research Library)/070_Proj_RESEARCH/02_Research_WIP/[DISCOVERY_FILENAME]_DISCOVERY.md`

**Note**: The discovery document contains the complete source material (conversation transcript, raw notes, full context). This research document synthesizes and preserves the key insights. For full context, refer to the discovery document.

**Key Sections in Discovery** (line number references):
- [Lines X-Y]: [Description of section]
- [Lines X-Y]: [Description of section]
- [Lines X-Y]: [Description of section]

---

## Appendix G â€” Framework Integration & Traceability

### ðŸ¤– Agent Usage Instructions

**Template**: `Internal_Research_Analysis_template.md` (Storytelling + Strategic Findings framework)
**Audience**: Technical teams, architects, developers, researchers
**Focus**: Narrative storytelling + research synthesis + implementation details
**Length**: 400-600 lines (storytelling + evidence-based + implementation-oriented)

**Usage Context**: This template transforms discovery material into engaging, narrative-driven research documents that preserve implementation details while telling a compelling story. Story and context come first; technical sections support understanding.

### ðŸ“‹ Template Traceability

**REQUIRED**: Every research document created from this template MUST include:

- **Template Used**: `Internal_Research_Analysis_template.md`
- **Template Version**: v2.3.0
- **Template Profile**: `internal_research_analysis_storytelling`
- **Template Location**: `ðŸ”¬ General_Research (Research Library)/030_Proj_TEMPLATES/Internal_Research_Analysis_template.md`
- **Mandatory Appendices**: Appendix D (Link Registry) and Appendix E (Deviation Log) are required for 100% link preservation

### ðŸ”— Framework Integration Notes

**Storytelling Architecture**: This template uses a narrative-first structure where Executive Summary (short story) and Deep Dive (long story) establish context before technical sections provide supplementary detail.

**Content Preservation**: All numbered blocks, principles, specific numbers, schemas, and links from discovery documents must be preserved in their respective sections. **Link Registry (Appendix D)** ensures 100% link preservation, and **Deviation Log (Appendix E)** prevents silent drift in specifications.

**Agent Routing**: Documents created from this template are processed by internal technical agents for requirements generation, implementation planning, and code generation workflows.

**Quality Assurance**: All documents must pass storytelling validation (engaging narrative) and content preservation validation (100% of key content preserved).

---

## Appendix H â€” Copy-Paste Prompt Snippet (For Research Analysts)

**Purpose**: This section provides a ready-to-use prompt snippet for research analysts when creating new research documents from discovery material.

Use `Internal_Research_Analysis_template.md` as the target structure.
Transform discovery material into an engaging, narrative-driven research document.

**STORYTELLING REQUIREMENTS**:

- **Executive Summary** = Short story (150-300 words)
  - Tell what this is about in narrative form
  - Hook with the problem (why does this matter?)
  - Present the insight (what's the breakthrough?)
  - Promise the outcome (what will readers gain?)
  - Make it engaging - readers should want to continue
  
- **Deep Dive** = Long story (800-1500 words)
  - Take readers on a journey through the discovery
  - Preserve the "aha moments" from the original source
  - Explain the "why" behind each key decision
  - Use narrative prose as the foundation
  - Structure with bullet points, bold text, and subheadings for navigation
  - Bullet points help readers find specific arguments and navigate the text
  - Reference discovery document for full context

- **Technical sections** = Supplementary for decisions
  - Come AFTER the story establishes context
  - Support understanding, don't replace the narrative

**CONTENT PRESERVATION REQUIREMENTS**:

- If source contains numbered blocks (e.g., "8 building blocks", "3 steps to...", "12 principles"), preserve them as numbered lists with names and explanations
- If source contains MVP definitions, core loop specs, or acceptance criteria, preserve them exactly
- Preserve specific numbers (thresholds, word limits, categories, etc.)
- Preserve database schemas, field definitions, and tech stack recommendations
- Preserve swappability matrices, portability requirements, and similar structured content
- Reference discovery document (do NOT duplicate full transcript)
- **MANDATORY**: Ensure 100% link preservation from source documents
- **MANDATORY**: All links must be preserved verbatim in Appendix D â€” Link Registry
- **MANDATORY**: Each link in Appendix D must include 1-2 sentences of context OR keywords + one sentence explaining what the link is about and why it's relevant
- **MANDATORY**: Any deviations from discovery specifications must be documented in Appendix E â€” Deviation Log
- **MANDATORY**: All tags/keywords must come from master tag system (`Master_Rules/master_tag_system.yml`)
- **Note:** Tags and keywords are the same internallyâ€”we treat them all as tags. When communicating externally, "tags/keywords" is acceptable for clarity.

**GENERATION PROCESS REQUIREMENTS**:

- **Pass 1: Creative Synthesis** - Generate narrative + architecture sections. You may curate and restructure content as needed for storytelling and clarity.
- **Pass 2: Evidence Preservation** - Append full Link Registry (Appendix D) verbatim from discovery document. Do NOT summarize or curate links. This is mandatory for 100% link preservation. Add 1-2 sentences of context OR keywords + one sentence to each link.

**POST-GENERATION VALIDATION**:

- Run link-preservation validation script to verify 100% canonical link preservation
- If preservation < 100%, regenerate Link Registry until complete
- Verify that each link in Appendix D includes context (1-2 sentences OR keywords + one sentence)
- Document any deviations in Deviation Log (Appendix E)

---

## Appendix D - Link Registry (Preserved from Discovery)

**Redundant once Source Registry is complete**: Appendix D is kept as a canonical â€œall-links capturedâ€ registry preserved from discovery. If all links have been fully captured in the Source Registry (with `SRC-###` IDs) and you donâ€™t need this redundancy, you can ignore or remove Appendix D.

**CRITICAL**: This section is **mandatory** and **non-negotiable**. It must contain **all canonical URLs** from the discovery document, preserved verbatim for traceability and evidence retention.

**Instructions for Research Analysts:**
- Extract all URLs from the discovery document using link validation script or manual extraction
- Canonicalize URLs (remove utm_* tracking parameters, normalize trailing slashes)
- List all links here in structured format, categorized by capability/topic
- Do NOT summarize, curate, or omit any links
- **MANDATORY**: Each link MUST include 1-2 sentences of context OR keywords + one sentence explaining what the link is about and why it's relevant
- This registry serves as the evidence backbone for traceability AND as a reference source for links used throughout the document
- Links should be organized by functional category for easy reference

**Link Format Requirements:**
- **Format Option 1 (Keywords + Sentence):** `- [Link Title](URL) - **Keywords:** keyword1, keyword2. One sentence explaining what this link covers and why it's relevant to the research.`
- **Format Option 2 (1-2 Sentences):** `- [Link Title](URL) - First sentence explaining what this link is about. Second sentence (if needed) explaining why it's relevant or how it fits into the architecture.`

**Example:**
- [Slack Events API](https://api.slack.com/apis/events-api) - **Keywords:** Slack, capture, real-time events, webhooks. Primary capture interface for ingesting messages, reactions, and channel activity into the second brain system as CloudEvents.

**Link Organization Categories:**
- Capture & Connectors (Slack, Teams, Email, Calendar, etc.)
- Workflow Orchestration (Temporal, LangGraph, Prefect, etc.)
- AI & Intelligence (LiteLLM, JSON Schema, MCP, etc.)
- Storage & Backup (MinIO, Hetzner, restic, WAL-G, etc.)
- Observability & Trust (OpenTelemetry, Braintrust, Langfuse, etc.)
- Entity Catalog & Metadata (Backstage, entity schemas, etc.)
- Policy & Governance (OPA bundles, Rego, etc.)
- Event Log & Event Sourcing (CloudEvents, NATS JetStream, etc.)
- Knowledge Graphs (Neo4j, etc.)
- Second Brain Methodology (PARA, CODE, etc.)
- Domain-Specific Integrations (USD/Omniverse, ComfyUI, Adobe, etc.)

### Capture & Connectors

**Format:** Each link must include 1-2 sentences of context OR keywords + one sentence.

- [Link Title](URL) - **Keywords:** keyword1, keyword2. One sentence explaining what this link covers and why it's relevant.
- [Link Title](URL) - First sentence explaining what this link is about. Second sentence (if needed) explaining why it's relevant or how it fits into the architecture.

[All capture/connector links from discovery document with context]

### Workflow Orchestration

[All workflow orchestration links from discovery document]

### AI & Intelligence

[All AI and intelligence-related links from discovery document]

### Storage & Backup

[All storage and backup links from discovery document]

### Observability & Trust

[All observability and trust-related links from discovery document]

### Entity Catalog & Metadata

[All entity catalog and metadata links from discovery document]

### Policy & Governance

[All policy and governance links from discovery document]

### Event Log & Event Sourcing

[All event log and event sourcing links from discovery document]

### Knowledge Graphs

[All knowledge graph links from discovery document]

### Second Brain Methodology

[All second brain methodology links from discovery document]

### Domain-Specific Integrations

[All domain-specific integration links from discovery document]

### Complete Link List (Alphabetical by Domain)

[Optional: Complete alphabetical list for quick reference and validation]

**Validation:**
- Total canonical links from discovery: [N]
- Links preserved in this registry: [N]
- Preservation rate: 100% (required)

