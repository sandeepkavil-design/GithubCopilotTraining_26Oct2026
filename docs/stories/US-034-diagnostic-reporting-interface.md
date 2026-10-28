# US-034 Diagnostic Reporting Interface

| Field | Value |
|---|---|
| Epic | E7 Diagnostics and Fault Handling |
| Size | M |
| Requirements | PR-064 |
| PRD verification | Integration test |

## Story
As a service engineer, I want diagnostics reported through the selected vehicle interface so that faults and driver indications are visible externally.

## Size rationale (M)
Abstraction layer with a mock implementation; real protocol deferred.

## Scope
- In: interface abstraction, mock/debug implementation, reporting of fault records and driver-indication requests.
- Out: production protocol implementation (pending decision).

## Acceptance criteria
- Given a recorded fault, then it is reported through the interface in the defined format.
- Given a driver-indication request (US-010, US-027), then it is passed to the interface or reported as unsupported.
- Protocol-specific code is isolated behind the abstraction.

## Independent test approach
Mock transport captures outputs; stub fault records.

## Dependencies
- **Depends on (stories):** US-030, US-031
- **Blocks:** US-010 (soft), US-027 (soft)
- **Open decisions:** Q10
- **External inputs:** vehicle interface and diagnostic protocol (out of scope per PRD Section 3 until specified)

## Requirement-analysis points
- AGENTS.md Q10 proposes UART for development; confirm it is acceptable evidence for PR-064 or only a placeholder.
