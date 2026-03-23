---
arys_schema_version: '1.2'
id: f0a1a226-df61-4ba0-8604-98b14523ebd9
title: ⚠️ TEMPLATE FILE — DO NOT SHIP AS-IS
type: PRACTICAL
status: active
trust_level: 2
visibility: internal
created: '2026-02-18T05:33:28Z'
last_modified: '2026-02-18T05:33:28Z'
---

# ⚠️ TEMPLATE FILE — DO NOT SHIP AS-IS

This file is a **TEMPLATE**.
Replace every `[REPLACE_ME:…]` placeholder before use.

---

# 99 Handoff Index — [REPLACE_ME:PROJECT_NAME]

**Version**: [REPLACE_ME:VERSION] | **Date**: [REPLACE_ME:DD.MM.YYYY] | **Time**: [REPLACE_ME:HH:MM] | **GlobalID**: [REPLACE_ME:GLOBAL_ID]

**Purpose**: Master index of all session handoffs. Keep this file lean; create dated session handoffs for each work unit or topic. Naming convention: `99A_Handoff_YYYYMMDD_[Topic].md`, `99B_Handoff_YYYYMMDD_[Topic].md`, etc.

**Tag block:**
#workflow_automation #best_practices #automation #framework_integration #deterministic_workflows #extension_development #analysis #quality_assurance

---

## Current status (summary)

- [REPLACE_ME:STATUS_SUMMARY]

---

## Session handoffs (chronological)

| ID | Date | Topic | File |
|----|------|-------|------|
| 99A | [REPLACE_ME:YYYYMMDD] | [REPLACE_ME:TOPIC] | [99A_Handoff_YYYYMMDD_Topic.md](99A_Handoff_YYYYMMDD_Topic.md) |

**When creating a new handoff:** Copy `99_HANDOFF_SESSION.md` (or the session template), rename to `99[Letter]_Handoff_YYYYMMDD_[Topic].md`, fill content, then add a row to this table.

---

## Quick links

- **Build**: See `11_BUILD_INSTRUCTIONS.md`
- **Test**: See `05_Testing_Plan.md`
- **WIP**: See `80_WIP.md` for in-progress work log
