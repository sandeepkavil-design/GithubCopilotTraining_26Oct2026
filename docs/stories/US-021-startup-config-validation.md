# US-021 Startup Motor Configuration Validation

| Field | Value |
|---|---|
| Epic | E5 Motor Variants, Torque and Limits |
| Size | S |
| Requirements | PR-046 |
| PRD verification | Fault injection |

## Story
As the control software, I want the motor variant configuration validated at startup so that invalid or unsupported configuration never enables unrestricted operation.

## Size rationale (S)
A single startup check with a defined result.

## Scope
- In: validity checks (variant supported, required fields populated, values in range, integrity OK), result flag, motor-enable permission.
- Out: parameter data (US-020), reaction beyond inhibiting enable (US-032).

## Acceptance criteria
- Given a valid configuration, then motor operation is permitted.
- Given an unsupported variant, missing field, or out-of-range value, then motor enable is denied or restricted per the documented rule.
- Validation runs before the first motor command after each reset.

## Independent test approach
Fixture configs (valid, invalid variant, TBD field, corrupt); assert enable permission.

## Dependencies
- **Depends on (stories):** US-020
- **Blocks:** US-022, US-033
- **Open decisions:** Q4
- **External inputs:** validity rules per parameter

## Requirement-analysis points
- "Restricted" operation: is there a permitted limp mode or is motor disabled entirely?
