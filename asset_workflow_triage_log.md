# Asset Workflow Triage Log

This log lists structural issues, bugs, and mismatches identified in the repository based on the Asset Workflow Guideline.

---

## 1. Major / Critical Structure & Workflow Violations

*   **Misspelled / Incorrect Asset Roots**:
    *   The environment root directory is misspelled as `asset/enviroment` (should be `asset/environment`).
    *   The props root directory is singular and misspelled as `asset/prop` (should be `asset/props`).
*   **Separated / Centralized Textures Folder**:
    *   A root-level `texture/` folder exists with 32 subdirectories. According to the workflow guideline, textures should be local to each asset:
        *   Characters: `asset/character/[character_name]/look/textures`
        *   Environment: `asset/environment/look/textures`
*   **Missing Standard Asset Structure**:
    *   **Characters**:
        *   `asset/character/grandma` contains raw geometry files (e.g., `grandma.mb`, `avo.usd`, `robes.obj`) scattered directly in its root. It completely lacks the expected `look/textures` structure.
        *   `asset/character/menino` has a `texture` subdirectory instead of the plural `textures` under `look`.
    *   **Environment**:
        *   `asset/enviroment` contains subfolders `house`, `kitchen`, and `sets` instead of the expected `look/textures` and `materials` directories.
    *   **Props**:
        *   None of the 47 prop directories under `asset/prop` contain the required `models` subdirectory. Model files (e.g., `armario.fbx` under `asset/prop/armario`, `bag_backpack.fbx` under `asset/prop/bag`) are placed directly in the asset root folder.
*   **Unsanctioned `asset/sets` Root**:
    *   An undocumented `asset/sets` folder exists under `asset`, containing scene layouts and scattered assets (e.g., `houses`, `kitchen`, `props`, `room`). This duplicates and bypasses the structure defined for `environment` and `props`.

---

## 2. Moderate / Consistency & Duplication Issues

*   **Duplicate / Conflicting Files**:
    *   `house clean.ma` exists in two separate locations with slightly different file sizes:
        *   `asset/enviroment/house/default/house clean.ma` (~82.7 MB)
        *   `asset/sets/environment/house/default/house clean.ma` (~83.4 MB)
    *   Duplicate/similar rig files exist in `asset/character/menino/pub/rig`:
        *   `menino_default_rig.ma`
        *   `menino_rig_default.ma`
    *   Splits/duplicates exist between the root `texture` folder and local asset folders (e.g., `texture/character/menino` vs. `asset/character/menino/look/texture`).
*   **Language and Naming Inconsistencies**:
    *   **Portuguese / English Mix**:
        *   Character folder is named `grandma` but its primary USD file is named `avo.usd`.
        *   Props directories are named using a mix of Portuguese and English terms (e.g., `armario` vs. `closet`/`shelf`, `cama` vs. `bed frame`, `fogao` vs. `cooker`/`oven`, `talheres`, `tapete` vs. `rug`).
        *   Sequence chapters under `seq` are named `capitulo 1`, `capitulo 2`, etc.
    *   **Duplicate categories**:
        *   `cadeira` & `chair`
        *   `pia` & `sink`
        *   `plantas` & `plants`
        *   `tapete` & `rug`
*   **Lack of Structured Versioning**:
    *   Layout files in `asset/sets/room` (e.g., `room_layout_v001.mb`, `room_layout_v002.mb`, `room_layout_v003.mb`) are placed directly in the asset folder without a dedicated publish/work hierarchy.

---

## 3. Minor / Hygiene & Cleanup Issues

*   **Spaces and Special Characters in Folder/File Names**:
    *   Spaces in folder names: `New Folder`, `pose library`, `books shelf`, `magazine pack`, `tundra grass`, `bed frame`, `capitulo 1`.
    *   Spaces in file names: `house clean.ma`, `kitchen layout.mb`, `books tool.hip`, `pe de pipa assets.hip`.
    *   Complex paint/texture filenames with spaces and hyphens (e.g., `eye_D_Utility - sRGB - Texture_ACES - ACEScg.png.tx`).
*   **Empty & Junk Folders**:
    *   Empty placeholder/junk folders: `New Folder` under `asset/character/` and `New folder` under `asset/character/grandma/`.
    *   Empty directories: `asset/enviroment/kitchen` and `asset/enviroment/sets`.
*   **Leftover / Cache Files in Production Areas**:
    *   SQLite database files (`seq_020.db`, `seq_020.db-shm`, `seq_020.db-wal`) are left in `usd/assets/`.
    *   SQLite database files (`pe de pipa_assets_room.db`, `pe de pipa_enviroment.db`) and journal files are scattered in `houdini/`.
    *   An archive file `TCom_3dplant_Bellflower_001.zip` is sitting in the root of `asset/prop`.
    *   Asset backup files (e.g., `weave_dress_bak1.hip`) are stored in `asset/character/grandma/backup` instead of the global backup folder or being git-ignored.
    *   Inconsistent XGen collections casing/naming (`Pooh_Col` vs. `Pooh_Coll`, `Centurion_Coll`, `vitinho_coll`).
