# code/hutchpp.py
# Hutch++ trace estimator for PSD matrix A using only matvecs.
# For NB/BD, use A = E^T E by providing functions Emul(x) and ETmul(x).

import numpy as np

def hutchpp_trace(Amul, n, s=20, r=40, rng=None):
    """
    Estimate tr(A) for A (n x n) PSD using Hutch++.
    Amul: function(v) -> A @ v  (matvec)
    n   : dimension
    s   : sketch size
    r   : probe size
    """
    rng = np.random.default_rng() if rng is None else rng

    # (i) Build sketch subspace Q from s Gaussian probes
    Omega = rng.standard_normal((n, s))
    Y = np.column_stack([Amul(Omega[:,i]) for i in range(s)])
    Q, _ = np.linalg.qr(Y, mode='reduced')  # (n x s')

    # (ii) Exact trace on the sketched subspace
    B = Q.T @ np.column_stack([Amul(Q[:,i]) for i in range(Q.shape[1])])
    tr_sketch = np.trace(B)

    # (iii) Hutchinson on orthogonal complement
    tr_hutch = 0.0
    for _ in range(r):
        z = rng.choice([-1.0, 1.0], size=n)  # Rademacher
        z_perp = z - Q @ (Q.T @ z)
        Az = Amul(z_perp)
        tr_hutch += z_perp @ Az
    tr_hutch /= r

    return tr_sketch + tr_hutch

# Helper for A = E^T E with only E matvecs available
def make_AtA(Emul, ETmul):
    def AtAmul(v):
        return ETmul(Emul(v))
    return AtAmul
