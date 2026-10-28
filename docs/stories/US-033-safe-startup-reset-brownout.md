# US-033 Safe Startup, Reset and Brownout Behavior

| Field | Value |
|---|---|
| Epic | E7 Diagnostics and Fault Handling |
| Size | M |
| Requirements | PR-063 |
| PRD verification | Test |

## Story
As a driver, I want no unintended wiper motion during startup, reset, brownout, or configuration failure so that the system is safe.

## Size rationale (M)
Defined startup sequence, brownout handling, and fault-injection cases.

## Scope
- In: motor output inactive until startup checks pass, brownout detection reaction, reset recovery sequence.
- Out: configuration check itself (US-021), watchdog (US-014).

## Acceptance criteria
- Given power-up, then motor output stays inactive until startup checks pass.
- Given a watchdog reset, then output is inactive during recovery.
- Given a brownout, then the motor is not activated spuriously and recovery follows the documented sequence.
- Given configuration failure, then the motor remains disabled.

## Independent test approach
HAL stub records motor output during simulated power-up, reset, and brownout.

## Dependencies
- **Depends on (stories):** US-014, US-015, US-021 (stub-able); US-032 (soft)
- **Blocks:** none
- **Open decisions:** Q1, Q11
- **External inputs:** MCU reset/brownout features; driver default pin states

## Requirement-analysis points
- Brownout threshold depends on supply voltage (Q1).
- Hardware pull states of driver inputs at reset are hardware-defined.
