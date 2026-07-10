# Daily Change Log

## Date: 2026-07-10

### Run 6 — Major pipe doc overhaul detected, full triage rewrite

1. **Pipe doc changes detected (significant)**:
   - File grew from 28 lines → 131 lines. Major restructure by Brendon (dated 7/09/2026).
   - **New exclusion list**: `art`, `library`, `production`, `seq`, `story`, `usd`, `xgen`, `images`, `pub`, `props` (until 7/10/2026).
   - **New bypass rules**: empty folders can be ignored; spaces & hyphens are not a problem; XGen collections in wrong places are not a problem; substance files in texture folders are correct structure; all texture formats can be bypassed.
   - **Full character folder structure** now specified: `model/default/`, `look/{work/,default/,textures/}`, `rig/{work/,default/,rig_code_release_area/}`, `groom/default/{xgen/,houdini/,cache/,source_images/}`.
   - **Look rules reversed**: "Its allowed to exist more them 1 look folder on the project" and "its allowed to have more them 1 texture folder, under main" — previous single-look-folder violation is now void.
   - **Texture categories rule retained**: 3 categories: `Character`, `props`, `environment`. Each character needs a name folder with `default/` and optional variant folders.

2. **Triage log fully rewritten**:
   - **Section 1 (Critical)**: `avo/groom/default/`, `avo/look/default/`, and `menino/rig/` still missing.
   - **Section 2 (Naming)**: `boy_groom` → should be `menino_default_groom`; `look/textures/prop` should be `props` (plural); `character` category casing mismatch; stray `character/` and `environment/` subfolders nested inside `prop/`; character texture folders missing `default/`.
   - **Section 3 (Moderate)**: Language mix PT/EN retained.
   - **Section 4 (Minor)**: Stray `.fbx` at prop root; `.db` leftover in look textures; `.spp` files listed (note: substance in texture folders is now bypassed per pipe doc, but `.spp` files in non-texture prop folders are still logged).
   - **New "Bypassed" section**: Explicitly lists items found but allowed by the updated pipe doc rules.
   - Previous items now formally excluded from checks (e.g. all `usd/assets/` texture folders, `pub/` rig duplicates, etc.) removed from the log.

3. **Backup**: `code/backup/2026-07-10_asset_workflow_triage_log_run6.md`

4. **Safeguards**: `pipe doc.txt` was NOT modified.

---

## Date: 2026-07-09

### Run 3 — pipe doc updated again, re-inspect

1. **Pipe doc changes detected**:
   - Line 20 added: `flag wrong name convention` — new rule to audit naming.
   - Line 53 changed: texture extension from `.[ext]` → `.[exr]` (specific format required).

2. **New Section 2 added — Naming Convention Violations**:
   - Character asset files: `grandma` files don't follow pattern; `menino/model` has generic `.fbx` names; `groom` uses `boy` prefix instead of `menino`.
   - Texture extensions: majority are `.png`/`.png.tx`/`.rat` instead of required `.exr`.
   - Texture naming: spaces/hyphens in filenames, extra `mtlSG` segment, inconsistent prefixes (`sam_eye`, `iris_eyes`, `boy_specular`), missing variant/lod fields.
   - Substance Painter project files (`.spp`, `.lock`, `.swatch`) found in texture folders.

3. **Updated `asset_workflow_triage_log.md`**:
   - Added full Section 2 for naming violations; renumbered sections 3→4.
   - Condensed Resolved table.
   - Backup saved: `code/backup/2026-07-09_asset_workflow_triage_log_run3.md`.

---

### Run 2 — pipe doc updated, re-inspect

1. **Pipe doc changes detected**:
   - `pub` added to the "don't check" exclusion list (line 14).
   - `all folders from here needs to exist:` rule added (line 19) — makes missing department folders a critical finding.

2. **Re-inspected `asset/character/` against updated rules**:
   - `grandma`: missing all 4 departments (`model/`, `look/`, `rig/`, `groom/`). Elevated to Critical.
   - `menino`: `rig/` absent at root (lives under `pub/` — now excluded). `model/`, `look/`, `groom/` each missing required `default/` subfolder. Elevated to Critical.
   - `menino/look/texture` (singular) noted vs pipe doc `textures/` (plural).
   - `pub/rig/` duplicate files logged for awareness only (excluded from checks).

3. **Updated `asset_workflow_triage_log.md`**:
   - Added exclusion list header reflecting `pub`.
   - New Section 1 (Critical) focused on missing required folders.
   - Removed `asset/prop` singular naming from violations (matches pipe doc as written).
   - Backup saved: `code/backup/2026-07-09_asset_workflow_triage_log_run2.md`.

---

### Run 1 — initial daily triage

1. **Dry-inspect run against `pipe doc.txt`**:
   - Re-scanned the full `asset/`, `look/texture/`, and `code/` directory trees.
   - Compared live filesystem state to every item in the existing `asset_workflow_triage_log.md`.

2. **Resolved items confirmed & removed from log**:
   - `asset/enviroment` misspelling → renamed to `asset/environment` ✔
   - `asset/sets` undocumented root → removed ✔
   - `asset/character/grandma/New folder` → removed ✔
   - `asset/prop/TCom_3dplant_Bellflower_001.zip` → removed ✔
   - `look/texture` root categories → now 3 correct folders (`character`, `environment`, `prop`) ✔

3. **Updated `asset_workflow_triage_log.md`**:
   - Condensed from 64 lines → 46 lines (28% reduction).
   - Merged resolved items into a compact "Resolved" table.
   - Added newly observed detail: `look/texture/prop` contains 30 mixed subdirs including stray `character`/`environment`/`set`/`sets` folders.
   - Added: `lencol.fbx` and `varal.fbx` loose at `asset/prop/` root.
   - `asset/environment/kitchen` now has content (no longer empty).

4. **Backup**:
   - Saved pre-update snapshot: `code/backup/2026-07-09_asset_workflow_triage_log.md`.

5. **Safeguards**:
   - `pipe doc.txt` was NOT modified.
   - No files moved, deleted, or renamed.

---

## Date: 2026-07-08

### Summary of Changes

1. **Updated Triage Log (`asset_workflow_triage_log.md`)**:
   - Realigned the look dev and texture specifications with the authoritative guidelines in `pipe doc.txt` (the main doc).
   - Removed instructions suggesting that textures should be local to assets.
   - Identified and listed the following new workflow violations based on `pipe doc.txt`:
     - **Missing Root Look Folder**: The repository lacks the required single root `look` folder.
     - **Incorrect Texture Location**: The `texture` folder is at the root of the project rather than nested under `look` (`look/texture`).
     - **Multiple Look/Texture Folders**: Individual assets contain local look/texture subfolders (e.g. `asset/character/menino/look`, `usd/assets/.../textures`), violating the single centralized look folder rule (except for `library`, which is exempt).
     - **Incorrect Texture Categories**: The `texture` folder contains 32 subfolders rather than exactly three categories (`Character`, `props`, and `environment`).
     - **Incorrect Character Texture Structure**: Character texture directories (e.g. `texture/character/avo` and `texture/character/menino`) do not contain a `default` folder as required, but are instead structured directly by map category (e.g. `skin`, `hair`, `clothes`).

2. **Created Backup Folder & Files**:
   - Created the backup folder `c:\joyfactor animation\pe de pipa\code\backup\`.
   - Saved a backup copy of the original triage log at `c:\joyfactor animation\pe de pipa\code\backup\2026-07-08_asset_workflow_triage_log_orig.md`.

3. **Document Safeguards**:
   - Verified that the source document `pipe doc.txt` was not modified in any way, strictly adhering to the constraint.


### Run 6 — Automated schedule scan

1. **Automated Triage Run**: Scanned workspace for structural and naming rules.
2. **Log Updated**: Refreshed `asset_workflow_triage_log.md` with latest findings.
3. **Backup Saved**: `code/backup/2026-07-09_asset_workflow_triage_log_run6.md`.


### Run 7 — Automated schedule scan

1. **Automated Triage Run**: Scanned workspace for structural and naming rules.
2. **Log Updated**: Refreshed `asset_workflow_triage_log.md` with latest findings.
3. **Backup Saved**: `code/backup/2026-07-09_asset_workflow_triage_log_run7.md`.


### Run 8 — Automated schedule scan

1. **Automated Triage Run**: Scanned workspace for structural and naming rules.
2. **Log Updated**: Refreshed `asset_workflow_triage_log.md` with latest findings.
3. **Backup Saved**: `code/backup/2026-07-09_asset_workflow_triage_log_run8.md`.


### Run 9 — Automated schedule scan

1. **Automated Triage Run**: Scanned workspace for structural and naming rules.
2. **Log Updated**: Refreshed `asset_workflow_triage_log.md` with latest findings.
3. **Backup Saved**: `code/backup/2026-07-09_asset_workflow_triage_log_run9.md`.


### Run 10 — Automated schedule scan

1. **Automated Triage Run**: Scanned workspace for structural and naming rules.
2. **Log Updated**: Refreshed `asset_workflow_triage_log.md` with latest findings.
3. **Backup Saved**: `code/backup/2026-07-09_asset_workflow_triage_log_run10.md`.


### Run 11 — Automated schedule scan

1. **Automated Triage Run**: Scanned workspace for structural and naming rules.
2. **Log Updated**: Refreshed `asset_workflow_triage_log.md` with latest findings.
3. **Backup Saved**: `code/backup/2026-07-09_asset_workflow_triage_log_run11.md`.


### Run 12 — Automated schedule scan

1. **Automated Triage Run**: Scanned workspace for structural and naming rules.
2. **Log Updated**: Refreshed `asset_workflow_triage_log.md` with latest findings.
3. **Backup Saved**: `code/backup/2026-07-09_asset_workflow_triage_log_run12.md`.


### Run 13 — Automated schedule scan

1. **Automated Triage Run**: Scanned workspace for structural and naming rules.
2. **Log Updated**: Refreshed `asset_workflow_triage_log.md` with latest findings.
3. **Backup Saved**: `code/backup/2026-07-09_asset_workflow_triage_log_run13.md`.


### Run 14 — Automated schedule scan

1. **Automated Triage Run**: Scanned workspace for structural and naming rules.
2. **Log Updated**: Refreshed `asset_workflow_triage_log.md` with latest findings.
3. **Backup Saved**: `code/backup/2026-07-09_asset_workflow_triage_log_run14.md`.


### Run 15 — Automated schedule scan

1. **Automated Triage Run**: Scanned workspace for structural and naming rules.
2. **Log Updated**: Refreshed `asset_workflow_triage_log.md` with latest findings.
3. **Backup Saved**: `code/backup/2026-07-09_asset_workflow_triage_log_run15.md`.


### Run 4 — Automated schedule scan

1. **Automated Triage Run**: Scanned workspace for structural and naming rules.
2. **Log Updated**: Refreshed `asset_workflow_triage_log.md` with latest findings.
3. **Backup Saved**: `code/backup/2026-07-10_asset_workflow_triage_log_run4.md`.


### Run 5 — Automated schedule scan

1. **Automated Triage Run**: Scanned workspace for structural and naming rules.
2. **Log Updated**: Refreshed `asset_workflow_triage_log.md` with latest findings.
3. **Backup Saved**: `code/backup/2026-07-10_asset_workflow_triage_log_run5.md`.


### Run 9 — Automated schedule scan

1. **Automated Triage Run**: Scanned workspace for structural and naming rules.
2. **Log Updated**: Refreshed `asset_workflow_triage_log.md` with latest findings.
3. **Backup Saved**: `code/backup/2026-07-10_asset_workflow_triage_log_run9.md`.


### Run 10 — Automated schedule scan

1. **Automated Triage Run**: Scanned workspace for structural and naming rules.
2. **Log Updated**: Refreshed `asset_workflow_triage_log.md` with latest findings.
3. **Backup Saved**: `code/backup/2026-07-10_asset_workflow_triage_log_run10.md`.


### Run 11 — Automated schedule scan

1. **Automated Triage Run**: Scanned workspace for structural and naming rules.
2. **Log Updated**: Refreshed `asset_workflow_triage_log.md` with latest findings.
3. **Backup Saved**: `code/backup/2026-07-10_asset_workflow_triage_log_run11.md`.
