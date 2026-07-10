# Asset Workflow Triage Log

Last inspected: 2026-07-09 | Ref: `pipe doc.txt`

---

## 1. Critical — Structure & Workflow Violations

*   **`asset/prop` still singular**: Pipeline doc implies plural `props`; directory remains `asset/prop`.
*   **Look & Texture Centralization**:
    *   Root `look/texture` exists with correct 3 categories (`character`, `environment`, `prop`) — ✔ fixed since last run.
    *   **Local look/texture folders persist** inside individual assets (e.g. `asset/character/menino/look/texture`, USD asset folders), violating single-centralized-texture rule (library exempt).
*   **Character Texture Structure — no `default` folders**: `look/texture/character/menino` has `eyes`, `shirt`, `skin` directly; `look/texture/character/avo` has `clothes`, `hair`, `skin` directly. Pipeline doc requires a `default` folder under each character name.
*   **Prop Texture Folder — 30 subdirs**: `look/texture/prop` contains 30 mixed subdirectories (including stray `character`, `environment`, `set`, `sets` folders inside it) instead of clean per-prop organisation.

---

## 2. Moderate — Consistency & Duplication

*   **Duplicate files**:
    *   `house clean.ma` in `asset/environment/house/default/` (~82.7 MB) — the old duplicate in `asset/sets` is gone ✔.
    *   `menino_default_rig.ma` and `menino_rig_default.ma` both exist in `asset/character/menino/pub/rig` (~64 MB each).
*   **Language mix (PT / EN)**:
    *   Character: folder `grandma` vs USD file `avo.usd`.
    *   Props duplicates: `cadeira` & `chair`, `pia` & `sink`, `plantas` & `plants`, `tapete` & `rug`.
    *   Sequences: `capitulo 1`, `capitulo 2`, etc.
*   **Versioning**: layout files in `asset/environment/sets/room` lack publish/work hierarchy.

---

## 3. Minor — Hygiene

*   **Spaces in names**: `pose library`, `books shelf`, `magazine pack`, `tundra grass`, `bed frame`, `house clean.ma`, `kitchen layout.mb`.
*   **Empty folder**: `New Folder` under `asset/character/` (empty, still present).
*   **Stray files at asset root**: `lencol.fbx` and `varal.fbx` loose in `asset/prop/`.
*   **Cache / leftover files in production areas**: SQLite `.db` files in `usd/assets/` and `houdini/`; `weave_dress_bak1.hip` in `asset/character/grandma/backup`.
*   **XGen naming inconsistency**: mixed casing (`Pooh_Col` vs `Pooh_Coll`, `vitinho_coll`).

---

### Resolved since previous run

| Item | Status |
|---|---|
| `asset/enviroment` misspelling | ✔ Renamed to `asset/environment` |
| `asset/sets` undocumented root | ✔ Removed |
| `New folder` under `asset/character/grandma/` | ✔ Removed |
| `TCom_3dplant_Bellflower_001.zip` in `asset/prop` | ✔ Removed |
| `look/texture` root categories | ✔ Now 3 correct folders (`character`, `environment`, `prop`) |
