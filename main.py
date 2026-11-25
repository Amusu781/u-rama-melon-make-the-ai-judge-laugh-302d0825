"""Make the AI Judge Laugh — one office-life joke, one line, under 200 chars.

Writes the joke to /output/entry.txt (or $OUTPUT_DIR/entry.txt when set).
Python standard library only; no network access. The file holds exactly
the joke, with no trailing newline, so its byte count equals the joke's
character count and it stays a single line.
"""

import os
import shutil

JOKE = (
    "Our boss banned working from home because collaboration matters, "
    "then spent the whole day on video calls with people three desks away."
)

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def main():
    # Create the output directory first, before any file is written.
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Clear only the directory's contents, never the directory itself.
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)

    entry_path = os.path.join(OUTPUT_DIR, "entry.txt")

    # Gate self-check: 1 to 200 characters, single line, not only whitespace.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert "\n" not in JOKE, "joke must be a single line"
    assert JOKE.strip(), "joke must not be only whitespace"

    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
