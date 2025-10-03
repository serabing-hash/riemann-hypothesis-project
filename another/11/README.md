
# v11 Resolution Package (Another Series) — math.NT (cross-list math.CA)

**Status:** Heuristic numerical note (not a proof).  
**Author:** Serabi (Independent Researcher, 24ping@naver.com)

This package accompanies the v11 Resolution note:
- `riemann_v11_resolution.tex` (LaTeX source)
- `figures/fig10.png` (comparative log–log figure)
- `data/table8_resolution_row.csv` (N=2,000,000 entry)
- `resolution_sim.py` (reproducibility script)

## Reproduce the figure
```bash
python resolution_sim.py
# saves figures/fig10.png
```

## Compile
- Overleaf: upload entire zip and compile `riemann_v11_resolution.tex`
- Local: `pdflatex riemann_v11_resolution.tex`

## Notes
All large-N values here are **simulated/extrapolated** under a zero-free boost model (ε=0.07, +40% on η). No RH proof is claimed.
