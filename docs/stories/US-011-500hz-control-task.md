# US-011 500 Hz Control Task Execution

| Field | Value |
|---|---|
| Epic | E3 Real-Time Control and MCU |
| Size | M |
| Requirements | PR-020 |
| PRD verification | Timing measurement |

## Story
As the control software, I want a high-priority task executing at 500 Hz (2 ms period) so that sensing and control run deterministically.

## Size rationale (M)
Scheduler/timer setup and period-jitter verification; hardware-near but small logic.

## Scope
- In: periodic task at 2 ms, jitter measurement hook, task entry for control modules.
- Out: WCET analysis and margin (US-012), isolation of other tasks (US-013).

## Acceptance criteria
- Given the task is running, then the measured period is 2 ms within the approved jitter tolerance.
- Task contains no blocking calls.
- Period source and tolerance are documented; sampling and PWM rates are documented separately.

## Independent test approach
Run on a simulated or target timer with a dummy workload; measure period statistics.

## Dependencies
- **Depends on (stories):** none
- **Blocks:** US-005 (soft), US-012, US-013, US-014, US-015
- **Open decisions:** Q3, Q9
- **External inputs:** MCU/RTOS choice (not mandated); jitter tolerance

## Requirement-analysis points
- PRD says "sensing/control task"; confirm whether rain-sensor sampling is inside this task (AGENTS.md Q3 says slower sampling is acceptable).
- Jitter tolerance undefined.
