---
arys_schema_version: '1.2'
id: 1c71bd55-2c26-4fd1-8818-46fd973c6ec3
title: Tag Governance Audit — Research WIP & Master Tag System
type: GOVERNANCE
status: active
trust_level: 3
visibility: internal
created: '2026-02-18T05:33:26Z'
last_modified: '2026-02-18T05:33:26Z'
---

# Tag Governance Audit — Research WIP & Master Tag System

**Version**: 1.0 | **Date**: 16.02.2026 | **Time**: 12:00 | **GlobalID**: 20260216_1200_General_Research_TAG_AUDIT
**Tag block:**
#framework_integration #best_practices #governance #conversion #openusd #aas_integration #catia #simulation #usd_core #omniverse #digital_twin #digital_twin_creation #workflow_automation #deterministic_workflows #analysis #case_study #workflow_optimization #export #materialx #materials

---

## 1. Research WIP — Topic Inventory

**Source**: `General_Research/070_Proj_RESEARCH/02_Research_WIP/` (incl. subdirs)  
**Total files**: 100

### 1.1 Topics inferred from filenames (grouped)

| Topic cluster | Files (sample) | Master tag coverage |
|---------------|----------------|---------------------|
| **AAS / Asset Administration Shell** | AAC_Asset Administration Shell and OpenUSD, IHEP_digital_twin_discovery | `aas_integration` ✓ |
| **CATIA / 3DXML / 3DX** | 3DX_CATIA_SiemensPlantSimulation, 3DX_Catia_3DXMLto DIGITAL TWIN, 3DX_Breakout_ETL | `catia` ✓ |
| **Plant Simulation / Siemens** | 3DX_CATIA_SiemensPlantSimulation, NVIDIA_SIEMENS_DigitalTwinComposer | `plant_simulation` ✓ |
| **Catena-X** | Catena-X_DISCOVERY, Catena-X__RESEARCH | `catena_x` ✓ |
| **Digital Twin** | DigitalTwin_IOT_Begriffsliste, Munich_Urban_Digital_TWIN_OGC, IHEP_digital_twin | `digital_twin`, `digital_twin_creation` ✓ |
| **Gaussian Splatting** | Gaussian Splatting Workflows | `gaussian_splatting` ✓ |
| **Agent / AI ecosystem** | Agent_Ecosystem_Tools, Agent_Rules_Update, General AI-AGENT Framework | `agent_orchestration`, `multi_agent_systems` ✓ |
| **OpenClaw / Soul / Skills** | OpenClaw_Soul-Skils_DISCOVERY | `openclaw`, `skills` ✓ |
| **Memex / Second Brain** | SecondBrain_Memex, Circular_Economy_Botrop | `memex`, `second_brain_system` ✓ |
| **Cursor / Codex / IDE** | Cursor_withLocal_AI, Codex CLI Integration, LinkList_Cursor_Docs | `cursor` ✓ |
| **ComfyUI / NVIDIA Cosmos / Replicator** | (in OpenUSD_GoodStart_ComfyUI_nodes) | `comfyui`, `nvidia_cosmos`, `nvidia_replicator` ✓ |
| **MaterialX** | MaterialX_nodegraphIntegration, MaterialX_GraphEditor_Extension | `materials` (partial) — **gap** |
| **ETL / Data pipeline** | ETL in OpenUSD, 3DX_Breakout_ETL | `conversion`, `file_processing` (partial) — **gap** |
| **WRAPP / Packaging** | WRAPP_Workflow Reproducible Asset Packaging | `packaging`, `distribution` ✓ |
| **Blender / C4D / Rhino** | Blender_USD_FAKE_References, C4D to USD pipeline | `export`, `conversion` — **no DCC tags** |
| **Omniverse / LED Dome / Sequencer** | LED Dome_Mukaab_OMNIVERSE, Omniverse_Sequenzer_Camera_Animation | `omniverse`, `sequencer`, `camera_management` ✓ |
| **BREV / Launchable** | Setting up BREV with Launchable | — **gap** (cloud/GPU compute) |
| **Sphinx** | Sphinx Setup | — **gap** (documentation tooling) |
| **Walrus DataViz** | Walrus_DataViz | — **gap** (data viz) |
| **WebRTC / Web frontends** | WebNativeFrontends_Omniverse_WebRTC | — **gap** (web_rtc, web_frontend) |
| **OGC / Geospatial** | Munich_Urban_Digital_TWIN_OGC_OpenUSD | — **gap** (ogc, geospatial) |
| **Forschungszulage / R&D tax** | Forschungszulage_Einzelunternehmer_DevFramework | `r_and_d_tax_credit`, `bsfz_certification` ✓ |
| **Circular Economy / Botrop** | Circular Economy Botrop, Circular_Economy_Botrop_Indicators | — **gap** (circular_economy, sustainability) |
| **European OSS / CRM** | European_OSS_CRM_01_Repositories | — **gap** (oss, crm) |
| **Quantum computing** | quantum_computing_applications | — **gap** (quantum_computing) |
| **Recursive / Language models** | Recursive_Language_Models | — **gap** (llm, language_models) |
| **Machine learning** | machine_learning_optimization | — **gap** (machine_learning) |
| **Claude Flow** | Claude_Flow | `claude_code` (partial) — **gap** |
| **Asset Resolver / IP Rights** | AssetResolver_IPRights | — **gap** (asset_resolver, ip_rights) |
| **Context window** | context_window_optimization_techniques | — **gap** (context_window) |
| **AI coding tools** | AI_coding_ColeMedin, aipowered_code_generation_tools | `ai_assisted_development` ✓ |
| **VariantSets / Session layer** | VarianSets_In_SessionLyr | `variants`, `layers` ✓ |
| **Workflow Engine** | Workflow_Engine_Userguide | `workflow_automation` ✓ |
| **Documentation layering** | documentation_layering_patterns | `layers`, `layered_architecture` ✓ |
| **Branding** | Branding_OpenGoodStart | — **gap** (branding) |
| **CAD / Mesher / Ngons** | CAD_mesher_Ngons_MOI | `manufacturing` (partial) — **gap** (cad, meshing) |

### 1.2 Topic gaps (no master tag)

| Proposed tag | Category | Rationale |
|--------------|----------|-----------|
| `materialx` | functionality | MaterialX node graph, GraphEditor |
| `etl` | functionality | Extract, Transform, Load pipelines |
| `blender` | integration | Blender DCC |
| `c4d` | integration | Cinema 4D DCC |
| `rhino` | integration | Rhino DCC |
| `brev` | integration | BREV cloud GPU |
| `sphinx` | integration | Sphinx documentation |
| `walrus` | integration | Walrus data viz |
| `web_rtc` | integration | WebRTC real-time |
| `ogc` | industry | OGC geospatial standards |
| `circular_economy` | industry | Circular economy / sustainability |
| `quantum_computing` | research_type | Quantum computing |
| `machine_learning` | functionality | ML optimization |
| `asset_resolver` | usd_specific | USD Asset Resolver |
| `context_window` | functionality | LLM context window |
| `branding` | use_case | Branding / identity |

---

## 2. Master Tag System — Audit

### 2.1 Tags by category (structured)

| Category | Count | Notes |
|----------|-------|------|
| environment | 5 | inside_omniverse, outside_omniverse, hybrid, standalone, omniverse_editor |
| functionality | 28 | materials, variants, debugging, … gaussian_splatting, agent_orchestration, … |
| use_case | 28 | scene_analysis, digital_twin_creation, … |
| complexity | 5 | beginner, intermediate, advanced, expert, sme |
| dependencies | 4 | usd_core, omniverse, python_standard, external_libs |
| industry | 16 | automotive, catia, plant_simulation, opc_ua, catena_x, … |
| research_type | 20 | workflow_optimization, best_practices, r_and_d_tax_credit, … |
| usd_specific | 25 | openusd, layers, aas_integration, … |
| performance | 5 | memory_efficient, fast_execution, … |
| safety | 5 | dry_run, backup_creation, … |
| integration | 18 | cursor, openclaw, beads, comfyui, … |
| output | 6 | csv_output, json_output, … |
| input | 6 | file_input, directory_input, … |

**Flat tag cloud**: ~200+ entries (PascalCase, mixed formats)

### 2.2 Likely redundancies

| Redundant pair | Recommendation |
|----------------|----------------|
| `digital_twin` (industry) vs `digital_twin_creation` (use_case) | Keep both — different axes: industry vs. use case. Document when to use which. |
| `semantic_integration` in functionality vs. research_type | Duplicate. **Merge**: keep in functionality, remove from research_type or alias. |
| `semantic_governance` in use_case vs. usd_specific | Duplicate. **Merge**: keep in usd_specific (AAS context), remove from use_case or document distinction. |
| `validation` in functionality vs. safety | Different: func = data validation, safety = pre-execution validation. Keep both. |
| `best_practice` (deprecated) vs `best_practices` | Master says use `best_practices`. Ensure no `best_practice` in structured tags. ✓ (only best_practices) |
| `variants` in functionality vs. usd_specific | Different: func = variant workflows, usd = USD variant system. Keep both. |
| `integration_pattern` (research) vs `framework_integration` (integration) | Overlap. Consider: `integration_pattern` = research about patterns; `framework_integration` = actual integration. Document. |
| `workflow_optimization` vs `workflow_automation` | Different: optimization = improving, automation = automating. Keep both. |

### 2.3 Flat tag cloud vs. structured tags

- **Issue**: Proposer uses structured tags; flat_tag_cloud is for backward compatibility.
- **Overlap**: Many flat tags (e.g. "CATIA", "Digital Twin", "OPC UA") duplicate or overlap structured tags.
- **Recommendation**: When adding to structured tags, add to flat_tag_cloud only if needed for legacy tools. Prefer structured tags for new tagging.

### 2.4 Tag_examples inconsistency

- Line 428: `tutorial_doc` uses `best_practice` (deprecated) — should be `best_practices`.
- Line 430: `product_shot_pipeline` uses `multimatte` — master has `multimatte` in usd_specific ✓.

---

## 3. Proposed Execution Plan

### Phase 1: Master tag system cleanup (1–2 hours)

**Deliverables:**
1. Fix `tag_examples`: replace `best_practice` → `best_practices`.
2. Resolve `semantic_integration` duplication: keep in functionality, add comment in research_type.
3. Document `digital_twin` vs `digital_twin_creation` usage in tag_usage_standards.
4. Add missing structured tags for Research WIP gaps (see 1.2).

**Execution:**
- Edit `master_tag_system.yml` directly.
- Add new tags to appropriate categories.
- Update meta version and last_updated.

### Phase 2: Topic inventory → master alignment (2–3 hours)

**Deliverables:**
1. Add all proposed tags from §1.2 to master (prioritize high-frequency topics).
2. Update `tag_semantic_proposer.py` filename cues for new tags.
3. Produce `TOPIC_TO_TAG_MAPPING.md` for manual tagging reference.

**Execution:**
- Batch-add tags to master.
- Extend proposer patterns.
- Create mapping doc: topic → recommended tags.

### Phase 3: File-by-file tagging (iterative)

**Workflow per file:**
1. Open file.
2. Identify main subjects (from content + filename).
3. Check master for matching tags.
4. If gap: add tag to master first, then apply.
5. Apply tags (min 4, sweet spot 12-15, max 25, from master only).
6. Move to next file.

**Batching:**
- Start with Research WIP (100 files).
- Then FILES_NEEDING_TAGGING.md (617 files, excluding archives).
- Use proposer for `#needs_tagging` files; manual review for files with wrong tags.

### Phase 4: Validation & maintenance

**Deliverables:**
1. Script or checklist: all tags in docs exist in master.
2. Quarterly review: tag usage stats, deprecation candidates.
3. Update FILES_NEEDING_TAGGING.md after each tagging batch.

**Execution:**
- Add validation step to tag_sync_tool or create `tag_validator.py`.
- Document in tag_sync_workflow.md.

---

## 4. Summary

| Item | Count / status |
|------|----------------|
| Research WIP files | 100 |
| Topic clusters identified | 32 |
| Master tag gaps (proposed) | 16 |
| Redundancies to resolve | 3–4 |
| FILES_NEEDING_TAGGING (post-archive) | 617 |

**Next step:** Execute Phase 1 (master cleanup + add missing tags), then Phase 2 (proposer + mapping doc).