# US-017 Resource Budgets and MCU Hosting

| Field | Value |
|---|---|
| Epic | E4 Embedded Application and Memory |
| Size | M |
| Requirements | PR-030, PR-031 |
| PRD verification | Integration test; Static analysis / Review |

## Story
As an engineer, I want RAM, flash, and stack budgets defined and checked so that the wiper software is shown to fit and run on the MCU.

## Size rationale (M)
Budget definition plus build-time checks (map/stack analysis); no functional logic.

## Scope
- In: budget table (code, stack, heap if used, calibration, diagnostics, persistent settings), build-time size/stack report, pass/fail check against budget, on-target hosting of the control software.
- Out: runtime exhaustion handling (US-019).

## Acceptance criteria
- A budget exists for each PR-031 category with a stated limit.
- Build output reports usage per category and fails the quality gate when a limit is exceeded.
- Heap use, if any, is justified; otherwise heap is zero.
- Software builds and runs on the target (or approved evaluation board).

## Independent test approach
Static analysis of linker map and stack usage tool output against the budget file.

## Dependencies
- **Depends on (stories):** none
- **Blocks:** US-016 (soft), US-019
- **Open decisions:** Q9
- **External inputs:** MCU memory sizes (depends on selection)

## Requirement-analysis points
- Budget numbers cannot be set until an MCU is chosen (US-016); define the format now and fill later.
