# v3_objective.py
# Joint quadratic optimization for NB/BD coefficients
# Basis: multiscale Gaussians in log n + mu(n)/n correction
import numpy as np
from sympy import mobius

def gaussian(ln, lam):
    return np.exp(-0.5*(ln/lam)**2)

def build_basis(N, factors=(0.5,0.75,1.0,1.5,2.0), include_mu_over_n=True):
    ns = np.arange(1, N+1, dtype=np.float64)
    ln = np.log(ns)
    lnN = np.log(max(2, N))
    mu = np.array([mobius(int(n)) for n in ns], dtype=np.int64)
    Bcols = []
    # Gaussian/sqrt(n) columns
    w = 1.0/np.sqrt(ns)
    for f in factors:
        lam = f*lnN
        Bcols.append((mu * w * gaussian(ln, lam)).astype(np.float64))
    if include_mu_over_n:
        Bcols.append((mu/ns).astype(np.float64))
    B = np.stack(Bcols, axis=1)  # shape (N, J)
    return ns, mu, B

def build_matrices(B, ns):
    K = B.T @ B
    s1 = B.T @ (1.0/ns)
    return K, s1

def build_W(ns):
    N = len(ns)
    logn = np.log(ns)
    # W_{mn} = exp(-|log(m/n)|/2), with zeros on diagonal
    diff = np.abs(logn.reshape(-1,1) - logn.reshape(1,-1))
    W = np.exp(-0.5*diff)
    np.fill_diagonal(W, 0.0)
    return W

def solve_cstar(N, lam=1.0, rho=1e-9, include_mu_over_n=True):
    ns, mu, B = build_basis(N, include_mu_over_n=include_mu_over_n)
    K, s1 = build_matrices(B, ns)
    W = build_W(ns)
    A = 2*np.pi*K + lam*(B.T @ W @ B) + rho*np.eye(B.shape[1])
    b = 2*np.pi*s1
    c = np.linalg.solve(A, b)
    a = B @ c
    # Diagnostics
    D = float(np.sum(a**2))
    M = float(2*np.pi*(1 - 2*(c@s1) + c@(K@c)))
    Eoff = float(c @ (B.T @ W @ B) @ c)
    return c, a, D, M, Eoff

if __name__ == "__main__":
    for N in (200, 500):
        for lam in (0.1, 0.3, 1.0):
            c, a, D, M, Eoff = solve_cstar(N, lam=lam, rho=1e-9, include_mu_over_n=True)
            ratio = Eoff/D if D>0 else np.inf
            print(f"N={N}, lambda={lam}:  M={M:.4f},  Eoff={Eoff:.6f},  Sum|a|^2={D:.6f},  ratio={ratio:.4f}")
