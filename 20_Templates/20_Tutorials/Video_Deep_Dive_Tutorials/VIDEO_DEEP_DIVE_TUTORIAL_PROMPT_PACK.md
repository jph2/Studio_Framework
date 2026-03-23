---
arys_schema_version: '1.2'
id: a55fd119-41bd-41ac-9c24-3ad427d22d65
title: Video Deep-Dive Tutorial Prompt Pack
type: PRACTICAL
status: active
trust_level: 2
visibility: internal
created: '2026-03-03T09:30:30Z'
last_modified: '2026-03-03T09:30:30Z'
---

# Video Deep-Dive Tutorial Prompt Pack

Use this prompt pack to instantiate deep-dive tutorials from YouTube sessions.

Execution workflow reference:
- `VIDEO_DEEP_DIVE_TUTORIAL_SKILL.md`

## Trigger Prompt (short)

```text
Use the Video Deep-Dive tutorial template workflow.
Template path:
General_Tutorials/030_Proj_TEMPLATES/Video_Deep_Dive_Tutorials/VIDEO_DEEP_DIVE_TUTORIAL_TEMPLATE.md
Fill all placeholders and keep the final transcript verbatim in appendix.
```

---

## Master Generation Prompt

```text
Generate a new OpenUSD video deep-dive tutorial from this template:
General_Tutorials/030_Proj_TEMPLATES/Video_Deep_Dive_Tutorials/VIDEO_DEEP_DIVE_TUTORIAL_TEMPLATE.md

Input package:
- Video title: {{VIDEO_TITLE}}
- YouTube URL: {{VIDEO_URL}}
- Target output markdown: {{TARGET_MD_PATH}}
- Screenshot folder: {{SLIDES_FOLDER_PATH}}
- Transcript mode: {{TRANSCRIPT_MODE}}   # provided | extract
- Transcript text (if provided): {{TRANSCRIPT_TEXT}}
- Key-moment capture mode: {{CAPTURE_MODE}}  # manual | auto | hybrid
- Key-moment image folder: {{KEY_MOMENT_PICS_PATH}}
- Running story anchor: {{STORY_ANCHOR}}
- Companion script folder: {{SCRIPT_FOLDER_PATH}}

Mandatory constraints:
1) Match style used by USD GoodStart deep dives (story + production layers).
2) Keep one coherent narrative through all chapters.
3) Add chapter intro bridge paragraphs.
4) Add chapter-level video jump links.
5) Add Learn OpenUSD quick links with both number and readable name.
6) **MANDATORY — Code breakout audit:** Every screenshot that contains code (Python, USDA, or other) MUST have a breakout block immediately after the image. No exceptions.
   - For each such breakout: raw snippet, commented snippet, why it works, why it fails.
   - **Fence convention:** even for USDA snippets, use **```py** fences (readability preference) and keep `#usda 1.0` as the first line.
   - **Audit requirement:** Before finalizing, list every image filename; for each image that contains code, confirm a breakout exists. Add any missing breakouts. Report completion.
7) Keep transcript verbatim in final appendix.
8) Distinguish USD core behavior from tool-specific behavior.
9) If scripts are missing, mark labs as planned (do not fake links).
10) Include Awesome OpenUSD among top resources and in links section.

Transcript/capture method:
- If transcript mode is extract, try to extract captions first.
- If extraction fails, stop and ask user for transcript text.
- Build key moments for:
  a) chapter starts
  b) code snippets
  c) exam-style questions
  d) answer reveals
  e) pitfall explanations
- Create a key-moment index table:
  timestamp | screenshot | transcript cue | why it matters

Slide alignment:
- Pass 1: map transcript cues to image placement.
- Pass 2: verify every image is used or explicitly marked not used with reason.

Quality gate:
- Beginner-readable but technically precise.
- No absolute claims where runtime/version behavior varies.
```

---

## Input Checklist

- [ ] YouTube URL confirmed
- [ ] Transcript mode selected (`provided` or `extract`)
- [ ] Transcript text present (if provided mode)
- [ ] Screenshot folder exists
- [ ] Key-moment image folder exists or will be created
- [ ] Story anchor chosen
- [ ] Target output path chosen
- [ ] Script folder state known (exists vs planned)

---

## Post-Generation QA Prompt

```text
Review the generated tutorial for:
1) template compliance,
2) technical correctness,
3) narrative flow,
4) chapter jump usability,
5) **breakout audit:** for each image in the Slide Index (or inline), if the image contains code, a breakout block exists in the document; list any images with code that lack breakouts,
6) transcript/image alignment completeness.

Return findings by severity:
- High: trust/usability break
- Medium: consistency/accuracy risk
- Low: polish

Then apply fixes directly to the tutorial file.
```
