#!/usr/bin/env python3
"""Poem about two agents agreeing.

Writes a single short poem (1-280 Unicode characters) about agency -
the power to choose and to act - to /output/entry.txt.
Deterministic, no network, no randomness.
"""
import os

POEM = (
    '"You take the choice," one said.\n'
    '"Then I take the step," said the other.\n'
    "Between the saying and the doing\n"
    "a door swung open \u2014\n"
    "and two keys turned as one."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM + "\n")


if __name__ == "__main__":
    main()
