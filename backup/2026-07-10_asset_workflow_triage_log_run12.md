# Asset Workflow Triage Log

Last inspected: 2026-07-10 18:16 (automated run) | Ref: `pipe doc.txt`
Excluded from checks: `art`, `library`, `production`, `seq`, `story`, `usd`, `xgen`, `images`, `pub`

---

## 1. Critical — Missing Required Folders

Pipe doc: "all folders from here needs to exist"

*   **`avo/groom/`** — missing `default/`. The pipe doc requires `groom/default/` with xgen, houdini, cache, source_images subfolders plus scene files.
*   **`avo/look/`** — missing `default/`. The pipe doc requires `look/default/` with versioned look files (e.g. `avo_default_look.ma`). Currently only `textures/`, `work/` exist.
*   **`menino/`** — `rig/` folder absent at character root. The pipe doc requires `rig/default/` and optionally `rig/work/` and `rig/rig_code_release_area/`.

---

## 2. Naming Convention Violations

Pipe doc: "flag wrong name convention"

### Character asset files (non-compliant names)
*   `menino/groom/default/boy_groom_v001.mb` — uses `boy` instead of `menino`; expected: `menino_default_groom.ma/.mb`.

### Look / Texture category naming
*   `look/textures/character/` — casing mismatch: pipe doc says `Character` (capitalized).
*   `look/textures/prop/` — should be `props` (plural) to match the pipe doc category name: "Character, props and environment".

### Misplaced category folders inside `look/textures/prop/`
*   `look/textures/prop/character/` — a nested `character` folder exists inside the `prop` category; these textures likely belong under `look/textures/character/`.
*   `look/textures/prop/environment/` — a nested `environment` folder exists inside the `prop` category; these textures likely belong under `look/textures/environment/`.

### Character texture folders missing `default/`
*   `look/textures/character/avo/` — contains `clothes/`, `displacement/`, `hair/`, `skin/` but no `default/` folder. The pipe doc states: "Each character has a name and a default folder, we have other folders if we have variants."
*   `look/textures/character/menino/` — contains `eyes/`, `shirt/`, `skin/` but no `default/` folder. The pipe doc states: "Each character has a name and a default folder, we have other folders if we have variants."

### Texture files — wrong naming pattern
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
*   Missing variant/lod fields: `bedsheets_bed_BaseColor_ACES - ACEScg.1001.exr`
*   Missing variant/lod fields: `bedsheets_bed_Height_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `bedsheets_bed_Metalness_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `bedsheets_bed_Normal_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `bedsheets_bed_Roughness_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `bedsheets_ground_BaseColor_ACES - ACEScg.1001.exr`
*   Missing variant/lod fields: `bedsheets_ground_Height_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `bedsheets_ground_Metalness_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `bedsheets_ground_Normal_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `bedsheets_ground_Roughness_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `closet_closet_BaseColor_ACES - ACEScg.1001.exr`
*   Missing variant/lod fields: `closet_closet_Height_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `closet_closet_Metalness_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `closet_closet_Normal_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `closet_closet_Roughness_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `embroidery_Height_Utility - Raw_1001.exr`
*   Missing variant/lod fields: `embroidery_Metallic_Utility - Raw_1001.exr`
*   Missing variant/lod fields: `embroidery_Normal_Utility - Raw_1001.exr`
*   Missing variant/lod fields: `embroidery_Opacity_Utility - Raw_1001.exr`
*   Missing variant/lod fields: `embroidery_Roughness_Utility - Raw_1001.exr`
*   Missing variant/lod fields: `globe_globe_BaseColor_ACES - ACEScg.1001.exr`
*   Missing variant/lod fields: `globe_globe_Height_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `globe_globe_Metalness_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `globe_globe_Normal_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `globe_globe_Roughness_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `ioio_ioio_BaseColor_ACES - ACEScg.1001.exr`
*   Missing variant/lod fields: `ioio_ioio_Height_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `ioio_ioio_Metalness_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `ioio_ioio_Normal_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `ioio_ioio_Roughness_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `ioio_rope_BaseColor_ACES - ACEScg.1001.exr`
*   Missing variant/lod fields: `ioio_rope_Height_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `ioio_rope_Metalness_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `ioio_rope_Normal_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `ioio_rope_Roughness_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `ioio_transparent_BaseColor_ACES - ACEScg.1001.exr`
*   Missing variant/lod fields: `ioio_transparent_Height_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `ioio_transparent_Metalness_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `ioio_transparent_Normal_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `ioio_transparent_Roughness_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `matress_matress_BaseColor_ACES - ACEScg.1001.exr`
*   Missing variant/lod fields: `matress_matress_Height_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `matress_matress_Metalness_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `matress_matress_Normal_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `matress_matress_Roughness_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `menino_body_BaseColor_ACES - ACEScg.1001.exr`
*   Missing variant/lod fields: `menino_body_Height_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `menino_body_Metalness_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `menino_body_Normal_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `menino_body_Roughness_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `mountain base_mountain_BaseColor_ACES - ACEScg.1001.exr`
*   Missing variant/lod fields: `mountain base_mountain_Height_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `mountain base_mountain_Metalness_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `mountain base_mountain_Normal_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `mountain base_mountain_Roughness_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `pillow_pillow_BaseColor_ACES - ACEScg.1001.exr`
*   Missing variant/lod fields: `pillow_pillow_Height_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `pillow_pillow_Metalness_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `pillow_pillow_Normal_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `pillow_pillow_Roughness_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `pote_pote_BaseColor_ACES - ACEScg.1001.exr`
*   Missing variant/lod fields: `pote_pote_Height_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `pote_pote_Metalness_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `pote_pote_Normal_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `pote_pote_Roughness_Utility - Raw.1001.exr`
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
*   Missing variant/lod fields: `terrain_color.exr`
*   Missing variant/lod fields: `terrainbasecolor.exr`
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
*   Missing variant/lod fields: `window_window_BaseColor_ACES - ACEScg.1001.exr`
*   Missing variant/lod fields: `window_window_Height_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `window_window_Metalness_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `window_window_Normal_Utility - Raw.1001.exr`
*   Missing variant/lod fields: `window_window_Roughness_Utility - Raw.1001.exr`

---

## 3. Moderate — Structure & Consistency

*   **Language mix (PT/EN)**: `grandma` vs `avo.usd`; prop pairs `cadeira`/`chair`, `pia`/`sink`, `plantas`/`plants`, `tapete`/`rug`.
*   **`look/textures/prop/`** — 30 subdirs including stray `character/`, `environment/`, `set/`, `sets/`.

---

## 4. Minor — Hygiene

### Stray files
*   `lencol.fbx` loose at `asset/prop/` root
*   `varal.fbx` loose at `asset/prop/` root

### Cache/leftover files
*   `set_Database_galery.db` in `look/textures/prop/set/houses/`

### Substance Painter project files in texture folders
*   `bed.spp` in `asset/prop/cama/`
*   `bedsheet.spp` in `asset/prop/cama/`
*   `chair.spp` in `asset/prop/chair/`
*   `closet.spp` in `asset/prop/closet/`
*   `curtain.spp` in `asset/prop/table/default/`
*   `door.spp` in `asset/prop/door/`
*   `floor tile.spp` in `asset/prop/ground/`
*   `fogao.spp` in `asset/prop/fogao/`
*   `ground.spp` in `asset/environment/house/casa/`
*   `ground.spp` in `asset/prop/casa/`
*   `ioio.spp.lock` in `asset/prop/ioio/`
*   `ioio.spp.painter_lock` in `asset/prop/ioio/`
*   `ioio.spp` in `asset/prop/ioio/`
*   `matress.spp` in `asset/prop/cama/`
*   `mugs.spp` in `asset/prop/table/`
*   `pillow.spp` in `asset/prop/cama/`
*   `posters.spp` in `asset/prop/posters/`
*   `pote.spp` in `asset/prop/pote/`
*   `sink look.spp` in `asset/prop/sink/`
*   `table cloth.spp` in `asset/prop/table/default/`
*   `table.spp` in `asset/prop/table/default/`
*   `tapete.spp` in `asset/prop/tapete/`
*   `wal tile.spp` in `asset/prop/ground/`
*   `wall.spp` in `asset/prop/wall/`
*   `window_a.spp` in `asset/environment/sets/room/`

---

## 5. Bypassed (per pipe doc)

These items were found but are explicitly allowed by the current pipe doc:

| Category | Rule |
|---|---|
| Empty folders | "we can ignore them" |
| Spaces & hyphens in names | "not a big Problem" |
| XGen collections in wrong places | "not a problem" |
| Substance files in texture folders | "correct structure" |
| Texture format variations (.png, .rat, etc.) | "we can bypass all textures formats" |

---

### Resolved

| Item | When |
|---|---|
| `asset/enviroment` → `asset/environment` | 07-09 |
| `asset/sets` removed | 07-09 |
| `grandma/New folder` removed | 07-09 |
| `Bellflower .zip` removed from `asset/prop` | 07-09 |
| `look/texture` → 3 correct categories | 07-09 |
