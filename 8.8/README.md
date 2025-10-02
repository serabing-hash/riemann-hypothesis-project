# NB/BD Project Final Package

This is the final research package (v9.4).

## Contents
- `main.tex`: LaTeX source of the final paper.
- `figures/`: Contains PNG figures.
- `results.csv`: Numerical results table.
- `README.md`: This file.

## Build Instructions
1. Ensure LaTeX is installed (TeX Live, MikTeX, or Overleaf).
2. Place the `figures/` folder in the same directory as `main.tex`.
3. Run:
   ```bash
   pdflatex main.tex
   bibtex main
   pdflatex main.tex
   pdflatex main.tex
   ```

The output will be `main.pdf`.
