#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
low_spec_nbbd_sampler.py

A low-spec, *approximate* NB/BD scaling sampler that can run on modest PCs.
It computes a proxy for the NB/BD mean-square error by solving a small
ridge-regularized least-squares problem on a coarse t-grid and moderate N.
If mpmath is available, it uses ζ(1/2+it); otherwise it falls back to ζ=1
(proxy), which still lets you test the pipeline end-to-end.

Outputs:
  - results_low_spec.csv   (N, MSE, CI, theta_OLS)
  - nbbd_low_spec.png      (log-log scaling plot with CI at last N)

Usage (default small run):
  python3 low_spec_nbbd_sampler.py

You can change parameters at the bottom under "if __name__ == '__main__':"
"""

import math, sys, time, argparse, csv, random
from typing import List, Tuple
import numpy as np

try:
    import mpmath as mp
    MP_AVAILABLE = True
except Exception as e:
    MP_AVAILABLE = False

# --------------------------- Utilities ---------------------------

def segmented_mobius(N: int) -> np.ndarray:
    """
    Compute Möbius mu(n) for 1..N with a simple sieve.
    Returns int8 array mu, where mu[0] is mu(1).
    Complexity ~ O(N log log N), fine up to ~ few*1e6 on low-spec.
    """
    mu = np.ones(N+1, dtype=np.int8)
    prime = np.ones(N+1, dtype=np.bool_)
    prime[:2] = False
    spf = np.zeros(N+1, dtype=np.int32)  # smallest prime factor
    for i in range(2, N+1):
        if prime[i]:
            spf[i] = i
            for j in range(i*i, N+1, i):
                if prime[j]:
                    prime[j] = False
                if spf[j] == 0:
                    spf[j] = i
    for i in range(2, N+1):
        # factorize using spf (fallback if zero: i is prime)
        x = i
        last = 0
        square = False
        parity = 0
        while x > 1:
            p = spf[x] if spf[x] != 0 else x
            if p == last:
                square = True
                break
            last = p
            parity ^= 1
            x //= p
            while x % p == 0:
                square = True
                x //= p
                break
            if square:
                break
        if square:
            mu[i] = 0
        else:
            mu[i] = -1 if parity == 1 else 1
    return mu[1:]  # return array for n=1..N (0-indexed -> n-1)

def smooth_cutoff(n: np.ndarray, N: int) -> np.ndarray:
    """
    Smooth compact support v(n/N) on (0,1):
    Use a simple C^1 bump: v(x) = sin(pi x)^2 for x in (0,1), else 0.
    """
    x = n / float(N)
    v = np.sin(np.pi * x)**2
    v[(x <= 0) | (x >= 1)] = 0.0
    return v

def zeta_half_plus_it(t: float) -> complex:
    """Return ζ(1/2 + i t) via mpmath if available; else return 1.0 as proxy."""
    if MP_AVAILABLE:
        mp.mp.dps = 50
        return complex(mp.zeta(0.5 + 1j*t))
    else:
        return 1.0 + 0.0j  # proxy

def build_design_matrix(N: int, t_grid: np.ndarray, ridge_lambda: float,
                        use_mobius_weights: bool = True) -> Tuple[np.ndarray, np.ndarray]:
    """
    Build complex design matrix X of shape (T, N), where
      X_{k,n} = ζ(1/2+it_k) * n^(-1/2 - i t_k)
    We solve min_a || X a - 1 ||^2 + λ ||a||^2.
    Return (X, y) with y = ones(T).
    """
    n = np.arange(1, N+1, dtype=np.float64)
    # precompute n^{-1/2} and phase terms
    n_half = n**(-0.5)
    X = np.empty((t_grid.size, N), dtype=np.complex128)
    # Optional: Möbius-weighted pre-factor on columns (a starting guess or implicit weighting)
    if use_mobius_weights:
        mu = segmented_mobius(N).astype(np.float64)
        v = smooth_cutoff(n, N)
        q = np.ones_like(n)  # simple low-frequency weight
        col_weight = mu * v * q
    else:
        col_weight = np.ones_like(n)
    for k, t in enumerate(t_grid):
        z = zeta_half_plus_it(float(t))
        phase = np.exp(-1j * t * np.log(n))  # n^{-i t} = e^{-i t log n}
        X[k, :] = z * (n_half * phase) * col_weight
    y = np.ones(t_grid.size, dtype=np.complex128)
    return X, y

def ridge_solve(X: np.ndarray, y: np.ndarray, ridge_lambda: float) -> Tuple[np.ndarray, float]:
    """
    Solve complex ridge regression: min ||X a - y||^2 + λ ||a||^2
    via normal equations. Returns (a, mse).
    """
    T, N = X.shape
    # Normal equations: (X* X + λ I) a = X* y
    Xh = X.conj().T
    A = Xh @ X + ridge_lambda * np.eye(N)
    b = Xh @ y
    # Solve (use np.linalg.solve; for stability, could use cholesky on Hermitian)
    try:
        a = np.linalg.solve(A, b)
    except np.linalg.LinAlgError:
        a = np.linalg.lstsq(A, b, rcond=None)[0]
    resid = X @ a - y
    mse = float(np.mean(np.abs(resid)**2))
    return a, mse

def bootstrap_ci(mse_samples: List[float], alpha: float = 0.05) -> Tuple[float, float]:
    """
    Basic percentile bootstrap CI from a list of MSE samples (already resampled).
    """
    arr = np.array(mse_samples, dtype=float)
    lo = np.percentile(arr, 100*alpha/2)
    hi = np.percentile(arr, 100*(1 - alpha/2))
    return float(lo), float(hi)

def estimate_theta_loglog(N_list: List[int], mse_list: List[float]) -> float:
    """
    Fit log(MSE) = alpha - theta * log log N (OLS) and return theta.
    """
    X = np.log(np.log(np.array(N_list, dtype=float))).reshape(-1,1)
    y = np.log(np.array(mse_list, dtype=float))
    X1 = np.hstack([np.ones_like(X), X])
    beta = np.linalg.lstsq(X1, y, rcond=None)[0]
    alpha, slope = beta[0], beta[1]
    theta = -float(slope)
    return theta

# --------------------------- Runner ---------------------------

def run_low_spec(
    N_list: List[int] = [8000, 12000, 16000, 20000, 32000],
    T_points: int = 128,
    T_max: float = 120.0,
    ridge_lambda: float = 1e-3,
    boot_B: int = 100,
    seed: int = 42,
    out_csv: str = "results_low_spec.csv",
    out_png: str = "nbbd_low_spec.png"
):
    """
    Low-spec run over N_list. For each N:
      - Build design with t in [-T_max, T_max], T_points evenly spaced
      - Solve ridge LS to get MSE
      - Bootstrap CI by resampling t indices
    Save CSV and a log-log plot.
    """
    rng = np.random.default_rng(seed)
    t_grid_full = np.linspace(-T_max, T_max, T_points)
    rows = []
    N_vals, MSE_vals = [], []

    for N in N_list:
        # Build full design once, then bootstrap on row subsets
        X, y = build_design_matrix(N, t_grid_full, ridge_lambda, use_mobius_weights=True)
        # Solve once on full grid
        _, mse_full = ridge_solve(X, y, ridge_lambda)
        # Bootstrap by resampling t rows with replacement
        mse_bs = []
        for b in range(boot_B):
            idx = rng.integers(0, T_points, size=T_points)
            Xb = X[idx, :]
            yb = y[idx]
            _, mse_b = ridge_solve(Xb, yb, ridge_lambda)
            mse_bs.append(mse_b)
        lo, hi = bootstrap_ci(mse_bs, alpha=0.05)

        rows.append({
            "N": N,
            "MSE": mse_full,
            "CI_low": lo,
            "CI_high": hi,
            "theta_OLS": "",
            "Tw": T_max,
            "lambda": ridge_lambda,
            "seed": seed
        })
        N_vals.append(N); MSE_vals.append(mse_full)
        print(f"N={N:>6d}  MSE={mse_full:.6f}  CI=[{lo:.6f},{hi:.6f}]")

    # Fit theta on accumulated points
    try:
        theta = estimate_theta_loglog(N_vals, MSE_vals)
    except Exception:
        theta = float("nan")

    # Write CSV
    with open(out_csv, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["N","MSE","CI_low","CI_high","theta_OLS","Tw","lambda","seed"])
        w.writeheader()
        for r in rows:
            r2 = dict(r)
            r2["theta_OLS"] = theta
            w.writerow(r2)

    # Plot (single chart; log-log axes; no specific colors)
    import matplotlib.pyplot as plt
    plt.figure()
    yerr = np.array([ (r["MSE"]-r["CI_low"], r["CI_high"]-r["MSE"]) for r in rows ]).T
    plt.errorbar(N_vals, MSE_vals, yerr=yerr, fmt='o-')
    plt.xscale("log"); plt.yscale("log")
    plt.xlabel("N"); plt.ylabel("Mean Square Error")
    plt.title("Low-Spec NB/BD Scaling (proxy)")
    plt.savefig(out_png, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"\nSaved: {out_csv}, {out_png}")
    print(f"Fitted theta (OLS on log-log): {theta:.4f}")

# --------------------------- CLI ---------------------------

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--Ns", type=str, default="8000,12000,16000,20000,32000",
                    help="Comma-separated N list, e.g., 8000,12000,16000")
    ap.add_argument("--T_points", type=int, default=128, help="Number of t-samples")
    ap.add_argument("--T_max", type=float, default=120.0, help="t range is [-T_max, T_max]")
    ap.add_argument("--ridge", type=float, default=1e-3, help="Ridge lambda")
    ap.add_argument("--boot", type=int, default=100, help="Bootstrap replicates")
    ap.add_argument("--seed", type=int, default=42, help="Random seed")
    ap.add_argument("--out_csv", type=str, default="results_low_spec.csv")
    ap.add_argument("--out_png", type=str, default="nbbd_low_spec.png")
    args = ap.parse_args()

    N_list = [int(x) for x in args.Ns.split(",") if x.strip()]
    run_low_spec(
        N_list=N_list,
        T_points=args.T_points,
        T_max=args.T_max,
        ridge_lambda=args.ridge,
        boot_B=args.boot,
        seed=args.seed,
        out_csv=args.out_csv,
        out_png=args.out_png
    )
