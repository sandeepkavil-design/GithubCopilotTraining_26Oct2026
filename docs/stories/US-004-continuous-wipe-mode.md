# US-004 Continuous Wipe Mode

| Field | Value |
|---|---|
| Epic | E1 Driver Input and Modes |
| Size | S |
| Requirements | PR-002 |
| PRD verification | Test |

## Story
As a driver, I want a continuous (ON) mode so that the wipers run constantly during heavy rain.

## Size rationale (S)
One mode producing a constant wipe request at a configured speed setting.

## Scope
- In: ON mode request generation at the approved continuous setting.
- Out: motor limit enforcement (US-022), motor output (US-015).

## Acceptance criteria
- Given mode ON, when evaluated, then a continuous wipe request at the configured speed setting is produced every control cycle.
- Given a switch from ON to OFF, then the request stops per US-003/US-006 behavior.
- Requested speed setting never exceeds the configured maximum for the selected variant (value check only; enforcement is US-022).

## Independent test approach
Stub mode manager output = ON; assert request content. Stub variant parameters.

## Dependencies
- **Depends on (stories):** US-003
- **Blocks:** US-006 (soft)
- **Open decisions:** Q4 (speed settings), Q6
- **External inputs:** "approved vehicle interface" for ON mode (PR-002); number of continuous speeds

## Requirement-analysis points
- Single or multiple continuous speeds? Not stated in PRD.
