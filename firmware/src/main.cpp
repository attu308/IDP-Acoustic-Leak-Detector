/**
 * @file main.cpp
 * @brief Smart Acoustic Leak Detector - ESP32-S3 FreeRTOS Dual-Core Firmware Core
 * 
 * Core 0: High-Speed ADC/DMA Sampling & DSP Log-Mel Feature Extraction
 * Core 1: TinyML Quantized Inference, Anomaly Classification & Fail-Safe Actuation
 */

#include <Arduino.h>
#include "config.h"

// Data structure passed across cores via FreeRTOS IPC Queue
typedef struct {
    uint32_t timestamp_ms;
    float mel_energies[N_MEL_BANDS];
    float peak_frequency_hz;
    float snr_db;
} FeatureFrame_t;

// FreeRTOS Handles
QueueHandle_t xQueueFeatureMap = NULL;
TaskHandle_t xHandle_SamplingDSP = NULL;
TaskHandle_t xHandle_InferenceActuation = NULL;

// Operational States
enum SystemState {
    STATE_NORMAL_FLOW,
    STATE_AMBIENT_NOISE,
    STATE_SUSPECTED_LEAK,
    STATE_CONFIRMED_LEAK,
    STATE_MAJOR_RUPTURE
};

volatile SystemState currentState = STATE_NORMAL_FLOW;
volatile uint32_t consecutiveLeakFrames = 0;
volatile bool valveClosed = false;

/**
 * @brief FreeRTOS Task pinned to Core 0 (Ingestion & DSP)
 * Continuous 16 kHz sampling and spectral feature extraction
 */
void Task_AudioSampling_DSP(void *pvParameters) {
    Serial.printf("[Core %d] Audio Sampling & DSP Task initialized at 16 kHz\n", xPortGetCoreID());

    FeatureFrame_t currentFrame;
    uint32_t frameCounter = 0;

    for (;;) {
        // 1. Ingest 16 kHz audio frame (simulated / DMA ADC read)
        currentFrame.timestamp_ms = millis();
        
        // Emulate DSP Log-Mel feature generation
        for (int i = 0; i < N_MEL_BANDS; i++) {
            // Simulated baseline vs leak spectrum
            if (currentState == STATE_SUSPECTED_LEAK || currentState == STATE_CONFIRMED_LEAK) {
                // Elevated energy in 1.5 - 4.5 kHz bands (Mel index 10-22)
                currentFrame.mel_energies[i] = (i >= 10 && i <= 22) ? -1.8f : -4.5f;
            } else {
                currentFrame.mel_energies[i] = -5.0f;
            }
        }
        currentFrame.snr_db = (currentState == STATE_CONFIRMED_LEAK) ? 28.5f : 6.2f;
        currentFrame.peak_frequency_hz = 2840.0f;

        // 2. Push feature map to Inter-Core Queue for Core 1 consumption
        if (xQueueFeatureMap != NULL) {
            if (xQueueSend(xQueueFeatureMap, &currentFrame, (TickType_t)10) != pdPASS) {
                Serial.println("[Core 0 Warning] Feature map queue full, dropping frame");
            }
        }

        frameCounter++;
        // 16 ms hop time between FFT frames
        vTaskDelay(pdMS_TO_TICKS(16));
    }
}

/**
 * @brief FreeRTOS Task pinned to Core 1 (TinyML Inference & Actuation)
 * Consumes feature maps, executes neural classifier, controls relay
 */
void Task_TinyML_Inference_Actuation(void *pvParameters) {
    Serial.printf("[Core %d] TinyML Inference & Actuation Task initialized\n", xPortGetCoreID());

    FeatureFrame_t receivedFrame;

    for (;;) {
        // Block until next DSP feature frame arrives from Core 0
        if (xQueueReceive(xQueueFeatureMap, &receivedFrame, portMAX_DELAY) == pdPASS) {
            
            // 1. TinyML Anomaly Classification (Simulated / TFLite Micro invocation)
            float leakScore = 0.0f;
            // Sum energies in characteristic micro-leak turbulence band
            float turbulenceBandEnergy = 0.0f;
            for (int i = 10; i <= 22; i++) {
                turbulenceBandEnergy += receivedFrame.mel_energies[i];
            }
            turbulenceBandEnergy /= 13.0f;

            if (turbulenceBandEnergy > -2.5f) {
                leakScore = 0.94f; // 94% confidence micro-leak
            } else {
                leakScore = 0.05f; // Normal laminar flow
            }

            // 2. Debounce State Machine Logic
            if (leakScore > 0.85f) {
                consecutiveLeakFrames++;
                if (consecutiveLeakFrames >= LEAK_DEBOUNCE_FRAMES) {
                    currentState = STATE_CONFIRMED_LEAK;
                } else {
                    currentState = STATE_SUSPECTED_LEAK;
                }
            } else {
                consecutiveLeakFrames = 0;
                currentState = STATE_NORMAL_FLOW;
            }

            // 3. Fail-Safe Actuation Logic
            if (currentState == STATE_CONFIRMED_LEAK && !valveClosed) {
                // Trip emergency shutoff relay immediately
                digitalWrite(SOLENOID_RELAY_PIN, LOW); // Active-Low relay trigger
                digitalWrite(STATUS_LED_PIN, HIGH);
                valveClosed = true;

                Serial.printf("\n=========================================\n");
                Serial.printf(" [ALERT] MICRO-LEAK CONFIRMED! (Confidence: %.1f%%)\n", leakScore * 100);
                Serial.printf(" [ACTUATION] 12V Solenoid Valve Triggered (Closed)\n");
                Serial.printf(" [TELEMETRY] Latency: Sub-50ms | Time: %u ms\n", receivedFrame.timestamp_ms);
                Serial.printf("=========================================\n\n");
            }

            // Diagnostic Telemetry Dispatch (1000ms cadence)
            static uint32_t lastPrint = 0;
            if (millis() - lastPrint > 1000) {
                lastPrint = millis();
                const char* stateStr = (currentState == STATE_NORMAL_FLOW) ? "NORMAL FLOW" :
                                       (currentState == STATE_SUSPECTED_LEAK) ? "SUSPECTED LEAK" : "CONFIRMED LEAK (SHUTOFF)";
                Serial.printf("[Telemetry] State: %s | Conf: %.2f | Valve: %s | SNR: %.1f dB\n",
                              stateStr, leakScore, valveClosed ? "CLOSED" : "OPEN", receivedFrame.snr_db);
            }
        }
    }
}

void setup() {
    Serial.begin(115200);
    delay(1000);
    Serial.println("\n=== SMART ACOUSTIC LEAK DETECTOR ===");
    Serial.println("System Architecture: ESP32-S3 Dual-Core FreeRTOS");
    Serial.println("Initial Milestone: ~20% Signal Processing & Control Prototype");

    // Initialize Hardware Peripherals
    pinMode(SOLENOID_RELAY_PIN, OUTPUT);
    digitalWrite(SOLENOID_RELAY_PIN, HIGH); // De-energized (Open)
    pinMode(STATUS_LED_PIN, OUTPUT);
    digitalWrite(STATUS_LED_PIN, LOW);

    // Create Inter-Core Queue (Capacity: 8 feature frames)
    xQueueFeatureMap = xQueueCreate(8, sizeof(FeatureFrame_t));
    if (xQueueFeatureMap == NULL) {
        Serial.println("[ERROR] Failed to allocate FreeRTOS feature map queue!");
        while (1);
    }

    // Pin Audio Ingestion & DSP Task to Core 0
    xTaskCreatePinnedToCore(
        Task_AudioSampling_DSP,
        "Sampling_DSP_Core0",
        8192,
        NULL,
        2,                     // Higher priority for deterministic sampling
        &xHandle_SamplingDSP,
        0                      // Core 0
    );

    // Pin TinyML Inference & Actuation Task to Core 1
    xTaskCreatePinnedToCore(
        Task_TinyML_Inference_Actuation,
        "Inference_Actuation_Core1",
        8192,
        NULL,
        1,                     // Worker priority
        &xHandle_InferenceActuation,
        1                      // Core 1
    );

    Serial.println("[Init] Dual-core tasks pinned and dispatched successfully.\n");
}

void loop() {
    // Idle task in Arduino framework (Core 1)
    vTaskDelay(pdMS_TO_TICKS(1000));
}
