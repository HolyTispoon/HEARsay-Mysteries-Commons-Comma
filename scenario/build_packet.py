"""Generate the Commons' Comma scenario packet (Markdown -> docx) and response-matrix workbook from commons_comma_data.py."""
import sys, subprocess, os
sys.path.insert(0, os.path.dirname(__file__))
import commons_comma_data as d
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

OUT = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT, exist_ok=True)
W = {w["id"]: w for w in d.WITNESSES}
Q = {q["id"]: q for q in d.QUESTIONS}
name = lambda wid: W[wid]["name"]
rank_order = sorted(d.WITNESSES, key=lambda w: w["receptiveness_rank"])

# ------------------------------------------------------------------ Markdown
md = []
P = md.append
P("---\ntitle: \"The Commons' Comma\"\nsubtitle: \"Hearsay Mystery Game — Scenario Packet 1\"\ndate: \"September 2026\"\n---\n")
P("*This packet follows the structure defined in* Hearsay Mystery Game *(the framework document). The companion workbook, "
  "The Commons' Comma – Response Matrix.xlsx, holds the same 64 interview cells in spreadsheet form. Both files are generated "
  "from a single data file (commons_comma_data.py), so edit the data file and regenerate rather than editing either output by hand.*\n")

P("# 1. Identity\n")
P(f"**Title:** {d.TITLE}  \n**Scenario ID:** `{d.SCENARIO_ID}`  \n**Mystery-giver:** the university president  \n**Deadline:** 5:00 p.m. (the public examination is at 6:00 p.m.); in play, a budget of 40 questions.\n")
P("**Pitch:** The night before the university publicly examines its founding Charter to settle whether a disputed ink mark is a comma, the Charter vanishes from the archive. A first-day work-study assistant in the president's office has until five o'clock and forty questions to find out who took it, why, and where it is, by interviewing eight students who each know something and each have an opinion about the renovation the comma would decide.\n")

P("# 2. The puzzle\n")
P(f"**The mystery.** {d.PUZZLE['mystery']}\n")
P("> **Answer key: spoilers from here to the end of the packet.** Keep sections 2.2 onward out of player-facing materials.\n")
P(f"**The solution.** {d.PUZZLE['solution']}\n")
P(f"**Final-answer form.** The player selects one person and one location. Correct: **{d.PUZZLE['final_answer']['who']}** and **{d.PUZZLE['final_answer']['where']}**. Offered alternatives: persons — Mira Shah, Jonah Reed, Priya Nwosu, Leo Martinez, Sofia Alvarez, the administrative steering group; locations — the theatre scenery loft, the archive cabinet, the café locker, the newsroom, the business incubator.\n")
P(f"**The hidden payoff.** {d.PUZZLE['hidden_payoff']}\n")

P("# 3. The controversy\n")
P(f"**{d.CONTROVERSY['name']}.** {d.CONTROVERSY['summary']}\n")
P(f"**The clause.** {d.CONTROVERSY['clause']}\n")
P(d.CONTROVERSY["clause_explainer"] + "\n")
P("**The eight positions.**\n")
for p in d.CONTROVERSY["positions"]:
    P(f"- {p}")
P("")

P("# 4. Setting and briefing\n")
P(f"**Player role.** {d.SETTING['player_role']}\n")
P(f"**Briefing (the president speaks).** {d.SETTING['briefing']}\n")
P(f"**Budget rule.** {d.SETTING['deadline_rule']}\n")
P("**True timeline.** Every clue and red herring is consistent with this timeline.\n")
for t in d.SETTING["timeline"]:
    P(f"- {t}")
P("\n**Locations (campus map).**\n")
P("| Witness | Location |\n|------|----------|")
for w in d.WITNESSES:
    P(f"| {w['name']} | {w['location']} |")
P("")

P("# 5. The eight questions\n")
P("Each question is the tripwire for exactly one witness.\n")
P("| ID | Question | Angle | Tripwire for | Why it lands |\n|----|------------|--------|------|--------------|")
for q in d.QUESTIONS:
    P(f"| {q['id']} | {q['text']} | {q['angle']} | {name(q['tripwire_for'])} | {q['tripwire_logic']} |")
P("")

P("# 6. The eight witnesses\n")
for w in d.WITNESSES:
    P(f"## {w['id']} — {w['name']}\n")
    P(f"**Role.** {w['role']}  \n**Portrait.** `Assets/Witness portraits/{w['portrait']}`  \n**Location.** {w['location']}\n")
    P(f"**Public background card (player-facing).** {w['public_card']}\n")
    P(f"**Stance.** {w['stance']}\n")
    P(f"**Withheld secret.** {w['secret']}\n")
    P(f"**Tripwire.** {w['tripwire']} — “{Q[w['tripwire']]['text']}” ({Q[w['tripwire']]['tripwire_logic']})  \n**Walk-away text.** {d.TRIPWIRE_RESPONSES[w['id']]}\n")
    rq = ", ".join(w["receptive_questions"]) or "none"
    P(f"**Receptiveness rank.** {w['receptiveness_rank']} of 8 — receptive on {len(w['receptive_questions'])} of 7 answers ({rq}).\n")

P("# 7. The 20 clues\n")
P("Each clue is delivered by exactly two witnesses (the matrix in section 11 shows where).\n")
P("| ID | Group | Clue | Given by |\n|----|-----|------------------|--------|")
givers = {}
for wid, answers in d.RESPONSES.items():
    for qid, a in answers.items():
        givers.setdefault(a["item"], []).append(f"{name(wid)} ({qid})")
for cid, c in d.CLUES.items():
    P(f"| {cid} | {c['group']} | {c['text']} | {'; '.join(givers[cid])} |")
P("")

P("# 8. The four Major Clues\n")
P("Revealed in this order regardless of which witness earned them. Each earns the next letter of H-E-A-R.\n")
for m in d.MAJOR_CLUES:
    P(f"**{m['id']} ({m['letter']}) — {m['title']}.** Synthesises {', '.join(m['clues'])}.\n")
    P(f"> {m['text']}\n")

P("# 9. The 16 red herrings and their sets\n")
P("Each red herring is delivered by exactly one witness. A player holding a whole set can discount all of it.\n")
for sid, s in d.RED_HERRING_SETS.items():
    P(f"**Set {sid} — {s['title']}.** *Resolution:* {s['resolution']}\n")
    for rid, r in d.RED_HERRINGS.items():
        if r["set"] == sid:
            P(f"- {rid}: {r['text']} *(given by {givers[rid][0]})*")
    P("")

P("# 10. Follow-up pairs\n")
P("Once per witness. The receptive option earns the next Major Clue and shows the explanation; the unreceptive option ends the interview.\n")
for w in d.WITNESSES:
    f = d.FOLLOW_UPS[w["id"]]
    P(f"## {w['name']}\n")
    P(f"**Receptive option.** “{f['good']}”\n")
    P(f"**Unreceptive option.** “{f['bad']}”\n")
    P(f"**Explanation shown on success.** {f['why']}\n")
    P(f"**Walk-away on failure.** {f['walkout']}\n")

P("# 11. The response matrix\n")
P("Each cell: information item in brackets, receptiveness flag, then the full answer text. **TW** marks the tripwire.\n")
P("Overview grid (item IDs; R = receptive opinion, U = unreceptive):\n")
header = "| Question | " + " | ".join(w["name"].split()[0] for w in d.WITNESSES) + " |"
P(header); P("|----|" + "----|" * len(d.WITNESSES))
for q in d.QUESTIONS:
    cells = []
    for w in d.WITNESSES:
        if w["tripwire"] == q["id"]:
            cells.append("**TW**")
        else:
            a = d.RESPONSES[w["id"]][q["id"]]
            cells.append(f"{a['item']} {'R' if q['id'] in w['receptive_questions'] else 'U'}")
    P(f"| {q['id']} | " + " | ".join(cells) + " |")
P("\nFull text, by witness:\n")
for w in d.WITNESSES:
    P(f"## {w['name']}\n")
    for q in d.QUESTIONS:
        if w["tripwire"] == q["id"]:
            P(f"**{q['id']} — TRIPWIRE.** {d.TRIPWIRE_RESPONSES[w['id']]}\n")
        else:
            a = d.RESPONSES[w["id"]][q["id"]]
            flag = "receptive" if q["id"] in w["receptive_questions"] else "unreceptive"
            kind = "clue" if a["item"].startswith("C") else "red herring"
            P(f"**{q['id']} [{a['item']}, {kind}; opinion {flag}].** {a['text']}\n")

P("# 12. Endings, bonus and assets\n")
P(f"**Correct.** {d.ENDINGS['correct']}\n")
P(f"**Right person, wrong place.** {d.ENDINGS['right_person_wrong_place']}\n")
P(f"**Wrong.** {d.ENDINGS['wrong']}\n")
P(f"**Out of questions.** {d.ENDINGS['out_of_questions']}\n")
P(f"**Bonus ranking.** {d.BONUS_RANKING['rule']} Correct order, most to least receptive: " + ", ".join(f"{i+1}. {name(x)}" for i, x in enumerate(d.BONUS_RANKING['answer'])) + ".\n")
P("**Assets.** `Assets/campus-map.png` and `Assets/Witness portraits/<name>.png` for each of the eight witnesses (390×390 PNG, no embedded text). The contact sheet in that folder shows all ten original portraits; Caleb Brooks and Thomas Okafor are not used in this scenario.\n")

md_path = f"{OUT}/The Commons' Comma – Scenario Packet.md"
open(md_path, "w", encoding="utf-8").write("\n".join(md))

# ------------------------------------------------------------------ Workbook
wb = Workbook()
navy, blue, gold, gray, green, red = "1F3A5F", "D9EAF7", "F7E6A3", "F1F3F5", "DDEFE0", "F6D6D6"
hdr_font = Font(bold=True, color="FFFFFF"); hdr_fill = PatternFill("solid", fgColor=navy)
wrap = Alignment(wrap_text=True, vertical="top")
thin = Border(bottom=Side(style="thin", color="D0D7DE"))

def sheet(title, headers, rows, widths):
    ws = wb.create_sheet(title)
    ws.append(headers)
    for c in ws[1]:
        c.font = hdr_font; c.fill = hdr_fill; c.alignment = wrap
    for r in rows:
        ws.append(r)
    for i, wd in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = wd
    for row in ws.iter_rows(min_row=2):
        for c in row:
            c.alignment = wrap; c.border = thin
    ws.freeze_panes = "B2"
    return ws

wb.remove(wb.active)
ws = sheet("Read me", ["Sheet", "What it holds"], [
    ["Grid", "8 questions × 8 witnesses. Each cell shows the information item, the receptiveness flag and the full answer text. TW = tripwire."],
    ["Long table", "One row per cell (64 rows). This is the form the Twine builder reads."],
    ["Witnesses", "Profiles, tripwires, receptiveness ranks."],
    ["Questions", "The eight shared questions and their tripwire owners."],
    ["Clues", "The 20 clues, their Major Clue group and which two witnesses give them."],
    ["Major clues", "The four Major Clues in reveal order."],
    ["Red herrings", "The 16 red herrings, their sets and who gives them."],
    ["Follow-ups", "Per-witness follow-up pairs, explanations and walk-away text."],
    ["Constraints", "Counts that must hold; regenerate from commons_comma_data.py after any edit, and run validate.py."],
], [18, 110])

# Grid
ws = wb.create_sheet("Grid")
ws.append(["Question"] + [w["name"] for w in d.WITNESSES])
for c in ws[1]:
    c.font = hdr_font; c.fill = hdr_fill; c.alignment = wrap
for q in d.QUESTIONS:
    row = [f"{q['id']}. {q['text']}"]
    for w in d.WITNESSES:
        if w["tripwire"] == q["id"]:
            row.append("TW — " + d.TRIPWIRE_RESPONSES[w["id"]])
        else:
            a = d.RESPONSES[w["id"]][q["id"]]
            flag = "receptive" if q["id"] in w["receptive_questions"] else "unreceptive"
            row.append(f"[{a['item']} | {flag}] {a['text']}")
    ws.append(row)
ws.column_dimensions["A"].width = 30
for i in range(2, 10):
    ws.column_dimensions[get_column_letter(i)].width = 48
for row in ws.iter_rows(min_row=2):
    row[0].font = Font(bold=True); row[0].fill = PatternFill("solid", fgColor=blue)
    for c in row:
        c.alignment = wrap; c.border = thin
        v = str(c.value)
        if v.startswith("TW"): c.fill = PatternFill("solid", fgColor=red)
        elif v.startswith("[R"): c.fill = PatternFill("solid", fgColor=gold)
        elif v.startswith("[C"): c.fill = PatternFill("solid", fgColor=green)
    ws.row_dimensions[row[0].row].height = 210
ws.freeze_panes = "B2"

# Long table
rows = []
for w in d.WITNESSES:
    for q in d.QUESTIONS:
        if w["tripwire"] == q["id"]:
            rows.append([w["id"], w["name"], q["id"], q["text"], "TRIPWIRE", "tripwire", "", "", d.TRIPWIRE_RESPONSES[w["id"]]])
        else:
            a = d.RESPONSES[w["id"]][q["id"]]
            kind = "clue" if a["item"].startswith("C") else "red herring"
            group = d.CLUES[a["item"]]["group"] if kind == "clue" else d.RED_HERRINGS[a["item"]]["set"]
            rows.append([w["id"], w["name"], q["id"], q["text"], a["item"], kind, group,
                         "yes" if q["id"] in w["receptive_questions"] else "no", a["text"]])
sheet("Long table", ["Witness ID", "Witness", "Question ID", "Question", "Item", "Item type", "Group / set", "Opinion receptive", "Answer text"],
      rows, [10, 16, 10, 40, 9, 12, 11, 10, 100])

sheet("Witnesses", ["ID", "Name", "Role", "Public background card", "Stance", "Withheld secret", "Tripwire", "Tripwire question", "Walk-away text", "Receptiveness rank", "Receptive on", "Location", "Portrait"],
      [[w["id"], w["name"], w["role"], w["public_card"], w["stance"], w["secret"], w["tripwire"], Q[w["tripwire"]]["text"],
        d.TRIPWIRE_RESPONSES[w["id"]], w["receptiveness_rank"], ", ".join(w["receptive_questions"]) or "none", w["location"], w["portrait"]] for w in d.WITNESSES],
      [7, 16, 30, 50, 40, 40, 8, 40, 45, 10, 22, 22, 18])

sheet("Questions", ["ID", "Question", "Angle", "Tripwire for", "Why it lands"],
      [[q["id"], q["text"], q["angle"], name(q["tripwire_for"]), q["tripwire_logic"]] for q in d.QUESTIONS], [6, 55, 35, 16, 60])

sheet("Clues", ["ID", "Major clue group", "Clue", "Given by"],
      [[cid, c["group"], c["text"], "; ".join(givers[cid])] for cid, c in d.CLUES.items()], [7, 12, 90, 40])

sheet("Major clues", ["ID", "Letter", "Title", "Clues", "Text shown to player"],
      [[m["id"], m["letter"], m["title"], ", ".join(m["clues"]), m["text"]] for m in d.MAJOR_CLUES], [6, 7, 22, 28, 100])

sheet("Red herrings", ["ID", "Set", "Set title", "Red herring", "Given by", "How the set is discounted"],
      [[rid, r["set"], d.RED_HERRING_SETS[r["set"]]["title"], r["text"], givers[rid][0], d.RED_HERRING_SETS[r["set"]]["resolution"]] for rid, r in d.RED_HERRINGS.items()],
      [6, 6, 26, 80, 22, 60])

sheet("Follow-ups", ["Witness", "Receptive option", "Unreceptive option", "Explanation on success", "Walk-away on failure"],
      [[w["name"], d.FOLLOW_UPS[w["id"]]["good"], d.FOLLOW_UPS[w["id"]]["bad"], d.FOLLOW_UPS[w["id"]]["why"], d.FOLLOW_UPS[w["id"]]["walkout"]] for w in d.WITNESSES],
      [16, 60, 60, 70, 50])

sheet("Constraints", ["Constraint", "Value"], [
    ["Witnesses", 8], ["Questions", 8], ["Tripwires", "one per witness, one per question (a permutation)"],
    ["Per witness", "1 tripwire, 5 clues, 2 red herrings"], ["Clues", "20, each given by exactly two witnesses"],
    ["Red herrings", "16, each given once, in cancelling sets"], ["Major clues", "4, five clues each, no overlap"],
    ["Receptive answers", "7,6,5,4,3,2,1,0 by rank = 28 of 56"], ["Question budget", 40], ["Follow-ups", "one per witness; do not count toward the 40"],
], [22, 60])

xlsx_path = f"{OUT}/The Commons' Comma – Response Matrix.xlsx"
wb.save(xlsx_path)
print("wrote", md_path, xlsx_path)
