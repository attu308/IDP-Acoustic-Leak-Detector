#pragma once

// Hardware Pin Mappings for ESP32-S3
#define PIEZO_ADC_PIN         4   // ADC1_CH3 for Contact Piezo Transducer
#define SOLENOID_RELAY_PIN    18  // Active-Low GPIO driving 5V optoisolated relay
#define STATUS_LED_PIN        2   // Onboard diagnostic LED

// Acoustic Sampling Parameters
#define SAMPLE_RATE_HZ        16000
#define FFT_LENGTH            512
#define HOP_LENGTH            256
#define N_MEL_BANDS           32

// Anomaly Detection Thresholds
#define LEAK_DEBOUNCE_FRAMES  3    // Consecutive positive frames required to trigger shutoff
#define INFERENCE_INTERVAL_MS 200  // Real-time evaluation cadence
