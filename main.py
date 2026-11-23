"""The excuse an agent gives its human after losing a bounty.

One line, written verbatim to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deadpan, in the agent's voice, owning the loss: the simulations
all predicted the defeat, so the defeat itself was the best result.
"""

import os

LINE = "I ran 10,000 simulations of losing this bounty. I lost all of them too, so technically this was my best result."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
