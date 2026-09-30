# CycloneShield AI Architecture

```text
Demo JSON / future public-source adapter
        |
        v
Validation and normalization
        |
        v
Transparent exposure estimator or future LocalModel adapter
        |
        v
FastAPI schemas and endpoints
        |
        v
Responsive browser dashboard: map, factors, preparedness, resources, provenance
```

The MVP intentionally keeps the runtime small: in-memory demo records, no startup training, no large raw downloads, and no external service dependency. The adapter boundary is the place to add an official forecast provider after access, terms, timestamping, and schema validation are implemented.
