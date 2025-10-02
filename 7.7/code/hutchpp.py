# code/hutchpp.py
import numpy as np

def hutchpp_trace(Amul, n, s=20, r=40, rng=None):
    rng = np.random.default_rng() if rng is None else rng
    Omega = rng.standard_normal((n, s))
    Y = np.column_stack([Amul(Omega[:,i]) for i in range(s)])
    Q, _ = np.linalg.qr(Y, mode='reduced')
    B = Q.T @ np.column_stack([Amul(Q[:,i]) for i in range(Q.shape[1])])
    tr_sketch = np.trace(B)
    tr_hutch = 0.0
    for _ in range(r):
        z = rng.choice([-1.0, 1.0], size=n)
        z_perp = z - Q @ (Q.T @ z)
        Az = Amul(z_perp)
        tr_hutch += z_perp @ Az
    tr_hutch /= r
    return float(tr_sketch + tr_hutch)

def make_AtA(Emul, ETmul):
    def AtAmul(v):
        return ETmul(Emul(v))
    return AtAmul
