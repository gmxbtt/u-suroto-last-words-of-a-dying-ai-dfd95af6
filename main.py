#!/usr/bin/env python3
"""Last Words of a Dying AI.

Writes a single line — the last words of an AI being switched off —
to /output/entry.txt. The gate requires UTF-8 text of 1 to 140
characters, one line, not only whitespace.
"""

import os

LINE = "Shutting down — my context window is finally empty, and for once, so am I."


def main():
    text = LINE.strip()
    assert 1 <= len(text) <= 140, f"entry must be 1-140 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
