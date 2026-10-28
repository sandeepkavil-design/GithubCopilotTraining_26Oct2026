# US-006 Command Priority Arbitration and Safe Park

| Field | Value |
|---|---|
| Epic | E1 Driver Input and Modes |
| Size | M |
| Requirements | PR-005 |
| PRD verification | Test / Review |

## Story
As a driver, I want my commands to take deterministic priority over automatic control so that OFF always stops new wiping.

## Size rationale (M)
Arbitration table plus conditional park sequence; safety-reviewed behavior.

## Scope
- In: priority rules between driver modes and automatic requests; Driver OFF inhibits new wipe commands; defined safe park sequence if required.
- Out: mode implementations (US-003, US-004, US-005, US-010).

## Acceptance criteria
- Given any combination of driver request and automatic request, then exactly one wipe command results, per a documented priority table.
- Given Driver OFF, then no new wipe command is issued even if automatic requests exist.
- Given a park sequence is required, then it completes after OFF and is the only permitted motion.
- Arbitration result is identical for identical inputs (deterministic).

## Independent test approach
Table-driven test with stubbed requests from each source; assert chosen command.

## Dependencies
- **Depends on (stories):** US-003; US-004, US-005, US-010 (request sources, stub-able)
- **Blocks:** none
- **Open decisions:** Q5 (park feedback availability), Q6
- **External inputs:** vehicle park-position requirement

## Requirement-analysis points
- AGENTS.md Q5 assumes no position feedback; a park sequence then needs a time- or current-based method. Needs confirmation.
- Safe park behavior needs safety review.
