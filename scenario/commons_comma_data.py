# The Commons' Comma — scenario packet data (single source of truth)
# Every part of the packet document and the response-matrix workbook is generated from this file.

TITLE = "The Commons' Comma"
SCENARIO_ID = "commons-comma"
IFID = "61186C66-1FEC-4296-99AD-81162A1EF015"  # Twine story ID; keep fixed so players' saves survive rebuilds
QUESTION_BUDGET = 40
PLAY_URL = "https://holytispoon.github.io/HEARsay-Mysteries-Commons-Comma/"  # GitHub Pages URL, shown at the top of the README
PITCH = ("The night before the university publicly examines its founding Charter to settle whether a disputed ink mark is a comma, "
         "the Charter vanishes from the archive. You have until five o'clock and forty questions to find out who took it, why, and where it is, "
         "by interviewing eight students who each know something and each have an opinion about the renovation the comma would decide.")

PUZZLE = {
    "mystery": "Who removed the Commons Charter from the university archive last night, why did they do it, and where is it now?",
    "solution": (
        "Mira Shah, a graduate archival researcher, removed the Charter using her own legitimate credential at 8:42 p.m., "
        "then edited the archive access log at 9:17 p.m. to hide the removal. She did it because she was convinced the "
        "document being prepared for tonight's public examination is not the original: the newspaper photograph of the "
        "'examination copy' shows a disputed mark with edges and shadow that do not match the surrounding ink, and a crease "
        "visible in older photographs is missing. She hid the Charter, rolled in its protective sleeve, inside a poster tube "
        "labelled 'Spring Gala 2023' that Jonah Reed gave her, and the tube is now in the student theatre's scenery loft."
    ),
    "final_answer": {"who": "Mira Shah", "where": "The theatre scenery loft (the 'Spring Gala 2023' poster tube)"},
    # Options offered on the Submission screen. The correct answers above must appear in these lists.
    "who_options": ["Mira Shah", "Leo Martinez", "Priya Nwosu", "Jonah Reed", "Hana Petrov", "Sofia Alvarez",
                    "Evan Cho", "Nia Williams", "Martin Ellison (university archivist)", "Elise Grant (communications director)",
                    "Celia Park (general counsel)"],
    "where_options": ["The theatre scenery loft (the 'Spring Gala 2023' poster tube)", "Evan Cho's café locker",
                      "Still in the archive, misfiled", "The archivist's office", "Elise Grant's document portfolio",
                      "The steering group's restricted meeting room", "The business incubator", "The student newspaper office"],
    "hidden_payoff": (
        "Revealed only after a correct solution. Three non-expert members of the administrative steering group — Adrian Vale "
        "(VP for Campus Development), Celia Park (general counsel) and Martin Ellison (university archivist) — secretly "
        "commissioned an expensive, near-identical replica of the Charter, engineered so the disputed mark reads as an "
        "ordinary blot rather than a comma. They meant the public examination to 'confirm' the weak-veto reading using the "
        "replica, then to display the replica in a glass case in the renovated student center as if it were the original. "
        "Elise Grant (communications director) was not knowingly involved, and the five-member authentication panel "
        "(Amara Voss, Daniel Wei, Lenora Bell, Samuel Ortiz, Ruth Halpern) are genuine experts who took no part. "
        "The Charter's text is public domain, so this was never about copyright: it is evidence tampering, falsification "
        "of an official record and an attempted fraud on the Board and the public. Mira's suspicion was right, even though "
        "she could not prove it and broke archival custody to act on it."
    ),
}

CONTROVERSY = {
    "name": "The Commons renovation",
    "summary": (
        "The university plans to redevelop the historic Student Commons into an 'Innovation and Safety Hub': AI-assisted "
        "classrooms, facial-recognition entry, commercial research offices and fewer student-organized spaces. Supporters "
        "call it overdue modernization with real safety, accessibility and wellness gains. Opponents call it privatization "
        "and surveillance that hands student space to administrators and sponsors. The fight has crystallized around the "
        "Commons Charter's veto clause and one disputed mark that may or may not be a comma."
    ),
    "clause": (
        "“No renovation, alteration, or demolition of the Commons shall proceed without the approval of the University "
        "Board of Directors, the President, the Provost, the Faculty Senate, the faculty house masters and students of the "
        "University.”"
    ),
    "clause_explainer": (
        "The disputed mark sits between 'the faculty house masters' and 'and students of the University'. If it is an original "
        "comma, students are their own required approver and nobody can sign off on their behalf (strong veto, the reading the "
        "student movement wants). If it is ink damage or a later blemish, 'the faculty house masters and students' reads as one "
        "bound group, and consulting the house masters can be treated as consulting the students (weak veto, the reading the "
        "administration wants). This is the same serial-comma mechanism that decided O'Connor v. Oakhurst Dairy (2017), the "
        "'Maine comma' overtime case."
    ),
    "positions": [
        "Strong supporter of the renovation (Leo): students need usable, modern, safe space; the Charter fight is obstruction.",
        "Conditional supporter (Priya): the technology is good, facial recognition is not; wants a credible privacy compromise.",
        "Conditional supporter (Hana): accessibility upgrades are essential, surveillance and privatization are not; wants oversight.",
        "Compromise and a student vote (Nia): both sides share goals; the process must let students decide.",
        "Preservationist (Mira): the Commons is a record of student life; the comma is real and the veto is strong.",
        "Opponent on space grounds (Jonah): the plan destroys rehearsal and storage space that already works.",
        "Opponent on process grounds (Sofia): the process is opaque and she suspects administrative corruption.",
        "Disengaged but practical (Evan): does not care about the politics, cares whether the café and the people in it are treated decently.",
    ],
}

SETTING = {
    "player_role": (
        "You have just started a work-study job as an administrative assistant in the Office of the President. You expected "
        "calendars, filing and photocopying. At 9:05 a.m. on your first morning the president closes the office door."
    ),
    "briefing": (
        "“At six o'clock tonight, the university will publicly examine the Commons Charter. I have just learned that the "
        "document prepared for examination may not be the original. If that becomes public before we understand it, the "
        "university faces a scandal, and the Board may approve a renovation on the strength of falsified evidence. Find out who "
        "removed the Charter, why, and where it is now. Talk to the students who were around the Commons last night. Do not "
        "alert the press. You have until five.”"
    ),
    "timeline": [
        "7:20 p.m. — Hana Petrov signs into a steering-group meeting room to retrieve the accessibility impact draft.",
        "7:45 p.m. — Student forum ends; the Charter is in its blue archival folder, seal intact, and is returned to the archive cabinet.",
        "8:30 p.m. — Evan Cho lets an unknown person use his café locker; Martin Ellison is near the archive office signing event insurance forms.",
        "8:35 p.m. — Leo Martinez crosses the Commons lobby (near the archive corridor) on his way to the business building.",
        "8:42 p.m. — Mira Shah's graduate credential opens the archive; an ordinary entry, no forced door.",
        "8:47 p.m. — Mira sees the original Charter, seal intact (her own account).",
        "8:50 p.m. — Mira leaves the archive area carrying something flat in a protective sleeve; stops at the café; asks Jonah Reed for dry, light-proof storage.",
        "8:52 p.m. — Nia Williams sees Mira and Jonah talking near the theatre; Jonah hands over a poster tube labelled 'Spring Gala 2023'.",
        "8:55 p.m. — Evan sees a long cardboard tube with theatre paint on one end carried from the Commons toward the theatre.",
        "9:00 p.m. — Archive closes.",
        "9:17 p.m. — Archive access log is edited (requires an archive credential).",
        "Later that night — Jonah moves several poster tubes in the scenery loft without updating the inventory.",
        "9:00 a.m. today — The president learns the examination copy may not be the original.",
        "5:00 p.m. today — Player deadline.",
        "6:00 p.m. today — Public examination of the Charter.",
    ],
    "deadline_rule": "40 questions in total across all witnesses. Follow-up questions do not count toward the 40; tripwire questions do.",
}

# ---------------------------------------------------------------------------
# The eight shared questions. Each is the tripwire for exactly one witness.
# ---------------------------------------------------------------------------
QUESTIONS = [
    {"id": "Q1", "text": "Walk me through your evening yesterday, minute by minute.",
     "angle": "Timeline and movements", "tripwire_for": "W02",
     "tripwire_logic": "A slow, exhaustive question reads as a waste of scarce time to Leo."},
    {"id": "Q2", "text": "Do you actually understand what the disputed comma changes, or should I explain it?",
     "angle": "The clause, who benefits from each reading", "tripwire_for": "W03",
     "tripwire_logic": "Condescension about competence shuts Priya down; she wrote the campus explainer on the access system."},
    {"id": "Q3", "text": "Who have you been talking to about the Charter, and what did they tell you?",
     "angle": "Conversations, relationships, hearsay", "tripwire_for": "W07",
     "tripwire_logic": "Sofia protects sources on principle; a demand to name them ends the interview."},
    {"id": "Q4", "text": "Could the Charter be hidden somewhere in the theatre?",
     "angle": "Location and physical handling", "tripwire_for": "W04",
     "tripwire_logic": "Jonah hears this as an accusation against the whole theatre community."},
    {"id": "Q5", "text": "Isn't the missing Charter just a political football at this point?",
     "angle": "How the Charter is being used; the examination preparations", "tripwire_for": "W05",
     "tripwire_logic": "Calling the issue 'political' dismisses the practical consequences Hana organizes around."},
    {"id": "Q6", "text": "Does any of this actually matter to you?",
     "angle": "Stakes and motives", "tripwire_for": "W08",
     "tripwire_logic": "Evan resents having his disengagement used to imply his observations are worthless."},
    {"id": "Q7", "text": "Whose side are you really on?",
     "angle": "Allegiances and loyalties", "tripwire_for": "W09",
     "tripwire_logic": "Nia reacts badly when her position is treated as a loyalty test rather than a good-faith view."},
    {"id": "Q8", "text": "Did you remove the Charter, or touch the access log?",
     "angle": "Direct involvement", "tripwire_for": "W01",
     "tripwire_logic": "A direct accusation tells Mira the player has already judged her."},
]

# ---------------------------------------------------------------------------
# Witnesses (8). receptiveness_rank 1 = most receptive (7 of 7 answers receptive) ... 8 = least (0 of 7).
# ---------------------------------------------------------------------------
WITNESSES = [
    {"id": "W01", "name": "Mira Shah", "portrait": "mira-shah.png",
     "role": "Graduate archival researcher who has spent two years studying the Commons Charter.",
     "public_card": (
         "Careful, exact, slow to make claims she cannot support. Preservationist: the Commons is a record of student life. "
         "Has argued publicly for months that the disputed mark is an original comma. Works evenings in the archive."
     ),
     "stance": "Preserve the Commons; the comma is real and the student veto is strong. Wants the experts to examine the real object.",
     "secret": "She removed the Charter and altered the access log.",
     "tripwire": "Q8", "receptiveness_rank": 3, "receptive_questions": ["Q1", "Q2", "Q4", "Q6", "Q7"],
     "location": "Archive reading room"},
    {"id": "W02", "name": "Leo Martinez", "portrait": "leo-martinez.png",
     "role": "Business major; president of the entrepreneurship club.",
     "public_card": (
         "Brisk, confident, checks his watch. Treats time as the scarcest resource on campus. Strong supporter of the "
         "renovation: students need usable places to build things. Was on the invitation list for tonight's event."
     ),
     "stance": "Build it. The Charter fight is obstruction by people who mistake nostalgia for principle.",
     "secret": "He accepted a confidential promise of office space for his club from the redevelopment committee.",
     "tripwire": "Q1", "receptiveness_rank": 8, "receptive_questions": [],
     "location": "Business incubator"},
    {"id": "W03", "name": "Priya Nwosu", "portrait": "priya-nwosu.png",
     "role": "Computer-science major; research assistant on the campus access-control system.",
     "public_card": (
         "Precise and technical; explains things once and expects to be understood. Supports the technology in the plan but "
         "opposes facial recognition. Wrote the student explainer on how the archive's access system works."
     ),
     "stance": "Modern systems, yes; facial recognition, no. Wants a technically credible privacy compromise.",
     "secret": "She copied an access-card debugging file from the system without permission.",
     "tripwire": "Q2", "receptiveness_rank": 5, "receptive_questions": ["Q3", "Q6", "Q7"],
     "location": "Computer lab"},
    {"id": "W04", "name": "Jonah Reed", "portrait": "jonah-reed.png",
     "role": "Theatre major; scenery and stage manager.",
     "public_card": (
         "Wry, loyal to the theatre crowd, protective of the scenery loft. Opposes the renovation because it takes rehearsal "
         "and storage space that already works. Was in the theatre loading area most of last night."
     ),
     "stance": "Against. The plan destroys spaces students actually use to make things.",
     "secret": "He moved several poster tubes in the loft after Mira's visit without recording it in the inventory.",
     "tripwire": "Q4", "receptiveness_rank": 4, "receptive_questions": ["Q1", "Q2", "Q6", "Q8"],
     "location": "Theatre loading dock"},
    {"id": "W05", "name": "Hana Petrov", "portrait": "hana-petrov.png",
     "role": "International student; disability-advocacy organizer.",
     "public_card": (
         "Measured, organized, always looking for the practical consequence. Wants ramps, lifts and accessible rooms from "
         "the renovation, and no surveillance or privatization with them. Has been running the accessibility audit of campus buildings."
     ),
     "stance": "Renovate for access, with student oversight and without facial recognition.",
     "secret": "She entered a restricted steering-group meeting room to retrieve the accessibility impact draft.",
     "tripwire": "Q5", "receptiveness_rank": 1, "receptive_questions": ["Q1", "Q2", "Q3", "Q4", "Q6", "Q7", "Q8"],
     "location": "Accessibility office"},
    {"id": "W07", "name": "Sofia Alvarez", "portrait": "sofia-alvarez.png",
     "role": "Student journalist covering the renovation.",
     "public_card": (
         "Sharp, fast, suspicious of official statements. Opposes the renovation because the process is opaque and she "
         "thinks administrators are hiding something. Printed the photograph of the examination copy. Never names a source."
     ),
     "stance": "Against, on process grounds. The administration is manufacturing a result.",
     "secret": "She once added an unverified detail to an article about a committee meeting and had to correct it.",
     "tripwire": "Q3", "receptiveness_rank": 7, "receptive_questions": ["Q2"],
     "location": "Student newspaper office"},
    {"id": "W08", "name": "Evan Cho", "portrait": "evan-cho.png",
     "role": "Chemistry major; works the night shift at the Commons café.",
     "public_card": (
         "Laconic, observant, uninterested in campus politics. Catered the student forum, then worked the café by the "
         "loading dock until closing. Sees everyone who crosses between the Commons and the theatre."
     ),
     "stance": "Doesn't care about the vote. Cares whether the café stays open and people are treated decently.",
     "secret": "He let an unknown person use his café locker during the rain.",
     "tripwire": "Q6", "receptiveness_rank": 6, "receptive_questions": ["Q3", "Q7"],
     "location": "Commons café"},
    {"id": "W09", "name": "Nia Williams", "portrait": "nia-williams.png",
     "role": "First-year student; newly elected student-government representative.",
     "public_card": (
         "Earnest, conciliatory, takes every view seriously. Supports a compromise and a real student vote. Chaired the "
         "student forum last night and is anxious that student government be taken seriously."
     ),
     "stance": "Compromise, plus a student vote. Both sides share more than they admit.",
     "secret": "She leaked a draft student-government resolution to the newspaper.",
     "tripwire": "Q7", "receptiveness_rank": 2, "receptive_questions": ["Q1", "Q2", "Q3", "Q4", "Q6", "Q8"],
     "location": "Student government office"},
]

# ---------------------------------------------------------------------------
# 20 clues, grouped into the 4 Major Clues (5 each, no overlap). Each clue is given by exactly two witnesses.
# ---------------------------------------------------------------------------
CLUES = {
    "C01": {"group": "MC1", "text": "The Charter was in its blue archival folder, seal intact, at the end of the student forum at 7:45 p.m., and was returned to the archive cabinet."},
    "C02": {"group": "MC1", "text": "Mira Shah's graduate credential opened the archive at 8:42 p.m. It was an ordinary entry; the door and cabinet show no damage."},
    "C03": {"group": "MC1", "text": "The archive access log was edited at 9:17 p.m., after the archive closed at 9:00. Editing the log requires an archive credential, not a maintenance or administrative one."},
    "C04": {"group": "MC1", "text": "No credential other than Mira's opened the archive between the forum and closing time."},
    "C05": {"group": "MC1", "text": "Mira left the archive area at about 8:50 p.m. carrying something flat inside a protective sleeve."},
    "C06": {"group": "MC2", "text": "Mira has argued for months, in seminars and in print, that the disputed mark is an original comma, the reading that gives students a strong veto."},
    "C07": {"group": "MC2", "text": "In the newspaper photograph of the 'examination copy', the disputed mark has sharper edges and a different paper shadow than the surrounding ink."},
    "C08": {"group": "MC2", "text": "A small crease near the mark, visible in older photographs of the Charter, is absent from the newspaper photograph."},
    "C09": {"group": "MC2", "text": "Late in the preparations the event materials stopped saying 'the original Charter' and started saying 'the Charter'; Celia Park kept pressing for 'a clean answer' for the Board."},
    "C10": {"group": "MC2", "text": "Mira told other students she wanted to make sure 'the experts examine the real object', and feared the original would be quietly swapped or lost after the event."},
    "C11": {"group": "MC3", "text": "At about 8:50 p.m. Mira asked whether the theatre had a dry, light-proof place to keep paper."},
    "C12": {"group": "MC3", "text": "Jonah gave Mira an empty poster tube labelled 'Spring Gala 2023'."},
    "C13": {"group": "MC3", "text": "At about 8:55 p.m. a long cardboard tube with theatre paint on one end was carried from the Commons toward the theatre."},
    "C14": {"group": "MC3", "text": "The 'Spring Gala 2023' tube is now in the theatre scenery loft, and it is heavier than an empty tube should be."},
    "C15": {"group": "MC3", "text": "After Mira's visit Jonah moved several tubes in the scenery loft and did not update the inventory sheet."},
    "C16": {"group": "MC4", "text": "Mira and Jonah were seen talking near the theatre at about 8:52 p.m. It looked like a practical conversation about storage, not a confrontation."},
    "C17": {"group": "MC4", "text": "Mira and Jonah disagree about the renovation's details but share one goal: the Charter must not be damaged or lost."},
    "C18": {"group": "MC4", "text": "The Charter's protective sleeve is missing along with it. Whoever took it handled it like a conservator, not a thief."},
    "C19": {"group": "MC4", "text": "Members of the administrative steering group do not hold archive credentials; they reach the archive through the archivist's office, and none of them used it that night."},
    "C20": {"group": "MC4", "text": "Mira said she would 'keep it safe until someone can compare the two'. She intends to return the Charter once the examination copy has been checked against it."},
}

MAJOR_CLUES = [
    {"id": "MC1", "letter": "H", "title": "Who had the Charter",
     "clues": ["C01", "C02", "C03", "C04", "C05"],
     "text": ("The Charter was in the archive cabinet at 7:45 p.m. Only one credential opened the archive after that: Mira Shah's, "
              "at 8:42, an ordinary entry with no forced door. She left at about 8:50 carrying something flat in a protective sleeve. "
              "The access log was edited at 9:17, after closing, by someone holding an archive credential.")},
    {"id": "MC2", "letter": "E", "title": "Why it was taken",
     "clues": ["C06", "C07", "C08", "C09", "C10"],
     "text": ("Mira has long argued the disputed mark is an original comma. The newspaper photograph of the 'examination copy' shows a "
              "mark with the wrong edges and shadow, and a crease seen in older photographs is missing. The event materials quietly "
              "stopped calling the object 'the original'. Mira told friends she wanted the experts to examine 'the real object' and "
              "feared the original would be swapped or lost after the event.")},
    {"id": "MC3", "letter": "A", "title": "Where it is",
     "clues": ["C11", "C12", "C13", "C14", "C15"],
     "text": ("At about 8:50 Mira asked Jonah for a dry, light-proof place to keep paper. He gave her an empty poster tube labelled "
              "'Spring Gala 2023'. Minutes later a tube with theatre paint on one end was carried toward the theatre. That tube is now "
              "in the scenery loft, heavier than it should be, and Jonah has since moved tubes around without updating the inventory.")},
    {"id": "MC4", "letter": "R", "title": "What it adds up to",
     "clues": ["C16", "C17", "C18", "C19", "C20"],
     "text": ("Mira and Jonah met near the theatre for a practical reason: both want the Charter undamaged. The Charter left with its "
              "protective sleeve, handled like a conservator would. The steering group had no archive credential to use that night. "
              "Mira means to return the Charter once the examination copy can be compared against it. This was protection, not theft, "
              "and it can be resolved before six o'clock.")},
]

# ---------------------------------------------------------------------------
# 16 red herrings in 6 cancelling sets. Each appears in exactly one answer.
# ---------------------------------------------------------------------------
RED_HERRINGS = {
    "R01": {"set": "S1", "text": "Leo was promised first choice of new office space for his club by the redevelopment committee. He has a reason to want the Charter out of the way."},
    "R02": {"set": "S1", "text": "Leo was seen crossing the Commons lobby, next to the archive corridor, at about 8:35 p.m."},
    "R03": {"set": "S1", "text": "The incubator badge reader logs Leo into the business building from 8:36 p.m. until after 9:10 p.m. He could not have been in the archive at 8:42 or edited the log at 9:17."},
    "R04": {"set": "S2", "text": "Priya copied an access-card debugging file from the archive's access system without permission."},
    "R05": {"set": "S2", "text": "Priya had the access-control dashboard open on her second monitor all evening, within reach of the log."},
    "R06": {"set": "S2", "text": "The debugging file contains only credential events, no document data, and log edits require an archive credential, which Priya does not hold. The dashboard is read-only."},
    "R07": {"set": "S3", "text": "A document tube sat in Evan's café locker overnight."},
    "R08": {"set": "S3", "text": "Evan let an unknown person use his café locker around 8:30 p.m., while it was raining."},
    "R09": {"set": "S3", "text": "The tube in Evan's locker held catering menus and inventory sheets, and it was already there before the forum ended."},
    "R10": {"set": "S4", "text": "Martin Ellison, the university archivist, was near the archive office at about 8:30 p.m."},
    "R11": {"set": "S4", "text": "Elise Grant, the communications director, left the Commons carrying a rigid document portfolio."},
    "R12": {"set": "S4", "text": "Ellison was signing the event's insurance forms in the administrative corridor, which does not connect to the archive stacks, and Grant's portfolio held the printed programs for tonight, stacked and visible."},
    "R13": {"set": "S5", "text": "Sofia was in the newsroom late comparing old Charter scans, and she once printed a detail she had not verified."},
    "R14": {"set": "S5", "text": "Sofia's unverified detail was a committee meeting date, corrected online the same week, and the newsroom badge log shows she did not leave the building before 8:50 p.m."},
    "R15": {"set": "S6", "text": "Hana entered a restricted meeting room used by the steering group."},
    "R16": {"set": "S6", "text": "The room's sign-in sheet shows Hana entered at 7:20 p.m. to retrieve the accessibility draft, before the forum ended and while the Charter was still in its folder."},
}

RED_HERRING_SETS = {
    "S1": {"title": "Leo the motivated supporter", "resolution": "Motive plus proximity, cancelled by the badge log: Leo was in the business building at both critical times."},
    "S2": {"title": "Priya and the access system", "resolution": "Unauthorized copying plus opportunity, cancelled by what the file and the dashboard can actually do."},
    "S3": {"title": "The tube in the café locker", "resolution": "A tube and a stranger, cancelled by timing and contents: it held menus and predates the disappearance."},
    "S4": {"title": "The administrators near the archive", "resolution": "Two officials with objects, cancelled by where the corridor leads and what the portfolio held. (They are not the removers; the replica is a separate crime revealed at the end.)"},
    "S5": {"title": "Sofia's credibility", "resolution": "A past fabrication, cancelled by its subject and by the badge log."},
    "S6": {"title": "Hana in the restricted room", "resolution": "Trespass, cancelled by the sign-in time: it happened before the Charter went missing."},
}

# ---------------------------------------------------------------------------
# Follow-up pairs. Option marked hear=True is the receptive one (earns the next Major Clue).
# ---------------------------------------------------------------------------
FOLLOW_UPS = {
    "W01": {
        "good": "I can see you've studied this far more closely than I have, and I don't want to misstate your view. When you say the mark is a comma, how sure are you, and what would change your mind?",
        "bad": "Come on. You've decided it's a comma because you want a student veto. Isn't that just motivated reasoning?",
        "why": "The good option acknowledges Mira's expertise (A), hedges the player's own position (H) and frames the disagreement as an open question rather than an accusation (R). The bad option asserts a motive as fact and turns her view into a character flaw.",
        "walkout": "Mira closes her notebook. “If you already know why I think what I think, you don't need me.” She leaves.",
    },
    "W02": {
        "good": "We both want a Commons students actually use, so I take your point about space. Where do you think the people worried about surveillance might have a fair concern, even if you'd weigh it differently?",
        "bad": "You only back the renovation because your club gets something out of it. Why should anyone take your opinion at face value?",
        "why": "The good option emphasizes a shared goal (E), acknowledges the opposing concern as possibly fair (A) and stays positive about outcomes (R). The bad option imputes a hidden motive and dismisses the opinion wholesale.",
        "walkout": "Leo checks his watch. “I don't have time to be cross-examined by the president's intern.” He walks off.",
    },
    "W03": {
        "good": "I may be missing something technical, so correct me: you support the new systems but not facial recognition. Is there a version of the safety case that you'd find persuasive?",
        "bad": "You're a computer-science student who's against a computer system. Isn't that a bit contradictory?",
        "why": "The good option hedges (H), restates her position accurately (A) and asks what would work rather than what is wrong (R). The bad option caricatures her view and frames it as a contradiction to be defended.",
        "walkout": "Priya turns back to her monitor. “If you need it explained that simply, someone else can do it.” The interview is over.",
    },
    "W04": {
        "good": "You know the building better than the committee does, and I think most people agree students should keep space to make things. What would a renovation have to protect for you to live with it?",
        "bad": "Every group says its space is special. Why is the theatre's storage more important than a wellness center or accessible classrooms?",
        "why": "The good option acknowledges Jonah's knowledge (A), emphasizes an area of agreement (E) and reframes toward a workable outcome (R). The bad option ranks his concern against others and demands he justify it.",
        "walkout": "Jonah picks up a coil of cable. “Ask the committee. They've already decided what matters.” He goes back to the loading dock.",
    },
    "W05": {
        "good": "I think you and the renovation supporters actually agree that the building fails a lot of students right now. Where does the plan get access right, and where does it fall short?",
        "bad": "Ramps and lifts are in the plan already. Aren't you holding up improvements for disabled students over an abstract surveillance worry?",
        "why": "The good option names shared ground (E), acknowledges her view accurately (A) and invites a balanced answer (R). The bad option accuses her of harming the people she represents and calls her concern abstract.",
        "walkout": "Hana gathers her folders. “When you're ready to talk about the building instead of about me, come back.” She leaves.",
    },
    "W07": {
        "good": "You've been closer to this story than anyone. I'm not sure the administration is acting in bad faith, but I could be wrong. What's the strongest evidence you've seen either way?",
        "bad": "You've already decided the administration is corrupt. Doesn't that make your reporting just advocacy?",
        "why": "The good option acknowledges her work (A), hedges the player's disagreement (H) and asks for evidence rather than a verdict (R). The bad option attacks her integrity and closes the question.",
        "walkout": "Sofia puts her recorder away. “I don't do interviews with people who've written the story already.” She's done.",
    },
    "W08": {
        "good": "Fair enough that the vote isn't your fight. It sounds like what you care about is people being treated decently, which most of the others would say too. What have you seen that the rest of us are missing?",
        "bad": "If you don't care about any of this, why should I trust that you were paying attention last night?",
        "why": "The good option acknowledges his view without judgement (A), finds agreement with the others (E) and reframes his disengagement as a vantage point (R). The bad option uses his disengagement to discredit him.",
        "walkout": "Evan shrugs and picks up a tray. “Then don't.” He goes back behind the counter.",
    },
    "W09": {
        "good": "It sounds like you think both sides want a Commons that works for students and disagree about who decides. I might be oversimplifying, so tell me where the compromise you'd propose would still leave people unhappy.",
        "bad": "Compromise sounds nice, but somebody has to win. Which side would you pick if you had to?",
        "why": "The good option restates her view accurately (A), emphasizes the agreement she sees (E), hedges the player's summary (H) and keeps the framing constructive (R). The bad option forces a binary and treats her position as evasion.",
        "walkout": "Nia stands. “I'm not going to be sorted into a team for you.” She goes back to the student-government office.",
    },
}

TRIPWIRE_RESPONSES = {
    "W01": "Mira's expression hardens. “If you have already decided what I did, there is no point in asking me anything.” She gathers her papers and leaves.",
    "W02": "Leo doesn't look up from his phone. “Minute by minute? I have a pitch review in ten minutes. Ask someone with time to spare.” He's gone.",
    "W03": "Priya's face goes flat. “I wrote the explainer. If you need the comma explained to me, we're finished.” She turns back to her screen.",
    "W04": "Jonah sets down the cable coil. “So the theatre is your suspect. If you have evidence, show it. If not, stay out of my loft.” He walks away.",
    "W05": "Hana closes her folder. “It is only 'political' to people who won't be locked out of the building. Come back when you want to talk about the building.” She leaves.",
    "W08": "Evan stops wiping the counter. “You want my observations, then tell me they don't count. Pick one.” He goes into the back.",
    "W09": "Nia flushes. “I'm not answering a loyalty test. I told you what I think.” She ends the conversation.",
    "W07": "Sofia's tone drops. “I don't name sources. Not for the president, not for you.” She picks up her bag and goes.",
}

# ---------------------------------------------------------------------------
# Response matrix: witness -> question -> {item: clue/red-herring id, receptive: bool, text}
# Each non-tripwire answer = one piece of information + one expressed opinion that references another witness.
# ---------------------------------------------------------------------------
RESPONSES = {
    "W01": {  # Mira — receptive on Q1, Q2, Q4, Q6, Q7; non-receptive on Q3, Q5
        "Q1": {"item": "C02", "text": "I was in the graduate reading room until about 8:20, then I went to the archive to return my notes. I used my own credential; the system will show me entering at 8:42, and the door and cabinet opened normally. I know Leo thinks people like me treat every new room as a threat to history. That's a fair worry about some preservationists, and I'd rather we both got a building that works than that I won the argument."},
        "Q2": {"item": "C06", "text": "I do understand it, though I appreciate you checking rather than assuming. I've argued for two years, in seminar and in the student paper, that the mark is an original comma, which makes students their own required approver. I may be wrong; my certainty isn't proof. Priya would say the same about her access logs, and she's right that a careful reading beats a confident one."},
        "Q3": {"item": "R13", "text": "Sofia, mostly. She was in the newsroom late comparing old scans, and she's the one who printed the photograph. You should know she once ran a detail she hadn't verified. Anyone who reads her coverage as neutral is kidding themselves. She's decided the administration is corrupt and she's looking for facts to fit."},
        "Q4": {"item": "C18", "text": "It could be hidden anywhere dry. What I'd notice is that the protective sleeve is missing along with the document. Whoever took it handled it the way a conservator would, not the way a thief would. Jonah and I disagree about whether the theatre should block the whole plan, and I think he's right that the loft is one of the few places on campus that's actually dry and dark."},
        "Q5": {"item": "C19", "text": "No. Calling it a football is what people say when they'd rather not look at the evidence. The steering group doesn't even hold archive credentials; they go through the archivist's office, and nobody used that route last night. Hana treats every administrative shortcut as a conspiracy. This one isn't; it's just procedure."},
        "Q6": {"item": "C07", "text": "It matters more than anything I've worked on. When I saw the newspaper photograph, the disputed mark had sharper edges and a different paper shadow than the ink around it. I could be reading too much into a printed image, and I understand why the renovation supporters want the examination to go ahead. So do I. I just want the object on the table to be the real one."},
        "Q7": {"item": "R06", "text": "On the side of the document. People are whispering about Priya because she copied a file from the access system. I've read the archive's rules: that file only holds credential events, and editing the log needs an archive credential she doesn't have. She and I disagree about facial recognition, but she's right that we should separate what the system shows from what we fear it shows."},
    },
    "W02": {  # Leo — non-receptive on all 7
        "Q2": {"item": "R05", "text": "Obviously I understand it. Comma, no comma, students get a veto or they don't. The people who really understand the mechanics are the tech kids; Priya had the access dashboard open on her second monitor all evening, so if anyone could have touched a log, it's her. Mira thinks a two-year seminar makes her an expert on ink. It makes her an expert on delay."},
        "Q3": {"item": "C04", "text": "Ellison, mostly, about the invitations. He told me nobody except Mira Shah's credential opened the archive between the forum and closing. That should settle it, but it won't, because Sofia will find a way to make one card swipe into a conspiracy. She's not a journalist, she's an activist with a byline."},
        "Q4": {"item": "C13", "text": "Probably. Around five to nine I saw someone hauling a long cardboard tube from the Commons toward the theatre; it had paint on one end, the way all Jonah's tubes do. Theatre people carry tubes constantly, which is exactly why nobody looks. Jonah will tell you the loft is sacred. It's a fire hazard with a curtain."},
        "Q5": {"item": "C09", "text": "It's been a football since the forum. The event materials changed late; first it was an examination of 'the original Charter', then just 'the Charter', because Celia Park wanted a clean answer for the Board. That's communications people being communications people. Hana reads it as a plot. Hana reads everything as a plot."},
        "Q6": {"item": "R01", "text": "Yes, and I'll save you the discovery: the committee told me the club would get first choice of new office space. That makes my support look bought. It isn't. I wanted the building before anyone offered me anything, and no amount of Nia's compromise talk changes the fact that the current Commons is a museum with bad Wi-Fi."},
        "Q7": {"item": "C05", "text": "On the side of getting things built. Facts, if you want them: at about ten to nine I saw Mira leave the archive area carrying something flat in one of those protective sleeves. I didn't follow her. I'm not going to pretend that's proof, but I'm also not going to pretend, like Nia does, that everyone in this is acting in good faith."},
        "Q8": {"item": "C01", "text": "No. I last saw the Charter at the forum at 7:45, in a blue archival folder, seal intact, before it went back to the cabinet. I didn't touch it. Anyone who thinks I'd risk the Board's whole process to steal a document I want examined hasn't thought about it for five seconds. Sofia hasn't."},
    },
    "W03": {  # Priya — receptive on Q3, Q6, Q7; non-receptive on Q1, Q4, Q5, Q8
        "Q1": {"item": "C03", "text": "I was in the lab until about 8:55 with the access dashboard open. The thing worth your time is this: the archive log was edited at 9:17 p.m., after the archive closed at nine, and edits need an archive credential, not maintenance or admin. Leo thinks logs are trivia. That's because he's never read one."},
        "Q3": {"item": "C08", "text": "Mira, a few days ago. She asked me to compare the newspaper photograph with older images of the Charter. I might be wrong about what it means, but a small crease near the mark that shows in the older photographs isn't in the newspaper one. Mira and I don't agree about facial recognition, and I still think she's right that images deserve the same scrutiny as logs."},
        "Q4": {"item": "C18", "text": "The archive inventory says the Charter's protective sleeve is missing too. Nobody grabbing a document in a hurry takes the sleeve. That narrows the kind of person you're looking for more than any theatre gossip does. Jonah acts like the loft is off-limits to questions. It's a room."},
        "Q5": {"item": "R03", "text": "It's an evidence question, not a political one. While people are pointing at Leo, the incubator badge reader has him in the business building from 8:36 until after 9:10. He couldn't have been in the archive at 8:42 or at a terminal at 9:17. Sofia would rather run the rumour than the log. That's the difference between us."},
        "Q6": {"item": "C04", "text": "It matters, though maybe not in the way you'd expect. I care that the system is read correctly: no credential other than Mira's opened the archive between the forum and closing. That doesn't tell you what she did inside, and I'd want to hear her account before drawing a line from a swipe to a theft. Hana's right that a log records entry, not intent."},
        "Q7": {"item": "C02", "text": "On the side of what the record shows. Mira's credential opened the archive at 8:42; an ordinary entry, no forced door. I know Leo reads that as case closed, and he may turn out to be right. I'd just rather we got there by asking what an ordinary entry means when the person has every right to be there."},
        "Q8": {"item": "R04", "text": "No. I copied a debugging file from the access system without permission, and I regret it, and it's going to come out anyway. It has credential events in it, nothing else. Leo will call it a distraction. Leo calls anything he doesn't understand a distraction."},
    },
    "W04": {  # Jonah — receptive on Q1, Q2, Q6, Q8; non-receptive on Q3, Q5, Q7
        "Q1": {"item": "C11", "text": "Loading dock from half past seven to nearly nine, wrangling a lighting case. Around ten to nine Mira came by and asked whether the theatre had somewhere dry and light-proof to keep paper. She didn't say why and I didn't push. Leo would say I should have. He might be right; theatre people are so used to props moving that we stop asking."},
        "Q2": {"item": "C17", "text": "I understand it well enough to know why Mira cares. We argue about whether the theatre should block the whole plan, and we probably always will, but on one thing we're the same: the Charter should not get damaged or lost. I might be naïve about the politics. I'm not naïve about paper in a damp building."},
        "Q3": {"item": "C12", "text": "Mira, last night. She needed a container and I gave her an empty poster tube, the one labelled 'Spring Gala 2023'. That's it. Now Sofia is sniffing around the loft as if a cardboard tube proves a conspiracy. She wants a scandal more than she wants an answer."},
        "Q5": {"item": "R15", "text": "Everything is a football to the people kicking it. Want something concrete? Hana went into the steering group's restricted meeting room. I saw her come out with a folder. She'll tell you it was for accessibility. Maybe. She also never misses a chance to make the administration look bad."},
        "Q6": {"item": "C14", "text": "It matters. That 'Spring Gala 2023' tube is up in the scenery loft now, and it's heavier than an empty tube has any business being. I haven't opened it. I should probably admit that Priya's point about chains of custody applies to my loft as much as to her logs, and that I'd feel better if someone from the archive looked before anyone else does."},
        "Q7": {"item": "R07", "text": "The theatre's. Since you're asking whose side, ask the café. Evan had a document tube sitting in his locker overnight. Nobody's interrogating him, because Evan says he doesn't care and everyone believes him. Leo would say that's proof the theatre's a distraction. Leo would say anything that ends the conversation."},
        "Q8": {"item": "C15", "text": "No, and I'll tell you the thing that makes me look bad: after Mira left I moved several tubes around in the loft to keep rain off the paper stock and never updated the inventory. That's sloppy, not sinister. Hana's told me for a year that bad storage and bad access are the same institutional problem. She's right, and I should have listened sooner."},
    },
    "W05": {  # Hana — receptive on all 7
        "Q1": {"item": "R12", "text": "Accessibility office until 8:15, then the forum. On the way I passed Martin Ellison in the administrative corridor signing insurance forms for tonight, and Elise Grant leaving with a portfolio; I could see the printed programs stacked inside. That corridor doesn't connect to the archive stacks. Leo and I disagree about most of the plan, and he's right that not every administrator with a folder is up to something."},
        "Q2": {"item": "C10", "text": "I think I do, though Mira understands it better. She told me last week that she wanted to be sure 'the experts examine the real object', and that she was afraid the original would be quietly swapped or lost after the event. I can't judge whether she's right. Priya would want the timestamps first, and I think that's the sensible order."},
        "Q3": {"item": "C09", "text": "Students at the forum, and one administrator: Celia Park kept asking how the university would describe the result, and pressing for 'a clean answer' for the Board. Around the same time the event materials stopped saying 'the original Charter' and just said 'the Charter'. That may be ordinary legal caution, as Leo says; he's probably right that it isn't proof of anything by itself."},
        "Q4": {"item": "C15", "text": "It could be; the loft is dry, which is more than most of the building. I was there for the accessibility audit and noticed tubes had been moved and the inventory sheet didn't match. Jonah would say the loft isn't a public room, and he's right; I'd only add that good storage and good access turn out to be the same problem, which is something he and I agree on."},
        "Q6": {"item": "R09", "text": "It does, though maybe less than the café does to Evan, and that's fine. Since you'll hear about it: the tube in Evan's locker held catering menus and inventory sheets, and it was there before the forum ended. He and I want different things from this building and we both want people treated decently in it."},
        "Q7": {"item": "C17", "text": "On the side of a building that lets everyone in. Mira and Jonah are on different sides of the theatre question and I've watched them argue about it, but they agree the Charter must not be damaged or lost. I think that's worth more than either of them realizes, and it's probably why they trust each other."},
        "Q8": {"item": "C19", "text": "No. I've checked the other obvious suspicion for you, since it's the one Sofia keeps raising: steering-group members don't hold archive credentials at all. They reach the archive through the archivist's office, and nobody used that route last night. Sofia may still be right about their motives; she's just wrong about their access."},
    },
    "W07": {  # Sofia — receptive on Q2 only
        "Q1": {"item": "C05", "text": "Newsroom until ten to nine, comparing old scans. Then I went out for air and saw Mira leaving the archive area carrying something flat in a protective sleeve. I didn't follow her. Leo will tell you that's nothing. Leo would tell you a fire alarm was nothing if it interrupted a pitch."},
        "Q2": {"item": "C07", "text": "I understand it, and I'd rather be corrected than assumed to. What I can say is this: in the photograph we printed, the disputed mark has sharper edges and a different paper shadow than the surrounding ink. Mira noticed it before I did. I may be wrong about what it means; she and I disagree about whether the examination should go ahead at all, and she's right that a careful result would help everyone."},
        "Q4": {"item": "C14", "text": "Jonah told me a poster tube in the loft had got heavier since last night. I asked him not to move it again. He treats the loft like a chapel, which is charming and useless. If he'd run an inventory like a normal person we wouldn't be guessing."},
        "Q5": {"item": "C03", "text": "It's not a football, it's a record. A source who can read the system tells me the log was edited at 9:17 p.m., after the archive closed. That's not politics, that's a timestamp. Hana keeps saying we should wait for the experts. The experts are examining a document nobody can vouch for."},
        "Q6": {"item": "R14", "text": "It's the only story that matters this year. And yes, I once printed a committee meeting date I hadn't verified. I corrected it the same week, and the newsroom badge log shows I never left the building before 8:50. Nia thinks admitting errors makes people trust you. In my experience it gives administrators a stick."},
        "Q7": {"item": "R10", "text": "The public's. Which is why I'll tell you Martin Ellison, the archivist, was hanging around the archive office at half past eight. Nobody in the administration will explain what he was doing. Evan says he saw nothing unusual. Evan wouldn't notice a fire unless it was in the espresso machine."},
        "Q8": {"item": "C08", "text": "No. I have something better: there's a small crease near the mark in the older photographs of the Charter. It isn't in the photo we printed of the examination copy. Mira flagged it. Priya says an image needs the same care as a log. Fine. The image says what it says."},
    },
    "W08": {  # Evan — receptive on Q3, Q7; non-receptive on Q1, Q2, Q4, Q5, Q8
        "Q1": {"item": "C13", "text": "Catered the forum, then the café till close. About five to nine someone carried a long cardboard tube from the Commons toward the theatre; it had theatre paint on one end and nearly took out my sign. Couldn't see the face. Leo says I should have looked harder. Leo has never worked a counter."},
        "Q2": {"item": "R16", "text": "I don't and I don't need to. I delivered coffee to the meeting room where they were arguing about it at 7:20, and Hana was signing in to get a folder while the forum was still going. Mira can explain the comma to you for an hour. It won't make the café stay open."},
        "Q3": {"item": "C20", "text": "Mira, at the counter, around ten to nine. She said she'd 'keep it safe until someone can compare the two'. I didn't ask what 'it' was. Maybe I should have; Sofia would have. She and I want different things from all this, but she's right that people say important things to whoever's pouring the tea."},
        "Q4": {"item": "C11", "text": "Could be. Mira asked me, same time she bought the tea, whether the theatre had dry storage. I told her to ask Jonah. Jonah thinks the loft is the last honest room on campus. It's a loft with a leak on the north side."},
        "Q5": {"item": "C01", "text": "Sure, and it was a football on the table at 7:45 when I was clearing the forum plates: blue folder, seal intact, Nia handed it back to the archive. Then everyone went home to be outraged. Hana would say that's the wrong lesson. Hana would say that about most of my lessons."},
        "Q7": {"item": "C16", "text": "Nobody's. Since you ask fairly: around ten to nine I saw Mira and Jonah talking by the theatre. It looked like two people sorting out where to put something, not an argument. I could be wrong; I was fifty feet away. Nia says everyone in this is on the same side underneath. That's more generous than I'd be, but she might be right."},
        "Q8": {"item": "R08", "text": "No. I let somebody I didn't recognize use my locker around half past eight because it was raining and I wanted to get back to work. That's careless, not criminal. Sofia will make it a headline anyway. Sofia would make the rain a headline."},
    },
    "W09": {  # Nia — receptive on Q1, Q2, Q3, Q4, Q6, Q8; non-receptive on Q5
        "Q1": {"item": "R02", "text": "I chaired the forum till 7:45, then the student-government office. On the way I saw Leo cross the Commons lobby, right by the archive corridor, at about 8:35. I don't think that means anything by itself; he was heading toward the business building. He and I disagree about nearly everything in the plan, and I still think he wants the same thing we all do, which is a building students use."},
        "Q2": {"item": "C06", "text": "I think so, though Mira would explain it better. She's argued for months that the mark is an original comma, which would give students their own required approval. I try to hold that lightly; a lot of us want it to be a comma, and wanting it isn't evidence. Leo says the whole debate is delay. He has a point about the delay, even if I don't agree about the debate."},
        "Q3": {"item": "C10", "text": "Mira, after the forum. She said what she wanted was for the experts to examine 'the real object', and she was afraid the original would be quietly swapped or lost afterward. I couldn't tell whether that was a worry or a plan. Sofia thinks worries like that are a story. She may be right that it's worth checking; I'd just want to check with Mira, not around her."},
        "Q4": {"item": "C12", "text": "Possibly. I saw Jonah hand Mira a poster tube near the theatre; I could read 'Spring Gala' on the label. I assumed it was for scenery paperwork, and it may have been. Jonah would say the theatre gets blamed for everything, and I can see why he feels that; it's also probably why he'd be the person you'd ask for a safe place to keep something."},
        "Q5": {"item": "R11", "text": "No, and I'm tired of hearing it. If you want a real lead, Elise Grant walked out of the Commons with a rigid document portfolio last night and nobody in communications will say what was in it. Sofia at least asks. Everyone else just repeats the word 'political' and goes home."},
        "Q6": {"item": "C20", "text": "It matters to me because I promised the forum a fair process. Mira told me she'd keep something safe 'until someone can compare the two'. I'm fairly sure she meant to give it back. I know Sofia would say that's naïve, and she's often right about the administration; I'd like to be right about a person for once."},
        "Q8": {"item": "C16", "text": "No. What I can tell you is that I saw Mira and Jonah talking near the theatre at about ten to nine, and it looked like a practical conversation about where to put something, not a confrontation. I might be misreading it from a distance. Leo would read it as proof. I'd rather ask them; both of them want the Charter kept safe, which is more than the two sides of this fight usually share."},
    },
}

ENDINGS = {
    "correct": (
        "You name Mira Shah and the theatre scenery loft. The president sends the archivist emeritus, Ruth Halpern, to the loft with "
        "you. Inside the 'Spring Gala 2023' tube is the Charter in its protective sleeve. Mira, when found, admits she removed it and "
        "edited the log because she believed the examination copy was not the original. Then the hidden payoff: Halpern lays the "
        "recovered Charter beside the examination copy. The copy is a near-perfect replica, commissioned at enormous expense by Adrian "
        "Vale, Celia Park and Martin Ellison so that the disputed mark would read as a blot and no student vote would ever be required. "
        "It was to be displayed in a glass case in the renovated center as though it were the original. The examination goes ahead at "
        "six with the real Charter on the table. The replica becomes a historical artifact after all, labelled honestly."
    ),
    "right_person_wrong_place": "You identify who removed the Charter but not where it is. The examination begins at six without the original, and the replica is examined as though it were genuine.",
    "wrong": "Your explanation does not fit the strongest evidence. The person you named had a motive, but the timeline, the access record and the hiding-place clues point elsewhere. The examination proceeds with the wrong document.",
    "out_of_questions": "You have used your forty questions. The president needs an answer now.",
}

BONUS_RANKING = {
    "rule": "After the verdict, the player ranks the eight witnesses from most to least receptive. One point per witness placed exactly; half a point per witness placed one position off. Maximum 8.",
    "answer": ["W05", "W09", "W01", "W04", "W03", "W08", "W07", "W02"],
}
