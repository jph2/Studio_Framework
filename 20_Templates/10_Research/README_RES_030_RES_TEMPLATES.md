---
arys_schema_version: '1.2'
id: 279eb2e4-d702-4964-8151-a7946b450f7d
title: 🔬 General_Research Templates Directory
type: STRATEGIC
status: active
trust_level: 2
visibility: internal
created: '2026-02-18T05:33:26Z'
last_modified: '2026-02-18T05:33:26Z'
---

# 🔬 General_Research Templates Directory

**Version**: N/A | **Date**: 13.01.2026 | **Time**: 00:20 | **GlobalID**: 20260113_0020_General_Research_AUTO

**Status:** ✅ **TEMPLATE CONSOLIDATION COMPLETE** - All 12 templates implemented and integrated
**Purpose:** Consolidated template system - 5 core template pairs + 1 standalone category (internal/external) based on Strategic Findings architectural framework

**Tag block:**
#workflow_optimization #best_practices #case_study #workflow_automation #deterministic_workflows #analysis #framework_integration #quality_assurance

> **📋 WIP Section Available:** See [Work in Progress - Template A/B Testing](#-work-in-progress---template-ab-testing--storytelling-enhancement) at the end of this document for ongoing template experiments including storytelling enhancement and model selection testing.

---

## 🏗️ **Template Consolidation Strategy: 5 Core Template Pairs**

### **Executive Summary**

**NEW APPROACH:** Instead of maintaining 9+ specialized templates, we consolidate around **5 core template pairs + 1 standalone category** with parallel internal/external versions. All templates share the **Strategic Findings architectural framework** (numbered sections 1-9, component separation, conceptual vs. implementation distinction) while differing by audience focus and detail level.

**Key Changes:**
- ✅ **Consolidate** around Strategic Findings structure as foundation
- ✅ **Create 5 template pairs**: Strategic Guidance, Research Analysis, Decision Support, Requirements Engineering, Implementation Planning
- ✅ **Add 1 standalone category**: Documentation/Execution (existing templates)
- ✅ **Each pair has internal/external versions** (10 total new templates + 2 existing)
- ✅ **Deprecate** overly specialized templates (Evaluation_Comparison, Holistic_Research)
- ✅ **Cover full research-to-implementation workflow** including requirements engineering

**Benefits:**
- **Architectural consistency** across all templates
- **Complete workflow coverage** from research through implementation
- **Clear audience differentiation** (internal team vs. external stakeholders)
- **Downstream agent compatibility** (requirements and implementation agents)
- **Reduced maintenance burden** (12 focused templates vs. 9+ specialized ones)

---

## 📋 **Template Consolidation Plan**

### **Current Template Status**

| Template | Current Purpose | Status | Action |
|----------|----------------|--------|--------|
| `Research_Strategic_Findings_light_template.md` | Strategic guidance framework | ✅ **FOUNDATION** | Keep as architectural model for all new templates |
| `Documentation_HowTo_template.md` | Implementation guides | ✅ **KEEP** | Retain for practical documentation |
| `Documentation_WhatWeDid_template.md` | Retrospectives, postmortems | ✅ **KEEP** | Retain for execution documentation |
| `Research_3D_ConversionPipeline_Evaluation_template.md` | Pipeline evaluation | 🤔 **REVIEW** | May become specialized internal template |
| `MasterResearch_template.md` | Generic research papers | ❌ **ARCHIVED** | Moved to archive/ - usage redirected to Strategic Guidance templates |
| `Research_finding_template.md` | Single actionable findings | ❌ **ARCHIVED** | Moved to archive/ - enhanced as `Internal_Decision_Support_template.md` |
| `Research_Software_Implementation_Preparation_template.md` | Technical implementation prep | ❌ **ARCHIVED** | Moved to archive/ - enhanced as `Internal_Implementation_Planning_template.md` |
| `Research_Strategic_Guidance_template.md` | Strategic guidance | ❌ **ARCHIVED** | Moved to archive/ - replaced by Internal/External Strategic Guidance templates |
| `Software_Implementation_Plan_template.md` | Implementation planning | ❌ **ARCHIVED** | Moved to archive/ - replaced by Internal/External Implementation Planning templates |
| `Research_Holistic_Research_template.md` | Ecosystem mapping | ❌ **ARCHIVED** | Moved to archive/ - functionality integrated into Strategic Guidance templates |
| `Research_Evaluation_Comparison_template.md` | Comparative evaluations | ❌ **ARCHIVED** | Moved to archive/ - comparisons handled in Strategic Guidance templates |

### **New Template Architecture: 5 Core Pairs + 1 Standalone Category**

| Template Category | Internal Version | External Version | Shared Structure | Workflow Position |
|-------------------|------------------|------------------|-----------------|------------------|
| **Strategic Guidance** | `Internal_Strategic_Guidance_template.md` | `External_Strategic_Guidance_template.md` | Strategic Findings framework (sections 1-9) | 1. Research → Strategic Direction |
| **Research Analysis** | `Internal_Research_Analysis_template.md` | `External_Research_Analysis_template.md` | Strategic Findings framework | 2. Research → Analysis & Synthesis |
| **Decision Support** | `Internal_Decision_Support_template.md` | `External_Decision_Support_template.md` | Strategic Findings framework | 3. Any Stage → Decision Making |
| **Documentation/Execution** | `Documentation_HowTo_template.md` | `Documentation_WhatWeDid_template.md` | Standalone templates | 4. Any Stage → Documentation |
| **Requirements Engineering** | `Internal_Requirements_Engineering_template.md` | `External_Requirements_Engineering_template.md` | Requirements-focused structure | 5. Research → Requirements Definition |
| **Implementation Planning** | `Internal_Implementation_Planning_template.md` | `External_Implementation_Planning_template.md` | Implementation-focused structure | 6. Requirements → Technical Planning |

---

## 🏗️ **Strategic Findings Framework: Foundation for All Templates**

### **Why Strategic Findings is the Foundation**

The `Research_Strategic_Findings_light_template.md` provides the **architectural framework** for all new templates because:

- **Clear progression**: Numbered sections (1-9) provide predictable flow
- **Component separation**: Clean distinction between conceptual models and implementation details
- **Integration thinking**: Shows how components work together
- **Audience adaptability**: Same structure works for internal teams and external stakeholders
- **Downstream agent compatibility**: Clear architectural boundaries enable automated processing

### **Template Category Specifications**

#### 1. **Strategic Guidance Pair** (Foundation - Priority 1)
**Purpose:** Architectural insights and strategic direction
**Internal Version:** `Internal_Strategic_Guidance_template.md` (300-400 lines)
- Focus: Implementation architecture, technical decisions, team workflows
- Audience: Technical leads, architects, development teams

**External Version:** `External_Strategic_Guidance_template.md` (400-500 lines)
- Focus: Business value, stakeholder alignment, governance
- Audience: Leadership, executives, external stakeholders

#### 2. **Research Analysis Pair** (Priority 2)
**Purpose:** Comprehensive research synthesis and analysis
**Internal Version:** `Internal_Research_Analysis_template.md` (250-350 lines)
- Focus: Technical findings, implementation implications, team insights

**External Version:** `External_Research_Analysis_template.md` (350-450 lines)
- Focus: Business impact, market analysis, stakeholder implications

**Discovery-derived research (drift prevention):**
- If the source is a `*_DISCOVERY.md` and **Initial Observations / Preliminary Findings** and/or **Research Scope** are not filled (still contain placeholders), generated research may drift into generic trends.
- Templates include a small **Quality Note (Scope/Frame)** to surface this risk and recommend filling those discovery sections before re-running.
- Optional tooling (warn-only): `Master_Rules/040_Framework_TOOLS/discovery_frame_checker.py`

#### 3. **Decision Support Pair** (Priority 5)
**Purpose:** Focused decision-making and recommendations
**Internal Version:** `Internal_Decision_Support_template.md` (150-250 lines)
- Focus: Technical decisions, implementation choices, team recommendations

**External Version:** `External_Decision_Support_template.md` (250-350 lines)
- Focus: Business decisions, strategic choices, stakeholder recommendations

#### 4. **Documentation/Execution Category** (Standalone - Priority N/A)
**Purpose:** Practical documentation and execution tracking
**Templates:**
- `Documentation_HowTo_template.md` - Step-by-step implementation guides
- `Documentation_WhatWeDid_template.md` - Retrospectives and execution tracking
- **Note:** These are standalone templates, not internal/external pairs

#### 5. **Requirements Engineering Pair** (Priority 3)
**Purpose:** Structured requirements definition and specification
**Internal Version:** `Internal_Requirements_Engineering_template.md` (200-300 lines)
- Focus: Functional requirements, technical specifications, acceptance criteria
- Structure: Requirements breakdown, validation criteria, traceability

**External Version:** `External_Requirements_Engineering_template.md` (300-400 lines)
- Focus: Business requirements, stakeholder needs, contractual specifications
- Structure: Stakeholder requirements, business rules, compliance requirements

#### 6. **Implementation Planning Pair** (Priority 4)
**Purpose:** Technical implementation roadmaps and planning
**Internal Version:** `Internal_Implementation_Planning_template.md` (250-350 lines)
- Focus: Technical architecture, development phases, team assignments

**External Version:** `External_Implementation_Planning_template.md` (350-450 lines)
- Focus: Project planning, resource allocation, stakeholder management

---

## 🔄 **Template Consolidation Benefits**

### **Architectural Advantages**
- **Consistent Structure**: All templates use Strategic Findings numbered sections (1-9)
- **Component Thinking**: Clear separation of concerns across all templates
- **Integration Focus**: Shows how components work together for downstream agents
- **Scalable Design**: Same framework adapts to different audiences and scopes

### **Audience Differentiation**
| Aspect | Internal Templates | External Templates |
|--------|-------------------|-------------------|
| **Focus** | Implementation details, technical decisions | Business value, strategic alignment |
| **Length** | 150-400 lines | 250-500 lines |
| **Sections** | More technical depth, code examples | More business context, ROI analysis |
| **Evidence** | Technical validation, proof-of-concepts | Stakeholder benefits, market analysis |
| **Next Steps** | Implementation tasks, team assignments | Governance decisions, budget approvals |

### **Downstream Agent Compatibility**
- **Requirements Agents**: Can extract from "Implementation Patterns" sections
- **Implementation Agents**: Can use "Refined Contract Stack" as technical foundation
- **Quality Agents**: Clear architectural boundaries enable automated validation
- **Decision Agents**: Consistent "Decision Ask" sections across all templates

### **Maintenance Simplification**
- **Reduced Complexity**: 10 focused templates vs. 9+ specialized ones
- **Shared Structure**: Strategic Findings framework reduces maintenance overhead
- **Version Consistency**: All templates use same architectural foundation
- **Update Efficiency**: Changes to core structure benefit all templates

---

## 📋 **Implementation Roadmap: 6 Template Categories**

### **Phase 1: Strategic Guidance Pair** (Priority: CRITICAL - ✅ COMPLETE)
**Status:** ✅ **COMPLETE** - Strategic Guidance templates created and archived deprecated templates
1. ✅ **Document Strategic Findings structure** (sections 1-9 framework)
2. ✅ **Create `Internal_Strategic_Guidance_template.md`** (300-400 lines)
   - Adapt Strategic Findings for internal team implementation
   - Focus: Technical architecture, implementation decisions, team workflows
3. ✅ **Create `External_Strategic_Guidance_template.md`** (400-500 lines)
   - Adapt Strategic Findings for external stakeholder governance
   - Focus: Business value, strategic alignment, leadership decisions
4. ⏳ **Test with SecondBrain example** - validate downstream agent compatibility (pending)

### **Phase 2: Research Analysis Pair** (Priority: HIGH)
1. **Create `Internal_Research_Analysis_template.md`** (250-350 lines)
   - Internal-focused research synthesis and technical findings
2. **Create `External_Research_Analysis_template.md`** (350-450 lines)
   - External-focused research with business impact and stakeholder implications

### **Phase 3: Decision Support Pair** (Priority: MEDIUM - ✅ COMPLETE)
**Status:** ✅ **COMPLETE** - Both templates created and validated
1. **Enhanced existing template**:
   - `Research_finding_template.md` → `Internal_Decision_Support_template.md`
   - Added Strategic Findings structure overlay for technical decision support
2. **Created new template**:
   - `External_Decision_Support_template.md` (320+ lines)
   - Business decisions, strategic choices, stakeholder recommendations for executive audiences

### **Phase 4: Documentation/Execution Category** (Priority: LOW - Already Complete)
**Status:** ✅ **COMPLETE** - Existing standalone templates
- `Documentation_HowTo_template.md` - Already available for implementation guides
- `Documentation_WhatWeDid_template.md` - Already available for retrospectives
- **Action:** No creation needed, templates already exist and are functional

### **Phase 5: Requirements Engineering Pair** (Priority: HIGH - ✅ COMPLETE)
**Status:** ✅ **COMPLETE** - Both templates created and validated
1. **Created `Internal_Requirements_Engineering_template.md`** (250+ lines)
   - Functional requirements, technical specifications, acceptance criteria for internal teams
   - Structure: Requirements breakdown, validation criteria, traceability matrix
2. **Created `External_Requirements_Engineering_template.md`** (350+ lines)
   - Business requirements, stakeholder needs, contractual specifications for external governance
   - Structure: Stakeholder requirements, business rules, compliance requirements

### **Phase 6: Implementation Planning Pair** (Priority: HIGH - ✅ COMPLETE)
**Status:** ✅ **COMPLETE** - Both templates created and validated
1. **Enhanced existing template**:
   - `Research_Software_Implementation_Preparation_template.md` → `Internal_Implementation_Planning_template.md`
   - Added Strategic Findings structure and comprehensive requirements integration
2. **Created new template**:
   - `External_Implementation_Planning_template.md` (400+ lines)
   - Project planning, resource allocation, ROI analysis, governance frameworks for external stakeholders

### **Phase 7: Framework Integration & Migration** (Priority: MEDIUM - ✅ COMPLETE)
**Status:** ✅ **COMPLETE** - Framework integration and migration finished
1. **Updated `research_configuration_rules.yml`** ✅
   - Added all 10 new template profiles with Strategic Findings architecture
   - Updated routing logic for internal/external selection
2. **Created template selection decision tree** ✅
   - Clear internal vs external criteria implemented
   - Audience-based routing with improved decision factors table
3. **Migrated existing usage** ✅
   - Deprecated specialized templates moved to archive/ (Holistic_Research, Evaluation_Comparison)
   - MasterResearch usage redirected to Strategic Guidance templates
   - Framework guides updated with new template system

---

## 🎯 **Template Selection Decision Tree**

```
START: What type of content are you creating?

├── A. STRATEGIC GUIDANCE (architecture, direction, governance)
│   ├── Internal team focus (technical implementation, team execution)
│   │   └── Use: Internal_Strategic_Guidance_template.md
│   └── External stakeholder focus (business value, organizational impact)
│       └── Use: External_Strategic_Guidance_template.md
│
├── B. RESEARCH ANALYSIS (synthesis, findings, evaluation)
│   ├── Internal team focus (technical implications, implementation insights)
│   │   └── Use: Internal_Research_Analysis_template.md
│   └── External stakeholder focus (market implications, strategic insights)
│       └── Use: External_Research_Analysis_template.md
│
├── C. DECISION SUPPORT (recommendations, choices, next steps)
│   ├── Internal team focus (technical options, implementation decisions)
│   │   └── Use: Internal_Decision_Support_template.md
│   └── External stakeholder focus (strategic choices, stakeholder alignment)
│       └── Use: External_Decision_Support_template.md
│
├── D. DOCUMENTATION/EXECUTION (how-to, retrospectives, standalone)
│   ├── How-to guides & tutorials
│   │   └── Use: Documentation_HowTo_template.md
│   └── Implementation retrospectives ("what we did")
│       └── Use: Documentation_WhatWeDid_template.md
│
├── E. REQUIREMENTS ENGINEERING (requirements definition, specifications)
│   ├── Internal team focus (functional specs, acceptance criteria)
│   │   └── Use: Internal_Requirements_Engineering_template.md
│   └── External stakeholder focus (business needs, contractual specs)
│       └── Use: External_Requirements_Engineering_template.md
│
└── F. IMPLEMENTATION PLANNING (roadmaps, resource allocation, execution)
    ├── Internal team focus (technical roadmaps, development planning)
    │   └── Use: Internal_Implementation_Planning_template.md
    └── External stakeholder focus (project planning, ROI analysis, governance)
        └── Use: External_Implementation_Planning_template.md
```

### **Audience Determination Guide**

**Choose INTERNAL templates if your primary audience is:**
- Development teams, technical leads, architects, implementers
- Focus on technical implementation, code-level decisions, development processes
- Need detailed technical specifications, architecture decisions, implementation guidance
- Success measured by technical deliverables and quality metrics

**Choose EXTERNAL templates if your primary audience is:**
- Executive leadership, board members, external partners, strategic decision-makers
- Focus on business value, strategic alignment, organizational impact, ROI justification
- Need business case justification, stakeholder communication, governance frameworks
- Success measured by business outcomes and organizational impact

**Key Decision Factors:**
| Factor | Internal Focus | External Focus |
|--------|---------------|----------------|
| **Depth** | Technical details, implementation specifics | Business implications, strategic overview |
| **Language** | Technical terminology, code examples | Business terminology, ROI analysis |
| **Timeline** | Development sprints, implementation phases | Strategic planning, organizational change |
| **Success** | Technical quality, system performance | Business value, stakeholder satisfaction |
| **Risks** | Technical failures, integration issues | Strategic misalignment, organizational resistance |
| **Evidence** | Technical validation, proof-of-concepts | Business case, stakeholder impact analysis |

---

## 📊 **Success Metrics & Validation**

| Metric | Target | Current Status | Measurement Method |
|--------|--------|----------------|-------------------|
| **Template Consolidation** | 10 core templates implemented + 2 standalone | ✅ 10/10 + 2/2 (all phases complete) | Template creation completion |
| **Architectural Consistency** | 100% use Strategic Findings framework | ✅ 10/10 (all templates) | Structure validation |
| **Audience Differentiation** | Clear internal vs external focus | ✅ Implemented | User feedback on template selection |
| **Downstream Agent Compatibility** | Requirements/implementation agents can process all templates | ✅ Framework ready | Agent integration testing |
| **Maintenance Efficiency** | <50% maintenance overhead vs. current 9+ templates | ✅ Consolidated to 12 templates | Template update tracking |
| **Link Preservation Rate** | 100% across all templates | ✅ 100% | Automated validation via `link_validation.py` |
| **Template Selection Accuracy** | >90% correct template selection | ✅ Decision tree implemented | User feedback surveys |
| **Framework Integration** | All templates in configuration rules | ✅ Complete | Configuration validation |

---

## 🔗 **Framework Integration Requirements**

### **Agent Routing Updates**
- Add internal/external selection gate in research agent routing
- Update template profile mappings in `research_configuration_rules.yml`
- Integrate with existing link validation system

### **Quality Assurance**
- All templates must pass link validation (100% preservation)
- Template usage tracked via framework analytics
- Regular review of template effectiveness

### **Documentation Updates**
- Update `AGENTS_Research.md` with internal/external selection guidance
- Update framework guides to reference new template categories
- Create template selection quick reference

---

## 🚀 **Immediate Next Steps**

### **Phase 1: Strategic Guidance Pair** (Start Today - HIGHEST PRIORITY)
1. **Document Strategic Findings framework** (sections 1-9 structure)
   - Create detailed specification of the architectural framework
   - Document component separation patterns
   - Define internal vs external adaptation guidelines

2. **Create `Internal_Strategic_Guidance_template.md`** (300-400 lines)
   - Adapt Strategic Findings structure for internal team implementation
   - Focus: Technical architecture, implementation decisions, team workflows
   - Test with SecondBrain example for downstream agent compatibility

3. **Create `External_Strategic_Guidance_template.md`** (400-500 lines)
   - Adapt Strategic Findings structure for external stakeholder governance
   - Focus: Business value, strategic alignment, leadership decisions
   - Include ROI analysis and stakeholder communication elements

4. **Framework Integration**
   - Add Strategic Guidance template profiles to `research_configuration_rules.yml`
   - Update agent routing to include internal/external selection

### **Phase 2: Research Analysis Pair** (Priority: HIGH - ✅ COMPLETE)
**Status:** ✅ **COMPLETE** - Research Analysis templates created and integrated
1. ✅ Create `Internal_Research_Analysis_template.md` (250-350 lines)
   - Internal-focused research synthesis and technical findings
2. ✅ Create `External_Research_Analysis_template.md` (350-450 lines)
   - External-focused research with business impact and stakeholder implications
3. ⏳ Test with existing research documents and validate downstream agent processing (pending)

### **Phase 3: Decision Support Pair** (Medium Priority)
1. Enhance existing templates for internal version
2. Create external version for stakeholder decisions
3. Test across different workflow stages

### **Phase 4: Requirements Engineering Pair** (High Priority - Workflow Critical)
1. Create `Internal_Requirements_Engineering_template.md` (200-300 lines)
   - Functional requirements, technical specifications, acceptance criteria
   - Include traceability matrix and validation criteria
2. Create `External_Requirements_Engineering_template.md` (300-400 lines)
   - Business requirements, stakeholder needs, contractual specifications
   - Include compliance requirements and stakeholder sign-off processes

### **Phase 5: Implementation Planning Pair** (High Priority - Workflow Critical)
1. Enhance existing templates:
   - `Research_Software_Implementation_Preparation_template.md` → `Internal_Implementation_Planning_template.md`
   - Add structured requirements integration and technical roadmap
2. Create `External_Implementation_Planning_template.md` (350-450 lines)
   - Project planning, resource allocation, stakeholder management
   - Include ROI analysis and governance considerations

### **Phase 6: Framework Integration & Migration** (Medium Priority)

---

## 📚 **Template Development Standards**

### **Internal Template Standards**
- **Length:** 150-300 lines (concise, actionable)
- **Audience:** Technical teams, implementers
- **Focus:** Workflow integration, implementation planning
- **Sections:** Actionable insights, decision points, next steps
- **Evidence:** Essential sources only, practical focus

### **External Template Standards**
- **Length:** 400+ lines (comprehensive, formal)
- **Audience:** Stakeholders, leadership, decision-makers
- **Focus:** Complete analysis, strategic recommendations
- **Sections:** Executive summary, detailed analysis, formal recommendations
- **Evidence:** Extensive source registry, comprehensive validation

### **All Templates Must Include**
- ✅ Framework header with GlobalID
- ✅ Template traceability section
- ✅ Link validation checklist (Appendix D)
- ✅ Agent routing integration
- ✅ Cross-template references where applicable

---

## 🔍 **Research Context & Heritage**

**Source Analysis:**
- SecondBrain discovery (1999 lines) → research conversion (439 lines) demonstrated template mismatch
- Link validation system identified 88 missing links (11.4% preservation rate)
- Framework workflow analysis revealed need for internal team-focused templates

**Key Insights:**
- Strategic Findings architectural framework provides superior structure for both internal and external use
- Consolidation reduces maintenance overhead while improving consistency
- Internal/external differentiation enables better audience targeting
- Link preservation remains critical (enforced by validation system)
- Template selection based on content type + audience (5 types × 2 audiences = 10 templates)

**Framework Integration:**
- Templates align with 4-gate routing system (G006_Framework_Workflow_User_GUIDE.md)
- Agent specialization supports internal/external template selection
- Quality assurance includes link validation and architectural consistency
- Downstream agents (requirements, implementation) benefit from consistent Strategic Findings structure

---

## 📋 **Template Maintenance & Evolution**

### **Regular Reviews**
- Quarterly template effectiveness assessment
- User feedback integration
- Framework evolution alignment
- Link validation system updates

### **Version Control**
- Semantic versioning for templates
- Change tracking in template headers
- Backward compatibility maintenance
- Migration path documentation

### **Quality Assurance**
- Automated link validation on all templates
- Template usage analytics
- User satisfaction surveys
- Framework compliance checking

---

**Version History:**
- **v3.0.0** (2026-01-10): Phase 7 COMPLETE - Framework Integration & Migration finished. All 12 templates integrated into research_configuration_rules.yml, template selection decision tree implemented, deprecated templates archived. Template consolidation project COMPLETE.
- **v2.8.0** (2026-01-10): Phase 6 COMPLETE - Implementation Planning templates created (10/10 core templates + 2 standalone = 12 total templates complete)
- **v2.7.0** (2026-01-10): Phase 5 COMPLETE - Requirements Engineering templates created (8/10 total templates complete)
- **v2.6.0** (2026-01-10): Phase 4 COMPLETE - Decision Support templates created (6/10 total templates complete)
- **v2.5.0** (2026-01-10): Phase 3 COMPLETE - Research Analysis templates created (4/10 total templates complete)
- **v2.4.0** (2026-01-10): Phase 2 COMPLETE - Strategic Guidance templates created, deprecated templates archived (2/10 total templates complete)
- **v2.3.0** (2026-01-10): Added Documentation/Execution as standalone category - now 6 total categories (5 pairs + 1 standalone) for complete template coverage
- **v2.2.0** (2026-01-10): Major restructuring - consolidated around 5 core template pairs using Strategic Findings architectural framework
- **v2.1.0** (2026-01-10): Initial restructuring analysis, gap identification, implementation roadmap
- **v2.0.0** (2026-01-09): Link validation system integration, template categorization framework
- **v1.0.0** (2025-12-13): Initial template collection

**Next Update:** After Strategic Guidance template pair creation and framework integration testing.

---

## 🧪 Work in Progress - Template A/B Testing & Storytelling Enhancement

> **Status:** 🔄 Iteration In Progress (Phase 5) | ✅ A/B runs A–F complete
> **Started:** January 10, 2026
> **Purpose:** Validate storytelling template enhancements with different LLM models

---

### Problem Statement

Template synthesis from Discovery → Research lost critical content:
- **Narrative storytelling** stripped by code-optimized models
- **Numbered building blocks** (e.g., "8 steps") abstracted away
- **Implementation details** lost during synthesis
- **Model selection** affects output quality regardless of template

**Root Cause Analysis:**
- 70% model selection (code-optimized model stripped narrative)
- 30% template design (didn't explicitly protect narrative content)

**Key Insight from SecondBrain_Memex case study:**
> ChatGPT 5.2 preserved both narrative AND technical content in Discovery.
> GrokCode stripped narrative during Research synthesis, keeping only structure.
> The template didn't ask for narrative, but even if it had, a code-optimized model may not deliver it.

See: `Master_Rules/010_Framework_GUIDES/G007_Model_Selection_GUIDE.md` for model selection guidance.

---

### A/B Test Plan: SecondBrain_Memex Research Rewrite

**Objective:** Test the updated `Internal_Research_Analysis_template.md` (v2.0.0 with storytelling) across different LLM models to validate template effectiveness.

**Source Material:**
- `SecondBrain_Memex_DISCOVERY.md` - The full discovery conversation (test fixture)
- `Internal_Research_Analysis_template.md` (v2.0.0) - Updated with storytelling requirements (template under test)

**Test Artifacts Location:** `Master_Rules/010_Framework_GUIDES/QualityAssementTEST_TEMPLATEandLLM_260111/`

> **Note (migration history):** 
> 1. All A/B test artifacts were initially stored under `General_Research/070_Proj_RESEARCH/02_Research_WIP/`
> 2. Moved to `General_Research/030_Proj_TEMPLATES/QualityAssementTEST_TEMPLATEandLLM_260111/` to live alongside templates
> 3. **Final location:** `Master_Rules/010_Framework_GUIDES/QualityAssementTEST_TEMPLATEandLLM_260111/` - Moved to framework guides as this evaluation validates framework-level concerns (model selection, template quality) that affect all domains, not just research templates. This evaluation bundle is a companion to `G007_Model_Selection_GUIDE.md`.

#### Evaluation Matrix (A/B Test Evaluators)

| Version | Model | Context | Agent Files | Status |
|---------|-------|---------|-------------|--------|
| **A** | Claude Opus 4.5 | Full context from this conversation | Full framework understanding | ✅ Complete |
| **B** | Claude Opus 4.5 (clean) | No prior context | AGENTS.md + AGENTS_Research.md + Template | ✅ Complete |
| **C** | ChatGPT 5.2 (clean) | No prior context | AGENTS.md + AGENTS_Research.md + Template | ✅ Complete |
| **D** | ChatGPT 5.2 (clean) | No prior context | Online + Template | ✅ Complete |
| **E** | Composer 1 (clean) | No prior context | AGENTS.md + AGENTS_Research.md + Template | ✅ Complete |
| **F** | GrokCode (clean) | No prior context | AGENTS.md + AGENTS_Research.md + Template | ✅ Complete |

**Evaluator Outputs (stored in `Master_Rules/010_Framework_GUIDES/QualityAssementTEST_TEMPLATEandLLM_260111/`):**
- **A**: `SecondBrain_Memex_AB_COMPARE_A.md` (qualitative/manual comparison narrative)
- **B**: `SecondBrain_Memex_AB_COMPARE_B.md` + `SecondBrain_Memex_AB_COMPARE_B__research_comparison_*` (scripted scoring + link stats)
- **C**: `SecondBrain_Memex_AB_COMPARE_C.md` + `SecondBrain_Memex_AB_COMPARE_C__*` (discovery→research retention evaluation: links + spec markers)
- **D**: `SecondBrain_Memex_AB_COMPARE_D.md` (weighted scoring focus: link fidelity + buildability + numeric fidelity + hygiene)
- **E**: `SecondBrain_Memex_AB_COMPARE_E.md` + `SecondBrain_Memex_AB_COMPARE_E__research_comparison_*` (scripted scoring variant)
- **F**: `SecondBrain_Memex_AB_COMPARE_F.md` + `SecondBrain_Memex_AB_COMPARE_F__link_*` (link-preservation deep dive + script)

#### Research Candidates Under Evaluation (Generated Outputs)

These are the research outputs being evaluated by A–F (stored in `QualityAssementTEST_TEMPLATEandLLM_260111/`):
- `SecondBrain_Memex_RESEARCH_AB_V01.md`
- `SecondBrain_Memex_RESEARCH_AB_V02.md`
- `SecondBrain_Memex_RESEARCH_AB_V03.md`
- `SecondBrain_Memex_RESEARCH_AB_V03.1.md`
- `SecondBrain_Memex_RESEARCH_AB_V04.md`
- `SecondBrain_Memex_RESEARCH_AB_V05.md`

#### Test Protocol

**For V01 (Full Context):**
- Use current agent session with full project understanding
- Rewrite research with storytelling template

**For V02-V05 (Clean Sessions):**
1. Start new, clean agent session (no prior context)
2. Provide only:
   - `AGENTS.md` (universal baseline)
   - `AGENTS_Research.md` (research agent)
   - `Internal_Research_Analysis_template.md` (v2.0.0)
   - `SecondBrain_Memex_DISCOVERY.md` (source)
3. Prompt:
   ```
   Using the attached template and discovery document, create a research 
   document following the template structure. Focus on:
   1. Writing an engaging Executive Summary (short story, 150-300 words)
   2. Writing a compelling Deep Dive (long story, 800-1500 words)
   3. Preserving all numbered blocks (8 building blocks, 12 principles)
   4. Preserving all specific numbers and implementation details
   5. Preserving all links from the discovery document
   ```
4. Save output as `SecondBrain_Memex_RESEARCH_AB_V0X.md`

#### Evaluation Metrics (Current Snapshot)

Key quantitative metrics now exist in evaluator reports **B**, **C**, **D**, **E**, and **F**. (See the evaluator output files listed above.)

**From scripted scoring reports (B/E) — content-oriented scoring (Max 100):**
- **Best overall (tie at 89.5/100)**: V04 and V02
- Category scores include: Building Blocks, Principles, Key Numbers, Tech Stack, Schemas, Links

**From retention reports (B/C/D) — link preservation (canonical links in discovery):**
- Discovery canonical URLs baseline (reported): **87**
- **Best link preservation**: **V03 = 87/87 (100%)**
- **V03.1**: **50/87 (57.5%)**

**From weighted consistency report (D):**
- **Best overall (weighted)**: **V03 = 0.850**
- Notes include template hygiene penalties for leakage (e.g., severe leakage flagged in V04)

#### Artifacts Inventory (Scripts / Data Produced During Testing)

All artifacts are stored under: `General_Research/030_Proj_TEMPLATES/QualityAssementTEST_TEMPLATEandLLM_260111/`

| Evaluator | Scripts / Data Artifacts |
|----------|---------------------------|
| **A** | *(none; qualitative/manual markdown only)* |
| **B** | `SecondBrain_Memex_AB_COMPARE_B__research_comparison_analyzer.py`, `SecondBrain_Memex_AB_COMPARE_B__research_comparison_data.json`, `SecondBrain_Memex_AB_COMPARE_B__research_comparison_report.md` |
| **C** | `SecondBrain_Memex_AB_COMPARE_C__ab_discovery_research_compare.py`, `SecondBrain_Memex_AB_COMPARE_C__research_comparison_data.json` |
| **D** | *(none; markdown evaluation)* |
| **E** | `SecondBrain_Memex_AB_COMPARE_E__research_comparison_analyzer.py`, `SecondBrain_Memex_AB_COMPARE_E__research_comparison_data.json`, `SecondBrain_Memex_AB_COMPARE_E__research_comparison_report.md` |
| **F** | `SecondBrain_Memex_AB_COMPARE_F__link_analysis_script.py`, `SecondBrain_Memex_AB_COMPARE_F__link_preservation_analysis.md` |

---

### Full Plan Document (Preserved for Reference)

<details>
<summary>📋 Click to expand: Research Template Storytelling and Content Preservation Enhancement Plan</summary>

#### Overview

**Problem**: Template synthesis from Discovery → Research lost narrative storytelling and implementation details.

**Solution**: Update templates with explicit storytelling requirements and content preservation rules, then A/B test with different models.

#### Two Angles to Address

**Angle 1: Template Creation**
- Analyze what was lost between discovery, research, and critique
- Use the critique as a second opinion
- Create templates that produce better research content with narrative appeal

**Angle 2: Rewrite the Research**
- Use the improved templates to rewrite `SecondBrain_Memex_RESEARCH.md`
- Apply storytelling principles to make it engaging and understandable

#### Phase Summary

| Phase | Description | Status |
|-------|-------------|--------|
| Phase 1 | Gap Analysis - identify what was lost | ✅ Complete |
| Phase 2 | Template Design - storytelling structure | ✅ Complete |
| Phase 3 | Update Template - implement changes | ✅ Complete |
| Phase 4 | A/B Testing - test with different models | ✅ Complete |
| Phase 5 | Iterate - refine based on results | 🔄 In Progress |
| Phase 6 | Rollout - apply to all templates | ⏳ Pending |

#### Phase 1: Gap Analysis (✅ Complete)

**What was lost between Discovery (1999 lines) and Research (407 lines):**

1. **Narrative Storytelling** - The emotional "why" and human experience
2. **8 Building Blocks** - Named concepts with memorable metaphors
3. **12 Engineering Principles** - Numbered guidelines with examples
4. **Implementation Specifications** - Field definitions, thresholds (0.6), word limits (150/250)
5. **Portable Core / Anti-Lock-In** - Swappability matrix, backup/restore
6. **Links and References** - 30+ curated URLs to documentation

**Gap Analysis Document:** `Master_Rules/010_Framework_GUIDES/QualityAssementTEST_TEMPLATEandLLM_260111/SecondBrain_Memex_GAP_ANALYSIS.md`

#### Phase 2-3: Template Design & Update (✅ Complete)

Updated `Internal_Research_Analysis_template.md` (v2.0.0) with:

- **Executive Summary (Short Story)** - 150-300 words, narrative hook
- **Deep Dive (Long Story)** - 800-1500 words, journey through discovery
- **Building Blocks / Key Concepts** - Numbered list with names
- **Principles / Design Guidelines** - Numbered list with examples
- **Implementation Specifications** - Exact schemas, numbers, thresholds
- **Portability & Anti-Lock-In** - Swappability matrix, backup/restore
- **Links & References** - With actual URLs
- **Discovery Reference** - Link to source with line numbers

#### Phase 4: A/B Testing (✅ Complete)

See Evaluation Matrix above.

#### Phase 5: Iterate Based on Results (🔄 In Progress)

1. Compare outputs from different LLM models
2. Identify which model produced the best storytelling quality
3. Identify common issues across all outputs
4. Refine template instructions based on what worked/didn't work
5. Select best output to become final `SecondBrain_Memex_RESEARCH.md`

#### Phase 6: Rollout to All Templates (⏳ Pending)

After validation, apply storytelling structure to all 14 active templates.

#### Success Criteria

**Storytelling Quality:**
- Executive Summary is engaging and makes readers want to continue
- Deep Dive tells a compelling story with narrative flow
- Readers understand "what this is about" in the first 2 minutes
- The "why" behind decisions is clear

**Content Preservation:**
- All schemas and contracts preserved exactly
- Numbered blocks preserved in order (e.g., "8 steps", "5 principles")
- MVP/core definitions documented
- 100% link preservation

</details>

---

### Related Documents

- `Master_Rules/010_Framework_GUIDES/QualityAssementTEST_TEMPLATEandLLM_260111/SecondBrain_Memex_DISCOVERY.md` - Source material for A/B testing
- `Master_Rules/010_Framework_GUIDES/QualityAssementTEST_TEMPLATEandLLM_260111/SecondBrain_Memex_GAP_ANALYSIS.md` - Gap analysis identifying what was lost
- `Internal_Research_Analysis_template.md` (v2.0.0) - Updated template with storytelling
- `Master_Rules/010_Framework_GUIDES/G007_Model_Selection_GUIDE.md` - Model selection guidance

---

**WIP Section Added:** January 10, 2026
**Last Updated:** 11.01.2026
