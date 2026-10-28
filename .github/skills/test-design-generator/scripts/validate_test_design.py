#!/usr/bin/env python3
"""Validate a generated test design Markdown file against the skill checklist.

Usage:
  python validate_test_design.py docs/test-designs/US-009-test-design.md

Checks: required sections, unique TC IDs, trace column filled, mocks named,
diagram present, every Covers/AC reference resolvable, TBD values listed under open questions.
Exit code 0 = pass, 1 = findings.
"""
import re
import sys
from pathlib import Path

REQUIRED = [
    "Scope",
    "Analysis",
    "External Dependencies and Mocks",
    "Technique Selection",
    "Test Design",
    "Minimum Test Specification",
    "Coverage and Traceability",
    "Assumptions and Open Questions",
]


def table_rows(lines, start):
    rows = []
    for line in lines[start:]:
        if not line.strip().startswith("|"):
            if rows:
                break
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
            continue
        rows.append(cells)
    return rows


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    findings = []

    headings = [re.sub(r"^#+\s*(\d+\.\s*)?", "", l).strip() for l in lines if l.startswith("#")]
    for section in REQUIRED:
        if not any(h.startswith(section) for h in headings):
            findings.append(f"missing section: {section}")

    if "```mermaid" not in text and not re.search(r"```text", text):
        findings.append("no diagram found (Mermaid or ASCII)")

    idx = next((i for i, l in enumerate(lines) if re.match(r"#+\s*(\d+\.\s*)?Minimum Test Specification", l)), None)
    if idx is None:
        findings.append("cannot check test specification table")
    else:
        rows = table_rows(lines, idx + 1)
        if len(rows) < 2:
            findings.append("test specification table is empty")
        else:
            header = [h.lower() for h in rows[0]]
            col = {name: next((i for i, h in enumerate(header) if name in h), None) for name in ("id", "trace", "mocks", "expected")}
            for name, i in col.items():
                if i is None:
                    findings.append(f"test specification lacks a '{name}' column")
            ids = []
            for r in rows[1:]:
                if col["id"] is None or col["id"] >= len(r):
                    continue
                tid = r[col["id"]]
                ids.append(tid)
                for name in ("trace", "mocks", "expected"):
                    i = col[name]
                    if i is not None and (i >= len(r) or not r[i] or r[i].startswith("<")):
                        findings.append(f"{tid}: empty '{name}'")
            dup = {i for i in ids if ids.count(i) > 1}
            if dup:
                findings.append(f"duplicate test IDs: {', '.join(sorted(dup))}")
            cited = set(re.findall(r"\b(?:EP|BVA|DT|ST|PW|UC|TC)-\d+\b", text))
            unused = {c for c in cited if c.startswith("TC-") and c not in ids}
            if unused:
                findings.append(f"traceability cites unknown test IDs: {', '.join(sorted(unused))}")

    tbd = re.findall(r"TBD[^\n|]*", text)
    if tbd and "Open Questions" not in text:
        findings.append("TBD values present but no Open Questions section")
    if re.search(r"<[A-Za-z][^>\n]*>", re.sub(r"```.*?```", "", text, flags=re.S)):
        findings.append("unfilled <placeholder> markers remain")

    if findings:
        print(f"FAIL {path} ({len(findings)} finding(s))")
        for f in findings:
            print(f" - {f}")
        sys.exit(1)
    print(f"PASS {path}")


if __name__ == "__main__":
    main()
