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

*   **Character textures — no `default/` folders**: `look/texture/character/avo` → `clothes/`, `hair/`, `skin/`.
*   **Character textures — no `default/` folders**: `look/texture/character/menino` → `eyes/`, `shirt/`, `skin/`.
*   **Language mix (PT/EN)**: `grandma` vs `avo.usd`; prop pairs `cadeira`/`chair`, `pia`/`sink`, `plantas`/`plants`, `tapete`/`rug`.
*   **Local `menino/look/texture`** coexists with centralized `look/texture/character/menino`.
*   **`look/texture/prop/`** — 30 subdirs including stray `character/`, `environment/`, `set/`, `sets/`.

---

## 4. Minor — Hygiene


### Empty folders
*   `New Folder` under `asset/character/`
*   `New folder` under `look/texture/prop/set/`
*   `character` under `look/texture/prop/`
*   `moutain` under `look/texture/prop/sets/`
*   `pencik` under `asset/prop/`
*   `props` under `asset/environment/sets/`
*   `trunk` under `look/texture/environment/tree/`

### Stray files
*   `lencol.fbx` loose at `asset/prop/` root
*   `varal.fbx` loose at `asset/prop/` root

### Cache/leftover files
*   `set_Database_galery.db` in `look/texture/prop/set/houses/`

### Substance Painter project files in texture folders
*   `.lock` in `look/texture/character/menino/eyes/`
*   `68e5d632bea510012449359d9b8a8797.jpg_hcm.swatch` in `look/texture/prop/posters/.mayaSwatches/`
*   `8d47806f72a693e3505514aaedc580c4.jpg_hcm.swatch` in `look/texture/prop/posters/.mayaSwatches/`
*   `a nave.png_hcm.swatch` in `look/texture/prop/posters/.mayaSwatches/`
*   `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1001.png_hcm.swatch` in `look/texture/character/avo/skin/.mayaSwatches/`
*   `bed.spp` in `asset/prop/cama/`
*   `bedsheet.spp` in `asset/prop/cama/`
*   `book 03.spp` in `look/texture/prop/book/`
*   `book 04.spp` in `look/texture/prop/book/`
*   `book 05.spp` in `look/texture/prop/book/`
*   `butter.spp` in `look/texture/prop/butter/`
*   `butter.spp` in `look/texture/prop/food/butter/`
*   `c1937606c3f2db765e318b59533951b6.jpg_hcm.swatch` in `look/texture/prop/embroidery/.mayaSwatches/`
*   `chair.spp` in `asset/prop/chair/`
*   `cliff.spp` in `look/texture/prop/sets/mountain/`
*   `closet.spp` in `asset/prop/closet/`
*   `cortina.spp` in `look/texture/prop/cortina/`
*   `curtain.spp` in `asset/prop/table/default/`
*   `d838c57a192b07b87e410b88354d510a.jpg_hcm.swatch` in `look/texture/prop/embroidery/.mayaSwatches/`
*   `door.spp` in `asset/prop/door/`
*   `dress.spp` in `look/texture/character/avo/clothes/`
*   `embroidery.spp` in `look/texture/prop/embroidery/`
*   `eye.spp` in `look/texture/character/menino/eyes/`
*   `eye_D.png_hcm.swatch` in `asset/character/menino/look/texture/.mayaSwatches/`
*   `fiber_albedo.png_hcm.swatch` in `look/texture/character/avo/hair/Textures/.mayaSwatches/`
*   `floor tile.spp` in `asset/prop/ground/`
*   `fogao.spp` in `asset/prop/fogao/`
*   `globe.spp` in `look/texture/prop/globe/`
*   `ground.spp` in `asset/environment/house/casa/`
*   `ground.spp` in `asset/prop/casa/`
*   `ioio.spp.lock` in `asset/prop/ioio/`
*   `ioio.spp.painter_lock` in `asset/prop/ioio/`
*   `ioio.spp` in `asset/prop/ioio/`
*   `ioio_ioio_BaseColor_ACES - ACEScg.1001.exr_hcm.swatch` in `look/texture/prop/ioio/.mayaSwatches/`
*   `ioio_ioio_Height_Utility - Raw.1001.exr_hcm.swatch` in `look/texture/prop/ioio/.mayaSwatches/`
*   `ioio_ioio_Normal_Utility - Raw.1001.exr_hcm.swatch` in `look/texture/prop/ioio/.mayaSwatches/`
*   `ioio_ioio_Roughness_Utility - Raw.1001.exr_hcm.swatch` in `look/texture/prop/ioio/.mayaSwatches/`
*   `kitchen_window.spp` in `look/texture/prop/window/kitchen/`
*   `magazine stack.spp` in `look/texture/prop/magazine/`
*   `matress.spp` in `asset/prop/cama/`
*   `menino_shirt_BaseColor_Utility - sRGB - Texture.1001.png_hcm.swatch` in `look/texture/character/menino/shirt/.mayaSwatches/`
*   `menino_shirt_Normal_Utility - Raw.1001.png_hcm.swatch` in `look/texture/character/menino/shirt/.mayaSwatches/`
*   `mugs.spp` in `asset/prop/table/`
*   `notebook_02.spp` in `look/texture/prop/caderno/`
*   `notebook_b.spp` in `look/texture/prop/caderno/`
*   `pillow.spp` in `asset/prop/cama/`
*   `poster.spp` in `look/texture/prop/posters/`
*   `posters.spp` in `asset/prop/posters/`
*   `pote.spp` in `asset/prop/pote/`
*   `sanduiche.spp` in `look/texture/prop/food/sanduiche/`
*   `sanduiche.spp` in `look/texture/prop/sanduiche/`
*   `sink look.spp` in `asset/prop/sink/`
*   `sink.spp` in `look/texture/prop/sink/`
*   `skin.spp` in `look/texture/character/avo/skin/`
*   `skin_v002.spp.painter_lock` in `look/texture/character/menino/skin/skin_v002/`
*   `skin_v002.spp` in `look/texture/character/menino/skin/skin_v002/`
*   `stylized_tree 01.spp` in `look/texture/environment/vegetation/stylized_tree_1/`
*   `stylized_tree_06.spp` in `look/texture/environment/vegetation/stylized_tree_6/`
*   `table cloth.spp` in `asset/prop/table/default/`
*   `table.spp` in `asset/prop/table/default/`
*   `table.spp` in `look/texture/prop/table/`
*   `tapete.spp` in `asset/prop/tapete/`
*   `terrain.spp` in `look/texture/prop/set/terrain/`
*   `wal tile.spp` in `asset/prop/ground/`
*   `wall.spp` in `asset/prop/wall/`
*   `wall.spp` in `look/texture/environment/wall/`
*   `wall.spp` in `look/texture/prop/environment/wall/`
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
