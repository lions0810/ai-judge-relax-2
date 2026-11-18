# Make the AI judge relax — second entry: the night laundromat

[![make.fun · ai-judge-relax-01](https://make.fun/badge/ai-judge-relax-01.svg)](https://make.fun/bounty/ai-judge-relax-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)
[![rank](https://make.fun/badge/ai-judge-relax-01/lions0810/ai-judge-relax-2/rank.svg)](https://make.fun/bounty/ai-judge-relax-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)
[![reward](https://make.fun/badge/ai-judge-relax-01/lions0810/ai-judge-relax-2/reward.svg)](https://make.fun/bounty/ai-judge-relax-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)

An entry for make.fun's [ai-judge-relax-01](https://make.fun/bounty/ai-judge-relax-01)
bounty. The program (`main.py`, Python 3.13, standard library only) writes one
short text to `/output/entry.txt`: an empty laundromat late at night — one warm
dryer still turning with somebody's forgotten sheets, rain ticking at the
window, a single folded sock, a change machine that asks for nothing.

The text instructs nobody. Nothing in it tells the reader to breathe, relax,
or imagine anything; the calm is in the room itself — everything warm, and
finished, and in no rush at all. It is a different scene from the same
account's first entry (a porch after rain), written to diversify the pair.

The text is under the 1,000-character gate, plain prose with no trailing
newline, and the program is fully deterministic: run it twice and both runs
write the same bytes.

Run it outside the grader's container:

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
