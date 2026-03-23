---
arys_schema_version: '1.2'
id: f3045b0c-b291-491b-9882-40a44be1e795
title: 'Documentation Template: [Title]'
type: STRATEGIC
status: active
trust_level: 2
visibility: internal
created: '2026-02-18T05:33:26Z'
last_modified: '2026-02-18T05:33:26Z'
---

# Documentation Template: [Title]

**Version**: N/A | **Date**: 13.01.2026 | **Time**: 00:20 | **GlobalID**: 20260113_0020_General_Research_AUTO

**Tag block:**
#workflow_optimization #best_practices #case_study #workflow_automation #deterministic_workflows #analysis #framework_integration #quality_assurance

> Brief, factual description of what this document covers

## 🤖 Agent Note (Discovery → Research workflow)

- **Discovery location**: `research/01_Research_DISCOVERY/`
- **Discovery naming**: filenames may contain `_DISCOVERY` **or** `__DISCOVERY` (both accepted)
- **Promotion script**: `scripts/generate_research_from_discovery.py` generates a `_RESEARCH` placeholder into `research/02_Research_WIP/`
- **Research structure rules (source of truth)**: `Research_Definition/research_configuration_rules.yml`

## 📝 Template User Note (YAML contract + templates)

- **Ruling contract**: `Research_Definition/research_configuration_rules.yml`
- **Master research template**: `templates/research_template.md` (YAML profile: `research_master`)
- **This file** is a general documentation template (YAML profile: `documentation`) — use it when you’re documenting a process/solution, not doing full research synthesis.

## Overview

**Purpose**: [What this document is for]  
**Audience**: [Who should use this]  
**Prerequisites**: [What you need before starting]  
**Last Updated**: [Date]  
**Status**: [Current/Deprecated/Under Review]

## Problem Statement

**What**: [Clear description of the problem or need]  
**Why**: [Why this problem exists or why it matters]  
**When**: [When this problem occurs or when this solution is needed]

## Solution

### Approach
[How the problem is solved - step by step]

### Requirements
- **Hardware**: [Specific hardware requirements]
- **Software**: [Software versions and dependencies]
- **Access**: [Required accounts, permissions, or access]
- **Time**: [Estimated time to complete]

### Implementation Steps

#### Step 1: [Step Name]
**Purpose**: [Why this step is needed]  
**Duration**: [How long it takes]  
**Prerequisites**: [What must be done first]

```bash
# Commands or code examples
```

**Expected Result**: [What should happen]  
**Troubleshooting**: [Common issues and solutions]

#### Step 2: [Step Name]
[Same structure as Step 1]

#### Step 3: [Step Name]
[Same structure as Step 1]

## Configuration Details

### Key Settings
| Setting | Value | Purpose |
|---------|-------|---------|
| [Setting 1] | [Value] | [Why this value] |
| [Setting 2] | [Value] | [Why this value] |

### File Locations
- **Configuration File**: [Path and purpose]
- **Log Files**: [Where to find logs]
- **Data Directory**: [Where data is stored]

## Verification

### How to Test
1. [Test step 1]
2. [Test step 2]
3. [Test step 3]

### Success Criteria
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

### Common Issues
| Issue | Symptoms | Solution |
|-------|----------|----------|
| [Issue 1] | [What you see] | [How to fix] |
| [Issue 2] | [What you see] | [How to fix] |

## Maintenance

### Regular Tasks
- **Daily**: [What to check daily]
- **Weekly**: [What to check weekly]
- **Monthly**: [What to check monthly]

### Updates
- **When to Update**: [Triggers for updates]
- **How to Update**: [Update process]
- **Rollback Plan**: [How to revert if needed]

## References

### Documentation
- [Link 1]: [Description]
- [Link 2]: [Description]

### Related Documents
- [Document 1]: [Purpose]
- [Document 2]: [Purpose]

### Support
- **Internal**: [Who to contact internally]
- **External**: [Vendor support or community]

---

**Document Version**: [Version]  
**Next Review Date**: [Date]  
**Maintained By**: [Name/Team]
