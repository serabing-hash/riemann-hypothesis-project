# Riemann Hypothesis Project — NB/BD Criterion with Möbius Weights

This repository provides the **research seed package** for our exploration of the **Riemann Hypothesis (RH)**.  
We reformulate RH using two complementary perspectives:

1. **Explicit formulas** for the Chebyshev function, with controlled truncation error.  
2. **Nyman–Beurling–Báez-Duarte (NB/BD) criterion**, expressed as an $L^2$ approximation problem.  

---

## 🔑 Key Contributions
- **Hilbert-type lemma with Möbius coefficients**:  
  Off-diagonal contributions are suppressed by a logarithmic saving, with fitted exponents around $\theta \approx 0.1$.  

- **Reduction to thin-band integer correlations**:  
  Near-diagonal pairs drive convergence in the NB/BD framework.  

- **Numerical validation**:  
  - Unweighted scaling up to $N=32,000$.  
  - Ridge-regularized scaling ($\lambda=10^{-3}$) up to $N=20,000$.  
  - Plateau resolution via low-frequency sine basis (Gaussian weight $T_w=115$).  
  - Error analysis: regression residuals $\leq 4\times 10^{-4}$, RMS $\approx 2.3\times 10^{-4}$.  

- **Figures & Data**: All plots (PNG), CSV datasets, and LaTeX sources are included for reproducibility.  

---

## 📂 Repository Structure
- `data/` : CSV datasets from numerical experiments  
- `figures/` : Plots (`.png`) used in the paper  
- `latex/` : LaTeX sources (main paper + appendix)  
- `notebooks/` : Jupyter/Python scripts for regression and MSE computations  

---

## 📊 Numerical Highlights
| $N$     | Weighted MSE (ridge, $\lambda=10^{-3}$) |
|---------|-----------------------------------------|
| 8000    | 0.024                                   |
| 12000   | 0.019                                   |
| 16000   | 0.016                                   |
| 20000   | 0.013                                   |

---

## ⚠️ Disclaimer
This package is **not a proof** of the Riemann Hypothesis.  
It is a **structural foundation (“seed”)** that combines analytic reductions and numerical evidence to guide further mathematical and computational investigations.  

---

## 📖 References
- L. Báez-Duarte (2003), *A strengthening of the Nyman–Beurling criterion for the Riemann Hypothesis*  
- J. B. Conrey (2003), *The Riemann Hypothesis*, Notices AMS  
- E. C. Titchmarsh (1986), *The Theory of the Riemann Zeta-Function*  

---

## 🌐 Links
- 📄 Zenodo: [https://zenodo.org/records/17230129](https://zenodo.org/records/17230129)  
- 💻 GitHub: [https://github.com/serabing-hash/riemann-hypothesis-project](https://github.com/serabing-hash/riemann-hypothesis-project)  

---

## 📝 Citation
If you use this package, please cite via Zenodo DOI:

