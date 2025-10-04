# Serabi v3.0 Academic (Orthodox) Package

This project contains an Overleaf-ready LaTeX paper and a reproducible Python script for the weighted NB/BD stability study.

## How to build (Overleaf)
1. Upload this entire folder (ZIP) to Overleaf via **Upload Project**.
2. Open `main.tex` and click **Recompile**.
3. The PDF should compile with figures. The bibliography uses `references.bib`.

## Reproducibility
- Run `appendix_code.py` (Python 3.9+, NumPy, SciPy, Matplotlib).  
  It will print regression coefficients and regenerate `figures/weighted_scaling.png`.

### Current regression (from this package)
- a = -1.9217
- b = 0.0640
- theta = -0.0640
- R^2 = 0.053

## Files
- `main.tex` : paper
- `abstract.tex` : abstract
- `references.bib` : references
- `appendix_code.py` : reproducibility script
- `figures/*.png` : included figures

