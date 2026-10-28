# US-015 Motor Driver Command Output

| Field | Value |
|---|---|
| Epic | E3 Real-Time Control and MCU |
| Size | L |
| Requirements | PR-022 |
| PRD verification | Integration test |

## Story
As the control software, I want wipe requests converted into motor-driver commands so that the motor runs at the requested speed using feedback where the strategy requires.

## Size rationale (L)
Command generation, driver HAL (PWM/enable), and feedback usage; hardware-dependent and central to many stories.

## Scope
- In: conversion of speed request to driver command via HAL, enable/disable control, feedback consumption interface.
- Out: limit enforcement (US-022), protection responses (US-023, US-027).

## Acceptance criteria
- Given a speed request, then the driver command corresponds to it per the documented transfer function.
- Given no request or a disable, then the driver output is in its defined inactive state.
- Hardware access is isolated behind a HAL interface.
- PWM frequency and sampling rates are documented separately from the 500 Hz rate.

## Independent test approach
HAL stub records commands; or integration test with driver evaluation hardware.

## Dependencies
- **Depends on (stories):** US-011 (soft)
- **Blocks:** US-022, US-025 (soft), US-033
- **Open decisions:** Q3 (PWM), Q5 (feedback)
- **External inputs:** motor-driver part and interface (TBD in PRD Section 8)

## Requirement-analysis points
- Control strategy (open-loop vs closed-loop) is not specified; "where required" is undefined.
- Direction/reversing or park control unspecified.
