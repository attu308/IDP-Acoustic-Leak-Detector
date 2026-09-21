#!/usr/bin/env bash
# Cumulative Verification Gate Script
# Usage: ./scripts/verify.sh <LAST_DONE_STEP>
# Example: ./scripts/verify.sh P2-S1

set -e

if [ -z "$1" ]; then
  echo "Error: Must provide the target step to verify (e.g., P2-S1)"
  exit 1
fi

TARGET_STEP=$(echo "$1" | tr '[:lower:]' '[:upper:]')
echo "============================================="
echo "Running Cumulative Verification up to $TARGET_STEP"
echo "============================================="

# Define ordered sequence of steps
STEPS=(
    "P1-S1"
    "P2-S1"
    "P2-S2"
    "P2-S3"
    "P2-S4"
    "P2-S5"
    "P2-S6"
    "P3-S1"
    "P3-S2"
    "P3-S3"
    "P3-S4"
    "P4-S1"
    "P4-S2"
    "P4-S3"
    "P4-S4"
    "P5-S1"
    "P5-S2"
    "P5-S3"
    "P5-S4"
    "P6-S1"
    "P6-S2"
    "P6-S3"
    "P7-S1"
    "P7-S2"
)

FOUND=0
for STEP in "${STEPS[@]}"; do
    echo "Verifying $STEP..."
    python3 scripts/verify_step.py "$STEP"
    if [ "$STEP" == "$TARGET_STEP" ]; then
        FOUND=1
        break
    fi
done

if [ "$FOUND" -eq 0 ]; then
    echo "Warning: Target step $TARGET_STEP not found in standard step list."
    python3 scripts/verify_step.py "$TARGET_STEP"
fi

echo "============================================="
echo "[SUCCESS] All cumulative checks passed up to $TARGET_STEP!"
exit 0
