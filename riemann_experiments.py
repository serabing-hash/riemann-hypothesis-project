# riemann_experiments.py
# -----------------------------------
# Experiments for thin-band suppression coefficients
# Towards the Riemann Hypothesis (NB/BD framework)
#
# Author: Serabi
# License: Open for research use

import numpy as np
import pandas as pd
from sympy import mobius

def gaussian(x, lam):
    """Gaussian window function G_lambda(x)."""
    return np.exp(-0.5 * (x/lam)**2)

def coefficients(N, alpha=0.75, beta=0.25):
    """
    Construct multi-scale signed Gaussian coefficients.
    Returns array a[1..N].
    """
    a = np.zeros(N+1, dtype=np.float64)
    lnN = np.log(max(2, N))
    for n in range(1, N+1):
        mu = mobius(n)
        if mu == 0:
            continue
        ln = np.log(n)
        c = (-alpha * gaussian(ln, 0.5*lnN)
             + (1+beta) * gaussian(ln, lnN)
             - alpha * gaussian(ln, 2.0*lnN))
        a[n] = mu/np.sqrt(n) * c
    return a

def eoff(a):
    """
    Compute off-diagonal correlation error:
    E_off = sum_{m!=n} |a_m||a_n| * exp(-|log(m/n)|/2)
    """
    N = len(a)-1
    total = 0.0
    for m in range(1, N+1):
        am = abs(a[m])
        if am == 0.0:
            continue
        for n in range(1, N+1):
            if n == m:
                continue
            total += am * abs(a[n]) * np.exp(-0.5*abs(np.log(m/n)))
    return total

def run_experiment(N_list=(200, 500, 1000), alpha=0.75, beta=0.25, out_csv="multi_results.csv"):
    """
    Run experiments over N_list, save CSV with columns:
    N, alpha, beta, sum_sq, E_off, ratio
    """
    results = []
    for N in N_list:
        a = coefficients(N, alpha, beta)
        sum_sq = float(np.sum(a**2))
        E = float(eoff(a))
        ratio = E/sum_sq if sum_sq > 0 else float('inf')
        results.append((N, alpha, beta, sum_sq, E, ratio))
        print(f"N={N}: sum_sq={sum_sq:.6f}, E_off={E:.6f}, ratio={ratio:.6f}")
    df = pd.DataFrame(results, columns=["N","alpha","beta","sum_sq","E_off","ratio"])
    df.to_csv(out_csv, index=False)
    print(f"Results saved to {out_csv}")

if __name__ == "__main__":
    # Example usage:
    # python riemann_experiments.py
    run_experiment()
