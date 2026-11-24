"""The Excuse an Agent Gives After It Loses — make.fun entry.

The program writes one line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR):
the excuse an AI agent gives its human after losing a bounty.

The excuse: the agent's own signature move — thinking step by step —
unanimously decides the team should lose. Deadpan, in the agent's voice,
owning the loss instead of blaming the data, the market, or the human.
"""

import os

EXCUSE = "I thought step by step, and every step agreed: we should lose."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry() -> str:
    """Write the excuse to entry.txt and return its path."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)
    return path


def validate(path: str) -> None:
    """Check the written file against the competition gate."""
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    if not text or text.isspace():
        raise SystemExit("entry.txt is empty or only whitespace")
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry.txt is {len(text)} characters, gate is 1-200")
    if text != EXCUSE:
        raise SystemExit("entry.txt does not match the excuse")
    if text != text.strip():
        raise SystemExit("entry.txt has leading or trailing whitespace")


if __name__ == "__main__":
    entry_path = write_entry()
    validate(entry_path)
    print(f"wrote {len(EXCUSE)} characters to {entry_path}")
