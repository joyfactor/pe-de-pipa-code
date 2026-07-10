# Asset Workflow Triage Log

Last inspected: 2026-07-09 (run 2) | Ref: `pipe doc.txt`
Excluded from checks per pipe doc: `art`, `library`, `production`, `seq`, `story`, `usd`, `xgen`, `images`, `pub`

---

## 1. Critical — Missing Required Folders (pipe doc: "all folders from here needs to exist")

*   **`grandma`** — missing all 4 department folders (`model/`, `look/`, `rig/`, `groom/`). Files sit loose at root: `grandma.mb`, `avo.usd`, `robes.obj`, `weave_dress.hip`.
*   **`menino`** — missing `rig/` at character root (exists under `pub/rig/` — excluded from checks per pipe doc).
*   **`menino/model/`** — missing `default/` subfolder. Files sit directly in `model/` (e.g. `menino_model_v001.mb`, `.fbx` files, `zbrush/`).
*   **`menino/look/`** — missing `work/` and `default/` subfolders. Contains `menino.usd` + `texture/` (singular, pipe doc says `textures/`).
*   **`menino/groom/`** — missing `default/` subfolder. Groom files sit directly in `groom/` (`boy_groom_v001.mb`, `.xgen`).

---

## 2. Moderate — Structure & Consistency

*   **`asset/prop` singular naming**: Pipe doc lists `prop` under asset; directory matches. (No action — matches doc.)
*   **Look & Texture Centralization**:
    *   Root `look/texture/` exists with 3 correct category folders (`character`, `environment`, `prop`) ✔.
    *   Local `asset/character/menino/look/texture` still exists alongside centralized folder.
*   **Character Texture Structure — no `default/` folders**:
    *   `look/texture/character/menino` → `eyes/`, `shirt/`, `skin/` (no `default/`).
    *   `look/texture/character/avo` → `clothes/`, `hair/`, `skin/` + loose `.exr`/`.rat` files (no `default/`).
*   **`look/texture/prop/`** — 30 subdirs including stray `character/`, `environment/`, `set/`, `sets/` folders that don't belong here.
*   **Duplicate rig files** in `asset/character/menino/pub/rig/`: `menino_default_rig.ma` and `menino_rig_default.ma` (~64 MB each). (Note: `pub` excluded from checks, logged for awareness only.)
*   **Language mix (PT / EN)**: `grandma` folder vs `avo.usd`; prop duplicates (`cadeira`/`chair`, `pia`/`sink`, `plantas`/`plants`, `tapete`/`rug`); sequences `capitulo 1`, `capitulo 2`.

---

## 3. Minor — Hygiene

*   **Spaces in names**: `pose library`, `books shelf`, `magazine pack`, `tundra grass`, `bed frame`, `house clean.ma`, `kitchen layout.mb`.
*   **Empty folder**: `New Folder` under `asset/character/` (empty).
*   **Stray files at `asset/prop/` root**: `lencol.fbx`, `varal.fbx`.
*   **Cache / leftover files**: SQLite `.db` files in production areas; `weave_dress_bak1.hip` in `asset/character/grandma/backup`.
*   **XGen naming inconsistency**: `Pooh_Col` vs `Pooh_Coll`, `vitinho_coll`.

---

### Resolved (confirmed removed from filesystem)

| Item | When |
|---|---|
| `asset/enviroment` misspelling → `asset/environment` | by 07-09 |
| `asset/sets` undocumented root | by 07-09 |
| `New folder` under `asset/character/grandma/` | by 07-09 |
| `TCom_3dplant_Bellflower_001.zip` in `asset/prop` | by 07-09 |
| `look/texture` root had 32 mixed subdirs → now 3 correct categories | by 07-09 |
