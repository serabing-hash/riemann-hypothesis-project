
# RH v3.1 (Consolidated Edition)

This package merges the orthodox mathematical write-up with the experimental visuals for the NB/BD stability track.

## Contents
- `main.tex` — LaTeX source (v3.1 consolidated)
- `figures/figure1_mse_star.png` — Combined MSE* vs N (rebuilt)
- `figures/figure2_boundaries.png` — Boundary reweighting bars (rebuilt)
- `data_ref.csv` — N, MSE+, MSE-, MSE* table (weighted w_- = 1.20, σ = 0.05)
- `appendix_code.py` — Minimal plotting script to regenerate figures

## Build
If you compile locally:
```
pdflatex main.tex
bibtex main (if you add a .bib)
pdflatex main.tex
pdflatex main.tex
```
On Overleaf, upload the whole zip and set `main.tex` as the main file.
