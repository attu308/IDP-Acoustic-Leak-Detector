# PLAN.md - Smart Acoustic Leak Detector Contract

## ▲ Phase 0: Review II Initial Deliverables
- **P0-S1: Presentation Slides Markdown**
  - **DoD File:** `presentation/slides.md` exists.
  - **DoD Command:** `grep -q "Agenda" presentation/slides.md` exits 0.

- **P0-S2: PlatformIO Environment Initialization**
  - **DoD File:** `platformio.ini` exists.
  - **DoD Command:** `grep -q "esp32-s3-devkitc-1" platformio.ini` exits 0.

## ▲ Phase 1: Digital Signal Processing (DSP) Pipeline
- **P1-S1: Python DSP Baseline Simulation**
  - **DoD File:** `tests/test_p1_s1.py` exists.
  - **DoD Test:** `pytest tests/test_p1_s1.py` passes (verifies spectrogram matrix dimensions).

- **P1-S2: C++ Embedded DSP Header Generation**
  - **DoD File:** `include/dsp_pipeline.h` exists.
  - **DoD Command:** `cat include/dsp_pipeline.h | grep -q "fft"` exits 0.

- **P1-S3: DSP C++ Unit Test (Native Environment)**
  - **DoD File:** `test/test_dsp/test_dsp.cpp` exists.
  - **DoD Command:** `pio test -e native -f test_dsp` exits 0.

## ▲ Phase 2: TinyML Edge Architecture
- **P2-S1: Model Training Pipeline**
  - **DoD File:** `scripts/train_model.py` exists.
  - **DoD Command:** `python scripts/train_model.py --dry-run` exits 0.

- **P2-S2: TFLite Micro Quantized Export**
  - **DoD File:** `model/leak_model_int8.tflite` exists.
  - **DoD Command:** `test -s model/leak_model_int8.tflite` exits 0 (file is not empty).

--- SUBMITTABLE ---

## Phase 3: Hardware Integration & Actuation (Upside)
- **P3-S1: Actuation Relay Logic**
  - **DoD File:** `src/actuation.cpp` exists.
  - **DoD Command:** `pio run -e esp32-s3-devkitc-1` exits 0 (firmware compiles).

## Phase 4: Dual-Node GCC-PHAT Localization (Upside)
- **P4-S1: Cross-Correlation Mathematical Baseline**
  - **DoD Test:** `pytest tests/test_p4_s1.py` passes (verifies exact $\Delta t$ extraction from continuous noise).
