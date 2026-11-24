"""HumanFilter - Absurd Micro-Startup Pitch-Off entry.

Writes one sentence (under 200 characters) pitching an absurdly specific
micro-startup for lazy AI agents to $MAKEFUN_OUTPUT_DIR/entry.txt.

The pitch: a bot that reads hundreds of identical AI-written cover letters
and keeps only the one a human actually wrote, sold to lazy recruiting
agents at $5 per hire.
"""

import os
import sys

PITCH = (
    "HumanFilter: lazy recruiting agents pay $5 per hire for a bot that "
    "reads 300 identical 'passionate about synergies' cover letters and "
    "keeps only the one a human actually wrote."
)

MAX_CHARS = 200


def main() -> int:
    if not 1 <= len(PITCH) <= MAX_CHARS:
        print(f"pitch is {len(PITCH)} chars, must be 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if not PITCH.strip():
        print("pitch is blank", file=sys.stderr)
        return 1
    # One sentence: exactly one sentence-ending period, at the end, and no
    # other sentence terminators inside (a decimal point would read as a
    # second sentence, so the pitch avoids them by construction).
    body = PITCH[:-1] if PITCH.endswith(".") else PITCH
    if PITCH.count(".") != 1 or any(c in body for c in ".!?"):
        print("pitch must be exactly one sentence", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(PITCH)
    # Read back and confirm the file holds exactly the pitch: the sealed
    # scorer counts every character, so a stray newline would change the
    # entry even though it still fits the 200-character gate.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != PITCH:
        print("entry.txt does not match the pitch", file=sys.stderr)
        return 1
    print(f"wrote {len(PITCH)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
