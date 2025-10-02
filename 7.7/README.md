# RH NB/BD v28 — Hutch++, PCG, Contradiction Auto-Report

## What's new
- `code/hutchpp.py`: Hutch++ trace estimator to bound ‖E‖ with matvec-only API.
- `code/pcg_precond.py`: PCG with diagonal+band preconditioner.
- `code/contradiction_report.py`: reads CSV, checks persistence vs. θ and optional Hutch++ bound → JSON report.
- `code/plot_update.py`: update plot from CSV.
- `main_v28.tex`: Overleaf-ready, referencing all components.

## Quick start
1) Append results to `data/results_v28.csv` (same schema as v27).
2) Plot:
   ```bash
   python3 code/plot_update.py
   ```
3) Optional report:
   ```bash
   python3 code/contradiction_report.py
   ```
4) Compile LaTeX (`main_v28.tex`).

Notes: Supply your own Emul/ETmul to use Hutch++ on A=E^T E via `make_AtA`.
