# Review II Technical Defense & Panel Q&A Guide

**Course:** BACSE291 - Innovative Design Project (AY 2026–2027)  
**Milestone:** Review II (Initial Design & 20% Prototype - 20 Marks)  
**Target Date:** 23 September 2026 (11:45 AM – 01:30 PM)  
**Duration:** Strictly 10 minutes total (6 mins presentation + 4 mins panel Q&A)

---

## 1. 10-Minute Presentation Run-Order & Slide Timing

| Slide # | Slide Title | Recommended Speaker | Target Time | Core Message / Takeaway |
| :---: | :--- | :---: | :---: | :--- |
| **1** | Title Slide | Member 1 | 0:30 min | Team intro, project scope, guide acknowledgement. |
| **2** | Agenda | Member 1 | 0:30 min | Roadmap of presentation. |
| **3** | Introduction & Problem Statement | Member 2 | 0:45 min | Non-Revenue Water (30-50% loss), micro-leak damage, limitations of manual patrols. |
| **4** | Literature Survey | Member 2 | 0:45 min | Hunaidi et al. acoustic propagation, SCADA mass-balance limits, cloud logger costs. |
| **5** | Challenges & Research Gap | Member 3 | 0:45 min | Bandwidth bottlenecks (1.2 GB/day), acoustic impedance, bridging the ₹1,00,000 cost gap. |
| **6** | Project Objectives & Scope | Member 3 | 0:45 min | 5 concrete deliverables (Piezo sensing, DSP Log-Mel, Int8 TinyML, 12V actuation, MQTT). |
| **7** | Proposed Methodology & Architecture | Member 1 | 1:15 min | FreeRTOS Core 0 vs Core 1 task segregation, hardware trade-offs (ESP32-S3 vs RPi). |
| **8** | Results / ~20% Initial Implementation | All Members | 1:00 min | Live demo of acoustic ingestion, spectrogram feature extraction, relay actuation loop. |
| **Q&A** | **Panel Question & Answer Defense** | **Designated per domain** | **4:00 min** | Direct, technically rigorous responses (see Section 3). |

---

## 2. Work Breakdown Structure & Individual Ownership Matrix

*Evaluated under Rubric 6 (Teamwork - 3 Marks) and Rubric 7 (Individual Contribution - 2 Marks).*

| Team Role | Technical Domain | Assigned Responsibilities | Primary Defense Topics |
| :--- | :--- | :--- | :--- |
| **Member 1** | **Embedded Systems & Firmware Architecture** | • ESP32-S3 FreeRTOS dual-core task architecture.<br>• I2S/ADC DMA audio buffer management.<br>• Hardware relay and solenoid valve circuit integration.<br>• Memory budgeting (SRAM vs PSRAM). | FreeRTOS task prioritization, DMA ring buffers, interrupt handling, fail-safe actuation. |
| **Member 2** | **Digital Signal Processing (DSP) & Math** | • Piezo sensor conditioning circuit (charge amp + HPF >500 Hz).<br>• Hanning window framing and 512-pt FFT engine.<br>• Log-Mel filterbank computation for 1–8 kHz turbulence.<br>• GCC-PHAT cross-correlation mathematics. | Acoustic wave speed in PVC/water, SNR optimization, Mel-scale vs speech MFCCs, phase correlation. |
| **Member 3** | **TinyML Engineering & Systems Integration** | • Synthetic & empirical acoustic dataset curation.<br>• 1D/2D CNN topology design and training.<br>• Post-Training Quantization (fp32 to int8) via TFLite Micro.<br>• MQTT telemetry payload design and Wi-Fi state machine. | Quantization error (<1%), MAC operations, inference latency (<200ms), tensor arena sizing. |

---

## 3. Top 10 Anticipated Panel "Grill" Questions & Model Answers

### Q1: "Why did you choose a contact Piezoelectric transducer instead of an I2S digital MEMS microphone like INMP441?"
> **Model Answer (Member 2):**  
> *"Airborne digital MEMS microphones have an acoustic port open to the air, creating a severe acoustic impedance mismatch when clamped to the exterior of a pipe. Airborne microphones pick up background ambient noise—such as human speech, HVAC systems, and room reverberation—far louder than the internal fluid vibrations. A contact piezoelectric ceramic transducer mechanically couples directly to the pipe substrate, picking up structural wall vibrations while naturally rejecting airborne room noise. Furthermore, the analog piezo signal allows us to implement a hardware active high-pass filter (>500 Hz) using an LM358 before sampling, completely removing 50 Hz electrical mains hum and structural building rumble."*

---

### Q2: "Sound in water travels at ~1,480 m/s. Over a 10-meter pipe, that's only 6.7 milliseconds. How can microcontrollers possibly measure this without being thrown off by network jitter?"
> **Model Answer (Member 2 / Member 1):**  
> *"We explicitly do not rely on Wi-Fi Network Time Protocol (NTP) timestamp subtraction, because Wi-Fi network jitter is 10 to 50 milliseconds, which exceeds the entire transit time across the pipe. Furthermore, a pressurized micro-leak produces continuous broadband turbulence (hissing) rather than a single sharp impulse. Therefore, for multi-node localization, we use **Generalized Cross-Correlation with Phase Transform (GCC-PHAT)** across simultaneous synchronized vibration recordings. For Review II, our demonstrable focus is single-node high-precision anomaly classification. Dual-node cross-correlation will use a physical synchronization trigger in Phase 6."*

---

### Q3: "Why use Edge AI (TinyML) on an ESP32 instead of just streaming the audio to AWS or Azure IoT for cloud processing?"
> **Model Answer (Member 3):**  
> *"Streaming continuous 16 kHz 16-bit audio generates approximately 1.1 to 1.3 GB of data per sensor node per day. Across an apartment complex or municipal sector with 50 pipes, that requires over 60 GB of continuous bandwidth daily, incurring substantial cloud compute and cellular charges. More critically, cloud streaming introduces network round-trip latency (1–3 seconds) and fails completely during network dropouts. If a major pipe rupture occurs during an internet failure, a cloud-dependent system cannot stop flooding. Our TinyML node performs local inference in under 200 ms and triggers a physical shutoff valve autonomously without needing an active internet connection."*

---

### Q4: "Why did you select the ESP32-S3 over a Raspberry Pi 4 or an Arduino Uno?"
> **Model Answer (Member 1):**  
> *"It comes down to power, unit cost, and computational suitability:  
> • **Vs. Arduino Uno:** An Uno runs at 16 MHz with only 2 KB of SRAM. It cannot store a single 1000ms audio buffer, let alone compute an FFT or run neural network weights.  
> • **Vs. Raspberry Pi 4:** A Raspberry Pi costs ₹4,500+, consumes 3 to 5 Watts of power, runs a full Linux OS with non-deterministic scheduling, and requires active cooling.  
> • **ESP32-S3:** Costs only ₹650, consumes under 500 mW, features dual Xtensa LX7 cores running at 240 MHz, includes specialized vector instructions (ESP-NN) for hardware-accelerated integer multiply-accumulate operations, and has 512 KB SRAM + 8 MB PSRAM, which is ideal for TFLite Micro."*

---

### Q5: "The Mel scale was invented for human speech. Why are you using Log-Mel spectrograms for pipe vibrations?"
> **Model Answer (Member 2):**  
> *"Standard speech MFCCs apply a discrete cosine transform (DCT) that discards spatial/temporal frequency relationships, which hurts 2D convolutional networks. While the classic Mel-scale mimics human auditory non-linearities, turbulent fluid micro-leaks in pressurized PVC pipes exhibit acoustic energy primarily concentrated between 1 kHz and 5 kHz. We retain 2D Log-Mel / linear-band Spectrograms because 2D-CNNs can detect spatial harmonic patterns, turbulence broadband smearing, and baseline pump hum much more effectively than compressed 1D cepstral coefficients."*

---

### Q6: "How do you prevent false positives from someone tapping on the pipe or a pump turning on?"
> **Model Answer (Member 3 / Member 1):**  
> *"We employ a three-tier defense against false positives:  
> 1. **Multi-Class Training:** Our neural network is trained on four distinct classes: Normal Laminar Flow, Ambient Noise/Mechanical Taps, Micro-Leak, and Major Rupture. Mechanical taps have impulsive, high-crest time-domain signatures that differ distinctly from the stationary spectral envelope of continuous leak turbulence.  
> 2. **Temporal Window Debouncing:** The actuation state machine requires the classifier to register positive leak predictions across 3 consecutive 1-second frames before declaring a confirmed leak.  
> 3. **High-Pass Hardware Filtering:** Mechanical vibrations from building foundations or motor hum (<500 Hz) are filtered out in analog hardware before ADC ingestion."*

---

### Q7: "What is your memory budget on the ESP32-S3? Will the model and DSP fit in internal SRAM?"
> **Model Answer (Member 1 / Member 3):**  
> *"Yes. The ESP32-S3 has 512 KB of internal SRAM. Our memory budget is structured as follows:  
> • **Audio DMA Double Buffer:** 16,000 samples @ 16-bit = ~32 KB.  
> • **DSP FFT & Spectrogram Buffers:** ~16 KB.  
> • **TFLite Micro Tensor Arena:** ~48 KB (sufficient for an int8 quantized 2-layer CNN with 8 and 16 filters).  
> • **FreeRTOS Stack & System Heaps:** ~64 KB.  
> Total active SRAM footprint is under 160 KB, leaving over 300 KB of headroom without even needing to page into external PSRAM."*

---

### Q8: "How does the emergency solenoid valve fail-safe operate?"
> **Model Answer (Member 1):**  
> *"The solenoid valve is driven via an optoisolated 5V relay module connected to an active-low GPIO pin on the ESP32. We utilize a 'Normally Closed' (NC) or 'Normally Open' (NO) fail-safe depending on installation requirements. The actuation logic runs on FreeRTOS Core 1 as a dedicated high-priority control task. If a confirmed leak state is flagged by the classifier, the GPIO immediately toggles the relay in under 50 milliseconds, closing the valve. The system does not wait for an MQTT acknowledgement from the cloud to actuate."*

---

### Q9: "What constitutes your 20% completion milestone for Review II today?"
> **Model Answer (All Members):**  
> *"To satisfy the 20% milestone under Review II guidelines:  
> 1. **Signal Processing Core:** We have a working 16 kHz audio sampling and DSP pipeline that converts raw acoustic time-domain data into Log-Mel Spectrograms.  
> 2. **Empirical Differentiation:** We have validated that artificial micro-cracks produce distinct, quantifiable spectral energy shifts in the 1.5–4.2 kHz frequency band compared to laminar flow.  
> 3. **Embedded Software Architecture:** We have structured the FreeRTOS dual-core firmware scaffold on the ESP32-S3, isolating high-speed DMA ingestion on Core 0 and control/actuation on Core 1."*

---

### Q10: "How will you safely test this in the laboratory without flooding the lab or damaging college infrastructure?"
> **Model Answer (Member 1 / Member 2):**  
> *"We constructed a closed-loop benchtop hydraulic test rig using 1-inch Schedule 40 PVC piping connected to a small 12V DC recirculating water pump and a reservoir tank. Controlled micro-leaks are introduced using a high-precision needle valve, allowing us to simulate leak apertures from 0.5 mm to 3 mm at safe operational pressures (2 to 3 bar) with 100% water recovery back into the reservoir."*

---

## 4. Pre-Review Guide Approval Sign-Off Checklist
- [ ] Met faculty guide during scheduled Thursday/Friday slot.
- [ ] Demonstrated the 8-slide presentation deck.
- [ ] Explained the ~20% signal processing module and architecture diagram.
- [ ] Rehearsed 10-minute presentation with team members.
- [ ] Received formal guide approval to present to the School panel.
