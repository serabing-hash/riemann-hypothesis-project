# nbbd_sampler.py
import argparse, os, csv
import numpy as np
import mpmath as mp
from numpy.linalg import lstsq

def design_matrix(t, N):
    n = np.arange(1, N+1)
    logn = np.log(n)
    return np.exp(-1j * np.outer(t, logn)) / np.sqrt(n)

def fit_and_eval(N, T_points, T_max, ridge, seed):
    rng = np.random.default_rng(seed)
    t = np.linspace(-T_max, T_max, T_points)
    rng.shuffle(t)
    split = T_points // 2
    t_train, t_test = t[:split], t[split:]

    Xtr, Xte = design_matrix(t_train, N), design_matrix(t_test, N)
    ytr = np.array([1/mp.zeta(0.5+1j*ti) for ti in t_train], dtype=complex)
    yte = np.array([1/mp.zeta(0.5+1j*ti) for ti in t_test], dtype=complex)

    A = Xtr.conj().T @ Xtr + ridge * np.eye(N)
    b = Xtr.conj().T @ ytr
    a, *_ = lstsq(A, b, rcond=None)

    resid_te = Xte @ a - yte
    mse_te = float(np.mean(np.abs(resid_te)**2))
    return mse_te, a, t_test, Xte, yte

def bootstrap_ci_from_test(a, t_test, Xte, yte, B=200, seed=42):
    rng = np.random.default_rng(seed)
    Tt = len(t_test)
    mses = []
    for _ in range(B):
        idx = rng.integers(0, Tt, size=Tt)
        Xb, yb = Xte[idx], yte[idx]
        resid = Xb @ a - yb
        mses.append(float(np.mean(np.abs(resid)**2)))
    arr = np.array(mses, dtype=float)
    lo = float(np.percentile(arr, 2.5))
    hi = float(np.percentile(arr, 97.5))
    return float(arr.mean()), lo, hi

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--Ns", type=str, default="4000")
    p.add_argument("--T_points", type=int, default=256)
    p.add_argument("--T_max", type=float, default=50.0)
    p.add_argument("--ridge", type=float, default=1e-2)
    p.add_argument("--boot", type=int, default=200)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--csv", type=str, default="results.csv")
    args = p.parse_args()

    Ns = [int(x) for x in str(args.Ns).split(",")]
    write_header = not os.path.exists(args.csv)
    with open(args.csv, "a", newline="") as f:
        w = csv.writer(f)
        if write_header:
            w.writerow(["N","MSE","CI_low","CI_high","T_points","T_max","ridge","boot","seed"])
        for N in Ns:
            mse, a, t_test, Xte, yte = fit_and_eval(N, args.T_points, args.T_max, args.ridge, args.seed)
            mean_bs, lo, hi = bootstrap_ci_from_test(a, t_test, Xte, yte, B=args.boot, seed=args.seed)
            print(f"N={N:6d}  MSE={mse:.6f}  CI=[{lo:.6f},{hi:.6f}]")
            lo = min(lo, mse); hi = max(hi, mse)
            w.writerow([N, mse, lo, hi, args.T_points, args.T_max, args.ridge, args.boot, args.seed])

if __name__ == "__main__":
    main()
