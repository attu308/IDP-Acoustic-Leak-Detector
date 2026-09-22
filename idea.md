# Smart Acoustic Leak Detector: Acoustic-Vibrational Micro-Leak and Infrastructure Integrity Monitor

---

## Executive Summary

Unaccounted-for water loss within municipal distribution networks and building plumbing structures—known as Non-Revenue Water (NRW)—presents a severe sustainability and infrastructure integrity challenge. Micro-leaks occurring in pressurized pipelines often remain undetected until structural damage or severe fluid losses manifest.

This project details the design and deployment of an Edge AI (TinyML) smart sensor system engineered to clamp onto municipal or commercial piping. By performing localized digital signal processing (DSP) and running an 8-bit quantized Convolutional Neural Network (CNN) directly on a low-power, dual-core microcontroller (ESP32-S3), the system classifies structural micro-leak acoustic signatures in sub-200 millisecond timeframes. This eliminates the need for streaming raw audio to cloud servers, vastly reducing bandwidth and power consumption. For multi-node setups, Generalized Cross-Correlation with Phase Transform (GCC-PHAT) is used to calculate the time delay of continuous leak turbulence, isolating precise leak coordinates and triggering local isolation valves autonomously.

---

## 1. Literature Survey, Research Gap & Requirements Analysis

### 1.1 Literature Survey & Baseline Systems
1. **Acoustic Wave Propagation in Plastic Pipes (Hunaidi & Chu, 1999):**
   * *Citation:* O. Hunaidi & W. T. Chu, *"Acoustical characteristics of leak signals in plastic water distribution pipes"*, Applied Acoustics, Vol. 58, No. 3, pp. 235–254. DOI: [10.1016/S0003-682X(99)00013-4](https://doi.org/10.1016/S0003-682X(99)00013-4).
   * *Key Finding:* Proved that acoustic leak signals in PVC pipes concentrate within the 1 kHz to 5 kHz band, while frequencies above 2 kHz suffer rapid structural attenuation over distance.
   * *Limitation:* Focused on offline manual cross-correlation using bulky PC-based laboratory instruments; lacks real-time embedded edge intelligence.
2. **SCADA District Metered Area (DMA) Flow-Balance (Eliades & Polycarpou, 2012):**
   * *Citation:* D. G. Eliades & M. M. Polycarpou, *"Leakage Fault Detection in a District Metered Area of a Water Distribution System"*, Water Resources Management, Vol. 29, No. 10, pp. 3843–3860. DOI: [10.1007/s11269-015-1066-z](https://doi.org/10.1007/s11269-015-1066-z).
   * *Key Finding:* Demonstrates boundary inflow/outflow balance monitoring using statistical cumulative sum (CUSUM) algorithms across municipal network sectors.
   * *Limitation:* Macroscopic scope: reliably detects only catastrophic burst anomalies (>10–15% volumetric drops) and is blind to localized weeping micro-cracks (<1 L/min).
3. **Time–Frequency Deep Learning for Acoustic Leak Detection (Kang et al., 2021 & IEEE Sensors 2026):**
   * *Citation:* J. Kang et al., *"Leakage detection in water distribution systems based on time–frequency convolutional neural network"*, Measurement, Vol. 186, 110094. DOI: [10.1016/j.measurement.2021.110094](https://doi.org/10.1016/j.measurement.2021.110094); and *"ATT-LCNN: Lightweight CNN for Pipeline Leak Detection"*, IEEE Sensors Journal, DOI: [10.1109/JSEN.2026.3609802](https://doi.org/10.1109/JSEN.2026.3609802).
   * *Key Finding:* Converts structural vibration signals into 2D time-frequency spectrograms, leveraging CNN spatial feature extraction for high classification accuracy (>92%).
   * *Limitation:* Designed for high-power GPU workstations streaming continuous audio to cloud servers; no sub-watt TinyML microcontroller deployment (e.g. ESP32-S3), int8 quantization, or direct valve actuation.
4. **Institutional Non-Revenue Water (NRW) Baselines:**
   * *World Bank Sector Report No. 8 (Kingdom et al.):* Establishes that >32 billion m³ of treated drinking water leaks from municipal networks worldwide annually (>US$14 billion annual loss). [Report Link](https://documents.worldbank.org/en/publication/documents-reports/documentdetail/659421468162125557).
   * *NITI Aayog Composite Water Management Index (CWMI):* Documents that approximately 40% of piped water in Indian urban supply systems is lost to distribution leaks. [Report Link](https://www.niti.gov.in/report-and-publication).

### 1.2 The Research Gap
There is a distinct lack of an **ultra-low-cost (<₹2,500), non-invasive, autonomous Edge AI classifier** that can detect micro-leaks, isolate faults via mechanical actuation, and operate independently of continuous cloud connectivity. 

### 1.3 Engineering Requirements (Review II Rubric Alignment)
* **Functional Requirements:** Real-time continuous acoustic sampling (16 kHz); sub-200ms anomaly classification; automated GPIO relay triggering for solenoid shutoff; lightweight MQTT telemetry alerts.
* **Non-Functional Requirements:** Sub-watt power envelope (<500 mW active inference); >90% classification precision; False Positive Rate (FPR) < 5%.
* **Physical Constraints:** Adaptable to 0.5"–2" pipe diameters; functional in 2–6 bar fluid pressure environments.

---

## 2. Project Objectives and Scope

### 2.1 Key Objectives
1. **Hardware Engineering:** Develop a clamp-on structural vibration sensing node utilizing contact piezoelectric transducers and analog signal conditioning.
2. **Embedded DSP Pipeline:** Implement onboard DSP to convert raw time-domain waveforms into Log-Mel Spectrograms tailored for industrial high-frequency turbulence (rather than human speech).
3. **TinyML Edge Classifier:** Train, quantize (int8), and deploy a CNN onto the ESP32-S3 using TFLite Micro, emphasizing memory profiling (SRAM/PSRAM) and hardware-accelerated vector instructions (ESP-NN).
4. **Leak Localization:** Implement continuous-signal GCC-PHAT cross-correlation mathematics for dual-node distance calculation.
5. **Autonomous Actuation:** Interface a GPIO relay to trigger a 12V motorized solenoid valve upon verified leak detection.

### 2.2 Scope Boundaries
* **In-Scope:** Benchtop hydraulic loop testing (PVC pipes), Edge ML pipeline execution, relay actuation, Wi-Fi/MQTT alert payloads.
* **Out-of-Scope:** Large-scale underground trenching, chemical water contamination analysis.

---

## 3. System Architecture & Component Justification

### 3.1 Tiered System Architecture
The software architecture is designed around the FreeRTOS capabilities of the ESP32-S3 to ensure real-time Computer Science rigor:
* **Core 0 (Data Ingestion & DSP):** Handles hardware interrupts, ADC sampling via Direct Memory Access (DMA), Hanning windowing, and FFT computations.
* **Core 1 (AI Inference & Control):** Consumes the DSP feature maps, executes the quantized TFLite Micro neural network, manages the relay state machine, and dispatches MQTT telemetry payloads.

### 3.2 Component Trade-Off & Technical Justification
| Component Category | Selected Hardware | Justification vs. Alternatives |
| :--- | :--- | :--- |
| **Microcontroller** | **ESP32-S3** | **Vs. Raspberry Pi 4:** RPi is too power-hungry, expensive, and runs a heavy Linux OS. **Vs. Arduino Uno:** Uno lacks SRAM and FPU required for CNN inference. ESP32-S3 provides dual-core processing, vector extensions, and Wi-Fi for <₹650. |
| **Acoustic Sensor** | **Contact Piezoelectric Disc** | **Vs. Digital MEMS (INMP441):** Airborne MEMS suffer from acoustic impedance mismatch when clamped to pipes, picking up ambient room noise. Piezo elements directly couple to structural pipe vibrations. |
| **Signal Conditioning** | **LM358 Active Charge Amp/Filter** | Essential for converting the high-impedance analog piezo signal into a clean, low-frequency-filtered (high-pass >500 Hz) analog voltage for the ESP32 ADC. |

### 3.3 Estimated Bill of Materials (BOM)
* **ESP32-S3 Dev Board:** ₹650
* **Piezoelectric Transducer + LM358 Circuit:** ₹300
* **5V Relay + 12V Solenoid Valve:** ₹450
* **Power (18650 Battery + TP4056):** ₹250
* **3D-Printed Clamp Housing:** ₹150
* **Total Cost per Node:** **~₹1,800** (Vastly cheaper than commercial ₹1,00,000+ loggers).

---

## 4. Digital Signal Processing (DSP) Pipeline

Raw acoustic waveforms contain phase noise and baseline fluctuations. We transform these into 2D spectro-temporal matrices suitable for CNNs. Unlike voice-recognition systems that use standard MFCCs (tuned to human hearing), this system utilizes **Log-Mel Spectrograms** scaled for industrial turbulence frequencies (1 kHz - 8 kHz).

```
Piezo Analog Signal ---> High-Pass Filter (>500 Hz) ---> ESP32 ADC (16 kHz) ---> Hanning Window (1000 ms) ---> FFT ---> Log-Filter Bank Conversion ---> 2D Spectrogram Matrix
```

### 4.1 Frame Windowing and FFT
Continuous audio is divided into overlapping frames using a Hanning window function $w(n)$ to reduce spectral leakage:
$$E(f, t) = \left\vert{} \sum_{n=0}^{N-1} x(n+t) \cdot w(n) \cdot e^{-j \frac{2\pi f n}{N}} \right\vert{}^2$$

---

## 5. Machine Learning Architecture & Quantization

### 5.1 1D/2D CNN Topology
The network architecture balances high-accuracy feature extraction with strict SRAM limitations:
* **Input:** Log-Spectrogram Feature Matrix.
* **Conv Layers:** Two layers of Convolution + ReLU Activation + Max Pooling.
* **Global Average Pooling:** Flattens dimensions to prevent overfitting and reduce parameter count.
* **Output (Softmax):** 4 Classes: *Normal Flow, Background Noise, Micro-Leak, Major Rupture*.

### 5.2 Model Quantization (TinyML Focus)
To execute on memory-constrained hardware, the model undergoes **Post-Training Quantization (PTQ)**. Floating-point weights (fp32) are mapped to 8-bit integers (int8). This reduces the memory footprint by ~75% and utilizes the ESP32-S3's vector instructions for faster Multiply-Accumulate (MAC) operations, maintaining >90% accuracy while dropping inference time below 200ms.

---

## 6. Leak Localization Mathematics: GCC-PHAT

Because pressurized leaks produce *continuous broadband turbulence* (hissing) rather than a single sharp click, naive time-of-arrival timestamp subtraction (via NTP/Wi-Fi) is physically invalid given the high speed of sound in water (~1480 m/s). 

Instead, the system utilizes **Generalized Cross-Correlation with Phase Transform (GCC-PHAT)** between two sensor nodes (A and B) separated by distance $L$.

### 6.1 Derivation
The cross-correlation function computes the similarity of the two continuous signals as a function of the time lag $\tau$:
$$ R_{AB}(\tau) = \int_{-\infty}^{\infty} \frac{X_A(f)X_B^*(f)}{\left\vert X_A(f)X_B^*(f) \right\vert} e^{j2\pi f \tau} df $$
The time delay $\Delta t$ corresponds to the argmax of $R_{AB}(\tau)$.
Once the phase delay $\Delta t$ is computed, the exact distance from Node A ($d_1$) is calculated as:
$$d_1 = \frac{L - (v_s \cdot \Delta t)}{2}$$
*(Note: Implementation requires physical clock synchronization or wired triggering between nodes to prevent microsecond drift).*

---

## 7. Execution Roadmap & Team Responsibilities

### 7.1 Demonstrable Review II Milestone (~20% Completion)
To satisfy the Review II rubric requirements, the immediate physical deliverable is the **Single-Node AI Core**:
1. Live acoustic/vibration sampling via the sensor and microcontroller.
2. Real-time generation of the DSP Spectrogram matrix on the ESP32.
3. Execution of the pre-trained, int8-quantized neural network classifying operational states via the serial monitor.

### 7.2 Team Roles & Division of Work
* **Member 1 (Embedded DSP & Hardware):** Piezo circuit design, ESP32 ADC DMA configuration, FreeRTOS Core 0 programming, and FFT optimization.
* **Member 2 (TinyML & Data Engineering):** Dataset curation, CNN architecture design, Edge Impulse training, int8 quantization, and memory profiling.
* **Member 3 (Systems Architecture & Actuation):** Relay/Solenoid state machine, MQTT telemetry payload design, Wi-Fi networking, and TDOA mathematical validation.

---

## 8. Expected Outcomes & Performance Metrics
* **Cost Envelope:** Total hardware build cost under ₹2,000 per node pair.
* **Classification Accuracy:** $>90\%$ true-positive detection rate for structural micro-leaks.
* **Inference Latency:** Sub-200 millisecond execution on Edge.
* **Bandwidth Optimization:** $>99\%$ data reduction compared to cloud audio streaming.
* **Autonomous Mitigation:** Relay isolation valve closure within 1 second of confirmed leak verification.