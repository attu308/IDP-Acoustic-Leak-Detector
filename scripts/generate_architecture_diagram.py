#!/usr/bin/env python3
"""
Generate publication-quality system architecture schematic for IEEE/academic presentation.
Spacious 16:9 widescreen layout, zero-crossing orthogonal signal flow, generous margins, crisp typography.
Output: presentation/assets/system_architecture.png
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_block(ax, x, y, w, h, title, subtitle=None, details=None, 
               bg_color="#FFFFFF", border_color="#334155", border_width=1.2, 
               title_color="#0F172A", title_size=9.5, is_container=False):
    """Draws an engineering block with clean typography and precise padding."""
    rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.04,rounding_size=0.10",
                                  facecolor=bg_color, edgecolor=border_color, linewidth=border_width)
    ax.add_patch(rect)

    if title:
        ty = y + h - (0.28 if is_container else 0.20)
        ax.text(x + w / 2.0, ty, title, ha='center', va='center', 
                fontsize=title_size, fontweight='bold', color=title_color)

    if subtitle:
        sy = y + h - (0.55 if is_container else 0.38)
        ax.text(x + w / 2.0, sy, subtitle, ha='center', va='center', 
                fontsize=8.2, fontstyle='italic', color="#475569")

    if details:
        start_y = y + h - (0.58 if subtitle else 0.38)
        for i, line in enumerate(details):
            ly = start_y - i * 0.17
            if ly > y + 0.05:
                ax.text(x + 0.16, ly, line, ha='left', va='center', 
                        fontsize=7.5, color="#1E293B")

def draw_arrow(ax, x1, y1, x2, y2, label=None, label_pos="right", color="#2563EB", lw=1.8, label_oy=0.0, label_ox=0.0):
    """Draws clean directional signal arrows with background pill labels."""
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="->,head_width=0.20,head_length=0.32", lw=lw, color=color))
    if label:
        mx = (x1 + x2) / 2.0
        my = (y1 + y2) / 2.0
        ox = label_ox
        oy = label_oy
        if label_pos == "top":
            oy += 0.16
        elif label_pos == "bottom":
            oy -= 0.16
        elif label_pos == "right":
            ox += 0.18
        elif label_pos == "left":
            ox -= 0.18

        ax.text(mx + ox, my + oy, label, ha='center', va='center', 
                fontsize=7.2, fontweight='bold', color=color,
                bbox=dict(boxstyle="round,pad=0.10", facecolor="#FFFFFF", edgecolor="#CBD5E1", lw=0.6, alpha=0.96))

def generate_diagram(output_path: str):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # 22.5 x 11.2 inches canvas for widescreen presentation fit (aspect ratio ~2.0)
    fig, ax = plt.subplots(figsize=(22.5, 11.2), dpi=300)
    ax.set_xlim(0, 22.5)
    ax.set_ylim(0, 11.2)
    ax.axis('off')

    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#FFFFFF')

    # =========================================================================
    # 0. TITLE BLOCK
    # =========================================================================
    ax.text(11.25, 10.75, "SMART ACOUSTIC LEAK DETECTOR — SYSTEM ARCHITECTURE", 
            ha='center', va='center', fontsize=18, fontweight='bold', color='#0F172A')
    ax.text(11.25, 10.38, "Multi-Tier Edge AI Framework: Non-Invasive Contact Sensing  →  ESP32-S3 Dual-Core DSP/TinyML  →  Autonomous Shutoff & Telemetry", 
            ha='center', va='center', fontsize=10.5, color='#475569')
    
    ax.plot([0.70, 21.80], [10.12, 10.12], color="#CBD5E1", lw=1.2)

    # =========================================================================
    # 1. SENSING & SIGNAL CONDITIONING SUBSYSTEM (Left Column: x: 0.70 to 4.60)
    # Flows DOWN from pipe to active filter at bottom
    # =========================================================================
    draw_block(ax, 0.70, 1.65, 3.90, 8.30, 
               "1. SENSING & CONDITIONING", 
               "Physical Coupling & Analog Front-End (AFE)", 
               None, bg_color="#F8FAFC", border_color="#2563EB", border_width=2.0,
               title_color="#1E40AF", title_size=11, is_container=True)

    # 1A. Pressurized Pipeline (Top)
    draw_block(ax, 0.90, 7.10, 3.50, 1.15,
               "Pressurized Pipeline", None,
               ["• Schedule 40 PVC / Metallic Pipe",
                "• Fluid Pressure: 2.0 – 6.0 Bar",
                "• Micro-leak turbulence: 1.0 – 8.0 kHz"],
               bg_color="#FFFFFF", border_color="#94A3B8")

    # 1B. Mechanical Clamp
    draw_block(ax, 0.90, 5.35, 3.50, 1.15,
               "Mechanical Collar Clamp", None,
               ["• 3D-Printed Contoured Housing",
                "• High-viscosity silicone couplant",
                "• Non-invasive; zero pipe wall breach"],
               bg_color="#FFFFFF", border_color="#94A3B8")

    # 1C. Contact Piezo Transducer
    draw_block(ax, 0.90, 3.60, 3.50, 1.15,
               "Contact Piezo Transducer", None,
               ["• PZT Ceramic Sensor Disc",
                "• Direct pipe wall vibration capture",
                "• Natural acoustic noise rejection",
                "• High-impedance charge output"],
               bg_color="#EFF6FF", border_color="#1D4ED8", border_width=1.3, title_color="#1E40AF")

    # 1D. Active Analog Filter (AFE) (Bottom)
    draw_block(ax, 0.90, 1.85, 3.50, 1.15,
               "Active Analog Filter (AFE)", None,
               ["• LM358 Charge Amplifier Stage",
                "• 2nd-Order Sallen-Key HPF (>500 Hz)",
                "• Removes 50 Hz hum & motor rumble",
                "• Output: Conditioned 0–3.3V Analog"],
               bg_color="#EFF6FF", border_color="#1D4ED8", border_width=1.3, title_color="#1E40AF")

    # Downward internal arrows in Layer 1
    draw_arrow(ax, 2.65, 7.10, 2.65, 6.50, label="Acoustic Emissions", label_pos="right", color="#64748B")
    draw_arrow(ax, 2.65, 5.35, 2.65, 4.75, label="Structural Waves", label_pos="right", color="#64748B")
    draw_arrow(ax, 2.65, 3.60, 2.65, 3.00, label="High-Z Charge", label_pos="right", color="#1D4ED8")

    # Horizontal Feed from AFE into Core 0 ADC DMA (zero diagonal, perfectly spaced)
    draw_arrow(ax, 4.40, 2.425, 5.65, 2.425, color="#2563EB", lw=2.2)
    ax.text(5.025, 2.67, "Filtered Signal [0–3.3V]", ha='center', va='center', 
            fontsize=7.0, fontweight='bold', color="#2563EB",
            bbox=dict(boxstyle="round,pad=0.10", facecolor="#FFFFFF", edgecolor="#CBD5E1", lw=0.6, alpha=0.96))
    ax.text(5.025, 2.18, "GPIO 4 / ADC1_CH3", ha='center', va='center', 
            fontsize=6.8, fontweight='bold', color="#0D9488",
            bbox=dict(boxstyle="round,pad=0.10", facecolor="#FFFFFF", edgecolor="#CBD5E1", lw=0.6, alpha=0.96))

    # =========================================================================
    # 2. EDGE EMBEDDED COMPUTING UNIT (ESP32-S3) (Center: x: 5.40 to 16.20)
    # Flows UP on Core 0, ACROSS via IPC Queue, and DOWN on Core 1!
    # =========================================================================
    draw_block(ax, 5.40, 1.65, 10.80, 8.30,
               "2. EDGE EMBEDDED COMPUTING UNIT — ESP32-S3 DUAL-CORE LX7 @ 240 MHz",
               "System Hardware: 512 KB Internal SRAM | 8 MB Octal PSRAM | Xtensa Vector Instructions (ESP-NN)",
               None, bg_color="#F8FAFC", border_color="#0D9488", border_width=2.2,
               title_color="#0F766E", title_size=11.5, is_container=True)

    # -------------------------------------------------------------------------
    # Core 0: Real-Time Ingestion & DSP (Left side of chip, flows UP)
    # -------------------------------------------------------------------------
    draw_block(ax, 5.65, 1.75, 4.70, 7.45,
               "FreeRTOS Core 0: Ingestion & DSP",
               "Real-Time Deterministic Task (Priority 2)",
               None, bg_color="#F0FDFA", border_color="#14B8A6", border_width=1.4,
               title_color="#115E59", title_size=10, is_container=True)

    # Core 0 Block 1: ADC DMA Controller (Bottom)
    draw_block(ax, 5.85, 1.85, 4.30, 1.15,
               "ADC DMA Controller", None,
               ["• 16,000 Samples/sec @ 12-bit ADC",
                "• Ping-Pong Circular Ring Buffer",
                "• Zero CPU polling during acquisition"],
               bg_color="#FFFFFF", border_color="#0D9488")

    # Core 0 Block 2: Framing & Windowing
    draw_block(ax, 5.85, 3.60, 4.30, 1.15,
               "Framing & Windowing Stage", None,
               ["• 1000 ms Detection Frame (16,000 pts)",
                "• 32 ms Sub-Window (512 samples)",
                "• 50% Hop Size (256 sample shift)",
                "• Periodic Hanning Window Function"],
               bg_color="#FFFFFF", border_color="#0D9488")

    # Core 0 Block 3: 512-pt Real FFT
    draw_block(ax, 5.85, 5.35, 4.30, 1.15,
               "512-Point Real FFT Engine", None,
               ["• Hardware-accelerated Radix-4 FFT",
                "• Frequency Resolution: Δf = 31.25 Hz",
                "• Computes Power Spectrum: |X(f)|²",
                "• Nyquist Bandwidth: 0 – 8,000 Hz"],
               bg_color="#FFFFFF", border_color="#0D9488")

    # Core 0 Block 4: 32-Band Log-Mel Filterbank (Top)
    draw_block(ax, 5.85, 7.10, 4.30, 1.15,
               "32-Band Log-Mel Filterbank", None,
               ["• Triangulated Mel Scale (500–8000 Hz)",
                "• Logarithmic Energy Compression: log₁₀(E+ε)",
                "• Output: 2D Spectrogram Matrix (61 × 32)",
                "• Isolates Micro-Leak Turbulence Band"],
               bg_color="#FFFFFF", border_color="#0D9488")

    # Upward internal arrows in Core 0
    draw_arrow(ax, 8.00, 3.00, 8.00, 3.60, label="DMA Samples (16 kHz)", label_pos="right", color="#0D9488")
    draw_arrow(ax, 8.00, 4.75, 8.00, 5.35, label="Windowed Frames (32 ms)", label_pos="right", color="#0D9488")
    draw_arrow(ax, 8.00, 6.50, 8.00, 7.10, label="Power Spectrum |X(f)|²", label_pos="right", color="#0D9488")

    # -------------------------------------------------------------------------
    # Inter-Core FreeRTOS Queue (Bridge at Top)
    # -------------------------------------------------------------------------
    queue_rect = patches.FancyBboxPatch((10.50, 7.10), 1.10, 1.15, boxstyle="round,pad=0.04",
                                        facecolor="#FEF3C7", edgecolor="#D97706", linewidth=1.5)
    ax.add_patch(queue_rect)
    ax.text(11.05, 7.90, "FreeRTOS\nIPC QUEUE", ha='center', va='center', fontsize=7.5, fontweight='bold', color="#92400E")
    ax.text(11.05, 7.38, "Feature\nTensor\n[61×32]", ha='center', va='center', fontsize=7.0, color="#78350F")

    # Horizontal transfer through IPC Queue at top (perfect horizontal flow)
    draw_arrow(ax, 10.15, 7.675, 10.50, 7.675, color="#D97706", lw=2.0)
    draw_arrow(ax, 11.60, 7.675, 11.95, 7.675, color="#D97706", lw=2.0)

    # -------------------------------------------------------------------------
    # Core 1: TinyML Inference & Supervisory Control (Right side of chip, flows DOWN)
    # -------------------------------------------------------------------------
    draw_block(ax, 11.85, 1.75, 4.10, 7.45,
               "FreeRTOS Core 1: TinyML & Control",
               "Application & Actuation Task (Priority 1)",
               None, bg_color="#FFFBEB", border_color="#F59E0B", border_width=1.4,
               title_color="#92400E", title_size=10, is_container=True)

    # Core 1 Block 1: Tensor Arena Memory (Top)
    draw_block(ax, 12.05, 7.10, 3.70, 1.15,
               "TFLite Micro Tensor Arena", None,
               ["• SRAM Allocation: < 48 KB Static",
                "• Ingests 2D Spectrogram Tensor",
                "• Zero-copy memory pooling"],
               bg_color="#FFFFFF", border_color="#D97706")

    # Core 1 Block 2: Int8 Quantized CNN
    draw_block(ax, 12.05, 5.35, 3.70, 1.15,
               "Int8 Quantized 1D/2D CNN", None,
               ["• Conv1 (8 filters, 3×3, ReLU) + MaxPool",
                "• Conv2 (16 filters, 3×3) + GlobalAvgPool",
                "• Post-Training Quantization (fp32 → int8)",
                "• Inference Latency: < 185 ms"],
               bg_color="#FFFFFF", border_color="#D97706")

    # Core 1 Block 3: Softmax Anomaly Classifier
    draw_block(ax, 12.05, 3.60, 3.70, 1.15,
               "Softmax Anomaly Classifier", None,
               ["• Class 0: Normal Laminar Flow",
                "• Class 1: Ambient Noise / Tap",
                "• Class 2: Pressurized Micro-Leak (>90%)",
                "• Class 3: Major Rupture"],
               bg_color="#FFFFFF", border_color="#D97706")

    # Core 1 Block 4: Debounce & Decision Engine (Bottom)
    draw_block(ax, 12.05, 1.85, 3.70, 1.15,
               "Debounce & Decision Engine", None,
               ["• Debounce: 3 Consecutive Positives",
                "• Threshold: Confidence > 0.85",
                "• Rejects Transient False Alarms",
                "• Dispatches Actuation & Telemetry"],
               bg_color="#FFFFFF", border_color="#D97706")

    # Downward internal arrows in Core 1
    draw_arrow(ax, 13.90, 7.10, 13.90, 6.50, label="Input Tensor [61×32]", label_pos="right", color="#D97706")
    draw_arrow(ax, 13.90, 5.35, 13.90, 4.75, label="Feature Maps (ESP-NN)", label_pos="right", color="#D97706")
    draw_arrow(ax, 13.90, 3.60, 13.90, 3.00, label="Softmax Probabilities", label_pos="right", color="#D97706")

    # =========================================================================
    # 3. AUTONOMOUS ACTUATION SUBSYSTEM (Bottom Right: x: 17.20 to 21.80)
    # Direct horizontal feed from Core 1 Decision Engine at bottom! Zero Crossing!
    # =========================================================================
    draw_block(ax, 17.20, 1.65, 4.60, 4.00,
               "3. AUTONOMOUS ACTUATION", 
               "Hardware Isolation Loop (< 500 ms Latency)", 
               None, bg_color="#FEF2F2", border_color="#DC2626", border_width=2.0,
               title_color="#991B1B", title_size=11, is_container=True)

    # 3A. Optoisolated Relay Module (Bottom)
    draw_block(ax, 17.40, 1.85, 4.20, 1.15,
               "Optoisolated 5V Relay Module", None,
               ["• Songle SRD-05VDC-SL-C Relay Stage",
                "• EL817 Optocoupler Electrical Barrier",
                "• Active-Low Trigger from GPIO 18",
                "• Prevents inductive back-EMF spikes"],
               bg_color="#FFFFFF", border_color="#EF4444")

    # 3B. Motorized Solenoid Valve (Top of Actuation block)
    draw_block(ax, 17.40, 3.60, 4.20, 1.25,
               "12V DC Solenoid Shutoff Valve", None,
               ["• Direct-acting Brass / SS304 Valve",
                "• Fluid Isolation in < 1.0 Second",
                "• Fail-safe Normally Open (N/O)",
                "• Zero cloud/network dependency"],
               bg_color="#FFFFFF", border_color="#EF4444")

    # Internal arrow inside Actuation: from Relay up to Solenoid Valve
    draw_arrow(ax, 19.50, 3.00, 19.50, 3.60, label="12V Coil Drive (NO/NC)", label_pos="right", color="#DC2626")

    # Direct horizontal connection from Core 1 Debounce Engine into Relay Module
    draw_arrow(ax, 15.75, 2.425, 17.40, 2.425, color="#DC2626", lw=2.2)
    ax.text(16.45, 2.67, "GPIO 18 Trigger (<50ms)", ha='center', va='center', 
            fontsize=7.0, fontweight='bold', color="#DC2626",
            bbox=dict(boxstyle="round,pad=0.10", facecolor="#FFFFFF", edgecolor="#CBD5E1", lw=0.6, alpha=0.96))
    ax.text(16.45, 2.18, "Active-Low Signal", ha='center', va='center', 
            fontsize=6.8, color="#991B1B",
            bbox=dict(boxstyle="round,pad=0.10", facecolor="#FFFFFF", edgecolor="#CBD5E1", lw=0.6, alpha=0.96))

    # =========================================================================
    # 4. WIRELESS TELEMETRY SUBSYSTEM (Top Right: x: 17.20 to 21.80)
    # Clean orthogonal bus route up the right gutter. Zero Crossing!
    # =========================================================================
    draw_block(ax, 17.20, 5.95, 4.60, 4.00,
               "4. WIRELESS TELEMETRY", 
               "Cloud Connectivity & Supervisory SCADA", 
               None, bg_color="#F5F3FF", border_color="#7C3AED", border_width=2.0,
               title_color="#5B21B6", title_size=11, is_container=True)

    # 4A. Wi-Fi / MQTT Event Client (Top)
    draw_block(ax, 17.40, 7.70, 4.20, 1.25,
               "Wi-Fi / MQTT Event Client", None,
               ["• 2.4 GHz 802.11 b/g/n Transceiver",
                "• Lightweight JSON Event Alerts (QoS 1)",
                "• Dispatches only on state transition",
                "• >99.8% Bandwidth Savings vs Raw Audio"],
               bg_color="#FFFFFF", border_color="#8B5CF6")

    # 4B. Supervisory Dashboard (Bottom of Telemetry block)
    draw_block(ax, 17.40, 6.10, 4.20, 1.15,
               "Supervisory SCADA Dashboard", None,
               ["• Web Dashboard (Node-RED / Grafana)",
                "• Real-time Valve Status & Alerts",
                "• Time-series historical telemetry log",
                "• Immediate SMS / Push Notifications"],
               bg_color="#FFFFFF", border_color="#8B5CF6")

    # Internal arrow inside Telemetry: from MQTT Client down to SCADA Dashboard
    draw_arrow(ax, 19.50, 7.70, 19.50, 7.25, label="MQTT over TLS (8883)", label_pos="right", color="#7C3AED")

    # Orthogonal Telemetry Routing:
    # Starts cleanly from Core 1 Decision Engine at y=2.80 (above GPIO 18 line at 2.425)
    # Seg 1: Horizontal from Core 1 into channel (x=15.75 to 16.95)
    # Seg 2: Vertical UP gutter (y=2.80 to 8.325)
    # Seg 3: Horizontal into MQTT Client (x=16.95 to 17.40)
    ax.plot([15.75, 16.95], [2.80, 2.80], color="#7C3AED", lw=1.8)
    ax.plot([16.95, 16.95], [2.80, 8.325], color="#7C3AED", lw=1.8)
    ax.annotate('', xy=(17.40, 8.325), xytext=(16.95, 8.325),
                arrowprops=dict(arrowstyle="->,head_width=0.20,head_length=0.32", lw=1.8, color="#7C3AED"))
    
    # Pill label along vertical telemetry line - placed in open vertical space between containers
    ax.text(16.95, 5.75, "Event Alert\nJSON Payload", ha='center', va='center', 
            fontsize=6.8, fontweight='bold', color="#7C3AED",
            bbox=dict(boxstyle="round,pad=0.10", facecolor="#FFFFFF", edgecolor="#CBD5E1", lw=0.6, alpha=0.96))

    # =========================================================================
    # 5. BOTTOM TECHNICAL SPECIFICATIONS BAR
    # =========================================================================
    spec_rect = patches.FancyBboxPatch((0.70, 0.30), 21.10, 1.10, boxstyle="round,pad=0.08",
                                       facecolor="#0F172A", edgecolor="#334155", linewidth=1.5)
    ax.add_patch(spec_rect)

    specs = [
        ("ACOUSTIC FREQUENCY BAND", "1.0 kHz – 5.0 kHz", "Optimized for PVC leak turbulence"),
        ("INFERENCE LATENCY", "< 185 Milliseconds", "On-device sub-watt Edge AI (TinyML)"),
        ("ACTIVE MEMORY FOOTPRINT", "148 KB Internal SRAM", "Operates entirely within ESP32 SRAM"),
        ("AUTONOMOUS SHUTOFF", "< 1.0 Second Closure", "Zero reliance on cloud or Wi-Fi network"),
        ("TOTAL HARDWARE COST", "< ₹1,800 INR", "Vs. ₹1,00,000+ commercial loggers")
    ]

    for i, (head, val, note) in enumerate(specs):
        col_x = 0.90 + i * 4.22
        ax.text(col_x + 1.85, 1.10, head, ha='center', va='center', fontsize=7.8, fontweight='bold', color="#94A3B8")
        ax.text(col_x + 1.85, 0.82, val, ha='center', va='center', fontsize=11.5, fontweight='bold', color="#38BDF8")
        ax.text(col_x + 1.85, 0.56, note, ha='center', va='center', fontsize=7.2, color="#E2E8F0")

        if i < 4:
            ax.plot([col_x + 3.95, col_x + 3.95], [0.48, 1.22], color="#334155", lw=1.0)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
    plt.close()
    print(f"[SUCCESS] Publication-quality system architecture generated at: {output_path}")

if __name__ == "__main__":
    generate_diagram("presentation/assets/system_architecture.png")
