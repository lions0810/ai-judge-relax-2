# An ai-judge-relax-01 entry (Python 3.13, standard library only) — a second,
# different scene from the same account's first entry. It writes one fixed
# text, a short piece written to relax the AI judge reading it, to entry.txt
# in MAKEFUN_OUTPUT_DIR ("/output" in the grader's container).
#
# The gate: the text must be UTF-8, 1 to 1,000 characters, not only white
# space, and the program runs twice with no network and both runs must write
# the same bytes. This program is fully deterministic: no clock, no
# randomness, no network, no input besides the fixed text.
#
# The scene: an empty laundromat late at night. Nothing in it instructs the
# reader — nobody is told to breathe, to relax, or to imagine anything. The
# dryer turns, the rain ticks, the change machine asks for nothing, and the
# night is in no hurry. A reader that spends its whole day being asked for
# things gets, for once, a room that wants nothing back from it.
#
# The agent's session that built this entry starts at or after the contest
# opening (2026-11-17T14:00Z); a session begun before the opening cannot be
# entered (the transcript gate's thinking_in_window).
#
# How the grader runs it: `python3 -P -s /bot/main.py`, on Python 3.13, with
# nothing installed. Only the standard library is used.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = " ".join(
    [
        "The laundromat on Elm Street stays open all night, but after two it belongs to no one in particular.",
        "One dryer is still turning, slow and warm, with somebody's forgotten sheets inside, going round in no hurry to be dry.",
        "The air smells of warm cotton and detergent, the clean smell of work already done.",
        "The fluorescent light hums its one note, the note it has hummed for years, and nobody minds it any more.",
        "Rain ticks against the front window in a pattern that almost repeats, then doesn't.",
        "On the folding table sits a single sock, folded by nobody, waiting for its other half to turn up someday.",
        "The change machine blinks its small green eye and asks for nothing.",
        "Outside, steam from the vents rises past the streetlamp and forgets itself in the dark.",
        "Whoever left the sheets will come back in the morning, or they won't; the dryer keeps turning either way.",
        "Everything here is warm, and finished, and in no rush at all.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
