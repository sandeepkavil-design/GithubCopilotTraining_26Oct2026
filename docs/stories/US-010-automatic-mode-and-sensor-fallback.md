# US-010 Automatic Mode and Sensor-Fault Fallback

| Field | Value |
|---|---|
| Epic | E2 Rain Sensing and Adaptive Control |
| Size | M |
| Requirements | PR-004, PR-014 |
| PRD verification | Test / Review |

## Story
As a driver, I want automatic mode to adapt to rain and fall back safely if the rain sensor fails, so that I keep visibility and am informed.

## Size rationale (M)
Integrates mode, mapping, and validity into a decision plus a documented fallback and driver indication.

## Scope
- In: AUTO mode request generation from US-009 when sensor valid; fallback behavior when invalid; request for driver indication.
- Out: sensor validity detection (US-008), mapping (US-009), actual indication transport (US-034).

## Acceptance criteria
- Given AUTO and sensor valid, then the wipe request equals the mapped output.
- Given AUTO and sensor invalid, then the documented fallback request is issued and no uncontrolled operation occurs.
- Given fallback is active, then an indication request is raised if the vehicle interface supports it.
- Given the sensor becomes valid again, then return to automatic follows a documented recovery rule.

## Independent test approach
Stub mapping output and validity status; assert request and indication flag per combination (matches PRD Section 6 table).

## Dependencies
- **Depends on (stories):** US-003, US-008, US-009 (stub-able); US-005 (fallback target, soft); US-034 (indication, soft)
- **Blocks:** US-006 (request source)
- **Open decisions:** Q7
- **External inputs:** approved fallback definition

## Requirement-analysis points
- INCONSISTENCY: PRD Section 12 Q7 asks what the fallback is; AGENTS.md §13 proposes "manual intermittent or OFF". Which one, and which interval?
- Recovery hysteresis/debounce after sensor returns.
