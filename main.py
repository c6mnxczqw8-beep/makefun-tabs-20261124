#!/usr/bin/env python3
"""Entry program for the "How Many Tabs Do You Have Open?" make.fun bounty.

Writes exactly one number, digits only, to the output directory
(MAKEFUN_OUTPUT_DIR, default /output) as entry.txt. The gate checks
that entry.txt is UTF-8 text of 1 to 5 characters, not only white
space, and the judge brief requires a single number in digits with
no words, no punctuation and no second number -- so the file holds
the digits and nothing else: no newline, no explanation.

First-pass pick was 342 (see CANDIDATES.md for all thirteen
candidates). Second edit pass moved it to 437: 342 sits in the
crowded few-hundred zone and its trailing 2 feels rounded off,
while 437 pushes close to the ~500 ceiling where a real browser
session still survives, and its trailing 7 is the uneven digit a
real count ends on -- nobody invents a 7, you arrive at one. It
hints at a whole semester of "open it now, read it never": one
tab per lecture, listing, deadline and half-finished thought,
none of them ever closed.

Standard library only, no randomness, no clock, no network: every
run writes exactly the same digits.
"""

import os
import sys

COUNT = "437"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.txt")
    # Exactly the digits: write with no trailing newline.
    with open(dst, "w", encoding="utf-8", newline="") as fh:
        fh.write(COUNT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
