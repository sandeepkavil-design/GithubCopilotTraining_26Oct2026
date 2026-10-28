# US-013 Scheduling Isolation of Lower-Priority Work

| Field | Value |
|---|---|
| Epic | E3 Real-Time Control and MCU |
| Size | M |
| Requirements | PR-025, PR-034 |
| PRD verification | Stress test |

## Story
As the control software, I want lower-priority and optional workloads isolated so that they cannot block or delay the 500 Hz task.

## Size rationale (M)
Priority/resource design plus stress-test harness.

## Scope
- In: priority assignment, preemption rules, shared-resource access rules (no blocking waits in control task), stress workload.
- Out: the optional workloads themselves.

## Acceptance criteria
- Given a stress workload running at lower priority, then the 500 Hz task shows no missed deadlines.
- Given a lower-priority task holds a shared resource, then the control task is not blocked.
- Control task has no dependency on a lower-priority task completing.

## Independent test approach
Add a synthetic low-priority load generator; observe control-task deadlines.

## Dependencies
- **Depends on (stories):** US-011
- **Blocks:** none
- **Open decisions:** Q9
- **External inputs:** list of other workloads (undefined in PRD); OS/scheduler choice

## Requirement-analysis points
- PR-030/PR-034 imply "approved supporting application functions" but none are named. AGENTS.md Q9 assumes none for the demo; confirm.
