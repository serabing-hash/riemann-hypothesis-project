# v13.3 Package (NB/BD heuristic record)

Contents
- paper_v13_3.tex  — LaTeX source (2–3 pp)
- figure1.png      — Comparative log–log (Base / Previous / v13 Finale)
- appendix_code.py — Reproducibility (OLS/ridge demo, zero-free boost sketch)
- table1.csv       — Main requested row (N=5,000,000)

Build
1) Ensure LaTeX environment (pdflatex) is available.
2) Compile:
   pdflatex paper_v13_3.tex
   (Run twice for references.)

Notes
- Colors/legend follow the spec: Base (black/red), Previous (colored), v13 Finale (teal/brown dashed).
- Appendix code saves a demo plot as figure1_demo.png for quick verification.
- All numbers match v13 line: η≈0.35→0.5075 (ε=0.08), θ: 0.03→0.280, R²: 0.008→0.315,
  N=5M: MSE+=0.098, MSE-=0.185, MSE*=0.145; ridge(5k): 12% improvement; w_-=1.2.

Disclaimer
Heuristic numerical record; no RH proof is claimed.
