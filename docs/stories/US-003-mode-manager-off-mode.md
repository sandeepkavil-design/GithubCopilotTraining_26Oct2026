# US-003 Mode Manager and OFF Mode

| Field | Value |
|---|---|
| Epic | E1 Driver Input and Modes |
| Size | S |
| Requirements | PR-001 |
| PRD verification | Test |

## Story
As a driver, I want a selectable OFF mode so that wiping stops when I request it.

## Size rationale (S)
Establishes the mode state container and implements one mode (OFF).

## Scope
- In: mode enumeration, mode selection from validated input, OFF behavior (no new wipe requests), deterministic mode transitions table.
- Out: continuous (US-004), intermittent (US-005), automatic (US-010), arbitration with safe park (US-006).

## Acceptance criteria
- Given a valid OFF selection, when evaluated, then the active mode is OFF and no new wipe request is produced.
- Given an invalid-input flag from US-002, then the mode follows the documented safe behavior.
- Mode transition table is complete: every (current mode, input) pair has a defined next mode.
- Initial mode after startup is OFF.

## Independent test approach
Inject validated-input stubs; assert mode output and absence of wipe requests.

## Dependencies
- **Depends on (stories):** US-002 (interface only; stub-able)
- **Blocks:** US-004, US-005, US-006, US-010
- **Open decisions:** Q6
- **External inputs:** approved driver-control set and mode list

## Requirement-analysis points
- PR-001 conflicts mildly with safe park: does OFF complete the current wipe? Decided in US-006.
