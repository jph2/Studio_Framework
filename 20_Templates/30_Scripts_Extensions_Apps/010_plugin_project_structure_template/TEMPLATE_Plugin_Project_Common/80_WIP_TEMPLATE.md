---
arys_schema_version: '1.2'
id: 4751a141-731c-4f72-8daf-ad41ec3b54ad
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

# 80 Work in Progress — [REPLACE_ME:PROJECT_NAME]

**Version**: [REPLACE_ME:VERSION] | **Date**: [REPLACE_ME:DD.MM.YYYY] | **Time**: [REPLACE_ME:HH:MM] | **GlobalID**: [REPLACE_ME:GLOBAL_ID]

**Purpose**: Running log of current work, recent completions, blockers, and next steps. Use this to stay focused and to hand off context. Chronological log: **oldest first, newest last**.

**Tag block:**
#workflow_automation #best_practices #automation #framework_integration #deterministic_workflows #extension_development #analysis #quality_assurance

---

## Current focus

- [REPLACE_ME:CURRENT_FOCUS_1]
- [REPLACE_ME:CURRENT_FOCUS_2]

---

## Next steps (priority order)

1. [REPLACE_ME:NEXT_STEP_1]
2. [REPLACE_ME:NEXT_STEP_2]
3. [REPLACE_ME:NEXT_STEP_3]

---

## Blockers

- [REPLACE_ME:BLOCKER_OR_NONE]

---

## Chronological log (oldest first, newest last)

### [REPLACE_ME:YYYY-MM-DD] — [REPLACE_ME:SESSION_SUMMARY]

**Done:**
- [REPLACE_ME:DONE_1]
- [REPLACE_ME:DONE_2]

**Files changed:** [REPLACE_ME:FILE_LIST]

---

---

## WIP archive pattern

When `80_WIP.md` exceeds **~300 lines**, archive older chronological log entries:

1. Create `80A_WIP_Archive_Phase1.md` (or `80B_...`, `80C_...` for subsequent archives)
2. Move entries older than the last 2-3 sessions to the archive file
3. Keep in `80_WIP.md` only: Current focus, Next steps, Blockers, last 2-3 session entries
4. Add a note at top of `80_WIP.md`: "Older entries: see `80A_WIP_Archive_Phase1.md`"

**Naming**: `80A_WIP_Archive_Phase1.md`, `80B_WIP_Archive_Phase2.md`, etc. Match phase naming to project phases.

**Purpose**: Agents load `80_WIP.md` for "where are we?" — keep it focused. Load archives only when investigating historical context.

---

**End of WIP.** Update "Current focus" and "Next steps" as work progresses; append new entries to the chronological log (newest at bottom). Requirements: `02_Detailed_Requirements.md`. Implementation detail: `04_Implementation_Plan.md` (and phase sub-documents e.g. `04A_Implementation_Plan_Phase1_[Name].md`).
