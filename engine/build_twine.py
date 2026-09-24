#!/usr/bin/env python3
"""
Build a HEARsay scenario into a playable Twine (SugarCube 2) game.

    python3 build_twine.py SCENARIO_DATA.py --assets ASSETS_DIR --out OUT_DIR [--repo]

Steps:
  1. Runs validate.py (next to the scenario data file) and stops if any count is wrong.
  2. Converts the scenario data into JSON and writes it into the engine as `setup.scenario`.
  3. Writes OUT_DIR/source/story.twee (engine + scenario data, Twee 3 format).
  4. Compiles it with Tweego into OUT_DIR/index.html.
  5. Copies the witness portraits and campus map into OUT_DIR/assets/.
  With --repo it also copies the engine, the scenario source and a README into OUT_DIR,
  so OUT_DIR is a complete, self-contained GitHub repository (GitHub Pages serves index.html).

Tweego: https://www.motoslave.net/tweego/ . Put `tweego` on your PATH, or set TWEEGO=/path/to/tweego.
Tweego must have the SugarCube 2 story format installed (it ships with it).
"""
import argparse, importlib.util, json, os, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ENGINE = os.path.join(HERE, "hearsay_engine.twee")
FOLLOWUP_BONUS = 1  # points per successful follow-up after all Major Clues are earned


def load(path):
    spec = importlib.util.spec_from_file_location("scenario_data", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def validate(data_path):
    v = os.path.join(os.path.dirname(os.path.abspath(data_path)), "validate.py")
    if not os.path.exists(v):
        sys.exit(f"validate.py not found next to {data_path}")
    r = subprocess.run([sys.executable, v], capture_output=True, text=True)
    print(r.stdout.strip())
    if r.returncode != 0:
        sys.exit("Validation failed; fix the scenario data before building.\n" + r.stderr)


def scenario_json(d, asset_dir="assets"):
    p = d.PUZZLE
    for key in ("who", "where"):
        opts = p[f"{key}_options"]
        if p["final_answer"][key] not in opts:
            sys.exit(f"PUZZLE['final_answer']['{key}'] is not one of PUZZLE['{key}_options']")
    # Only what the game needs. Designer-only fields (secrets, receptive flags, tripwire logic) stay out.
    return {
        "id": d.SCENARIO_ID,
        "title": d.TITLE,
        "pitch": getattr(d, "PITCH", "") or p["mystery"],
        "budget": d.QUESTION_BUDGET,
        "followup_bonus": FOLLOWUP_BONUS,
        "asset_dir": asset_dir,
        "map": getattr(d, "MAP", "campus-map.png"),
        "puzzle": {
            "mystery": p["mystery"],
            "solution": p["solution"],
            "final_answer": p["final_answer"],
            "who_options": p["who_options"],
            "where_options": p["where_options"],
        },
        "controversy": {k: d.CONTROVERSY[k] for k in ("name", "summary", "clause", "clause_explainer")},
        "setting": {"player_role": d.SETTING["player_role"], "briefing": d.SETTING["briefing"]},
        "questions": [{"id": q["id"], "text": q["text"]} for q in d.QUESTIONS],
        "witnesses": [{k: w[k] for k in ("id", "name", "portrait", "role", "public_card", "location", "tripwire")}
                      for w in d.WITNESSES],
        "responses": {wid: {qid: {"item": a["item"], "text": a["text"]} for qid, a in qs.items()}
                      for wid, qs in d.RESPONSES.items()},
        "tripwire_responses": d.TRIPWIRE_RESPONSES,
        "follow_ups": d.FOLLOW_UPS,
        "clues": {k: v["text"] for k, v in d.CLUES.items()},
        "red_herrings": {k: v["text"] for k, v in d.RED_HERRINGS.items()},
        "red_herring_sets": d.RED_HERRING_SETS,
        "major_clues": [{k: m[k] for k in ("id", "letter", "title", "text")} for m in d.MAJOR_CLUES],
        "endings": d.ENDINGS,
        "ranking_answer": d.BONUS_RANKING["answer"],
    }


def find_file(root, name):
    for dp, _, files in os.walk(root):
        if name in files:
            return os.path.join(dp, name)
    sys.exit(f"Asset {name} not found under {root}")


def same(a, b):
    return os.path.exists(b) and os.path.samefile(a, b)


def copy(src, dst):
    if same(src, dst):
        return
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copyfile(src, dst)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("scenario", help="path to the scenario data .py file")
    ap.add_argument("--assets", required=True, help="folder holding the campus map and the portrait PNGs (searched recursively)")
    ap.add_argument("--out", required=True, help="output folder")
    ap.add_argument("--repo", action="store_true", help="also copy engine, scenario source and README into --out")
    a = ap.parse_args()

    validate(a.scenario)
    d = load(a.scenario)
    out = os.path.abspath(a.out)
    os.makedirs(out, exist_ok=True)

    # assets
    for w in d.WITNESSES:
        copy(find_file(a.assets, w["portrait"]), os.path.join(out, "assets", "portraits", w["portrait"]))
    map_file = getattr(d, "MAP", "campus-map.png")  # the scenario can name its map, e.g. a compressed .jpg
    copy(find_file(a.assets, map_file), os.path.join(out, "assets", map_file))

    # twee
    data = json.dumps(scenario_json(d), ensure_ascii=False).replace("</", "<\\/")
    header = (
        f":: StoryTitle\n{d.TITLE}\n\n\n"
        ":: StoryData\n" + json.dumps({"ifid": d.IFID, "format": "SugarCube", "format-version": "2.37.3",
                                       "start": "Start"}, indent=2) + "\n\n\n"
    )
    scen = f":: ScenarioData [script]\n/* Generated by build_twine.py from {os.path.basename(a.scenario)}. Do not edit by hand. */\nsetup.scenario = {data};\n"
    with open(ENGINE, encoding="utf-8") as f:
        engine = f.read()
    # scenario data must load before the engine script, so it comes first
    twee = header + scen + "\n\n" + engine
    src_dir = os.path.join(out, "source")
    os.makedirs(src_dir, exist_ok=True)
    twee_path = os.path.join(src_dir, "story.twee")
    with open(twee_path, "w", encoding="utf-8") as f:
        f.write(twee)

    # compile
    tweego = os.environ.get("TWEEGO") or shutil.which("tweego")
    if not tweego:
        sys.exit(f"Wrote {twee_path}, but Tweego was not found. Install it or set TWEEGO=/path/to/tweego, then rerun.")
    r = subprocess.run([tweego, "-f", "sugarcube-2", "-o", os.path.join(out, "index.html"), twee_path],
                       capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit("Tweego failed:\n" + r.stderr)
    if r.stderr.strip():
        print(r.stderr.strip())

    if a.repo:
        for fn in ("hearsay_engine.twee", "build_twine.py"):
            copy(os.path.join(HERE, fn), os.path.join(out, "engine", fn))
        scen_dir = os.path.dirname(os.path.abspath(a.scenario))
        for fn in sorted(os.listdir(scen_dir)):
            if fn.endswith(".py"):
                copy(os.path.join(scen_dir, fn), os.path.join(out, "scenario", fn))
        readme = os.path.join(HERE, "README_template.md")
        if os.path.exists(readme):
            with open(readme, encoding="utf-8") as f:
                txt = f.read().replace("{{TITLE}}", d.TITLE).replace("{{DATA}}", os.path.basename(a.scenario))
            play_url = getattr(d, "PLAY_URL", "")  # the scenario's GitHub Pages URL; the line is omitted if unset
            txt = txt.replace("{{PLAY_LINE}}", f"**Play online: {play_url}**\n\n" if play_url else "")
            with open(os.path.join(out, "README.md"), "w", encoding="utf-8") as f:
                f.write(txt)
        open(os.path.join(out, ".nojekyll"), "w").close()

    print(f"Built {os.path.join(out, 'index.html')}")


if __name__ == "__main__":
    main()
