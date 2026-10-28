# US-025 Cumulative Duty-Cycle Accounting and Eight-Hour Policy

| Field | Value |
|---|---|
| Epic | E6 Thermal Management and Duty Cycle |
| Size | M |
| Requirements | PR-050, PR-051 |
| PRD verification | Test / Analysis; Safety review |

## Story
As the control software, I want operating time accounted against a defined duty-cycle policy so that the eight-hour constraint is enforced without creating an unsafe visibility condition.

## Size rationale (M)
Counter logic plus a policy that needs safety review; interpretation is open.

## Scope
- In: operating-time accounting per the chosen definition, warning and limit actions per the policy, reset rules.
- Out: thermal sensing/model (US-026), threshold protection (US-027).

## Acceptance criteria
- Given operation per the defined accounting rule, then the counter advances accordingly and stops when idle.
- Given the limit is reached, then the policy action occurs (not an abrupt stop unless hazard analysis permits).
- Counter behavior across power cycles follows the documented rule.
- Policy parameters are configuration data.

## Independent test approach
Accelerated simulated time; stub energization signal; assert counter, warning, and limit action.

## Dependencies
- **Depends on (stories):** US-020 (duty-cycle limit, stub-able); US-015 (energization signal, soft); US-011 (tick, soft)
- **Blocks:** US-027, US-029
- **Open decisions:** Q8
- **External inputs:** approved definition of "eight hours"; hazard assessment

## Requirement-analysis points
- CONFLICT: AGENTS.md Q8 proposes "inhibit new wipe commands" at 8 h, which is an abrupt shutdown that PR-051 and PR-055 warn against without hazard assessment.
- PRD says "continuous" operation; AGENTS.md Q8 says "cumulative". Confirm.
- Counter persistence across power cycles vs "recovery after power cycle" in Q8 are mutually inconsistent.
