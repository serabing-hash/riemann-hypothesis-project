# Appendix reproducibility code for v3.0 (orthodox)
import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt

N = np.array([8000, 12000, 16000, 20000, 50000, 100000, 200000])
MSE = np.array([0.163, 0.168, 0.173, 0.170, 0.180, 0.169, 0.167])

log_logN = np.log(np.log(N))
log_MSE = np.log(MSE)

slope, intercept, r, _, _ = linregress(log_logN, log_MSE)
theta = -slope
print(f"a={intercept:.4f}, b={slope:.4f}, theta={theta:.4f}, R^2={r**2:.3f}")

plt.figure(figsize=(6,4))
plt.scatter(log_logN, log_MSE, label="Data")
xline = np.linspace(log_logN.min(), log_logN.max(), 200)
plt.plot(xline, intercept + slope * xline, label=f"Fit (theta={theta:.3f})")
plt.xlabel("log log N")
plt.ylabel("log MSE")
plt.title("Weighted NB/BD Scaling (v3.0)")
plt.legend()
plt.tight_layout()
plt.savefig("figures/weighted_scaling.png", dpi=300)
