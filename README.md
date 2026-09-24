# HEARsay Mysteries: The Commons' Comma

**Play online: https://holytispoon.github.io/HEARsay-Mysteries-Commons-Comma/**

A short investigative game about conversational receptiveness. You interview eight student witnesses on a university campus, and you get the most out of them by using the HEAR framework (**H**edge your claims, **E**mphasize agreement, **A**cknowledge the other perspective, **R**eframe to the positive), which comes from Julia Minson's research on conversational receptiveness.

The game is built in [Twine 2](https://twinery.org) with the [SugarCube 2](https://www.motoslave.net/sugarcube/2/) story format.

## Play

- **Online:** open the GitHub Pages link for this repository.
- **Offline:** download the repository (Code → Download ZIP), unzip it, and open `index.html` in a web browser. Keep `index.html` and the `assets` folder together; the images are loaded from `assets/`.

A game takes about 45 to 75 minutes. Progress can be saved from the sidebar (Saves). Saves are kept in the browser you're playing in.

## What's in this repository

| Path | What it is |
|---|---|
| `index.html` | The compiled game. This is the only file a player needs, along with `assets/`. |
| `assets/` | Witness portraits and the campus map. |
| `engine/hearsay_engine.twee` | The generic game engine: SugarCube passages, JavaScript and CSS. It is the same for every scenario. |
| `engine/build_twine.py` | Build script: checks the scenario, adds its data to the engine, and compiles `index.html` with Tweego. |
| `engine/scenario_matrix.py` | Reads the Response Matrix and checks the framework's rules (tripwires, clue counts, receptiveness ranks) and that the workbook agrees with itself. |
| `engine/check_packet.py` | Checks that the scenario packet says the same things as the Response Matrix. |
| `scenario/The Commons' Comma – Response Matrix.xlsx` | The scenario the game is built from: settings, story text, witnesses, questions, every answer, clues, red herrings, follow-ups, endings and the final-answer options. |
| `scenario/The Commons' Comma – Scenario Packet.docx` | The designer's scenario packet: the same scenario written up for people, plus the timeline, the positions and the hidden payoff. Spoilers throughout. |
| `source/story.twee` | The generated Twee source that `index.html` is compiled from. You can import it into Twine to inspect the passages. |

## Rebuild after editing the scenario

Edit the Response Matrix and make the same change in the packet, then rebuild.

Requirements: Python 3.8+ with `openpyxl` and `python-docx` (`pip3 install openpyxl python-docx`), and [Tweego](https://www.motoslave.net/tweego/) 2.1+ (it ships with SugarCube 2). Put `tweego` on your PATH, or set `TWEEGO=/path/to/tweego`.

From the repository root:

```
python3 engine/build_twine.py "scenario/The Commons' Comma – Response Matrix.xlsx" --assets assets --out .
```

The build stops if the matrix breaks a rule or disagrees with itself, or if the packet disagrees with the matrix, and it lists each problem. Open `index.html` to test, then commit.

## Make a new scenario

Copy the Response Matrix and the packet, replace the content while keeping the same sheets and columns, put a new `IFID` (any UUID, uppercase) on the Settings sheet, add the new portraits and map to an assets folder, and build into a new folder or repository. You don't need to change the engine.

## Credits

Game design: Tomer Perry. The HEAR framework is from Yeomans, Minson, Collins, Chen and Gino, "Conversational receptiveness: Improving engagement with opposing views", *Organizational Behavior and Human Decision Processes* 160 (2020). All characters and events are fictional.
