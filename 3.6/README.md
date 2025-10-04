# NB/BD Stability via a Weighted Hilbert Lemma (v3.6)

This package contains the v3.6 “Appendix 확장판”:
- **main.tex** — 4pp LaTeX preprint (band-by-band constants; spectral near-normality)
- **figures/band_constants_sum.png** — generated figure
- **code/band_constants_demo.py** — script to recompute the figure

## Compile (Overleaf or local)
1. Upload the entire ZIP to Overleaf, or place files in the same folder locally.
2. Compile `main.tex` with pdfLaTeX.
3. If the figure is missing, run:
   ```bash
   python code/band_constants_demo.py
   ```
   then recompile LaTeX.

## Math Highlights
- Decompose off-diagonal Hilbert interactions into logarithmic bands `B_j`.
- Each band contributes at most `C_j (log N)^{-1}` with
  `C_j ≍ exp(-c 2^{-j}) (2^{-j})^{1-ε}`, yielding a convergent sum and an overall
  `(log N)^{-θ}` decay (θ > 0).
- Near-normality: the commutator norm `||[E,E*]||` decays like `(log N)^{-2θ}`, improving
  stability of the Neumann series for `(I+E)^{-1}`.

## License
MIT
