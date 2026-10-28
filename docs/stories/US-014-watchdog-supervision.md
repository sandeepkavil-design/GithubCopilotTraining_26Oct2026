# US-014 Watchdog Supervision and Overrun/Lockup Behavior

| Field | Value |
|---|---|
| Epic | E3 Real-Time Control and MCU |
| Size | M |
| Requirements | PR-026 |
| PRD verification | Fault injection |

## Story
As the control software, I want watchdog supervision with defined behavior on overrun, lockup, or reset so that a hung controller reaches a safe state.

## Size rationale (M)
Watchdog service logic, defined reactions, and fault-injection cases.

## Scope
- In: watchdog servicing tied to healthy control-task execution, defined action on overrun/lockup, reset-cause capture.
- Out: motor output state during reset (US-033), fault storage (US-031).

## Acceptance criteria
- Given healthy execution, then the watchdog is serviced only after the control task completes its checks.
- Given a simulated lockup or overrun, then the watchdog resets the MCU within the configured timeout.
- Given a reset, then the reset cause is captured and made available.
- Watchdog cannot be disabled by application code outside the documented init.

## Independent test approach
Fault injection: stall the task in a test build; observe reset and reset-cause value.

## Dependencies
- **Depends on (stories):** US-011
- **Blocks:** US-031 (reset cause), US-033
- **Open decisions:** Q11 (safety level)
- **External inputs:** MCU watchdog capability, timeout value

## Requirement-analysis points
- Windowed vs simple watchdog and timeout not defined.
- AGENTS.md prohibits disabling watchdogs; debug-build exceptions need a documented rule.
