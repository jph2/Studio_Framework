---
arys_schema_version: '1.2'
id: 1b9ea400-c5fe-4401-afe8-5db896fab32e
title: 'Template: OmniConnector / Pipeline Architecture Overview (Data A → B)'
type: TECHNICAL
status: active
trust_level: 2
visibility: internal
created: '2026-02-18T05:33:26Z'
last_modified: '2026-02-18T05:33:26Z'
---

# Template: OmniConnector / Pipeline Architecture Overview (Data A → B)

**Version**: N/A | **Date**: 13.01.2026 | **Time**: 00:20 | **GlobalID**: 20260113_0020_General_Research_AUTO

**Tag block:**
#workflow_optimization #best_practices #case_study #openusd #usd_core #omniverse #workflow_automation #deterministic_workflows #analysis #framework_integration #aas_integration #semantic_governance #omniverse_nucleus

## 🤖 Agent Note (Discovery → Research workflow)

- **Discovery location**: `research/01_Research_DISCOVERY/`
- **Discovery naming**: filenames may contain `_DISCOVERY` **or** `__DISCOVERY` (both accepted)
- **Promotion script**: `scripts/generate_research_from_discovery.py` generates a `_RESEARCH` placeholder into `research/02_Research_WIP/`
- **Research structure rules (source of truth)**: `Research_Definition/research_configuration_rules.yml`

## 📝 Template User Note (YAML contract + templates)

- **Ruling contract**: `Research_Definition/research_configuration_rules.yml`
- **This template is NOT the master**. It’s the specialized variant for **connector/pipeline evaluations** (YAML profile: `connector_pipeline_evaluation`).
- **Master template** (default starting point): `templates/research_template.md` (YAML profile: `research_master`).
- Use this when your question is: **“What data moves from A → B, with what fidelity, and how do we validate it?”**



> **Purpose**: Evaluate and communicate what a connector/pipeline can **move, preserve, enrich, and validate** when transferring data from **System A → System B** using **OpenUSD / Omniverse** (or adjacent mechanisms).

>

> **Mindset**: *3D geometry is only one slice.* Treat this as a **data-product transfer**: IDs, BOM, PMI, requirements, certifications, DPP/AAS fields, runtime signals, provenance.



---



## 📋 Discovery Metadata



- **Date**: 13.12.2025

- **Author**: [Name]

- **System A (Source of truth)**: [e.g., NX | CATIA | Plant Simulation | Teamcenter]

- **System B (Target / Consumer)**: [e.g., Omniverse | Nucleus | Kit App | downstream platform]

- **Connector / Pipeline Name**: [Name]

- **Versions**: A=[v], Connector=[v], B=[v]

- **Transfer Mode**: [export | incremental | live_sync | bidirectional]

- **Primary Use Case**: [engineering_review | marketing_visuals | simulation_replay | DPP/DigitalThread | ops_runtime]

- **Status**: [Draft | In Review | Final]

- **Confidence**: [Low | Medium | High]



---



## 🧭 TL;DR (copy/paste for stakeholders)



- **What is it?** [1–2 sentences]

- **What value does it unlock?** [3 bullets max]

- **What does it reliably transfer?** [3–6 bullets]

- **What does it NOT transfer (or loses)?** [3–6 bullets]

- **Key constraint**: [1 sentence]

- **Recommended next step**: [1 sentence]



---



## ☁️ Tech Cloud (quick stack map)



- **Source ecosystem**: [CAD/CAE/MFG toolchain, PLM, naming/ID strategy]

- **Connector layer**: [plugin/exporter/SDK, where it runs]

- **Transport & storage**: [USD files | Nucleus live | API | sidecars]

- **Target ecosystem**: [Kit apps, viewers, render, automation]

- **Adjacent enterprise systems**: [PLM/ERP/MES/ALM/DAM/PIM/AAS/OPC UA]



---



## 🧩 What This Evaluation Is About



### Context



[What triggered this evaluation? Which client/pipeline pain?]



### Definition of “Done”



- [ ] I can explain the connector’s **data contract** (what moves, what doesn’t, why)

- [ ] I can describe **system-of-record boundaries** and roundtrip limitations

- [ ] I can estimate **integration effort** (security, deployment, ops)

- [ ] I have a **minimal PoC** plan with success criteria



---



## 🗺️ Architecture Overview (one-picture)



```mermaid

flowchart LR

  A[System A\n(Authoring / SoR)] -->|Connector / Export / Sync| X[Transfer Layer\n(USD + sidecars + APIs)]

  X --> B[System B\n(Omniverse / Consumers)]



  subgraph Enterprise Touchpoints

    PLM[PLM / PDM]:::sys

    ERP[ERP]:::sys

    MES[MES]:::sys

    DAM[DAM / PIM]:::sys

    AAS[AAS / DPP]:::sys

    OPC[OPC UA / Telemetry]:::sys

  end



  A <--> PLM

  X <--> AAS

  X <--> DAM

  B <--> OPC



  classDef sys fill:#ffd166,stroke:#333,color:#111;

```



---



## 📦 Payload Inventory (what data is actually crossing the boundary?)



> Treat this as the *core* of the template. Don’t hand-wave “supports USD” — specify **which domains** and **how** they are represented.



### Data Domains Checklist



| Data domain | In scope? | Transfer representation | Fidelity expectation | Notes / loss modes |

|---|---:|---|---|---|

| Geometry (B-Rep / tessellated) | [ ] | [USD Mesh | USDGeom | …] | [High/Med/Low] | [tessellation limits, LOD] |

| Assembly structure | [ ] | [prim hierarchy | references | payloads] | | |

| Units / axes | [ ] | [metadata] | | |

| Materials / looks | [ ] | [UsdShade | MDL | preview surface] | | |

| Naming + stable IDs | [ ] | [attrs | prim paths | external IDs] | | |

| BOM / product structure | [ ] | [attrs | sidecar JSON | PLM links] | | |

| Variants / configurations | [ ] | [variantSets | layers] | | |

| PMI / GD&T / annotations | [ ] | [USD prims? sidecar?] | | |

| Kinematics / joints | [ ] | [schemas | conventions] | | |

| Simulation model (behavior/logic) | [ ] | [not in USD / streamed / custom] | | |

| Requirements / compliance refs | [ ] | [links/IDs] | | |

| Certifications / declarations | [ ] | [docs/IDs] | | |

| DPP fields (Digital Product Passport) | [ ] | [mapping strategy] | | |

| AAS mapping (Asset Admin Shell) | [ ] | [submodel mapping] | | |

| Documents (PDF, specs) | [ ] | [sidecars / DAM link] | | |

| Thumbnails / previews | [ ] | [render outputs] | | |

| Runtime telemetry (states, KPIs) | [ ] | [OPC UA/ROS2/custom] | | |

| Provenance / lineage | [ ] | [metadata, logs] | | |



### “Hidden Payload” Notes



- **What System A knows that USD alone won’t carry**: [IDs, PMI, BOM semantics, requirements, …]

- **What must be carried via sidecars or external links**: [JSON, PLM refs, AAS submodels]

- **What must be computed/enriched downstream**: [classification, DPP aggregation]



---



## 📜 Data Contract (make it explicit)



### Identity & Traceability



- **Stable object identity**: [what is the unique ID?]

- **Where is it stored?**: [prim path vs attribute vs sidecar vs PLM]

- **Provenance fields**: [source system, version, timestamp, author]



### Naming / Structure Conventions



- **Prim path stability rules**: [what changes are allowed?]

- **Namespace strategy for metadata**: [e.g., `plm:*`, `dpp:*`, `aas:*`]

- **Layer ownership**:

  - Source-authored layers: [list]

  - Consumer-authored layers: [list]

  - Runtime override layers: [list]



### Interop strategy (schemas vs raw attributes)



- **Approach**: [raw namespaced attrs first | codeless schema | compiled schema]

- **Why**: [tooling, validation, cross-team consumption]



---



## 🔁 Transfer Semantics (how updates behave)



- **Export style**: [full snapshot | incremental delta | live stream]

- **Update triggers**: [manual | scheduled | event-driven]

- **Conflict resolution**: [source wins | merge | manual review]

- **Roundtrip**: [none | limited | supported] + **what is safe to edit in B**

- **Performance envelope**: [model size, expected time, bandwidth]



---



## ✅ Benefits (by stakeholder)



- **Engineering**: [design review, faster iteration, fewer translation steps]

- **Manufacturing / simulation**: [layout verification, replay, KPI visibility]

- **Marketing / content**: [high-quality renders, reuse variants]

- **IT / security**: [governed access, auditability]

- **Compliance / sustainability (DPP)**: [traceability, declarations, IDs]



---



## ⚠️ Limitations / Failure Modes



- **Data loss hotspots**: [PMI, materials, IDs, variant semantics]

- **Operational risks**: [version skew, brittle mappings, dependency on plugins]

- **Licensing constraints**: [seats, runtime distribution, connector cost]

- **Security constraints**: [network zones, auth patterns]



---



## 🧪 Validation Plan (prove it fast)



### Minimal PoC Scenarios



1. **3D + identity**: geometry + stable IDs survive 2 updates

2. **BOM/metadata**: extract IDs/BOM links for downstream reporting

3. **DPP/AAS**: demonstrate mapping of 5–10 DPP fields into a target representation

4. **Runtime updates (optional)**: stream one KPI/state into USD/Kit display



### Success criteria checklist



- [ ] Unit/axis correctness

- [ ] Path/ID stability across updates

- [ ] Variant/config correctness

- [ ] Material intent preserved (or known downgrade path)

- [ ] Metadata completeness for chosen use case (BOM/DPP)

- [ ] Measured performance (time + size + bandwidth)



---



## 🔐 Security / Deployment (enterprise reality)



- **Deployment model**: [workstation | on-prem | hybrid | cloud]

- **Identity**: [SSO/OAuth2/token model]

- **Access control**: [publish vs consume roles]

- **Auditability**: [logs, provenance, change history]



---



## 📚 Source Registry (preserve links)



| ID | Link | Type | What it supports | Notes |

|---|---|---|---|---|

| S1 | [URL] | Vendor | [claim] | |

| S2 | [URL] | Community | [claim] | |

| S3 | [URL] | Standards | [claim] | |



## 🧾 Evidence Matrix (claim ↔ source)



| Claim | Source IDs | Confidence | Notes |

|---|---|---|---|

| [claim] | S1,S2 | [Low/Med/High] | |



---



## 🧷 Glossary



- **SoR (System of Record)**: [definition]

- **DPP**: Digital Product Passport

- **AAS**: Asset Administration Shell

- **Roundtrip**: [definition]

