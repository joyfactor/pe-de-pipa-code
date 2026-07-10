# Asset Workflow Triage Log

Last inspected: 2026-07-10 13:21 (automated run) | Ref: `pipe doc.txt`
Excluded from checks: `art`, `library`, `production`, `seq`, `story`, `usd`, `xgen`, `images`, `pub`, `props` (until 7/10/2026)

---

## 1. Critical — Missing Required Folders

Pipe doc: "all folders from here needs to exist"

*   **`avo/groom/`** — missing `default/`. The pipe doc requires `groom/default/` with xgen, houdini, cache, source_images subfolders plus scene files.
*   **`avo/look/`** — missing `default/`. The pipe doc requires `look/default/` with versioned look files (e.g. `avo_default_look.ma`). Currently only `textures/` and `work/` exist.
*   **`menino/`** — `rig/` folder absent at character root. The pipe doc requires `rig/default/` and optionally `rig/work/` and `rig/rig_code_release_area/`.

---

## 2. Naming Convention Violations

Pipe doc: "flag wrong name convention"

### Character asset files (non-compliant names)
*   `menino/groom/default/boy_groom_v001.mb` — uses `boy` instead of `menino`; expected pattern: `menino_default_groom.ma/.mb`.
*   `menino/groom/default/boy_groom_v001__boy_coll.xgen` — uses `boy` instead of `menino`, contains double underscore; expected: `menino_default_groom_col.xgen`.

### Look / Texture category naming
*   `look/textures/prop/` — should be `props` (plural) to match the pipe doc category name: "Character, props and environment".
*   `look/textures/character/` — casing mismatch: pipe doc says `Character` (capitalized).

### Misplaced category folders inside `look/textures/prop/`
*   `look/textures/prop/character/` — a nested `character` folder exists inside the `prop` category; these textures likely belong under `look/textures/character/`.
*   `look/textures/prop/environment/` — a nested `environment` folder exists inside the `prop` category; these textures likely belong under `look/textures/environment/`.

### Character texture folders missing `default/`
*   `look/textures/character/avo/` — contains `clothes/`, `displacement/`, `hair/`, `skin/` but no `default/` folder. The pipe doc states: "Each character has a name and a default folder, we have other folders if we have variants."
*   `look/textures/character/menino/` — contains `eyes/`, `shirt/`, `skin/` but no `default/` folder.

---

## 3. Moderate — Structure & Consistency

*   **Language mix (PT/EN)**: `grandma` vs `avo.usd`; prop pairs `cadeira`/`chair`, `pia`/`sink`, `plantas`/`plants`, `tapete`/`rug`.

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
*   `dress.spp` in `asset/character/avo/look/textures/clothes/`
*   `avo_skin.spp` in `asset/character/avo/look/textures/skin/`

---

### Bypassed (per pipe doc)

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
