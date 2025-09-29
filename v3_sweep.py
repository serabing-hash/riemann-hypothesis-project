# v3_sweep.py
# Sweep experiment for V3 objective: vary N, lambda, rho and record results
import numpy as np
from v3_objective import solve_cstar

def run_sweep(N_values=(200, 500, 800, 1000),
              lam_values=(0.1, 0.3, 1.0, 3.0),
              rho_values=(1e-9, 1e-7, 1e-6)):
    results = []
    for N in N_values:
        for lam in lam_values:
            for rho in rho_values:
                c, a, D, M, Eoff = solve_cstar(N, lam=lam, rho=rho)
                ratio = Eoff/D if D > 0 else np.inf
                results.append({
                    "N": N,
                    "lambda": lam,
                    "rho": rho,
                    "M": M,
                    "Sum|a|^2": D,
                    "Eoff": Eoff,
                    "ratio": ratio,
                    "M_neg?": M < 0,
                    "Eoff_log?": ratio <= 1/np.log(max(N, 2))
                })
                print(f"N={N}, λ={lam}, ρ={rho:.0e} | "
                      f"M={M:.4f}, Eoff={Eoff:.6f}, Σ|a|^2={D:.6f}, "
                      f"ratio={ratio:.4f}, "
                      f"M<0={M<0}, Eoff/logN={ratio <= 1/np.log(max(N, 2))}")
    return results

if __name__ == "__main__":
    data = run_sweep()
    import pandas as pd
    df = pd.DataFrame(data)
    df.to_csv("v3_sweep_results.csv", index=False)
    print("\nSaved results to v3_sweep_results.csv")
