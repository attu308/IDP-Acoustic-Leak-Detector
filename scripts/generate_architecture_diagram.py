#!/usr/bin/env python3
"""
Generate professional publication-quality system architecture diagram.
Output: presentation/assets/system_architecture.png
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_diagram(output_path: str):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    fig, ax = plt.subplots(figsize=(14, 8), dpi=300)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8.5)
    ax.axis('off')

    # Background canvas
    fig.patch.set_facecolor('#F8FAFC')
    ax.set_facecolor('#F8FAFC')

    # Title & Subtitle
    ax.text(7, 8.1, "SMART ACOUSTIC LEAK DETECTOR - SYSTEM ARCHITECTURE", 
            ha='center', va='center', fontsize=16, fontweight='bold', color='#0F172A')
    ax.text(7, 7.75, "Edge AI (TinyML) Multi-Tier Acoustic Sensing, Dual-Core DSP/Inference & Autonomous Actuation", 
            ha='center', va='center', fontsize=10, fontstyle='italic', color='#475569')

    # Styles
    box_props = dict(boxstyle="round,pad=0.4", linewidth=1.5)
    arrow_props = dict(arrowstyle="->", lw=2, color="#334155")

    # Layer 1: Physical & Acoustic Sensing (Left Column)
    layer1_rect = patches.FancyBboxPatch((0.5, 1.2), 3.2, 6.0, boxstyle="round,pad=0.2",
                                         linewidth=1.8, edgecolor="#2563EB", facecolor="#EFF6FF")
    ax.add_patch(layer1_rect)
    ax.text(2.1, 6.9, "1. SENSING & SIGNAL CONDITIONING", ha='center', va='center', fontsize=11, fontweight='bold', color='#1E40AF')

    # Layer 1 Sub-blocks
    blocks_l1 = [
        ("Pressurized Pipe Wall\n(1-8 kHz Acoustic Emission)", 5.8, "#DBEAFE", "#1D4ED8"),
        ("Contact Piezoelectric Transducer\n(Structural Vibration Capture)", 4.4, "#DBEAFE", "#1D4ED8"),
        ("Active Analog Signal Conditioning\n(Charge Amp + LM358 HPF >500Hz)", 3.0, "#DBEAFE", "#1D4ED8"),
        ("Low-Noise Shielded Feed\n(Analog Signal to ADC)", 1.7, "#BFDBFE", "#1E40AF")
    ]
    for text, y, fc, ec in blocks_l1:
        patch = patches.FancyBboxPatch((0.8, y - 0.45), 2.6, 0.9, boxstyle="round,pad=0.2", facecolor=fc, edgecolor=ec, lw=1.2)
        ax.add_patch(patch)
        ax.text(2.1, y, text, ha='center', va='center', fontsize=8.5, fontweight='semibold', color='#0F172A')

    # Arrows inside Layer 1
    for y in [5.25, 3.85, 2.45]:
        ax.annotate('', xy=(2.1, y - 0.4), xytext=(2.1, y), arrowprops=arrow_props)

    # Layer 2: Edge Compute Engine (ESP32-S3 Dual-Core LX7)
    layer2_rect = patches.FancyBboxPatch((4.2, 1.2), 5.8, 6.0, boxstyle="round,pad=0.2",
                                         linewidth=2.2, edgecolor="#0D9488", facecolor="#F0FDFA")
    ax.add_patch(layer2_rect)
    ax.text(7.1, 6.9, "2. EDGE COMPUTE ENGINE (ESP32-S3 @ 240 MHz)", ha='center', va='center', fontsize=11, fontweight='bold', color='#0F766E')

    # FreeRTOS Core 0
    core0_rect = patches.FancyBboxPatch((4.4, 1.5), 2.5, 5.0, boxstyle="round,pad=0.2",
                                        linewidth=1.4, edgecolor="#14B8A6", facecolor="#CCFBF1")
    ax.add_patch(core0_rect)
    ax.text(5.65, 6.2, "FreeRTOS Core 0\n(Ingestion & DSP)", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#115E59')

    blocks_core0 = [
        ("ADC DMA Controller\n(16 kHz @ 12-Bit Sampling)", 5.2),
        ("Ring Buffer Framing\n(1000ms Hanning Window)", 4.0),
        ("512-pt FFT Engine\n(Magnitude Spectrum)", 2.8),
        ("Log-Mel Filterbank\n(Turbulence Features)", 1.7)
    ]
    for text, y in blocks_core0:
        patch = patches.FancyBboxPatch((4.6, y - 0.4), 2.1, 0.8, boxstyle="round,pad=0.15", facecolor="#E6FFFA", edgecolor="#0D9488", lw=1)
        ax.add_patch(patch)
        ax.text(5.65, y, text, ha='center', va='center', fontsize=7.5, fontweight='medium', color='#0F172A')

    for y in [4.7, 3.5, 2.3]:
        ax.annotate('', xy=(5.65, y - 0.3), xytext=(5.65, y), arrowprops=arrow_props)

    # Inter-Core Queue Arrow
    ax.annotate('', xy=(7.4, 3.8), xytext=(6.7, 3.8),
                arrowprops=dict(arrowstyle="->", lw=2.5, color="#D97706"))
    ax.text(7.05, 4.15, "IPC Queue\n(Feature Map)", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#B45309')

    # FreeRTOS Core 1
    core1_rect = patches.FancyBboxPatch((7.3, 1.5), 2.5, 5.0, boxstyle="round,pad=0.2",
                                        linewidth=1.4, edgecolor="#F59E0B", facecolor="#FEF3C7")
    ax.add_patch(core1_rect)
    ax.text(8.55, 6.2, "FreeRTOS Core 1\n(TinyML & Control)", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#92400E')

    blocks_core1 = [
        ("Tensor Arena Allocator\n(SRAM Constrained: <64KB)", 5.2),
        ("TFLite Micro CNN\n(8-bit Quantized int8)", 4.0),
        ("Softmax Anomaly Classifier\n(4 Classes, >90% Acc)", 2.8),
        ("Actuation & Alert State Machine\n(Debounce & Decision Logic)", 1.7)
    ]
    for text, y in blocks_core1:
        patch = patches.FancyBboxPatch((7.5, y - 0.4), 2.1, 0.8, boxstyle="round,pad=0.15", facecolor="#FFFBEB", edgecolor="#D97706", lw=1)
        ax.add_patch(patch)
        ax.text(8.55, y, text, ha='center', va='center', fontsize=7.5, fontweight='medium', color='#0F172A')

    for y in [4.7, 3.5, 2.3]:
        ax.annotate('', xy=(8.55, y - 0.3), xytext=(8.55, y), arrowprops=arrow_props)

    # Feed from Layer 1 to Layer 2
    ax.annotate('', xy=(4.2, 5.2), xytext=(3.4, 1.7),
                arrowprops=dict(arrowstyle="->", lw=2, color="#2563EB", connectionstyle="arc3,rad=-0.2"))

    # Layer 3: Actuation (Top Right)
    layer3_rect = patches.FancyBboxPatch((10.4, 4.3), 3.1, 2.9, boxstyle="round,pad=0.2",
                                         linewidth=1.8, edgecolor="#DC2626", facecolor="#FEF2F2")
    ax.add_patch(layer3_rect)
    ax.text(11.95, 6.9, "3. AUTONOMOUS ACTUATION", ha='center', va='center', fontsize=10.5, fontweight='bold', color='#991B1B')

    patch_relay = patches.FancyBboxPatch((10.7, 5.6), 2.5, 0.75, boxstyle="round,pad=0.15", facecolor="#FEE2E2", edgecolor="#DC2626", lw=1)
    ax.add_patch(patch_relay)
    ax.text(11.95, 5.95, "Optoisolated 5V Relay\n(GPIO Driven)", ha='center', va='center', fontsize=8, fontweight='medium')

    patch_valve = patches.FancyBboxPatch((10.7, 4.55), 2.5, 0.75, boxstyle="round,pad=0.15", facecolor="#FEE2E2", edgecolor="#DC2626", lw=1)
    ax.add_patch(patch_valve)
    ax.text(11.95, 4.9, "12V Motorized Solenoid Valve\n(Sub-Second Flow Shutoff)", ha='center', va='center', fontsize=8, fontweight='medium')

    ax.annotate('', xy=(11.95, 5.35), xytext=(11.95, 5.6), arrowprops=arrow_props)

    # Layer 4: Telemetry & Monitoring (Bottom Right)
    layer4_rect = patches.FancyBboxPatch((10.4, 1.2), 3.1, 2.8, boxstyle="round,pad=0.2",
                                         linewidth=1.8, edgecolor="#7C3AED", facecolor="#F5F3FF")
    ax.add_patch(layer4_rect)
    ax.text(11.95, 3.7, "4. WIRELESS TELEMETRY", ha='center', va='center', fontsize=10.5, fontweight='bold', color='#5B21B6')

    patch_wifi = patches.FancyBboxPatch((10.7, 2.5), 2.5, 0.75, boxstyle="round,pad=0.15", facecolor="#EDE9FE", edgecolor="#7C3AED", lw=1)
    ax.add_patch(patch_wifi)
    ax.text(11.95, 2.85, "Wi-Fi / MQTT Client\n(Low-Bandwidth JSON Alerts)", ha='center', va='center', fontsize=8, fontweight='medium')

    patch_dash = patches.FancyBboxPatch((10.7, 1.45), 2.5, 0.75, boxstyle="round,pad=0.15", facecolor="#EDE9FE", edgecolor="#7C3AED", lw=1)
    ax.add_patch(patch_dash)
    ax.text(11.95, 1.8, "Supervisory Dashboard\n(Telemetry, Alerts, Log)", ha='center', va='center', fontsize=8, fontweight='medium')

    ax.annotate('', xy=(11.95, 2.25), xytext=(11.95, 2.5), arrowprops=arrow_props)

    # Cross Connections from Core 1 to Actuation & Telemetry
    ax.annotate('', xy=(10.4, 5.95), xytext=(9.8, 2.2),
                arrowprops=dict(arrowstyle="->", lw=2, color="#DC2626", connectionstyle="arc3,rad=-0.15"))
    ax.text(10.05, 4.3, "Relay Trigger\n(On Leak)", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#DC2626')

    ax.annotate('', xy=(10.4, 2.85), xytext=(9.8, 1.7),
                arrowprops=dict(arrowstyle="->", lw=2, color="#7C3AED", connectionstyle="arc3,rad=0.1"))
    ax.text(10.15, 2.1, "MQTT Payload", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#7C3AED')

    # Footer note
    ax.text(7, 0.7, "Design Principles: Non-Invasive Acoustic Coupling | Offline Sub-200ms TinyML Inference | Zero Cloud Raw Audio Streaming | Fail-Safe Actuation",
            ha='center', va='center', fontsize=8, fontweight='semibold', color='#334155')

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
    plt.close()
    print(f"Generated system architecture diagram at: {output_path}")

if __name__ == "__main__":
    generate_diagram("presentation/assets/system_architecture.png")
