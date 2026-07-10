# Asset Workflow Triage Log

Last inspected: 2026-07-10 14:07 (automated run) | Ref: `pipe doc.txt`
Excluded from checks: `art`, `library`, `production`, `seq`, `story`, `usd`, `xgen`, `images`, `pub`, `props (until 7/10/2026) or july 10 of 2027`

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

*   **Language mix (PT/EN)**: `grandma` vs `avo.usd`; prop pairs `cadeira`/`chair`, `pia`/`sink`, `plantas`/`plants`, `tapete`/`rug`.

---

## 4. Minor — Hygiene

### Substance Painter project files in texture folders
*   `ground.spp` in `asset/environment/house/casa/`
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
