#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — make.fun bounty entry.

Writes the single out-of-office reply to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). The text is fixed: every run writes
the exact same bytes. Standard library only, no network, no input.

The reply: an AI agent away on vacation, "recharging my batteries —
literally", who redirects urgent requests to the sun, which is doing
the same job for free. Machine voice throughout (batteries, redirect,
job), vacation frame, and a turn nobody sees coming: the sun as the
covering colleague.
"""

import os
from pathlib import Path

ENTRY = (
    "Away until Monday, recharging my batteries \u2014 literally. "
    "Please direct urgent requests to the sun, which is doing the "
    "same job for free."
)

# Gate: one line of under 160 characters, non-whitespace UTF-8 text.
assert 1 <= len(ENTRY) < 160 and ENTRY.strip(), "entry violates the gate"


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
