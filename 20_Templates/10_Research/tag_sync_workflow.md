---
arys_schema_version: '1.2'
id: cc90aa75-4690-4d28-bc05-019314ec8ace
title: Tag Sync Workflow — Discovery and Research Document Tag Management
type: STRATEGIC
status: active
trust_level: 2
visibility: internal
created: '2026-02-18T05:33:26Z'
last_modified: '2026-02-18T05:33:26Z'
---

# Tag Sync Workflow — Discovery and Research Document Tag Management

**Version**: 1.1.0 | **Date**: 17.02.2026 | **Time**: 10:00 | **GlobalID**: 20260217_1000_General_Research_AUTO
**Tag block:**
#framework_integration #best_practices #conversion #validation #governance #consolidation #stage #workflow_automation #deterministic_workflows #analysis #case_study #workflow_optimization #quality_assurance #knowledge_graph #stable_knowledge_navigation

**Purpose**: Govern the discovery, validation, and addition of new tags/keywords from discovery and research documents to the master tag system while preventing tag explosion.

---

## Overview

This workflow ensures that:
1. New keywords/tags discovered in documents are identified and evaluated
2. Relevant tags are added to the master tag system (`Master_Rules/master_tag_system.yml`)
3. Tag explosion is prevented through governance rules and consolidation strategies
4. Tag quality and consistency are maintained across the framework

---

## Terminology Clarification

**Internal Framework Usage:**
- Tags and keywords are the same—we treat them all as tags
- All tags come from the master tag system (`Master_Rules/master_tag_system.yml`)
- The term "tags/keywords" is used in workflow documentation for external clarity

**External Communication:**
- When communicating with external audiences, "tags/keywords" is acceptable
- The master tag system is the single source of truth for both

---

## Workflow Steps

### Tag block format rule (Obsidian)

- Use exactly one labeled tag block near the top: `**Tag block:**` followed by one hashtag line.
- Example: `#tag_a #tag_b #tag_c`.
- Do not keep multiple tag clouds in the same document header.

---

### Step 1: Extract Keywords from Documents

**Sources:**
- Discovery documents (`*_DISCOVERY.md`)
- Research documents (`*_RESEARCH_*.md`)
- Template Tags/Keywords sections
- Terminology/Glossary sections
- Inline keyword mentions

**Extraction Patterns:**
- Tags section (preferred): `#tag1 #tag2 #tag3` — Obsidian-compatible hashtags
- Template Tags section (legacy/back-compat): `**Tags**: [tag1, tag2, tag3]`
- Template Keywords section (legacy/back-compat): `**Keywords**: [keyword1, keyword2]`
- Terminology sections: `## Terminology`, `## Glossary`
- Inline keywords: `*Keywords: keyword1, keyword2*`

**Tool:** Use `tag_sync_tool.py` for automated extraction

---

### Step 2: Normalize Keywords

**Normalization Rules:**
- Convert to lowercase
- Replace spaces with underscores
- Remove special characters (except underscores)
- Maximum length: 30 characters
- Remove common stop words if appropriate

**Examples:**
- "Second Brain" → `second_brain`
- "AI Loop" → `ai_loop`
- "Composable Bindings" → `composable_bindings`

---

### Step 3: Compare with Master Tag System

**Comparison Process:**
1. Check categorized tags (all categories in `core.tag_categories`)
2. Check flat tag cloud (`core.flat_tag_cloud`)
3. Check for similar/duplicate tags (fuzzy matching)
4. Identify exact matches (already in system)
5. Identify new keywords (not in system)

**Tool:** `tag_sync_tool.py` performs automated comparison

---

### Step 4: Evaluate New Keywords

**Evaluation Criteria:**

#### Tag vs Noise Decision Rule

Treat candidate as a **tag** only if at least one is true:
- Recurs across 3+ documents, or
- Represents a core framework capability/domain/integration used operationally.

Treat candidate as **noise** when it is:
- Document-state wording (`final`, `test`, `draft`, `userguide`, `normal_subject`),
- Person-name based (`*_colemedin`), or
- Overly long topic phrases that should map to canonical tags.

#### Semantic overlap handling

Before adding a new tag:
1. Check canonical equivalent in `Master_Rules/master_tag_system.yml`.
2. If overlap exists, use canonical tag and document alias mapping in `TOPIC_TO_TAG_MAPPING.md`.
3. Add a new tag only when no canonical tag captures the meaning and recurrence threshold is met.

**Must Meet:**
- ✅ Represents a recurring concept (appears in 3+ documents OR is a core framework concept)
- ✅ Fits naming convention (lowercase_with_underscores, max 30 chars)
- ✅ Has clear category fit OR can justify new category
- ✅ Not a duplicate of existing tag (exact or similar)

**Should Meet:**
- ⚠️ Has clear description/definition
- ⚠️ Has usage examples
- ⚠️ Related to existing tags (can link to related concepts)

**Rejection Criteria:**
- ❌ One-off concept (only in one document)
- ❌ Violates naming conventions
- ❌ Duplicate of existing tag
- ❌ Too generic or too specific
- ❌ Category would exceed 50 tags (requires consolidation first)

---

### Step 5: Propose New Tags

**Tag Proposal Format:**

```yaml
proposed_tag: "second_brain"
category: "functionality"  # or "use_case", "research_type", etc.
description: "AI-powered knowledge management system that actively classifies, routes, and surfaces information"
source_documents:
  - "SecondBrain_Memex_DISCOVERY.md"
  - "SecondBrain_Memex_RESEARCH_AB_V04.md"
proposed_by: "[Author Name]"
date: "2026-01-11"
related_tags:
  - "automation"
  - "knowledge_management"
usage_examples:
  - "Second brain systems reduce cognitive overhead by automating classification"
rationale: "Core concept appearing in multiple research documents, represents significant framework capability"
```

**Category Assignment Guidelines:**
- **functionality**: Core capabilities, features, operations
- **use_case**: Specific use cases, scenarios, applications
- **research_type**: Types of research (benchmark, case study, etc.)
- **industry**: Industry-specific tags
- **usd_specific**: USD/OpenUSD-specific concepts
- **New category**: Only if existing categories don't fit AND concept is significant

---

### Canonical mapping examples (do not create new tags)

- `variansets_in_sessionlyr` -> `variants`, `layers`
- `forschungszulage_einzelunternehmer_devframework` -> `r_and_d_tax_credit`, `bsfz_certification`, `sme_status`
- `workflow_engine_userguide` -> `workflow_automation`
- `ai_coding_colemedin` -> `ai_assisted_development`

---

### Step 6: Review and Approval

**Auto-Approve Criteria:**
- ✅ Matches naming convention exactly
- ✅ Fits clearly into existing category
- ✅ Category has < 40 tags
- ✅ Not duplicate of existing tag
- ✅ Has clear description

**Manual Review Required:**
- ⚠️ Category has 40-50 tags (consolidation review needed)
- ⚠️ Requires new category
- ⚠️ Similar to existing tag (fuzzy match > 80%)
- ⚠️ Unclear category fit
- ⚠️ Exceeds 30 character limit

**Rejection:**
- ❌ Duplicate tag
- ❌ Violates naming conventions
- ❌ Category would exceed 50 tags (must consolidate first)
- ❌ One-off concept (not recurring)
- ❌ Too generic or too specific

---

### Step 7: Update Master Tag System

**Update Process:**
1. Add approved tag to appropriate category in `master_tag_system.yml`
2. Add to flat tag cloud if appropriate
3. Update tag usage examples if provided
4. Document tag in tag_examples section if it's a common pattern
5. Update version and last_updated metadata

**File Location:** `Master_Rules/master_tag_system.yml`

---

### Step 8: Update Documents

**Document Update:**
1. Replace keywords in document Tags/Keywords section with standardized tags from master system
2. Add new tags to document if they were approved
3. Remove deprecated/consolidated tags
4. Update document metadata if needed

---

## Tag Explosion Prevention

### Quarterly Review Process

**Review Frequency:** Every 3 months

**Review Tasks:**
1. **Usage Analysis:**
   - Count tag usage frequency across all documents
   - Identify unused tags (0-1 uses in 12 months)
   - Identify low-usage tags (2-5 uses in 12 months)

2. **Category Analysis:**
   - Count tags per category
   - Identify categories approaching 50-tag limit
   - Identify consolidation opportunities

3. **Consolidation:**
   - Merge similar tags (fuzzy match > 85%)
   - Deprecate unused tags
   - Create subcategories if needed (requires approval)

4. **Documentation:**
   - Update tag descriptions
   - Add usage examples for popular tags
   - Document deprecation decisions

### Consolidation Strategy

**When to Consolidate:**
- Category exceeds 45 tags
- Multiple similar tags exist (> 85% similarity)
- Tags have overlapping usage patterns

**How to Consolidate:**
1. Identify similar tags
2. Choose primary tag (most used, clearest name)
3. Merge secondary tags into primary
4. Update all documents using secondary tags
5. Deprecate secondary tags in master system
6. Document consolidation decision

**Example:**
- `knowledge_management` (15 uses) + `second_brain` (8 uses) + `memex` (3 uses)
- Consolidate to: `knowledge_management` (primary)
- Deprecate: `second_brain`, `memex`
- Update documents to use `knowledge_management`

---

## Tool Usage

### Automated Tag Sync

**Run tag sync tool:**
```bash
python tag_sync_tool.py --discovery <discovery_file> --research <research_file>
```

**Options:**
- `--discovery <file>`: Discovery document to extract keywords from
- `--research <file>`: Research document to extract keywords from
- `--master-tags <file>`: Path to master tag system YAML (default: `Master_Rules/master_tag_system.yml`)
- `--propose`: Generate tag proposals for new keywords
- `--update-docs`: Update documents with standardized tags
- `--review`: Show tags requiring manual review
- `--consolidation`: Show consolidation opportunities

**Output:**
- List of new keywords found
- Tag proposals with category suggestions
- Tags requiring manual review
- Consolidation opportunities
- Updated tag lists for documents

---

## Governance Rules Summary

**Tag Limits:**
- Max tags per category: 50
- Max flat tags: 500
- Review threshold: 40 tags per category
- Min tags per document: 5
- Sweet spot per document: 14-18
- Max tags per document: 25

**Document-size targeting:**
- Short notes: 5-10 tags
- Medium docs: 10-16 tags
- Long/complex research: 14-20 tags

**Quality Gates:**
- Naming: `lowercase_with_underscores`, max 30 chars
- Uniqueness: Must be unique within category and flat cloud
- Relevance: Must represent recurring concepts (3+ documents)
- Category fit: Must fit existing category or justify new one

**Lifecycle:**
- Proposal → Review → Approval → Usage Tracking → Deprecation Review → Consolidation

---

## Related Documentation

- **Master Tag System:** `Master_Rules/master_tag_system.yml`
- **Tag Sync Tool:** `General_Research/030_Proj_TEMPLATES/tag_sync_tool.py`
- **Template:** `General_Research/030_Proj_TEMPLATES/Internal_Research_Analysis_template.md`
- **Framework Guide:** `Master_Rules/AGENTS.md` (Universal Tag Cloud System section)

---

**Version**: 1.1.0  
**Last Updated**: 17.02.2026  
**Framework**: Master_Rules (Universal Framework Foundation)