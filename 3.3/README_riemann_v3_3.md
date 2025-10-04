# v3.3 Operator Framework Package

This package contains the LaTeX source and a diagram for the **operator/functional-equation** route toward RH.

## Files
- `v3_3_operator_framework.tex` — 3-page LaTeX note (Overleaf-ready).
- `operator_framework_v3_3.png` — Operator roadmap figure (include via `\includegraphics`).
- `README_riemann_v3_3.md` — This file.

## How to compile (Overleaf)
1. Upload all files.
2. In your main document, add:
   ```latex
   \usepackage{graphicx}
   ```
3. Insert the figure:
   ```latex
   \begin{figure}[t]
   \centering
   \includegraphics[width=.9\linewidth]{operator_framework_v3_3.png}
   \caption{Operator roadmap for RH.}
   \end{figure}
   ```
4. Compile with pdfLaTeX.

## Notes
- The document is **not** a proof of RH. It formalizes a clean operator template aligned with NB/BD stability and a weighted Hilbert kernel.
- Next versions (v3.4+) will add quantitative bounds for the compact remainder and symmetry domain issues.
