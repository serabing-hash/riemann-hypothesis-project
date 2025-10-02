# code/pcg_precond.py
import numpy as np

def build_band_preconditioner(A, k=3):
    P = np.diag(np.diag(A)).astype(float)
    n = A.shape[0]
    for i in range(n):
        j0, j1 = max(0, i-k), min(n, i+k+1)
        P[i, j0:j1] = A[i, j0:j1]
    # Use diagonal inverse of P for cheap M^{-1} approx
    d = np.diag(P).copy()
    d[d==0.0] = 1.0
    invd = 1.0/d
    return lambda r: invd * r

def pcg_normal(A_mul, AT_mul, b, M_inv=None, iters=300, tol=1e-9):
    n = AT_mul(b).shape[0]
    x = np.zeros(n)
    r = AT_mul(b) - AT_mul(A_mul(x))
    z = M_inv(r) if M_inv else r
    p = z.copy()
    rz = np.dot(r, z)
    for _ in range(iters):
        Ap = AT_mul(A_mul(p))
        alpha = rz / (np.dot(p, Ap) + 1e-30)
        x += alpha * p
        r -= alpha * Ap
        if np.linalg.norm(r) < tol:
            break
        z = M_inv(r) if M_inv else r
        rz_new = np.dot(r, z)
        beta = rz_new / (rz + 1e-30)
        p = z + beta * p
        rz = rz_new
    return x
