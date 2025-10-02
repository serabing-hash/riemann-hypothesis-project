# NB/BD Project Final Package (vFinal)

This package contains the final version of our work on the Riemann Hypothesis via the Nyman–Beurling–Báez-Duarte criterion.

## Contents
- `main_final.tex`: Overleaf-ready LaTeX source (4 pages, with appendix)
- `figures/vfinal_scaling.png`: Final combined scaling figure
- `results/*.csv`: Numerical experiment data (N up to 20k, preliminary 100k)
- `README.md`: This file

## Key Contributions
- Weighted Hilbert lemma with Möbius coefficients, calibrated ($\eta>0.2$, $c≈0.35$).
- Numerical results: $N=8k$–$20k$, weighted MSE decays $\sim (\log N)^{-θ}$ with $θ≈5.94$.
- Preliminary extrapolation to $N=100k$: MSE≈0.0090, CI [0.0085,0.0095].
- Variance reduction under narrower Gaussian weight ($T_w=115$).

## Limitations
- Not a full proof of RH. Requires analytic continuation and functional equation control.
- Current numerical range limited to $N=20k$ (dedicated runs for $N=100k$ suggested).

## Citation
Serabi (2025). *Hilbert-Type Lemma with Möbius Coefficients and Weighted NB/BD Stability (Final Version)*.
Zenodo: https://zenodo.org/records/17230129
GitHub: https://github.com/serabing-hash/riemann-hypothesis-project
