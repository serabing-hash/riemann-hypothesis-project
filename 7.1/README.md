# Riemann Hypothesis Project (v12)

This repository provides the research package for our exploration of the Riemann Hypothesis (RH).
We reformulate RH using two equivalent perspectives:

1. Explicit formulas for the Chebyshev function with truncation error control.
2. Nyman–Beurling–Báez-Duarte (NB/BD) criterion, expressed as an approximation problem.

## Key Contributions
- Reduction of RH to thin-band integer correlations, showing how near-diagonal pairs drive convergence.
- New coefficient constructions (multi-scale, phase-modulated Dirichlet polynomials).
- Numerical evidence (up to N=1e5) that diagonal sign stabilization and off-diagonal suppression can be achieved simultaneously.
- Weighted Hilbert lemma with Möbius coefficients, giving analytic stability.

## Numerical Results
- **Unweighted scaling** up to N=32,000 (Fig.1).
- **Dedicated run at N=100,000**, MSE ≈ 0.0090 ± 0.0005 (bootstrap SE).
- **Regression estimate**: θ ≈ 5.94 (R²=0.99) with sensitivity θ≈6.15 under narrower Gaussian weight (Fig.2).
- **Plateau resolution** by adding low-frequency sine basis (Tw=115) (Fig.3).

## Files
- `main_v12_full.tex`: Full LaTeX document.
- `figures/`: Contains all PNG plots for Overleaf inclusion.
- `results/exp_1e5.csv`: Raw numerical results for reproducibility.

## References
- Báez-Duarte (2003), DOI:10.1007/s10231-003-0074-5
- Conrey (2003), Notices AMS
- Titchmarsh (1986), *The Theory of the Riemann Zeta-Function*
