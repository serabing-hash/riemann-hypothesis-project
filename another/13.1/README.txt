v13.1 — Figure Bundle
---------------------
This zip contains:
- figure1.png — Comparative log–log plot for the paper.

How to use:
1) Put 'figure1.png' in the same folder as your LaTeX file (v13_1.tex).
2) Ensure the LaTeX source includes:

   \begin{figure}[t]
     \centering
     \includegraphics[width=0.9\linewidth]{figure1.png}
     \caption{Comparative log–log: base (black/red), previous (colored), v13 finale (teal/brown dashed).}
   \end{figure}

3) Compile with: pdflatex v13_1.tex  (or latexmk).

Notes:
- The plot uses synthetic illustrative curves consistent with the spec (base θ≈0.03 vs finale θ≈0.280 trend).
- If you already have code to regenerate the plot, you can overwrite this file.
