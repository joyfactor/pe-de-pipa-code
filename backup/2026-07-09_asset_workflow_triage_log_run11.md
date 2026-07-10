# Asset Workflow Triage Log

Last inspected: 2026-07-09 (automated run) | Ref: `pipe doc.txt`
Excluded from checks: `art`, `library`, `production`, `seq`, `story`, `usd`, `xgen`, `images`, `pub`

---

## 1. Critical — Missing Required Folders

Pipe doc: "all folders from here needs to exist"

*   **`grandma`** — Files loose at root: `avo.usd`, `grandma.mb`, `robes.obj`, `weave_dress.hip`.
*   **`grandma`** — missing all 4 departments (`model/`, `look/`, `rig/`, `groom/`).
*   **`menino/groom/`** — missing `default/`.
*   **`menino/look/`** — missing `work/` and `default/`. Has `texture/` (singular, pipe doc: `textures/`).
*   **`menino/model/`** — missing `default/`.
*   **`menino`** — `rig/` absent at character root.

---

## 2. Naming Convention Violations

Pipe doc: "flag wrong name convention" — expected: `[asset]_[variant]_[lod]_[channel]_[aov]_[udim].[exr]`

### Character asset files (non-compliant names)
*   `grandma`: `avo.usd` — does not follow `[asset]_[variant]_...` pattern.
*   `grandma`: `grandma.mb` — does not follow `[asset]_[variant]_...` pattern.
*   `grandma`: `robes.obj` — does not follow `[asset]_[variant]_...` pattern.
*   `grandma`: `weave_dress.hip` — does not follow `[asset]_[variant]_...` pattern.
*   `menino/groom`: `boy_groom_v001.mb` — uses `boy` instead of `menino`, double underscore.
*   `menino/groom`: `boy_groom_v001__boy_coll.xgen` — uses `boy` instead of `menino`, double underscore.
*   `menino/model`: `baby_sneakers_02.fbx` — generic names, no variant/lod fields.
*   `menino/model`: `body.fbx` — generic names, no variant/lod fields.
*   `menino/model`: `eyes.fbx` — generic names, no variant/lod fields.
*   `menino/model`: `hair.fbx` — generic names, no variant/lod fields.
*   `menino/model`: `menino.usd` — generic names, no variant/lod fields.
*   `menino/model`: `menino_model_v001.mb` — generic names, no variant/lod fields.
*   `menino/model`: `pants.fbx` — generic names, no variant/lod fields.
*   `menino/model`: `shirt.fbx` — generic names, no variant/lod fields.

### Texture files — wrong extension (`.png`/`.png.tx`/`.rat` instead of `.exr`)

### Texture files — wrong naming pattern

---

## 3. Moderate — Structure & Consistency

*   **Character textures — no `default/` folders**: `look/texture/character/avo` → `clothes/`, `hair/`, `skin/`.
*   **Character textures — no `default/` folders**: `look/texture/character/menino` → `eyes/`, `shirt/`, `skin/`.
*   **Language mix (PT/EN)**: `grandma` vs `avo.usd`; prop pairs `cadeira`/`chair`, `pia`/`sink`, `plantas`/`plants`, `tapete`/`rug`.
*   **Local `menino/look/texture`** coexists with centralized `look/texture/character/menino`.
*   **`look/texture/prop/`** — 30 subdirs including stray `character/`, `environment/`, `set/`, `sets/`.

---

## 4. Minor — Hygiene


### Empty folders
*   `New Folder` under `asset/character/`
*   `trunk` under `look/texture/environment/tree/`

### Substance Painter project files in texture folders
*   `.lock` in `look/texture/character/menino/eyes/`
*   `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1001.png_hcm.swatch` in `look/texture/character/avo/skin/.mayaSwatches/`
*   `dress.spp` in `look/texture/character/avo/clothes/`
*   `eye.spp` in `look/texture/character/menino/eyes/`
*   `eye_D.png_hcm.swatch` in `asset/character/menino/look/texture/.mayaSwatches/`
*   `fiber_albedo.png_hcm.swatch` in `look/texture/character/avo/hair/Textures/.mayaSwatches/`
*   `ground.spp` in `asset/environment/house/casa/`
*   `menino_shirt_BaseColor_Utility - sRGB - Texture.1001.png_hcm.swatch` in `look/texture/character/menino/shirt/.mayaSwatches/`
*   `menino_shirt_Normal_Utility - Raw.1001.png_hcm.swatch` in `look/texture/character/menino/shirt/.mayaSwatches/`
*   `skin.spp` in `look/texture/character/avo/skin/`
*   `skin_v002.spp.painter_lock` in `look/texture/character/menino/skin/skin_v002/`
*   `skin_v002.spp` in `look/texture/character/menino/skin/skin_v002/`
*   `stylized_tree 01.spp` in `look/texture/environment/vegetation/stylized_tree_1/`
*   `stylized_tree_06.spp` in `look/texture/environment/vegetation/stylized_tree_6/`
*   `wall.spp` in `look/texture/environment/wall/`
*   `window_a.spp` in `asset/environment/sets/room/`

---

### Resolved

| Item | When |
|---|---|
| `asset/enviroment` → `asset/environment` | 07-09 |
| `asset/sets` removed | 07-09 |
| `grandma/New folder` removed | 07-09 |
| `Bellflower .zip` removed from `asset/prop` | 07-09 |
| `look/texture` → 3 correct categories | 07-09 |
