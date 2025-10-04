# v2.9 Orthodox Package (ε–δ Hilbert Framework)

This package provides a mathematics-first consolidation of the weighted Hilbert approach to NB/BD stability.

## Files
- `main.tex` — Article with ε–δ lemma and stability consequence.
- `appendix.tex` — Minimal Python toy code (verbatim) and notes.
- `figures/fig1_framework.png` — Schematic flow figure.
- `code/hilbert_toy.py` — Standalone toy script (same as in appendix).

## Compile
Use LaTeX twice for references:
```
pdflatex main.tex
pdflatex main.tex
```

## Disclaimer
This package does **not** claim a proof of RH; it formalizes an analytic stability mechanism.