# Changelog

## 2.1.0-beta.1 (2026-10-09)
- Consolidated previously stacked V1/V2/beta.2 instruction overrides into one coherent protocol.
- Corrected published-version mismatch.
- Added explicit causal attribution, fair handling of unknowns, source-aware score confidence, and re-evaluation deltas.
- Distinguished shipping vs adoption vs demonstrated impact; prevented automatic score promotion after evidence provenance upgrade.
- Added 22 adversarial scenario specifications, blank execution log and static structure check.
- Clearly marked model-consistency testing **not performed**.
- Preserved previous references and tests under `legacy/` for provenance, not execution.
