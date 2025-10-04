# NB/BD Stability via a Weighted Hilbert Lemma (v3.0) — Orthodox Package

This package contains a clean, publication-ready LaTeX note consolidating the orthodox (analytic number theory) line.
It compiles without any figures and is suitable for arXiv/Zenodo submission.

## Files
- `main.tex` — the LaTeX source
- `references.bib` — BibTeX references
- `build_instructions.txt` — step-by-step compile commands

## Quick compile
```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```
The output is `main.pdf`.