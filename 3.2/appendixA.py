import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt

# Data (consistent with v3.2 calibration)
N = np.array([8000, 12000, 16000, 20000, 50000, 100000, 200000, 500000, 1000000])
MSE_star = np.array([0.163, 0.168, 0.173, 0.170, 0.180, 0.169, 0.167, 0.160, 0.155])

# Regression
x = np.log(np.log(N))
y = np.log(MSE_star)
slope, intercept, r, _, _ = linregress(x, y)
theta = -slope

print(f"a={intercept:.3f}, b={slope:.3f}, theta={theta:.3f}, R²={r**2:.3f}")

# Plot
plt.figure(figsize=(7,5))
plt.scatter(x, y, color='black', label='Base Data')
plt.plot(x, intercept + slope*x, color='red', label=f'Fit: slope={slope:.3f}')
plt.title("Asymptotic Comparative Log-Log Regression")
plt.xlabel("log log N")
plt.ylabel("log MSE*")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("figures/asymptotic_curve.png", dpi=300)
plt.show()