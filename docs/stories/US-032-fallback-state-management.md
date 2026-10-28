# US-032 Fallback State Management

| Field | Value |
|---|---|
| Epic | E7 Diagnostics and Fault Handling |
| Size | M |
| Requirements | PR-062 |
| PRD verification | Fault injection |

## Story
As a driver, I want a documented fallback state when critical inputs or control functions are unavailable so that the system stays safe and predictable.

## Size rationale (M)
State definition, entry/exit conditions, and per-fault mapping.

## Scope
- In: fallback state(s), entry conditions from critical faults, behavior in fallback, exit conditions.
- Out: sensor-specific fallback (US-010), thermal response (US-027).

## Acceptance criteria
- Given each critical-fault flag, then the system enters the defined fallback state.
- In fallback, motor behavior matches the documented specification.
- Exit occurs only when the documented conditions are met.

## Independent test approach
Inject stubbed critical-fault flags; assert state and motor-request output.

## Dependencies
- **Depends on (stories):** US-030; US-031 (soft)
- **Blocks:** US-033 (soft), US-019 (response definition)
- **Open decisions:** Q7, Q11
- **External inputs:** safety analysis defining which functions are critical

## Requirement-analysis points
- "Critical inputs" is undefined; list needed from safety analysis.
- Multiple fallback levels vs a single state?
