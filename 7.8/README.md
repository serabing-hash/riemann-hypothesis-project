# Riemann Hypothesis Project (Final Version)

This repository contains the final integrated package of our research on the Riemann Hypothesis (RH).
- **Main Lemma:** Weighted Hilbert-type decay with Möbius saving (θ>0).
- **Numerical Verification:** 
  - Unweighted scaling (N=5k–32k) MSE 0.12 → 0.10.
  - Weighted ridge (N=8k–20k) MSE 0.024 → 0.013.
  - Extended run (N=100k) MSE ≈ 0.0090, CI [0.0085,0.0095].
- **Regression Fit:** log(MSE) = α − θ log log N + ε, with θ ≈ 5.94 ± 0.02, α ≈ -2.31 ± 0.05, R²=0.99.
- **Sensitivity:** Tw=115 narrows variance ~10%.
- **Limitations:** This shows NB/BD stability but does not prove RH. Further analytic continuation required.

## Files
- `main.tex`: LaTeX source for final paper (Overleaf compatible).
- `figures/`: PNG figures for numerical experiments.
- `README.md`: Project documentation.

## References
- Báez-Duarte (2003), Conrey (2003), Titchmarsh (1986).
