
# NB/BD Stability Baseline (v2.10)

**Status:** stable, reproducible demo; not a proof of RH.

## What's here
- `paper/riemann_v2_10.tex`: Clean LaTeX baseline with weighted Hilbert lemma (sketch) and a tiny numerical demo.
- `paper/references.bib`: Minimal references.
- `paper/figures/figure1.png`: Generated scaling figure (from `data/demo_results.csv`).
- `data/demo_results.csv`: Demo values (replace with your measurements).
- `code/run_demo.py`: Regenerates `figure1.png` from CSV.
- `code/requirements.txt`: `numpy`, `matplotlib` only.

## How to build
1. (Optional) Update `data/demo_results.csv` with your measurements.
2. `pip install -r code/requirements.txt`
3. `python code/run_demo.py`
4. Compile `paper/riemann_v2_10.tex` in Overleaf or locally (pdfLaTeX).

## Notes
- The figure is intentionally minimal (single-axes, no style overrides).
- All numbers in the CSV are placeholders for the demo.
