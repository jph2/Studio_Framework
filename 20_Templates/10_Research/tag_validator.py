#!/usr/bin/env python3
"""
Tag Validator — Verify all #tag values in docs exist in master_tag_system.yml

Purpose: Scan tagged documents, extract all #tag values, verify each exists in master.
Report orphans (tags in docs but not in master).

Usage:
    python tag_validator.py [--root <path>] [--list FILES_NEEDING_TAGGING.md] [--scan]
    python tag_validator.py --file path/to/doc.md
"""

import re
import sys
import yaml
import argparse
from pathlib import Path
from typing import List, Set, Dict, Tuple
from collections import defaultdict

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_ROOT = SCRIPT_DIR.parent.parent.parent
DEFAULT_MASTER = SCRIPT_DIR.parent.parent / "Master_Rules" / "master_tag_system.yml"

# Tags that are placeholders, structural, or special (not topic tags)
SKIP_TAGS = {
    'needs_tagging', 'category', 'tags', 'appendices', 'appendix', 'section', '_',
    'tldr', 'faq', 'executive', 'implementation', 'key', 'decision', 'evidence',
    'resources', 'deep', 'common', 'basic', 'changelog', 'development', 'installation',
    'quick', 'what', 'github', 'integration_tests', 'taga', 'tagb', 'tagc',
    'comprehensive', 'current', 'digital', 'framework', 'future', 'industrial',
    'introduction', 'list_operations', 'migration', 'overall', 'phase', 'project',
    'success', 'table', 'usdomniverse',  # markdown anchor slug, not tag
}


def is_likely_tag(s: str) -> bool:
    """Filter out numbers, hex colors, single chars, and non-tag patterns."""
    if not s or len(s) < 2:
        return False
    if s.isdigit():
        return False
    if s in SKIP_TAGS:
        return False
    # Hex color codes (3 or 6 hex digits)
    if re.match(r'^[a-f0-9]{3}$', s) or re.match(r'^[a-f0-9]{6}$', s):
        return False
    return bool(re.match(r'^[a-z][a-z0-9_]*$', s.lower()))


def load_master_tags(path: Path) -> Set[str]:
    """Load all tags from master_tag_system.yml."""
    with open(path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    tags = set()
    if 'core' in data and 'tag_categories' in data['core']:
        for cat_name, cat_data in data['core']['tag_categories'].items():
            if isinstance(cat_data, list):
                tags.update(t.lower() for t in cat_data)
            elif isinstance(cat_data, dict):
                for sub in cat_data.values():
                    if isinstance(sub, list):
                        tags.update(t.lower() for t in sub)
    if 'core' in data and 'flat_tag_cloud' in data['core']:
        flat = data['core']['flat_tag_cloud']
        if isinstance(flat, list):
            tags.update(t.lower().strip() for t in flat if isinstance(t, str))
    return tags


def extract_hashtag_tags(content: str, header_only: bool = True) -> Set[str]:
    """Extract #tag values. If header_only, only scan first 15 lines (canonical tag line)."""
    if header_only:
        lines = content.splitlines()[:15]
        text = '\n'.join(lines)
    else:
        text = content
    tags = set()
    for m in re.finditer(r'#([a-zA-Z][a-zA-Z0-9_]*)', text):
        tag = m.group(1).lower()
        if is_likely_tag(tag):
            tags.add(tag)
    return tags


def parse_file_list(list_path: Path, root: Path) -> List[Path]:
    """Parse FILES_NEEDING_TAGGING.md and return absolute paths."""
    text = list_path.read_text(encoding='utf-8')
    paths = []
    for line in text.splitlines():
        line = line.strip()
        if line.startswith('- ') and '.md' in line:
            rel = line[2:].strip().replace('\\', '/')
            full = root / rel
            if full.exists():
                paths.append(full)
    return paths


def scan_md_files(root: Path) -> List[Path]:
    """Scan for .md files under root (exclude .git, node_modules)."""
    import os
    files = []
    for dirpath, _, filenames in os.walk(root, onerror=lambda e: None):
        if '.git' in dirpath or 'node_modules' in dirpath:
            continue
        for name in filenames:
            if name.lower().endswith('.md'):
                files.append(Path(dirpath) / name)
    return sorted(files)


def main():
    ap = argparse.ArgumentParser(description='Validate tags in docs against master')
    ap.add_argument('--list', type=Path, help='Path to file list (FILES_NEEDING_TAGGING.md)')
    ap.add_argument('--file', type=Path, help='Single file to validate')
    ap.add_argument('--scan', action='store_true', help='Scan root for all .md files')
    ap.add_argument('--root', type=Path, default=DEFAULT_ROOT, help='Root path')
    ap.add_argument('--limit', type=int, default=0, help='Max files to process (0=all)')
    ap.add_argument('--full', action='store_true', help='Scan full document (default: header only)')
    args = ap.parse_args()

    root = args.root.resolve()
    master_path = root / "General_Dev" / "Master_Rules" / "master_tag_system.yml"
    if not master_path.exists():
        master_path = SCRIPT_DIR.parent.parent / "Master_Rules" / "master_tag_system.yml"
    if not master_path.exists():
        print(f"Error: master_tag_system.yml not found at {master_path}")
        return 1

    master = load_master_tags(master_path)

    if args.file:
        files = [args.file.resolve()]
        if not files[0].exists():
            print(f"Error: file not found: {files[0]}")
            return 1
    elif args.list:
        list_path = args.list if args.list.is_absolute() else root / args.list
        if not list_path.exists():
            list_path = Path(args.list)
        if not list_path.exists():
            print(f"Error: list file not found: {list_path}")
            return 1
        files = parse_file_list(list_path, root)
        if args.limit:
            files = files[:args.limit]
    elif args.scan:
        files = scan_md_files(root)
        if args.limit:
            files = files[:args.limit]
    else:
        files = scan_md_files(root)
        if args.limit:
            files = files[:args.limit]

    print(f"Validating {len(files)} files with {len(master)} master tags")
    orphans: Dict[str, List[str]] = defaultdict(list)  # tag -> [file paths]
    total_orphan_count = 0

    for fp in files:
        try:
            content = fp.read_text(encoding='utf-8')
        except Exception as e:
            print(f"  [ERROR] {fp}: {e}")
            continue
        doc_tags = extract_hashtag_tags(content, header_only=not args.full)
        if not doc_tags:
            continue
        for tag in doc_tags:
            if tag not in master:
                rel = fp.relative_to(root) if root in fp.parents else fp
                orphans[tag].append(str(rel))
                total_orphan_count += 1

    if orphans:
        print(f"\nOrphan tags (in docs but not in master): {total_orphan_count} occurrences")
        for tag in sorted(orphans.keys()):
            paths = orphans[tag]
            print(f"  #{tag}: {len(paths)} file(s)")
            for p in paths[:5]:
                print(f"    - {p}")
            if len(paths) > 5:
                print(f"    ... and {len(paths) - 5} more")
        return 1
    else:
        print("All tags valid.")
        return 0


if __name__ == '__main__':
    sys.exit(main())
