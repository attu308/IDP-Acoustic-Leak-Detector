# Review II Operational Checklist & Guide Sign-Off Protocol

**Course:** BACSE291 - Innovative Design Project (AY 2026–2027)  
**Evaluation:** Review II (Initial Design & 20% Prototype - 20 Marks)  
**Scheduled Date:** 23 September 2026 (11:45 AM – 01:30 PM)  
**Venue:** Allotted Department Panel Lab  

---

## 1. University Administrative & Prerequisite Compliance

- [x] **Faculty Guide Review & Approval:**
  - Progress discussed with assigned project mentor during scheduled Thursday/Friday consultation slot.
  - Review II slide deck, system architecture, and 20% prototype demonstrated to guide.
  - Formal mentor consent obtained prior to attending the panel review.
- [x] **Team Attendance & Reporting:**
  - All registered team members scheduled to report punctually at **11:45 AM**.
  - All team members confirmed to remain present throughout the evaluation slot.
- [x] **Venue & Panel Confirmation:**
  - Verified assigned lab venue and faculty panel roster on department notice sheet.

---

## 2. Mandatory Presentation Compliance (8 Slides)

- [x] **Slide Structure Adherence:**
  - **Slide 1:** Title, student roll numbers, specialization, guide details.
  - **Slide 2:** Structured agenda.
  - **Slide 3:** Problem definition, Non-Revenue Water (NRW) crisis, real-world relevance.
  - **Slide 4:** Literature survey (Hunaidi et al. acoustic propagation, SCADA DMA flow-balance, commercial loggers).
  - **Slide 5:** Identified technical challenges & clear research gap.
  - **Slide 6:** Concrete, measurable project objectives across hardware, DSP, TinyML, and actuation.
  - **Slide 7:** Proposed methodology, high-res system architecture diagram, FreeRTOS Core 0/1 segregation, component trade-off matrix.
  - **Slide 8:** Results / Initial implementation (~20% completion milestone) with simulation-based spectral comparison.
- [x] **Design Integrity:**
  - Zero auto-generated/generic AI slide templates; custom professional engineering formatting.
  - High-resolution visual diagrams (`presentation/assets/system_architecture.png` and `spectral_comparison.png`) embedded.

---

## 3. 20% Prototype Demonstration Deliverables

- [x] **DSP Acoustic Feature Extraction Engine:**
  - 16 kHz sampling and 1st-order analog high-pass emulation (>500 Hz).
  - 512-point FFT framing with Hanning windowing and 32-band Log-Mel filterbank conversion.
  - Validated via self-test (`python3 dsp/dsp_pipeline.py --test` exits 0).
- [x] **Simulation-Based Turbulence Differentiation:**
  - Validated DSP pipeline using synthetic acoustic signals modeled on published literature (>30 dB surge in 1.5–5 kHz band vs. laminar baseline).
- [x] **Embedded Firmware Architecture:**
  - ESP32-S3 PlatformIO project configured with FreeRTOS dual-core task segregation (`firmware/src/main.cpp`).
  - Thread-safe FreeRTOS queue (`xQueueFeatureMap`) passing feature frames from Core 0 to Core 1.
  - GPIO relay trigger (`SOLENOID_RELAY_PIN`) executing sub-50ms shutoff upon simulated anomaly.

---

## 4. 10-Minute Presentation Rehearsal & Defense Prep

- [x] **Timing Budget (Strict 10 Minutes Total):**
  - **6 Minutes:** Slide presentation (Strict adherence to speaker allocation).
  - **4 Minutes:** Panel Q&A defense.
- [x] **Individual Q&A Mastery (Rubric 7 - 2 Marks):**
  - **Member 1:** Prepared to defend FreeRTOS task prioritization, DMA double-buffering, and relay fail-safe actuation.
  - **Member 2:** Prepared to defend acoustic physics in water/PVC, Mel filterbank vs speech MFCCs, and GCC-PHAT math.
  - **Member 3:** Prepared to defend TinyML int8 quantization error, MAC operation budgeting, and false-positive debouncing.

---

## 5. Review Day Backup & Redundancy Measures

- [x] Presentation deck saved in multiple offline formats:
  - Primary: `presentation/Review2_Presentation.pptx`
  - Fallback: High-resolution exported PDF slides.
- [x] Offline execution: Presentation and demonstration scripts run locally without requiring venue Wi-Fi.
- [x] Prototype fallback: Video recording and high-res spectral plots available if projector hardware fails.
