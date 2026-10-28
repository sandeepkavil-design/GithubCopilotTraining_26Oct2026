# US-028 Thermal Protection Recovery

| Field | Value |
|---|---|
| Epic | E6 Thermal Management and Duty Cycle |
| Size | S |
| Requirements | PR-056 |
| PRD verification | Test |

## Story
As a driver, I want normal operation restored only when approved recovery conditions are met so that the motor is not damaged by premature restart.

## Size rationale (S)
One state transition with defined conditions.

## Scope
- In: recovery condition evaluation, exit from derating/shutdown, driver notification of recovery.
- Out: thresholds and protection entry (US-027).

## Acceptance criteria
- Given protection is active and recovery conditions are not met, then protection remains.
- Given all recovery conditions are met, then normal operation resumes per the documented behavior.
- Recovery cannot occur through a mere power cycle unless the policy allows it.

## Independent test approach
Stub protection state and temperature decay; assert state transitions.

## Dependencies
- **Depends on (stories):** US-027
- **Blocks:** none
- **Open decisions:** Q8
- **External inputs:** approved recovery conditions (hysteresis, time)

## Requirement-analysis points
- AGENTS.md Q8: "power-cycle or service reset" contradicts a temperature-based recovery; confirm.
