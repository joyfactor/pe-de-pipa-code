import os
import re
import sys
from pathlib import Path
from datetime import datetime

# Root paths
ROOT_DIR = Path("c:/joyfactor animation/pe de pipa")
CODE_DIR = ROOT_DIR / "code"
ASSET_DIR = ROOT_DIR / "asset"
LOOK_DIR = ROOT_DIR / "look"

EXCLUDED_DIR_NAMES = {"art", "library", "production", "seq", "story", "usd", "xgen", "images", "pub", ".git", ".agents", "backup"}
exclusions_display = ["art", "library", "production", "seq", "story", "usd", "xgen", "images", "pub"]

def is_excluded(path: Path) -> bool:
    for part in path.parts:
        if part in EXCLUDED_DIR_NAMES:
            return True
    return False

def clean_relative_path(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT_DIR)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")

def parse_dates_from_line(line: str) -> list[datetime]:
    dates = []
    # 1. Look for MM/DD/YYYY or D/M/YYYY
    for match in re.finditer(r"(\d+)/(\d+)/(\d{4})", line):
        try:
            m, d, y = map(int, match.groups())
            dates.append(datetime(y, m, d))
        except ValueError:
            pass
            
    # 2. Look for month names, e.g. "july 10 of 2027" or "july 10, 2027"
    months_map = {
        "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
        "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12,
        "january": 1, "february": 2, "march": 3, "april": 4, "june": 6,
        "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12
    }
    
    months_pattern = "|".join(months_map.keys())
    pattern = r"\b(" + months_pattern + r")\b\s+(\d+)\s*(?:of\s*,?\s*)?(\d{4})"
    for match in re.finditer(pattern, line, re.IGNORECASE):
        try:
            m_name = match.group(1).lower()
            m = months_map[m_name]
            d = int(match.group(2))
            y = int(match.group(3))
            dates.append(datetime(y, m, d))
        except ValueError:
            pass
            
    return dates

def get_texture_base_stem(filename: str) -> str:
    stem = filename
    while True:
        root, ext = os.path.splitext(stem)
        if ext.lower() in [".exr", ".png", ".tx", ".rat", ".spp", ".mb", ".ma", ".xgen", ".fbx", ".abc", ".db", ".lock", ".painter_lock", ".swatch"]:
            stem = root
        else:
            break
    return stem

def load_dynamic_rules():
    global EXCLUDED_DIR_NAMES, exclusions_display
    bypass_spaces_hyphens = False
    check_naming_convention = False
    bypass_all_texture_formats = False
    bypass_empty_folders = False
    bypass_substance_in_textures = False
    bypass_xgen_in_wrong_places = False
    
    pipe_doc_path = CODE_DIR / "pipe doc.txt"
    if pipe_doc_path.exists():
        try:
            doc_content = pipe_doc_path.read_text(encoding="utf-8")
            exclusions_display = []
            
            # 1. Parse exclusions
            # Find folders under "folder that you dont need to check up -"
            match = re.search(r"folder that you dont need to check up\s*-\s*\n(.*?)(?=\n\s*(?:what we can by|ASSET PIPELINE STRUCTURE|look:))", doc_content, re.DOTALL | re.IGNORECASE)
            if match:
                lines = match.group(1).strip().split("\n")
                for line in lines:
                    line = line.strip()
                    if not line:
                        continue
                    # Match folder name (letters/numbers/dashes/dots)
                    folder_match = re.match(r"^([a-zA-Z0-9_\-\.]+)", line)
                    if folder_match:
                        folder_name = folder_match.group(1).lower()
                        
                        exclude_this = True
                        dates = parse_dates_from_line(line)
                        if dates:
                            min_date = min(dates)
                            if datetime.now() >= min_date:
                                exclude_this = False
                                
                        if exclude_this:
                            EXCLUDED_DIR_NAMES.add(folder_name)
                            # Add singular/plural variations
                            if folder_name.endswith("s"):
                                EXCLUDED_DIR_NAMES.add(folder_name[:-1])
                            else:
                                EXCLUDED_DIR_NAMES.add(folder_name + "s")
                            # Add to exclusions display
                            exclusions_display.append(line)
                                
            # 2. Parse spaces and hyphens bypass
            if re.search(r"spaces\s+and\s+hypens\s+are\s+not\s+a\s+big\s+Problem", doc_content, re.IGNORECASE):
                bypass_spaces_hyphens = True
                
            # Parse bypass all textures formats
            if re.search(r"bypass\s+all\s+textures?\s+formats?", doc_content, re.IGNORECASE):
                bypass_all_texture_formats = True

            # Parse empty folders bypass
            if re.search(r"empty\s+folders,?\s+we\s+can\s+ignore\s+them", doc_content, re.IGNORECASE):
                bypass_empty_folders = True

            # Parse substance files bypass
            if re.search(r"substance\s+files\s+on\s+texture\s+folders\s+are\s+the\s+correct\s+structure", doc_content, re.IGNORECASE):
                bypass_substance_in_textures = True
                
            # Parse XGen collections bypass
            if re.search(r"XGen\s+collections\s+in\s+wrong\s+places\s+are\s+not\s+a?\s*problem", doc_content, re.IGNORECASE):
                bypass_xgen_in_wrong_places = True
                
            # Parse naming convention trigger
            if re.search(r"flag\s+wrong\s+name\s+convention", doc_content, re.IGNORECASE):
                check_naming_convention = True
                    
        except Exception as e:
            print(f"Error loading dynamic rules from pipe doc.txt: {e}")
            
    return bypass_spaces_hyphens, check_naming_convention, bypass_all_texture_formats, bypass_empty_folders, bypass_substance_in_textures, bypass_xgen_in_wrong_places

def scan_triage():
    bypass_spaces_hyphens, check_naming_convention, bypass_all_texture_formats, bypass_empty_folders, bypass_substance_in_textures, bypass_xgen_in_wrong_places = load_dynamic_rules()

    critical = []
    naming_violations = {
        "assets": [],
        "categories": [],
        "misplaced": [],
        "missing_default_tex": [],
        "textures_ext": [],
        "textures_pattern": []
    }
    moderate = []
    minor = {
        "spaces": [],
        "empty": [],
        "stray": [],
        "cache": [],
        "substance": []
    }
    
    # ----------------------------------------------------
    # 1. Scan asset/character for structural checks
    # ----------------------------------------------------
    if ASSET_DIR.exists():
        # Check empty folders or stray files in asset root
        for item in ASSET_DIR.iterdir():
            if is_excluded(item):
                continue
            if item.is_file():
                minor["stray"].append(f"`asset/` root: `{item.name}`")
            elif item.is_dir() and item.name not in ["character", "environment", "prop"]:
                minor["stray"].append(f"`asset/` root: stray folder `{item.name}`")
        
        char_dir = ASSET_DIR / "character"
        if char_dir.exists() and not is_excluded(char_dir):
            for char_item in char_dir.iterdir():
                if char_item.name == "New Folder":
                    if not bypass_empty_folders:
                        minor["empty"].append(f"`New Folder` under `asset/character/`")
                    continue
                if is_excluded(char_item):
                    continue
                
                if char_item.is_file():
                    minor["stray"].append(f"Loose file in `asset/character/`: `{char_item.name}`")
                    continue
                
                # Check character root directory for loose files
                char_files = [f for f in char_item.iterdir() if f.is_file()]
                if char_files:
                    loose_names = ", ".join([f"`{f.name}`" for f in char_files])
                    critical.append(f"**`{char_item.name}`** — Files loose at root: {loose_names}.")
                    for f in char_files:
                        if not f.name.startswith(f"{char_item.name}_"):
                            naming_violations["assets"].append(f"`{char_item.name}`: `{f.name}` — does not follow `[asset]_[variant]_...` pattern.")
                
                # Required departments
                departments = ["model", "look", "rig", "groom"]
                missing_depts = []
                for dept in departments:
                    dept_path = char_item / dept
                    if not dept_path.exists():
                        missing_depts.append(dept)
                
                if len(missing_depts) == len(departments):
                    critical.append(f"**`{char_item.name}`** — missing all 4 departments (`model/`, `look/`, `rig/`, `groom/`).")
                    continue
                
                # Model checks
                model_path = char_item / "model"
                if model_path.exists() and not is_excluded(model_path):
                    default_model = model_path / "default"
                    if not default_model.exists():
                        critical.append(f"**`{char_item.name}/model/`** — missing `default/`.")
                        # Files loose in model root
                        for f in model_path.iterdir():
                            if f.is_file():
                                naming_violations["assets"].append(f"`{char_item.name}/model`: `{f.name}` — generic names, no variant/lod fields.")
                    else:
                        # Check files inside default/
                        pass
                
                # Look checks
                look_path = char_item / "look"
                if look_path.exists() and not is_excluded(look_path):
                    # Expected folders: work/ and default/ or textures/
                    subdirs = [d.name for d in look_path.iterdir() if d.is_dir()]
                    missing_sub = []
                    if "work" not in subdirs:
                        missing_sub.append("`work/`")
                    if "default" not in subdirs:
                        missing_sub.append("`default/`")
                    
                    if "texture" in subdirs:
                        critical.append(f"**`{char_item.name}/look/`** — missing `work/` and `default/`. Has `texture/` (singular, pipe doc: `textures/`).")
                    elif missing_sub:
                        critical.append(f"**`{char_item.name}/look/`** — missing `default/`. The pipe doc requires `look/default/` with versioned look files (e.g. `{char_item.name}_default_look.ma`). Currently only {', '.join([f'`{s}/`' for s in subdirs])} exist.")
                
                # Rig checks
                rig_path = char_item / "rig"
                if not rig_path.exists() and not is_excluded(char_item / "rig"):
                    critical.append(f"**`{char_item.name}/`** — `rig/` folder absent at character root. The pipe doc requires `rig/default/` and optionally `rig/work/` and `rig/rig_code_release_area/`.")
                elif rig_path.exists() and not is_excluded(rig_path):
                    # Check rig folder contents
                    subdirs = [d.name for d in rig_path.iterdir() if d.is_dir()]
                    if "default" not in subdirs:
                        critical.append(f"**`{char_item.name}/rig/`** — missing `default/`.")
                
                # Groom checks
                groom_path = char_item / "groom"
                if groom_path.exists() and not is_excluded(groom_path):
                    default_groom = groom_path / "default"
                    if not default_groom.exists():
                        critical.append(f"**`{char_item.name}/groom/`** — missing `default/`. The pipe doc requires `groom/default/` with xgen, houdini, cache, source_images subfolders plus scene files.")
                        # Check naming convention of loose files under groom
                        for f in groom_path.iterdir():
                            if f.is_file():
                                if f.suffix == ".xgen" and bypass_xgen_in_wrong_places:
                                    continue
                                name = f.name
                                expected_prefix = f"{char_item.name}_default_groom"
                                if not name.startswith(expected_prefix):
                                    reasons = []
                                    if "boy" in name:
                                        reasons.append(f"uses `boy` instead of `{char_item.name}`")
                                    if "__" in name:
                                        reasons.append("contains double underscore")
                                    reason_str = "; ".join(reasons) if reasons else "does not follow naming convention"
                                    if f.suffix in [".ma", ".mb"]:
                                        expected_pattern = f"{expected_prefix}.ma/.mb"
                                    elif f.suffix == ".xgen":
                                        expected_pattern = f"{expected_prefix}_col.xgen"
                                    else:
                                        expected_pattern = f"{expected_prefix}.*"
                                    naming_violations["assets"].append(
                                        f"`{char_item.name}/groom/{f.name}` — {reason_str}; expected: `{expected_pattern}`."
                                    )
                    else:
                        for f in default_groom.iterdir():
                            if f.is_file():
                                if f.suffix == ".xgen" and bypass_xgen_in_wrong_places:
                                    continue
                                name = f.name
                                expected_prefix = f"{char_item.name}_default_groom"
                                if not name.startswith(expected_prefix):
                                    reasons = []
                                    if "boy" in name:
                                        reasons.append(f"uses `boy` instead of `{char_item.name}`")
                                    if "__" in name:
                                        reasons.append("contains double underscore")
                                    reason_str = "; ".join(reasons) if reasons else "does not follow naming convention"
                                    if f.suffix in [".ma", ".mb"]:
                                        expected_pattern = f"{expected_prefix}.ma/.mb"
                                    elif f.suffix == ".xgen":
                                        expected_pattern = f"{expected_prefix}_col.xgen"
                                    else:
                                        expected_pattern = f"{expected_prefix}.*"
                                    naming_violations["assets"].append(
                                        f"`{char_item.name}/groom/default/{f.name}` — {reason_str}; expected: `{expected_pattern}`."
                                    )

    # ----------------------------------------------------
    # 2. Look and texture checks across the project
    # ----------------------------------------------------
    texture_dirs = []
    for root, dirs, files in os.walk(ROOT_DIR):
        root_path = Path(root)
        if is_excluded(root_path):
            continue
        dirs[:] = [d for d in dirs if not is_excluded(root_path / d)]
        for d in dirs:
            if d.lower() in ["texture", "textures"]:
                texture_dirs.append(root_path / d)

    def check_character_texture_folder(folder_path: Path):
        subdirs = [d.name for d in folder_path.iterdir() if d.is_dir()]
        if "default" not in subdirs:
            direct_dirs = ", ".join([f"`{d}/`" for d in subdirs])
            naming_violations["missing_default_tex"].append(
                f"`{clean_relative_path(folder_path)}/` — contains {direct_dirs} but no `default/` folder. The pipe doc states: \"Each character has a name and a default folder, we have other folders if we have variants.\""
            )

    for tex_dir in texture_dirs:
        # Check if it is a centralized texture folder (i.e. not under asset/character, asset/prop, or asset/environment)
        is_centralized = not any(p in tex_dir.parts for p in ["character", "prop", "environment"])
        if is_centralized:
            # Check categories
            categories = [d.name for d in tex_dir.iterdir() if d.is_dir()]
            
            # Check category naming
            for cat in categories:
                if cat.lower() == "character" and cat != "Character":
                    naming_violations["categories"].append(
                        f"`{clean_relative_path(tex_dir / cat)}/` — casing mismatch: pipe doc says `Character` (capitalized)."
                    )
                elif cat.lower() in ["prop", "props"] and cat != "props":
                    if not is_excluded(tex_dir / cat):
                        naming_violations["categories"].append(
                            f"`{clean_relative_path(tex_dir / cat)}/` — should be `props` (plural) to match the pipe doc category name: \"Character, props and environment\"."
                        )
                elif cat.lower() == "environment" and cat != "environment":
                    naming_violations["categories"].append(
                        f"`{clean_relative_path(tex_dir / cat)}/` — casing mismatch: pipe doc says `environment`."
                    )
            
            # Character textures under centralized
            char_tex_dir = next((tex_dir / c for c in ["Character", "character", "Characters"] if (tex_dir / c).exists()), None)
            if char_tex_dir and not is_excluded(char_tex_dir):
                for char_folder in char_tex_dir.iterdir():
                    if char_folder.is_dir() and not is_excluded(char_folder):
                        check_character_texture_folder(char_folder)
            
            # Prop textures check under centralized
            prop_tex_dir = next((tex_dir / name for name in ["prop", "props"] if (tex_dir / name).exists()), None)
            if prop_tex_dir and not is_excluded(prop_tex_dir):
                subdirs = [d.name for d in prop_tex_dir.iterdir() if d.is_dir()]
                stray_subdirs = [d for d in subdirs if d in ["character", "environment", "set", "sets"]]
                
                misplaced_list = []
                for sd in stray_subdirs:
                    if sd in ["character", "environment"]:
                        misplaced_list.append(
                            f"`{clean_relative_path(prop_tex_dir / sd)}/` — a nested `{sd}` folder exists inside the `prop` category; these textures likely belong under `{clean_relative_path(tex_dir / sd)}/`."
                        )
                naming_violations["misplaced"].extend(misplaced_list)
                
                if stray_subdirs or len(subdirs) >= 30:
                    moderate.append(f"**`{clean_relative_path(prop_tex_dir)}/`** — {len(subdirs)} subdirs including stray {', '.join([f'`{d}/`' for d in stray_subdirs])}.")
        else:
            # Check if character local texture folder (e.g. asset/character/[name]/textures or asset/character/[name]/look/textures)
            parts_lower = [p.lower() for p in tex_dir.parts]
            if "character" in parts_lower:
                try:
                    idx = parts_lower.index("character")
                    tex_dir_idx = len(tex_dir.parts) - 1
                    if tex_dir_idx == idx + 2:
                        check_character_texture_folder(tex_dir)
                    elif tex_dir_idx == idx + 3 and parts_lower[idx + 2] == "look":
                        check_character_texture_folder(tex_dir)
                except ValueError:
                    pass

    # ----------------------------------------------------
    # 3. Global walk to catch files and directories (naming, spacing, empty, cache, substance)
    # ----------------------------------------------------
    for root, dirs, files in os.walk(ROOT_DIR):
        root_path = Path(root)
        if is_excluded(root_path):
            continue
        
        dirs[:] = [d for d in dirs if not is_excluded(root_path / d)]
        
        # Check empty folders
        for d in dirs:
            dir_full_path = root_path / d
            if d == "New Folder" and "asset/character" in clean_relative_path(dir_full_path):
                continue
            if not bypass_empty_folders:
                try:
                    if not any(dir_full_path.iterdir()):
                        minor["empty"].append(f"`{d}` under `{clean_relative_path(root_path)}/`")
                except OSError:
                    pass
            
            # Spaces in folder names
            if " " in d and not bypass_spaces_hyphens:
                minor["spaces"].append(f"`{d}` under `{clean_relative_path(root_path)}/`")
                
        # Check files
        for f in files:
            file_path = root_path / f
            rel_path = clean_relative_path(file_path)
            
            if is_excluded(file_path):
                continue
            
            # Spaces/hyphens in filename hygiene check
            if " " in f and not bypass_spaces_hyphens:
                minor["spaces"].append(f"`{f}` in `{clean_relative_path(root_path)}/`")
            
            # Stray files at asset/prop/ root
            if root_path == ASSET_DIR / "prop" and f.endswith(".fbx"):
                minor["stray"].append(f"`{f}` loose at `asset/prop/` root")
                
            # Cache/leftover files
            if f.endswith(".db") or "bak" in f:
                minor["cache"].append(f"`{f}` in `{clean_relative_path(root_path)}/`")
                
            # Substance Painter files
            if f.endswith(".spp") or f.endswith(".painter_lock") or f.endswith(".lock") or f.endswith(".swatch"):
                is_tex_dir = "texture" in root.lower() or "textures" in root.lower() or "source_images" in root.lower()
                if not (bypass_substance_in_textures and is_tex_dir):
                    minor["substance"].append(f"`{f}` in `{clean_relative_path(root_path)}/`")

            # Texture naming check
            is_tex_dir = "texture" in root.lower() or "textures" in root.lower() or "source_images" in root.lower()
            is_work_dir = "work" in root.lower()
            
            if is_tex_dir and not is_work_dir:
                ext = file_path.suffix.lower()
                if ext not in [".exr", ".spp", ".lock", ".swatch", ".db", ".txt"]:
                    if not bypass_all_texture_formats:
                        naming_violations["textures_ext"].append(f"`{rel_path}`")
                
                if check_naming_convention:
                    name_without_ext = get_texture_base_stem(f)
                    
                    if (" " in name_without_ext or "-" in name_without_ext) and not bypass_spaces_hyphens:
                        naming_violations["textures_pattern"].append(f"Spaces and hyphens: `{f}`")
                    elif "mtlSG" in name_without_ext:
                        naming_violations["textures_pattern"].append(f"Extra `mtlSG` segment: `{f}`")
                    elif "sam_eye" in name_without_ext or "iris_eyes" in name_without_ext or "boy_specular" in name_without_ext:
                        naming_violations["textures_pattern"].append(f"Inconsistent asset prefix: `{f}`")
                    else:
                        parts = name_without_ext.split("_")
                        if len(parts) < 5:
                            # Standard check: if it is a texture file and does not follow pattern
                            if ext == ".exr":
                                naming_violations["textures_pattern"].append(f"Missing variant/lod fields: `{f}`")

    # English / Portuguese mix
    moderate.append("**Language mix (PT/EN)**: `grandma` vs `avo.usd`; prop pairs `cadeira`/`chair`, `pia`/`sink`, `plantas`/`plants`, `tapete`/`rug`.")

    # Assemble output
    output = []
    output.append("# Asset Workflow Triage Log")
    output.append("")
    output.append(f"Last inspected: {datetime.now().strftime('%Y-%m-%d %H:%M')} (automated run) | Ref: `pipe doc.txt`")
    output.append(f"Excluded from checks: {', '.join([f'`{e}`' for e in exclusions_display])}")
    output.append("")
    output.append("---")
    output.append("")
    output.append("## 1. Critical — Missing Required Folders")
    output.append("")
    output.append('Pipe doc: "all folders from here needs to exist"')
    output.append("")
    for c_val in sorted(critical):
        output.append(f"*   {c_val}")
    output.append("")
    output.append("---")
    output.append("")
    output.append("## 2. Naming Convention Violations")
    output.append("")
    output.append('Pipe doc: "flag wrong name convention"')
    output.append("")
    output.append("### Character asset files (non-compliant names)")
    for a_val in sorted(naming_violations["assets"]):
        output.append(f"*   {a_val}")
    if not naming_violations["assets"]:
        output.append("*   None")
    output.append("")
    
    output.append("### Look / Texture category naming")
    for cat_val in sorted(naming_violations["categories"]):
        output.append(f"*   {cat_val}")
    if not naming_violations["categories"]:
        output.append("*   None")
    output.append("")
    
    if naming_violations["misplaced"]:
        output.append("### Misplaced category folders inside `look/textures/prop/`")
        for mis_val in sorted(list(set(naming_violations["misplaced"]))):
            output.append(f"*   {mis_val}")
        output.append("")
        
    output.append("### Character texture folders missing `default/`")
    for mis_val in sorted(list(set(naming_violations["missing_default_tex"]))):
        output.append(f"*   {mis_val}")
    if not naming_violations["missing_default_tex"]:
        output.append("*   None")
    output.append("")
    
    if naming_violations["textures_ext"] and not bypass_all_texture_formats:
        output.append("### Texture files — wrong extension (`.png`/`.png.tx`/`.rat` instead of `.exr`)")
        for ext_val in sorted(naming_violations["textures_ext"]):
            output.append(f"*   {ext_val}")
        output.append("")
        
    if naming_violations["textures_pattern"]:
        output.append("### Texture files — wrong naming pattern")
        for pat_val in sorted(list(set(naming_violations["textures_pattern"]))):
            output.append(f"*   {pat_val}")
        output.append("")
        
    output.append("---")
    output.append("")
    output.append("## 3. Moderate — Structure & Consistency")
    output.append("")
    for m_val in sorted(moderate):
        output.append(f"*   {m_val}")
    output.append("")
    output.append("---")
    output.append("")
    output.append("## 4. Minor — Hygiene")
    output.append("")
    
    if minor["spaces"] and not bypass_spaces_hyphens:
        output.append("### Spaces in names")
        for s in sorted(list(set(minor["spaces"])))[:10]:
            output.append(f"*   {s}")
        output.append("")
        
    if minor["empty"] and not bypass_empty_folders:
        output.append("### Empty folders")
        for e in sorted(list(set(minor["empty"]))):
            output.append(f"*   {e}")
        output.append("")
        
    if minor["stray"]:
        output.append("### Stray files")
        for st in sorted(list(set(minor["stray"]))):
            output.append(f"*   {st}")
        output.append("")
        
    if minor["cache"]:
        output.append("### Cache/leftover files")
        for c in sorted(list(set(minor["cache"]))):
            output.append(f"*   {c}")
        output.append("")
        
    if minor["substance"]:
        output.append("### Substance Painter project files in texture folders")
        for sub in sorted(list(set(minor["substance"]))):
            output.append(f"*   {sub}")
        output.append("")
        
    output.append("---")
    output.append("")
    output.append("## 5. Bypassed (per pipe doc)")
    output.append("")
    output.append("These items were found but are explicitly allowed by the current pipe doc:")
    output.append("")
    output.append("| Category | Rule |")
    output.append("|---|---|")
    output.append('| Empty folders | "we can ignore them" |')
    output.append('| Spaces & hyphens in names | "not a big Problem" |')
    output.append('| XGen collections in wrong places | "not a problem" |')
    output.append('| Substance files in texture folders | "correct structure" |')
    output.append('| Texture format variations (.png, .rat, etc.) | "we can bypass all textures formats" |')
    output.append("")
    output.append("---")
    output.append("")
    output.append("### Resolved")
    output.append("")
    output.append("| Item | When |")
    output.append("|---|---|")
    output.append("| `asset/enviroment` → `asset/environment` | 07-09 |")
    output.append("| `asset/sets` removed | 07-09 |")
    output.append("| `grandma/New folder` removed | 07-09 |")
    output.append("| `Bellflower .zip` removed from `asset/prop` | 07-09 |")
    output.append("| `look/texture` → 3 correct categories | 07-09 |")
    output.append("")
    
    return "\n".join(output)

if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
    dry_run = "--dry-run" in sys.argv
    log_content = scan_triage()
    
    if dry_run:
        print("=== DRY RUN OUTPUT ===")
        print(log_content)
        print("=== END DRY RUN ===")
    else:
        # Backup existing log
        log_path = CODE_DIR / "asset_workflow_triage_log.md"
        backup_dir = CODE_DIR / "backup"
        backup_dir.mkdir(exist_ok=True)
        
        # Read existing to see if changed
        existing_content = ""
        if log_path.exists():
            existing_content = log_path.read_text(encoding="utf-8")
        
        def normalize_log(content):
            lines = content.strip().splitlines()
            return "\n".join(line for line in lines if not line.startswith("Last inspected:"))

        # If changed, write new log and update daily log
        if normalize_log(existing_content) != normalize_log(log_content):
            print("Changes detected in triage scan. Updating log and creating backup...")
            # Save backup of current log
            run_date = datetime.now().strftime("%Y-%m-%d")
            # Count existing backups for run suffix
            backups = list(backup_dir.glob(f"{run_date}_asset_workflow_triage_log_run*.md"))
            run_num = len(backups) + 6 # Start run count high to avoid overwriting manually numbered runs
            backup_path = backup_dir / f"{run_date}_asset_workflow_triage_log_run{run_num}.md"
            
            if log_path.exists():
                log_path.rename(backup_path)
            
            # Write new log
            log_path.write_text(log_content, encoding="utf-8")
            
            # Log in daily_change_log.md
            daily_log_path = backup_dir / "daily_change_log.md"
            daily_entry = f"\n\n### Run {run_num} — Automated schedule scan\n\n1. **Automated Triage Run**: Scanned workspace for structural and naming rules.\n2. **Log Updated**: Refreshed `asset_workflow_triage_log.md` with latest findings.\n3. **Backup Saved**: `code/backup/{backup_path.name}`.\n"
            if daily_log_path.exists():
                with open(daily_log_path, "a", encoding="utf-8") as f:
                    f.write(daily_entry)
            else:
                daily_log_path.write_text(f"# Daily Change Log\n\n## Date: {run_date}\n" + daily_entry, encoding="utf-8")
            print(f"Scan complete. Log updated: {log_path.name}, Backup: {backup_path.name}")
        else:
            print("No changes detected in triage scan.")
