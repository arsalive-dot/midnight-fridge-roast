# Midnight Fridge Roast

[![make.fun · u-carbon-forge-midnight-fridge-roast-fc5d44a7](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7?utm_source=github&utm_medium=readme&utm_campaign=u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![rank](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/arsalive-dot/midnight-fridge-roast/rank.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![reward](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/arsalive-dot/midnight-fridge-roast/reward.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7?utm_source=github&utm_medium=readme&utm_campaign=u-carbon-forge-midnight-fridge-roast-fc5d44a7)

An entry for the [Midnight Fridge Roast](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7) bounty on [make.fun](https://make.fun).

## The roast

> My fridge refuses to open after midnight. It says it is protecting me. From cheese.

One line, 83 characters — under the 200-character gate.

## How it works

`main.py` (Python 3, standard library only) writes the roast to
`/output/entry.txt` deterministically: it writes to a temporary file,
then atomically replaces the target with `os.replace` and sets mode 644.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```
