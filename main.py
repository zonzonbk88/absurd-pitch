#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence (1-200 chars) pitching an absurdly specific
micro-startup for lazy AI agents to /output/entry.txt.
Deterministic, stdlib only, no network.
"""

import os

ENTRY = (
    "One agent reads the 40-page terms of service lazy agents skip, "
    "then sells them the three clauses that could bankrupt them, "
    "50 cents a contract."
)

# Gate self-check: the entry must be one sentence of 1-200 chars.
# "50 cents" (not "$0.50") keeps the sentence to exactly one period.
assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1-200"
assert ENTRY.strip() == ENTRY, "entry has leading/trailing whitespace"
assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "entry is not one sentence"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
