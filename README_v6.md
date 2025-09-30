# Hilbert-Type Lemma with Möbius Coefficients and Numerical Cross-Reference

## Overview
This project presents a weighted Hilbert-type lemma for Möbius-weighted coefficients and its corollary for the stability of the Nyman–Beurling/Báez-Duarte criterion.  

- **Main result**: Off-diagonal contributions in the normal equations are suppressed by a logarithmic factor, ensuring stability and decay of the NB/BD approximation error.  
- **Numerical evidence**: Ridge-regularized least squares computations up to `N = 20,000` confirm the lemma’s predictions. Plateaus observed at large `N` are resolved by introducing low-frequency sine basis functions.  

The project combines **theoretical analysis** (LaTeX writeup) and **numerical experiments** (Python/Matplotlib output figures).

---

## File Contents
- `RH_v6.tex`  
  Full LaTeX source of the paper section, including:
  - Lemma, Corollary, and Proof Sketch
  - Numerical cross-reference with included figures
  - References

- `unweighted_scaling.png`  
- `ridge_scaling.png`  
- `plateau_resolution_7basis.png`  
  Numerical plots showing unweighted decay, ridge scaling, and plateau resolution.

- `hilbert_lemma_crossref.tex.pdf`  
  Precompiled PDF of the core lemma and discussion, ready to cite or embed in other work.

- `reader.md`  
  Short reader-friendly summary for Zenodo or metadata upload.

---

## Usage
### Compile LaTeX
Open `main.tex` in [Overleaf](https://overleaf.com) or run locally:
```bash
pdflatex main.tex
