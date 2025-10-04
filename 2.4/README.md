# NB/BD v2.4 (Orthodox Line) — Package

This package contains the LaTeX source for the v2.4 preprint in the orthodox analytic number theory line toward RH.

## Files
- `main.tex` — strengthened proof outline (log-band + Abel), hypothesis H_eta(beta) stated, unconditional remark, minimal numerical appendix.
- `README.md` — this file.
- `compile.sh` — convenience script for local PDF build.
- `numerics_minimal.csv` — small table mirrored from Appendix B (illustrative only).

## Compile
- Overleaf: create a new project, upload all files, and compile with pdfLaTeX.
- Local:
  ```bash
  pdflatex main.tex
  pdflatex main.tex
  ```

## Notes
- All central results are analytic; the CSV is only a sanity record.
