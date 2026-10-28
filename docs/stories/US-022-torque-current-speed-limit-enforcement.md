# US-022 Torque, Current and Speed Limit Enforcement

| Field | Value |
|---|---|
| Epic | E5 Motor Variants, Torque and Limits |
| Size | L |
| Requirements | PR-042, PR-043 |
| PRD verification | Test; Test / Analysis |

## Story
As the control software, I want commands limited to the selected motor's approved torque, current, and speed envelope so that the motor is never driven beyond manufacturer limits.

## Size rationale (L)
Safety-relevant limiting using feedback, multiple quantities, and envelope checks.

## Scope
- In: limiting of commanded speed/current/torque against variant parameters, use of available feedback, envelope check on operating point.
- Out: stall/overload detection (US-023), thermal derating (US-027).

## Acceptance criteria
- Given a request above any limit for the active variant, then the output is limited to that limit.
- Given measured current above the limit, then drive is reduced per the documented response.
- Operating point is checked against the manufacturer's envelope, not only individual limits.
- Limits are read from the variant parameters, never hard-coded.

## Independent test approach
Stub variant parameters and current feedback; sweep requests and measurements; assert limited output.

## Dependencies
- **Depends on (stories):** US-015, US-020, US-021 (interfaces; stub-able)
- **Blocks:** US-023
- **Open decisions:** Q1, Q4, Q5
- **External inputs:** motor datasheets; current-sensing hardware

## Requirement-analysis points
- AGENTS.md Q5 assumes current feedback only. Torque must then be estimated from current; the torque constant is not given.
- Limit values depend on supply voltage (Q1).
