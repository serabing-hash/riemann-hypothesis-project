# CSF v9.0 — Cancellation Symmetry Framework (Final)

This package consolidates the analytic & numerical pieces of the NB/BD project under the **CSF** interpretation.

## Files
- `main.tex` — LaTeX source (compile with pdfLaTeX/XeLaTeX).
- `figures/` — PNG figures:
  - `unweighted_scaling.png`
  - `weighted_scaling.png`
  - `boundary_reweighting.png`
- `results_unweighted_ci.csv` — Unweighted scaling with 95% CI.
- `results_w12.csv` — Weighted runs (σ=0.05, w_- = 1.2).

## Notes
- Regression in `weighted_scaling.png` fits `log(MSE*) = a + b log log N`; we report `θ = -b` on the plot.
- We intentionally exclude unverified projections (e.g., `N=100000`) from the fit.
- CSF emphasizes **cancellation–symmetry–stability**; this is **not** a proof of RH.
