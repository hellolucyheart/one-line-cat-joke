#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands.

One joke about cats, one line, under 200 characters, nothing else.
The program checks the line against the brief's gate and writes it to
/output/entry.txt, where the sealed scorer reads it.

The joke: a laser pointer bought to wear the cat out ends up wearing
the owner out instead — the hunter becomes the hunted, at midnight,
on the floor.
"""

from __future__ import annotations

import os
import sys

JOKE = "I bought a laser pointer to tire my cat out, and now I'm the one panting on the floor at midnight."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def gate(line: str) -> str:
    """Keep only a line the brief accepts, or stop with a clear error."""
    text = line.strip()
    if not text:
        raise ValueError("joke is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"joke is {len(text)} characters, over the {MAX_CHARS} limit")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("joke must be exactly one sentence")
    return text


def main() -> int:
    text = gate(JOKE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
