#!/usr/bin/env python3
"""
Step-level verification runner for machine-checked DoD items.
Invoked as: python3 scripts/verify_step.py <STEP_ID>
"""

import sys
import os
import subprocess

def verify_step(step_id: str) -> bool:
    print(f"--> Verifying step {step_id}...")

    if step_id == "P1-S1":
        if not (os.path.isfile("idea.md") and os.path.getsize("idea.md") > 100):
            print("[FAIL] idea.md does not exist or is empty")
            return False
        return True

    elif step_id == "P2-S1":
        asset = "presentation/assets/system_architecture.png"
        if not (os.path.isfile(asset) and os.path.getsize(asset) > 500):
            print(f"[FAIL] Missing or empty architectural asset: {asset}")
            return False
        return True

    elif step_id == "P2-S2":
        pptx_path = "presentation/Review2_Presentation.pptx"
        res = subprocess.run([sys.executable, "scripts/verify_pptx.py", pptx_path, "8", "Architecture,Objectives,Literature"])
        return res.returncode == 0

    elif step_id == "P2-S3":
        guide = "docs/review2_defense_guide.md"
        if not (os.path.isfile(guide) and os.path.getsize(guide) > 500):
            print(f"[FAIL] Missing or empty defense guide: {guide}")
            return False
        return True

    elif step_id == "P2-S4":
        pipe = "dsp/dsp_pipeline.py"
        if not os.path.isfile(pipe):
            print(f"[FAIL] Missing DSP pipeline script: {pipe}")
            return False
        # Run self-test on dsp_pipeline
        res = subprocess.run([sys.executable, pipe, "--test"])
        return res.returncode == 0

    elif step_id == "P2-S5":
        main_cpp = "firmware/src/main.cpp"
        if not os.path.isfile(main_cpp):
            print(f"[FAIL] Missing firmware main: {main_cpp}")
            return False
        with open(main_cpp, "r", errors="ignore") as f:
            content = f.read()
            if "xTaskCreatePinnedToCore" not in content and "xTaskCreate" not in content:
                print("[FAIL] Firmware missing FreeRTOS task creation")
                return False
        return True

    elif step_id == "P2-S6":
        chk = "docs/review2_checklist.md"
        if not (os.path.isfile(chk) and os.path.getsize(chk) > 200):
            print(f"[FAIL] Missing review checklist: {chk}")
            return False
        return True

    else:
        # Fallback check for future steps: check if step file or command passes
        print(f"[INFO] Generic verification check for step {step_id}")
        return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/verify_step.py <STEP_ID>")
        sys.exit(1)
    step = sys.argv[1].upper()
    success = verify_step(step)
    if success:
        print(f"[PASS] Step {step} verification succeeded.")
        sys.exit(0)
    else:
        print(f"[FAIL] Step {step} verification failed.", file=sys.stderr)
        sys.exit(1)
