# US-026 Motor/Driver Temperature Monitoring or Thermal Model

| Field | Value |
|---|---|
| Epic | E6 Thermal Management and Duty Cycle |
| Size | M |
| Requirements | PR-052 |
| PRD verification | Test / Analysis |

## Story
As the control software, I want motor/driver temperature measured or estimated so that thermal protection has a reliable input.

## Size rationale (M)
Either sensor interface or model implementation plus validation evidence.

## Scope
- In: temperature value from a sensor, or from a thermal model when no sensor exists; validity status.
- Out: threshold actions (US-027).

## Acceptance criteria
- Given a sensor, then the temperature output follows the stubbed input with the documented conversion.
- Given a model, then the estimate follows the model for stubbed current and time inputs and is traceable to validation data.
- Output carries a validity/confidence status.

## Independent test approach
Stub current/temperature inputs; compare outputs to reference model or table.

## Dependencies
- **Depends on (stories):** US-020 (model parameters, stub-able); US-022 (current, soft)
- **Blocks:** US-027, US-029
- **Open decisions:** Q5
- **External inputs:** thermal parameters, validation data

## Requirement-analysis points
- AGENTS.md Q5 assumes no temperature sensor, so the model must be validated against test data that does not exist yet.
- Ambient temperature input unspecified.
