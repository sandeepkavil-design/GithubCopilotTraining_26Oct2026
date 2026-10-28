# US-005 Intermittent Wipe Mode

| Field | Value |
|---|---|
| Epic | E1 Driver Input and Modes |
| Size | M |
| Requirements | PR-003 |
| PRD verification | Test |

## Story
As a driver, I want an intermittent mode with an adjustable interval so that wipes occur at a pace suited to light rain.

## Size rationale (M)
Needs timing logic, interval range handling, and behavior on interval change mid-cycle.

## Scope
- In: interval timer, interval setting to time conversion, wipe request generation per interval, handling of interval change.
- Out: automatic interval mapping (US-009), motor output (US-015).

## Acceptance criteria
- Given a configured interval T, when intermittent mode is active, then wipe requests occur once per T within the specified tolerance.
- Given the interval dial changes, then the new interval applies per a documented rule (immediately or next cycle).
- Given an interval outside the configured range, then it is clamped or rejected per documented rule.
- Interval timing is derived from the control tick, not blocking delays.

## Independent test approach
Simulated tick counter plus stubbed dial value; assert request timestamps.

## Dependencies
- **Depends on (stories):** US-003; US-011 (timebase, soft, stub-able)
- **Blocks:** US-010 (fallback target)
- **Open decisions:** Q6 (interval range)
- **External inputs:** interval range and timing tolerance (not in PRD)

## Requirement-analysis points
- Interval measured from wipe start or wipe end?
- Does the first wipe occur immediately on mode entry?
