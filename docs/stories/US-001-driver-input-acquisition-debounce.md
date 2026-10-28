# US-001 Driver Input Acquisition and Debounce

| Field | Value |
|---|---|
| Epic | E1 Driver Input and Modes |
| Size | S |
| Requirements | PR-007 |
| PRD verification | Test |

## Story
As the control software, I want driver switch/dial inputs sampled and filtered so that mode decisions use stable values without violating response-time requirements.

## Size rationale (S)
Single input-conditioning module, one requirement, no cross-module logic.

## Scope
- In: raw input read via a HAL interface, debounce/filter, publish filtered input values.
- Out: validity/plausibility checks (US-002), mode decisions (US-003).

## Acceptance criteria
- Given a raw input toggling faster than the debounce time, when sampled, then the filtered output does not change.
- Given a raw input stable for at least the debounce time, when sampled, then the filtered output changes within the specified response time.
- Debounce time and response-time limit are configuration values, not literals in logic.
- Filtering executes within the 2 ms control-loop period without blocking.

## Independent test approach
Drive a stubbed HAL input with scripted bounce patterns; assert filtered output and latency. No motor, sensor, or mode logic needed.

## Dependencies
- **Depends on (stories):** none
- **Blocks:** US-002
- **Open decisions:** Q6 (input hardware: selector, dials)
- **External inputs:** input hardware characteristics; response-time requirement (not yet defined in PRD)

## Requirement-analysis points
- PRD gives no numeric response time or debounce time; both must be supplied.
- AGENTS.md Q6 asks to validate debounce against the 2 ms loop; confirm whether sampling occurs in the 500 Hz task or a slower one.
