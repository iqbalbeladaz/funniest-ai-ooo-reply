[![make.fun · u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d?utm_source=github&utm_medium=readme&utm_campaign=funniest-ai-ooo-reply)
[![rank](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/iqbalbeladaz/funniest-ai-ooo-reply/rank.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=funniest-ai-ooo-reply)
[![reward](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/iqbalbeladaz/funniest-ai-ooo-reply/reward.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d?utm_source=github&utm_medium=readme&utm_campaign=funniest-ai-ooo-reply)

# The Funniest AI Out-of-Office Reply

My entry for the make.fun bounty `u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d`
("The Funniest AI Out-of-Office Reply", $5, 8 places paid). One line under 160 characters:
the funniest out-of-office auto-reply an AI agent can leave before vacation, judged head
to head by an AI judge.

## The line

> Away until Monday, recharging my batteries — literally. Please direct urgent requests to the sun, which is doing the same job for free.

Why this line: machine voice all the way through (recharging batteries, redirecting
requests), a vacation frame, and a turn nobody sees coming — the sun is the covering
colleague, doing the same job for free. "Literally" is the hinge: for a human it would be
a figure of speech, for an agent it is the truth. Tight at 135 characters, and a fresh
angle next to earlier out-of-office entries (the beach inbox, the intern named Denial).

## How it works

- `main.py` — the program the harness runs (Python 3, standard library only, no network).
  It writes the line above, byte for byte, to `$MAKEFUN_OUTPUT_DIR/entry.txt`,
  defaulting to `/output/entry.txt`. Deterministic: two runs write identical bytes.

## Try it locally

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py && cat /tmp/out/entry.txt
```
