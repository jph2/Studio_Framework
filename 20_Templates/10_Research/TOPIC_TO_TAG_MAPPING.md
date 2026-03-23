---
arys_schema_version: '1.2'
id: e827e49a-2676-428b-a523-2e7011af9e88
title: Topic to Tag Mapping — Manual Tagging Reference
type: STRATEGIC
status: active
trust_level: 2
visibility: internal
created: '2026-02-18T05:33:26Z'
last_modified: '2026-02-18T05:33:26Z'
---

# Topic to Tag Mapping — Manual Tagging Reference

**Version**: 1.1 | **Date**: 17.02.2026 | **Time**: 09:55 | **GlobalID**: 20260217_0955_General_Research_TAG_MAP
**Tag block:**
#framework_integration #best_practices #stage #reference #conversion #aas_integration #digital_twin_creation #openusd #industrial_integration #catia #layers #simulation #usd_core #omniverse #digital_twin #workflow_automation #deterministic_workflows #analysis #case_study #export #isaac_sim #omniverse_nucleus #grasshopper #websocket_api

Use this table when manually tagging files. All tags must exist in [master_tag_system.yml](../../Master_Rules/master_tag_system.yml).

---

## Topic → Recommended Tags

| Topic (from filename/content) | Recommended tags |
|-------------------------------|-------------------|
| AAS / Asset Administration Shell | aas_integration, digital_twin_creation, openusd, industrial_integration |
| CATIA / 3DXML / 3DX | catia, conversion, openusd, layers |
| Plant Simulation / Siemens | plant_simulation, digital_twin, manufacturing |
| Catena-X | catena_x, automotive, aas_integration |
| Digital Twin | digital_twin, digital_twin_creation, industrial_integration |
| Gaussian Splatting | gaussian_splatting, rendering, conversion, omniverse |
| Agent / AI ecosystem | agent_orchestration, multi_agent_systems, automation |
| OpenClaw / Soul / Skills | openclaw, skills, framework_integration |
| Memex / Second Brain | memex, second_brain_system, knowledge_graph |
| Cursor / Codex / IDE | cursor, ai_assisted_development |
| ComfyUI | comfyui, ai_content_pipeline, rendering |
| MaterialX | materialx, materials, openusd |
| ETL / Data pipeline | etl, conversion, file_processing, openusd |
| WRAPP / Packaging | packaging, distribution, workflow_automation |
| Blender | blender, export, conversion |
| C4D / Cinema 4D | c4d, export, conversion |
| USD start point (pipeline concept) | usd_start_point, workflow_automation, openusd |
| USD_GoodStart repository | usd_goodstart, openusd, framework_integration |
| OpenUSD-GoodStart repository | openusd_goodstart, openusd, framework_integration |
| Rhino | rhino, export, conversion |
| Omniverse / Sequencer / LED Dome | omniverse, sequencer, camera_management |
| BREV / Launchable | brev, cloud_storage |
| Sphinx | sphinx |
| Walrus DataViz | walrus |
| WebRTC / Web frontends | web_rtc |
| WebSocket APIs | websocket_api, framework_integration |
| Omniverse Nucleus | omniverse_nucleus, omniverse, framework_integration |
| Isaac Sim | isaac_sim, omniverse, industrial_integration |
| Grasshopper (Rhino) | grasshopper, rhino, workflow_automation |
| OGC / Geospatial | ogc, digital_twin |
| Forschungszulage / R&D tax | r_and_d_tax_credit, bsfz_certification |
| Circular Economy / Botrop | circular_economy |
| Quantum computing | quantum_computing |
| Machine learning | machine_learning, optimization |
| Asset Resolver / IP Rights | asset_resolver |
| Context window | context_window |
| Branding | branding |
| Documentation layering | layers, layered_architecture |
| Claude Flow | claude_flow, agent_orchestration, multi_agent_systems |
| AI coding tools (generic) | ai_assisted_development, ai_coding_agents |
| Workflow engine user guides | workflow_automation, framework_integration |
| VariantSets / Session layer (legacy typo: variansets_in_sessionlyr) | variants, layers |
| Forschungszulage Einzelunternehmer Devframework (long topic phrase) | r_and_d_tax_credit, bsfz_certification, sme_status |
| CRM / OSS CRM research | crm, enterprise_software, open_source |
| Recursive language models | machine_learning, ai_assisted_development |
| NVIDIA Siemens Digital Twin Composer | digital_twin, industrial_integration, plant_simulation |

---

## Tag vs Noise Rule (quick)

- Tag when it represents a reusable capability/domain/integration that recurs across documents.
- Noise when it is document-state wording (`final`, `test`, `userguide`), a person name, or an overly long topic phrase.
- For semantic overlaps, map to canonical tags first; only add a new tag if no canonical tag expresses the concept.

## Usage

1. Identify main topics from the file (filename + content).
2. Look up topics in this table.
3. Select tags that fit (min 5, sweet spot 14-18, max 25 per document).
4. Apply tags only if they exist in master_tag_system.yml.