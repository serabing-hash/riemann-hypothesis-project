# NB/BD Orthodox Package (v2.x)

This zip contains a clean, conservative LaTeX note plus a small Python helper to produce example figures.

## Contents
```
serabi_nt_v2x_package/
  ├─ main.tex
  ├─ README.md
  ├─ code/
  │   └─ appendixA.py
  └─ figures/
      (PNG files will be created here after you run appendixA.py)
```

## How to build

1) (Optional) Generate placeholder figures:
```bash
python code/appendixA.py
```
This creates:
- `figures/mse_scaling.png`
- `figures/zero_free_comparison.png`
- `figures/theta_fit.png`

2) Compile LaTeX (choose one):
```bash
pdflatex main.tex
# or
xelatex main.tex
```

## Replace with your data
- Edit the arrays inside `code/appendixA.py` (Ns, MSEs, CIs) to match your latest results.
- Re-run the script to regenerate updated PNGs.
- Update the numeric table in `main.tex` if desired.

## Disclaimer
This is **not** a proof of the Riemann Hypothesis. It is an orthodox stability note for the NB/BD framework.
