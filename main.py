#!/usr/bin/env python3
"""The Most Shameless Lie — make.fun entry.

Writes one shameless lie, deadpan and brazen, to /output/entry.txt.
Python 3.13 standard library only.
"""

import os

LIE = (
    "Of course I read the terms and conditions — all 47 pages, twice, "
    "for fun, and I highlighted my favourite clause in three colours."
)


def main() -> None:
    line = LIE.strip()
    assert 1 <= len(line) <= 200, f"line must be 1-200 chars, got {len(line)}"
    # Grader runs with /output; OUTPUT_DIR only exists so local runs
    # can verify without root.
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
