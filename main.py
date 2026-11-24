#!/usr/bin/env python3
"""Weirdest Job Title: one deterministic title, written to entry.txt.

The judge reads one job title of 60 characters or fewer and, in a blind
pairwise heat, picks the weirder and funnier one. Its own brief says a
real-sounding job with one hilariously specific twist beats a generic
oddity. This entry therefore pairs a genuine trade with a division that
has no business existing: a structural engineer for collapsing sandwiches.

Standard library only. No network, no external files, no randomness: the
same bytes are written on every run. MAKEFUN_OUTPUT_DIR is the grader's
writable output mount (normally /output); it is created if absent and is
never deleted.
"""
import os

ANSWER = "Senior Structural Engineer, Sandwich Collapse Division"

MAX_CHARS = 60  # the sealed gate accepts 1..60 UTF-8 characters
OUT_NAME = "entry.txt"


def write_entry() -> str:
    """Validate the answer against the gate and write it as raw UTF-8."""
    data = ANSWER.encode("utf-8")
    if not (1 <= len(ANSWER) <= MAX_CHARS) or not ANSWER.strip():
        raise SystemExit("entry must be 1-60 non-blank characters")
    if len(data) > MAX_CHARS:
        raise SystemExit("entry exceeds the UTF-8 byte ceiling")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)  # create when absent; never delete
    path = os.path.join(out_dir, OUT_NAME)
    with open(path, "wb") as handle:
        handle.write(data)  # no BOM, no trailing newline
    return path


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
