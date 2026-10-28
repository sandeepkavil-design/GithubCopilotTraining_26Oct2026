# US-002 Driver Input Validation

| Field | Value |
|---|---|
| Epic | E1 Driver Input and Modes |
| Size | S |
| Requirements | PR-006 |
| PRD verification | Fault injection |

## Story
As the control software, I want invalid, contradictory, noisy, or unavailable driver inputs detected and safely handled so that they never cause undefined wiper behavior.

## Size rationale (S)
Rule-based validation of one input set; output is a validity flag plus a defined safe value.

## Scope
- In: detection of invalid encodings, contradictory combinations, out-of-range dial values, missing input; safe-value substitution; validity status output.
- Out: fault recording (US-031), fallback state transitions (US-032).

## Acceptance criteria
- Given an undefined switch encoding, when evaluated, then input is flagged invalid and a defined safe value is output.
- Given contradictory inputs (combination rule from the input specification), then input is flagged invalid.
- Given an unavailable input (e.g. open circuit), then input is flagged unavailable.
- Given a dial value out of its configured range, then the value is rejected or clamped per the documented rule.
- Validity flag is exposed for later fault recording.

## Independent test approach
Feed US-001 output interface with stubbed filtered values covering each invalid class; assert flag and safe value.

## Dependencies
- **Depends on (stories):** US-001 (interface only; stub-able)
- **Blocks:** US-003, US-006
- **Open decisions:** Q6
- **External inputs:** input-encoding specification, definition of "contradictory" for the chosen controls

## Requirement-analysis points
- "Safely handle" is undefined: which safe value (OFF, last valid, intermittent)?
- Does this story report faults or only flag validity? Assumed flag only (recording in US-031).
