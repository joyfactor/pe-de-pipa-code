# Asset Workflow Triage Log

This log lists structural issues, bugs, and mismatches identified in the repository based on the Asset Workflow Guideline.

---

## 1. Major / Critical Structure & Workflow Violations

*   **Misspelled / Incorrect Asset Roots**:
    *   The environment root directory is misspelled as `asset/enviroment` (should be `asset/environment`).
    *   The props root directory is singular and misspelled as `asset/prop` (should be `asset/props`).
*   **Look & Texture Centralization Violations**:
    *   **Missing Project-Wide Look Folder**: The repository lacks a single `look` folder at the root level of the project directory. The guideline states: "It should exist 1 look folder inside the project directory".
    *   **Incorrect Texture Folder Location**: The main `texture` folder is located at the project root level rather than inside a root-level `look` folder (should be `look/texture`).
    *   **Multiple Look Dev & Textures Folders**: There are multiple local look dev/textures folders scattered inside individual asset folders (e.g., `asset/character/menino/look` and local `textures` folders in `usd/assets/` assets), violating the rule: "We dont have multiple look dev folders, and it should exist only 1 texture folder, under look." (Note: The `library` folder is exempt).
*   **Incorrect Centralized Texture Folder Structure**:
    *   **Root Categories**: The `texture` folder has 32 subdirectories at its root level instead of exactly three category folders: `Character`, `props`, and `environment`.
    *   **Character Texture Folders**: Under character textures (e.g., `texture/character/avo` and `texture/character/menino`), there are no `default` folders. Instead, they are organized directly into subfolders named `clothes`, `hair`, `skin`, `eyes`, `shirt`. The pipeline doc states: "Each character has a name and a default folder, we have other foldesr if we have variants."
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
    *   **Non-Centralized Look/Texture Folders**: Local asset folders (e.g. `asset/character/menino/look/texture` and local folders under `usd/assets/`) duplicate or conflict with the centralized rule.
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
