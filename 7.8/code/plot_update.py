#!/usr/bin/env python3
# code/plot_update.py
# Read data/results_v27.csv and regenerate figures/nbbd_scaling.png
import os, sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = os.path.join(BASE, "data", "results_v27.csv")
OUT = os.path.join(BASE, "figures", "nbbd_scaling.png")

def main(csv_path=CSV, out_path=OUT):
    df = pd.read_csv(csv_path)
    df = df.sort_values("N")
    x = df["N"].to_numpy()
    y = df["MSE"].to_numpy()
    yerr = None
    if "CI_low" in df.columns and "CI_high" in df.columns:
        lo = df["CI_low"].to_numpy(dtype=float)
        hi = df["CI_high"].to_numpy(dtype=float)
        lo[np.isnan(lo)] = y[np.isnan(lo)]
        hi[np.isnan(hi)] = y[np.isnan(hi)]
        yerr = np.vstack([y - lo, hi - y])
    plt.figure()
    if yerr is not None:
        plt.errorbar(x, y, yerr=yerr, fmt='o-')
    else:
        plt.plot(x, y, 'o-')
    plt.xscale("log"); plt.yscale("log")
    plt.xlabel("N"); plt.ylabel("Mean Square Error")
    plt.title("NB/BD Scaling (auto-generated)")
    plt.savefig(out_path, dpi=300, bbox_inches="tight")
    plt.close()
    print("Updated figure:", out_path)

if __name__ == "__main__":
    main()
