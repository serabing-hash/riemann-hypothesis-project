#!/usr/bin/env python3
import os, numpy as np, pandas as pd, matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = os.path.join(BASE, "data", "results_v28.csv")
OUT = os.path.join(BASE, "figures", "nbbd_scaling.png")

def main(csv_path=CSV, out_path=OUT):
    df = pd.read_csv(csv_path).sort_values("N")
    x = df["N"].to_numpy(); y = df["MSE"].to_numpy()
    if "CI_low" in df.columns and "CI_high" in df.columns:
        lo = pd.to_numeric(df["CI_low"], errors="coerce").to_numpy()
        hi = pd.to_numeric(df["CI_high"], errors="coerce").to_numpy()
        yerr = np.vstack([np.nan_to_num(y-lo, nan=0.0), np.nan_to_num(hi-y, nan=0.0)])
        plt.figure(); plt.errorbar(x, y, yerr=yerr, fmt='o-')
    else:
        plt.figure(); plt.plot(x, y, 'o-')
    plt.xscale("log"); plt.yscale("log")
    plt.xlabel("N"); plt.ylabel("Mean Square Error")
    plt.title("NB/BD Scaling (auto-generated)")
    plt.savefig(out_path, dpi=300, bbox_inches="tight"); plt.close()
    print("Updated figure:", out_path)

if __name__ == "__main__":
    main()
