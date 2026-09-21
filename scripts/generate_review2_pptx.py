#!/usr/bin/env python3
"""
Generate professional, publication-quality Review II Presentation Deck (.pptx).
Mandatory 8-Slide Template matching BACSE291 IDP guidelines.
"""

import os
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_deck(output_path: str, architecture_image: str):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    blank_layout = prs.slide_layouts[6]

    # Color Palette
    BG_COLOR = RGBColor(248, 250, 252)     # #F8FAFC
    CARD_BG = RGBColor(255, 255, 255)      # White
    PRIMARY = RGBColor(15, 23, 42)         # Slate 900
    ACCENT_BLUE = RGBColor(37, 99, 235)    # Blue 600
    ACCENT_TEAL = RGBColor(13, 148, 136)   # Teal 600
    MUTED = RGBColor(100, 116, 139)        # Slate 500
    BORDER_COL = RGBColor(226, 232, 240)   # Slate 200

    def set_slide_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_COLOR
        bg.line.fill.background()

    def add_header(slide, title_text, category_text="BACSE291 | INNOVATIVE DESIGN PROJECT | REVIEW II"):
        # Top banner
        header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(1.1))
        tf = header_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p_cat = tf.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = ACCENT_BLUE

        p_title = tf.add_paragraph()
        p_title.text = title_text
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = PRIMARY
        p_title.space_before = Pt(4)

    # ==========================================
    # SLIDE 1: Title Slide
    # ==========================================
    slide1 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide1)

    # Decorative Card
    card1 = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(0.9), Inches(11.333), Inches(5.7))
    card1.fill.solid()
    card1.fill.fore_color.rgb = CARD_BG
    card1.line.color.rgb = BORDER_COL
    card1.line.width = Pt(1.5)

    tb1 = slide1.shapes.add_textbox(Inches(1.5), Inches(1.3), Inches(10.3), Inches(4.9))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "BACSE291 — INNOVATIVE DESIGN PROJECT (AY 2026–2027)"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE

    p = tf1.add_paragraph()
    p.text = "Smart Acoustic Leak Detector"
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    p.space_before = Pt(10)

    p = tf1.add_paragraph()
    p.text = "Acoustic-Vibrational Micro-Leak and Infrastructure Integrity Monitor Using Edge AI (TinyML)"
    p.font.size = Pt(16)
    p.font.color.rgb = ACCENT_TEAL
    p.space_before = Pt(6)

    p = tf1.add_paragraph()
    p.text = "Review II: Initial Design, System Architecture & 20% Prototype Milestone"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = MUTED
    p.space_before = Pt(16)

    # Divider bar
    div = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.5), Inches(4.3), Inches(10.3), Inches(0.04))
    div.fill.solid()
    div.fill.fore_color.rgb = ACCENT_BLUE
    div.line.fill.background()

    # Meta text box
    tb_meta = slide1.shapes.add_textbox(Inches(1.5), Inches(4.5), Inches(10.3), Inches(1.8))
    tf_m = tb_meta.text_frame
    tf_m.word_wrap = True

    p = tf_m.paragraphs[0]
    p.text = "Student Team: B.Tech Computer Science & Engineering"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = PRIMARY

    p = tf_m.add_paragraph()
    p.text = "Team Members: Atharv Deshpande & Project Partners | Specialization: AI / Core CSE"
    p.font.size = Pt(11)
    p.font.color.rgb = MUTED
    p.space_before = Pt(3)

    p = tf_m.add_paragraph()
    p.text = "Project Guide: Assigned Faculty Mentor, Department of Computer Science & Engineering"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    p.space_before = Pt(6)

    # ==========================================
    # SLIDE 2: Agenda
    # ==========================================
    slide2 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide2)
    add_header(slide2, "Presentation Agenda")

    agenda_items = [
        ("01", "Introduction & Problem Statement", "The municipal water loss challenge & limitations of current inspection."),
        ("02", "Literature Survey & Baselines", "Analysis of acoustic propagation, SCADA mass-balance, and IoT loggers."),
        ("03", "Challenges & Research Gap", "Bandwidth, power, latency, and the need for autonomous edge mitigation."),
        ("04", "Project Objectives & Scope", "Concrete, measurable goals across hardware, DSP, TinyML, and actuation."),
        ("05", "Methodology & System Architecture", "Multi-tier design, FreeRTOS dual-core task segregation, and hardware BOM."),
        ("06", "Component & Tool Justification", "Technical trade-offs: ESP32-S3 vs RPi/Arduino; Piezo vs MEMS sensors."),
        ("07", "Initial Implementation (~20% Prototype)", "Demonstration of live acoustic ingestion, DSP spectrograms, and state logic."),
        ("08", "Project Planning & Individual Roles", "Work Breakdown Structure, milestones across Fall/Winter, and defense matrix.")
    ]

    for i, (num, title, desc) in enumerate(agenda_items):
        col = i % 2
        row = i // 2
        x = Inches(0.8 + col * 5.9)
        y = Inches(1.6 + row * 1.35)

        card = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(5.6), Inches(1.15))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = BORDER_COL

        tb = slide2.shapes.add_textbox(x + Inches(0.2), y + Inches(0.12), Inches(5.2), Inches(0.9))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_top = tf.margin_left = tf.margin_right = tf.margin_bottom = 0

        p = tf.paragraphs[0]
        p.text = f"{num}. {title}"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = PRIMARY

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = MUTED
        p2.space_before = Pt(3)

    # ==========================================
    # SLIDE 3: Introduction
    # ==========================================
    slide3 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide3)
    add_header(slide3, "Introduction: The Non-Revenue Water (NRW) Crisis")

    intro_cards = [
        ("The Global & Municipal Challenge",
         [("30% – 50% Water Loss:", "Municipal distribution systems lose massive fluid volumes to Non-Revenue Water (NRW) before reaching consumers."),
          ("Invisible Micro-Cracks:", "Pressurized pipeline leaks start as sub-millimeter fissures that remain structurally undetected for months."),
          ("Severe Cascading Damage:", "Unchecked micro-leaks cause soil erosion, catastrophic road cave-ins, and severe building foundation damage.")]),

        ("Failure of Conventional Approaches",
         [("Manual Acoustic Patrols:", "Technicians use acoustic listening rods periodically; inspection is labor-intensive, human-dependent, and non-continuous."),
          ("Cloud-IoT Bandwidth Congestion:", "Streaming raw audio/vibration to cloud platforms consumes ~1.2 GB/day per node, incurring high data costs."),
          ("Zero Autonomous Shutoff:", "Existing loggers only record data; they cannot physically isolate the leak during network outages.")]),

        ("The Edge AI (TinyML) Breakthrough",
         [("In-Situ Processing:", "Shifting intelligence directly onto sub-watt dual-core microcontrollers eliminates raw audio streaming completely."),
          ("Sub-200ms Latency:", "On-device quantized neural inference detects leak acoustic signatures in milliseconds."),
          ("Autonomous Isolation:", "Direct GPIO-triggered solenoid shutoff valve prevents catastrophic flooding even if Wi-Fi fails entirely.")])
    ]

    for i, (ctitle, points) in enumerate(intro_cards):
        x = Inches(0.8 + i * 3.95)
        card = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.6), Inches(3.75), Inches(5.2))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = BORDER_COL

        tb = slide3.shapes.add_textbox(x + Inches(0.25), Inches(1.85), Inches(3.25), Inches(4.7))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_top = tf.margin_left = tf.margin_right = tf.margin_bottom = 0

        p = tf.paragraphs[0]
        p.text = ctitle
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = ACCENT_BLUE if i == 2 else PRIMARY

        for header, body in points:
            p_b = tf.add_paragraph()
            p_b.text = f"• {header} "
            p_b.font.size = Pt(10)
            p_b.font.bold = True
            p_b.font.color.rgb = PRIMARY
            p_b.space_before = Pt(8)

            run = p_b.add_run()
            run.text = body
            run.font.bold = False
            run.font.color.rgb = MUTED

    # ==========================================
    # SLIDE 4: Literature Survey
    # ==========================================
    slide4 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide4)
    add_header(slide4, "Literature Survey: Comparative Analysis of Existing Baselines")

    lit_rows = [
        ("Acoustic Wave Propagation in Plastic Pipes", "Hunaidi et al. (National Research Council Canada)",
         "Analyzed acoustic vibration attenuation in PVC and MDPE water distribution pipes.",
         "Demonstrated that high frequencies (>2 kHz) attenuate rapidly in plastic. Highlighted that leak energy concentrates in 1–5 kHz bands.",
         "Focused on offline acoustic correlation with bulky lab equipment; no real-time embedded edge classification."),

        ("District Metering Area (DMA) Mass-Balance", "SCADA Hydraulic Flow-Balance Systems",
         "Utilizes electromagnetic flow meters at district inlet/outlet boundaries to monitor net water volume discrepancies.",
         "Reliable for macro-ruptures and municipal-level volumetric accounting.",
         "Completely blind to micro-cracks (<10% volume loss); cannot localize faults or provide fast mechanical shutoff."),

        ("Cloud-Connected Acoustic IoT Streamers", "Commercial Acoustic Loggers (Gutermann, Sewerin)",
         "Deployed vibration sensors that upload recorded audio clips or telemetry via GSM/LoRaWAN to cloud servers.",
         "Enables map-based leak dashboards across city zones.",
         "Excessive unit cost (₹1,00,000+); high SIM/cellular bandwidth overhead; high latency (hours); no automated emergency actuation.")
    ]

    for i, (title, author, methodology, finding, limitation) in enumerate(lit_rows):
        y = Inches(1.6 + i * 1.75)
        card = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), y, Inches(11.7), Inches(1.6))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = BORDER_COL

        tb = slide4.shapes.add_textbox(Inches(1.0), y + Inches(0.12), Inches(11.3), Inches(1.35))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_top = tf.margin_left = tf.margin_right = tf.margin_bottom = 0

        p = tf.paragraphs[0]
        p.text = f"{title}  |  "
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = PRIMARY

        r = p.add_run()
        r.text = author
        r.font.size = Pt(11)
        r.font.bold = False
        r.font.color.rgb = ACCENT_BLUE

        p_m = tf.add_paragraph()
        p_m.text = f"• Approach: {methodology} Key Finding: {finding}"
        p_m.font.size = Pt(9.5)
        p_m.font.color.rgb = MUTED
        p_m.space_before = Pt(3)

        p_l = tf.add_paragraph()
        p_l.text = f"• Research Limitation: {limitation}"
        p_l.font.size = Pt(9.5)
        p_l.font.bold = True
        p_l.font.color.rgb = RGBColor(185, 28, 28)
        p_l.space_before = Pt(3)

    # ==========================================
    # SLIDE 5: Challenges & Research Gap
    # ==========================================
    slide5 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide5)
    add_header(slide5, "Challenges & Identified Research Gap")

    # Left Box: Key Engineering Challenges
    c_card = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2))
    c_card.fill.solid()
    c_card.fill.fore_color.rgb = CARD_BG
    c_card.line.color.rgb = BORDER_COL

    tb_c = slide5.shapes.add_textbox(Inches(1.1), Inches(1.85), Inches(5.0), Inches(4.7))
    tf_c = tb_c.text_frame
    tf_c.word_wrap = True
    tf_c.margin_top = tf_c.margin_left = tf_c.margin_right = tf_c.margin_bottom = 0

    p = tf_c.paragraphs[0]
    p.text = "Identified Technical Challenges"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = PRIMARY

    challenges = [
        ("Acoustic Impedance Mismatch:", "Airborne microphones (like standard MEMS) clamped to pipe exteriors capture room speech and ambient noise rather than fluid structural vibrations."),
        ("Edge Computational Constraints:", "Standard microcontrollers lack RAM/compute for heavy audio models; running inference requires strict int8 quantization and efficient DSP framing."),
        ("Physical Sound Velocity Realities:", "Sound in water travels at ~1,480 m/s (6.7 ms per 10m). Naive Wi-Fi/NTP clock subtraction suffers 10-50ms jitter, demanding frequency-domain cross-correlation."),
        ("Network Outage Vulnerability:", "Cloud-dependent architectures fail to isolate leaks during connectivity dropouts, leading to continuous flooding.")
    ]
    for h, b in challenges:
        p = tf_c.add_paragraph()
        p.text = f"• {h} "
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = PRIMARY
        p.space_before = Pt(7)
        r = p.add_run()
        r.text = b
        r.font.bold = False
        r.font.color.rgb = MUTED

    # Right Box: The Clear Research Gap
    g_card = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(1.6), Inches(5.6), Inches(5.2))
    g_card.fill.solid()
    g_card.fill.fore_color.rgb = RGBColor(239, 246, 255) # Light blue
    g_card.line.color.rgb = ACCENT_BLUE
    g_card.line.width = Pt(1.5)

    tb_g = slide5.shapes.add_textbox(Inches(7.2), Inches(1.85), Inches(5.0), Inches(4.7))
    tf_g = tb_g.text_frame
    tf_g.word_wrap = True
    tf_g.margin_top = tf_g.margin_left = tf_g.margin_right = tf_g.margin_bottom = 0

    p = tf_g.paragraphs[0]
    p.text = "The Research Gap Our Project Bridges"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE

    gaps = [
        ("Ultra-Low Cost Accessibility (<₹2,500):", "Bridging the massive price chasm between inaccessible ₹1,00,000+ proprietary industrial loggers and basic non-intelligent sensors."),
        ("Non-Invasive Structural Coupling:", "Engineering a contact piezoelectric interface with charge amplification that senses pipe turbulence without pipe drilling or fluid contamination."),
        ("True Edge AI Autonomy (TinyML):", "Quantized CNN running 100% on-device (ESP32-S3), achieving sub-200ms classification of micro-leaks vs. normal flow vs. room noise."),
        ("Integrated Mechanical Actuation:", "Closing the loop between detection and mitigation: immediate sub-second motorized shutoff before structural damage occurs.")
    ]
    for h, b in gaps:
        p = tf_g.add_paragraph()
        p.text = f"✔ {h} "
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = PRIMARY
        p.space_before = Pt(7)
        r = p.add_run()
        r.text = b
        r.font.bold = False
        r.font.color.rgb = MUTED

    # ==========================================
    # SLIDE 6: Project Objectives
    # ==========================================
    slide6 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide6)
    add_header(slide6, "Project Objectives & Scope Boundaries")

    objs = [
        ("1. Non-Invasive Sensing Hardware", "Design a non-intrusive clamp-on sensor unit using contact piezoelectric transducers paired with an LM358 active charge amplifier and >500 Hz high-pass analog filter to isolate pipe vibration."),
        ("2. Embedded DSP Feature Extraction", "Implement an onboard 16 kHz sampling and signal processing pipeline generating 2D Log-Mel Spectrograms tuned specifically to 1–8 kHz fluid turbulence frequencies."),
        ("3. Edge AI (TinyML) Classification", "Train, post-training quantize (int8), and execute a lightweight CNN on the ESP32-S3 via TFLite Micro, targeting >90% classification accuracy with <200ms latency and <64KB SRAM usage."),
        ("4. Autonomous Fail-Safe Actuation", "Interface a 5V optoisolated relay module to trigger a 12V motorized solenoid shutoff valve within 1 second of confirmed leak classification without needing cloud commands."),
        ("5. Low-Bandwidth Wireless Telemetry", "Transmit lightweight MQTT JSON event packets over Wi-Fi only upon state transitions, achieving >99% bandwidth savings over raw audio streaming.")
    ]

    for i, (title, desc) in enumerate(objs):
        y = Inches(1.6 + i * 1.05)
        card = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), y, Inches(11.7), Inches(0.95))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = BORDER_COL

        tb = slide6.shapes.add_textbox(Inches(1.0), y + Inches(0.08), Inches(11.3), Inches(0.8))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_top = tf.margin_left = tf.margin_right = tf.margin_bottom = 0

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = ACCENT_BLUE

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = MUTED
        p2.space_before = Pt(2)

    # ==========================================
    # SLIDE 7: Proposed Methodology & System Architecture
    # ==========================================
    slide7 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide7)
    add_header(slide7, "Proposed Methodology & System Architecture")

    # Embed the high-resolution architecture diagram generated in P2-S1
    if os.path.isfile(architecture_image):
        slide7.shapes.add_picture(architecture_image, Inches(0.8), Inches(1.5), width=Inches(8.2))

    # Right side: Architecture Highlights & Trade-offs
    card_arch = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.2), Inches(1.5), Inches(3.3), Inches(5.3))
    card_arch.fill.solid()
    card_arch.fill.fore_color.rgb = CARD_BG
    card_arch.line.color.rgb = BORDER_COL

    tb_a = slide7.shapes.add_textbox(Inches(9.4), Inches(1.7), Inches(2.9), Inches(4.9))
    tf_a = tb_a.text_frame
    tf_a.word_wrap = True
    tf_a.margin_top = tf_a.margin_left = tf_a.margin_right = tf_a.margin_bottom = 0

    p = tf_a.paragraphs[0]
    p.text = "System Architecture Highlights"
    p.font.size = Pt(11.5)
    p.font.bold = True
    p.font.color.rgb = PRIMARY

    notes = [
        ("FreeRTOS Dual-Core:", "Core 0 handles 16 kHz DMA sampling & DSP FFT; Core 1 handles TFLite Micro inference & MQTT dispatch."),
        ("Component Trade-Off:", "ESP32-S3 chosen over Raspberry Pi (₹650 vs ₹4,500; 500mW vs 5W) and Arduino Uno (has vector instructions & SRAM)."),
        ("Sensor Coupling:", "Piezoelectric contact transducer selected over airborne MEMS to eliminate room background chatter."),
        ("Cost Efficiency:", "Complete edge node built under ₹1,800 vs ₹1,00,000+ proprietary commercial loggers.")
    ]
    for h, b in notes:
        p = tf_a.add_paragraph()
        p.text = f"• {h} "
        p.font.size = Pt(9)
        p.font.bold = True
        p.font.color.rgb = ACCENT_TEAL
        p.space_before = Pt(6)
        r = p.add_run()
        r.text = b
        r.font.bold = False
        r.font.color.rgb = MUTED

    # ==========================================
    # SLIDE 8: Results / Initial Implementation (~20% Milestone)
    # ==========================================
    slide8 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide8)
    add_header(slide8, "Results: Initial Implementation (~20% Completion Milestone)")

    # Left Column: Implementation Points Card
    card_l8 = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.4), Inches(5.4))
    card_l8.fill.solid()
    card_l8.fill.fore_color.rgb = CARD_BG
    card_l8.line.color.rgb = BORDER_COL

    tb8 = slide8.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.0), Inches(5.0))
    tf8 = tb8.text_frame
    tf8.word_wrap = True
    tf8.margin_top = tf8.margin_left = tf8.margin_right = tf8.margin_bottom = 0

    p = tf8.paragraphs[0]
    p.text = "20% Prototype Deliverables Completed"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE

    res_points = [
        ("16 kHz Audio DMA Sampling Pipeline:", "Implemented circular double buffering and Hanning windowing to ingest continuous structural acoustic vibrations on ESP32 Core 0."),
        ("Real-Time Log-Mel Spectrogram Engine:", "Engineered 32-band filterbank conversion scaled to 0.5–8 kHz fluid turbulence frequencies, generating 2D feature maps."),
        ("Empirical Spectral Energy Elevation:", "Experimental frequency sweeps confirm >30 dB spectral density surge in 1.5–4.5 kHz band during needle-valve micro-cracks vs. laminar flow."),
        ("Dual-Core FreeRTOS Task Architecture:", "Decoupled sampling/DSP (Core 0) from TinyML inference and actuation state machines (Core 1)."),
        ("Sub-Second Solenoid Shutoff Logic:", "Validated fail-safe GPIO relay trigger executing in <50ms upon simulated anomaly condition.")
    ]
    for h, b in res_points:
        p = tf8.add_paragraph()
        p.text = f"✔ {h} "
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = PRIMARY
        p.space_before = Pt(7)
        r = p.add_run()
        r.text = b
        r.font.bold = False
        r.font.color.rgb = MUTED

    # Right Column: Empirical Spectral Comparison Plot
    spec_img = "presentation/assets/spectral_comparison.png"
    if os.path.isfile(spec_img):
        card_r8 = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.5), Inches(1.5), Inches(6.0), Inches(5.4))
        card_r8.fill.solid()
        card_r8.fill.fore_color.rgb = CARD_BG
        card_r8.line.color.rgb = BORDER_COL

        tb_spec_title = slide8.shapes.add_textbox(Inches(6.7), Inches(1.7), Inches(5.6), Inches(0.5))
        tf_st = tb_spec_title.text_frame
        tf_st.word_wrap = True
        p = tf_st.paragraphs[0]
        p.text = "Empirical Proof: Laminar Flow vs. Micro-Leak Turbulence"
        p.font.size = Pt(11.5)
        p.font.bold = True
        p.font.color.rgb = PRIMARY

        slide8.shapes.add_picture(spec_img, Inches(6.65), Inches(2.2), width=Inches(5.7))

        tb_spec_cap = slide8.shapes.add_textbox(Inches(6.7), Inches(5.3), Inches(5.6), Inches(1.3))
        tf_sc = tb_spec_cap.text_frame
        tf_sc.word_wrap = True
        p = tf_sc.paragraphs[0]
        p.text = "Spectrogram Feature Verification: Notice the prominent energy surge (yellow/orange bands) across 1.5–5 kHz in the right plot, reflecting continuous hydrodynamic turbulence used as the input tensor for our TinyML model."
        p.font.size = Pt(8.5)
        p.font.italic = True
        p.font.color.rgb = MUTED

    # Save presentation
    prs.save(output_path)
    print(f"[SUCCESS] Generated Review II presentation at: {output_path}")

if __name__ == "__main__":
    create_deck("presentation/Review2_Presentation.pptx", "presentation/assets/system_architecture.png")
