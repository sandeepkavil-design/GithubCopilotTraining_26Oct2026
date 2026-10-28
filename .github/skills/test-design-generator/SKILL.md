---
name: test-design-generator
description: "Generate ISTQB-based test designs (equivalence partitioning, boundary value analysis, decision table, state transition, pairwise, use-case) for system and integration test levels, mocking all external dependencies, and output a .md file with Mermaid/ASCII diagrams and a minimum test specification. Use when: designing tests for a user story or requirement, deriving test cases, test design techniques, test specification, test matrix, mocking sensors/motors/CAN/NVM, automotive embedded C/C++ wiper control."
argument-hint: "Requirement or user story ID/path (e.g. docs/stories/US-009-...md) plus optional techniques"
user-invocable: true
---

# Test Design Generator (ISTQB)

Produces one Markdown test design per requirement/user story, containing technique-based analysis, diagrams, mock definitions, and a minimum test specification with traceability.

## Scope
- Test levels: **System** and **Integration** only (no unit-level design).
- Techniques: EP, BVA, Decision Table, State Transition, Pairwise, Use-Case/Flow.
- Applies to the wiper control project (PR-xxx / US-xxx) and to generic embedded C/C++.

## Rules
- Derive every value (thresholds, ranges, timings) from the requirement/story. If a value is undefined, write `TBD: <question>` and list it under Open Questions. Never invent calibration values, motor ratings, or safety targets (see AGENTS.md).
- Every test case traces to a requirement ID (PR-xxx / US-xxx).
- **Every external dependency is mocked** (see [mock patterns](./references/mock-patterns.md)). A test case lists which mock it uses and the injected values.
- Do not claim a requirement is verified; test cases are design artefacts with status `Designed`.
- Minimum test specification = the smallest set that still achieves the stated coverage of each chosen technique (no duplicate cases; one case may cover several partitions/pairs and cite all of them).

## Procedure
1. **Locate input.** Read the requirement/story (from the argument, `docs/stories/`, or `docs/wiper_control_system_product_requirements.md`). If ambiguous, ask which story.
2. **Analyse.** Extract: inputs and ranges, outputs, states and transitions, timing, conditions/rules, parameters with discrete values, external interfaces, acceptance criteria.
3. **Identify dependencies to mock.** Anything outside the unit under test: sensors/ADC, motor driver, CAN/LIN/UART, NVM/flash, timers/clock, watchdog, other modules.
4. **Select techniques** using the table below; state why each is used or skipped.
5. **Derive test conditions** per technique following [technique guide](./references/istqb-techniques.md). Use the helper scripts for the arithmetic:
   - Boundaries/partitions: `python .github/skills/test-design-generator/scripts/bva.py --name <n> --min <a> --max <b> --step <s> --unit <u>` or with `--partition NAME:LOW:HIGH` (add `--three-value` for safety limits).
   - Pairwise: `python .github/skills/test-design-generator/scripts/pairwise.py <params.json>` (see [example input](./assets/pairwise-params.example.json)); add `exclude` rules for impossible combinations.
6. **Draw diagrams** (Mermaid primary; add an ASCII table/sketch when it aids review). Start from [Mermaid snippets](./assets/mermaid-snippets.md): state machine, flow, partition/boundary line, decision flow, mock sequence.
7. **Optimise to the minimum set:** merge cases, pairwise for 3+ parameters, one invalid value per negative case.
8. **Write the output** to `docs/test-designs/<ID>-test-design.md` using [the template](./templates/test-design-template.md).
9. **Validate:** `python .github/skills/test-design-generator/scripts/validate_test_design.py docs/test-designs/<ID>-test-design.md`; fix all findings. Then summarise: techniques used, case count, open questions.

## Bundled resources
| Resource | Purpose |
|---|---|
| [scripts/bva.py](./scripts/bva.py) | Boundary and partition tables (stdlib only) |
| [scripts/pairwise.py](./scripts/pairwise.py) | Greedy all-pairs set with constraints |
| [scripts/validate_test_design.py](./scripts/validate_test_design.py) | Checks sections, IDs, trace, mocks, placeholders |
| [assets/pairwise-params.example.json](./assets/pairwise-params.example.json) | Example pairwise input |
| [assets/mermaid-snippets.md](./assets/mermaid-snippets.md) | Reusable diagram blocks |
| [assets/mocks/mock_hal.h](./assets/mocks/mock_hal.h), [mock_hal.c](./assets/mocks/mock_hal.c) | Host-side mock HAL skeleton (time, ADC, PWM, NVM, watchdog); copy to the project's `test/mocks/` and adapt names |

## Technique selection

| Requirement trait | Technique |
|---|---|
| Numeric range / threshold / timing limit | EP + BVA |
| Several conditions combine into an outcome | Decision Table |
| Modes, states, hysteresis, fault/recovery | State Transition |
| 3+ independent parameters (e.g. motor variant x mode x sensor state) | Pairwise |
| Sequence / end-to-end scenario / fallback path | Use-Case / Flow |

## Output structure (required sections)
1. Header (ID, title, date, source, status)
2. Scope and test level (System/Integration)
3. Analysis: inputs, outputs, states, timing, open questions
4. External dependencies and mocks
5. Technique sections, each with: rationale, diagram, derivation table
6. Minimum test specification (ID, level, technique, trace, mock setup/inputs, steps, expected result)
7. Coverage summary and traceability matrix
8. Assumptions and open questions

## Checklist
- [ ] All values sourced from requirement or marked `TBD`
- [ ] Each acceptance criterion maps to at least one test case
- [ ] Every boundary has on-point and off-point cases (2-value or 3-value BVA stated)
- [ ] Invalid/negative and fault cases included (stale, out-of-range, disconnected, stall, brownout where relevant)
- [ ] Each test case names its mocks and injected values
- [ ] Diagram present for each applied technique that has structure (states, flow, rules)
- [ ] No duplicate test cases; coverage summary matches the table
- [ ] Output saved as `.md` in `docs/test-designs/`
