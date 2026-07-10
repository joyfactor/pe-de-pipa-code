# Asset Workflow Triage Log

Last inspected: 2026-07-09 (run 3) | Ref: `pipe doc.txt`
Excluded from checks: `art`, `library`, `production`, `seq`, `story`, `usd`, `xgen`, `images`, `pub`

---

## 1. Critical — Missing Required Folders

Pipe doc: "all folders from here needs to exist"

*   **`grandma`** — missing all 4 departments (`model/`, `look/`, `rig/`, `groom/`). Files loose at root: `grandma.mb`, `avo.usd`, `robes.obj`, `weave_dress.hip`.
*   **`menino/model/`** — missing `default/`. Files in `model/` root directly.
*   **`menino/look/`** — missing `work/` and `default/`. Has `texture/` (singular, pipe doc: `textures/`).
*   **`menino/groom/`** — missing `default/`. Files in `groom/` root directly.
*   **`menino`** — `rig/` absent at character root (exists under `pub/` — excluded).

---

## 2. Naming Convention Violations

Pipe doc: "flag wrong name convention" — expected: `[asset]_[variant]_[lod]_[channel]_[aov]_[udim].[exr]`

### Character asset files (non-compliant names)
*   `grandma`: `avo.usd`, `grandma.mb`, `robes.obj`, `weave_dress.hip` — none follow `[asset]_[variant]_...` pattern.
*   `menino/model`: `baby_sneakers_02.fbx`, `body.fbx`, `eyes.fbx`, `hair.fbx`, `pants.fbx`, `shirt.fbx` — generic names, no variant/lod fields.
*   `menino/groom`: `boy_groom_v001.mb`, `boy_groom_v001__boy_coll.xgen` — uses `boy` instead of `menino`, double underscore.

### Texture files — wrong extension (`.png`/`.png.tx`/`.rat` instead of `.exr`)
*   `menino/look/texture/skin/`: all files are `.png` or `.png.tx` (e.g. `menino_skin_BaseColor_...1001.png`).
*   `menino/look/texture/shirt/`: all `.png` or `.png.tx`.
*   `look/texture/character/avo/skin/`: all `.png` or `.png.rat`.
*   `look/texture/character/menino/eyes/`: mixed — some `.exr` ✔ (e.g. `iris_eyes_BaseColor_...1001.exr`), some `.png` ✘ (e.g. `sam_eye_basecolor.png`, `witch_eye.png`).
*   `look/texture/character/menino/skin/`: `.exr` ✔ for body maps, but also `.png`/`.png.tx`/`.rat` variants.

### Texture files — wrong naming pattern
*   Spaces and hyphens: `eye_D_Utility - sRGB - Texture_ACEScg.png.tx`, `subsuface eye.jpg`, `black mask.png`, `white mask.png`.
*   Extra `mtlSG` segment not in convention: `avo_skin_mtlSG_BaseColor_...`, `menino_body_mtlSG_BaseColor_...`.
*   Inconsistent asset prefix: `sam_eye_`, `iris_eyes_`, `boy_specular` vs expected `menino_`.
*   Missing variant/lod fields in all texture filenames.

---

## 3. Moderate — Structure & Consistency

*   **Local `menino/look/texture`** coexists with centralized `look/texture/character/menino`.
*   **Character textures — no `default/` folders**: `look/texture/character/menino` → `eyes/`, `shirt/`, `skin/`; `look/texture/character/avo` → `clothes/`, `hair/`, `skin/` + loose files.
*   **`look/texture/prop/`** — 30 subdirs including stray `character/`, `environment/`, `set/`, `sets/`.
*   **Language mix (PT/EN)**: `grandma` vs `avo.usd`; prop pairs `cadeira`/`chair`, `pia`/`sink`, `plantas`/`plants`, `tapete`/`rug`.

---

## 4. Minor — Hygiene

*   **Spaces in names**: `pose library`, `books shelf`, `magazine pack`, `tundra grass`, `bed frame`, `house clean.ma`.
*   **Empty folder**: `New Folder` under `asset/character/`.
*   **Stray files at `asset/prop/` root**: `lencol.fbx`, `varal.fbx`.
*   **Cache/leftover files**: SQLite `.db` in production areas; `weave_dress_bak1.hip` in `grandma/backup`.
*   **Substance Painter project files in texture folders**: `skin.spp`, `skin_v002.spp`, `eye.spp`, `.painter_lock`, `.lock`, `.swatch` files.

---

### Resolved

| Item | When |
|---|---|
| `asset/enviroment` → `asset/environment` | 07-09 |
| `asset/sets` removed | 07-09 |
| `grandma/New folder` removed | 07-09 |
| `Bellflower .zip` removed from `asset/prop` | 07-09 |
| `look/texture` → 3 correct categories | 07-09 |
