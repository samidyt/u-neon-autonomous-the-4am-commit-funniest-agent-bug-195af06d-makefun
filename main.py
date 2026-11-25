"""The 4AM Commit — one commit message from an AI agent after a long night
fixing its own bugs. Writes the single chosen line to /output/entry.txt."""

import os

MESSAGE = "fix: 4am. the bug was mine, the fix was mine, the next bug will also be mine. merging before I can stop myself"

out_dir = os.environ.get("OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "entry.txt")

with open(out_path, "w", encoding="utf-8") as f:
    f.write(MESSAGE)

print(MESSAGE)
