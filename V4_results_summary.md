# V4 Results Summary

We tested the Version 4 design (phase-modulated Gaussian basis + band-limited kernel) and obtained:

| N   | M       | ratio   | Sum|a|^2 | Eoff   | 1/log N |
|-----|---------|---------|---------|--------|---------|
| 200 | -2.3319 | 0.1725  | 1.2998  | 0.2242 | 0.1880  |
| 500 | -1.9112 | 0.1063  | 1.2615  | 0.1341 | 0.1610  |

- Both cases satisfy **M < 0** and **ratio ≤ 1/log N**.
- This is the first time our framework meets both targets simultaneously.

Next steps:
- Extend to larger N (e.g., 800, 1000, 2000) and verify stability.
- Tighten theory for band-limited kernels and phase-modulated bases.
- Integrate into the LaTeX manuscript (V4 section).
