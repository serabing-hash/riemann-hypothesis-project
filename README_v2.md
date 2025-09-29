# Thin-band Suppression and Multi-scale Coefficient Design Towards the Riemann Hypothesis

## Overview
This repository contains preliminary research notes and experiments related to the Riemann Hypothesis (RH) using the Nyman–Beurling/Báez-Duarte framework.  
We introduce **multi-scale signed Gaussian coefficients** to suppress near-diagonal correlations, a long-standing obstacle in this line of research.  

## Contents
- **Paper (PDF/TeX)**: Draft manuscript describing the method, lemma sketch, and numerical results.
- **Data (CSV)**:
  - `eoff_experiments.csv` — baseline off-diagonal error growth.
  - `multi_eoff_experiments.csv` — results for multi-scale signed coefficients.
  - `family_search_alpha_beta.csv` — parameter tuning experiments.
  - `largeN_eoff_results.csv` — scaling experiments up to N=1000.
- **Code (optional)**: Scripts for reproducing numerical experiments.

## Key Ideas
- Standard coefficients show rapid growth in off-diagonal error.
- Introducing signed, multi-scale Gaussian weights produces destructive interference.
- Numerical experiments show up to **10× suppression** of near-diagonal terms.
- A **Thin-band Suppression Lemma** is sketched, suggesting a pathway to rigorous control.

## How to Use
1. Compile the LaTeX source (`riemann_draft_v2_1.tex`) to generate the paper PDF.
2. Explore the CSV files for experimental results.
3. Modify or extend the coefficient design for further experiments.

## Citation
If you wish to cite this work, please use:

```bibtex
@misc{serabi2025thinband,
  author       = {Serabi},
  title        = {Thin-band Suppression and Multi-scale Coefficient Design Towards the Riemann Hypothesis},
  year         = {2025},
  howpublished = {Zenodo preprint},
}
