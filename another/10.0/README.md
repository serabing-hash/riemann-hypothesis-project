
# RH Project — Another Version v10.0 (Experimental Extensions)

**Status:** Heuristic / Numerical note (not a proof).  
**Primary category:** math.NT (cross-list: math.CA)  
**Author:** Serabi (Independent Researcher, 24ping@naver.com)

## What is this?
This package archives the experimental line beyond v9.3. It bundles:
- A concise LaTeX note (`v10_another.tex`)
- A generated PNG figure (`figures/fig9.png`) comparing base data and simulated extrapolations (v9.6–v10.0)
- This README

The intent is to preserve the numerical exploration and zero-free–inspired extrapolations without overclaiming.

## Figure (reproducible)
The figure plots `(x, y) = (log log N, log MSE*)` with:
- Base data points: N = [8k, 12k, 16k, 20k, 50k, 100k, 200k], MSE* in [0.163, 0.180]
- Simulated points: v9.6 (50k ≈ 0.168), v9.7 (100k ≈ 0.164), v9.8 (200k ≈ 0.160), v10.0 (1M ≈ 0.148)

> IMPORTANT: v9.6–v10.0 points are **simulated extrapolations**, not raw zeta computations.

## Compile
- Overleaf: upload the entire zip, ensure `figures/fig9.png` path is preserved.
- Local: `pdflatex v10_another.tex`

## Suggested public stance
- **arXiv:** keep to v9.3 (data-backed).  
- **GitHub/Zenodo:** publish this `Another Version v10.0` as experimental extensions.

## References
- Báez-Duarte (2003), Conrey (2003), Titchmarsh (1986).
