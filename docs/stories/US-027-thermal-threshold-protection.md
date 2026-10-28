# US-027 Thermal Warning, Derating and Shutdown Protection

| Field | Value |
|---|---|
| Epic | E6 Thermal Management and Duty Cycle |
| Size | L |
| Requirements | PR-054, PR-055 |
| PRD verification | Test; Safety review / Test |

## Story
As a driver, I want thermal protection that warns and derates before shutting down so that I never lose wiping abruptly without need.

## Size rationale (L)
Three-stage protection tied to safety analysis and driver visibility.

## Scope
- In: warning, derating, and shutdown thresholds per variant; staged response; driver-notification request.
- Out: temperature input (US-026), duty-cycle policy (US-025), recovery (US-028).

## Acceptance criteria
- Given temperature below the warning threshold, then no action.
- Given it exceeds warning, derating, then shutdown thresholds, then each corresponding response occurs in order.
- Thresholds are read from the variant parameter set.
- Abrupt loss of wiping occurs only when the documented hazard assessment allows it.

## Independent test approach
Stub temperature ramps; assert response stage and notification request.

## Dependencies
- **Depends on (stories):** US-020, US-025, US-026 (stub-able); US-015 (derate output, soft); US-034 (notification, soft)
- **Blocks:** US-028, US-031 (soft)
- **Open decisions:** Q4, Q8
- **External inputs:** thresholds, hazard assessment

## Requirement-analysis points
- Threshold values are TBD in PRD Section 8.
- Derating method (speed reduction vs duty reduction) unspecified.
- Needs safety-review sign-off before production per AGENTS.md.
