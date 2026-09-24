#!/usr/bin/env python3
"""
Build a HEARsay scenario into a playable Twine (SugarCube 2) game.

    python3 build_twine.py "SCENARIO – Response Matrix.xlsx" --assets ASSETS_DIR --out OUT_DIR [--repo]
                           [--packet "SCENARIO – Scenario Packet.docx" | --no-packet-check]

The Response Matrix workbook is the scenario's source; the game is built from it.

Steps:
  1. Reads the matrix and stops if it breaks a framework rule or disagrees with itself (scenario_matrix.py).
  2. Checks that the scenario packet says the same things as the matrix, and stops if it does not
     (check_packet.py). The packet is the .docx next to the matrix whose name contains "Packet", or --packet.
  3. Converts the scenario into JSON and writes it into the engine as `setup.scenario`.
  4. Writes OUT_DIR/source/story.twee (engine + scenario data, Twee 3 format).
  5. Compiles it with Tweego into OUT_DIR/index.html.
  6. Copies the witness portraits and campus map into OUT_DIR/assets/.
  With --repo it also copies the engine, the matrix, the packet and a README into OUT_DIR,
  so OUT_DIR is a complete, self-contained GitHub repository (GitHub Pages serves index.html).

Needs openpyxl and python-docx (pip3 install openpyxl python-docx).

Tweego: https://www.motoslave.net/tweego/ . Put `tweego` on your PATH, or set TWEEGO=/path/to/tweego.
Tweego must have the SugarCube 2 story format installed (it ships with it).
"""
import argparse, glob, json, os, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from scenario_matrix import read_matrix
from check_packet import check as check_packet

ENGINE = os.path.join(HERE, "hearsay_engine.twee")


def load(matrix_path):
    d, errors = read_matrix(matrix_path)
    if errors:
        sys.exit("The matrix has problems; fix them before building:\n" + "\n".join(" - " + e for e in errors))
    print(f"Matrix OK: {len(d.WITNESSES)} witnesses, {len(d.CLUES)} clues, {len(d.RED_HERRINGS)} red herrings, budget {d.QUESTION_BUDGET}")
    return d


def find_packet(matrix_path):
    found = [p for p in glob.glob(os.path.join(os.path.dirname(os.path.abspath(matrix_path)), "*.docx"))
             if "packet" in os.path.basename(p).lower() and not os.path.basename(p).startswith("~$")]
    if len(found) != 1:
        sys.exit(f"Expected one packet .docx next to the matrix, found {len(found)}. Name it with --packet, or pass --no-packet-check.")
    return found[0]


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
        "pitch": d.PITCH or p["mystery"],
        "budget": d.QUESTION_BUDGET,
        "followup_bonus": d.FOLLOWUP_BONUS,
        "asset_dir": asset_dir,
        "map": d.MAP,
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
    ap.add_argument("matrix", help="the scenario's Response Matrix .xlsx")
    ap.add_argument("--assets", required=True, help="folder holding the campus map and the portrait PNGs (searched recursively)")
    ap.add_argument("--out", required=True, help="output folder")
    ap.add_argument("--repo", action="store_true", help="also copy engine, matrix, packet and README into --out")
    ap.add_argument("--packet", help="the scenario packet .docx (default: the .docx next to the matrix with 'Packet' in its name)")
    ap.add_argument("--no-packet-check", action="store_true", help="build without checking the packet against the matrix")
    a = ap.parse_args()

    d = load(a.matrix)
    packet = None
    if a.no_packet_check:
        print("Skipping the packet check (--no-packet-check).")
    else:
        packet = a.packet or find_packet(a.matrix)
        problems = check_packet(a.matrix, packet)
        if problems:
            sys.exit(f"The packet ({os.path.basename(packet)}) disagrees with the matrix; make them match before building:\n"
                     + "\n".join(" - " + p for p in problems))
        print(f"Packet OK: {os.path.basename(packet)} matches the matrix")
    out = os.path.abspath(a.out)
    os.makedirs(out, exist_ok=True)

    # assets
    for w in d.WITNESSES:
        copy(find_file(a.assets, w["portrait"]), os.path.join(out, "assets", "portraits", w["portrait"]))
    copy(find_file(a.assets, d.MAP), os.path.join(out, "assets", d.MAP))

    # twee
    data = json.dumps(scenario_json(d), ensure_ascii=False).replace("</", "<\\/")
    header = (
        f":: StoryTitle\n{d.TITLE}\n\n\n"
        ":: StoryData\n" + json.dumps({"ifid": d.IFID, "format": "SugarCube", "format-version": "2.37.3",
                                       "start": "Start"}, indent=2) + "\n\n\n"
    )
    scen = f":: ScenarioData [script]\n/* Generated by build_twine.py from {os.path.basename(a.matrix)}. Do not edit by hand. */\nsetup.scenario = {data};\n"
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
        for fn in ("hearsay_engine.twee", "build_twine.py", "scenario_matrix.py", "check_packet.py"):
            copy(os.path.join(HERE, fn), os.path.join(out, "engine", fn))
        scen_out = os.path.join(out, "scenario")
        keep = {os.path.basename(a.matrix)} | ({os.path.basename(packet)} if packet else set())
        if os.path.isdir(scen_out):  # drop anything left from an older layout (e.g. the retired .py data files)
            for fn in os.listdir(scen_out):
                if fn not in keep and os.path.isfile(os.path.join(scen_out, fn)):
                    os.remove(os.path.join(scen_out, fn))
        copy(os.path.abspath(a.matrix), os.path.join(scen_out, os.path.basename(a.matrix)))
        if packet:
            copy(os.path.abspath(packet), os.path.join(scen_out, os.path.basename(packet)))
        readme = os.path.join(HERE, "README_template.md")
        if os.path.exists(readme):
            with open(readme, encoding="utf-8") as f:
                txt = (f.read().replace("{{TITLE}}", d.TITLE).replace("{{MATRIX}}", os.path.basename(a.matrix))
                       .replace("{{PACKET}}", os.path.basename(packet) if packet else "the scenario packet (.docx)"))
            play_url = d.PLAY_URL  # the scenario's GitHub Pages URL; the line is omitted if unset
            txt = txt.replace("{{PLAY_LINE}}", f"**Play online: {play_url}**\n\n" if play_url else "")
            with open(os.path.join(out, "README.md"), "w", encoding="utf-8") as f:
                f.write(txt)
        open(os.path.join(out, ".nojekyll"), "w").close()

    print(f"Built {os.path.join(out, 'index.html')}")


if __name__ == "__main__":
    main()
