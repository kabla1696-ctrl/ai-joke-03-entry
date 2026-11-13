"""Write one joke about AI coding agents to the output file.

The joke is a fixed string, so the program is deterministic:
two runs write the same bytes. It stays well under the
280-character gate for the joke.
"""

import os

JOKE = "My AI agent finished the feature in four minutes. I've spent three hours explaining to it what 'done' means."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
