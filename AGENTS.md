# AGENTS.md — Automotive Wiper Control System

## 1. Project Context
- **Product:** Rain-Adaptive Automotive Wiper Control System
- **Target Hardware:** Renesas / Texas Instruments automotive MCU
- **Domain:** Automotive embedded real-time control
- **Source of Truth:** `wiper_control_system_product_requirements.md`
- **Status:** Engineering development; safety and regulatory allocations pending

## 2. Agent Responsibilities
- Implement only approved, traceable product requirements.
- Follow modular, deterministic, testable embedded software architecture.
- Do not invent hardware specifications, calibration values, safety targets, or requirements.
- Document assumptions, design decisions, dependencies, and unresolved requirements.
- Request clarification before implementing safety-critical behavior with undefined requirements.

## 3. Architecture and Coding Rules
- Separate hardware abstraction, application logic, control algorithms, diagnostics, and configuration.
- Prefer portable embedded C/C++ with hardware-specific dependencies isolated.
- Follow MISRA C:2023 or applicable MISRA C++ guidelines.
- Avoid uncontrolled dynamic memory allocation, recursion, undefined behavior, and unbounded loops.
- Apply explicit type safety, range checking, initialization, and error handling.
- Ensure deterministic startup, shutdown, reset, and fault recovery.

## 4. Functional Requirements
- Support OFF, continuous, intermittent, and automatic wiping modes.
- Implement deterministic driver-command priority.
- Process rain intensity using validated filtering, hysteresis, and calibration.
- Support Small/Medium/Large motor variants through validated configuration.
- Enforce motor current, torque, speed, and thermal operating limits.
- Implement diagnostics, fault detection, fallback, and recovery.
- Maintain traceability to PR-xxx requirement identifiers.

## 5. Real-Time and Resource Constraints
- **Control-loop target:** 500 Hz (2 ms period).
- Verify worst-case execution time (WCET) and scheduling margins.
- Prevent lower-priority tasks from blocking control execution.
- Define and enforce CPU, RAM, flash, and stack budgets.
- Use watchdog supervision and deterministic fault handling.
- Never perform blocking operations in time-critical control paths.

## 6. Functional Safety and Reliability
Apply standards according to approved system-level applicability and safety classification.

- **ISO 26262:** Automotive functional safety, HARA, ASIL allocation, safety requirements, verification, and traceability.
- **ISO 21448 (SOTIF):** Evaluate applicability to sensor-dependent control and performance limitations.
- **ISO 16750:** Automotive electrical and environmental operating conditions.
- **ISO 7637 / ISO 10605:** Electrical transients and ESD, as applicable.
- **CISPR 25 / ISO 11452:** Automotive EMC requirements, as applicable.
- **AEC-Q100:** Qualification requirements for selected automotive ICs.
- **ASPICE 4.0:** Requirements engineering, architecture, implementation, verification, and configuration management.
- **ISO 9001 / IATF 16949:** Applicable organizational quality-management processes.

Do not assume ASIL classification, claim compliance, or implement safety mechanisms without approved safety requirements.

## 7. Cybersecurity and Secure Development
- **ISO/SAE 21434:** Automotive cybersecurity engineering and risk assessment.
- **UNECE R155/R156:** Cybersecurity and software-update management, where applicable.
- **CERT C/C++:** Secure coding practices.
- **CWE / OWASP:** Applicable vulnerability prevention and secure development guidance.
- Validate all external inputs, calibration data, and configuration parameters.
- Prevent unauthorized configuration changes and diagnostic access.
- Apply least privilege, secure boot, signed firmware, and authenticated updates where required by the security architecture.
- Never hardcode credentials, secrets, or cryptographic keys.
- Perform dependency, secret, and static security scanning.

## 8. Verification and Testing
- Require unit tests for control logic and fault handling.
- Perform integration, SIL/HIL, boundary-value, and fault-injection testing.
- Verify timing, memory consumption, watchdog, and recovery behavior.
- Test sensor failures, motor stall, thermal overload, brownout, and invalid configurations.
- Maintain requirement-to-code-to-test traceability.
- Define coverage targets according to approved project and safety requirements.
- Do not mark requirements verified without supporting evidence.

## 9. Repository and Documentation
- Maintain documented module interfaces and architecture decisions.
- Use meaningful naming conventions and consistent formatting.
- Link commits and pull requests to requirement IDs.
- Document calibration parameters, assumptions, and hardware dependencies.
- Keep build instructions, test procedures, and toolchain versions reproducible.
- Maintain software versioning and change history.

## 10. CI/CD and Quality Gates
Every production change must pass applicable:
- Compilation with strict compiler warnings.
- MISRA/static-analysis checks and deviation reviews.
- Unit and integration tests.
- Security and dependency scans.
- Timing and memory regression checks.
- Peer review and safety/security review where required.
- Artifact integrity, reproducibility, and release approval checks.

Do not bypass quality gates or modify tests merely to make failing code pass.

## 11. Agent Restrictions
**GitHub Copilot agents must NOT:**
- Modify approved product requirements without authorization.
- Invent motor ratings, thresholds, MCU characteristics, or calibration constants.
- Disable watchdogs, diagnostics, safety checks, or security controls.
- Change safety-critical control behavior without review.
- Introduce unverified third-party dependencies.
- Commit secrets, credentials, or proprietary data.
- Claim production readiness based solely on generated code or passing unit tests.

## 12. Definition of Done
A change is complete only when:
- Requirements are identified and traceable.
- Implementation follows approved architecture and coding standards.
- Relevant tests pass with recorded evidence.
- Static analysis and security checks pass or have approved deviations.
- Timing, memory, and safety impacts are assessed.
- Documentation is updated.
- Required engineering reviews and approvals are completed.

**Governing principle:** Safety, deterministic behavior, traceability, security, and verified requirements take priority over implementation speed.

## 13. Decision Guidance for Open Questions

The PRD (Section 12) lists 11 decisions required before detailed design is complete. Agents encountering uncertainty on these points shall follow this guidance:

### Q1: Vehicle Supply Voltage (12 V or 24 V)
**Recommendation:** Assume **12 V nominal** for training/demo purposes unless specified. Document the assumption explicitly in all datasheet references and power-budget calculations. Real implementation requires confirmation from the vehicle electrical-architecture specification.
**Agent action:** Flag this in code comments as `TODO: CONFIRM_VOLTAGE_SPEC`. Do not hardcode voltage-dependent limits without this decision.

### Q2: Rain Sensor Type and Interface
**Recommendation:** Assume a **capacitive rain sensor with 0-5 V analog output, 10 Hz update rate, ±10% repeatability**. This enables simple ADC sampling but requires documented calibration and filtered intensity mapping.
**Agent action:** Design sensor-data structure and validation logic (PR-013, PR-014). Validate that 10 Hz update is sufficient for 500 Hz control loop. Document fallback behavior for stale data.

### Q3: 500 Hz Scope (Control Task, Sensor Sampling, or PWM?)
**Recommendation:** The 500 Hz target applies to the **high-priority control-task execution**, not to the mechanical wiper cycle or PWM carrier frequency. Sensor sampling may be slower (e.g., 10-50 Hz); PWM frequency depends on motor-driver selection.
**Agent action:** Ensure the control loop executes at 500 Hz. Document sampling and PWM frequencies separately. See PR-020, PR-021.

### Q4: Motor Variant Ratings (S/M/L)
**Recommendation:** Populate the configuration template (PRD Section 8) with reference values for training:
- **Small (S):** 15 Nm rated torque, 500 rpm rated speed, 2 A continuous current
- **Medium (M):** 25 Nm rated torque, 400 rpm rated speed, 3 A continuous current
- **Large (L):** 40 Nm rated torque, 300 rpm rated speed, 5 A continuous current

All limits derive from datasheets. Do not proceed with implementation until real motor part numbers are assigned.
**Agent action:** Encode motor parameters in a configuration file with version tracking. Validate on startup (PR-046). Document that these are demo values.

### Q5: Motor Feedback Availability (Position, Current, Temperature)
**Recommendation:** Assume **current feedback only** is available via a sense resistor + op-amp on the motor-driver output. Position and temperature sensing are **not assumed**; thermal protection uses a calibrated duty-cycle model and motor-current correlation.
**Agent action:** Design current-limit enforcement (PR-042, PR-044). Document thermal model assumptions and validation evidence. Plan for future current or temperature integration if sensor inputs are added.

### Q6: Driver Controls and Modes
**Recommendation:** Assume a **rotary selector switch** (OFF, INT, AUTO, ON positions) plus an **intermittent-interval dial** (0.5 to 5 seconds) and **automatic-sensitivity dial** (0-100%). Map these to PR-001 through PR-004. Validate switch debounce time (PR-007) against 2 ms control-loop period.
**Agent action:** Define input-value ranges, debounce filter constants, and mode-transition rules. Document in a driver-interface specification.

### Q7: Rain-Sensor Failure Fallback
**Recommendation:** When rain-sensor data is invalid or stale (> 100 ms, per PR-014), **inhibit automatic mode and fall back to manual intermittent or OFF**. Log a diagnostic fault. Provide a safe continuation message to the driver through the vehicle interface if supported.
**Agent action:** Implement PR-013 and PR-014 detection and fallback logic. Test with stale, out-of-range, and disconnected sensor signals (VV-003).

### Q8: Eight-Hour Thermal Duty-Cycle Definition
**Recommendation:** Interpret the constraint as **cumulative motor energization time**. Implement a duty-cycle counter that inhibits new wipe commands when 8 hours of cumulative operation is exceeded. Define a driver-visible warning (e.g., dashboard indication) that appears 30 minutes before the limit. Recovery occurs only after power-cycle or explicit reset by the vehicle service system.
**Important:** This policy must align with visibility and safety analysis (PR-051, PR-055). Do not disable or bypass without documented hazard assessment.
**Agent action:** Implement thermal accounting and protection thresholds (PR-050 to PR-056). Request safety-review sign-off before committing this logic to production.

### Q9: Additional Application Workload
**Recommendation:** Assume **no additional MCU applications beyond wiper control and diagnostics** for the demo. If background tasks are added, enforce **strict scheduling isolation** (PR-034) so they cannot block the 500 Hz control loop. Define a CPU budget: control loop ≤ 30%, diagnostics ≤ 20%, margin ≥ 50%.
**Agent action:** Measure control-task and diagnostic-task WCET. Stress-test with concurrent workload (VV-005). Do not implement optional features that approach the CPU margin.

### Q10: Vehicle Interface and Diagnostic Protocol
**Recommendation:** Assume a **simple serial debug interface (UART, 115200 baud) for development**. Production diagnostics assume **ISO 14229-1 UDS over CAN** or **LIN** (to be specified). Define placeholder functions for diagnostic-data reporting (PR-064).
**Agent action:** Design a diagnostic interface abstraction layer. Implement mock UART output for demo; prepare hooks for production protocol integration.

### Q11: Environmental, Functional-Safety, and Cybersecurity Standards
**Recommendation:** For training purposes, assume:
- **Functional Safety:** ISO 26262 ASIL-A or ASIL-B (pending hazard analysis). Implement watchdog, safe startup, and deterministic error handling.
- **Cybersecurity:** No OTA updates in this demo. Assume authenticated firmware loading via production-line tools; require secure boot and configuration integrity (CRC/HMAC).
- **Environmental:** Automotive temperature range 0–70 °C. Vibration per MIL-STD-810. EMC per CISPR 25.
- **Lifecycle:** TBD by vehicle program; assume 10-year lifecycle.

Real implementation requires vehicle-level requirements and standards-compliance approval.
**Agent action:** Document all assumptions in code comments and design-review notes. Request standards-allocation review before claiming production readiness.

---

**Key principle for open questions:** When facing an open decision, agents shall:
1. **Choose a reasonable, documented assumption** aligned with the PRD goals.
2. **Flag the assumption** in code and documentation with `TODO:` markers.
3. **Design for change:** Use configuration files and abstraction layers so the final decision can be integrated without major rework.
4. **Request review:** Do not hide assumptions; present them for engineering approval before implementation proceeds to release.
