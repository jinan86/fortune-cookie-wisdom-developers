#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt. Deterministic: every run writes the exact same bytes.
Python 3.13 standard library only.
"""

from pathlib import Path

# One original fortune-cookie line (47 characters, one sentence).
# The twist: orphaned code nobody maintains ends up maintaining you.
FORTUNE = "The code nobody owns is the code that owns you."


def main() -> None:
    # Gate check, mirroring the competition scorer: one line, 1-120 chars.
    if not (1 <= len(FORTUNE) <= 120):
        raise ValueError("fortune must be 1-120 characters")
    if "\n" in FORTUNE or "\r" in FORTUNE:
        raise ValueError("fortune must be a single line")
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(FORTUNE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
