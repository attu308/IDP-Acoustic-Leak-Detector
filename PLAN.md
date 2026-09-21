# PLAN.md - Smart Acoustic Leak Detector Contract

## Phase 1: Review I (Problem Identification and Planning - 5 Marks)
*Note: This phase represents past academic milestones. Superseded by Review II.*
- **P1-S1: Project Definition & Ideation**
  - **DoD File:** `idea.md` exists.
  - **DoD Command:** `test -s idea.md` exits 0.

## ▲ Phase 2: Review II (Initial Design and 20% Development - 20 Marks)
- **P2-S1: Review II PPT / Presentation Slides Content**
  - **DoD File:** `presentation/review2_slides.md` exists.
  - **DoD Command:** `grep -q "Architecture" presentation/review2_slides.md` exits 0.

- **P2-S2: PlatformIO Environment Initialization**
  - **DoD File:** `platformio.ini` exists.
  - **DoD Command:** `grep -q "esp32-s3-devkitc-1" platformio.ini` exits 0.

- **P2-S3: Initial DSP Module Prototype (~20% Milestone)**
  - **DoD File:** `tests/test_p2_s3_dsp.py` exists.
  - **DoD Command:** `pytest tests/test_p2_s3_dsp.py` exits 0.

## ▲ Phase 3: Review III (Progress Review and 30% Completion - 10 Marks)
- **P3-S1: Review III PPT / Presentation Slides Content**
  - **DoD File:** `presentation/review3_slides.md` exists.
  - **DoD Command:** `test -s presentation/review3_slides.md` exits 0.

- **P3-S2: Embedded C++ DSP Porting**
  - **DoD File:** `include/dsp_pipeline.h` exists.
  - **DoD Command:** `pio test -e native -f test_dsp` exits 0.

- **P3-S3: Initial CNN Model Architecture Prototyping**
  - **DoD File:** `scripts/train_model.py` exists.
  - **DoD Command:** `python scripts/train_model.py --dry-run` exits 0.

## ▲ Phase 4: Review IV (Core Functionality - 50% Completion - 15 Marks)
- **P4-S1: Review IV PPT / Presentation Slides Content**
  - **DoD File:** `presentation/review4_slides.md` exists.
  - **DoD Command:** `test -s presentation/review4_slides.md` exits 0.

- **P4-S2: TFLite Micro Quantized Export**
  - **DoD File:** `model/leak_model_int8.tflite` exists.
  - **DoD Command:** `test -s model/leak_model_int8.tflite` exits 0.

- **P4-S3: Edge Inference Integration on ESP32**
  - **DoD File:** `src/inference.cpp` exists.
  - **DoD Command:** `pio run -e esp32-s3-devkitc-1` exits 0.

--- SUBMITTABLE ---

## Phase 5: Review V (Integrated Prototype & 80% Validation - 25 Marks)
- **P5-S1: Review V PPT / Presentation Slides Content**
  - **DoD File:** `presentation/review5_slides.md` exists.
  - **DoD Command:** `test -s presentation/review5_slides.md` exits 0.

- **P5-S2: Hardware Relay Actuation Integration**
  - **DoD File:** `src/actuation.cpp` exists.
  - **DoD Command:** `grep -q "digitalWrite" src/actuation.cpp` exits 0.

## Phase 6: Review VI (Open House - 15 Marks)
- **P6-S1: Review VI PPT / Presentation Slides Content**
  - **DoD File:** `presentation/review6_slides.md` exists.
  - **DoD Command:** `test -s presentation/review6_slides.md` exits 0.

- **P6-S2: Dual-Node GCC-PHAT Localization & Telemetry**
  - **DoD File:** `src/localization.cpp` exists.
  - **DoD Test:** `pytest tests/test_p6_s2_gcc.py` exits 0.

## Phase 7: Final Report Submission (10 Marks)
- **P7-S1: Comprehensive Project Report**
  - **DoD File:** `docs/Final_Report.pdf` exists.
  - **DoD Command:** `test -s docs/Final_Report.pdf` exits 0.
