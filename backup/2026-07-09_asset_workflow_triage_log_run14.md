# Asset Workflow Triage Log

Last inspected: 2026-07-09 15:04:57 (automated run) | Ref: `pipe doc.txt`
Excluded from checks: `art`, `library`, `production`, `seq`, `story`, `usd`, `xgen`, `images`, `pub`

---

## 1. Critical — Missing Required Folders

Pipe doc: "all folders from here needs to exist"

*   **`avo/groom/`** — missing `default/`.
*   **`avo/look/`** — missing `default/`.
*   **`avo/rig/`** — missing `default/`.
*   **`menino`** — `rig/` absent at character root.

---

## 2. Naming Convention Violations

Pipe doc: "flag wrong name convention" — expected: `[asset]_[variant]_[lod]_[channel]_[aov]_[udim].[exr]`

### Character asset files (non-compliant names)
*   `menino/groom`: `boy_groom_v001.mb` — uses `boy` instead of `menino`, double underscore.
*   `menino/groom`: `boy_groom_v001__boy_coll.xgen` — uses `boy` instead of `menino`, double underscore.

### Texture files — wrong extension (`.png`/`.png.tx`/`.rat` instead of `.exr`)

### Texture files — wrong naming pattern

---

## 3. Moderate — Structure & Consistency

*   **Language mix (PT/EN)**: `grandma` vs `avo.usd`; prop pairs `cadeira`/`chair`, `pia`/`sink`, `plantas`/`plants`, `tapete`/`rug`.

---

## 4. Minor — Hygiene


### Empty folders
*   `clothes` under `asset/character/menino/look/textures/`
*   `default` under `asset/character/menino/look/`
*   `groom` under `asset/character/avo/`
*   `rig` under `asset/character/avo/`
*   `trunk` under `look/textures/environment/tree/`

### Substance Painter project files in texture folders
*   `.lock` in `look/textures/character/menino/eyes/`
*   `avo_skin.spp` in `asset/character/avo/look/textures/skin/`
*   `avo_skin.spp` in `look/textures/character/avo/skin/`
*   `dress.spp` in `asset/character/avo/look/textures/clothes/`
*   `dress.spp` in `look/textures/character/avo/clothes/`
*   `eye.spp` in `look/textures/character/menino/eyes/`
*   `fiber_albedo.png_hcm.swatch` in `asset/character/avo/look/textures/hair/Textures/.mayaSwatches/`
*   `fiber_albedo.png_hcm.swatch` in `look/textures/character/avo/hair/Textures/.mayaSwatches/`
*   `ground.spp` in `asset/environment/house/casa/`
*   `menino_shirt_BaseColor_Utility - sRGB - Texture.1001.png_hcm.swatch` in `look/textures/character/menino/shirt/.mayaSwatches/`
*   `menino_shirt_Normal_Utility - Raw.1001.png_hcm.swatch` in `look/textures/character/menino/shirt/.mayaSwatches/`
*   `skin_v002.spp.painter_lock` in `look/textures/character/menino/skin/skin_v002/`
*   `skin_v002.spp` in `look/textures/character/menino/skin/skin_v002/`
*   `stylized_tree 01.spp` in `look/textures/environment/vegetation/stylized_tree_1/`
*   `stylized_tree_06.spp` in `look/textures/environment/vegetation/stylized_tree_6/`
*   `wall.spp` in `look/textures/environment/wall/`
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
