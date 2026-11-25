#!/usr/bin/env python3
"""The 3AM Fridge Text — writes the fridge's one-line 3am text to /output/entry.txt.

Stdlib only, no network, deterministic: the same bytes every run.
"""

import os

LINE = "3am. I hum all night so you can sleep, and here you are foraging like a raccoon, lit only by me. Go to bed."


def main() -> None:
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
