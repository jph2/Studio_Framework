---
arys_schema_version: '1.2'
id: b7909611-4cc0-4952-9776-a3a5869d6e93
title: Internal_Research_Analysis_template — Deviations vs Other Active Templates
  (ARCHIVED)
type: STRATEGIC
status: active
trust_level: 2
visibility: internal
created: '2026-02-18T05:33:26Z'
last_modified: '2026-02-18T05:33:26Z'
---

# Internal_Research_Analysis_template — Deviations vs Other Active Templates (ARCHIVED)

**Version**: N/A | **Date**: 13.01.2026 | **Time**: 00:20 | **GlobalID**: 20260113_0020_General_Research_AUTO

**Archived on**: 12.01.2026  
**Superseded by**: `../CHANGELOG.md` (templates-only change history)

#workflow_optimization #best_practices #case_study

---

# Internal_Research_Analysis_template — Deviations vs Other Active Templates

**Baseline (“master candidate”)**: `Internal_Research_Analysis_template.md` (**v2.3.0**)  
**Comparison set**: All non-archived templates in `General_Research/030_Proj_TEMPLATES/` (excludes `archive/`; ignores `legacy/`).

**Why this document exists**: to make the next step (rolling improvements into other templates) concrete and low-risk by clearly stating (a) what differs, (b) why the `Internal_Research_Analysis_template` approach is likely better, and (c) what should be ported (or not) into other templates.

---

## 2a) Deviation Table (Baseline vs Others)

Legend:
- **Baseline** = `Internal_Research_Analysis_template.md`
- **Families** referenced below:
  - **Research Analysis**: `External_Research_Analysis_template.md`
  - **Strategic Guidance**: `Internal_Strategic_Guidance_template.md`, `External_Strategic_Guidance_template.md`
  - **Decision Support**: `Internal_Decision_Support_template.md`, `External_Decision_Support_template.md`
  - **Requirements Engineering**: `Internal_Requirements_Engineering_template.md`, `External_Requirements_Engineering_template.md`
  - **Implementation Planning**: `Internal_Implementation_Planning_template.md`, `External_Implementation_Planning_template.md`
  - **Documentation**: `Documentation_HowTo_template.md`, `Documentation_WhatWeDid_template.md`
  - **Reference / specialized**: `Research_Strategic_Findings_light_template.md`, `Research_3D_ConversionPipeline_Evaluation_template.md`

| Feature / Section | Baseline behavior (Internal Research Analysis) | Other templates behavior (summary) | Why baseline is likely better | Cost / risk if ported into other templates | Recommendation |
|---|---|---|---|---|---|
| 2a.1) Narrative-first opening | Starts with **Executive Summary (Short Story)** + **Deep Dive (Long Story)** (explicit word ranges) before technical sections. | Most templates start with **Executive Summary** but not explicit narrative requirements; they are “analysis-first” or “decision/plan-first”. | Strongly improves human uptake + preserves “why” and “aha moments”, which reduces downstream drift and mis-implementation. Also more robust against code-optimized models stripping narrative. | Adds length and may not fit “pure planning/spec” templates; external exec docs may prefer shorter narrative or business framing. | **Port selectively**: keep full narrative requirement for Research Analysis; add *light narrative* option (short story only) in other templates where appropriate. |
| 2a.2) Story → Tech sequencing | Explicitly forces story first, tech later (“technical sections are supplementary for decisions”). | Most templates mix context and analysis early; the specialized pipeline template uses guided flow but not explicit story primacy. | Prevents “structure without understanding”: readers get context before details; improves agent summary quality. | Some audiences want immediately actionable checklists; risk of “too slow to value” for decision/planning docs. | **Keep baseline-only** as default; offer an **optional** “Narrative Context” subsection for other templates. |
| 2a.3) Building blocks + principles preservation | Dedicated sections for **Building Blocks / Key Concepts** and **Principles / Design Guidelines** (explicitly preserve numbered lists). | Rare/absent in most templates; Strategic Findings light has similar “architecture model / patterns” but not explicitly framed as “preserve numbered blocks”. | Directly mitigates a known failure mode: models drop numbered artifacts (steps/principles) during synthesis. | Adds structure some docs don’t need; could create empty sections when source has no numbered blocks. | **Port as conditional**: add “If present, preserve numbered blocks/principles” guidance to all research-family templates. |
| 2a.4) “Preserve exact specs” section | **Implementation Specifications** section is explicitly “CRITICAL: preserve exact specifications, do not synthesize”. | Requirements/Planning templates preserve specs via their own sections; others are less explicit. | Creates a hard barrier against silent abstraction of schemas, thresholds, and constraints (high value for buildability). | Can be redundant in Requirements/Planning templates; may push authors to copy too much into non-spec documents. | **Port conceptually**: keep as-is for Research Analysis; add a short “spec preservation” note to other templates where they include numeric/spec fields. |
| 2a.5) Anti-lock-in / swappability | Explicit **Portability & Anti-Lock-In** + **Swappability Matrix** + **Backup/Restore/Replay**. | Mostly absent outside baseline; planning templates cover “risk/resources” but not portability. | High leverage for architecture decisions (especially platform/tooling choices); prevents vendor lock-in drift. | Adds complexity and length; may be irrelevant for many topics. | **Optional port**: add a conditional “Portability & Anti-Lock-In (if relevant)” block to Strategic Guidance + Implementation Planning. |
| 2a.6) Evidence structure (Source Registry) | Has **Evidence & Recommendations → Evidence Matrix (Top claims only) → Source Registry** (complete list). | Most templates include a Source Registry; some include Evidence Matrices as well. | Standardizing **SRC-IDs** + ordering (matrix before registry) improves auditability and avoids “hand-wavy recommendations”. | If required everywhere, increases table size; in external templates it may be too long/noisy. | **DONE (ported)**: Evidence Matrix before Source Registry + SRC-ID format `SRC-###` + policy: “Source Registry must include 100% of canonical URLs captured in Appendix X (or explicitly mark exclusion with rationale).” |
| 2a.7) Evidence matrix (claims → sources) | Baseline includes an Evidence Matrix table mapping claims/recommendations → **SRC-IDs** (Top claims only). | Many templates include **Evidence Matrix** (Decision Support, Planning, pipeline evaluation, etc.). | Evidence matrices improve auditability and reduce “hand-wavy recommendations”. | Adds author effort; can become busywork unless scoped to top claims. | **DONE (standardized)**: keep “Top claims only” scope; enforce SRC-ID references only. |
| 2a.8) Link preservation enforcement mechanism | Baseline has **Appendix X — Link Registry (Preserved from Discovery)** with strict rules + per-link context requirements, kept as final appendix. | Other templates now also include Appendix X as the canonical capture list. | Appendix X is the strongest enforcement because it defines a single place where *all canonical URLs* must be preserved. | If ported everywhere, documents balloon; for external audiences this may be too much in the main doc (but can live as appendix). | **DONE (ported to discovery-derived templates)**: Appendix X exists and is labeled “redundant once Source Registry is complete”; Source Registry remains the working list with `SRC-###` IDs. |
| 2a.9) Link visibility where decisions happen (A034 policy alignment) | Baseline enforces link capture in Appendix X; main body Source Registry is the single working registry. | Other templates align the same way. | Best practice is “audit + usability”: Appendix X guarantees completeness; Source Registry guarantees discoverability and consistent referencing via SRC-IDs. | Enforcing 100% in main body can make the table large; may require grouping or additional columns/tags. | **DONE (standardized)**: Source Registry must include 100% of Appendix X (or explicit exclusions with rationale). |
| 2a.10) Two-pass generation strategy | Baseline describes **Pass 1 (creative synthesis)** and **Pass 2 (evidence preservation)** in Appendix H. | Many templates have generation guidance; the two-pass idea remains valuable for robustness. | Separates creativity from completeness enforcement (especially for links/specs). | Adds process detail; some teams may ignore it. | **Keep recommendation**: add/retain two-pass guidance for discovery-derived generation workflows where link/spec preservation matters. |
| 2a.11) Deviation / anti-drift logging | Baseline includes **Deviation Log** (Appendix E). | Other templates now include a **Deviation Log (Required)** appendix (with N/A allowed if not derived from discovery/source). | Prevents silent drift; makes intentional improvements explicit and reviewable. | Extra work when the doc is not derived from discovery/source. | **DONE (mandatory)**: Deviation Log present across active templates. |
| 2a.12) Prompt snippet placement (“moved down”) | Baseline now has a short top prompt snippet and a full prompt appendix (Appendix H remains the full contract). | Other templates now follow the same pattern: short top snippet + full prompt appendix. | Keeps reader-facing doc clean while preserving author convenience. | Low risk; minor template churn. | **DONE (standardized)** across active templates. |
| 2a.13) Tag system integration | Baseline has **Tags (Keywords)** at top and mandates master tags; references tag sync workflow. | Other templates now also include top-level tags lines (while keeping tag appendices where they exist). | Improves indexing/discoverability and prevents tag drift. | Low risk. | **DONE (mandatory)** across active templates. |
| 2a.14) “Discovery Content Not Included” safety net | Baseline does **not** include a “Discovery Content Not Included” appendix. | Present in `Research_3D_ConversionPipeline_Evaluation_template.md` and `Research_Strategic_Findings_light_template.md` (and some archived templates). | Captures “left on the cutting-room floor” topics, preventing information loss during discovery → synthesis. | Adds another appendix and requires authors to actively curate excluded items. | **Import into baseline (recommended)** as optional appendix for discovery-derived research. |
| 2a.15) Requirements traceability | Baseline includes a discovery reference appendix but does not include a formal requirements traceability matrix. | Requirements/Planning templates include traceability matrices and structured IDs (FR-001, etc.). | For research synthesis, full traceability may be overkill; but referencing where key specs came from is valuable. | Adding full matrices to research templates may bloat and duplicate requirements docs. | **Do not port** full traceability into baseline; keep cross-links and add “key decision→source IDs” evidence matrix instead. |
| 2a.16) Decision framing (“Decision Ask”) | Baseline has recommendations and next steps but not an explicit “Decision Ask” section. | Pipeline evaluation template has a **Decision Ask** section; decision support templates also effectively implement decision framing. | When research is meant to drive an immediate decision, explicit “Decision Ask” reduces ambiguity and speeds governance. | Not every research doc needs a decision request; could feel forced. | **Optional port**: add a small “Decision Ask (optional)” subsection under Evidence & Recommendations. |
| 2a.17) Discovery frame/scope enforcement (pre-flight check) | Baseline includes **Pre-flight (Discovery frame check)** with warn-only Quality Note. Tooling support: `discovery_frame_checker.py`. | Discovery-derived templates now include the same pre-flight check (warn-only). | Prevents the exact problem: drift into generic trends when discovery’s frame/scope is incomplete. | Minimal cost. | **DONE (ported)** to discovery-derived templates (Research Analysis, Strategic Guidance, Decision Support). |

---

## 2b) Explanatory Analysis (What differs, why it’s better, what to change next)

### 2b.1) Summary: the biggest structural advantages of the baseline

1. **Narrative-first structure is deliberate** (Short Story + Long Story) and protects context and intent, which reduces downstream mis-implementation.
2. **Hard enforcement of content preservation** exists for: numbered building blocks, numbered principles, exact specs, and (critically) **links**.
3. **Appendix X + Deviation Log are “governance primitives”**: Link Registry (auditability) and Deviation Log (anti-drift).
4. **Two-pass workflow** (“creative synthesis” then “evidence preservation”) is explicitly described, making the template resilient to model choice issues.
5. **Master tag system enforcement** is explicit and up-front, improving cross-document discoverability and preventing tag drift.
6. **Discovery frame/scope enforcement** (Pre-flight check) prevents research drift by detecting when discovery’s interpretation frame is missing and surfacing a warning. This addresses the core failure mode: research becoming generic instead of context-aware (e.g., "how to integrate into existing system").

### 2b.2) The “moved to appendix” pattern (what moved and why it’s better)

Across the template set, many templates put operational instructions (“how to run an agent”, “how to validate links”, “traceability requirements”) near the top. The baseline pushes heavy operational detail into appendices (e.g., **Appendix H** prompt snippet; **Appendix C/D/E** validation and enforcement).

**Why this is better**:
- **Reader-first**: humans see story + substance first, rather than process boilerplate.
- **Agent robustness**: appendices act as “non-negotiable guardrails” that are harder to overlook during generation.
- **Reduced template fatigue**: readers are less likely to skip the document because the front matter is bloated.

**Tradeoff**: authors may miss the prompt snippet if they expect it at the top. A hybrid pattern (short top snippet + full appendix snippet) works well across the broader template family.

### 2b.3) Appendix D enforcement (baseline) vs “checklist-only” enforcement (others)

Most templates rely on one or both of:
- A **Source Registry** table in the body.
- A **link validation checklist** that counts links and yields PASS/FAIL.

Those are necessary but not sufficient because they do not guarantee completeness without a canonical “all links go here” mechanism.

The baseline’s **Appendix X — Link Registry (Preserved from Discovery)** is the strongest enforcement because it:
- Defines a single place where *all canonical URLs* must be preserved.
- Requires per-link context (keywords + one sentence, or 1–2 sentences).
- Provides functional categorization (connectors/orchestration/storage/etc.).

### 2b.4) Important alignment point from A034 (link registry vs source registry)

Per `A034_Link_Preservation_Evidence_Sources_and_Model_Selection_Update_HANDOVER.md`:
- Appendix X is the **completeness/audit** mechanism.
- The same links should be surfaced where decisions are made: **Evidence → Source Registry**.

**Practical implication for next steps**:
- Other templates should gain an Appendix X audit mechanism, OR explicitly state an “exclusion log” pattern.
- Source Registry should contain 100% of Appendix X canonical URLs (or explicit exclusions with rationale).

---

### 2b.5) What other templates have that may be worth importing into the baseline

1. **Evidence Matrix (claims → source IDs)**
   - Present in many non-baseline templates.
   - Suggested import: a lightweight Evidence Matrix under “Evidence & Recommendations” that maps only the top ~5 claims/recommendations to Source IDs.

2. **Discovery Content Not Included appendix** (loss-prevention)
   - Present in `Research_3D_ConversionPipeline_Evaluation_template.md` and `Research_Strategic_Findings_light_template.md`.
   - Suggested import: add an optional appendix to capture “topics discovered but not included”, with links to discovery sections.

3. **Top-of-doc short prompt snippet** (author convenience)
   - Most templates include this near the top.
   - Suggested import: add a 2–4 line snippet at top that points to Appendix H for full prompt (keep Appendix H as the real contract).

4. **Explicit “Decision Ask” section** (when research is decision-driving)
   - Present in pipeline evaluation.
   - Suggested import: optional subsection under Evidence & Recommendations.

---

### 2b.6) Rollout checklist (what to adjust next in other templates)

**Priority 0 — Discovery frame enforcement (CRITICAL for preventing drift)**
- Port the **Pre-flight (Discovery frame check)** mechanism to all discovery-derived templates (Research Analysis, Strategic Guidance, Decision Support).
- This prevents the exact problem: research drifting into generic trends when discovery’s Initial Observations / Research Scope are not filled.
- Tooling support already exists: `Master_Rules/040_Framework_TOOLS/discovery_frame_checker.py`

**Priority 1 — Link preservation policy consistency**
- Add/standardize a “canonical link audit” appendix across discovery-derived templates (baseline already has it).
- Add the explicit A034 rule: Source Registry in the main body should include **100% of canonical URLs**.

**Priority 2 — Anti-drift controls where specs matter**
- Add a Deviation Log section (or equivalent) to any template intended for discovery → implementation flows.

**Priority 3 — Evidence matrices for decision-making templates**
- Ensure Decision Support / Planning templates consistently include an Evidence Matrix.

**Priority 4 — Optional narrative context**
- Add an optional “Narrative Context” block to templates that are commonly used from discovery material (Decision Support / Strategic Guidance), but don’t force full long-story requirements.

---

### 2b.7) Templates reviewed (active, non-archived)

Baseline:
- `Internal_Research_Analysis_template.md` — v2.3.0

Comparators (all v1.0.0):
- `External_Research_Analysis_template.md`
- `Internal_Strategic_Guidance_template.md`
- `External_Strategic_Guidance_template.md`
- `Internal_Decision_Support_template.md`
- `External_Decision_Support_template.md`
- `Internal_Requirements_Engineering_template.md`
- `External_Requirements_Engineering_template.md`
- `Internal_Implementation_Planning_template.md`
- `External_Implementation_Planning_template.md`
- `Documentation_HowTo_template.md`
- `Documentation_WhatWeDid_template.md`
- `Research_Strategic_Findings_light_template.md`
- `Research_3D_ConversionPipeline_Evaluation_template.md`

