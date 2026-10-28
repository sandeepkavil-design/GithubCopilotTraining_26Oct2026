# Mermaid Snippets for Test Designs

## Partition line
```mermaid
flowchart LR
    A["below min (invalid)"] --- B["valid partition 1"] --- C["valid partition 2"] --- D["above max (invalid)"]
```

## Boundary markers
```mermaid
flowchart LR
    L1["min-1"] --> L2["min"] --> L3["min+1"] --> L4["..."] --> L5["max-1"] --> L6["max"] --> L7["max+1"]
```

## Mode state machine (wiper modes)
```mermaid
stateDiagram-v2
    [*] --> OFF
    OFF --> CONTINUOUS: select ON
    OFF --> INTERMITTENT: select INT
    OFF --> AUTOMATIC: select AUTO
    CONTINUOUS --> OFF: select OFF
    INTERMITTENT --> OFF: select OFF
    AUTOMATIC --> OFF: select OFF
    AUTOMATIC --> INTERMITTENT: sensor invalid or stale
    AUTOMATIC --> FAULT: fault detected
    FAULT --> OFF: recovery condition
```
Adapt transitions to the actual story; this is a layout example, not a requirement.

## Decision flow
```mermaid
flowchart TD
    S([Start]) --> C1{Condition 1?}
    C1 -- Y --> C2{Condition 2?}
    C1 -- N --> A3[Action 3]
    C2 -- Y --> A1[Action 1]
    C2 -- N --> A2[Action 2]
```

## Integration sequence with mocks
```mermaid
sequenceDiagram
    participant T as Test harness
    participant MI as Mock input (ADC/switch)
    participant SUT as Software under test
    participant MO as Mock output (PWM/bus)
    T->>MI: load script / inject fault
    T->>SUT: advance virtual time (2 ms step)
    SUT->>MI: read
    MI-->>SUT: value, age
    SUT->>MO: command
    T->>MO: read recorded output
    T-->>T: compare with expected
```

## Traceability
```mermaid
flowchart LR
    R["PR-xxx"] --> U["US-xxx"] --> AC["AC-n"] --> TC["TC-nnn"]
```

## Fault handling flow
```mermaid
flowchart TD
    D[Detect fault] --> L[Log fault]
    L --> F[Enter fallback]
    F --> R{Recovery condition?}
    R -- Y --> N[Return to normal]
    R -- N --> F
```
