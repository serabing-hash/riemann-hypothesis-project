#!/usr/bin/env python3
# code/contradiction_report.py
# Read CSV, fit theta, check persistence, and (optionally) pull Hutch++ norm estimates.
import os, json, numpy as np, pandas as pd

def loglog(x): 
    return np.log(np.log(x))

def fit_theta(N, mse):
    X = loglog(np.array(N)).reshape(-1,1)
    y = np.log(np.array(mse))
    X1 = np.hstack([np.ones_like(X), X])
    beta = np.linalg.lstsq(X1, y, rcond=None)[0]
    alpha, slope = beta[0], beta[1]
    theta = -slope
    return float(alpha), float(theta)

def contradiction_report(csv_path, eps0=1e-2, theta_min=0.2, hutch_norm=None, out_path=None):
    df = pd.read_csv(csv_path).sort_values("N")
    N = df["N"].to_numpy(); mse = df["MSE"].to_numpy()
    alpha, theta = fit_theta(N, mse)
    persistent = bool(any(mse[-min(3,len(mse)):] > eps0))
    report = {
        "alpha": alpha, "theta": theta, "persistent": persistent,
        "eps0": eps0, "theta_min": theta_min,
        "hutch_op_norm_bound": hutch_norm
    }
    status = "OK"
    if persistent and theta < theta_min and (hutch_norm is not None and hutch_norm < 0.5):
        status = "CONTRADICTION-FLAG"
    report["status"] = status
    if out_path:
        with open(out_path, "w") as f:
            json.dump(report, f, indent=2)
    return report

if __name__ == "__main__":
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv = os.path.join(base, "data", "results_v28.csv")
    out = os.path.join(base, "data", "contradiction_report.json")
    norm = None  # plug your Hutch++ norm estimate here
    rep = contradiction_report(csv, hutch_norm=norm, out_path=out)
    print(rep)
