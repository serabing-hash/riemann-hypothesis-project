# Riemann Hypothesis – NB/BD Criterion Numerical Project (v9.4)

This package contains the LaTeX source, numerical results, and figures for our exploration of the Riemann Hypothesis (RH) using the Nyman–Beurling–Báez-Duarte (NB/BD) framework.

## Contents
- `main_v9_4.tex` – Full LaTeX source of the paper.
- `riemann_v8_3.pdf` – Earlier compiled version.
- `results_w12.csv`, `v9_3_regression_summary.csv` – Numerical data.
- `figures/` – Actual experiment output PNGs:
  - `unweighted_scaling.png`
  - `weighted_scaling.png`
  - `plateau_resolution.png`

## Summary
- **Hilbert-type lemma** with Möbius coefficients suppresses off-diagonal terms by $(\log N)^{-\theta}$.
- **Numerical results** up to $N=10^5$ show decay of $d_N$ and weighted MSE $\to 0$.
- **Stability** is confirmed, but **not a full proof** of RH. Further analytic tools (functional equation, $\varepsilon$–$\delta$ bounds) are required.

## References
- Báez-Duarte (2003), *A strengthening of the Nyman–Beurling criterion*.
- Conrey (2003), *The Riemann Hypothesis*.
- Titchmarsh (1986), *The Theory of the Riemann Zeta-Function*.