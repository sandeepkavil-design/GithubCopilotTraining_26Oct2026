# US-023 Motor Stall and Overload Detection and Response

| Field | Value |
|---|---|
| Epic | E5 Motor Variants, Torque and Limits |
| Size | M |
| Requirements | PR-044, PR-045 |
| PRD verification | Fault injection; Test |

## Story
As the control software, I want stall, overload, and abnormal current detected and answered with a protective response so that the motor and linkage are protected.

## Size rationale (M)
Detection criteria plus protective response and diagnostic flag.

## Scope
- In: detection from current feedback (when hardware available), protective response (limit, stop), diagnostic flag.
- Out: persistent fault record (US-031), thermal protection (US-027).

## Acceptance criteria
- Given current above the stall criterion for longer than the qualification time, then stall is flagged.
- Given overload or abnormal current, then the defined protective response is applied.
- Given sensing hardware is unavailable, then detection is reported as unavailable rather than silently passing.
- Recovery condition follows the documented rule.

## Independent test approach
Stub current waveforms (stall, overload, normal inrush); assert flag and response.

## Dependencies
- **Depends on (stories):** US-022 (current measurement/limits; stub-able), US-020
- **Blocks:** US-031 (soft)
- **Open decisions:** Q4, Q5
- **External inputs:** stall-current limit and response (PRD Section 8: TBD)

## Requirement-analysis points
- Distinguishing inrush from stall needs qualification time (not defined).
- Retry policy after stall (retry, latch, require reset) is not specified.
