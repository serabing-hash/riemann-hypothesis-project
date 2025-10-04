
# NB/BD Stable (v2.9): Weighted Hilbert Lemma — Analytic Stability

This repository contains a **conservative, math-first** stabilization of the NB/BD approach.
It focuses on a band-wise proof of a **Möbius-weighted Hilbert lemma** that yields off-diagonal decay by a power of log, and a **small-N reproducible demo**.
**It is *not* a proof of RH.**

## Layout
```
riemann_v2_9_stable/
 ├─ paper/
 │   ├─ main.tex            # v2.9 LaTeX (stable analytic version)
 │   ├─ refs.bib
 │   └─ figures/
 │       └─ scaling_smallN.png
 ├─ code/
 │   ├─ run_demo.py         # generates data/demo_results.csv and paper/figures/scaling_smallN.png
 │   └─ requirements.txt
 ├─ data/
 │   ├─ demo_results.csv    # small-N demo results
 │   └─ README.md
 └─ README.md
```

## How to build the paper
1. Install a LaTeX distribution (TeX Live or MiKTeX).
2. Run: `pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex` inside `paper/`.

## How to run the demo
```
pip install -r code/requirements.txt
python code/run_demo.py
```
This updates `data/demo_results.csv` and regenerates `paper/figures/scaling_smallN.png`.

## Scope / Disclaimer
- Focus: analytic stability via a weighted Hilbert lemma.
- Out of scope: large-N claims; RH is **not** proved here.
- The small-N plot is illustrative and reproducible.
