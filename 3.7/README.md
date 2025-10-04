\
# NB/BD Stability via a Weighted Hilbert Lemma — v3.7

This package extends v3.6 by:
- giving **explicit band-wise constants** \(C_j\) with a convergent model profile,
- adding a **worked estimate** for the \(j=1\) band,
- plotting a **near-normality** commutator decay schematic.

## How to build (Overleaf)
Upload the whole ZIP and compile `main.tex` with pdfLaTeX.

## How to rebuild figures locally
```bash
python code/band_constants_demo.py
python code/commutator_schematic.py
```
They will (re)write images into `figures/`.

## What to look for
- Eq. (1): kernel and band partition.
- Lemma 1: band-wise bound with \(\sum_j C_j<\infty\).
- Corollary: \(\|[E,E^\ast]\|\ll(\log N)^{-2\theta}\) near-normality.
- Appendix-style worked band \(j=1\) inside the main text.
