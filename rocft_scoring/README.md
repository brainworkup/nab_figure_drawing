# Rey-Osterrieth Complex Figure (ROCFT) Interactive Scoring Dashboard

A self-contained HTML tool for **manual clinician scoring** of the ROCFT,
modeled on the NAB Figure Drawing dashboard (`../form_02/nab_scoring_dashboard.html`).
No build step, no server. Styling/icons load via Tailwind + Font Awesome CDNs; optional Word export uses the html-docx-js CDN (the rest of the tool works without it).

## Open it

Just open `rocft_scoring_dashboard.html` in any browser. Keep the two image files
alongside it (they're referenced by relative path).

## What it does

- **18-unit Osterrieth scoring** — each unit scored `0 / 0.5 / 1 / 2` (max **36**),
  across **three trials**: Copy, Immediate Recall, Delayed Recall.
- **Age-banded norms** (Meyers & Meyers, 1995; ages 22–79) — enter the examinee's
  age to get z-score, percentile, and classification per trial.
- **% Retention** (Delayed/Copy, with Immediate/Copy shown alongside).
- **Qualitative matrix** (rotation, perseveration, confabulation, fragmentation,
  micro/macrographia, asymmetry, hemispatial neglect) per trial.
- **Organizational approach** rating (per trial) + **per-trial construction-order**
  (colored-pencil) logs for Copy, Immediate, and Delayed.
- **Stimulus overlay** viewer (upload the examinee drawing, overlay the canonical
  figure with adjustable opacity/scale/rotation/offset) + **18-unit reference map**.
- **Auto-generated, editable clinical narrative**.
- **Report export** (Summary tab) — one full report (scores + norms + qualitative +
  narrative) you can:
  - **Copy** to clipboard (Markdown)
  - download as **Markdown** (`.md`)
  - download as **Quarto** (`.qmd`, with YAML front-matter) → run
    `quarto render <file>.qmd --to pdf` (or `--to docx` / `--to html`) for a
    branded, print-ready document
  - download as **Word** (`.docx`, via the html-docx-js CDN — needs internet)
  - **PDF** via the browser's print-to-PDF (opens a clean report-only view)
- **Save/restore**: JSON Export / Import (clinician-controlled files) plus same-tab
  autosave (sessionStorage — survives reload, not persisted long-term).
- **Print** — print CSS renders the Summary & Report tab cleanly.

This is a manual scoring aid; it does **not** auto-score from an image.

## Assets

| File | Source | How generated |
|---|---|---|
| `rocft_stimulus.png` | Rey figure stimulus PDF (source not committed) | `pdftoppm -png -r 200` then `magick -trim +repage` |
| `rocft_18unit_schematic.jpg` | Langer et al. (*eLife* 2024) figure (CC-BY; source not committed) | copied |

Unit labels follow the Osterrieth (1944) / Meyers & Meyers (1995) 18-item system,
matching the official score sheet (source not committed).
