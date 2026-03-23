#!/usr/bin/env python3
"""
Tag Semantic Proposer — Propose and apply tags based on file content semantics

Purpose: For files with #needs_tagging, extract semantic cues (filename, headers, content)
and match against master_tag_system.yml. Propose tags, optionally apply.

Usage:
    python tag_semantic_proposer.py --list FILES_NEEDING_TAGGING.md --root <path> [--dry-run]
    python tag_semantic_proposer.py --file "path/to/doc.md" [--dry-run]
"""

import re
import sys
import yaml
import argparse
from pathlib import Path
from typing import List, Set, Dict, Optional, Tuple
from difflib import SequenceMatcher

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_ROOT = SCRIPT_DIR.parent.parent.parent  # 9999_LocalRepo
DEFAULT_MASTER = SCRIPT_DIR.parent.parent / "Master_Rules" / "master_tag_system.yml"
PLACEHOLDER = "needs_tagging"
PLACEHOLDER_CATEGORY_TAGS = "#category #tags"
MAX_TAGS = 12

# Generic default tag patterns (useless, replace with rule-based)
GENERIC_PATTERN_A = "#workflow_optimization #best_practices #case_study #workflow_automation"
GENERIC_PATTERN_B = "#workflow_optimization #integration_pattern #best_practices #case_study #workflow_automation"
BATCH_TAG_DATE = "16.02.2026"


def normalize(s: str) -> str:
    """Normalize to lowercase_with_underscores, max 30 chars."""
    s = re.sub(r'[\[\]()]', '', s)
    s = s.lower().strip()
    s = re.sub(r'[\s\-]+', '_', s)
    s = re.sub(r'[^a-z0-9_]', '', s)
    s = re.sub(r'_+', '_', s).strip('_')
    return s[:30] if s else ""


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
            tags.update(normalize(t) for t in flat)
    return tags


def extract_semantic_cues(file_path: Path, content: str) -> List[str]:
    """Extract potential tag cues from filename and content."""
    cues = []
    name = file_path.stem

    # Filename patterns -> cues
    patterns = [
        (r'Blender', 'blender'),
        (r'Rhino', 'rhino'),
        (r'C4D|Cinema_4D|Cinema4D', 'c4d'),
        (r'USD|OpenUSD|openusd', 'openusd'),
        (r'Omniverse|omniverse', 'omniverse'),
        (r'ComfyUI|comfyui', 'comfyui'),
        (r'DISCOVERY', 'discovery'),
        (r'RESEARCH', 'research'),
        (r'REQUIREMENTS|Requirements', 'requirements'),
        (r'Implementation_Plan|Implementation', 'implementation'),
        (r'Handoff|HANDOFF', 'handoff'),
        (r'Template|TEMPLATE', 'template'),
        (r'Guide|GUIDE', 'guide'),
        (r'Gaussian|Splatting|3DGS|3dgs', 'gaussian_splatting'),
        (r'WRAPP|wrapp', 'packaging'),
        (r'Cursor|cursor', 'cursor'),
        (r'Agent|agent', 'agent_orchestration'),
        (r'Digital.?Twin|DigitalTwin', 'digital_twin'),
        (r'MaterialX|Materialx', 'materialx'),
        (r'ETL|ETL ', 'etl'),
        (r'Catia|CATIA|3DX|3DXML', 'catia'),
        (r'PlantSimulation|Plant.?Simulation', 'plant_simulation'),
        (r'OPC.?UA|OpcUa|opc_ua', 'opc_ua'),
        (r'Catena.?X|CatenaX|catena_x', 'catena_x'),
        (r'Isaac|IsaacSim|IsaacLab', 'omniverse'),
        (r'AAS|Asset.?Administration', 'aas_integration'),
        (r'Memex|memex', 'memex'),
        (r'Second.?Brain', 'second_brain_system'),
        (r'BREV|Brev', 'brev'),
        (r'Sphinx', 'sphinx'),
        (r'Walrus', 'walrus'),
        (r'WebRTC|Web.?RTC', 'web_rtc'),
        (r'OGC|ogc', 'ogc'),
        (r'Circular.?Economy|CircularEconomy', 'circular_economy'),
        (r'quantum', 'quantum_computing'),
        (r'machine_learning|machine.?learning', 'machine_learning'),
        (r'Asset.?Resolver|AssetResolver', 'asset_resolver'),
        (r'context.?window', 'context_window'),
        (r'Branding', 'branding'),
    ]
    for pattern, tag in patterns:
        if re.search(pattern, name, re.IGNORECASE):
            cues.append(tag)

    # Headers (##) - first 5
    headers = re.findall(r'^##\s+(.+)$', content, re.MULTILINE)[:5]
    for h in headers:
        h_norm = normalize(h)
        if len(h_norm) >= 3:
            cues.append(h_norm)

    # First 800 chars - extract significant words (3+ chars, not common stopwords)
    stop = {'the', 'and', 'for', 'with', 'this', 'that', 'from', 'are', 'was', 'has', 'have', 'been', 'will', 'can', 'not', 'but', 'you', 'your', 'our', 'all', 'any', 'how', 'when', 'what', 'which'}
    sample = content[:800]
    words = re.findall(r'\b[a-zA-Z][a-zA-Z0-9_]{2,}\b', sample)
    for w in words:
        n = normalize(w)
        if n and n not in stop and len(n) >= 4:
            cues.append(n)

    return cues


def match_cues_to_master(cues: List[str], master: Set[str], threshold: float = 0.8) -> List[str]:
    """Match cues to master tags. Exact match or fuzzy (threshold)."""
    matched = []
    seen = set()
    for cue in cues:
        c = normalize(cue)
        if not c or c == PLACEHOLDER:
            continue
        if c in master and c not in seen:
            matched.append(c)
            seen.add(c)
            continue
        best = None
        best_ratio = 0.0
        for mt in master:
            r = SequenceMatcher(None, c, mt).ratio()
            if r >= threshold and r > best_ratio:
                best = mt
                best_ratio = r
        if best and best not in seen:
            matched.append(best)
            seen.add(best)
    return matched[:MAX_TAGS]


def get_default_tags_for_path(rel_path: str) -> List[str]:
    """Default tags based on path patterns (for READMEs, templates, etc.)."""
    path_lower = rel_path.lower()
    tags = []
    if 'blender' in path_lower:
        tags.extend(['blender', 'framework_integration'])
    if 'rhino' in path_lower:
        tags.extend(['rhino', 'framework_integration'])
    if 'omniusd' in path_lower or 'omniverse' in path_lower:
        tags.extend(['omniverse', 'openusd'])
    if 'webdev' in path_lower:
        tags.extend(['framework_integration'])
    if 'readme' in path_lower:
        tags.append('framework_integration')
    if 'template' in path_lower:
        tags.extend(['framework_integration', 'best_practices'])
    if 'guide' in path_lower:
        tags.extend(['best_practices', 'framework_integration'])
    if 'mcp_profile' in path_lower:
        tags.extend(['mcp_protocol', 'framework_integration'])
    return tags


def propose_tags(file_path: Path, content: str, master: Set[str], root: Path) -> List[str]:
    """Propose tags for a file."""
    rel = str(file_path.relative_to(root)) if root in file_path.parents else str(file_path)
    cues = extract_semantic_cues(file_path, content)
    defaults = get_default_tags_for_path(rel)
    all_cues = list(dict.fromkeys(defaults + cues))
    matched = match_cues_to_master(all_cues, master)
    if not matched:
        matched = match_cues_to_master(['framework', 'documentation'], master)
    return list(dict.fromkeys(matched))[:MAX_TAGS]


def enrich_existing_tags(content: str, file_path: Path, master: Set[str]) -> Tuple[str, bool]:
    """Add missing filename-derived tags to files that already have real tags.
    Returns (new_content, changed). Only adds tags that exist in master."""
    # Find the tag line (a line of space-separated #tag values in first 15 lines)
    lines = content.splitlines()
    tag_line_idx = None
    existing_tags = []
    for i, line in enumerate(lines[:15]):
        stripped = line.strip()
        if stripped and re.match(r'^#[a-z][a-z0-9_]+(\s+#[a-z][a-z0-9_]+)*$', stripped):
            tag_line_idx = i
            existing_tags = [t.lstrip('#') for t in stripped.split()]
            break
    if tag_line_idx is None or not existing_tags:
        return content, False

    # Extract filename cues using the same patterns as extract_semantic_cues
    name = file_path.stem
    filename_patterns = [
        (r'Blender', 'blender'),
        (r'Rhino', 'rhino'),
        (r'C4D|Cinema_4D|Cinema4D', 'c4d'),
        (r'USD|OpenUSD|openusd', 'openusd'),
        (r'Omniverse|omniverse', 'omniverse'),
        (r'ComfyUI|comfyui', 'comfyui'),
        (r'MaterialX|Materialx', 'materialx'),
        (r'Catia|CATIA|3DX|3DXML', 'catia'),
    ]
    needed = []
    for pattern, tag in filename_patterns:
        if re.search(pattern, name, re.IGNORECASE):
            if tag in master and tag not in existing_tags:
                needed.append(tag)
    if not needed:
        return content, False

    # Insert needed tags at the front
    all_tags = needed + existing_tags
    all_tags = list(dict.fromkeys(all_tags))[:MAX_TAGS]
    new_tag_line = ' '.join(f'#{t}' for t in all_tags)
    lines[tag_line_idx] = new_tag_line
    return '\n'.join(lines), True


def replace_needs_tagging(content: str, new_tags: List[str]) -> Tuple[str, bool]:
    """Replace #needs_tagging or #category #tags with new tags. Returns (new_content, changed)."""
    tag_line = ' '.join(f'#{t}' for t in new_tags if t)
    patterns = [
        re.compile(r'^#needs_tagging\s*$', re.MULTILINE),
        re.compile(r'^#category\s+#tags\s*$', re.MULTILINE),
    ]
    for pattern in patterns:
        if pattern.search(content):
            new_content = pattern.sub(tag_line, content, count=1)
            return new_content, new_content != content
    return content, False


def has_generic_tags(content: str) -> bool:
    """True if content has generic default tag patterns."""
    for line in content.splitlines()[:15]:
        s = line.strip()
        if GENERIC_PATTERN_A in s or GENERIC_PATTERN_B in s:
            # Check it's mostly generic (no real content-specific tags)
            stripped = s.replace(GENERIC_PATTERN_B, '').replace(GENERIC_PATTERN_A, '').strip()
            if not stripped or len(stripped.split()) <= 1:
                return True
    return False


def has_tag_line(content: str) -> bool:
    """True if first 15 lines contain a proper #tag line."""
    for line in content.splitlines()[:15]:
        s = line.strip()
        if re.match(r'^#[a-z][a-z0-9_]+(\s+#[a-z][a-z0-9_]+)+$', s):
            return True
    return False


def has_canonical_header(content: str) -> bool:
    """True if content has **Version** or **Version:** in first 10 lines."""
    for line in content.splitlines()[:10]:
        if '**Version**' in line or '**Version:**' in line:
            return True
    return False


def retag_file(content: str, file_path: Path, master: Set[str], root: Path) -> Tuple[str, bool, str]:
    """
    Apply rule-based retag. Returns (new_content, changed, reason).
    Handles: generic tags, no tags, no header.
    """
    tags = propose_tags(file_path, content, master, root)
    tag_line = ' '.join(f'#{t}' for t in tags if t)
    lines = content.splitlines()

    # 1. No header at all -> add minimal header + tag line at top
    if not has_canonical_header(content):
        repo_name = file_path.relative_to(root).parts[0] if root in file_path.parents else "Unknown"
        header = f"**Version**: 1.0.0 | **Date**: {BATCH_TAG_DATE} | **Time**: 12:00 | **GlobalID**: 20260216_1200_{repo_name}_batch\n\n"
        new_content = header + tag_line + "\n\n" + content
        return new_content, True, "no_header"

    # 2. Generic tags -> replace that line
    for i, line in enumerate(lines[:15]):
        s = line.strip()
        if (GENERIC_PATTERN_A in s or GENERIC_PATTERN_B in s) and re.match(r'^#[a-z][a-z0-9_]+(\s+#[a-z][a-z0-9_]+)*$', s):
            stripped = s.replace(GENERIC_PATTERN_B, '').replace(GENERIC_PATTERN_A, '').strip()
            if not stripped or len(stripped.split()) <= 1:
                lines[i] = tag_line
                # Also update Version date if present
                for j, l in enumerate(lines[:10]):
                    if '**Version**' in l or '**Date**' in l:
                        lines[j] = re.sub(r'\*\*Date\*\*:\s*[\d.]+', f'**Date**: {BATCH_TAG_DATE}', l)
                        break
                return '\n'.join(lines), True, "generic_tags"
            break

    # 3. No tag line -> insert after header block (after first blank line or after **Version** line)
    if not has_tag_line(content):
        insert_idx = 0
        for i, line in enumerate(lines[:15]):
            if '**Version**' in line or '**Version:**' in line:
                insert_idx = i + 1
                break
        # Find end of header block (blank line or next ##)
        while insert_idx < len(lines) and insert_idx < 15:
            l = lines[insert_idx]
            if l.strip() == '' or l.strip().startswith('##'):
                break
            insert_idx += 1
        lines.insert(insert_idx, tag_line)
        # Update Version date
        for j, l in enumerate(lines[:10]):
            if '**Version**' in l or '**Date**' in l:
                lines[j] = re.sub(r'\*\*Date\*\*:\s*[\d.]+', f'**Date**: {BATCH_TAG_DATE}', l)
                break
        return '\n'.join(lines), True, "no_tags"

    return content, False, ""


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


def scan_for_needs_tagging(root: Path) -> List[Path]:
    """Scan for .md files containing #needs_tagging or #category #tags."""
    import os
    files = []
    for dirpath, _, filenames in os.walk(root, onerror=lambda e: None):
        if '.git' in dirpath or 'node_modules' in dirpath:
            continue
        for name in filenames:
            if not name.lower().endswith('.md'):
                continue
            p = Path(dirpath) / name
            try:
                text = p.read_text(encoding='utf-8')
                if PLACEHOLDER in text or PLACEHOLDER_CATEGORY_TAGS in text:
                    files.append(p)
            except Exception:
                pass
    return sorted(files)


def _is_archive_path(p: Path, root: Path) -> bool:
    """Skip archive/history/cache folders."""
    try:
        rel = p.relative_to(root)
    except ValueError:
        return False
    for part in rel.parts:
        pl = part.lower()
        if 'archive' in pl or 'history' in pl or '.pytest_cache' in pl:
            return True
    return False


def scan_for_retag(root: Path, scope_dirs: Optional[List[Path]] = None) -> List[Path]:
    """
    Scan for .md files needing rule-based retag: generic tags, no tags, or no header.
    Excludes archive/history paths. If scope_dirs given, only scan those.
    """
    import os
    files = []
    if scope_dirs:
        dirs_to_scan = scope_dirs
    else:
        dirs_to_scan = [root]
    for scan_root in dirs_to_scan:
        if not scan_root.exists():
            continue
        for dirpath, _, filenames in os.walk(scan_root, onerror=lambda e: None):
            if '.git' in dirpath or 'node_modules' in dirpath:
                continue
            p = Path(dirpath)
            if _is_archive_path(p, root):
                continue
            for name in filenames:
                if not name.lower().endswith('.md'):
                    continue
                fp = p / name
                try:
                    text = fp.read_text(encoding='utf-8')
                    if len(text.splitlines()) < 3:
                        continue
                    if has_generic_tags(text) or (not has_tag_line(text) and not '**TAGS**:' in text[:500]) or not has_canonical_header(text):
                        files.append(fp)
                except Exception:
                    pass
    return sorted(set(files))


def main():
    ap = argparse.ArgumentParser(description='Propose and apply semantic tags for #needs_tagging files')
    ap.add_argument('--list', type=Path, default=None,
                    help='Path to file list (FILES_NEEDING_TAGGING.md)')
    ap.add_argument('--file', type=Path, help='Single file to process')
    ap.add_argument('--scan', action='store_true', help='Scan root for files with #needs_tagging')
    ap.add_argument('--root', type=Path, default=DEFAULT_ROOT, help='Root path (9999_LocalRepo)')
    ap.add_argument('--enrich', action='store_true',
                    help='Add missing filename-derived tags to already-tagged files')
    ap.add_argument('--retag', action='store_true',
                    help='Rule-based batch: replace generic tags, add missing tags/headers. Use --root or --list.')
    ap.add_argument('--dry-run', action='store_true', help='Report only, do not write')
    ap.add_argument('--limit', type=int, default=0, help='Max files to process (0=all)')
    args = ap.parse_args()

    root = args.root.resolve()
    master_path = root / "General_Dev" / "Master_Rules" / "master_tag_system.yml"
    if not master_path.exists():
        master_path = SCRIPT_DIR.parent.parent / "Master_Rules" / "master_tag_system.yml"
    master = load_master_tags(master_path)

    if args.file:
        files = [args.file.resolve()]
        if not files[0].exists():
            print(f"Error: file not found: {files[0]}")
            return 1
    elif args.scan:
        files = scan_for_needs_tagging(root)
        if args.limit:
            files = files[:args.limit]
        print(f"Scan found {len(files)} files with #needs_tagging")
    elif args.list:
        list_path = args.list if args.list.is_absolute() else root / args.list
        if not list_path.exists():
            print(f"Error: list file not found: {list_path}")
            return 1
        files = parse_file_list(list_path, root)
        if args.limit:
            files = files[:args.limit]
    else:
        files = scan_for_needs_tagging(root)
        if args.limit:
            files = files[:args.limit]

    if args.retag:
        # Retag mode: rule-based batch for generic tags, no tags, no header
        if args.list:
            list_path = args.list if args.list.is_absolute() else root / args.list
            if not list_path.exists():
                print(f"Error: list file not found: {list_path}")
                return 1
            files = parse_file_list(list_path, root)
        else:
            # Default: scan General_Research, General_Tutorials, General_Scripts, Master_Rules, plugin repos
            scope = [
                root / "General_Dev" / "General_Research",
                root / "General_Dev" / "General_Tutorials",
                root / "General_Dev" / "General_Scripts_Extensions_Apps",
                root / "General_Dev" / "Master_Rules",
                root / "Blender_USD_MultiExport",
                root / "Blender_USD_FAKE_References",
                root / "Rhino_USD_MultiExport",
                root / "Rhino_USD_FAKE_References",
                root / "C4D_USD_MultiExport",
                root / "USD_GoodStart",
                root / "OpenUSD_GoodStart_ComfyUI_nodes",
                root / "USDcodeNIM_MCP",
                root / "usd-mcp-server",
                root / "haluszka-com-webdev",
                root / "jph2_company.openPBRbase_material_Creator",
            ]
            scope = [s for s in scope if s.exists()]
            files = scan_for_retag(root, scope)
        if args.limit:
            files = files[:args.limit]
        print(f"Retag: {len(files)} files (rule-based batch, date={BATCH_TAG_DATE})")
        updated = 0
        for fp in files:
            try:
                content = fp.read_text(encoding='utf-8')
            except Exception as e:
                print(f"  [ERROR] {fp}: {e}")
                continue
            new_content, changed, reason = retag_file(content, fp, master, root)
            if changed:
                rel = fp.relative_to(root) if root in fp.parents else fp
                print(f"  {rel} [{reason}]")
                print(f"    -> {' '.join(f'#{t}' for t in propose_tags(fp, content, master, root))}")
                if not args.dry_run:
                    fp.write_text(new_content, encoding='utf-8')
                updated += 1
        print(f"\nRetagged: {updated} files")
        if args.dry_run and updated:
            print("[DRY RUN] No files were modified. Run without --dry-run to apply.")
        return 0

    if args.enrich:
        # Enrich mode: scan all .md files and add missing filename-derived tags
        import os
        if args.file:
            all_files = [args.file.resolve()]
        else:
            all_files = []
            scan_root = root
            for dirpath, _, filenames in os.walk(scan_root, onerror=lambda e: None):
                if '.git' in dirpath or 'node_modules' in dirpath:
                    continue
                for name in filenames:
                    if name.lower().endswith('.md'):
                        all_files.append(Path(dirpath) / name)
            all_files.sort()
        if args.limit:
            all_files = all_files[:args.limit]
        print(f"Enriching {len(all_files)} files (master tags: {len(master)})")
        updated = 0
        for fp in all_files:
            try:
                content = fp.read_text(encoding='utf-8')
            except Exception as e:
                print(f"  [ERROR] {fp}: {e}")
                continue
            new_content, changed = enrich_existing_tags(content, fp, master)
            if changed:
                rel = fp.relative_to(root) if root in fp.parents else fp
                # Show what was added
                old_tags = set()
                new_tags_set = set()
                for line in content.splitlines()[:15]:
                    s = line.strip()
                    if re.match(r'^#[a-z][a-z0-9_]+(\s+#[a-z][a-z0-9_]+)*$', s):
                        old_tags = {t.lstrip('#') for t in s.split()}
                for line in new_content.splitlines()[:15]:
                    s = line.strip()
                    if re.match(r'^#[a-z][a-z0-9_]+(\s+#[a-z][a-z0-9_]+)*$', s):
                        new_tags_set = {t.lstrip('#') for t in s.split()}
                added = new_tags_set - old_tags
                print(f"  {rel}")
                print(f"    + {' '.join(f'#{t}' for t in sorted(added))}")
                if not args.dry_run:
                    fp.write_text(new_content, encoding='utf-8')
                updated += 1
        print(f"\nEnriched: {updated} files")
        if args.dry_run and updated:
            print("[DRY RUN] No files were modified. Run without --dry-run to apply.")
        return 0

    print(f"Processing {len(files)} files (master tags: {len(master)})")
    updated = 0
    for fp in files:
        try:
            content = fp.read_text(encoding='utf-8')
        except Exception as e:
            print(f"  [ERROR] {fp}: {e}")
            continue
        if PLACEHOLDER not in content and PLACEHOLDER_CATEGORY_TAGS not in content:
            continue
        tags = propose_tags(fp, content, master, root)
        new_content, changed = replace_needs_tagging(content, tags)
        if changed:
            rel = fp.relative_to(root) if root in fp.parents else fp
            print(f"  {rel}")
            print(f"    -> {' '.join(f'#{t}' for t in tags)}")
            if not args.dry_run:
                fp.write_text(new_content, encoding='utf-8')
            updated += 1
    print(f"\nUpdated: {updated} files")
    if args.dry_run and updated:
        print("[DRY RUN] No files were modified. Run without --dry-run to apply.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
