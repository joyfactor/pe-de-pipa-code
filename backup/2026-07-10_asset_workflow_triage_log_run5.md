# Asset Workflow Triage Log

Last inspected: 2026-07-10 13:18:27 (automated run) | Ref: `pipe doc.txt`
Excluded from checks: `art`, `library`, `production`, `seq`, `story`, `usd`, `xgen`, `images`, `pub`

---

## 1. Critical — Missing Required Folders

Pipe doc: "all folders from here needs to exist"

*   **`avo/groom/`** — missing `default/`.
*   **`avo/look/`** — missing `default/`.
*   **`menino`** — `rig/` absent at character root.

---

## 2. Naming Convention Violations

Pipe doc: "flag wrong name convention" — expected: `[asset]_[variant]_[lod]_[channel]_[aov]_[udim].[exr]`

### Character asset files (non-compliant names)
*   `menino/groom`: `boy_groom_v001.mb` — uses `boy` instead of `menino`, double underscore.
*   `menino/groom`: `boy_groom_v001__boy_coll.xgen` — uses `boy` instead of `menino`, double underscore.

### Texture files — wrong extension (`.png`/`.png.tx`/`.rat` instead of `.exr`)

### Texture files — wrong naming pattern

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

### Resolved

| Item | When |
|---|---|
| `asset/enviroment` → `asset/environment` | 07-09 |
| `asset/sets` removed | 07-09 |
| `grandma/New folder` removed | 07-09 |
| `Bellflower .zip` removed from `asset/prop` | 07-09 |
| `look/texture` → 3 correct categories | 07-09 |
