import numpy as np

def mobius_upto(N):
    """Simple Möbius via sieve (μ(1)=1)."""
    mu = np.ones(N+1, dtype=int)
    is_prime = np.ones(N+1, dtype=bool)
    is_prime[:2] = False
    for p in range(2, N+1):
        if is_prime[p]:
            mu[p::p] *= -1
            sq = p*p
            if sq <= N:
                mu[sq::sq] = 0
            is_prime[p*p::p] = False
    return mu

def smooth_cutoff(N):
    """v(n/N): compactly supported C^∞-like window (numerical surrogate)."""
    n = np.arange(1, N+1, dtype=float)
    x = n / (N+1.0)
    w = np.exp(-1.0/(x*(1.0-x)))
    w[(x<=0) | (x>=1)] = 0.0
    w /= w.max()
    return w

def kernel_K(N):
    n = np.arange(1, N+1, dtype=float)
    logn = np.log(n)
    M = logn[:,None] - logn[None,:]
    K = np.exp(-0.5*np.abs(M))
    np.fill_diagonal(K, 0.0)  # off-diagonal part
    return K

def weighted_quadratic_form(N, q_logC=2.0, seed=0):
    rng = np.random.default_rng(seed)
    mu = mobius_upto(N)
    v = smooth_cutoff(N)
    q = (np.log(N+1.0))**q_logC * np.ones(N)
    a = mu[1:N+1].astype(float) * v * q
    K = kernel_K(N)
    off_diag = a @ (K @ a)
    diag = np.dot(a, a)
    return off_diag, diag, off_diag/diag, np.linalg.norm(K, 2)

if __name__ == "__main__":
    for N in (2000, 4000, 8000):
        off, diag, ratio, opnorm = weighted_quadratic_form(N)
        print(f"N={N:5d}  off={off: .3e}  diag={diag: .3e}  off/diag={ratio: .3e}  ||K||₂≈{opnorm: .3f}")