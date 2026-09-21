# DECISIONS.md - Technical Reasoning Log

## [2026-09-21] D001: Methodology & Framework Adoption
*   **Context:** Project initialized for IDP Review II. Needed a robust workflow for AI-assisted embedded engineering that survives context resets and session handoffs.
*   **Decision:** Adopted the Attest Phase/Step methodology with strict machine-verifiable Definition of Done (DoD).
*   **Reasoning:** Embedded systems and TinyML have a high risk of silent regressions (e.g., modifying DSP parameters breaks neural net input tensor shape). Cumulative, machine-checkable gates prevent this.

## [2026-09-21] D002: Build System Choice
*   **Context:** C++ embedded development on ESP32-S3.
*   **Decision:** Use PlatformIO (`pio`) with FreeRTOS dual-core task segregation.
*   **Reasoning:** PlatformIO natively supports a `native` environment for running DSP C++ unit tests on host machines without needing an ESP32 plugged in constantly, speeding up algorithmic development.

## [2026-09-21] D003: Presentation Pipeline Strategy & Machine-Checked DoD
*   **Context:** University reviews require formal `.pptx` presentation decks matching strict slide outlines and time limits.
*   **Decision:** Generate real binary `.pptx` slide files programmatically and verify their structure using an automated Python verification script (`scripts/verify_pptx.py`).
*   **Reasoning:** Markdown slides do not meet faculty expectations for visual diagrams and standard classroom presentation. Automated generation from structured data ensures 100% adherence to the mandatory 8-slide template while eliminating manual formatting errors.

## [2026-09-21] D004: Sensor & DSP Acoustic Feature Selection
*   **Context:** `idea.md` initially proposed airborne MEMS microphones (INMP441) and speech-oriented MFCCs with an analog op-amp.
*   **Decision:** Standardized on contact Piezoelectric sensors coupled to an active charge amplifier/filter, feeding into Log-Mel Spectrograms scaled to 1–8 kHz pipe turbulence frequencies.
*   **Reasoning:** Airborne microphones suffer massive acoustic impedance mismatch when clamped to pipe exteriors and pick up room speech. INMP441 is digital and cannot interface with analog op-amps. Piezoelectric contact transducers directly measure structural wall vibrations.

## [2026-09-21] D005: Localization Algorithm Selection
*   **Context:** Naive arrival timestamp subtraction over Wi-Fi/NTP was mathematically flawed due to the high speed of sound in water (~1480 m/s) and continuous turbulence nature of leaks.
*   **Decision:** Upgraded multi-node localization to Generalized Cross-Correlation with Phase Transform (GCC-PHAT) across continuous vibration signals.
*   **Reasoning:** Pressurized micro-leaks emit continuous stationary broadband noise rather than discrete impulses. Cross-correlation in the frequency domain is the established signal processing standard for continuous acoustic emission delay estimation.
