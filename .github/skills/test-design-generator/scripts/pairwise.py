#!/usr/bin/env python3
"""Generate a pairwise (all-pairs) covering set and print it as a Markdown table.

Usage:
  python pairwise.py params.json
  python pairwise.py --param "Motor=S,M,L" --param "Mode=OFF,INT,AUTO,ON"

params.json:
  {"parameters": {"Motor": ["S","M","L"], "Mode": ["OFF","INT"]},
   "exclude": [{"Motor": "S", "Mode": "INT"}]}   # optional forbidden combinations

Greedy algorithm; result is small but not guaranteed minimal.
"""
import argparse
import itertools
import json
import sys


def load(args):
    if args.file:
        with open(args.file, encoding="utf-8") as fh:
            data = json.load(fh)
        return data["parameters"], data.get("exclude", [])
    params = {}
    for item in args.param or []:
        name, _, values = item.partition("=")
        params[name.strip()] = [v.strip() for v in values.split(",") if v.strip()]
    return params, []


def forbidden(case, exclude):
    return any(all(case.get(k) == v for k, v in rule.items()) for rule in exclude)


def all_pairs(names, params, exclude):
    pairs = set()
    for a, b in itertools.combinations(names, 2):
        for va in params[a]:
            for vb in params[b]:
                if not forbidden({a: va, b: vb}, exclude):
                    pairs.add(((a, va), (b, vb)))
    return pairs


def case_pairs(case, names):
    return {((a, case[a]), (b, case[b])) for a, b in itertools.combinations(names, 2)}


def generate(params, exclude):
    names = list(params)
    uncovered = all_pairs(names, params, exclude)
    total_pairs = len(uncovered)
    suite = []
    while uncovered:
        seed = sorted(uncovered)[0]  # sorted for deterministic output
        case = {seed[0][0]: seed[0][1], seed[1][0]: seed[1][1]}
        for name in names:
            if name in case:
                continue
            best, best_gain = None, -1
            for value in params[name]:
                trial = dict(case, **{name: value})
                if forbidden(trial, exclude):
                    continue
                gain = sum(
                    1
                    for other, ov in case.items()
                    if tuple(sorted(((name, value), (other, ov)), key=lambda x: names.index(x[0]))) in uncovered
                )
                if gain > best_gain:
                    best, best_gain = value, gain
            if best is None:
                break
            case[name] = best
        if len(case) < len(names) or forbidden(case, exclude):
            uncovered.discard(seed)  # pair cannot be completed under constraints
            continue
        suite.append(case)
        uncovered -= case_pairs(case, names)
    return names, suite, total_pairs


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", nargs="?", help="JSON file with parameters")
    ap.add_argument("--param", action="append", help='"Name=v1,v2,v3" (repeatable)')
    ap.add_argument("--prefix", default="PW", help="test id prefix (default PW)")
    args = ap.parse_args()

    params, exclude = load(args)
    if len(params) < 2:
        sys.exit("error: at least two parameters with values are required")
    if any(not v for v in params.values()):
        sys.exit("error: every parameter needs at least one value")

    names, suite, total_pairs = generate(params, exclude)
    full = 1
    for v in params.values():
        full *= len(v)

    print("| ID | " + " | ".join(names) + " |")
    print("|---|" + "---|" * len(names))
    for i, case in enumerate(suite, 1):
        print(f"| {args.prefix}-{i:03d} | " + " | ".join(case[n] for n in names) + " |")
    print()
    print(f"Full combinations: {full}; pairwise set: {len(suite)}; value pairs covered: {total_pairs}.")


if __name__ == "__main__":
    main()
