#!/usr/bin/env bash
# Cumulative Verification Gate Script
# Usage: ./scripts/verify.sh <LAST_DONE_STEP>
# Example: ./scripts/verify.sh P1-S1

set -e

if [ -z "$1" ]; then
  echo "Error: Must provide the target step to verify (e.g., P0-S1)"
  exit 1
fi

TARGET_STEP=$1
echo "============================================="
echo "Running Cumulative Verification up to $TARGET_STEP"
echo "============================================="

# P0-S1
if [[ "$TARGET_STEP" == "P0-S1" || "$TARGET_STEP" > "P0-S1" ]]; then
    echo "Verifying P0-S1..."
    if [ ! -f "presentation/slides.md" ]; then echo "Fail: presentation/slides.md missing"; exit 1; fi
    if ! grep -q "Agenda" presentation/slides.md; then echo "Fail: 'Agenda' not found in slides"; exit 1; fi
    echo "[PASS] P0-S1"
fi

# P0-S2
if [[ "$TARGET_STEP" == "P0-S2" || "$TARGET_STEP" > "P0-S2" ]]; then
    echo "Verifying P0-S2..."
    if [ ! -f "platformio.ini" ]; then echo "Fail: platformio.ini missing"; exit 1; fi
    if ! grep -q "esp32-s3-devkitc-1" platformio.ini; then echo "Fail: Board missing in platformio.ini"; exit 1; fi
    echo "[PASS] P0-S2"
fi

# Add subsequent steps here as the project progresses...

echo "============================================="
echo "[SUCCESS] All cumulative checks passed up to $TARGET_STEP!"
exit 0
