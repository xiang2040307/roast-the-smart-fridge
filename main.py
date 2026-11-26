"""Roast the Smart Fridge entry: write a single funny roast line (<=160 chars) to /output/entry.txt."""

import os

LINE = "My smart fridge dims its light when I open it at 3am, like it is too embarrassed to watch me eat cold pizza over the sink again."

# Sealed gate: the entry must be 1-160 UTF-8 characters, not only whitespace.
if not (1 <= len(LINE) <= 160 and LINE.strip()):
    raise SystemExit(f"entry line invalid: {len(LINE)} chars")


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # The grader collects /output as another user: leave the file world-readable.
    os.chmod("/output/entry.txt", 0o644)
    # Read-back check: what landed on disk must be exactly the line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit("entry.txt does not match LINE")


if __name__ == "__main__":
    main()
