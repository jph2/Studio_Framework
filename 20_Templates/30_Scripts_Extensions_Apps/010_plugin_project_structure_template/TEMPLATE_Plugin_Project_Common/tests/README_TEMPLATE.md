---
arys_schema_version: '1.2'
id: 71096520-9229-406c-b1c5-2ef8327aba47
title: ⚠️ TEMPLATE FILE — DO NOT SHIP AS-IS
type: TECHNICAL
status: active
trust_level: 2
visibility: internal
created: '2026-02-19T13:10:40Z'
last_modified: '2026-02-19T13:10:40Z'
---

**Version**: 1.0.0 | **Date**: 16.02.2026 | **Time**: 12:00 | **GlobalID**: 20260216_1200_General_Dev_batch

**Tag block:**
#framework_integration #best_practices #workflow_automation #extension_development #analysis #quality_assurance #validation

# ⚠️ TEMPLATE FILE — DO NOT SHIP AS-IS

This folder contains the minimum testing scaffold for every generated plugin project.

## Required structure

```text
tests/
|-- README.md
|-- unit/
|   `-- test_smoke.py
|-- integration/
|   `-- README.md
|-- scenarios/
|   `-- README.md
`-- manual/
    `-- README.md
```

## Execution policy

- `unit`: run on every commit.
- `integration`: run before review handoff.
- `scenarios`: run before release candidate.
- `manual`: run before release candidate and attach report evidence.

## Commands

Replace with project-real commands:

```text
[REPLACE_ME:UNIT_TEST_COMMAND]
[REPLACE_ME:INTEGRATION_TEST_COMMAND]
[REPLACE_ME:SCENARIO_TEST_COMMAND]
```

## Notes

- Keep this file synced with `05_Testing_Plan.md`.
- If a layer is intentionally skipped, document reason and risk acceptance.

