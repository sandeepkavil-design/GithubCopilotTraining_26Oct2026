# Story Index: Rain-Adaptive Wiper Control System

Source: [wiper_control_system_product_requirements.md](wiper_control_system_product_requirements.md). Open-decision references (Q1-Q11) follow [AGENTS.md](../AGENTS.md) Section 13.

**Sizing:** S/M/L is story effort (not motor variant). S = one narrow behavior; M = one module or analysis with several cases; L = multi-requirement or safety-relevant integration.

**Independence rule:** every story is testable alone by stubbing the interfaces of the stories it depends on. "Depends on" means an interface is needed, not that the other story must be finished first.

## Stories

| ID | Title | Size | Requirements | Depends on | Open decisions |
|---|---|---|---|---|---|
| [US-001](stories/US-001-driver-input-acquisition-debounce.md) | Driver input acquisition and debounce | S | PR-007 | - | Q6 |
| [US-002](stories/US-002-driver-input-validation.md) | Driver input validation | S | PR-006 | 001 | Q6 |
| [US-003](stories/US-003-mode-manager-off-mode.md) | Mode manager and OFF mode | S | PR-001 | 002 | Q6 |
| [US-004](stories/US-004-continuous-wipe-mode.md) | Continuous wipe mode | S | PR-002 | 003 | Q4, Q6 |
| [US-005](stories/US-005-intermittent-wipe-mode.md) | Intermittent wipe mode | M | PR-003 | 003, 011 (soft) | Q6 |
| [US-006](stories/US-006-command-priority-and-safe-park.md) | Command priority and safe park | M | PR-005 | 003, 004, 005, 010 | Q5, Q6 |
| [US-007](stories/US-007-rain-sensor-acquisition-and-intensity.md) | Rain sensor acquisition and intensity | M | PR-010 | - | Q2 |
| [US-008](stories/US-008-rain-sensor-validity-detection.md) | Rain sensor validity detection | M | PR-013 | 007 | Q2, Q7 |
| [US-009](stories/US-009-intensity-to-wipe-mapping-hysteresis.md) | Intensity-to-wipe mapping with hysteresis | L | PR-011, 012, 015 | 007 | Q2, Q3, Q6 |
| [US-010](stories/US-010-automatic-mode-and-sensor-fallback.md) | Automatic mode and sensor fallback | M | PR-004, 014 | 003, 008, 009, 005 (soft), 034 (soft) | Q7 |
| [US-011](stories/US-011-500hz-control-task.md) | 500 Hz control task | M | PR-020 | - | Q3, Q9 |
| [US-012](stories/US-012-timing-wcet-overrun-diagnostics.md) | Timing, WCET, overrun diagnostics | M | PR-021, 027 | 011 | Q9 |
| [US-013](stories/US-013-scheduling-isolation.md) | Scheduling isolation | M | PR-025, 034 | 011 | Q9 |
| [US-014](stories/US-014-watchdog-supervision.md) | Watchdog supervision | M | PR-026 | 011 | Q11 |
| [US-015](stories/US-015-motor-driver-command-output.md) | Motor driver command output | L | PR-022 | 011 (soft) | Q3, Q5 |
| [US-016](stories/US-016-mcu-suitability-assessment.md) | MCU suitability assessment | M | PR-023, 024 | 012, 017 (soft) | Q1, Q9, Q11 |
| [US-017](stories/US-017-resource-budgets-and-hosting.md) | Resource budgets and hosting | M | PR-030, 031 | - | Q9 |
| [US-018](stories/US-018-persistent-settings-integrity.md) | Persistent settings integrity | M | PR-033 | - | Q11 |
| [US-019](stories/US-019-memory-exhaustion-and-corrupt-config.md) | Memory exhaustion and corrupt config | M | PR-032 | 017, 018 | Q9 |
| [US-020](stories/US-020-motor-variant-parameter-set.md) | Motor variant parameter set | M | PR-040, 041 | - | Q4 |
| [US-021](stories/US-021-startup-config-validation.md) | Startup config validation | S | PR-046 | 020 | Q4 |
| [US-022](stories/US-022-torque-current-speed-limit-enforcement.md) | Torque/current/speed limit enforcement | L | PR-042, 043 | 015, 020, 021 | Q1, Q4, Q5 |
| [US-023](stories/US-023-stall-overload-detection-response.md) | Stall and overload detection | M | PR-044, 045 | 022, 020 | Q4, Q5 |
| [US-024](stories/US-024-motor-linkage-sizing-validation.md) | Motor and linkage sizing validation | M | PR-047 | 020 | Q1, Q4 |
| [US-025](stories/US-025-duty-cycle-accounting-eight-hour-policy.md) | Duty-cycle accounting and 8 h policy | M | PR-050, 051 | 020, 015 (soft), 011 (soft) | Q8 |
| [US-026](stories/US-026-temperature-monitoring-thermal-model.md) | Temperature monitoring / thermal model | M | PR-052 | 020, 022 (soft) | Q5 |
| [US-027](stories/US-027-thermal-threshold-protection.md) | Thermal threshold protection | L | PR-054, 055 | 020, 025, 026, 015 (soft), 034 (soft) | Q4, Q8 |
| [US-028](stories/US-028-thermal-recovery.md) | Thermal recovery | S | PR-056 | 027 | Q8 |
| [US-029](stories/US-029-thermal-design-adequacy.md) | Thermal design adequacy | S | PR-053 | 020, 025, 026 | Q4, Q8 |
| [US-030](stories/US-030-fault-catalogue.md) | Fault catalogue | M | PR-061 | - | Q10, Q11 |
| [US-031](stories/US-031-fault-detection-and-recording.md) | Fault detection and recording | L | PR-060 | 030; sources 008, 012, 014, 023, 027 | Q10 |
| [US-032](stories/US-032-fallback-state-management.md) | Fallback state management | M | PR-062 | 030, 031 (soft) | Q7, Q11 |
| [US-033](stories/US-033-safe-startup-reset-brownout.md) | Safe startup, reset, brownout | M | PR-063 | 014, 015, 021, 032 (soft) | Q1, Q11 |
| [US-034](stories/US-034-diagnostic-reporting-interface.md) | Diagnostic reporting interface | M | PR-064 | 030, 031 | Q10 |

Totals: S = 7, M = 22, L = 5.

## Requirement coverage

All 46 PRD requirement IDs map to exactly one story: PR-001 (003), 002 (004), 003 (005), 004 (010), 005 (006), 006 (002), 007 (001), 010 (007), 011 (009), 012 (009), 013 (008), 014 (010), 015 (009), 020 (011), 021 (012), 022 (015), 023 (016), 024 (016), 025 (013), 026 (014), 027 (012), 030 (017), 031 (017), 032 (019), 033 (018), 034 (013), 040 (020), 041 (020), 042 (022), 043 (022), 044 (023), 045 (023), 046 (021), 047 (024), 050 (025), 051 (025), 052 (026), 053 (029), 054 (027), 055 (027), 056 (028), 060 (031), 061 (030), 062 (032), 063 (033), 064 (034).

## Suggested analysis order (by dependency depth)

1. Foundations with no dependencies: 001, 007, 011, 017, 018, 020, 030.
2. Next: 002, 008, 009, 012, 013, 014, 015, 021, 024, 034.
3. Then: 003, 004, 005, 010, 019, 022, 023, 025, 026, 031.
4. Last: 006, 016, 027, 028, 029, 032, 033.

## Cross-story issues for requirement analysis

1. AGENTS.md Q7 cites "stale > 100 ms, per PR-014", but PR-014 has no number (US-008).
2. AGENTS.md Q2 assumes a 10 Hz (100 ms) sensor, so a 100 ms staleness limit would flag normal samples (US-008).
3. AGENTS.md Q8 shutdown at 8 h conflicts with PR-051/PR-055; "cumulative" differs from PRD "continuous" (US-025, US-028).
4. AGENTS.md Q5 assumes no position feedback, which affects safe park (US-006) and torque estimation (US-022).
5. AGENTS.md Q11 assumes 0-70 degC, narrower than typical automotive MCU ranges (US-016).
6. AGENTS.md Q11 offers "CRC/HMAC"; HMAC conflicts with the no-hardcoded-keys rule unless key storage is defined (US-018).
7. Stories US-016, US-024, US-029 are analysis deliverables, not code; confirm ownership.

## Training purposes
