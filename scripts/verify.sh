#!/usr/bin/env bash
# Cumulative Verification Gate Script
# Usage: ./scripts/verify.sh <LAST_DONE_STEP>
# Example: ./scripts/verify.sh P2-S1

set -e

if [ -z "$1" ]; then
  echo "Error: Must provide the target step to verify (e.g., P2-S1)"
  exit 1
fi

TARGET_STEP=$1
echo "============================================="
echo "Running Cumulative Verification up to $TARGET_STEP"
echo "============================================="

# P1-S1
if [[ "$TARGET_STEP" == "P1-S1" || "$TARGET_STEP" > "P1-S1" ]]; then
    echo "Verifying P1-S1..."
    if [ ! -f "idea.md" ]; then echo "Fail: idea.md missing"; exit 1; fi
    echo "[PASS] P1-S1"
fi

# P2-S1
if [[ "$TARGET_STEP" == "P2-S1" || "$TARGET_STEP" > "P2-S1" ]]; then
    echo "Verifying P2-S1..."
    if [ ! -f "presentation/review2_slides.md" ]; then echo "Fail: presentation/review2_slides.md missing"; exit 1; fi
    if ! grep -q "Architecture" presentation/review2_slides.md; then echo "Fail: 'Architecture' not found in slides"; exit 1; fi
    echo "[PASS] P2-S1"
fi

# P2-S2
if [[ "$TARGET_STEP" == "P2-S2" || "$TARGET_STEP" > "P2-S2" ]]; then
    echo "Verifying P2-S2..."
    if [ ! -f "platformio.ini" ]; then echo "Fail: platformio.ini missing"; exit 1; fi
    if ! grep -q "esp32-s3-devkitc-1" platformio.ini; then echo "Fail: Board missing in platformio.ini"; exit 1; fi
    echo "[PASS] P2-S2"
fi

echo "============================================="
echo "[SUCCESS] All cumulative checks passed up to $TARGET_STEP!"
exit 0
