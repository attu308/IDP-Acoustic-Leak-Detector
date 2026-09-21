# PLAN.md - Smart Acoustic Leak Detector Contract

## Phase 1: Review I (Problem Identification and Planning - 5 Marks)
*Note: This phase represents past academic milestones. Superseded by Review II.*
- **P1-S1: Project Definition & Ideation**
  - **DoD File:** `idea.md` exists.
  - **DoD Command:** `test -s idea.md` exits 0.

## ▲ Phase 2: Review II (Initial Design and 20% Development - 20 Marks)
*Expected Outcome: Requirement analysis, system design, justified component selection, and initial ~20% module development.*
- **P2-S1: Review II Presentation Slides**
  - **DoD File:** `presentation/review2_slides.md` exists.
  - **DoD Command:** `grep -q "Architecture" presentation/review2_slides.md` exits 0.

- **P2-S2: PlatformIO Environment Initialization**
  - **DoD File:** `platformio.ini` exists.
  - **DoD Command:** `grep -q "esp32-s3-devkitc-1" platformio.ini` exits 0.

- **P2-S3: Initial DSP Module Prototype (~20% Milestone)**
  - **DoD File:** `tests/test_p2_s3_dsp.py` exists.
  - **DoD Command:** `pytest tests/test_p2_s3_dsp.py` exits 0 (Verifies the mathematical correctness of the audio windowing/spectrogram logic).

## ▲ Phase 3: Review III (Progress Review and 30% Completion - 10 Marks)
*Expected Outcome: Refined requirements/design, early testing of module.*
- **P3-S1: Embedded C++ DSP Porting**
  - **DoD File:** `include/dsp_pipeline.h` exists.
  - **DoD Command:** `pio test -e native -f test_dsp` exits 0.

- **P3-S2: Initial CNN Model Architecture Prototyping**
  - **DoD File:** `scripts/train_model.py` exists.
  - **DoD Command:** `python scripts/train_model.py --dry-run` exits 0.

## ▲ Phase 4: Review IV (Core Functionality - 50% Completion - 15 Marks)
*Expected Outcome: Major modules implemented and integrated.*
- **P4-S1: TFLite Micro Quantized Export**
  - **DoD File:** `model/leak_model_int8.tflite` exists.
  - **DoD Command:** `test -s model/leak_model_int8.tflite` exits 0.

- **P4-S2: Edge Inference Integration on ESP32**
  - **DoD File:** `src/inference.cpp` exists.
  - **DoD Command:** `pio run -e esp32-s3-devkitc-1` exits 0.

--- SUBMITTABLE ---

## Phase 5: Review V (Integrated Prototype & 80% Validation - 25 Marks)
*Expected Outcome: Integrate planned modules, test functionality.*
- **P5-S1: Hardware Relay Actuation Integration**
  - **DoD File:** `src/actuation.cpp` exists.
  - **DoD Command:** `grep -q "digitalWrite" src/actuation.cpp` exits 0.

## Phase 6: Review VI (Open House - 15 Marks)
*Expected Outcome: Fully functional prototype demonstrated.*
- **P6-S1: Dual-Node GCC-PHAT Localization & Telemetry**
  - **DoD File:** `src/localization.cpp` exists.
  - **DoD Test:** `pytest tests/test_p6_s1_gcc.py` exits 0.

## Phase 7: Final Report Submission (10 Marks)
- **P7-S1: Comprehensive Project Report**
  - **DoD File:** `docs/Final_Report.pdf` exists.
