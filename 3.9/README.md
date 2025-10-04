# NB/BD Stability via a Weighted Hilbert Lemma (Orthodox v3.9)

This package is a conservative, overleaf-ready writeup of the weighted Hilbert lemma line.

## Files
- `main.tex` — LaTeX source (compiles on Overleaf).
- `figures/*.png` — schematic figures (safe placeholders; replace with real plots anytime).
- `code/make_figures.py` — regenerates the placeholder figures.
- `data/mse_weighted_template.csv` — template for future measured results.
- `CHANGELOG.md` — history from v3.8 to v3.9.

## How to compile
1. Upload the entire zip to Overleaf.
2. Ensure `main.tex` is the root document and click Compile.
3. To recreate figures locally:
   ```bash
   python code/make_figures.py
   ```

## Notes
- This is **not** a proof of RH. It is a rigorous stability scaffold for NB/BD.
- The text is toned for an orthodox submission: minimal claims, clear caveats, explicit MSC/keywords.
