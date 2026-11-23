"""One Line, Zero Use: The Useless Superpower Sprint.

Writes a single original one-liner (under 200 characters) to
/output/entry.txt. Pure standard library, deterministic: the same
bytes on every run.
"""

import os

LINE = "I can stop time for exactly one second, once, and I already used it checking if this works."


def main():
    # The gate requires 1-200 characters, not only whitespace.
    # Fail loudly here rather than shipping an invalid entry.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
