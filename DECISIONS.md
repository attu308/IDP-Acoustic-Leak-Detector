# DECISIONS.md - Technical Reasoning Log

## [2026-09-21] D001: Methodology & Framework Adoption
*   **Context:** Project initialized for IDP Review II. Needed a robust workflow for AI-assisted embedded engineering.
*   **Decision:** Adopted the Attest Phase/Step methodology with strict machine-verifiable Definition of Done (DoD).
*   **Reasoning:** Embedded systems and TinyML have a high risk of "silent regressions" (e.g., modifying DSP code breaks model input shape). Cumulative, machine-checkable gates prevent this.

## [2026-09-21] D002: Build System Choice
*   **Context:** C++ embedded development on ESP32-S3.
*   **Decision:** Use PlatformIO (`pio`) over Arduino IDE or raw ESP-IDF.
*   **Reasoning:** PlatformIO natively supports a `native` environment for running DSP C++ unit tests on the host machine without needing an ESP32 plugged in constantly, speeding up algorithmic development.
