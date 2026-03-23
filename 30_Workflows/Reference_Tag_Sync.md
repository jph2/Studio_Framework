---
arys_schema_version: '1.2'
id: cca090c7-6434-4a6a-af2a-47bd2f3bb325
title: Tag Sync System — Quick Reference
type: STRATEGIC
status: active
trust_level: 2
visibility: internal
created: '2026-02-18T05:33:26Z'
last_modified: '2026-02-18T05:33:26Z'
---

# Tag Sync System — Quick Reference

**Version**: v1.0.0 | **Date**: 13.01.2026 | **Time**: 00:20 | **GlobalID**: 20260113_0020_General_Research_AUTO

**Purpose**: Lightweight reference for tag synchronization between research documents and Master Tag System  
**Full Documentation**: `tag_sync_workflow.md`  
**Tool**: `tag_sync_tool.py`

**Tag block:**
#framework_integration #best_practices #integration_tests #reference #conversion #stage #export #workflow_automation #deterministic_workflows #analysis #case_study

---

## Quick Usage

### Enforce Tag Format (All Documents)
```bash
python tag_format_enforcer.py --path <root> [--dry-run]
python tag_format_enforcer.py --dry-run  # scan General_Dev, report only
```
Replaces legacy tag formats with `#tagA #tagB #tagC`. Adds `#needs_tagging` when missing. Excludes ARCHIVED by default.

### Extract & Compare Tags
```bash
python tag_sync_tool.py extract "path/to/research.md" --compare
```

### Sync Tags (Dry Run)
```bash
python tag_sync_tool.py sync "path/to/research.md" --dry-run
```

### Sync Tags (Apply)
```bash
python tag_sync_tool.py sync "path/to/research.md"
```

---

## Tag Format Standards

- **Document format**: `#tagA #tagB #tagC` (Obsidian-compatible hashtags, space-separated)
- **Tag format**: `lowercase_with_underscores`
- **Max Length**: 30 characters
- **Max Tags/Doc**: 12 tags
- **Required Categories**: `environment`, `functionality`, `use_case`

---

## Integration Points

- **Master Tag System**: `10_Artifact_System/10_Schema/master_tag_system.yml`
- **Workflow**: `30_Workflows/Workflow_Tag_Sync.md`
- **Tag Semantic Index**: `10_Artifact_System/10_Schema/TAG_SEMANTIC_INDEX.md`
- **Tools**: deterministic tag utilities (to be finalized in the Studio utility layer)

---

## When to Use

- After completing research documents
- When adding new keywords/concepts
- Before publishing research documents
- Quarterly tag system maintenance

---

**Last Updated**: 07.01.2026

07.01.2026

