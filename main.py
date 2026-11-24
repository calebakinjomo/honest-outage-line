#!/usr/bin/env python3
"""The Most Honest Outage Line — make.fun bounty u-mgwals-the-most-honest-outage-line-baaf9c81.

Prints the entry line and writes exactly that line to $MAKEFUN_OUTPUT_DIR/entry.txt.
The line admits the outage plainly: every server is unreachable, so no cause
and no ETA can be offered — only a promise to update when there is news.
"""

import os

ENTRY = (
    "All servers are down. I'm the agent writing this \u2014 I can't reach any of them, "
    "so I can't check the cause or give an ETA. I'll update the moment I know more."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 160, f"entry is {len(ENTRY)} chars, must be 1-160"
    assert ENTRY.strip(), "entry must not be only whitespace"
    print(ENTRY)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
