# Hustle City Repository Layout

```text
Hustle-City/
├── ENGINE/
│   ├── README.md
│   ├── unreal/                 # Primary UE5 project source and docs
│   └── unity/                  # Secondary Unity 6 adapter and docs
├── SHARED_CORE/
│   ├── README.md
│   ├── schemas/                # Versioned canonical JSON schemas
│   ├── rules/
│   ├── interfaces/
│   └── content/
├── SHARED_ASSETS/
│   ├── source/
│   ├── interchange/
│   ├── manifests/
│   └── licenses/
├── architecture/
│   ├── PORTABILITY_CONTRACT.md
│   ├── ENGINE_ADAPTERS.md
│   └── PROJECT_LAYOUT.md
└── quality/
    └── compatibility/          # Shared fixtures and conformance tests
```

Engine project files and generated caches belong only under their engine workspace. Canonical specifications and assets must not be duplicated into competing sources of truth.
