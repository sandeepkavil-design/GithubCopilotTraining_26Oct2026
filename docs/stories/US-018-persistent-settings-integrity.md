# US-018 Persistent Settings Integrity and Versioning

| Field | Value |
|---|---|
| Epic | E4 Embedded Application and Memory |
| Size | M |
| Requirements | PR-033 |
| PRD verification | Test / Review |

## Story
As the control software, I want persistent settings stored with an integrity check, version, and safe defaults so that corrupted or outdated data is never used.

## Size rationale (M)
Storage format, integrity check, version handling, and default fallback.

## Scope
- In: record format with version, integrity check, load with validation, safe-default substitution.
- Out: what settings exist (defined by consuming stories), memory-exhaustion handling (US-019).

## Acceptance criteria
- Given a valid record, then it loads and is flagged valid.
- Given a record with a failed integrity check, then safe defaults are used and the failure flagged.
- Given an unsupported version, then safe defaults are used or migration follows the documented rule.
- Safe defaults never enable unrestricted motor operation.

## Independent test approach
Stub NVM with valid, bit-flipped, and old-version images; assert outcome.

## Dependencies
- **Depends on (stories):** none
- **Blocks:** US-019, US-021 (soft)
- **Open decisions:** Q11 (integrity mechanism: CRC vs HMAC)
- **External inputs:** NVM type, settings list

## Requirement-analysis points
- AGENTS.md Q11 says "CRC/HMAC"; choose one (HMAC needs key management, which conflicts with the no-hardcoded-keys rule).
