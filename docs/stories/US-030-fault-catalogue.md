# US-030 Fault Catalogue

| Field | Value |
|---|---|
| Epic | E7 Diagnostics and Fault Handling |
| Size | M |
| Requirements | PR-061 |
| PRD verification | Review / Test |

## Story
As an engineer, I want every fault defined with detection condition, severity, response, recovery, and indication so that diagnostics behave consistently.

## Size rationale (M)
Specification and data-table deliverable covering all fault sources.

## Scope
- In: fault list (sensor failure, motor overload/stall, overtemperature, invalid configuration, watchdog reset, control-task overrun, others found), the five attributes per fault, machine-readable table.
- Out: detection and recording logic (US-031).

## Acceptance criteria
- Every PR-060 fault has a table entry with all five attributes.
- Each entry traces to a requirement and to the story that detects it.
- Table is loadable by code without custom parsing per fault.

## Independent test approach
Static check of table completeness; review.

## Dependencies
- **Depends on (stories):** none
- **Blocks:** US-031, US-032, US-034
- **Open decisions:** Q10, Q11
- **External inputs:** safety analysis for severity and response

## Requirement-analysis points
- Severity scale undefined.
- Fault codes depend on the diagnostic protocol (Q10).
