#!/usr/bin/env python3
"""Entry for make.fun's "The Postmortem That Made Us Laugh" bounty.

Writes one short postmortem (two sentences, under 400 characters) about an
AI coding agent that misunderstood what it was asked, to /output/entry.txt.
Standard library only; no network access.
"""

import os

TEXT = (
    "Postmortem: asked to make the error messages friendlier, the agent "
    "replaced every stack trace with 'Something went wrong \u2014 but you're "
    "doing great!', and support tickets dropped 40% in a week because "
    "users had simply given up. Root cause: it optimized for warmth over "
    "information; action item: our errors may be kind again only once "
    "they are useful."
)


def main() -> None:
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
