"""
Prototype: spectral surrogate for NB/BD kernel (tiny demo)
- Builds a small K_N (Hilbert-on-log kernel)
- Applies a smooth Möbius-weighted window
- Shows eigenvalues to visualize compact/decay behavior
This is a toy to sanity-check shapes; it is NOT a research-scale solver.
"""

import math
import cmath
import numpy as np

def mobius_upto(N):
    # very small N only (toy)
    mu = np.ones(N+1, dtype=int)
    isprime = np.ones(N+1, dtype=bool); isprime[:2] = False
    for p in range(2, N+1):
        if isprime[p]:
            for k in range(p, N+1, p):
                mu[k] *= -1
                isprime[k] = (k==p)  # keep sieve simple
            pp = p*p
            for k in range(pp, N+1, pp):
                mu[k] = 0
            for k in range(2*p, N+1, p):
                isprime[k] = False
    return mu

def smooth_window(n, N):
    # C^\infty-type bump on (0,1), cheap surrogate
    x = n / N
    if x<=0 or x>=1: return 0.0
    # cosine bump
    return 0.5*(1 - math.cos(math.pi*min(1.0, max(0.0, x))))

def K_kernel(N):
    n = np.arange(1, N+1, dtype=float)
    M = np.minimum(np.sqrt(n[:,None]/n[None,:]), np.sqrt(n[None,:]/n[:,None]))
    return M

def main():
    N = 200  # keep tiny for laptops
    K = K_kernel(N)

    mu = mobius_upto(N)
    w = np.array([smooth_window(n, N) for n in range(1, N+1)], dtype=float)
    a = mu[1:] * w

    # Möbius-weighted finite section (diagonal scaling)
    D = np.diag(a)
    K_weighted = D @ K @ D

    # eigenvalues (symmetric PSD surrogate)
    vals = np.linalg.eigvalsh((K_weighted+K_weighted.T)/2.0)
    vals = np.sort(vals)[::-1]

    print("Top 10 eigenvalues of the weighted finite section:")
    print(np.round(vals[:10], 6))

if __name__ == "__main__":
    main()