import numpy as np

def smooth_bump(x):
    y = np.zeros_like(x)
    mask = (x>0) & (x<1)
    t = x[mask]
    y[mask] = np.exp(-1.0/(t*(1.0-t)))
    y /= (y.max() if y.max()>0 else 1.0)
    return y

def assemble_a(N):
    mu_toy = np.ones(N, dtype=float)
    mu_toy[1::2] = -1.0
    v = smooth_bump(np.arange(1, N+1)/N)
    q = np.ones(N, dtype=float)
    return mu_toy * v * q

def off_diag_ratio(N):
    a = assemble_a(N)
    n = np.arange(1, N+1, dtype=float)
    M, Nn = np.meshgrid(n, n, indexing='ij')
    K = np.exp(-0.5*np.abs(np.log(M/Nn)))
    A = np.outer(a, a)
    off = (A*K).sum() - np.sum(np.diag(A))
    diag = np.sum(a*a)
    return off/diag

if __name__ == "__main__":
    for N in [2000, 4000, 8000, 16000]:
        print(N, off_diag_ratio(N))