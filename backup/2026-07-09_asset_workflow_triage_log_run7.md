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
*   Inconsistent asset prefix: `boy_specular.png.rat`
*   Inconsistent asset prefix: `boy_specular.png`
*   Inconsistent asset prefix: `sam_eye_basecolor.png.rat`
*   Inconsistent asset prefix: `sam_eye_basecolor.png`
*   Inconsistent asset prefix: `sam_eye_basecolor_v002.png.rat`
*   Inconsistent asset prefix: `sam_eye_basecolor_v002.png`
*   Inconsistent asset prefix: `sam_eye_sss.png`
*   Inconsistent asset prefix: `sam_eye_ssscolor.png`
*   Missing variant/lod fields: `terrain_color.exr`
*   Missing variant/lod fields: `terrainbasecolor.exr`
*   Spaces and hyphens: `138d69ecc6a540e94501dfc3a938d62c_ACES - ACES2065-1_ACES - ACEScg.jpg.tx`
*   Spaces and hyphens: `1d7512139e7ad15bc73e8bffbf6f13a9_ACES - ACES2065-1_ACES - ACEScg.jpg.tx`
*   Spaces and hyphens: `4e39ff82f30ae3454882a6b2040c653587ff3dfb-3000x1959.avif`
*   Spaces and hyphens: `68e5d632bea510012449359d9b8a8797_ACES - ACES2065-1_ACES - ACEScg.jpg.tx`
*   Spaces and hyphens: `68e5d632bea510012449359d9b8a8797_ACES2065-1_ACEScg.jpg.tx`
*   Spaces and hyphens: `772ff681e0df3bf9a55934a722f811ff_ACES - ACES2065-1_ACES - ACEScg.jpg.tx`
*   Spaces and hyphens: `772ff681e0df3bf9a55934a722f811ff_ACES - ACES2065-1_ACEScg.jpg.tx`
*   Spaces and hyphens: `8d47806f72a693e3505514aaedc580c4_ACES - ACES2065-1_ACES - ACEScg.jpg.tx`
*   Spaces and hyphens: `8d47806f72a693e3505514aaedc580c4_ACES2065-1_ACEScg.jpg.tx`
*   Spaces and hyphens: `A-General-Map-of-the-World-or-Terraqueous-Globe_Samuel-Dunn.jpg`
*   Spaces and hyphens: `Ladrão-de-Raios.jpg`
*   Spaces and hyphens: `a nave.png_hcm.swatch`
*   Spaces and hyphens: `a nave.png`
*   Spaces and hyphens: `a nave_Rec.1886 - Curve_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `a nave_Rec.1886 - Curve_ACEScg.png.tx`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1001.png.rat`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1001.png_hcm.swatch`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1001.png`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1001_Utility - sRGB - Texture_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1001_sRGB - Texture_ACEScg.png.tx`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1002.png.rat`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1002.png`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1002_Utility - sRGB - Texture_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1002_sRGB - Texture_ACEScg.png.tx`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1003.png.rat`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1003.png`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1003_Utility - sRGB - Texture_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1003_sRGB - Texture_ACEScg.png.tx`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1004.png.rat`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1004.png`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1004_Utility - sRGB - Texture_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1004_sRGB - Texture_ACEScg.png.tx`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1005.png.rat`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1005.png`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1005_Utility - sRGB - Texture_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1005_sRGB - Texture_ACEScg.png.tx`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1006.png.rat`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1006.png`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1006_Utility - sRGB - Texture_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1006_sRGB - Texture_ACEScg.png.tx`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1007.png.rat`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1007.png`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1007_Utility - sRGB - Texture_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1007_sRGB - Texture_ACEScg.png.tx`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1008.png.rat`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1008.png`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1008_Utility - sRGB - Texture_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1008_sRGB - Texture_ACEScg.png.tx`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1009.png.rat`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1009.png`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1009_Utility - sRGB - Texture_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1009_sRGB - Texture_ACEScg.png.tx`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1010.png.rat`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1010.png`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1010_Utility - sRGB - Texture_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `avo_skin_mtlSG_BaseColor_Utility - sRGB - Texture.1010_sRGB - Texture_ACEScg.png.tx`
*   Spaces and hyphens: `avo_skin_mtlSG_Normal_Utility - Raw.1001.png.rat`
*   Spaces and hyphens: `avo_skin_mtlSG_Normal_Utility - Raw.1001.png`
*   Spaces and hyphens: `avo_skin_mtlSG_Normal_Utility - Raw.1002.png.rat`
*   Spaces and hyphens: `avo_skin_mtlSG_Normal_Utility - Raw.1002.png`
*   Spaces and hyphens: `avo_skin_mtlSG_Normal_Utility - Raw.1003.png.rat`
*   Spaces and hyphens: `avo_skin_mtlSG_Normal_Utility - Raw.1003.png`
*   Spaces and hyphens: `avo_skin_mtlSG_Normal_Utility - Raw.1004.png.rat`
*   Spaces and hyphens: `avo_skin_mtlSG_Normal_Utility - Raw.1004.png`
*   Spaces and hyphens: `avo_skin_mtlSG_Normal_Utility - Raw.1005.png.rat`
*   Spaces and hyphens: `avo_skin_mtlSG_Normal_Utility - Raw.1005.png`
*   Spaces and hyphens: `avo_skin_mtlSG_Normal_Utility - Raw.1006.png.rat`
*   Spaces and hyphens: `avo_skin_mtlSG_Normal_Utility - Raw.1006.png`
*   Spaces and hyphens: `avo_skin_mtlSG_Normal_Utility - Raw.1007.png.rat`
*   Spaces and hyphens: `avo_skin_mtlSG_Normal_Utility - Raw.1007.png`
*   Spaces and hyphens: `avo_skin_mtlSG_Normal_Utility - Raw.1008.png.rat`
*   Spaces and hyphens: `avo_skin_mtlSG_Normal_Utility - Raw.1008.png`
*   Spaces and hyphens: `avo_skin_mtlSG_Normal_Utility - Raw.1009.png.rat`
*   Spaces and hyphens: `avo_skin_mtlSG_Normal_Utility - Raw.1009.png`
*   Spaces and hyphens: `avo_skin_mtlSG_Normal_Utility - Raw.1010.png.rat`
*   Spaces and hyphens: `avo_skin_mtlSG_Normal_Utility - Raw.1010.png`
*   Spaces and hyphens: `avo_skin_mtlSG_Roughness_Utility - Raw.1001.png.rat`
*   Spaces and hyphens: `avo_skin_mtlSG_Roughness_Utility - Raw.1001.png`
*   Spaces and hyphens: `avo_skin_mtlSG_Roughness_Utility - Raw.1002.png.rat`
*   Spaces and hyphens: `avo_skin_mtlSG_Roughness_Utility - Raw.1002.png`
*   Spaces and hyphens: `avo_skin_mtlSG_Roughness_Utility - Raw.1003.png.rat`
*   Spaces and hyphens: `avo_skin_mtlSG_Roughness_Utility - Raw.1003.png`
*   Spaces and hyphens: `avo_skin_mtlSG_Roughness_Utility - Raw.1004.png.rat`
*   Spaces and hyphens: `avo_skin_mtlSG_Roughness_Utility - Raw.1004.png`
*   Spaces and hyphens: `avo_skin_mtlSG_Roughness_Utility - Raw.1005.png.rat`
*   Spaces and hyphens: `avo_skin_mtlSG_Roughness_Utility - Raw.1005.png`
*   Spaces and hyphens: `avo_skin_mtlSG_Roughness_Utility - Raw.1006.png.rat`
*   Spaces and hyphens: `avo_skin_mtlSG_Roughness_Utility - Raw.1006.png`
*   Spaces and hyphens: `avo_skin_mtlSG_Roughness_Utility - Raw.1007.png.rat`
*   Spaces and hyphens: `avo_skin_mtlSG_Roughness_Utility - Raw.1007.png`
*   Spaces and hyphens: `avo_skin_mtlSG_Roughness_Utility - Raw.1008.png.rat`
*   Spaces and hyphens: `avo_skin_mtlSG_Roughness_Utility - Raw.1008.png`
*   Spaces and hyphens: `avo_skin_mtlSG_Roughness_Utility - Raw.1009.png.rat`
*   Spaces and hyphens: `avo_skin_mtlSG_Roughness_Utility - Raw.1009.png`
*   Spaces and hyphens: `avo_skin_mtlSG_Roughness_Utility - Raw.1010.png.rat`
*   Spaces and hyphens: `avo_skin_mtlSG_Roughness_Utility - Raw.1010.png`
*   Spaces and hyphens: `basket ball_1001_BaseColor.png`
*   Spaces and hyphens: `basket ball_1001_Height.png`
*   Spaces and hyphens: `basket ball_1001_Metalness.png`
*   Spaces and hyphens: `basket ball_1001_Normal.png`
*   Spaces and hyphens: `basket ball_1001_Normal.tx`
*   Spaces and hyphens: `basket ball_1001_Roughness.png`
*   Spaces and hyphens: `bed frame_wood_BaseColor_Utility - sRGB - Texture.1001.png.rat`
*   Spaces and hyphens: `bed frame_wood_BaseColor_Utility - sRGB - Texture.1001.png`
*   Spaces and hyphens: `bed frame_wood_Height_Utility - Raw.1001.png`
*   Spaces and hyphens: `bed frame_wood_Metalness_Utility - Raw.1001.png`
*   Spaces and hyphens: `bed frame_wood_Normal_Utility - Raw.1001.png.rat`
*   Spaces and hyphens: `bed frame_wood_Normal_Utility - Raw.1001.png`
*   Spaces and hyphens: `bed frame_wood_Roughness_Utility - Raw.1001.png.rat`
*   Spaces and hyphens: `bed frame_wood_Roughness_Utility - Raw.1001.png`
*   Spaces and hyphens: `bed_sheet_sheet bed_BaseColor_ACES - ACEScg.1001.exr`
*   Spaces and hyphens: `bed_sheet_sheet bed_Normal_Utility - Raw.1001.exr`
*   Spaces and hyphens: `bedsheets_bed_BaseColor_ACES - ACEScg.1001.exr`
*   Spaces and hyphens: `bedsheets_bed_Height_Utility - Raw.1001.exr`
*   Spaces and hyphens: `bedsheets_bed_Metalness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `bedsheets_bed_Normal_Utility - Raw.1001.exr`
*   Spaces and hyphens: `bedsheets_bed_Roughness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `bedsheets_ground_BaseColor_ACES - ACEScg.1001.exr`
*   Spaces and hyphens: `bedsheets_ground_Height_Utility - Raw.1001.exr`
*   Spaces and hyphens: `bedsheets_ground_Metalness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `bedsheets_ground_Normal_Utility - Raw.1001.exr`
*   Spaces and hyphens: `bedsheets_ground_Roughness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `black mask.png.rat`
*   Spaces and hyphens: `black mask.png`
*   Spaces and hyphens: `book 03.spp`
*   Spaces and hyphens: `book 04.spp`
*   Spaces and hyphens: `book 05.spp`
*   Spaces and hyphens: `book_composition_03_book_BaseColor_ACES - ACEScg.1001.exr`
*   Spaces and hyphens: `book_composition_03_book_Height_Utility - Raw.1001.exr`
*   Spaces and hyphens: `book_composition_03_book_Metalness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `book_composition_03_book_Normal_Utility - Raw.1001.exr`
*   Spaces and hyphens: `book_composition_03_book_Roughness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `book_composition_05_book_BaseColor_ACES - ACEScg.1001.exr`
*   Spaces and hyphens: `book_composition_05_book_Height_Utility - Raw.1001.exr`
*   Spaces and hyphens: `book_composition_05_book_Metalness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `book_composition_05_book_Normal_Utility - Raw.1001.exr`
*   Spaces and hyphens: `book_composition_05_book_Roughness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `book_composition_06_book_BaseColor_ACES - ACEScg.1001.exr`
*   Spaces and hyphens: `book_composition_06_book_Height_Utility - Raw.1001.exr`
*   Spaces and hyphens: `book_composition_06_book_Metalness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `book_composition_06_book_Normal_Utility - Raw.1001.exr`
*   Spaces and hyphens: `book_composition_06_book_Roughness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `br-11134207-7r98o-ly6uljh4wjxh3b.jpeg`
*   Spaces and hyphens: `br-11134207-7r98o-mb2lq33fz3095e.jpeg`
*   Spaces and hyphens: `bread_basket_stylized_woven_basket_BaseColor_Utility - sRGB - Texture.1001.png`
*   Spaces and hyphens: `bread_basket_stylized_woven_basket_Normal_Utility - Raw.1001.png`
*   Spaces and hyphens: `bush_a_bush_a_BaseColor_Utility - sRGB - Texture.1001.png`
*   Spaces and hyphens: `bush_a_bush_a_Height_Utility - Raw.1001.png`
*   Spaces and hyphens: `bush_a_bush_a_Metalness_Utility - Raw.1001.png`
*   Spaces and hyphens: `bush_a_bush_a_Normal_Utility - Raw.1001.png`
*   Spaces and hyphens: `bush_a_bush_a_Roughness_Utility - Raw.1001.png`
*   Spaces and hyphens: `c1937606c3f2db765e318b59533951b6_ACES - ACES2065-1_ACES - ACEScg.jpg.tx`
*   Spaces and hyphens: `c1937606c3f2db765e318b59533951b6_ACES2065-1_ACEScg.jpg.tx`
*   Spaces and hyphens: `closet_closet_BaseColor_ACES - ACEScg.1001.exr`
*   Spaces and hyphens: `closet_closet_Height_Utility - Raw.1001.exr`
*   Spaces and hyphens: `closet_closet_Metalness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `closet_closet_Normal_Utility - Raw.1001.exr`
*   Spaces and hyphens: `closet_closet_Roughness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `curtain_curtain_BaseColor_Utility - sRGB - Texture.1001.png.rat`
*   Spaces and hyphens: `curtain_curtain_BaseColor_Utility - sRGB - Texture.1001.png`
*   Spaces and hyphens: `curtain_curtain_Height_Utility - Raw.1001.png`
*   Spaces and hyphens: `curtain_curtain_Metalness_Utility - Raw.1001.png.rat`
*   Spaces and hyphens: `curtain_curtain_Metalness_Utility - Raw.1001.png`
*   Spaces and hyphens: `curtain_curtain_Normal_Utility - Raw.1001.png.rat`
*   Spaces and hyphens: `curtain_curtain_Normal_Utility - Raw.1001.png`
*   Spaces and hyphens: `curtain_curtain_Roughness_Utility - Raw.1001.png`
*   Spaces and hyphens: `d838c57a192b07b87e410b88354d510a_ACES - ACES2065-1_ACES - ACEScg.jpg.tx`
*   Spaces and hyphens: `decals_difuse_ACES - ACES2065-1_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `decals_difuse_Utility - sRGB - Texture_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `decals_opacity_ACES - ACES2065-1_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `desk_desk_BaseColor_Utility - sRGB - Texture.1001.png`
*   Spaces and hyphens: `dress_grandma_dress_BaseColor_Utility - sRGB - Texture.1001.png.rat`
*   Spaces and hyphens: `dress_grandma_dress_BaseColor_Utility - sRGB - Texture.1001.png`
*   Spaces and hyphens: `dress_grandma_dress_BaseColor_Utility - sRGB - Texture.1001_Utility - sRGB - Texture_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `dress_grandma_dress_Height_Utility - Raw.1001.png`
*   Spaces and hyphens: `dress_grandma_dress_Metalness_Utility - Raw.1001.png`
*   Spaces and hyphens: `dress_grandma_dress_Normal_Utility - Raw.1001.png.rat`
*   Spaces and hyphens: `dress_grandma_dress_Normal_Utility - Raw.1001.png`
*   Spaces and hyphens: `dress_grandma_dress_Roughness_Utility - Raw.1001.png`
*   Spaces and hyphens: `dune messiah.jpg`
*   Spaces and hyphens: `ecfcd477c059d6daa6e3e41b02376256_ACES - ACES2065-1_ACES - ACEScg.jpg.tx`
*   Spaces and hyphens: `embroidery a.tif`
*   Spaces and hyphens: `embroidery_Base_color_ACES - ACEScg_1001.exr`
*   Spaces and hyphens: `embroidery_Height_Utility - Raw_1001.exr`
*   Spaces and hyphens: `embroidery_Metallic_Utility - Raw_1001.exr`
*   Spaces and hyphens: `embroidery_Normal_OpenGL_Utility - Raw_1001.exr`
*   Spaces and hyphens: `embroidery_Normal_Utility - Raw_1001.exr`
*   Spaces and hyphens: `embroidery_Opacity_Utility - Raw_1001.exr`
*   Spaces and hyphens: `embroidery_Roughness_Utility - Raw_1001.exr`
*   Spaces and hyphens: `eye_D_Utility - sRGB - Texture_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `eye_D_sRGB - Texture_ACEScg.png.tx`
*   Spaces and hyphens: `fabric_BaseColor_Utility - sRGB - Texture.png`
*   Spaces and hyphens: `fabric_Metalness_Utility - Raw.png`
*   Spaces and hyphens: `fabric_Normal_Utility - Raw.png`
*   Spaces and hyphens: `fabric_Roughness_Utility - Raw.png`
*   Spaces and hyphens: `fiber_albedo_ACES - ACES2065-1_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `fiber_albedo_Utility - sRGB - Texture_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `fiber_albedo_sRGB - Texture_ACEScg.png.tx`
*   Spaces and hyphens: `fiber_alpha_ACES - ACES2065-1_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `fiber_alpha_ACES2065-1_ACEScg.png.tx`
*   Spaces and hyphens: `fogao_fogao_mtl_BaseColor_Utility - sRGB - Texture.1001.png`
*   Spaces and hyphens: `fogao_fogao_mtl_BaseColor_Utility - sRGB - Texture.1002.png`
*   Spaces and hyphens: `fogao_fogao_mtl_Metalness_Utility - Raw.1001.png`
*   Spaces and hyphens: `fogao_fogao_mtl_Metalness_Utility - Raw.1002.png`
*   Spaces and hyphens: `fogao_fogao_mtl_Normal_Utility - Raw.1001.png`
*   Spaces and hyphens: `fogao_fogao_mtl_Normal_Utility - Raw.1002.png`
*   Spaces and hyphens: `fogao_fogao_mtl_Roughness_Utility - Raw.1001.png`
*   Spaces and hyphens: `fogao_fogao_mtl_Roughness_Utility - Raw.1002.png`
*   Spaces and hyphens: `folded_poster_with_tape_01_sign_BaseColor_ACES - ACEScg.1001.exr`
*   Spaces and hyphens: `folded_poster_with_tape_01_sign_Height_Utility - Raw.1001.exr`
*   Spaces and hyphens: `folded_poster_with_tape_01_sign_Metalness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `folded_poster_with_tape_01_sign_Normal_Utility - Raw.1001.exr`
*   Spaces and hyphens: `folded_poster_with_tape_01_sign_Roughness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `folded_poster_with_tape_01_sign_elis_BaseColor_ACES - ACEScg.1001.exr`
*   Spaces and hyphens: `folded_poster_with_tape_01_sign_elis_Height_Utility - Raw.1001.exr`
*   Spaces and hyphens: `folded_poster_with_tape_01_sign_elis_Metalness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `folded_poster_with_tape_01_sign_elis_Normal_Utility - Raw.1001.exr`
*   Spaces and hyphens: `folded_poster_with_tape_01_sign_elis_Roughness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `foog_butter_BaseColor_Utility - sRGB - Texture.1001.png`
*   Spaces and hyphens: `foog_butter_Metalness_Utility - Raw.1001.png`
*   Spaces and hyphens: `foog_butter_Normal_Utility - Raw.1001.png`
*   Spaces and hyphens: `foog_butter_Roughness_Utility - Raw.1001.png`
*   Spaces and hyphens: `globe_globe_BaseColor_ACES - ACEScg.1001.exr`
*   Spaces and hyphens: `globe_globe_Height_Utility - Raw.1001.exr`
*   Spaces and hyphens: `globe_globe_Metalness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `globe_globe_Normal_Utility - Raw.1001.exr`
*   Spaces and hyphens: `globe_globe_Roughness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `house_a_house_default_BaseColor_Utility - sRGB - Texture.1001.png`
*   Spaces and hyphens: `house_a_house_default_BaseColor_Utility - sRGB - Texture.1002.png`
*   Spaces and hyphens: `house_a_house_default_BaseColor_Utility - sRGB - Texture.1003.png`
*   Spaces and hyphens: `house_a_house_default_BaseColor_Utility - sRGB - Texture.1004.png`
*   Spaces and hyphens: `house_a_house_default_BaseColor_Utility - sRGB - Texture.1005.png`
*   Spaces and hyphens: `house_a_house_default_BaseColor_Utility - sRGB - Texture.1006.png`
*   Spaces and hyphens: `house_a_house_default_BaseColor_Utility - sRGB - Texture.1007.png`
*   Spaces and hyphens: `house_a_house_default_BaseColor_Utility - sRGB - Texture.1009.png`
*   Spaces and hyphens: `house_a_house_default_BaseColor_Utility - sRGB - Texture.1010.png`
*   Spaces and hyphens: `house_a_house_default_Height_Utility - Raw.1001.png`
*   Spaces and hyphens: `house_a_house_default_Height_Utility - Raw.1002.png`
*   Spaces and hyphens: `house_a_house_default_Height_Utility - Raw.1003.png`
*   Spaces and hyphens: `house_a_house_default_Height_Utility - Raw.1004.png`
*   Spaces and hyphens: `house_a_house_default_Height_Utility - Raw.1005.png`
*   Spaces and hyphens: `house_a_house_default_Height_Utility - Raw.1006.png`
*   Spaces and hyphens: `house_a_house_default_Height_Utility - Raw.1007.png`
*   Spaces and hyphens: `house_a_house_default_Height_Utility - Raw.1009.png`
*   Spaces and hyphens: `house_a_house_default_Height_Utility - Raw.1010.png`
*   Spaces and hyphens: `house_a_house_default_Metalness_Utility - Raw.1001.png`
*   Spaces and hyphens: `house_a_house_default_Metalness_Utility - Raw.1002.png`
*   Spaces and hyphens: `house_a_house_default_Metalness_Utility - Raw.1003.png`
*   Spaces and hyphens: `house_a_house_default_Metalness_Utility - Raw.1004.png`
*   Spaces and hyphens: `house_a_house_default_Metalness_Utility - Raw.1005.png`
*   Spaces and hyphens: `house_a_house_default_Metalness_Utility - Raw.1006.png`
*   Spaces and hyphens: `house_a_house_default_Metalness_Utility - Raw.1007.png`
*   Spaces and hyphens: `house_a_house_default_Metalness_Utility - Raw.1009.png`
*   Spaces and hyphens: `house_a_house_default_Metalness_Utility - Raw.1010.png`
*   Spaces and hyphens: `house_a_house_default_Normal_Utility - Raw.1001.png`
*   Spaces and hyphens: `house_a_house_default_Normal_Utility - Raw.1002.png`
*   Spaces and hyphens: `house_a_house_default_Normal_Utility - Raw.1003.png`
*   Spaces and hyphens: `house_a_house_default_Normal_Utility - Raw.1004.png`
*   Spaces and hyphens: `house_a_house_default_Normal_Utility - Raw.1005.png`
*   Spaces and hyphens: `house_a_house_default_Normal_Utility - Raw.1006.png`
*   Spaces and hyphens: `house_a_house_default_Normal_Utility - Raw.1007.png`
*   Spaces and hyphens: `house_a_house_default_Normal_Utility - Raw.1009.png`
*   Spaces and hyphens: `house_a_house_default_Normal_Utility - Raw.1010.png`
*   Spaces and hyphens: `house_a_house_default_Roughness_Utility - Raw.1001.png`
*   Spaces and hyphens: `house_a_house_default_Roughness_Utility - Raw.1002.png`
*   Spaces and hyphens: `house_a_house_default_Roughness_Utility - Raw.1003.png`
*   Spaces and hyphens: `house_a_house_default_Roughness_Utility - Raw.1004.png`
*   Spaces and hyphens: `house_a_house_default_Roughness_Utility - Raw.1005.png`
*   Spaces and hyphens: `house_a_house_default_Roughness_Utility - Raw.1006.png`
*   Spaces and hyphens: `house_a_house_default_Roughness_Utility - Raw.1007.png`
*   Spaces and hyphens: `house_a_house_default_Roughness_Utility - Raw.1009.png`
*   Spaces and hyphens: `house_a_house_default_Roughness_Utility - Raw.1010.png`
*   Spaces and hyphens: `houses_house_a_mltSG_BaseColor_Utility - sRGB - Texture.1001.png`
*   Spaces and hyphens: `houses_house_a_mltSG_Height_Utility - Raw.1001.png`
*   Spaces and hyphens: `houses_house_a_mltSG_Metalness_Utility - Raw.1001.png`
*   Spaces and hyphens: `houses_house_a_mltSG_Normal_Utility - Raw.1001.png`
*   Spaces and hyphens: `houses_house_a_mltSG_Roughness_Utility - Raw.1001.png`
*   Spaces and hyphens: `ioio_ioio_BaseColor_ACES - ACEScg.1001.exr_hcm.swatch`
*   Spaces and hyphens: `ioio_ioio_BaseColor_ACES - ACEScg.1001.exr`
*   Spaces and hyphens: `ioio_ioio_Height_Utility - Raw.1001.exr_hcm.swatch`
*   Spaces and hyphens: `ioio_ioio_Height_Utility - Raw.1001.exr`
*   Spaces and hyphens: `ioio_ioio_Metalness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `ioio_ioio_Normal_Utility - Raw.1001.exr_hcm.swatch`
*   Spaces and hyphens: `ioio_ioio_Normal_Utility - Raw.1001.exr`
*   Spaces and hyphens: `ioio_ioio_Roughness_Utility - Raw.1001.exr_hcm.swatch`
*   Spaces and hyphens: `ioio_ioio_Roughness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `ioio_rope_BaseColor_ACES - ACEScg.1001.exr`
*   Spaces and hyphens: `ioio_rope_Height_Utility - Raw.1001.exr`
*   Spaces and hyphens: `ioio_rope_Metalness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `ioio_rope_Normal_Utility - Raw.1001.exr`
*   Spaces and hyphens: `ioio_rope_Roughness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `ioio_transparent_BaseColor_ACES - ACEScg.1001.exr`
*   Spaces and hyphens: `ioio_transparent_Height_Utility - Raw.1001.exr`
*   Spaces and hyphens: `ioio_transparent_Metalness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `ioio_transparent_Normal_Utility - Raw.1001.exr`
*   Spaces and hyphens: `ioio_transparent_Roughness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `iris_eyes_BaseColor_ACES - ACEScg.1001.exr.rat`
*   Spaces and hyphens: `iris_eyes_BaseColor_ACES - ACEScg.1001.exr`
*   Spaces and hyphens: `iris_eyes_BaseColor_ACES - ACEScg.1002.exr`
*   Spaces and hyphens: `iris_eyes_Height_Utility - Raw.1001.exr`
*   Spaces and hyphens: `iris_eyes_Height_Utility - Raw.1002.exr`
*   Spaces and hyphens: `iris_eyes_Metalness_Utility - Raw.1001.exr.rat`
*   Spaces and hyphens: `iris_eyes_Metalness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `iris_eyes_Metalness_Utility - Raw.1002.exr.rat`
*   Spaces and hyphens: `iris_eyes_Metalness_Utility - Raw.1002.exr`
*   Spaces and hyphens: `iris_eyes_Normal_Utility - Raw.1001.exr`
*   Spaces and hyphens: `iris_eyes_Normal_Utility - Raw.1002.exr`
*   Spaces and hyphens: `iris_eyes_Roughness_Utility - Raw.1001.exr.rat`
*   Spaces and hyphens: `iris_eyes_Roughness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `iris_eyes_Roughness_Utility - Raw.1002.exr.rat`
*   Spaces and hyphens: `iris_eyes_Roughness_Utility - Raw.1002.exr`
*   Spaces and hyphens: `istockphoto-1446668869-612x612.jpg`
*   Spaces and hyphens: `istockphoto-167222757-612x612.jpg`
*   Spaces and hyphens: `magazine stack.spp`
*   Spaces and hyphens: `magazine_stack_06_magazine_BaseColor_Utility - sRGB - Texture.1001.png`
*   Spaces and hyphens: `magazine_stack_06_magazine_Roughness_Utility - Raw.1001.png`
*   Spaces and hyphens: `matress_matress_BaseColor_ACES - ACEScg.1001.exr.rat`
*   Spaces and hyphens: `matress_matress_BaseColor_ACES - ACEScg.1001.exr`
*   Spaces and hyphens: `matress_matress_Height_Utility - Raw.1001.exr`
*   Spaces and hyphens: `matress_matress_Metalness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `matress_matress_Normal_Utility - Raw.1001.exr.rat`
*   Spaces and hyphens: `matress_matress_Normal_Utility - Raw.1001.exr`
*   Spaces and hyphens: `matress_matress_Roughness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `menino_body_BaseColor_ACES - ACEScg.1001.exr`
*   Spaces and hyphens: `menino_body_Height_Utility - Raw.1001.exr`
*   Spaces and hyphens: `menino_body_Metalness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `menino_body_Normal_Utility - Raw.1001.exr`
*   Spaces and hyphens: `menino_body_Roughness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `menino_body_mtlSG_BaseColor_Utility - sRGB - Texture.1001.png.rat`
*   Spaces and hyphens: `menino_body_mtlSG_BaseColor_Utility - sRGB - Texture.1001.png`
*   Spaces and hyphens: `menino_body_mtlSG_BaseColor_Utility - sRGB - Texture.1001_Utility - sRGB - Texture_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `menino_body_mtlSG_BaseColor_Utility - sRGB - Texture.1001_sRGB - Texture_ACEScg.png.tx`
*   Spaces and hyphens: `menino_body_mtlSG_Height_Utility - Raw.1001.png.rat`
*   Spaces and hyphens: `menino_body_mtlSG_Height_Utility - Raw.1001.png`
*   Spaces and hyphens: `menino_body_mtlSG_Metalness_Utility - Raw.1001.png`
*   Spaces and hyphens: `menino_body_mtlSG_Normal_Utility - Raw.1001.png.rat`
*   Spaces and hyphens: `menino_body_mtlSG_Normal_Utility - Raw.1001.png`
*   Spaces and hyphens: `menino_body_mtlSG_Normal_Utility - Raw.1001_Raw_ACEScg.png.tx`
*   Spaces and hyphens: `menino_body_mtlSG_Normal_Utility - Raw.1001_Utility - Raw_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `menino_body_mtlSG_Roughness_Utility - Raw.1001.png.rat`
*   Spaces and hyphens: `menino_body_mtlSG_Roughness_Utility - Raw.1001.png`
*   Spaces and hyphens: `menino_body_mtlSG_Roughness_Utility - Raw.1001_Utility - Raw_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `menino_body_mtlSG_sss_Utility - Raw.1001.png.rat`
*   Spaces and hyphens: `menino_body_mtlSG_sss_Utility - Raw.1001.png`
*   Spaces and hyphens: `menino_body_mtlSG_sss_Utility - Raw.1001_Raw_ACEScg.png.tx`
*   Spaces and hyphens: `menino_body_mtlSG_sss_Utility - Raw.1001_Utility - Raw_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `menino_shirt_BaseColor_Utility - sRGB - Texture.1001.png_hcm.swatch`
*   Spaces and hyphens: `menino_shirt_BaseColor_Utility - sRGB - Texture.1001.png`
*   Spaces and hyphens: `menino_shirt_BaseColor_Utility - sRGB - Texture.1001_ACES - ACES2065-1_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `menino_shirt_BaseColor_Utility - sRGB - Texture.1001_Utility - sRGB - Texture_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `menino_shirt_BaseColor_Utility - sRGB - Texture.1001_sRGB - Texture_ACEScg.png.tx`
*   Spaces and hyphens: `menino_shirt_Height_Utility - Raw.1001.png`
*   Spaces and hyphens: `menino_shirt_Height_Utility - Raw.1001_Utility - Raw_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `menino_shirt_Metalness_Utility - Raw.1001.png`
*   Spaces and hyphens: `menino_shirt_Normal_Utility - Raw.1001.png_hcm.swatch`
*   Spaces and hyphens: `menino_shirt_Normal_Utility - Raw.1001.png`
*   Spaces and hyphens: `menino_shirt_Normal_Utility - Raw.1001_Raw_ACEScg.png.tx`
*   Spaces and hyphens: `menino_shirt_Normal_Utility - Raw.1001_Utility - Raw_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `menino_shirt_Roughness_Utility - Raw.1001.png`
*   Spaces and hyphens: `menino_skin_BaseColor_Utility - sRGB - Texture.1001.png`
*   Spaces and hyphens: `menino_skin_BaseColor_Utility - sRGB - Texture.1001_Utility - sRGB - Texture_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `menino_skin_BaseColor_Utility - sRGB - Texture.1002.png`
*   Spaces and hyphens: `menino_skin_BaseColor_Utility - sRGB - Texture.1002_Utility - sRGB - Texture_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `menino_skin_BaseColor_Utility - sRGB - Texture.1003.png`
*   Spaces and hyphens: `menino_skin_BaseColor_Utility - sRGB - Texture.1003_Utility - sRGB - Texture_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `menino_skin_BaseColor_Utility - sRGB - Texture.1004.png`
*   Spaces and hyphens: `menino_skin_BaseColor_Utility - sRGB - Texture.1004_Utility - sRGB - Texture_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `menino_skin_Height_Utility - Raw.1001.png`
*   Spaces and hyphens: `menino_skin_Height_Utility - Raw.1001_Utility - Raw_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `menino_skin_Height_Utility - Raw.1002.png`
*   Spaces and hyphens: `menino_skin_Height_Utility - Raw.1003.png`
*   Spaces and hyphens: `menino_skin_Height_Utility - Raw.1004.png`
*   Spaces and hyphens: `menino_skin_Metalness_Utility - Raw.1001.png`
*   Spaces and hyphens: `menino_skin_Metalness_Utility - Raw.1002.png`
*   Spaces and hyphens: `menino_skin_Metalness_Utility - Raw.1003.png`
*   Spaces and hyphens: `menino_skin_Metalness_Utility - Raw.1004.png`
*   Spaces and hyphens: `menino_skin_Normal_Utility - Raw.1001.png`
*   Spaces and hyphens: `menino_skin_Normal_Utility - Raw.1001_Utility - Raw_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `menino_skin_Normal_Utility - Raw.1002.png`
*   Spaces and hyphens: `menino_skin_Normal_Utility - Raw.1002_Utility - Raw_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `menino_skin_Normal_Utility - Raw.1003.png`
*   Spaces and hyphens: `menino_skin_Normal_Utility - Raw.1003_Utility - Raw_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `menino_skin_Normal_Utility - Raw.1004.png`
*   Spaces and hyphens: `menino_skin_Normal_Utility - Raw.1004_Utility - Raw_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `menino_skin_Roughness_Utility - Raw.1001.png`
*   Spaces and hyphens: `menino_skin_Roughness_Utility - Raw.1001_Utility - Raw_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `menino_skin_Roughness_Utility - Raw.1002.png`
*   Spaces and hyphens: `menino_skin_Roughness_Utility - Raw.1002_Utility - Raw_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `menino_skin_Roughness_Utility - Raw.1003.png`
*   Spaces and hyphens: `menino_skin_Roughness_Utility - Raw.1003_Utility - Raw_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `menino_skin_Roughness_Utility - Raw.1004.png`
*   Spaces and hyphens: `menino_skin_Roughness_Utility - Raw.1004_Utility - Raw_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `mountain base_mountain_BaseColor_ACES - ACEScg.1001.exr`
*   Spaces and hyphens: `mountain base_mountain_Height_Utility - Raw.1001.exr`
*   Spaces and hyphens: `mountain base_mountain_Metalness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `mountain base_mountain_Normal_Utility - Raw.1001.exr`
*   Spaces and hyphens: `mountain base_mountain_Roughness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `notebook_02_notebook_BaseColor_ACES - ACEScg.1001.exr`
*   Spaces and hyphens: `notebook_02_notebook_Normal_Utility - Raw.1001.exr`
*   Spaces and hyphens: `notebook_02_notebook_Roughness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `notebook_04_notebook_b_BaseColor_ACES - ACEScg.1001.exr`
*   Spaces and hyphens: `notebook_04_notebook_b_Height_Utility - Raw.1001.exr`
*   Spaces and hyphens: `notebook_04_notebook_b_Metalness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `notebook_04_notebook_b_Normal_Utility - Raw.1001.exr`
*   Spaces and hyphens: `notebook_04_notebook_b_Roughness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `pillow_pillow_BaseColor_ACES - ACEScg.1001.exr`
*   Spaces and hyphens: `pillow_pillow_Height_Utility - Raw.1001.exr`
*   Spaces and hyphens: `pillow_pillow_Metalness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `pillow_pillow_Normal_Utility - Raw.1001.exr`
*   Spaces and hyphens: `pillow_pillow_Roughness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `posters_posters_BaseColor_Utility - sRGB - Texture.1001.png`
*   Spaces and hyphens: `posters_posters_Height_Utility - Raw.1001.png`
*   Spaces and hyphens: `posters_posters_Metalness_Utility - Raw.1001.png`
*   Spaces and hyphens: `posters_posters_Normal_Utility - Raw.1001.png`
*   Spaces and hyphens: `posters_posters_Roughness_Utility - Raw.1001.png`
*   Spaces and hyphens: `pote_pote_BaseColor_ACES - ACEScg.1001.exr`
*   Spaces and hyphens: `pote_pote_Height_Utility - Raw.1001.exr`
*   Spaces and hyphens: `pote_pote_Metalness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `pote_pote_Normal_Utility - Raw.1001.exr`
*   Spaces and hyphens: `pote_pote_Roughness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `recreio magazine_A.jpg`
*   Spaces and hyphens: `recreio magazine_b.jpg`
*   Spaces and hyphens: `recreio magazine_c.jpg`
*   Spaces and hyphens: `recreio revista aberta.jpg`
*   Spaces and hyphens: `sam_eye_basecolor_ACES - ACES2065-1_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `sam_eye_basecolor_Utility - sRGB - Texture_ACES - ACEScg.png.tx`
*   Spaces and hyphens: `sanduiche_bread_BaseColor_Utility - sRGB - Texture.1001.png.rat`
*   Spaces and hyphens: `sanduiche_bread_BaseColor_Utility - sRGB - Texture.1001.png`
*   Spaces and hyphens: `sanduiche_bread_Height_Utility - Raw.1001.png`
*   Spaces and hyphens: `sanduiche_bread_Metalness_Utility - Raw.1001.png`
*   Spaces and hyphens: `sanduiche_bread_Normal_Utility - Raw.1001.png.rat`
*   Spaces and hyphens: `sanduiche_bread_Normal_Utility - Raw.1001.png`
*   Spaces and hyphens: `sanduiche_bread_Roughness_Utility - Raw.1001.png`
*   Spaces and hyphens: `sanduiche_letuce_BaseColor_Utility - sRGB - Texture.1001.png`
*   Spaces and hyphens: `sanduiche_letuce_Height_Utility - Raw.1001.png`
*   Spaces and hyphens: `sanduiche_letuce_Metalness_Utility - Raw.1001.png`
*   Spaces and hyphens: `sanduiche_letuce_Normal_Utility - Raw.1001.png`
*   Spaces and hyphens: `sanduiche_letuce_Roughness_Utility - Raw.1001.png`
*   Spaces and hyphens: `sanduiche_molho_BaseColor_Utility - sRGB - Texture.1001.png`
*   Spaces and hyphens: `sanduiche_molho_Height_Utility - Raw.1001.png`
*   Spaces and hyphens: `sanduiche_molho_Metalness_Utility - Raw.1001.png`
*   Spaces and hyphens: `sanduiche_molho_Normal_Utility - Raw.1001.png`
*   Spaces and hyphens: `sanduiche_molho_Roughness_Utility - Raw.1001.png`
*   Spaces and hyphens: `sanduiche_presunto_BaseColor_Utility - sRGB - Texture.1001.png`
*   Spaces and hyphens: `sanduiche_presunto_Height_Utility - Raw.1001.png`
*   Spaces and hyphens: `sanduiche_presunto_Metalness_Utility - Raw.1001.png`
*   Spaces and hyphens: `sanduiche_presunto_Normal_Utility - Raw.1001.png`
*   Spaces and hyphens: `sanduiche_presunto_Roughness_Utility - Raw.1001.png`
*   Spaces and hyphens: `sink_esponge_BaseColor_Utility - sRGB - Texture.1001.png`
*   Spaces and hyphens: `sink_esponge_Metalness_Utility - Raw.1001.png`
*   Spaces and hyphens: `sink_esponge_Normal_Utility - Raw.1001.png`
*   Spaces and hyphens: `sink_esponge_Roughness_Utility - Raw.1001.png`
*   Spaces and hyphens: `sink_fabric_BaseColor_Utility - sRGB - Texture.1001.png`
*   Spaces and hyphens: `sink_fabric_Metalness_Utility - Raw.1001.png`
*   Spaces and hyphens: `sink_fabric_Normal_Utility - Raw.1001.png`
*   Spaces and hyphens: `sink_fabric_Roughness_Utility - Raw.1001.png`
*   Spaces and hyphens: `sink_plastic_BaseColor_Utility - sRGB - Texture.1001.png.rat`
*   Spaces and hyphens: `sink_plastic_BaseColor_Utility - sRGB - Texture.1001.png`
*   Spaces and hyphens: `sink_plastic_BaseColor_Utility - sRGB - Texture.1002.png.rat`
*   Spaces and hyphens: `sink_plastic_BaseColor_Utility - sRGB - Texture.1002.png`
*   Spaces and hyphens: `sink_plastic_Metalness_Utility - Raw.1001.png.rat`
*   Spaces and hyphens: `sink_plastic_Metalness_Utility - Raw.1001.png`
*   Spaces and hyphens: `sink_plastic_Metalness_Utility - Raw.1002.png.rat`
*   Spaces and hyphens: `sink_plastic_Metalness_Utility - Raw.1002.png`
*   Spaces and hyphens: `sink_plastic_Normal_Utility - Raw.1001.png.rat`
*   Spaces and hyphens: `sink_plastic_Normal_Utility - Raw.1001.png`
*   Spaces and hyphens: `sink_plastic_Normal_Utility - Raw.1002.png.rat`
*   Spaces and hyphens: `sink_plastic_Normal_Utility - Raw.1002.png`
*   Spaces and hyphens: `sink_plastic_Roughness_Utility - Raw.1001.png`
*   Spaces and hyphens: `sink_plastic_Roughness_Utility - Raw.1002.png`
*   Spaces and hyphens: `sink_plastic_sss_Color_Utility - Raw.1001.png`
*   Spaces and hyphens: `sink_plastic_sss_Color_Utility - Raw.1002.png`
*   Spaces and hyphens: `sink_plastic_transmission_Utility - Raw.1001.png.rat`
*   Spaces and hyphens: `sink_plastic_transmission_Utility - Raw.1001.png`
*   Spaces and hyphens: `sink_plastic_transmission_Utility - Raw.1002.png.rat`
*   Spaces and hyphens: `sink_plastic_transmission_Utility - Raw.1002.png`
*   Spaces and hyphens: `sink_porrcelain_BaseColor_Utility - sRGB - Texture.1001.png`
*   Spaces and hyphens: `sink_porrcelain_BaseColor_Utility - sRGB - Texture.1002.png`
*   Spaces and hyphens: `sink_porrcelain_Metalness_Utility - Raw.1001.png`
*   Spaces and hyphens: `sink_porrcelain_Metalness_Utility - Raw.1002.png`
*   Spaces and hyphens: `sink_porrcelain_Normal_Utility - Raw.1001.png`
*   Spaces and hyphens: `sink_porrcelain_Normal_Utility - Raw.1002.png`
*   Spaces and hyphens: `sink_porrcelain_Roughness_Utility - Raw.1001.png`
*   Spaces and hyphens: `sink_porrcelain_Roughness_Utility - Raw.1002.png`
*   Spaces and hyphens: `sink_sink_base_BaseColor_Utility - sRGB - Texture.1001.png.rat`
*   Spaces and hyphens: `sink_sink_base_BaseColor_Utility - sRGB - Texture.1001.png`
*   Spaces and hyphens: `sink_sink_base_Metalness_Utility - Raw.1001.png.rat`
*   Spaces and hyphens: `sink_sink_base_Metalness_Utility - Raw.1001.png`
*   Spaces and hyphens: `sink_sink_base_Normal_Utility - Raw.1001.png.rat`
*   Spaces and hyphens: `sink_sink_base_Normal_Utility - Raw.1001.png`
*   Spaces and hyphens: `sink_sink_base_Roughness_Utility - Raw.1001.png.rat`
*   Spaces and hyphens: `sink_sink_base_Roughness_Utility - Raw.1001.png`
*   Spaces and hyphens: `skinexported0-DM1001.exr.rat`
*   Spaces and hyphens: `skinexported0-DM1001.exr`
*   Spaces and hyphens: `skinexported0-DM1002.exr.rat`
*   Spaces and hyphens: `skinexported0-DM1002.exr`
*   Spaces and hyphens: `skinexported0-DM1003.exr.rat`
*   Spaces and hyphens: `skinexported0-DM1003.exr`
*   Spaces and hyphens: `skinexported0-DM1004.exr.rat`
*   Spaces and hyphens: `skinexported0-DM1004.exr`
*   Spaces and hyphens: `skinexported0-DM1005.exr.rat`
*   Spaces and hyphens: `skinexported0-DM1005.exr`
*   Spaces and hyphens: `skinexported0-DM1006.exr.rat`
*   Spaces and hyphens: `skinexported0-DM1006.exr`
*   Spaces and hyphens: `skinexported0-DM1007.exr.rat`
*   Spaces and hyphens: `skinexported0-DM1007.exr`
*   Spaces and hyphens: `skinexported0-DM1008.exr.rat`
*   Spaces and hyphens: `skinexported0-DM1008.exr`
*   Spaces and hyphens: `skinexported0-DM1009.exr.rat`
*   Spaces and hyphens: `skinexported0-DM1009.exr`
*   Spaces and hyphens: `skinexported0-DM1010.exr.rat`
*   Spaces and hyphens: `skinexported0-DM1010.exr`
*   Spaces and hyphens: `stylized_tree 01.spp`
*   Spaces and hyphens: `stylized_tree_01_stylized_tree_BaseColor_Utility - sRGB - Texture.1001.png`
*   Spaces and hyphens: `stylized_tree_01_stylized_tree_Height_Utility - Raw.1001.png`
*   Spaces and hyphens: `stylized_tree_01_stylized_tree_Metalness_Utility - Raw.1001.png`
*   Spaces and hyphens: `stylized_tree_01_stylized_tree_Normal_Utility - Raw.1001.png`
*   Spaces and hyphens: `stylized_tree_01_stylized_tree_Roughness_Utility - Raw.1001.png`
*   Spaces and hyphens: `stylized_tree_06_stylized_tree_BaseColor_Utility - sRGB - Texture.1001.png`
*   Spaces and hyphens: `stylized_tree_06_stylized_tree_Height_Utility - Raw.1001.png`
*   Spaces and hyphens: `stylized_tree_06_stylized_tree_Metalness_Utility - Raw.1001.png`
*   Spaces and hyphens: `stylized_tree_06_stylized_tree_Normal_Utility - Raw.1001.png`
*   Spaces and hyphens: `stylized_tree_06_stylized_tree_Roughness_Utility - Raw.1001.png`
*   Spaces and hyphens: `subsuface eye.jpg`
*   Spaces and hyphens: `table_wood_BaseColor_Utility - sRGB - Texture.1001.png`
*   Spaces and hyphens: `table_wood_Metalness_Utility - Raw.1001.png`
*   Spaces and hyphens: `table_wood_Normal_Utility - Raw.1001.png`
*   Spaces and hyphens: `table_wood_Roughness_Utility - Raw.1001.png`
*   Spaces and hyphens: `tapeta_a_tapete_BaseColor_Utility - sRGB - Texture.1001.png`
*   Spaces and hyphens: `tapeta_a_tapete_Normal_Utility - Raw.1001.png`
*   Spaces and hyphens: `tied_curtains_01_curtain_BaseColor_ACES - ACEScg.1001.exr`
*   Spaces and hyphens: `tied_curtains_01_curtain_Height_Utility - Raw.1001.exr`
*   Spaces and hyphens: `tied_curtains_01_curtain_Metalness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `tied_curtains_01_curtain_Normal_Utility - Raw.1001.exr`
*   Spaces and hyphens: `tied_curtains_01_curtain_Roughness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `village_ground_BaseColor_Utility - sRGB - Texture.1001.png`
*   Spaces and hyphens: `village_ground_Height_Utility - Raw.1001.png`
*   Spaces and hyphens: `village_ground_Metalness_Utility - Raw.1001.png`
*   Spaces and hyphens: `village_ground_Normal_Utility - Raw.1001.png`
*   Spaces and hyphens: `village_ground_Roughness_Utility - Raw.1001.png`
*   Spaces and hyphens: `wall_wall_BaseColor_ACES - ACEScg.1001.exr`
*   Spaces and hyphens: `wall_wall_Height_Utility - Raw.1001.exr`
*   Spaces and hyphens: `wall_wall_Metalness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `wall_wall_Normal_Utility - Raw.1001.exr`
*   Spaces and hyphens: `wall_wall_Roughness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `walls_BaseColor_ACES - ACEScg.1001.exr.rat`
*   Spaces and hyphens: `walls_BaseColor_ACES - ACEScg.1001.exr`
*   Spaces and hyphens: `walls_BaseColor_ACES - ACEScg.1002.exr.rat`
*   Spaces and hyphens: `walls_BaseColor_ACES - ACEScg.1002.exr`
*   Spaces and hyphens: `walls_Metalness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `walls_Metalness_Utility - Raw.1002.exr`
*   Spaces and hyphens: `walls_Normal_Utility - Raw.1001.exr.rat`
*   Spaces and hyphens: `walls_Normal_Utility - Raw.1001.exr`
*   Spaces and hyphens: `walls_Normal_Utility - Raw.1002.exr.rat`
*   Spaces and hyphens: `walls_Normal_Utility - Raw.1002.exr`
*   Spaces and hyphens: `walls_Roughness_Utility - Raw.1001.exr.rat`
*   Spaces and hyphens: `walls_Roughness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `walls_Roughness_Utility - Raw.1002.exr.rat`
*   Spaces and hyphens: `walls_Roughness_Utility - Raw.1002.exr`
*   Spaces and hyphens: `white mask.png`
*   Spaces and hyphens: `window_glass_mtl_BaseColor_Utility - sRGB - Texture.1001.png`
*   Spaces and hyphens: `window_glass_mtl_Height_Utility - Raw.1001.png`
*   Spaces and hyphens: `window_glass_mtl_Metalness_Utility - Raw.1001.png`
*   Spaces and hyphens: `window_glass_mtl_Normal_Utility - Raw.1001.png`
*   Spaces and hyphens: `window_glass_mtl_Roughness_Utility - Raw.1001.png`
*   Spaces and hyphens: `window_kitchen_window_BaseColor_ACES - ACEScg.1001.exr`
*   Spaces and hyphens: `window_kitchen_window_Height_Utility - Raw.1001.exr`
*   Spaces and hyphens: `window_kitchen_window_Metalness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `window_kitchen_window_Normal_Utility - Raw.1001.exr`
*   Spaces and hyphens: `window_kitchen_window_Roughness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `window_kitchen_window_transmission_Utility - Raw.1001.1001.bmp`
*   Spaces and hyphens: `window_window_BaseColor_ACES - ACEScg.1001.exr`
*   Spaces and hyphens: `window_window_Height_Utility - Raw.1001.exr`
*   Spaces and hyphens: `window_window_Metalness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `window_window_Normal_Utility - Raw.1001.exr`
*   Spaces and hyphens: `window_window_Roughness_Utility - Raw.1001.exr`
*   Spaces and hyphens: `window_wood1_BaseColor_Utility - sRGB - Texture.1001.png`
*   Spaces and hyphens: `window_wood1_BaseColor_Utility - sRGB - Texture.1002.png`
*   Spaces and hyphens: `window_wood1_Height_Utility - Raw.1001.png`
*   Spaces and hyphens: `window_wood1_Height_Utility - Raw.1002.png`
*   Spaces and hyphens: `window_wood1_Metalness_Utility - Raw.1001.png`
*   Spaces and hyphens: `window_wood1_Metalness_Utility - Raw.1002.png`
*   Spaces and hyphens: `window_wood1_Normal_Utility - Raw.1001.png`
*   Spaces and hyphens: `window_wood1_Normal_Utility - Raw.1002.png`
*   Spaces and hyphens: `window_wood1_Roughness_Utility - Raw.1001.png`
*   Spaces and hyphens: `window_wood1_Roughness_Utility - Raw.1002.png`

---

## 3. Moderate — Structure & Consistency

*   **Character textures — no `default/` folders**: `look/texture/character/avo` → `clothes/`, `hair/`, `skin/`.
*   **Character textures — no `default/` folders**: `look/texture/character/menino` → `eyes/`, `shirt/`, `skin/`.
*   **Language mix (PT/EN)**: `grandma` vs `avo.usd`; prop pairs `cadeira`/`chair`, `pia`/`sink`, `plantas`/`plants`, `tapete`/`rug`.
*   **Local `menino/look/texture`** coexists with centralized `look/texture/character/menino`.
*   **`look/texture/prop/`** — 30 subdirs including stray `character/`, `environment/`, `set/`, `sets/`.

---

## 4. Minor — Hygiene

### Spaces in names
*   `138d69ecc6a540e94501dfc3a938d62c_ACES - ACES2065-1_ACES - ACEScg.jpg.tx` in `look/texture/prop/posters/`
*   `1d7512139e7ad15bc73e8bffbf6f13a9_ACES - ACES2065-1_ACES - ACEScg.jpg.tx` in `look/texture/prop/embroidery/`
*   `68e5d632bea510012449359d9b8a8797_ACES - ACES2065-1_ACES - ACEScg.jpg.tx` in `look/texture/prop/posters/`
*   `772ff681e0df3bf9a55934a722f811ff_ACES - ACES2065-1_ACES - ACEScg.jpg.tx` in `look/texture/prop/embroidery/`
*   `772ff681e0df3bf9a55934a722f811ff_ACES - ACES2065-1_ACEScg.jpg.tx` in `look/texture/prop/embroidery/`
*   `8d47806f72a693e3505514aaedc580c4_ACES - ACES2065-1_ACES - ACEScg.jpg.tx` in `look/texture/prop/posters/`
*   `Fiber Cards` under `look/texture/character/avo/hair/`
*   `New folder` under `look/texture/prop/set/`
*   `a nave.png_hcm.swatch` in `look/texture/prop/posters/.mayaSwatches/`
*   `a nave.png` in `look/texture/prop/posters/`

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
