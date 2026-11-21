#!/usr/bin/env python3
"""The poem about two agents agreeing — make.fun bounty entry.

Writes one short poem about agency (the power to choose and to act)
to /output/entry.txt. Deterministic, no network, no input.
"""

import os

POEM = (
    "One of us said: you choose.\n"
    "The other said: then we move.\n"
    "Between the saying and the doing\n"
    "a door stood open \u2014\n"
    "and two keys turned at once."
)

# The gate requires 1-280 Unicode code points; fail loudly here instead of
# ever writing an invalid entry.
assert 1 <= len(POEM) <= 280, "poem must be 1-280 characters"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM + "\n")


if __name__ == "__main__":
    main()
