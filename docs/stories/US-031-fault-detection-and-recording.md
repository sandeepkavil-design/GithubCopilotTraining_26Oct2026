# US-031 Fault Detection and Recording

| Field | Value |
|---|---|
| Epic | E7 Diagnostics and Fault Handling |
| Size | L |
| Requirements | PR-060 |
| PRD verification | Fault injection |

## Story
As a service engineer, I want defined faults detected and recorded so that failures can be diagnosed.

## Size rationale (L)
Aggregates many fault sources into one recording mechanism with debounce and storage.

## Scope
- In: fault status inputs, qualification/debounce, active/stored state, event record, clearing rules.
- Out: fault definitions (US-030), detection of each source (owning stories), transport (US-034).

## Acceptance criteria
- Given an injected status flag for each cataloged fault, then the fault becomes active after its qualification time and is recorded.
- Given the condition clears, then the active state follows the documented recovery rule while the record persists as specified.
- Records survive reset per the documented rule.
- Recording does not block the control task.

## Independent test approach
Inject synthetic fault flags from stubs of each source; assert records.

## Dependencies
- **Depends on (stories):** US-030; fault sources US-008, US-012, US-014, US-023, US-027 (stub-able)
- **Blocks:** US-034
- **Open decisions:** Q10
- **External inputs:** NVM capacity and endurance for records

## Requirement-analysis points
- Storage depth, aging, and clearing authority unspecified.
