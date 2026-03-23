---
arys_schema_version: '1.2'
id: 84ef7bf2-52db-4198-b8b7-1a00b72c5563
title: 00 Discovery - [REPLACE_ME:TOPIC]
type: STRATEGIC
status: active
trust_level: 2
visibility: internal
created: '2026-02-26T17:10:24Z'
last_modified: '2026-02-26T17:10:24Z'
---

# 00 Discovery - [REPLACE_ME:TOPIC]

**Version**: [REPLACE_ME:VERSION] | **Date**: [REPLACE_ME:DD.MM.YYYY] | **Time**: [REPLACE_ME:HH:MM] | **GlobalID**: [REPLACE_ME:GLOBAL_ID]

**Last Updated:** [REPLACE_ME:DD.MM.YYYY HH:MM]  
**Framework:** General_Research (Discovery Phase)  
**Status:** [REPLACE_ME:Initial Exploration / In Progress / Ready for Research Phase]

**Research Artifact:** [REPLACE_ME_TOPIC_RESEARCH.md](./REPLACE_ME_TOPIC_RESEARCH.md)

**Tag block:**
#needs_tagging

Template-first note: This file follows a two-stage lifecycle:
1. **GATHERING PHASE** (`status: gathering`): The "Raw Reservoir". Focus on **Gathering & Exploration**. Shed light on the unspoken, make the implicit explicit, and explore domain connections. **MANDATORY**: All explorations and questions for Jan MUST live in the **Appendix**. The main document body stays clean as a template.
2. **ACTIVE PHASE** (`status: active`): The "Distillation Phase". Move the gathered insights into the formal sections (Objectives, Architecture). The Gathering notes remain in the Appendix as an archive.

---

## Link and Citation Policy (Inherited)

Use `.cursor/rules/documentation-standards.mdc` as the single source of truth for in-text citations (`[[N]](#link-N)`) and `## Links` entry format (`N. <a id="link-N"></a>[Title](URL) - ...`).
If links are used in this document, add a dedicated `## Links` section and follow the canonical format from that rule file.

---

## External Prompt Policy (Embedded)

- Default behavior: keep external review prompts inside this discovery file.
- Do not create a separate `*_EXTERNAL_PROMPT.md` unless explicitly requested.
- Place the prompt in a dedicated section named `## External Review Prompt`.
- Place `## External Review Prompt` in the bottom area of the file, directly after `## Appendix: Raw Findings`.
- Required bottom order: `## Links` -> `## Appendix: Raw Findings` -> `## External Review Prompt`.
- If required context for a usable prompt is missing, ask concise clarifying questions before generating the prompt.

---

<!-- GATHERING PHASE: This section is empty. See the Appendix for questions and discoveries. -->

## Discovery Overview

**Subject:** [REPLACE_ME:TOPIC_NAME]

**Purpose:** [REPLACE_ME:What this discovery explores and why it matters]

**Research Framework:**
- **Ruling contract:** [REPLACE_ME:research_configuration_rules.yml or N/A]
- **Location:** `General_Research/070_Proj_RESEARCH/02_Research_WIP/`
- **Next Phase:** Convert to [REPLACE_ME:Topic_RESEARCH.md](./REPLACE_ME:Topic_RESEARCH.md) when ready for structured analysis

---

## Initial Observations

<!-- FRAME_STATUS: SET -->

> Why this matters: [REPLACE_ME:One sentence on why this discovery is important]

*Replace this placeholder text with your discovery findings...*

### Key Questions to Explore

- **Question 1:** [REPLACE_ME:What do we need to find out?]
  - [REPLACE_ME:Sub-question or context]
- **Question 2:** [REPLACE_ME:What do we need to find out?]
  - [REPLACE_ME:Sub-question or context]
- **Question 3:** [REPLACE_ME:What do we need to find out?]
  - [REPLACE_ME:Sub-question or context]

### Preliminary Findings

- **Finding 1:** [REPLACE_ME:Initial finding or insight]
- **Finding 2:** [REPLACE_ME:Initial finding or insight]
- **Finding 3:** [REPLACE_ME:Initial finding or insight]

---

## Research Scope

### Boundaries

- **Include:**
  - [REPLACE_ME:Scope item 1]
  - [REPLACE_ME:Scope item 2]
  - [REPLACE_ME:Scope item 3]
- **Exclude (for later):**
  - [REPLACE_ME:Out of scope item 1]
  - [REPLACE_ME:Out of scope item 2]

---

### Success Criteria

- [REPLACE_ME:Success criterion 1]
- [REPLACE_ME:Success criterion 2]
- [REPLACE_ME:Success criterion 3]

---

## References and Resources

*Add links, documentation, or resources discovered during exploration (local notes and external docs).*

Citation rule for body text: every linked claim uses `[[N]](#link-N)` pointing to the `## Links` index below.

---

## Next Steps

- [REPLACE_ME:Action item 1]
- [REPLACE_ME:Action item 2]
- [REPLACE_ME:Action item 3]

---

## Promotion Quality Gate (Mandatory Before Research Generation)

Run deterministic link validation on this discovery file before generating `*_RESEARCH.md`:

```powershell
python Master_Rules/040_Framework_TOOLS/link_existence_validator.py <this_discovery_file> --root . --template-mode off --skip-external
```

Pass condition:
- `failed_internal = 0`

Optional publish-ready check (external reachability):

```powershell
python Master_Rules/040_Framework_TOOLS/link_existence_validator.py <this_discovery_file> --root . --template-mode off
```

---

## Links

1. <a id="link-1"></a>[REPLACE_ME:Title](REPLACE_ME:URL) - [REPLACE_ME:1-2 sentences: what it is and why it matters].
2. <a id="link-2"></a>[REPLACE_ME:Title](REPLACE_ME:URL) - [REPLACE_ME:1-2 sentences: what it is and why it matters].

In running text, cite like:

`[REPLACE_ME:Linked claim](REPLACE_ME:URL) [[1]](#link-1)`

---

## Appendix: Raw Findings (The Gathering Reservoir)

**Status Trigger**: When `status: gathering`, this is the ONLY place for exploration.
**Purpose**: Gather ideas, make the implicit explicit, and explore domain connections. Shed light on the unspoken.

### Mandatory Feedback Loop: Questions for Jan
- [ ] [QUESTION 1 - Focus on making the implicit explicit]
- [ ] [QUESTION 2 - Focus on shedding light on the unspoken]

### Peripheral Exploration & Findings
- [PASTE RAW DATA HERE]

---

## External Review Prompt

Use this block when requesting independent external model review. Keep this prompt in this discovery file by default.

```text
[REPLACE_ME:External review prompt content]
```

---
