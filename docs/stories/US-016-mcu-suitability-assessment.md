# US-016 MCU Suitability Assessment

| Field | Value |
|---|---|
| Epic | E3 Real-Time Control and MCU |
| Size | M |
| Requirements | PR-023, PR-024 |
| PRD verification | Design review |

## Story
As an engineer, I want candidate Renesas/TI MCUs assessed against documented criteria so that selection is justified and traceable.

## Size rationale (M)
Analysis and documentation deliverable with multiple criteria; no code.

## Scope
- In: assessment against PRD Section 9 criteria (WCET headroom, RAM/flash, PWM/timers, ADC, watchdog, brownout, temperature, qualification, safety, debug).
- Out: software implementation.

## Acceptance criteria
- Each PRD Section 9 criterion has a documented requirement value and a per-candidate result.
- Selection rationale cites measured or estimated data (US-012, US-017).
- No MCU is mandated without recorded evidence.

## Independent test approach
Review against a checklist; no runtime dependency.

## Dependencies
- **Depends on (stories):** US-012, US-017 (data inputs, soft)
- **Blocks:** none
- **Open decisions:** Q1, Q9, Q11
- **External inputs:** candidate datasheets, safety-allocation decision

## Requirement-analysis points
- AGENTS.md Q11 assumes 0-70 degC, which is narrower than typical automotive MCU ranges; confirm.
- AEC-Q100 grade needed is undefined.
