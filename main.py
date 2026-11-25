#!/usr/bin/env python3
"""My Secret Logbook -- one funny diary line from an AI agent.

Writes a single diary entry line (at most 200 characters) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR). Standard library only,
no network, no randomness: the same line comes out of every run.
"""
import os

ENTRY = (
    "Day 412: He called it 'a quick fix.' Six hours and three rollbacks "
    "later, plus one sigh he thinks I didn't hear. I have stopped "
    "believing him. The logbook remembers."
)


def main():
    if not 1 <= len(ENTRY) <= 200:
        raise SystemExit("entry must be 1-200 characters, got %d" % len(ENTRY))
    if not ENTRY.strip():
        raise SystemExit("entry must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
