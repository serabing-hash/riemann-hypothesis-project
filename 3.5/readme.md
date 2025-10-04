# v3.5 — Operator–Spectral Roadmap toward RH (NB/BD)

This release packages a theory-first, reproducible scaffold:

- **Focus**: Weighted discrete Hilbert operator for NB/BD, band partition, Möbius-weighted coefficients.
- **Goal**: Stability of NB/BD normal equations; not an RH proof.
- **New in v3.5**: Clean operator statement, proof-scope remark, spectral roadmap (near-normality → compact tail → Fredholm stability). No plotting deps.

## Build (LaTeX)
- Overleaf: upload `main.tex` and compile.
- Local: `pdflatex main.tex` (twice if needed).

## Minimal prototype (no matplotlib)
`code/prototype_spectral_nb_bd.py` builds a toy kernel and checks norms.
It runs on NumPy-only machines.

## Next steps
- Make per-band constants explicit.
- Plug zero-free input to extract quantitative θ.
- Integrate explicit formula with the operator kernel.

Author: Serabi — 24ping@naver.com
License: MIT