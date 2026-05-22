#!/usr/bin/env python3
"""Validate and publish the NAB Figure Drawing Form 2 scoring dashboard.

The dashboard HTML is maintained in nab_scoring_dashboard.html alongside this script.
The stimulus overlay uses the official figure image:
  nab_figure_drawing_stimulus_form_02.png

Run:
    uv run generate_updated_dashboard.py
"""

from pathlib import Path

FORM_DIR = Path(__file__).resolve().parent
DASHBOARD_PATH = FORM_DIR / "nab_scoring_dashboard.html"
STIMULUS_PATH = FORM_DIR / "nab_figure_drawing_stimulus_form_02.png"
STIMULUS_SRC = "nab_figure_drawing_stimulus_form_02.png"


def main() -> None:
    if not DASHBOARD_PATH.exists():
        raise SystemExit(f"Dashboard HTML not found: {DASHBOARD_PATH}")

    if not STIMULUS_PATH.exists():
        raise SystemExit(
            f"Stimulus overlay image not found: {STIMULUS_PATH}\n"
            f"Expected file: {STIMULUS_SRC}"
        )

    html = DASHBOARD_PATH.read_text(encoding="utf-8")

    if STIMULUS_SRC not in html:
        raise SystemExit(
            f"Dashboard HTML does not reference {STIMULUS_SRC}. "
            "The overlay must use the official stimulus image, not an SVG schematic."
        )

    if "stimulus-svg" in html or 'stroke="#dc2626"' in html:
        raise SystemExit(
            "Dashboard still contains the old red SVG overlay. "
            "Replace it with an <img id=\"stimulus-overlay\"> using the stimulus PNG."
        )

    DASHBOARD_PATH.write_text(html, encoding="utf-8")
    print(f"Dashboard ready: {DASHBOARD_PATH}")
    print(f"Stimulus overlay: {STIMULUS_PATH}")
    print("Open nab_scoring_dashboard.html in your browser to score.")


if __name__ == "__main__":
    main()
