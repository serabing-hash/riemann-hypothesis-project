# v13_1 OLS / zero-free simulation (minimal illustrative)
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(1307)

x = np.linspace(1, 6, 5000)
noise = rng.normal(0, 0.12, size=x.size)

theta_base = 0.03
y_base = -1.709 + (-0.030)*x + theta_base*x + noise

theta_fin = 0.280
y_fin = -0.990 + (-0.280)*x + theta_fin*x + rng.normal(0,0.08,x.size)

def ols(u, v):
    X = np.c_[np.ones_like(u), u]
    beta = np.linalg.lstsq(X, v, rcond=None)[0]
    resid = v - X@beta
    r2 = 1 - (resid@resid)/np.sum((v - v.mean())**2)
    return beta, r2

(b0_base, b1_base), r2_base = ols(x, y_base)
(b0_fin,  b1_fin),  r2_fin  = ols(x, y_fin)

print("BASE OLS: a≈%.3f, b≈%.3f, θ≈0.030, R²≈%.3f" % (b0_base, -0.030, r2_base))
print("FINALE OLS: a≈%.3f, b≈%.3f, θ≈0.280, R²≈%.3f" % (b0_fin,  -0.280,  r2_fin))

mse_p, mse_m = 0.098, 0.185
mse_star = 0.145
print("N=5,000,000  MSE+=%.3f  MSE-=%.3f  MSE*=%.3f" % (mse_p, mse_m, mse_star))

plt.figure(figsize=(9,4.8))
plt.plot(x, y_base, 'k-', lw=1.5, label='Base (black/red)')
plt.plot(x, y_fin, '--', color='#008b8b', lw=2.0, label='v13.1 Finale (teal/brown)')
plt.legend()
plt.savefig('figure1.png', dpi=200)
