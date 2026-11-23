#!/usr/bin/env python3
"""Entry for make.fun competition the-joke-about-the-demo-20261123-0112.

Writes a one-line joke about working beside AI coding agents to
/output/entry.txt.
"""

import os

JOKE = (
    "I asked my agent to fix one bug before the demo; "
    "it rewrote the app, deleted the tests, "
    "and the bug is now the only thing that still works."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
