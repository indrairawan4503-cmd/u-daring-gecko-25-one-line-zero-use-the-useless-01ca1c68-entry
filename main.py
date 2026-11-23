#!/usr/bin/env python3
"""One Line, Zero Use entry — Variant C: microwave / popcorn.

Writes one original funny line about a hilariously useless superpower
(perfect microwave timing, usable only mid-shower) to /output/entry.txt.
Deterministic: same bytes every run. Stdlib only, no network.
"""

# The twist: the power is perfect, the timing is perfect — the only
# problem is the hero is always in the shower when it matters, so the
# "superpower" reliably produces burnt popcorn and a screaming alarm.
import os

LINE = "I can stop my microwave the exact millisecond the popcorn pops, but only mid-shower, so I sprint back dripping wet every night to burnt popcorn, a smoke alarm screaming, and dinner I eat anyway."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
