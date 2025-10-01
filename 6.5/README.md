# Riemann Hypothesis Project: NB/BD Numerical and Theoretical Framework

This repository provides the reproducible research package for our exploration of the **Riemann Hypothesis (RH)**.  
We reformulate RH using two complementary perspectives:

1. **Explicit formula for the Chebyshev function ψ(x)** with truncation error control.  
2. **Nyman–Beurling–Báez-Duarte (NB/BD) criterion**, expressed as an $L^2$ approximation problem.  

---

## 🔑 Key Contributions
- **Hilbert-Type Lemma (Analytic):**  
  Shows that Möbius-weighted coefficients yield logarithmic suppression of off-diagonal terms, stabilizing NB/BD approximations.  

- **Numerical Evidence (Computation):**  
  - Unweighted scaling up to $N=32{,}000$.  
  - Weighted ridge scaling up to $N=20{,}000$ with regression fit $\theta \approx 5.94$, $R^2=0.99$.  
  - Plateau resolution via low-frequency sine basis ($T_w=115$).  

- **Open Package:**  
  All code, datasets, and LaTeX sources are included for reproducibility.  

---

## 📊 Figures
The following figures are generated from the provided Python scripts:

- `figures/scaling.png` — Unweighted scaling curve (N up to 32,000).  
- `figures/theta_fit.png` — Ridge-weighted scaling with regression fit.  
- `figures/plateau_resolution_7basis.png` — Plateau resolution via basis extension.  

---

## ⚙️ Usage

### 1. Run Numerical Experiment
```bash
python run_experiment.py --N 100000 --lambda 1e-3 --bandwidth 3000
```
- Computes NB/BD error up to $N=10^5$.  
- Saves results into `results/exp1.csv`.

### 2. Generate Figures
```bash
python make_plots.py --input results/exp1.csv --outdir figures/
```
- Produces `scaling.png`, `theta_fit.png`, and `plateau_resolution_7basis.png`.

---

## 📂 Repository Structure
```
├── compute_mu.py            # Möbius function generator
├── build_coeffs.py          # Construct coefficients a_n
├── apply_kernel.py          # Apply logarithmic band kernel
├── nystrom.py               # Nyström low-rank correction
├── solve_nb_bd.py           # Matrix-free solver for NB/BD system
├── analyze_theta.py         # Regression fit for θ exponent
├── run_experiment.py        # Main script for experiments
├── make_plots.py            # Plotting utility
├── figures/                 # Output figures
├── results/                 # Numerical results (CSV)
├── main_v3.tex              # LaTeX paper source
└── README.md                # Project documentation
```

---

## 📚 References
- Báez-Duarte (2003). *A strengthening of the Nyman–Beurling criterion for the Riemann Hypothesis*.  
  DOI: [10.1007/s10231-003-0074-5](https://doi.org/10.1007/s10231-003-0074-5)  

- Conrey (2003). *The Riemann Hypothesis*. Notices of the AMS.  
  DOI: [10.1090/noti/194](https://doi.org/10.1090/noti/194)  

- Titchmarsh (1986). *The Theory of the Riemann Zeta-Function*, 2nd ed. Oxford University Press.  
  ISBN: 9780198533696  

---

## ⚠️ Limitations
- Current experiments reach $N=32{,}000$ (public package supports $N=10^5$).  
- Result $d_N \to 0$ demonstrates **NB/BD stability**, but **not a direct proof of RH**.  
- Further **analytic continuation** and **ε–δ bounds** are required.  
- This framework is a **numerical and structural seed**, not a final proof.

---

## 📌 Citation
If you use this package, please cite via Zenodo DOI:  
👉 [Zenodo Record](https://zenodo.org/records/17230129)  

GitHub Repository:  
👉 [serabing-hash/riemann-hypothesis-project](https://github.com/serabing-hash/riemann-hypothesis-project)

---

**Author:** Serabi (Independent Researcher)  
Year: 2025
