# US-012 Timing Measurement, WCET and Overrun Diagnostics

| Field | Value |
|---|---|
| Epic | E3 Real-Time Control and MCU |
| Size | M |
| Requirements | PR-021, PR-027 |
| PRD verification | WCET analysis / Stress test; Test / Review |

## Story
As an engineer, I want execution time measured and overruns reported so that the 2 ms deadline and timing margin are demonstrably met.

## Size rationale (M)
Instrumentation, worst-case workload definition, and overrun flag.

## Scope
- In: per-cycle execution-time measurement, maximum tracking, margin check against approved limit, overrun flag for diagnostics.
- Out: fault storage (US-031), scheduling isolation (US-013).

## Acceptance criteria
- Given a task exceeding its budget, then the overrun flag is raised in the same or next cycle.
- Given the defined worst-case workload, then measured maximum execution time is reported and compared to the approved margin.
- Instrumentation can be disabled or reduced in production per documented decision.
- Instrumentation overhead is measured and stated.

## Independent test approach
Dummy workloads of known duration on the 500 Hz task (stub or real); assert measured values and flag.

## Dependencies
- **Depends on (stories):** US-011
- **Blocks:** US-016 (data input), US-031 (soft)
- **Open decisions:** Q9 (CPU budget)
- **External inputs:** definition of worst-case workload; approved timing margin

## Requirement-analysis points
- Timing margin value is "engineering-approved" and not yet defined.
- AGENTS.md Q9 proposes control loop at most 30 % CPU; confirm.
