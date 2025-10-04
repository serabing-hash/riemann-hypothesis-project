# RH via NB/BD — Orthodox v3.8 Package

This package contains a cleaned, orthodox presentation of the weighted Hilbert lemma route to NB/BD stability.

## Contents
- `main.tex` — 6–7 page LaTeX note. Safer statements; explicit ε–θ bookkeeping; near-normality via commutator.
- `figures/`
  - `band_constants_vs_eps.png` — Band constants profile vs. ε.
  - `band_partial_sums.png` — Convergence of ∑ C_j (schematic).
  - `commutator_decay_multi.png` — Commutator decay ~ (log N)^(-2θ) for θ ∈ {0.2,0.3,0.4}.
- `code/`
  - `make_figures.py` — Regenerates figures.

## Compile
Upload the folder (or zip) to Overleaf and compile `main.tex` (pdfLaTeX).

## Notes
- The figures are schematic sanity checks, not empirical ζ-data. Replace with real numerics if desired.
- The lemma isolates the *off-diagonal* effect. For a full RH proof, additional analytic control is required.
