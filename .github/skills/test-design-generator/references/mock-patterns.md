# Mock Patterns for System / Integration Tests

Principle: the software under test (SUT) only sees the hardware abstraction interface; each mock implements that interface and exposes a test-control API (inject, observe, fault).

## Mock inventory table (put in every test design)

| Dependency | SUT interface | Mock behaviour | Inject | Observe | Faults |
|---|---|---|---|---|---|
| Rain sensor (ADC) | `Adc_Read` | returns scripted values with timestamps | value, update period | read count | stale, out-of-range, disconnected |
| Driver switch/dials | `Din_Read` / `Adc_Read` | scripted raw levels per tick | level sequence, bounce | - | stuck, invalid code |
| Motor driver (PWM) | `Pwm_SetDuty` | records commands | - | duty, enable, timestamps | command rejected |
| Motor current sense | `Adc_Read` | model or script | current profile | - | overcurrent, stall, open load |
| Temperature (if any) | `Temp_Read` | script | value | - | invalid |
| NVM / flash | `Nvm_Read/Write` | RAM-backed store | content, CRC | write log | corrupt, write fail |
| Clock / scheduler | `Time_GetMs`, tick | virtual time | advance(ms) | - | jitter, overrun |
| Watchdog | `Wdg_Kick` | counter | - | kick count/timing | missed kick |
| Vehicle bus / UART / UDS | `Com_Send/Recv` | queue capture | rx frames | tx frames | bus off, timeout |
| Supply | `Supply_GetMv` | script | voltage profile | - | brownout, dropout |

## Pattern 1: scripted input
A table of `(time_ms, value)` the mock replays as virtual time advances.

```c
typedef struct { uint32_t t_ms; uint16_t raw; } MockSample_t;
/* test: MockAdc_Load(CH_RAIN, samples, n); */
```

## Pattern 2: recording output
The mock stores every command with a virtual timestamp so tests assert on value, order, and timing.

```c
typedef struct { uint32_t t_ms; uint16_t duty_permille; bool enable; } MockPwmRec_t;
```

## Pattern 3: virtual time
Tests step the clock deterministically (for example in 2 ms steps for the control task) instead of sleeping. Staleness, debounce, intermittent intervals, and duty-cycle limits are tested by advancing virtual time.

## Pattern 4: fault injection
Each mock exposes `Mock_xxx_InjectFault(kind, params)` with kinds taken from the fault catalogue (US-030). Document the fault, the trigger time, and the expected SUT reaction in the test case.

## Pattern 5: closed-loop plant model (integration)
For motor/current behaviour, a simple plant model maps duty to current/speed so stall and overload can be triggered. Mark all model constants `TBD` or as demo values from AGENTS.md; do not present them as real motor data.

## Pattern 6: NVM
RAM-backed store with CRC; helpers to corrupt a byte, truncate, or fail the next write.

## Test case mock fields (required)
- Mocks used
- Initial mock state
- Injected sequence (with virtual times)
- Observed outputs checked

## Hosting
Run on host (SIL) with the real application code and mocked HAL; keep mocks in a `test/mocks/` folder, separate from production sources. Do not add test hooks (`#ifdef TEST`) in production code.
