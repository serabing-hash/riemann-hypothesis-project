#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse, os, json
import numpy as np
import pandas as pd

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", default="data/results.csv")
    ap.add_argument("--out", default="reports/regression_v5.json")
    args = ap.parse_args()

    df = pd.read_csv(args.csv).sort_values("N")
    x = np.log(np.log(df["N"].to_numpy()))
    y = np.log(df["mse_star"].to_numpy())

    b, a = np.polyfit(x, y, 1)  # y ≈ a + b x
    yhat = a + b*x
    ss_res = float(np.sum((y - yhat)**2))
    ss_tot = float(np.sum((y - np.mean(y))**2))
    r2 = 1.0 - (ss_res/ss_tot if ss_tot>0 else 0.0)
    theta = -b

    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(dict(alpha=float(a), beta=float(b), theta=float(theta), r2=float(r2)),
                  f, ensure_ascii=False, indent=2)
    print("[OK]", args.out)

if __name__ == "__main__":
    main()