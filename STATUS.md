# STATUS.md - State Tracker

## Current Focus
*   **Target Step:** Phase 2 (Review II) Complete!
*   **Status:** All Review II deliverables (8-slide PPTX, high-res architecture, 20% DSP prototype, FreeRTOS firmware scaffold, Q&A defense script, and guide checklist) are 100% verified, tested, and ready for panel evaluation.
*   **Next Milestone:** Phase 3 (Review III - Progress Review & 30% Completion) starting with Step P3-S1.

---

## Phase Status Board

### Phase 1: Review I (Problem Identification & Planning - 5 Marks)
- [x] **P1-S1:** DONE (Project Definition, Literature Baseline & Scope in `idea.md`)

### ▲ Phase 2: Review II (Initial Design & 20% Prototype - 20 Marks) [COMPLETED]
- [x] **P2-S1:** DONE (Architecture & System Design Visual Assets in `presentation/assets/system_architecture.png`)
- [x] **P2-S2:** DONE (Review II Mandatory 8-Slide PPTX Deck in `presentation/Review2_Presentation.pptx`)
- [x] **P2-S3:** DONE (Panel Q&A Defense Script & Individual Contribution Guide in `docs/review2_defense_guide.md`)
- [x] **P2-S4:** DONE (DSP Audio Feature Extraction Prototype in `dsp/dsp_pipeline.py`)
- [x] **P2-S5:** DONE (Embedded Firmware Scaffold & FreeRTOS Dual-Core Architecture in `firmware/src/main.cpp`)
- [x] **P2-S6:** DONE (Pre-Review Guide Sign-Off & 10-Minute Rehearsal Checklist in `docs/review2_checklist.md`)

### ▲ Phase 3: Review III (Progress Review & 30% Completion - 10 Marks)
- [ ] **P3-S1:** TODO (Review III PPT Presentation Deck)
- [ ] **P3-S2:** TODO (C++ Embedded DSP Fixed-Point FFT Engine)
- [ ] **P3-S3:** TODO (Acoustic Leak Dataset Preprocessing & Augmentation Pipeline)
- [ ] **P3-S4:** TODO (1D-CNN Baseline Classifier Training Pipeline)

### ▲ Phase 4: Review IV (Core Functionality - 50% Completion - 15 Marks)
- [ ] **P4-S1:** TODO (Review IV PPT Presentation Deck)
- [ ] **P4-S2:** TODO (Post-Training Int8 Quantization & SRAM Memory Profiling)
- [ ] **P4-S3:** TODO (TFLite Micro Embedded Inference Engine on ESP32 Core 1)
- [ ] **P4-S4:** TODO (Sub-200ms Latency & Accuracy Verification Benchmarking Suite)

### ▲ Phase 5: Review V (Integrated Prototype & 80% Validation - 25 Marks)
- [ ] **P5-S1:** TODO (Review V PPT Presentation Deck)
- [ ] **P5-S2:** TODO (Emergency Solenoid Valve Actuation State Machine)
- [ ] **P5-S3:** TODO (MQTT Telemetry & Wi-Fi Anomaly Dispatch Module)
- [ ] **P5-S4:** TODO (Integrated Hydraulic Rig Test Validation Protocol & Results)

### — SUBMITTABLE BASELINE (75 Marks) —

### Phase 6: Review VI (Open House Evaluation - 15 Marks)
- [ ] **P6-S1:** TODO (Open House Presentation Deck & Demonstration Posters)
- [ ] **P6-S2:** TODO (Dual-Node GCC-PHAT Continuous Acoustic Cross-Correlation Module)
- [ ] **P6-S3:** TODO (Comparative Evaluation & Industrial Cost-Benefit Analysis)

### Phase 7: Final Report Submission (10 Marks)
- [ ] **P7-S1:** TODO (Comprehensive Project Report Compilation)
- [ ] **P7-S2:** TODO (Open-Source Codebase Release & Reproducibility Package)

---

## Handoff Notes
*   **Gate Verification:** `P2-S6` verified successfully with `./scripts/verify.sh P2-S6` (Exit 0).
*   **Visual Assets:** Redesigned publication-quality, widescreen 16:9 system architecture diagram (`presentation/assets/system_architecture.png`) with orthogonal zero-crossing routing, generous margins, and no text collisions.
*   **Presentation:** Embedded full-width diagram into Slide 7 of `presentation/Review2_Presentation.pptx`.
*   **Next Action:** Awaiting explicit user approval before proceeding to Phase 3 (Review III).
