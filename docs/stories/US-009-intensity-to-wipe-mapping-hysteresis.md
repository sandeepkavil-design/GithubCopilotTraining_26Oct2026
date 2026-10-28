# US-009 Rain Intensity to Wipe Mapping with Hysteresis

| Field | Value |
|---|---|
| Epic | E2 Rain Sensing and Adaptive Control |
| Size | L |
| Requirements | PR-011, PR-012, PR-015 |
| PRD verification | Test / Review |

## Story
As a driver in automatic mode, I want wipe interval/speed to follow rain intensity smoothly so that the wipers neither lag nor oscillate.

## Size rationale (L)
Calibration mapping, filtering, hysteresis, and transition rules with three requirements and heavy calibration dependency.

## Scope
- In: filtering of intensity, threshold table, hysteresis, transition behavior, output of calibrated interval and/or speed command.
- Out: automatic mode enablement and fallback (US-010), motor limits (US-022).

## Acceptance criteria
- Given steady intensity at each calibrated level, then the output matches the approved mapping.
- Given intensity oscillating around a threshold within the hysteresis band, then the output does not change.
- Given intensity crossing a threshold beyond hysteresis, then the output changes following the defined transition behavior.
- The intensity value is never used directly as a motor-speed command unless the calibration explicitly defines it (PR-015).
- Thresholds, hysteresis width, and filter constants are configuration data.

## Independent test approach
Feed stubbed intensity time series (ramps, steps, dithering) and assert output sequence against the mapping table.

## Dependencies
- **Depends on (stories):** US-007 (intensity interface; stub-able)
- **Blocks:** US-010
- **Open decisions:** Q2, Q3 (sampling vs loop rates), Q6 (sensitivity dial)
- **External inputs:** calibration data from representative rain tests (PRD Section 7: to be calibrated)

## Requirement-analysis points
- Whether the automatic-sensitivity dial shifts thresholds or scales output is unspecified.
- Interval-only, speed-only, or both?
- Filter type and time constant need definition.
