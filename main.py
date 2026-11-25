"""Midnight Fridge Roast — one-line roast entry.

The entry is one line roasting a smart fridge that refuses to open
after midnight. It writes the roast to /output/entry.txt deterministically.

Craft: the fridge's own excuse becomes the joke — it claims to protect
me, and the protection is from cheese, so the midnight refusal itself
is the target and the punch lands on the last words.
"""

import os


ENTRY = "My fridge refuses to open after midnight. It says it is protecting me. From cheese."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    tmp_path = os.path.join(out_dir, ".entry.txt.tmp")
    final_path = os.path.join(out_dir, "entry.txt")
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp_path, final_path)
    os.chmod(final_path, 0o644)


if __name__ == "__main__":
    main()
