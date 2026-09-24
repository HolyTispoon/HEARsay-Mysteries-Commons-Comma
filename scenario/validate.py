import sys, os
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import commons_comma_data as d

errors = []
qids = [q["id"] for q in d.QUESTIONS]
wids = [w["id"] for w in d.WITNESSES]

# tripwires: permutation
tw = [w["tripwire"] for w in d.WITNESSES]
if sorted(tw) != sorted(qids):
    errors.append(f"tripwires not a permutation of questions: {tw}")
for q in d.QUESTIONS:
    owner = next(w for w in d.WITNESSES if w["tripwire"] == q["id"])
    if owner["id"] != q["tripwire_for"]:
        errors.append(f"{q['id']} tripwire_for mismatch: {q['tripwire_for']} vs {owner['id']}")

clue_count = Counter()
rh_count = Counter()
for w in d.WITNESSES:
    r = d.RESPONSES[w["id"]]
    expected_qs = [q for q in qids if q != w["tripwire"]]
    if sorted(r.keys()) != sorted(expected_qs):
        errors.append(f"{w['id']} answers {sorted(r.keys())} != expected {expected_qs}")
    items = [a["item"] for a in r.values()]
    clues = [i for i in items if i.startswith("C")]
    rhs = [i for i in items if i.startswith("R")]
    if len(clues) != 5 or len(rhs) != 2:
        errors.append(f"{w['id']}: {len(clues)} clues / {len(rhs)} red herrings")
    if len(set(clues)) != len(clues):
        errors.append(f"{w['id']}: duplicate clue within witness")
    clue_count.update(clues); rh_count.update(rhs)
    expected_receptive = 7 - (w["receptiveness_rank"] - 1)
    if len(w["receptive_questions"]) != expected_receptive:
        errors.append(f"{w['id']}: rank {w['receptiveness_rank']} needs {expected_receptive} receptive, has {len(w['receptive_questions'])}")
    if w["tripwire"] in w["receptive_questions"]:
        errors.append(f"{w['id']}: tripwire listed as receptive")
    for q in w["receptive_questions"]:
        if q not in r: errors.append(f"{w['id']}: receptive {q} has no answer")

for c in d.CLUES:
    if clue_count[c] != 2: errors.append(f"{c} used {clue_count[c]} times")
for r in d.RED_HERRINGS:
    if rh_count[r] != 1: errors.append(f"{r} used {rh_count[r]} times")
if len(d.CLUES) != 20: errors.append("need 20 clues")
if len(d.RED_HERRINGS) != 16: errors.append("need 16 red herrings")
mc_clues = [c for m in d.MAJOR_CLUES for c in m["clues"]]
if sorted(mc_clues) != sorted(d.CLUES): errors.append("major clues do not partition the 20 clues")
for m in d.MAJOR_CLUES:
    for c in m["clues"]:
        if d.CLUES[c]["group"] != m["id"]: errors.append(f"{c} group mismatch")
sets = Counter(r["set"] for r in d.RED_HERRINGS.values())
for s in d.RED_HERRING_SETS:
    if sets[s] < 2: errors.append(f"set {s} too small")
ranking = [w["id"] for w in sorted(d.WITNESSES, key=lambda w: w["receptiveness_rank"])]
if ranking != d.BONUS_RANKING["answer"]:
    errors.append(f"bonus ranking answer {d.BONUS_RANKING['answer']} != {ranking}")
for wid in wids:
    if wid not in d.FOLLOW_UPS: errors.append(f"no follow-up for {wid}")
    if wid not in d.TRIPWIRE_RESPONSES: errors.append(f"no tripwire response for {wid}")
total_receptive = sum(len(w["receptive_questions"]) for w in d.WITNESSES)
print("receptive answers:", total_receptive, "of 56")
print("ERRORS:" if errors else "OK — all counts check out")
for e in errors: print(" -", e)
sys.exit(1 if errors else 0)
