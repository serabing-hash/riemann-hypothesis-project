# code/sketch_lsqr_v26.py
import numpy as np
from sklearn.linear_model import HuberRegressor, LinearRegression

def countsketch_build(m, N, rng=None):
    rng = np.random.default_rng() if rng is None else rng
    h = rng.integers(0, m, size=N, dtype=np.int64)   # bucket index
    s = rng.choice(np.array([-1,1], dtype=np.int8), size=N)
    return h, s

def countsketch_apply(h, s, x):
    y = np.zeros(h.max()+1, dtype=np.float64)
    np.add.at(y, h, s * x)
    return y

def pcg_normal(A_mul, AT_mul, b, M_inv=None, iters=300, tol=1e-9):
    n = AT_mul(b).shape[0]
    x = np.zeros(n)
    r = AT_mul(b) - AT_mul(A_mul(x))
    z = M_inv(r) if M_inv else r
    p = z.copy()
    rz = np.dot(r, z)
    for k in range(iters):
        Ap = AT_mul(A_mul(p))
        alpha = rz / (np.dot(p, Ap)+1e-30)
        x += alpha * p
        r -= alpha * Ap
        if np.linalg.norm(r) < tol:
            break
        z = M_inv(r) if M_inv else r
        rz_new = np.dot(r, z)
        beta = rz_new / (rz+1e-30)
        p = z + beta * p
        rz = rz_new
    return x

# Regression example (replace with real data)
def demo_regression():
    N = np.array([8000, 12000, 16000, 20000, 32000, 100000])
    mse = np.array([0.024, 0.020, 0.016, 0.013, 0.010, 0.0090])
    X = np.log(np.log(N)).reshape(-1,1)
    y = np.log(mse)

    ols = LinearRegression().fit(X,y)
    huber = HuberRegressor().fit(X,y)

    return dict(theta_OLS = -ols.coef_[0],
                theta_Huber = -huber.coef_[0],
                alpha_OLS = ols.intercept_,
                alpha_Huber = huber.intercept_)

if __name__ == "__main__":
    print(demo_regression())
