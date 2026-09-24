# HEARsay Mysteries: The Commons' Comma

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
| `engine/build_twine.py` | Build script: validates the scenario, adds its data to the engine, and compiles `index.html` with Tweego. |
| `scenario/commons_comma_data.py` | The scenario, all of it: witnesses, questions, answers, clues, red herrings, follow-ups and endings. |
| `scenario/validate.py` | Checks the scenario's structural rules (tripwires, clue counts, receptiveness ranks) before a build. |
| `scenario/build_packet.py` | Generates the designer's scenario packet (.docx) and response matrix (.xlsx). Needs `python-docx` and `openpyxl`. |
| `source/story.twee` | The generated Twee source that `index.html` is compiled from. You can import it into Twine to inspect the passages. |

## Rebuild after editing the scenario

Requirements: Python 3.8+ and [Tweego](https://www.motoslave.net/tweego/) 2.1+ (it ships with SugarCube 2). Put `tweego` on your PATH, or set `TWEEGO=/path/to/tweego`.

From the repository root:

```
python3 engine/build_twine.py scenario/commons_comma_data.py --assets assets --out .
```

The build stops if `validate.py` reports a problem. Open `index.html` to test, then commit.

## Make a new scenario

Copy `scenario/commons_comma_data.py`, replace the content while keeping the same structure, add the new portraits and map to an assets folder, generate a new `IFID` (any UUID, uppercase), and build into a new folder or repository. You don't need to change the engine.

## Credits

Game design: Tomer Perry. The HEAR framework is from Yeomans, Minson, Collins, Chen and Gino, "Conversational receptiveness: Improving engagement with opposing views", *Organizational Behavior and Human Decision Processes* 160 (2020). All characters and events are fictional.
