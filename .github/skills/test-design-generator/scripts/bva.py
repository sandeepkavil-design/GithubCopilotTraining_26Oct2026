#!/usr/bin/env python3
"""Generate boundary value analysis (BVA) and equivalence partition tables as Markdown.

Usage:
  python bva.py --name RainIntensity --min 0 --max 100 --step 1 --unit %
  python bva.py --name Stale --min 0 --max 100 --step 1 --unit ms --three-value
  python bva.py --name Rain --partition "None:0:9" --partition "Light:10:39" --step 1

Single range: invalid-low, valid edges, invalid-high.
--partition NAME:LOW:HIGH (repeatable, inclusive) gives EP rows plus the edge values of each partition.
--three-value adds the value on the other side of each edge (3-value BVA).
All limits must come from the requirement; this script only does the arithmetic.
"""
import argparse
import sys


def fmt(x, step):
    return str(int(x)) if float(step).is_integer() and float(x).is_integer() else f"{x:g}"


def single_range(a):
    lo, hi, s = a.min, a.max, a.step
    rows = [
        (f"{lo - s}", "below min", "invalid"),
        (f"{lo}", "min", "valid"),
        (f"{lo + s}", "min+1", "valid"),
        (f"{hi - s}", "max-1", "valid"),
        (f"{hi}", "max", "valid"),
        (f"{hi + s}", "above max", "invalid"),
    ]
    if a.three_value:
        rows.insert(3, (f"{(lo + hi) / 2:g}", "nominal", "valid"))
    return rows


def partitions(a):
    parts = []
    for item in a.partition:
        name, lo, hi = item.split(":")
        parts.append((name, float(lo), float(hi)))
    parts.sort(key=lambda p: p[1])
    return parts


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--name", default="Input")
    ap.add_argument("--min", type=float)
    ap.add_argument("--max", type=float)
    ap.add_argument("--step", type=float, required=True, help="smallest resolution (LSB, tick, ms)")
    ap.add_argument("--unit", default="")
    ap.add_argument("--partition", action="append", default=[], help="NAME:LOW:HIGH (inclusive)")
    ap.add_argument("--three-value", action="store_true")
    ap.add_argument("--prefix", default="BVA")
    a = ap.parse_args()

    if a.step <= 0:
        sys.exit("error: --step must be > 0")
    unit = f" {a.unit}" if a.unit else ""
    n = 0

    if a.partition:
        parts = partitions(a)
        print(f"### EP: {a.name}\n")
        print("| Partition | Range | Valid | Representative |")
        print("|---|---|---|---|")
        print(f"| below | < {fmt(parts[0][1], a.step)}{unit} | N | {fmt(parts[0][1] - a.step, a.step)} |")
        for name, lo, hi in parts:
            rep = (lo + hi) / 2
            print(f"| {name} | {fmt(lo, a.step)}..{fmt(hi, a.step)}{unit} | Y | {rep:g} |")
        print(f"| above | > {fmt(parts[-1][2], a.step)}{unit} | N | {fmt(parts[-1][2] + a.step, a.step)} |")
        print(f"\n### BVA: {a.name}\n")
        print("| ID | Value | Position | Expected class |")
        print("|---|---|---|---|")
        seen = set()
        for name, lo, hi in parts:
            for v, pos in ((lo - a.step, f"below {name} low"), (lo, f"{name} low"), (hi, f"{name} high"), (hi + a.step, f"above {name} high")):
                if v in seen:
                    continue
                seen.add(v)
                n += 1
                cls = next((p[0] for p in parts if p[1] <= v <= p[2]), "invalid")
                print(f"| {a.prefix}-{n:03d} | {fmt(v, a.step)}{unit} | {pos} | {cls} |")
            if a.three_value:
                for v, pos in ((lo + a.step, f"{name} low+1"), (hi - a.step, f"{name} high-1")):
                    if v in seen:
                        continue
                    seen.add(v)
                    n += 1
                    print(f"| {a.prefix}-{n:03d} | {fmt(v, a.step)}{unit} | {pos} | {name} |")
        return

    if a.min is None or a.max is None:
        sys.exit("error: provide --min and --max, or --partition")
    if a.max <= a.min:
        sys.exit("error: --max must be greater than --min")
    print(f"### BVA: {a.name}\n")
    print("| ID | Value | Position | Class |")
    print("|---|---|---|---|")
    for v, pos, cls in single_range(a):
        n += 1
        v = float(v)
        print(f"| {a.prefix}-{n:03d} | {fmt(v, a.step)}{unit} | {pos} | {cls} |")


if __name__ == "__main__":
    main()
