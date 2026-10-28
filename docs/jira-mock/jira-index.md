# Dummy Jira Index (stand-in until a Jira MCP server is available)

Each dummy Jira key maps 1:1 to a story in `docs/stories/`. Rule: `US-0NN` -> `WIPER-1NN`.
If `docs/jira-mock/<JIRA_KEY>.md` exists it is the Jira issue content; otherwise the mapped story file is the issue content.
Replace this lookup with the Jira MCP `get issue` call once available; downstream agents only use the `US-xxx` key.

| Jira key | Story key | Story file |
|---|---|---|
| WIPER-101 | US-001 | [US-001](../stories/US-001-driver-input-acquisition-debounce.md) |
| WIPER-102 | US-002 | [US-002](../stories/US-002-driver-input-validation.md) |
| WIPER-103 | US-003 | [US-003](../stories/US-003-mode-manager-off-mode.md) |
| WIPER-104 | US-004 | [US-004](../stories/US-004-continuous-wipe-mode.md) |
| WIPER-105 | US-005 | [US-005](../stories/US-005-intermittent-wipe-mode.md) |
| WIPER-106 | US-006 | [US-006](../stories/US-006-command-priority-and-safe-park.md) |
| WIPER-107 | US-007 | [US-007](../stories/US-007-rain-sensor-acquisition-and-intensity.md) |
| WIPER-108 | US-008 | [US-008](../stories/US-008-rain-sensor-validity-detection.md) |
| WIPER-109 | US-009 | [US-009](../stories/US-009-intensity-to-wipe-mapping-hysteresis.md) |
| WIPER-110 | US-010 | [US-010](../stories/US-010-automatic-mode-and-sensor-fallback.md) |
| WIPER-111 | US-011 | [US-011](../stories/US-011-500hz-control-task.md) |
| WIPER-112 | US-012 | [US-012](../stories/US-012-timing-wcet-overrun-diagnostics.md) |
| WIPER-113 | US-013 | [US-013](../stories/US-013-scheduling-isolation.md) |
| WIPER-114 | US-014 | [US-014](../stories/US-014-watchdog-supervision.md) |
| WIPER-115 | US-015 | [US-015](../stories/US-015-motor-driver-command-output.md) |
| WIPER-116 | US-016 | [US-016](../stories/US-016-mcu-suitability-assessment.md) |
| WIPER-117 | US-017 | [US-017](../stories/US-017-resource-budgets-and-hosting.md) |
| WIPER-118 | US-018 | [US-018](../stories/US-018-persistent-settings-integrity.md) |
| WIPER-119 | US-019 | [US-019](../stories/US-019-memory-exhaustion-and-corrupt-config.md) |
| WIPER-120 | US-020 | [US-020](../stories/US-020-motor-variant-parameter-set.md) |
| WIPER-121 | US-021 | [US-021](../stories/US-021-startup-config-validation.md) |
| WIPER-122 | US-022 | [US-022](../stories/US-022-torque-current-speed-limit-enforcement.md) |
| WIPER-123 | US-023 | [US-023](../stories/US-023-stall-overload-detection-response.md) |
| WIPER-124 | US-024 | [US-024](../stories/US-024-motor-linkage-sizing-validation.md) |
| WIPER-125 | US-025 | [US-025](../stories/US-025-duty-cycle-accounting-eight-hour-policy.md) |
| WIPER-126 | US-026 | [US-026](../stories/US-026-temperature-monitoring-thermal-model.md) |
| WIPER-127 | US-027 | [US-027](../stories/US-027-thermal-threshold-protection.md) |
| WIPER-128 | US-028 | [US-028](../stories/US-028-thermal-recovery.md) |
| WIPER-129 | US-029 | [US-029](../stories/US-029-thermal-design-adequacy.md) |
| WIPER-130 | US-030 | [US-030](../stories/US-030-fault-catalogue.md) |
| WIPER-131 | US-031 | [US-031](../stories/US-031-fault-detection-and-recording.md) |
| WIPER-132 | US-032 | [US-032](../stories/US-032-fallback-state-management.md) |
| WIPER-133 | US-033 | [US-033](../stories/US-033-safe-startup-reset-brownout.md) |
| WIPER-134 | US-034 | [US-034](../stories/US-034-diagnostic-reporting-interface.md) |
