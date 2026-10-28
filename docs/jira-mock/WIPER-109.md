# WIPER-109: Rain intensity to wipe mapping with hysteresis

Dummy Jira issue (mock of a Jira MCP response). Mapped to [US-009](../stories/US-009-intensity-to-wipe-mapping-hysteresis.md).

| Jira field | Value |
|---|---|
| Key | WIPER-109 |
| Issue type | Story |
| Status | Ready for Design |
| Priority | High |
| Epic link | E2 Rain Sensing and Adaptive Control |
| Story points / size | L |
| Labels | wiper, automatic-mode, calibration, PR-011, PR-012, PR-015 |
| Linked requirements | PR-011, PR-012, PR-015 |
| Blocked by | WIPER-107 (interface only; stub-able) |
| Blocks | WIPER-110 |
| Story key (repo) | US-009 |

## Description
As a driver in automatic mode, I want wipe interval/speed to follow rain intensity smoothly so that the wipers neither lag nor oscillate.

Scope in: filtering of intensity, threshold table, hysteresis, transition behaviour, output of calibrated interval and/or speed command.
Scope out: automatic mode enablement and fallback (WIPER-110), motor limits (WIPER-122).

## Acceptance criteria
1. Given steady intensity at each calibrated level, then the output matches the approved mapping.
2. Given intensity oscillating around a threshold within the hysteresis band, then the output does not change.
3. Given intensity crossing a threshold beyond hysteresis, then the output changes following the defined transition behaviour.
4. The intensity value is never used directly as a motor-speed command unless the calibration explicitly defines it (PR-015).
5. Thresholds, hysteresis width, and filter constants are configuration data.

## Open points (from refinement)
- Does the automatic-sensitivity dial shift thresholds or scale output? (Q6)
- Interval-only, speed-only, or both?
- Filter type and time constant. (Q2, Q3)

## Comments
- (mock) Calibration data from representative rain tests is not yet available; use `TODO:` markers.
