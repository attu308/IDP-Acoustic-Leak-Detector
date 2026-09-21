#!/usr/bin/env python3
"""
Verification helper for PPTX presentation files.
Checks:
1. File exists and is non-empty.
2. Valid PPTX format (valid ZIP structure with ppt/presentation.xml).
3. Contains at least the required number of slides.
4. (Optional) Checks for required text strings across slide XMLs.
"""

import sys
import os
import zipfile
import re

def verify_pptx(file_path: str, min_slides: int = 1, required_keywords: list = None) -> bool:
    if not os.path.isfile(file_path):
        print(f"[FAIL] Presentation file not found: {file_path}", file=sys.stderr)
        return False

    size = os.path.getsize(file_path)
    if size < 1024:
        print(f"[FAIL] Presentation file too small ({size} bytes): {file_path}", file=sys.stderr)
        return False

    try:
        with zipfile.ZipFile(file_path, 'r') as z:
            names = z.namelist()
            if 'ppt/presentation.xml' not in names:
                print(f"[FAIL] Not a valid PPTX structure (missing ppt/presentation.xml): {file_path}", file=sys.stderr)
                return False

            slide_files = [n for n in names if re.match(r'^ppt/slides/slide\d+\.xml$', n)]
            slide_count = len(slide_files)

            if slide_count < min_slides:
                print(f"[FAIL] Found {slide_count} slides, expected at least {min_slides} in {file_path}", file=sys.stderr)
                return False

            if required_keywords:
                all_text = ""
                for s in slide_files:
                    try:
                        xml_content = z.read(s).decode('utf-8', errors='ignore')
                        all_text += " " + xml_content
                    except Exception:
                        pass
                for kw in required_keywords:
                    if kw.lower() not in all_text.lower():
                        print(f"[FAIL] Required keyword '{kw}' not found in presentation slides: {file_path}", file=sys.stderr)
                        return False

            print(f"[PASS] PPTX verification passed: {file_path} ({slide_count} slides, size {size} bytes)")
            return True

    except zipfile.BadZipFile:
        print(f"[FAIL] Corrupted or invalid ZIP archive for PPTX: {file_path}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"[FAIL] Unexpected error reading PPTX: {e}", file=sys.stderr)
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/verify_pptx.py <pptx_path> [min_slides] [keyword1,keyword2,...]")
        sys.exit(1)

    path = sys.argv[1]
    min_count = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    keywords = [k.strip() for k in sys.argv[3].split(',')] if len(sys.argv) > 3 else None

    success = verify_pptx(path, min_count, keywords)
    sys.exit(0 if success else 1)
