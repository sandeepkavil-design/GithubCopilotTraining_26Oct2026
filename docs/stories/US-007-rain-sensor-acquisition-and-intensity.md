# US-007 Rain Sensor Acquisition and Intensity Classification

| Field | Value |
|---|---|
| Epic | E2 Rain Sensing and Adaptive Control |
| Size | M |
| Requirements | PR-010 |
| PRD verification | Test |

## Story
As the control software, I want rain-sensor data acquired and converted to a calibrated intensity level so that automatic mode has a usable input.

## Size rationale (M)
Acquisition, scaling, and calibration application; depends on sensor definition.

## Scope
- In: sensor read via HAL, scaling to engineering units, calibrated intensity level output with timestamp.
- Out: validity checks (US-008), mapping to wipe interval (US-009).

## Acceptance criteria
- Given a stubbed sensor raw value, when processed, then the output intensity level equals the calibration-table result.
- Each output sample carries a timestamp or age for later staleness checks.
- Calibration data is loaded from configuration, not embedded in logic.
- Out-of-range raw values are passed on unaltered with a flag, not silently clamped (handled in US-008).

## Independent test approach
Stub HAL with scripted raw values and a test calibration table; assert levels.

## Dependencies
- **Depends on (stories):** none
- **Blocks:** US-008, US-009
- **Open decisions:** Q2 (sensor type, interface, update rate)
- **External inputs:** sensor datasheet, calibration data

## Requirement-analysis points
- AGENTS.md Q2 assumes capacitive, 0-5 V, 10 Hz, ±10 %; PRD has none of these. Confirm they apply.
- Number of intensity levels not defined.
