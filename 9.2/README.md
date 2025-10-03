# CSF v9.2 (math.CA-aligned)

Changes from v9.1:
- **Title revised** to emphasize the framework and explicit exponent.
- **Explicit exponent**: θ(δ) ≍ min{η, δ} stated in Lemma and abstract.
- Figures & table regenerated from a single source CSV.
- Regression definition fixed: `log(MSE*) = a + b log log N`, θ := −b.
- No unverified N=100000 rows.

## Files
- `main.tex` — LaTeX source (explicit θ(δ) estimate, math.CA tone).
- `data/results_w12.csv` — dataset (σ=0.05, w_- = 1.2).
- `figures/weighted_scaling.png` — combined MSE with OLS (θ = -0.49, R² = 0.72).
- `figures/boundary_reweighting.png` — boundary-wise MSEs.

## Compile
Use pdfLaTeX or XeLaTeX. Ensure `figures/` and `data/` are alongside `main.tex`.

## Disclaimer
Analytic stability study; not a proof of RH.
