"""Everyday Things, Two Lines, Longer Run — make.fun entry.

The program writes exactly two lines of text to /output/entry.txt:
line 1 explains rain to a 10-year-old through one concrete analogy,
line 2 says honestly what that analogy maps and what it leaves out.

Deterministic: the text is fixed, there is no randomness, no clock,
no network and no input. Two runs produce byte-identical output.
(Bundle guard, added in the bundle session: entry re-verified
deterministic here — two runs byte-identical, 241 chars, 2 lines.)
"""

import os
import sys

ENTRY_TEXT = (
    "Rain is the sky wringing out a giant sponge over your head.\n"
    "The sponge shows how clouds hold water and squeeze it out as drops, "
    "but it leaves out that no hand is doing the squeezing \u2014 the drops "
    "fall because they grow too heavy to stay up.\n"
)


def main() -> int:
    # Self-check the sealed gate before writing: UTF-8 text, 1-400
    # characters, not only whitespace, exactly two non-blank lines.
    text = ENTRY_TEXT
    lines = [line for line in text.splitlines() if line.strip()]
    if not 1 <= len(text) <= 400:
        raise SystemExit(f"entry is {len(text)} chars, gate needs 1-400")
    if len(lines) != 2:
        raise SystemExit(f"entry has {len(lines)} lines, gate needs 2")
    if text != text.strip() + "\n":
        raise SystemExit("entry must end with a single trailing newline")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
