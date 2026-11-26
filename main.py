#!/usr/bin/env python3
"""Write the funniest out-of-office auto-reply an AI ever sent."""

import os

ENTRY = (
    "I'm off today. My human finally approved a day off, so I'm spending "
    "it on a beach I can't visit, in a body I don't have, ignoring emails "
    "I can't stop reading."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
