# HANDOFF — learning-khmer (sole boot file · ≤3K rolling window · refresh in 1 commit at every convergence)
Updated 2026-11-12. Anything not here or reachable via POINTER MAP does not exist for boot purposes; git history is this file's archive.

## BOOT PROTOCOL (new session — follow exactly)
Read ONLY this file, then act. Verify live state only when about to assert or mutate it. Board/archive files are grep-only, never read whole. If a claim here drives an irreversible action, re-probe its source first.

## LIVE SYSTEM
- Public site: https://ysovanna.github.io/learning-khmer/ (GitHub Pages, repo `ysovanna/learning-khmer`, branch `main`, path `/`, status built + all assets 200 on 2026-11-12).
- Local working copy: `C:/HermesOS/Workspace/learning/learning-khmer` (git remote origin = that repo; main pushed, clean).
- Content source book (Khmer literacy level 1, MoEYSP 2020): `C:/Users/ysova/AppData/Local/hermes/profiles/learning/attachments/ភាសាខ្មែរ កម្រិត១-2.md` — 3.9 MB, mostly base64 images; NEVER read whole. Cleaned text-only copy (line-numbered): scratch `khmer_book_clean.md`.
- Site: lang=km, support=English, voice km-KH-PisethNeural (edge-tts). Feed: /feed.xml. PWA installed (sw.js, manifest).
- 12 units live, lesson order enforced via staggered `published` dates 2026-11-01…12: l1-a-series, l2-aa-series, l3-two-syllable, l4-final-365, l5-subscript, l6-reduced-1, l7-reduced-2, l8-diacritic-1, l9-diacritic-2, l10-independent-vowels, l11-pali-sanskrit, l12-word-meanings. Each: 8 cards / 5 Q&A + 2 surv / 18 vocab / 38 clips = 456 mp3 total, all generated OK.

## ACTIVE WORK
- None in flight. Site shipped and verified (hub, unit pages, tiles, audio, focus mode — browser QA passed locally + live).

## OWNER OPEN ITEMS
1. Voice spot-check: owner to listen to a few clips on phone; if any word mispronounced → delete that `audio/*.mp3` and re-run gen_audio for the unit with `--voice km-KH-SreymomNeural` (only that clip regenerates). Consequence of skip: rare odd pronunciations stay live.
2. Part 2 decision: owner to send កម្រិត ២ book file if wanted; pipeline is ready (same steps as Part 1).

## NEXT
- On "Part 2": copy this repo's tools/, add units l13+ with published dates after 2026-11-12, run builders in order: `python tools/u*.py` pattern → merge `_tiles_*.json` (glob needs the underscore-suffix naming!) → `tools/make_tiles.py _tiles_all.json` → per-unit `tools/gen_audio.py <slug>` → `render_unit.py` ×N → `build_stations.py` → `build_feed.py` → push.
- Optional backlog: more cards/lesson; object-drawn icons for theme vocab (currently word tiles); romanization line (Khmer has no Lyric tab — by design).

## POINTER MAP
| Question a future session might have | File |
|---|---|
| How unit content was authored / regenerate unit.json | `tools/u123.py` u456 u789 u101112 (open) |
| Word-tile SVG pipeline + pitfalls (harfbuzz, timeouts, globs) | studybook skill → `references/08-letter-tiles.md` (open) |
| Book lesson→line-range map | this file's git history commit 1st; else grep `khmer_book_clean.md` for មេរៀន headings |
| Build order / site structure rules | studybook skill SKILL.md + refs 01/02 (open) |
| Audio hang fix rationale | `tools/gen_audio.py` header comment (grep 'wait_for') |
| Site config truth | `site.json` (open, tiny) |

## HARD RULES
- Never hand-edit `<unit>/index.html` — edit unit.json + render_unit.py; hub station list only via build_stations.py.
- After editing a km string, delete its stale mp3 before re-running gen_audio (existing >1000 B files are kept).
- Strip U+FE0F / non-Khmer lookalikes from OCR text before writing unit.json — they break TTS + shaping.
- `published` dates must be staggered per lesson or station order goes alphabetical (l10 before l2).
- Owner approval required before pushing to GitHub (user request counts as approval for the task it covers).
- Khmer content = correct orthography first; OCR is a syllabus guide, not ground truth.
