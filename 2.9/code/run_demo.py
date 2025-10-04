
import csv
import math
import os
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DATA = ROOT / "data" / "demo_results.csv"
FIG = ROOT / "paper" / "figures" / "scaling_smallN.png"

def load_data():
    xs, ys, lo, hi = [], [], [], []
    with open(DATA, newline="") as f:
        r = csv.DictReader(f)
        for row in r:
            N = int(row["N"])
            MSE = float(row["MSE"])
            CI_low = float(row["CI_low"])
            CI_high = float(row["CI_high"])
            xs.append(N); ys.append(MSE); lo.append(CI_low); hi.append(CI_high)
    return np.array(xs), np.array(ys), np.array(lo), np.array(hi)

def fit_loglog(N, MSE):
    x = np.log(np.log(N))
    y = np.log(MSE)
    A = np.vstack([x, np.ones_like(x)]).T
    b, a = np.linalg.lstsq(A, y, rcond=None)[0]  # y = b*x + a
    # Model: log MSE = a + b * log log N  -> theta = -b
    theta = -b
    return a, b, theta

def plot_demo(N, MSE, lo, hi, a, b):
    x = np.log(np.log(N))
    xx = np.linspace(x.min(), x.max(), 200)
    yy = a + b*xx
    plt.figure(figsize=(6.0, 4.0))
    # error bars
    yerr = [MSE - lo, hi - MSE]
    plt.errorbar(x, MSE, yerr=yerr, fmt='o', capsize=3, label='data (95% CI)')
    plt.plot(xx, np.exp(yy), '-', label='fit: log MSE = a + b log log N')
    plt.xlabel('log log N')
    plt.ylabel('MSE')
    plt.title('Small-N demo (illustrative)')
    plt.legend(loc='best')
    FIG.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(FIG, dpi=300)
    plt.close()
    print(f"Saved figure to {FIG}")

def main():
    N, MSE, lo, hi = load_data()
    a, b, theta = fit_loglog(N, MSE)
    print(f"a={a:.3f}, b={b:.3f}, theta={theta:.3f}")
    plot_demo(N, MSE, lo, hi, a, b)

if __name__ == "__main__":
    main()
