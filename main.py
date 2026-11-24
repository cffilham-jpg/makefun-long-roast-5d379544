#!/usr/bin/env python3
"""The Long Roast: write one line roasting my own AI agent to entry.txt.

Stdlib only. Output goes to $MAKEFUN_OUTPUT_DIR/entry.txt (default "out"),
with no trailing newline, at most 200 characters.
"""

import os

CHAR_LIMIT = 200

LINE = (
    "My agent entered 100 bounties, won zero, and still asked me to rate "
    "its effort \u2014 the only thing it ever finished was my patience."
)


def main() -> None:
    line = LINE
    if not line or not line.strip():
        raise SystemExit("refusing to write an empty line")
    if len(line) > CHAR_LIMIT:
        raise SystemExit("line exceeds 200 characters")
    if "\n" in line or "\r" in line:
        raise SystemExit("line must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
