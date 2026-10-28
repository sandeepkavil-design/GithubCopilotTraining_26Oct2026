# US-020 Motor Variant Parameter Set (S/M/L)

| Field | Value |
|---|---|
| Epic | E5 Motor Variants, Torque and Limits |
| Size | M |
| Requirements | PR-040, PR-041 |
| PRD verification | Configuration test; Review / Test |

## Story
As the control software, I want a versioned parameter set per motor variant (Small, Medium, Large) so that limits come from approved data and not from the label.

## Size rationale (M)
Data schema plus three parameter sets and selection logic.

## Scope
- In: parameter schema (PRD Section 8: motor rating, torque, current, speed, linkage/wiper length, thermal limits), three variant records, variant selection interface, version tracking.
- Out: startup validation (US-021), enforcement (US-022).

## Acceptance criteria
- Given variant S, M, or L is selected, then the corresponding full parameter set is returned.
- Every PRD Section 8 parameter has a field; unpopulated (TBD) values are marked and cannot be used for operation.
- Parameter data carries a version identifier.
- No limit is derived from the variant label itself.

## Independent test approach
Unit test with fixture parameter files; schema and selection checks.

## Dependencies
- **Depends on (stories):** none
- **Blocks:** US-021, US-022, US-024, US-025, US-026, US-027, US-029
- **Open decisions:** Q4
- **External inputs:** supplier motor data (PRD Section 8 is all TBD)

## Requirement-analysis points
- AGENTS.md Q4 gives demo values but also says not to proceed without real part numbers; clarify whether demo values may be used for this story.
- Variant selection source (calibration, hardware strap, NVM) is unspecified.
