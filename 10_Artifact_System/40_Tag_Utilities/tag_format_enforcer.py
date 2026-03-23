#!/usr/bin/env python3
"""
Tag Format Enforcer — Ensure all framework documents have Obsidian-compatible tags

Purpose: Scan the workspace for .md files with the canonical header (Version, GlobalID).
- If tags exist in legacy format (pipe, bracket, **Tags (Keywords)**): replace with #tagA #tagB #tagC
- If no tags: add #needs_tagging placeholder (user fills in or runs tag_sync_tool --propose)

Usage:
    python tag_format_enforcer.py --path <root> [--dry-run] [--include-yaml]
    python tag_format_enforcer.py  # defaults to General_Dev parent
"""

import os
import re
import sys
import argparse
from pathlib import Path
from typing import List, Optional, Tuple

# Ensure UTF-8 output on Windows
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Default: assume script is in General_Research/030_Proj_TEMPLATES/, workspace root is parent of General_Dev
SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_ROOT = SCRIPT_DIR.parent.parent  # General_Dev
PLACEHOLDER_TAG = "needs_tagging"

# Patterns to detect canonical header and extract tags
HEADER_PATTERN = re.compile(
    r'\*\*Version\*\*:.*\*\*GlobalID\*\*:',
    re.DOTALL
)

# Hashtag line: only #tags, Obsidian-compatible (already correct)
HASHTAG_LINE_PATTERN = re.compile(r'^#\w+(?:\s+#\w+)*\s*$', re.MULTILINE)

# Legacy patterns (need replacement)
LEGACY_PATTERNS = [
    (re.compile(r'(\*\*Tags\s*\(Keywords\)\*\*:\s*)([^\n]+)(\s*\n)', re.IGNORECASE), 2),  # group 2 = tag content
    (re.compile(r'(\*\*Tags:\*\*\s*\|)([^\n]+)(\|\s*\n)', re.IGNORECASE), 2),
    (re.compile(r'(\*\*Tags\*\*:\s*\|)([^\n]+)(\|\s*\n)', re.IGNORECASE), 2),
    (re.compile(r'(\*\*Tags\*\*:\s*\[)([^\]]+)(\]\s*\n)', re.IGNORECASE), 2),
    (re.compile(r'(\*\*Keywords\*\*:\s*\[)([^\]]+)(\]\s*\n)', re.IGNORECASE), 2),
    (re.compile(r'(\*\*TAGS\*\*:\s*)([^\n]+)(\s*\n)', re.IGNORECASE), 2),  # **TAGS**: tag1, tag2, tag3
]


def normalize_tag(raw: str) -> str:
    """Normalize to lowercase_with_underscores, max 30 chars."""
    raw = re.sub(r'[\[\]()]', '', raw)
    raw = raw.lower().strip()
    raw = re.sub(r'[\s\-]+', '_', raw)
    raw = re.sub(r'[^a-z0-9_]', '', raw)
    raw = re.sub(r'_+', '_', raw).strip('_')
    return raw[:30] if raw else ""


def extract_tags_from_legacy(tag_content: str) -> List[str]:
    """Extract normalized tags from pipe- or comma-separated string."""
    tags = []
    for part in re.split(r'[|,]', tag_content):
        n = normalize_tag(part)
        if n and n != PLACEHOLDER_TAG:
            tags.append(n)
    return list(dict.fromkeys(tags))  # preserve order, dedupe


def extract_existing_tags(content: str) -> Tuple[Optional[List[str]], Optional[str], Optional[int]]:
    """
    Extract tags from content. Returns (tags_list, full_match_string, start_pos).
    If hashtag format: return those tags.
    If legacy format: return extracted tags and the match for replacement.
    If none: return (None, None, None).
    """
    # Check for hashtag line (already correct format)
    for m in HASHTAG_LINE_PATTERN.finditer(content):
        line = m.group(0)
        tags = [normalize_tag(t) for t in re.findall(r'#(\w+)', line) if t]
        if tags and all(t != PLACEHOLDER_TAG for t in tags):
            return (tags, None, None)  # Already correct
        if tags and tags == [PLACEHOLDER_TAG]:
            return ([PLACEHOLDER_TAG], m.group(0), m.start())  # Placeholder, can replace

    # Check legacy formats
    for pattern, group_idx in LEGACY_PATTERNS:
        m = pattern.search(content)
        if m:
            tag_content = m.group(group_idx)
            tags = extract_tags_from_legacy(tag_content)
            return (tags, m.group(0), m.start())

    return (None, None, None)


def has_canonical_header(content: str) -> bool:
    """Check if content has the canonical framework header."""
    return bool(HEADER_PATTERN.search(content))


def find_tag_insert_position(content: str) -> int:
    """
    Find position to insert tags: after the header block (after first --- or after GlobalID line).
    Insert after the line containing GlobalID, before the next --- or ##.
    """
    lines = content.split('\n')
    insert_after = -1
    for i, line in enumerate(lines):
        if '**GlobalID**' in line or 'GlobalID' in line:
            insert_after = i
            break
    if insert_after < 0:
        return -1
    # Skip optional metadata lines (Purpose, Status, etc.) until we hit --- or ##
    for i in range(insert_after + 1, len(lines)):
        stripped = lines[i].strip()
        if stripped.startswith('---') or stripped.startswith('##'):
            return sum(len(l) + 1 for l in lines[:i])  # position before this line
        if stripped and not stripped.startswith('**'):  # Non-metadata content
            return sum(len(l) + 1 for l in lines[:i])
    return sum(len(l) + 1 for l in lines[: insert_after + 2])


def format_tags_hashtag(tags: List[str]) -> str:
    """Format tags as #tagA #tagB #tagC."""
    return ' '.join(f'#{t}' for t in tags if t)


def process_file(file_path: Path, dry_run: bool) -> Optional[str]:
    """
    Process a single file. Returns action taken: 'replaced', 'added', 'skipped', or None if no change needed.
    """
    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"  [ERROR] Could not read {file_path}: {e}")
        return None

    if not has_canonical_header(content):
        return None

    tags, match_str, match_pos = extract_existing_tags(content)

    # Already correct format with real tags
    if tags and match_str is None and PLACEHOLDER_TAG not in tags:
        return None

    # Already has placeholder
    if tags == [PLACEHOLDER_TAG] and match_str:
        return None

    # Need to replace legacy format
    if tags is not None and match_str is not None and match_pos is not None:
        new_tags_line = format_tags_hashtag(tags)
        if not dry_run:
            new_content = content[:match_pos] + new_tags_line + '\n\n' + content[match_pos + len(match_str):]
            file_path.write_text(new_content, encoding='utf-8')
        return 'replaced'

    # No tags: add placeholder
    if tags is None:
        insert_pos = find_tag_insert_position(content)
        if insert_pos < 0:
            print(f"  [WARN] Could not find insert position in {file_path}")
            return None
        new_tags_line = f'#{PLACEHOLDER_TAG}\n\n'
        if not dry_run:
            new_content = content[:insert_pos] + new_tags_line + content[insert_pos:]
            file_path.write_text(new_content, encoding='utf-8')
        return 'added'

    return None


def _walk_error_handler(exc: OSError) -> None:
    """Skip inaccessible directories instead of raising."""
    pass


def collect_md_files(root: Path, include_yaml: bool, exclude_archived: bool = True) -> List[Path]:
    """Collect .md files (and optionally .yml/.yaml) under root, excluding common non-doc paths."""
    exclude_dirs = {'node_modules', '.git', '__pycache__', 'venv', '.venv', 'dist', 'build'}
    if exclude_archived:
        exclude_dirs.add('ARCHIVED')
    suffixes = ('.md',) + (('.yml', '.yaml') if include_yaml else ())
    files = []
    for dirpath, dirnames, filenames in os.walk(root, topdown=True, onerror=_walk_error_handler):
        dirnames[:] = [d for d in dirnames if d not in exclude_dirs]
        for name in filenames:
            if Path(name).suffix.lower() in suffixes:
                files.append(Path(dirpath) / name)
    return sorted(files)


def main():
    parser = argparse.ArgumentParser(
        description='Enforce Obsidian-compatible tag format (#tagA #tagB) on all framework documents'
    )
    parser.add_argument('--path', type=Path, default=DEFAULT_ROOT,
                        help=f'Root path to scan (default: {DEFAULT_ROOT})')
    parser.add_argument('--dry-run', action='store_true',
                        help='Report changes without writing')
    parser.add_argument('--include-yaml', action='store_true',
                        help='Also process .yml/.yaml files (experimental)')
    parser.add_argument('--include-archived', action='store_true',
                        help='Include ARCHIVED directory (excluded by default)')
    args = parser.parse_args()

    root = args.path.resolve()
    if not root.exists():
        print(f"Error: path does not exist: {root}")
        return 1

    files = collect_md_files(root, args.include_yaml, exclude_archived=not args.include_archived)
    print(f"Scanning {len(files)} files under {root}")

    replaced = []
    added = []

    for f in files:
        action = process_file(f, args.dry_run)
        rel = f.relative_to(root) if root in f.parents else f
        if action == 'replaced':
            replaced.append(str(rel))
        elif action == 'added':
            added.append(str(rel))
    print(f"\nResults:")
    print(f"  Replaced (legacy -> hashtag): {len(replaced)}")
    for r in replaced:
        print(f"    - {r}")
    print(f"  Added (#{PLACEHOLDER_TAG}): {len(added)}")
    for a in added:
        print(f"    - {a}")
    print(f"  No change needed: {len(files) - len(replaced) - len(added)}")

    if args.dry_run and (replaced or added):
        print(f"\n[DRY RUN] No files were modified. Run without --dry-run to apply.")

    return 0


if __name__ == '__main__':
    exit(main())
