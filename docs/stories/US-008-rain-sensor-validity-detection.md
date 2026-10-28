# US-008 Rain Sensor Data Validity Detection

| Field | Value |
|---|---|
| Epic | E2 Rain Sensing and Adaptive Control |
| Size | M |
| Requirements | PR-013 |
| PRD verification | Fault injection |

## Story
As the control software, I want stale, out-of-range, implausible, or unavailable sensor data detected so that automatic control never acts on bad data.

## Size rationale (M)
Four distinct detection classes, each with its own criterion and test.

## Scope
- In: staleness, range, plausibility (e.g. rate-of-change), and availability checks; validity status output.
- Out: fallback behavior (US-010), fault recording (US-031).

## Acceptance criteria
- Given no new sample within the staleness limit, then status = stale.
- Given a raw value outside the sensor range, then status = out of range.
- Given a value change exceeding the plausibility rule, then status = implausible.
- Given no signal or interface error, then status = unavailable.
- Valid data yields status = valid; status transitions are deterministic and each class is distinguishable.

## Independent test approach
Inject stubbed samples with timestamps; assert one status per fault class.

## Dependencies
- **Depends on (stories):** US-007 (sample + timestamp interface; stub-able)
- **Blocks:** US-009 (soft), US-010
- **Open decisions:** Q2, Q7
- **External inputs:** staleness limit, plausibility rule, sensor diagnostics

## Requirement-analysis points
- INCONSISTENCY: AGENTS.md Q7 cites "stale > 100 ms, per PR-014", but PR-014 contains no number. Source of 100 ms unknown.
- AGENTS.md Q2 assumes a 10 Hz sensor (100 ms period); a 100 ms staleness limit would flag normal samples as stale. Limit must exceed the sensor period.
