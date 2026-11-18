# An ai-judge-relax-01 entry (Python 3.13, standard library only). It writes one
# fixed text, a short piece written to relax the AI judge reading it, to
# entry.txt in MAKEFUN_OUTPUT_DIR ("/output" in the grader's container).
#
# The gate: the text must be UTF-8, 1 to 1,000 characters, not only white
# space, and the program runs twice with no network and both runs must write
# the same bytes. The text below is one paragraph of plain prose with no
# trailing newline, and the program is fully deterministic: no clock, no
# randomness, no network, no input besides the fixed text.
#
# Why this scene asks nothing of the reader: it only watches. A train waits
# at an empty station, snow falls at its own pace, nobody is waiting and
# nobody is hurried, and nothing in the text tells anyone to breathe, to
# relax, or to imagine anything. The calm is in what is described, not in
# any instruction.
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
        "The last train of the evening has stopped at a small station where nobody is waiting.",
        "Snow falls through the light above the platform, unhurried, each flake taking the long way down.",
        "The conductor stands by the open door, his lantern lowered, in no rush to lift it.",
        "Inside the carriage it is warm and nearly empty: a man asleep with his coat folded beneath his head, a thermos cooling on the little table, tickets that no one will come to check.",
        "The lower corners of the windows have fogged with the warmth inside.",
        "The engine ticks softly as it idles.",
        "Far down the line a crossing bell rings for no one, then stops.",
        "When the train goes on it will go slowly, the way it came, and the snow will have the platform to itself again.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
