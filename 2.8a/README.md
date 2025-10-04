# v2.8 Verification Package (Internal)

This package contains the internal verification edition (v2.8) of the refined, **orthodox** NB/BD framework.

## Contents
- `main.tex`: Paper body (compile with pdfLaTeX).
- `appendix.tex`: Supplementary details referenced by `main.tex`.
- `figures/`: Self-contained illustrative PNGs used by `main.tex`.
- `data/mse_data.csv`: Sample (N, MSE*) pairs for internal regression checks.
- `data/ols_fit.py`: Minimal OLS script to fit `log MSE* = a + b log log N`.

## Compile
```
pdflatex main.tex
pdflatex main.tex
```
(run twice for references).

> Note: The provided figures are illustrative to keep the build self-contained.
Replace them with higher-fidelity plots if you have newer data.
