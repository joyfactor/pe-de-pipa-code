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
*   `look/texture/character/avo/skin/`: all `.png` or `.png.rat`.
*   `look/texture/character/menino/eyes/`: mixed — some `.exr` ✔, some `.png` ✘ (e.g. `sam_eye_basecolor.png`, `witch_eye.png`).
*   `look/texture/character/menino/skin/`: `.exr` ✔ for body maps, but also `.png`/`.png.tx`/`.rat` variants.

### Texture files — wrong naming pattern
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1001.png.rat`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1001.png_hcm.swatch`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1001.png`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1001_Utility - sRGB - Texture_ACES - ACEScg.png.tx`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1001_sRGB - Texture_ACEScg.png.tx`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1002.png.rat`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1002.png`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1002_Utility - sRGB - Texture_ACES - ACEScg.png.tx`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1002_sRGB - Texture_ACEScg.png.tx`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1003.png.rat`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1003.png`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1003_Utility - sRGB - Texture_ACES - ACEScg.png.tx`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1003_sRGB - Texture_ACEScg.png.tx`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1004.png.rat`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1004.png`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1004_Utility - sRGB - Texture_ACES - ACEScg.png.tx`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1004_sRGB - Texture_ACEScg.png.tx`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1005.png.rat`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1005.png`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1005_Utility - sRGB - Texture_ACES - ACEScg.png.tx`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1005_sRGB - Texture_ACEScg.png.tx`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1006.png.rat`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1006.png`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1006_Utility - sRGB - Texture_ACES - ACEScg.png.tx`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1006_sRGB - Texture_ACEScg.png.tx`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1007.png.rat`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1007.png`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1007_Utility - sRGB - Texture_ACES - ACEScg.png.tx`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1007_sRGB - Texture_ACEScg.png.tx`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1008.png.rat`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1008.png`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1008_Utility - sRGB - Texture_ACES - ACEScg.png.tx`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1008_sRGB - Texture_ACEScg.png.tx`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1009.png.rat`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1009.png`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1009_Utility - sRGB - Texture_ACES - ACEScg.png.tx`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1009_sRGB - Texture_ACEScg.png.tx`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1010.png.rat`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1010.png`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1010_Utility - sRGB - Texture_ACES - ACEScg.png.tx`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1010_sRGB - Texture_ACEScg.png.tx`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Normal_Utility - Raw.1001.png.rat`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Normal_Utility - Raw.1001.png`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Normal_Utility - Raw.1002.png.rat`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Normal_Utility - Raw.1002.png`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Normal_Utility - Raw.1003.png.rat`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Normal_Utility - Raw.1003.png`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Normal_Utility - Raw.1004.png.rat`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Normal_Utility - Raw.1004.png`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Normal_Utility - Raw.1005.png.rat`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Normal_Utility - Raw.1005.png`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Normal_Utility - Raw.1006.png.rat`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Normal_Utility - Raw.1006.png`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Normal_Utility - Raw.1007.png.rat`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Normal_Utility - Raw.1007.png`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Normal_Utility - Raw.1008.png.rat`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Normal_Utility - Raw.1008.png`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Normal_Utility - Raw.1009.png.rat`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Normal_Utility - Raw.1009.png`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Normal_Utility - Raw.1010.png.rat`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Normal_Utility - Raw.1010.png`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Roughness_Utility - Raw.1001.png.rat`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Roughness_Utility - Raw.1001.png`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Roughness_Utility - Raw.1002.png.rat`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Roughness_Utility - Raw.1002.png`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Roughness_Utility - Raw.1003.png.rat`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Roughness_Utility - Raw.1003.png`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Roughness_Utility - Raw.1004.png.rat`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Roughness_Utility - Raw.1004.png`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Roughness_Utility - Raw.1005.png.rat`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Roughness_Utility - Raw.1005.png`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Roughness_Utility - Raw.1006.png.rat`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Roughness_Utility - Raw.1006.png`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Roughness_Utility - Raw.1007.png.rat`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Roughness_Utility - Raw.1007.png`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Roughness_Utility - Raw.1008.png.rat`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Roughness_Utility - Raw.1008.png`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Roughness_Utility - Raw.1009.png.rat`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Roughness_Utility - Raw.1009.png`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Roughness_Utility - Raw.1010.png.rat`
*   Extra `mtlSG` segment: `avo_skin_mtlSG_Roughness_Utility - Raw.1010.png`
*   Extra `mtlSG` segment: `menino_body_mtlSG_BaseColor_Utility - sRGB - Texture.1001.png.rat`
*   Extra `mtlSG` segment: `menino_body_mtlSG_BaseColor_Utility - sRGB - Texture.1001.png`
*   Extra `mtlSG` segment: `menino_body_mtlSG_BaseColor_Utility - sRGB - Texture.1001_Utility - sRGB - Texture_ACES - ACEScg.png.tx`
*   Extra `mtlSG` segment: `menino_body_mtlSG_BaseColor_Utility - sRGB - Texture.1001_sRGB - Texture_ACEScg.png.tx`
*   Extra `mtlSG` segment: `menino_body_mtlSG_Height_Utility - Raw.1001.png.rat`
*   Extra `mtlSG` segment: `menino_body_mtlSG_Height_Utility - Raw.1001.png`
*   Extra `mtlSG` segment: `menino_body_mtlSG_Metalness_Utility - Raw.1001.png`
*   Extra `mtlSG` segment: `menino_body_mtlSG_Normal_Utility - Raw.1001.png.rat`
*   Extra `mtlSG` segment: `menino_body_mtlSG_Normal_Utility - Raw.1001.png`
*   Extra `mtlSG` segment: `menino_body_mtlSG_Normal_Utility - Raw.1001_Raw_ACEScg.png.tx`
*   Extra `mtlSG` segment: `menino_body_mtlSG_Normal_Utility - Raw.1001_Utility - Raw_ACES - ACEScg.png.tx`
*   Extra `mtlSG` segment: `menino_body_mtlSG_Roughness_Utility - Raw.1001.png.rat`
*   Extra `mtlSG` segment: `menino_body_mtlSG_Roughness_Utility - Raw.1001.png`
*   Extra `mtlSG` segment: `menino_body_mtlSG_Roughness_Utility - Raw.1001_Utility - Raw_ACES - ACEScg.png.tx`
*   Extra `mtlSG` segment: `menino_body_mtlSG_sss_Utility - Raw.1001.png.rat`
*   Extra `mtlSG` segment: `menino_body_mtlSG_sss_Utility - Raw.1001.png`
*   Extra `mtlSG` segment: `menino_body_mtlSG_sss_Utility - Raw.1001_Raw_ACEScg.png.tx`
*   Extra `mtlSG` segment: `menino_body_mtlSG_sss_Utility - Raw.1001_Utility - Raw_ACES - ACEScg.png.tx`
*   Inconsistent asset prefix: `boy_specular.png.rat`
*   Inconsistent asset prefix: `boy_specular.png`
*   Inconsistent asset prefix: `iris_eyes_BaseColor_ACES - ACEScg.1001.exr.rat`
*   Inconsistent asset prefix: `iris_eyes_BaseColor_ACES - ACEScg.1001.exr`
*   Inconsistent asset prefix: `iris_eyes_BaseColor_ACES - ACEScg.1002.exr`
*   Inconsistent asset prefix: `iris_eyes_Height_Utility - Raw.1001.exr`
*   Inconsistent asset prefix: `iris_eyes_Height_Utility - Raw.1002.exr`
*   Inconsistent asset prefix: `iris_eyes_Metalness_Utility - Raw.1001.exr.rat`
*   Inconsistent asset prefix: `iris_eyes_Metalness_Utility - Raw.1001.exr`
*   Inconsistent asset prefix: `iris_eyes_Metalness_Utility - Raw.1002.exr.rat`
*   Inconsistent asset prefix: `iris_eyes_Metalness_Utility - Raw.1002.exr`
*   Inconsistent asset prefix: `iris_eyes_Normal_Utility - Raw.1001.exr`
*   Inconsistent asset prefix: `iris_eyes_Normal_Utility - Raw.1002.exr`
*   Inconsistent asset prefix: `iris_eyes_Roughness_Utility - Raw.1001.exr.rat`
*   Inconsistent asset prefix: `iris_eyes_Roughness_Utility - Raw.1001.exr`
*   Inconsistent asset prefix: `iris_eyes_Roughness_Utility - Raw.1002.exr.rat`
*   Inconsistent asset prefix: `iris_eyes_Roughness_Utility - Raw.1002.exr`
*   Inconsistent asset prefix: `sam_eye_basecolor.png.rat`
*   Inconsistent asset prefix: `sam_eye_basecolor.png`
*   Inconsistent asset prefix: `sam_eye_basecolor_ACES - ACES2065-1_ACES - ACEScg.png.tx`
*   Inconsistent asset prefix: `sam_eye_basecolor_Utility - sRGB - Texture_ACES - ACEScg.png.tx`
*   Inconsistent asset prefix: `sam_eye_basecolor_v002.png.rat`
*   Inconsistent asset prefix: `sam_eye_basecolor_v002.png`
*   Inconsistent asset prefix: `sam_eye_sss.png`
*   Inconsistent asset prefix: `sam_eye_ssscolor.png`
*   Missing variant/lod fields: `bedsheets_ground_BaseColor_ACES - ACEScg.1001.exr`
*   Missing variant/lod fields: `bedsheets_ground_Height_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `bedsheets_ground_Metalness_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `bedsheets_ground_Normal_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `bedsheets_ground_Roughness_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `menino_body_BaseColor_ACES - ACEScg.1001.exr`
*   Missing variant/lod fields: `menino_body_Height_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `menino_body_Metalness_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `menino_body_Normal_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `menino_body_Roughness_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `skinexported0-DM1001.exr`
*   Missing variant/lod fields: `skinexported0-DM1002.exr`
*   Missing variant/lod fields: `skinexported0-DM1003.exr`
*   Missing variant/lod fields: `skinexported0-DM1004.exr`
*   Missing variant/lod fields: `skinexported0-DM1005.exr`
*   Missing variant/lod fields: `skinexported0-DM1006.exr`
*   Missing variant/lod fields: `skinexported0-DM1007.exr`
*   Missing variant/lod fields: `skinexported0-DM1008.exr`
*   Missing variant/lod fields: `skinexported0-DM1009.exr`
*   Missing variant/lod fields: `skinexported0-DM1010.exr`
*   Missing variant/lod fields: `wall_wall_BaseColor_ACES - ACEScg.1001.exr`
*   Missing variant/lod fields: `wall_wall_Height_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `wall_wall_Metalness_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `wall_wall_Normal_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `wall_wall_Roughness_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `walls_BaseColor_ACES - ACEScg.1001.exr`
*   Missing variant/lod fields: `walls_BaseColor_ACES - ACEScg.1002.exr`
*   Missing variant/lod fields: `walls_Metalness_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `walls_Metalness_Utility - Raw.1002.exr`
*   Missing variant/lod fields: `walls_Normal_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `walls_Normal_Utility - Raw.1002.exr`
*   Missing variant/lod fields: `walls_Roughness_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `walls_Roughness_Utility - Raw.1002.exr`

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
