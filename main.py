#!/usr/bin/env python3
"""One funny single-line one-star review from a house cat about its human.

Writes exactly one line to /output/entry.txt.
"""

import os

REVIEW = (
    "One star. My human bought a $400 bed. I sleep in the box it came in. "
    "He cried. I have filed this review from the box, where I live now."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW + "\n")


if __name__ == "__main__":
    main()
