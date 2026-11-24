#!/usr/bin/env python3
"""Dad Joke Showdown entry: one dad joke, written to /output/entry.txt.

The joke is a single sentence, 75 characters, told in a father's voice:
a dog named after a distance, so the daily walk becomes a boast.
No network, no randomness, no clock, no arguments. The same bytes
come out on every run, so the judge always reads the same joke.
"""

import os

JOKE = "I named my dog Five Miles so I can tell people I walk five miles every day."

OUTPUT_PATH = "/output/entry.txt"


def write_joke():
    """Write the joke to the grader's output file, one line, UTF-8."""
    if not 1 <= len(JOKE) <= 200:
        raise ValueError("joke must be 1 to 200 characters")
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(JOKE + "\n")


if __name__ == "__main__":
    write_joke()
