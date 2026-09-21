# PLAN.md - Smart Acoustic Leak Detector Contract

## Phase 1: Review I (Problem Identification and Planning - 5 Marks)
*Note: Academic milestone achieved prior to Review II. Maintained as historical contract record.*
- **P1-S1: Project Definition, Literature Baseline & Scope Specification**
  - **DoD File:** `idea.md` exists and is non-empty.
  - **DoD Command:** `test -s idea.md` exits 0.

---

## ▲ Phase 2: Review II (Initial Design & 20% Prototype - 20 Marks)
*Expected Milestone: Complete ~20% of project. Requirement analysis, system architecture, component selection justification, and initial demonstrable prototype/module.*

- **P2-S1: Architecture & System Design Visual Assets**
  - **DoD File:** `presentation/assets/system_architecture.png` exists.
  - **DoD Command:** `test -s presentation/assets/system_architecture.png` exits 0.

- **P2-S2: Review II Mandatory 8-Slide Presentation Deck (`Review2_Presentation.pptx`)**
  - **DoD File:** `presentation/Review2_Presentation.pptx` exists.
  - **DoD Command:** `python3 scripts/verify_pptx.py presentation/Review2_Presentation.pptx 8 "Architecture,Objectives,Literature"` exits 0.

- **P2-S3: Panel Q&A Defense Script & Individual Contribution Guide**
  - **DoD File:** `docs/review2_defense_guide.md` exists.
  - **DoD Command:** `test -s docs/review2_defense_guide.md` exits 0.

- **P2-S4: DSP Audio Feature Extraction Prototype (~20% Algorithmic Core)**
  - **DoD File:** `dsp/dsp_pipeline.py` exists.
  - **DoD Command:** `python3 scripts/verify_step.py P2-S4` exits 0.

- **P2-S5: Embedded Firmware Scaffold & FreeRTOS Dual-Core Architecture**
  - **DoD File:** `firmware/src/main.cpp` exists.
  - **DoD Command:** `python3 scripts/verify_step.py P2-S5` exits 0.

- **P2-S6: Review II Pre-Review Guide Sign-Off & 10-Minute Rehearsal Checklist**
  - **DoD File:** `docs/review2_checklist.md` exists.
  - **DoD Command:** `test -s docs/review2_checklist.md` exits 0.

---

## ▲ Phase 3: Review III (Progress Review & 30% Completion - 10 Marks)
*Expected Milestone: Complete ~30% of project. Refined requirement analysis & system design, component confirmation, prototype with early testing, follow-up on Review II feedback.*

- **P3-S1: Review III Presentation Deck (`Review3_Presentation.pptx`)**
  - **DoD File:** `presentation/Review3_Presentation.pptx` exists.
  - **DoD Command:** `python3 scripts/verify_pptx.py presentation/Review3_Presentation.pptx 6` exits 0.

- **P3-S2: C++ Embedded DSP Fixed-Point FFT Engine**
  - **DoD File:** `firmware/include/dsp_engine.h` exists.
  - **DoD Command:** `python3 scripts/verify_step.py P3-S2` exits 0.

- **P3-S3: Acoustic Leak Dataset Preprocessing & Augmentation Pipeline**
  - **DoD File:** `data/pipeline.py` exists.
  - **DoD Command:** `python3 data/pipeline.py --verify` exits 0.

- **P3-S4: 1D-CNN Baseline Classifier Training Pipeline**
  - **DoD File:** `ml/train_cnn.py` exists.
  - **DoD Command:** `python3 ml/train_cnn.py --dry-run` exits 0.

---

## ▲ Phase 4: Review IV (Core Functionality - 50% Completion - 15 Marks)
*Expected Milestone: Complete ~50% of project. Major modules implemented and integrated to demonstrate core functionality.*

- **P4-S1: Review IV Presentation Deck (`Review4_Presentation.pptx`)**
  - **DoD File:** `presentation/Review4_Presentation.pptx` exists.
  - **DoD Command:** `python3 scripts/verify_pptx.py presentation/Review4_Presentation.pptx 6` exits 0.

- **P4-S2: Post-Training Int8 Quantization (PTQ) & SRAM Memory Profiling**
  - **DoD File:** `ml/quantized/leak_model_int8.tflite` exists.
  - **DoD Command:** `test -s ml/quantized/leak_model_int8.tflite` exits 0.

- **P4-S3: TFLite Micro Embedded Inference Engine on ESP32 Core 1**
  - **DoD File:** `firmware/src/inference_engine.cpp` exists.
  - **DoD Command:** `test -s firmware/src/inference_engine.cpp` exits 0.

- **P4-S4: Sub-200ms Latency & Accuracy Verification Benchmarking Suite**
  - **DoD File:** `tests/test_p4_s4_benchmark.py` exists.
  - **DoD Command:** `python3 scripts/verify_step.py P4-S4` exits 0.

---

## ▲ Phase 5: Review V (Integrated Prototype & 80% Validation - 25 Marks)
*Expected Milestone: Complete ~80% of project. Integrated planned modules; validate functionality through testing; demonstrate a complete working prototype.*

- **P5-S1: Review V Presentation Deck (`Review5_Presentation.pptx`)**
  - **DoD File:** `presentation/Review5_Presentation.pptx` exists.
  - **DoD Command:** `python3 scripts/verify_pptx.py presentation/Review5_Presentation.pptx 6` exits 0.

- **P5-S2: Emergency Solenoid Valve Actuation State Machine**
  - **DoD File:** `firmware/src/actuation.cpp` exists.
  - **DoD Command:** `grep -q "SOLENOID_RELAY_PIN" firmware/src/actuation.cpp` exits 0.

- **P5-S3: MQTT Telemetry & Wi-Fi Anomaly Dispatch Module**
  - **DoD File:** `firmware/src/telemetry.cpp` exists.
  - **DoD Command:** `grep -q "mqttClient" firmware/src/telemetry.cpp` exits 0.

- **P5-S4: Integrated Hydraulic Rig Test Validation Protocol & Results**
  - **DoD File:** `docs/test_validation_report.md` exists.
  - **DoD Command:** `test -s docs/test_validation_report.md` exits 0.

---

## — SUBMITTABLE —
*The project at Phase 5 forms a complete, functional baseline (75/100 cumulative marks). The subsequent phases represent upside and open-house exhibition enhancements.*

---

## Phase 6: Review VI (Open House Evaluation - 15 Marks)
*Expected Milestone: Fully functional prototype demonstrated during Open House for independent external evaluation.*

- **P6-S1: Open House Presentation Deck & Demonstration Posters**
  - **DoD File:** `presentation/Review6_OpenHouse.pptx` exists.
  - **DoD Command:** `python3 scripts/verify_pptx.py presentation/Review6_OpenHouse.pptx 6` exits 0.

- **P6-S2: Dual-Node GCC-PHAT Continuous Acoustic Cross-Correlation Module**
  - **DoD File:** `src/gcc_phat.py` exists.
  - **DoD Command:** `python3 scripts/verify_step.py P6-S2` exits 0.

- **P6-S3: Comparative Evaluation & Industrial Cost-Benefit Analysis**
  - **DoD File:** `docs/comparative_evaluation.md` exists.
  - **DoD Command:** `test -s docs/comparative_evaluation.md` exits 0.

---

## Phase 7: Final Report Submission (10 Marks)
*Expected Milestone: Comprehensive project report adhering to academic formatting guidelines.*

- **P7-S1: Comprehensive Project Report Compilation**
  - **DoD File:** `docs/IDP_Final_Report.pdf` exists.
  - **DoD Command:** `test -s docs/IDP_Final_Report.pdf` exits 0.

- **P7-S2: Open-Source Codebase Release & Reproducibility Package**
  - **DoD File:** `README.md` exists.
  - **DoD Command:** `test -s README.md` exits 0.
