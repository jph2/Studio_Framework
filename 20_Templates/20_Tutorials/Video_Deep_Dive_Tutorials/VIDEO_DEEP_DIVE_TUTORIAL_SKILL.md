---
arys_schema_version: '1.2'
id: 1c7a95b5-a176-4bae-b59e-224eec988d54
title: Video Deep-Dive Tutorial Skill
type: PRACTICAL
status: active
trust_level: 2
visibility: internal
created: '2026-03-03T09:30:23Z'
last_modified: '2026-03-03T09:30:23Z'
---

# Video Deep-Dive Tutorial Skill

Purpose: keep the execution workflow lean and reusable while the template files
focus on output structure.

## Use this skill when

- Creating `__VIDEO_DEEP_DIVE_TUTORIAL.md` from a YouTube session
- Building a transcript-to-slide mapping
- Capturing key moments for chapter anchors and code breakouts
- Generating beginner-safe commented breakouts for screenshot code snippets

## Inputs

- `video_title`
- `video_url`
- `target_md_path`
- `slides_folder_path`
- `transcript_mode` (`provided` or `extract`)
- `transcript_text` (required when `provided`)
- `capture_mode` (`manual`, `auto`, `hybrid`)
- `key_moment_pics_path`
- `story_anchor`
- `script_folder_path`

## Workflow

1. **Transcript ingest**
   - If `provided`, use transcript as-is.
   - If `extract`, attempt caption extraction; if unavailable, request transcript.
2. **Key moment detection**
   - Identify chapter starts, code snippets, exam questions, answer reveals,
     and operational pitfalls.
3. **Capture plan**
   - Create timestamp list and screenshot naming plan.
4. **Two-pass alignment**
   - Pass 1: map transcript cues to images.
   - Pass 2: verify each image is used or explicitly marked unused.
5. **Draft generation**
   - Fill the deep-dive template.
   - Keep one narrative thread across chapters.
6. **Breakout authoring**
   - For each screenshot code block: raw snippet, commented snippet,
     why it works, why it fails.
   - **Fence convention:** use **```py** fences for both Python and USDA snippets (readability preference). Keep `#usda 1.0` as the first line for USDA snippets.
6.1 **Breakout audit (mandatory, non-negotiable)**
   - List every image in the document (from Slide Index or inline references).
   - For each image, inspect whether it contains code (Python, USDA, or other).
   - If an image contains code, a breakout block MUST exist immediately after that image.
   - Do not declare the tutorial complete until every image-with-code has a breakout.
   - Report any images with code that lack breakouts and add them.
7. **Quality gate**
   - Distinguish USD core behavior from tool-specific behavior.
   - Include Learn OpenUSD + Awesome OpenUSD links.
   - Keep transcript verbatim in appendix.

## Output guarantees

- A complete deep-dive tutorial markdown file
- Chapter jumps with video timestamps
- Key Moments Index table
- Slide Index with usage status
- Operational checklist + pitfalls appendix
- Verbatim transcript appendix
