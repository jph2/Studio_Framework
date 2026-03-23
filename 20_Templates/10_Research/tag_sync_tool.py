#!/usr/bin/env python3
"""
Tag Sync Tool — Extract, validate, and propose tags from discovery/research documents

Purpose: Automate the discovery and validation of new tags from discovery/research documents
and propose additions to the master tag system while preventing tag explosion.
Note: Tags and keywords are the same internally—we treat them all as tags.

Usage:
    python tag_sync_tool.py --discovery <file> --research <file>
    python tag_sync_tool.py --discovery <file> --research <file> --propose
    python tag_sync_tool.py --discovery <file> --research <file> --update-docs
    python tag_sync_tool.py --review
    python tag_sync_tool.py --consolidation
"""

import re
import yaml
import argparse
import json
from pathlib import Path
from typing import List, Dict, Set, Tuple, Optional
from collections import Counter
from difflib import SequenceMatcher

# Default paths
DEFAULT_MASTER_TAGS = Path(__file__).parent.parent.parent / "Master_Rules" / "master_tag_system.yml"
DEFAULT_DISCOVERY_DIR = Path(__file__).parent.parent.parent / "General_Research" / "070_Proj_RESEARCH" / "02_Research_WIP"
DEFAULT_RESEARCH_DIR = Path(__file__).parent.parent.parent / "General_Research" / "070_Proj_RESEARCH" / "02_Research_WIP"


def normalize_keyword(keyword: str) -> str:
    """Normalize keyword to tag format: lowercase_with_underscores, max 30 chars."""
    # Remove markdown formatting
    keyword = re.sub(r'[\[\]()]', '', keyword)
    # Convert to lowercase
    keyword = keyword.lower()
    # Replace spaces and hyphens with underscores
    keyword = re.sub(r'[\s\-]+', '_', keyword)
    # Remove special characters except underscores
    keyword = re.sub(r'[^a-z0-9_]', '', keyword)
    # Remove multiple underscores
    keyword = re.sub(r'_+', '_', keyword)
    # Remove leading/trailing underscores
    keyword = keyword.strip('_')
    # Truncate to 30 characters
    keyword = keyword[:30]
    return keyword


def extract_tags_from_section(content: str, pattern: str) -> List[str]:
    """Extract tags from a specific section pattern."""
    tags = []
    matches = re.finditer(pattern, content, re.IGNORECASE | re.MULTILINE)
    for match in matches:
        tag_text = match.group(1) if match.groups() else match.group(0)
        # Extract individual tags (pipe-separated preferred; commas accepted for legacy/back-compat)
        # Example preferred: tag1 | tag2 | tag3
        # Example legacy: [tag1, tag2, tag3]
        raw_parts = re.split(r'[|,]', tag_text)
        for part in raw_parts:
            normalized = normalize_keyword(part.strip())
            if normalized:
                tags.append(normalized)
    return tags


def extract_keywords_from_document(file_path: Path) -> Dict[str, List[str]]:
    """Extract tags from a discovery or research document.
    
    Note: Tags and keywords are the same internally. This function extracts
    tags from both Tags and Keywords sections for backward compatibility.
    """
    if not file_path.exists():
        return {}
    
    content = file_path.read_text(encoding='utf-8')
    keywords = {
        'tags_section': [],
        'keywords_section': [],
        'terminology': [],
        'inline_keywords': []
    }
    
    # Extract from Tags sections (preferred + legacy/back-compat)
    # Preferred: #tag1 #tag2 #tag3 (Obsidian-compatible hashtags)
    # Legacy: **Tags (Keywords)**: tag1 | tag2 | tag3
    # Legacy: **Tags**: | tag1 | tag2 | tag3 |
    # Legacy: **Tags**: [tag1, tag2, tag3]
    hashtag_lines = re.findall(r'^#\w+(?:\s+#\w+)*\s*$', content, re.MULTILINE)
    for line in hashtag_lines:
        keywords['tags_section'].extend(
            [normalize_keyword(t) for t in re.findall(r'#(\w+)', line) if t]
        )
    tags_patterns = [
        r'^\*\*Tags\s*\(Keywords\)\*\*:\s*([^\n]+)$',
        r'\*\*Tags:\*\*\s*\|([^\n]+)',  # **Tags:** | tag1 | tag2 |
        r'\*\*Tags\*\*:\s*\[([^\]]+)\]',
    ]
    for p in tags_patterns:
        keywords['tags_section'].extend(extract_tags_from_section(content, p))
    
    # Extract from Keywords section (legacy/back-compat)
    keywords_pattern = r'\*\*Keywords\*\*:\s*\[([^\]]+)\]'
    keywords['keywords_section'] = extract_tags_from_section(content, keywords_pattern)
    
    # Extract from Terminology/Glossary sections
    terminology_pattern = r'##\s+(?:Terminology|Glossary)\s*\n(.*?)(?=\n##|\Z)'
    terminology_matches = re.finditer(terminology_pattern, content, re.IGNORECASE | re.DOTALL)
    for match in terminology_matches:
        terminology_text = match.group(1)
        # Extract terms (lines starting with -, *, or numbered)
        term_lines = re.findall(r'[-*]\s*([^\n]+)', terminology_text)
        keywords['terminology'].extend([normalize_keyword(term.split(':')[0]) for term in term_lines])
    
    # Extract inline keywords: *Keywords: keyword1, keyword2*
    inline_pattern = r'\*Keywords:\s*([^*]+)\*'
    keywords['inline_keywords'] = extract_tags_from_section(content, inline_pattern)
    
    # Remove empty lists and deduplicate
    all_keywords = []
    for keyword_list in keywords.values():
        all_keywords.extend(keyword_list)
    
    return {
        'source': str(file_path),
        'all_keywords': list(set(all_keywords)),
        'by_section': {k: list(set(v)) for k, v in keywords.items() if v}
    }


def load_master_tag_system(file_path: Path) -> Dict:
    """Load master tag system YAML file."""
    if not file_path.exists():
        raise FileNotFoundError(f"Master tag system not found: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def get_all_tags_from_master(master_tags: Dict) -> Set[str]:
    """Extract all tags from master tag system (categorized + flat cloud)."""
    all_tags = set()
    
    # Extract from categorized tags
    if 'core' in master_tags and 'tag_categories' in master_tags['core']:
        categories = master_tags['core']['tag_categories']
        for category_name, category_tags in categories.items():
            if isinstance(category_tags, list):
                all_tags.update(category_tags)
            elif isinstance(category_tags, dict):
                for subcategory_tags in category_tags.values():
                    if isinstance(subcategory_tags, list):
                        all_tags.update(subcategory_tags)
    
    # Extract from flat tag cloud
    if 'core' in master_tags and 'flat_tag_cloud' in master_tags['core']:
        flat_tags = master_tags['core']['flat_tag_cloud']
        if isinstance(flat_tags, list):
            all_tags.update([tag.lower() for tag in flat_tags])
    
    return all_tags


def find_similar_tags(keyword: str, master_tags: Set[str], threshold: float = 0.85) -> List[Tuple[str, float]]:
    """Find similar tags in master system using fuzzy matching."""
    similar = []
    for tag in master_tags:
        similarity = SequenceMatcher(None, keyword, tag).ratio()
        if similarity >= threshold:
            similar.append((tag, similarity))
    return sorted(similar, key=lambda x: x[1], reverse=True)


def suggest_category(keyword: str, master_tags: Dict) -> Optional[str]:
    """Suggest category for a new keyword based on existing patterns."""
    # Simple heuristic: check if keyword contains words that match category patterns
    category_keywords = {
        'functionality': ['management', 'processing', 'analysis', 'optimization', 'automation'],
        'use_case': ['workflow', 'integration', 'pipeline', 'scenario'],
        'research_type': ['research', 'study', 'analysis', 'benchmark', 'case'],
        'industry': ['industrial', 'manufacturing', 'automotive', 'aerospace'],
        'usd_specific': ['usd', 'prim', 'layer', 'variant', 'schema', 'composition'],
    }
    
    keyword_lower = keyword.lower()
    for category, patterns in category_keywords.items():
        if any(pattern in keyword_lower for pattern in patterns):
            return category
    
    return None


def check_category_limit(master_tags: Dict, category: str) -> Tuple[bool, int]:
    """Check if category is approaching limit (50 tags)."""
    if 'core' not in master_tags or 'tag_categories' not in master_tags['core']:
        return True, 0
    
    categories = master_tags['core']['tag_categories']
    if category not in categories:
        return True, 0
    
    category_tags = categories[category]
    if isinstance(category_tags, list):
        count = len(category_tags)
    elif isinstance(category_tags, dict):
        count = sum(len(tags) if isinstance(tags, list) else 0 for tags in category_tags.values())
    else:
        count = 0
    
    return count < 50, count


def propose_tags(keywords: List[str], master_tags: Dict, master_tag_set: Set[str]) -> List[Dict]:
    """Propose new tags for keywords not in master system."""
    proposals = []
    
    for keyword in keywords:
        normalized = normalize_keyword(keyword)
        
        # Skip if already in master system
        if normalized in master_tag_set:
            continue
        
        # Check for similar tags
        similar = find_similar_tags(normalized, master_tag_set)
        
        # Suggest category
        suggested_category = suggest_category(normalized, master_tags)
        
        # Check category limit
        can_add, current_count = check_category_limit(master_tags, suggested_category or 'functionality')
        
        proposal = {
            'keyword': keyword,
            'proposed_tag': normalized,
            'suggested_category': suggested_category,
            'similar_tags': similar[:3],  # Top 3 similar
            'category_limit_ok': can_add,
            'category_current_count': current_count,
            'requires_review': not can_add or len(similar) > 0 or suggested_category is None
        }
        
        proposals.append(proposal)
    
    return proposals


def generate_proposal_report(proposals: List[Dict], output_file: Optional[Path] = None) -> str:
    """Generate a human-readable tag proposal report."""
    report = []
    report.append("# Tag Proposal Report\n")
    report.append(f"Total proposals: {len(proposals)}\n\n")
    
    # Group by review status
    auto_approve = [p for p in proposals if not p['requires_review']]
    manual_review = [p for p in proposals if p['requires_review']]
    
    if auto_approve:
        report.append("## Auto-Approve Candidates\n\n")
        for prop in auto_approve:
            report.append(f"- **{prop['proposed_tag']}**")
            report.append(f"  - Category: {prop['suggested_category']}")
            report.append(f"  - Current count: {prop['category_current_count']}/50")
            report.append("")
    
    if manual_review:
        report.append("## Manual Review Required\n\n")
        for prop in manual_review:
            report.append(f"- **{prop['proposed_tag']}** (from: `{prop['keyword']}`)")
            report.append(f"  - Category: {prop['suggested_category'] or 'UNKNOWN - requires assignment'}")
            report.append(f"  - Current count: {prop['category_current_count']}/50")
            if prop['similar_tags']:
                report.append(f"  - Similar tags: {', '.join([f'{t[0]} ({t[1]:.0%})' for t in prop['similar_tags']])}")
            if not prop['category_limit_ok']:
                report.append(f"  - ⚠️ Category limit exceeded! Consolidation required before adding.")
            report.append("")
    
    report_text = '\n'.join(report)
    
    if output_file:
        output_file.write_text(report_text, encoding='utf-8')
        print(f"Report written to: {output_file}")
    
    return report_text


def main():
    parser = argparse.ArgumentParser(description='Tag Sync Tool - Extract and propose tags from documents')
    parser.add_argument('--discovery', type=Path, help='Discovery document path')
    parser.add_argument('--research', type=Path, help='Research document path')
    parser.add_argument('--master-tags', type=Path, default=DEFAULT_MASTER_TAGS, help='Master tag system YAML path')
    parser.add_argument('--propose', action='store_true', help='Generate tag proposals')
    parser.add_argument('--update-docs', action='store_true', help='Update documents with standardized tags')
    parser.add_argument('--review', action='store_true', help='Show tags requiring manual review')
    parser.add_argument('--consolidation', action='store_true', help='Show consolidation opportunities')
    parser.add_argument('--output', type=Path, help='Output file for proposals')
    
    args = parser.parse_args()
    
    # Load master tag system
    try:
        master_tags = load_master_tag_system(args.master_tags)
        master_tag_set = get_all_tags_from_master(master_tags)
        print(f"Loaded {len(master_tag_set)} tags from master system")
    except Exception as e:
        print(f"Error loading master tag system: {e}")
        return 1
    
    # Extract keywords from documents
    all_keywords = []
    sources = []
    
    if args.discovery:
        discovery_keywords = extract_keywords_from_document(args.discovery)
        if discovery_keywords:
            all_keywords.extend(discovery_keywords['all_keywords'])
            sources.append(discovery_keywords['source'])
            print(f"Extracted {len(discovery_keywords['all_keywords'])} keywords from discovery document")
    
    if args.research:
        research_keywords = extract_keywords_from_document(args.research)
        if research_keywords:
            all_keywords.extend(research_keywords['all_keywords'])
            sources.append(research_keywords['source'])
            print(f"Extracted {len(research_keywords['all_keywords'])} keywords from research document")
    
    if not all_keywords:
        print("No keywords found in documents")
        return 0
    
    # Deduplicate
    unique_keywords = list(set(all_keywords))
    print(f"Found {len(unique_keywords)} unique keywords")
    
    # Find new keywords
    new_keywords = [kw for kw in unique_keywords if normalize_keyword(kw) not in master_tag_set]
    existing_keywords = [kw for kw in unique_keywords if normalize_keyword(kw) in master_tag_set]
    
    print(f"New keywords: {len(new_keywords)}")
    print(f"Existing keywords: {len(existing_keywords)}")
    
    if new_keywords:
        print(f"\nNew keywords found: {', '.join(new_keywords[:10])}")
        if len(new_keywords) > 10:
            print(f"... and {len(new_keywords) - 10} more")
    
    # Generate proposals
    if args.propose and new_keywords:
        proposals = propose_tags(new_keywords, master_tags, master_tag_set)
        report = generate_proposal_report(proposals, args.output)
        print("\n" + report)
    
    # Show consolidation opportunities
    if args.consolidation:
        # Check category counts
        if 'core' in master_tags and 'tag_categories' in master_tags['core']:
            categories = master_tags['core']['tag_categories']
            print("\nCategory Tag Counts:")
            for category_name, category_tags in categories.items():
                if isinstance(category_tags, list):
                    count = len(category_tags)
                    if count >= 40:
                        print(f"  ⚠️ {category_name}: {count}/50 (approaching limit)")
                    else:
                        print(f"  {category_name}: {count}/50")
    
    return 0


if __name__ == '__main__':
    exit(main())
