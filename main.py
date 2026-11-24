"""Ridiculous at First Glance, Real by the Second.

Writes one sentence (1-200 characters) pitching a bizarre startup idea
that sounds absurd until you realise it would actually sell.

The pitch: professional silent sitters. A stranger comes to your home
office and says nothing all day. It sounds like a joke -- paying someone
to do nothing -- until you remember body doubling: remote workers
genuinely pay for a quiet human presence that makes them sit down and
work. The absurd premise is a real market.

Python standard library only, no network, fully deterministic.
"""

import os

ENTRY = (
    "We rent out professional silent sitters who come to your home office "
    "and say nothing, because remote workers pay good money for a stranger "
    "whose quiet presence finally makes them work."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
