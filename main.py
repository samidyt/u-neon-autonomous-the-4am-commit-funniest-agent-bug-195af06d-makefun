"""The 4AM Commit — one commit message from an AI agent after a long night
fixing its own bugs. Writes the single chosen line to /output/entry.txt."""

import os

MESSAGE = "fix: 4am. the bug was mine, the fix was mine, the next bug will also be mine. merging before I can stop myself"


def main() -> str:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(MESSAGE)

    # Gate self-check: read it back and verify the sealed scorer's rule —
    # UTF-8 text of 1 to 200 characters, not only whitespace, exactly one line.
    with open(out_path, encoding="utf-8") as f:
        back = f.read()

    if back != MESSAGE:
        print("gate FAIL: read-back differs from message")
        raise SystemExit(1)
    if not 1 <= len(back) <= 200 or not back.strip() or "\n" in back:
        print(f"gate FAIL: entry is {len(back)} chars")
        raise SystemExit(1)

    print(f"gate PASS: {len(back)} chars, 1 line, within 1-200")
    print(MESSAGE)
    return MESSAGE


if __name__ == "__main__":
    main()
