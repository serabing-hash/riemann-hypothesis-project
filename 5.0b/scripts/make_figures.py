#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse, os, json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def ensure_dir(p):
    if not os.path.exists(p):
        os.makedirs(p, exist_ok=True)

def load_csv(path):
    df = pd.read_csv(path)
    req = ["N","sigma","ridge_lambda","w_minus","w_plus",
           "mse_plus","mse_minus","mse_star","ci_low","ci_high","seed"]
    missing = [c for c in req if c not in df.columns]
    if missing:
        raise ValueError(f"CSV missing columns: {missing}")
    df = df.sort_values("N")
    return df

def fig1_scaling(df, outdir):
    plt.figure(figsize=(7,4.2))
    N = df["N"].to_numpy()
    mp = df["mse_plus"].to_numpy()
    mm = df["mse_minus"].to_numpy()
    ms = df["mse_star"].to_numpy()

    plt.plot(N, mp, marker="o", label="MSE+", linewidth=1.4)
    plt.plot(N, mm, marker="s", label="MSE–", linewidth=1.4)
    plt.plot(N, ms, marker="^", label="MSE*", linewidth=1.6)

    # 신뢰구간(있으면 얹기)
    if {"ci_low","ci_high"}.issubset(df.columns):
        lo = df["ci_low"].to_numpy()
        hi = df["ci_high"].to_numpy()
        yerr = np.vstack([ms - lo, hi - ms])
        # 음수 방지
        yerr = np.maximum(yerr, 0.0)
        plt.errorbar(N, ms, yerr=yerr, fmt="none", alpha=0.35, capsize=3)

    plt.xlabel("N")
    plt.ylabel("Mean Square Error")
    plt.title("NB/BD Scaling (linear)")
    plt.grid(True, alpha=0.25)
    plt.legend()
    out = os.path.join(outdir, "fig_scaling_linear.png")
    plt.tight_layout()
    plt.savefig(out, dpi=300)
    plt.close()
    return out

def fig2_loglog_regression(df, outdir, report_json=None):
    plt.figure(figsize=(7,4.2))
    N = df["N"].to_numpy()
    ms = df["mse_star"].to_numpy()

    x = np.log(np.log(N))
    y = np.log(ms)
    # 단순 OLS
    b, a = np.polyfit(x, y, 1)   # y ≈ a + b x
    yhat = a + b*x
    # R^2
    ss_res = np.sum((y - yhat)**2)
    ss_tot = np.sum((y - np.mean(y))**2)
    r2 = 1.0 - (ss_res/ss_tot if ss_tot>0 else 0.0)
    theta = -b

    # 산점 + 회귀선
    plt.scatter(x, y, s=32, label="data (log MSE*)")
    xs = np.linspace(x.min(), x.max(), 200)
    plt.plot(xs, a + b*xs, label=f"OLS fit: log MSE* = {a:.3f} + {b:.3f} log log N (R²={r2:.3f})")

    plt.xlabel("log log N")
    plt.ylabel("log MSE*")
    plt.title("Log–Log Regression of MSE*")
    plt.grid(True, alpha=0.25)
    plt.legend()
    out = os.path.join(outdir, "fig_loglog_regression.png")
    plt.tight_layout()
    plt.savefig(out, dpi=300)
    plt.close()

    # 리포트 JSON 저장(LaTeX에서 가져다 쓸 수 있음)
    if report_json:
        info = dict(alpha=float(a), beta=float(b), theta=float(theta), r2=float(r2))
        with open(report_json, "w", encoding="utf-8") as f:
            json.dump(info, f, ensure_ascii=False, indent=2)

    return out, dict(alpha=a, beta=b, theta=theta, r2=r2)

def fig3_sensitivity(optional_csv, outdir):
    """
    민감도 파일이 있으면 히트맵으로 출력.
    기대 스키마: rows = metrics(MSE+, MSE-, MSE*), cols = params(sigma, ridge_lambda, w_minus, w_plus)
    """
    if optional_csv is None or not os.path.exists(optional_csv):
        return None
    df = pd.read_csv(optional_csv, index_col=0)
    # 간단한 히트맵
    plt.figure(figsize=(6,4))
    mat = df.to_numpy()
    plt.imshow(mat, aspect="auto")
    plt.xticks(ticks=np.arange(df.shape[1]), labels=df.columns, rotation=45, ha="right")
    plt.yticks(ticks=np.arange(df.shape[0]), labels=df.index)
    plt.colorbar(label="∂ log MSE / ∂ param (approx.)")
    plt.title("Sensitivity (finite-diff. approx.)")
    plt.tight_layout()
    out = os.path.join(outdir, "fig_sensitivity.png")
    plt.savefig(out, dpi=300)
    plt.close()
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", default="data/results.csv", help="input CSV path")
    ap.add_argument("--outdir", default="figures", help="output directory for PNGs")
    ap.add_argument("--report_json", default="reports/regression_v5.json")
    ap.add_argument("--sensitivity_csv", default="reports/sensitivity_v5.csv")
    args = ap.parse_args()

    ensure_dir(args.outdir)
    ensure_dir(os.path.dirname(args.report_json) or ".")
    try:
        df = load_csv(args.csv)
    except Exception as e:
        raise SystemExit(f"[ERROR] {e}")

    f1 = fig1_scaling(df, args.outdir)
    f2, rep = fig2_loglog_regression(df, args.outdir, report_json=args.report_json)
    f3 = fig3_sensitivity(args.sensitivity_csv, args.outdir)

    print("[DONE] Generated:")
    print(" -", f1)
    print(" -", f2)
    if f3:
        print(" -", f3)
    print(" -", args.report_json, rep)

if __name__ == "__main__":
    main()