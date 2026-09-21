#!/usr/bin/env python3
"""
DSP Audio Feature Extraction Engine (~20% Prototype Core).
Converts 16 kHz structural acoustic waveforms into Log-Mel Spectrograms.
Designed for low-power edge execution and TinyML ingestion.
"""

import sys
import os
import math
import numpy as np

SAMPLE_RATE = 16000     # 16 kHz acoustic sampling
FRAME_SIZE = 512        # 32 ms window
HOP_SIZE = 256          # 16 ms hop (50% overlap)
N_MELS = 32             # 32 Mel filter bands
F_MIN = 500.0           # High-pass cutoff (removes 50Hz hum and low rumble)
F_MAX = 8000.0          # Nyquist limit for 16 kHz

def hz_to_mel(hz: float) -> float:
    return 2595.0 * math.log10(1.0 + hz / 700.0)

def mel_to_hz(mel: float) -> float:
    return 700.0 * (10.0 ** (mel / 2595.0) - 1.0)

def create_mel_filterbank(n_mels=N_MELS, n_fft=FRAME_SIZE, sr=SAMPLE_RATE, f_min=F_MIN, f_max=F_MAX):
    mel_min = hz_to_mel(f_min)
    mel_max = hz_to_mel(f_max)
    mel_points = np.linspace(mel_min, mel_max, n_mels + 2)
    hz_points = np.array([mel_to_hz(m) for m in mel_points])
    bin_points = np.floor((n_fft + 1) * hz_points / sr).astype(int)

    filters = np.zeros((n_mels, n_fft // 2 + 1))
    for i in range(1, n_mels + 1):
        left = bin_points[i - 1]
        center = bin_points[i]
        right = bin_points[i + 1]

        for k in range(left, center):
            if center > left:
                filters[i - 1, k] = (k - left) / (center - left)
        for k in range(center, right):
            if right > center:
                filters[i - 1, k] = (right - k) / (right - center)

    return filters

def high_pass_filter(signal: np.ndarray, cutoff=F_MIN, sr=SAMPLE_RATE) -> np.ndarray:
    """Simple 1st-order IIR high-pass filter mimicking analog RC stage (>500 Hz)."""
    rc = 1.0 / (2.0 * math.pi * cutoff)
    dt = 1.0 / sr
    alpha = rc / (rc + dt)
    filtered = np.zeros_like(signal)
    for i in range(1, len(signal)):
        filtered[i] = alpha * (filtered[i - 1] + signal[i] - signal[i - 1])
    return filtered

def compute_log_mel_spectrogram(signal: np.ndarray, sr=SAMPLE_RATE) -> np.ndarray:
    """Transforms 1-second raw waveform (16000 samples) into (Time x Mel) feature map."""
    # 1. Analog High-Pass Emulation
    filtered_signal = high_pass_filter(signal, cutoff=F_MIN, sr=sr)

    # 2. Windowing and Framing
    hanning_window = 0.5 * (1.0 - np.cos(2.0 * np.pi * np.arange(FRAME_SIZE) / (FRAME_SIZE - 1)))
    num_frames = (len(filtered_signal) - FRAME_SIZE) // HOP_SIZE + 1

    spectrogram_frames = []
    for f in range(num_frames):
        start = f * HOP_SIZE
        frame = filtered_signal[start : start + FRAME_SIZE] * hanning_window
        fft_complex = np.fft.rfft(frame, n=FRAME_SIZE)
        power_spectrum = (np.abs(fft_complex) ** 2) / FRAME_SIZE
        spectrogram_frames.append(power_spectrum)

    power_spectrogram = np.array(spectrogram_frames) # Shape: (num_frames, 257)

    # 3. Mel Filterbank Multiplication
    mel_filters = create_mel_filterbank(n_mels=N_MELS, n_fft=FRAME_SIZE, sr=sr, f_min=F_MIN, f_max=F_MAX)
    mel_energy = np.dot(power_spectrogram, mel_filters.T) # Shape: (num_frames, N_MELS)

    # 4. Log Compression
    log_mel = np.log10(np.maximum(mel_energy, 1e-6))
    return log_mel

def synthesize_test_signals(duration_sec=1.0, sr=SAMPLE_RATE):
    """
    Synthesize physical test acoustic regimes:
    1. Baseline: Laminar water flow (low freq noise) + slight electrical noise.
    2. Micro-Leak: Laminar water flow + sharp high-frequency turbulent hiss in 1.5–4.5 kHz band.
    """
    num_samples = int(duration_sec * sr)
    t = np.linspace(0, duration_sec, num_samples, endpoint=False)

    np.random.seed(42)
    # Low frequency laminar rumble (<800 Hz)
    laminar_flow = 0.15 * np.sin(2 * np.pi * 320 * t) + 0.1 * np.sin(2 * np.pi * 480 * t) + 0.05 * np.random.normal(0, 0.05, num_samples)

    # Baseline signal
    baseline_signal = laminar_flow + 0.02 * np.random.normal(0, 0.02, num_samples)

    # Micro-leak broadband turbulence centered at 2.5 kHz to 4.2 kHz
    turbulence_carrier = np.sin(2 * np.pi * 2800 * t) + np.sin(2 * np.pi * 3600 * t)
    turbulent_noise = 0.35 * np.random.normal(0, 0.3, num_samples) * (1.0 + 0.5 * turbulence_carrier)
    leak_signal = laminar_flow + turbulent_noise

    return baseline_signal, leak_signal

def run_self_test() -> bool:
    print("Running DSP Audio Feature Extraction Self-Test...")
    baseline, leak = synthesize_test_signals(duration_sec=1.0, sr=SAMPLE_RATE)

    spec_baseline = compute_log_mel_spectrogram(baseline, sr=SAMPLE_RATE)
    spec_leak = compute_log_mel_spectrogram(leak, sr=SAMPLE_RATE)

    print(f"Log-Mel Spectrogram Shape (Time x Mel): {spec_baseline.shape}")
    assert spec_baseline.shape[1] == N_MELS, f"Expected {N_MELS} mel bands, got {spec_baseline.shape[1]}"
    assert spec_baseline.shape[0] > 50, f"Expected >50 time frames, got {spec_baseline.shape[0]}"

    # Compare energy density in leak band (Mel bands 8 to 24 correspond roughly to 1.5 kHz to 4.5 kHz)
    leak_band_baseline_energy = np.mean(spec_baseline[:, 8:24])
    leak_band_leak_energy = np.mean(spec_leak[:, 8:24])

    energy_diff_db = leak_band_leak_energy - leak_band_baseline_energy
    print(f"Baseline Average Energy in Leak Band (Log): {leak_band_baseline_energy:.3f}")
    print(f"Leak Signal Average Energy in Leak Band (Log): {leak_band_leak_energy:.3f}")
    print(f"Turbulence Elevation: {energy_diff_db:.3f} log units (~{energy_diff_db*10:.1f} dB SNR elevation)")

    assert energy_diff_db > 0.5, "Failed: Leak turbulence energy did not sufficiently exceed baseline!"
    print("[PASS] DSP Feature Extraction Engine verified successfully!")
    return True

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        success = run_self_test()
        sys.exit(0 if success else 1)

    # If run standalone, run self-test and generate spectral comparison chart
    run_self_test()

    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt

        baseline, leak = synthesize_test_signals()
        spec_base = compute_log_mel_spectrogram(baseline)
        spec_leak = compute_log_mel_spectrogram(leak)

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4), dpi=200)
        im1 = ax1.imshow(spec_base.T, aspect='auto', origin='lower', cmap='inferno')
        ax1.set_title("Laminar Flow (Normal Baseline)")
        ax1.set_xlabel("Time Frames (16 ms)")
        ax1.set_ylabel("Mel Frequency Bands (0.5 - 8 kHz)")
        fig.colorbar(im1, ax=ax1, label="Log Energy")

        im2 = ax2.imshow(spec_leak.T, aspect='auto', origin='lower', cmap='inferno')
        ax2.set_title("Simulated Structural Micro-Leak (Turbulent Hiss)")
        ax2.set_xlabel("Time Frames (16 ms)")
        ax2.set_ylabel("Mel Frequency Bands (0.5 - 8 kHz)")
        fig.colorbar(im2, ax=ax2, label="Log Energy")

        plt.tight_layout()
        os.makedirs("presentation/assets", exist_ok=True)
        plt.savefig("presentation/assets/spectral_comparison.png")
        print("Generated spectral comparison asset at: presentation/assets/spectral_comparison.png")
    except ImportError:
        pass
