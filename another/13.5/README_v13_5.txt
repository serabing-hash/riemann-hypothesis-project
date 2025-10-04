
v13.5 Incremental Zero-Free Simulation Package
==============================================

Files:
- riemann_v13_5.tex : LaTeX paper (Overleaf-ready).
- figure3.png : Comparative log–log regression (base vs. v13.5 extended).
- data_v13_5.csv : Dataset (base ≤10M + v13.5 simulated 20M point).
- results_v13_5.csv : OLS results for base and extended fits.
- analysis_v13_5.py : Reproducible Python code (generates CSVs and figure).

Key numbers (computed here):
- Base fit (≤10M): a=-1.099964, b=-0.291886, theta=0.291886, R2=0.673733
- Extended fit (≤20M incl. v13.5): a=-1.052557, b=-0.311912, theta=0.311912, R2=0.736454

Notes:
- The 20M point (MSE*: 0.141; MSE+ 0.092; MSE- (w_-=1.2) 0.175) is a simulated, heuristic entry
  derived from an assumed zero-free strip ε=0.10 and boundary reweighting. It is not a
  direct large-scale computation. Treat as exploratory evidence only.
- No claim of an RH proof is made.
