import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt  # Optional: plot for figures

# Original data from v9.4 (N and MSE*)
N = np.array([8000, 12000, 16000, 20000])
MSE_star = np.array([0.163120, 0.167860, 0.172909, 0.169604])

# Compute log log N and log MSE*
log_log_N = np.log(np.log(N))
log_MSE = np.log(MSE_star)

# OLS fit: log(MSE*) = a + b * log log N
slope, intercept, r_value, p_value, std_err = linregress(log_log_N, log_MSE)
a = intercept
b = slope
theta = -b
r_squared = r_value**2

print(f"OLS fit: a ≈ {a:.3f}, b ≈ {b:.3f}, θ = -b ≈ {theta:.3f}, R² ≈ {r_squared:.3f}")

# Predict for N=50k (extrapolation)
N_50k = 50000
log_log_N_50k = np.log(np.log(N_50k))
log_MSE_50k_pred = a + b * log_log_N_50k
MSE_50k_pred = np.exp(log_MSE_50k_pred)
print(f"N=50k predicted MSE* ≈ {MSE_50k_pred:.3f}")

# Mock ridge simulation (simple scale-up for N=5k subset, assuming ridge with alpha=0.05, w_minus=1.2)
# Baseline unweighted MSE ~0.177 (extrapolated from trend), 5% improvement
unweighted_MSE_mock = 0.177  # mock baseline at N=5k scale
ridge_improvement = 0.05  # 5% reduction with w_-=1.2
weighted_MSE_mock = unweighted_MSE_mock * (1 - ridge_improvement)
print(f"Mock ridge sim (N=5k scale-up): MSE ≈ {weighted_MSE_mock:.3f} (w_-=1.2, σ=0.05; 5% improvement over unweighted)")

# Boundary-wise example: Assume MSE- stabilizes (e.g., +0.02 from N=20k)
MSE_minus_mock = 0.217620 + 0.02  # from Table, slight increase but stabilized
print(f"Boundary-wise MSE- stabilization example (N=50k): ≈ {MSE_minus_mock:.3f}")

# Optional: Plot for Figure (save as PNG for paper)
plt.figure(figsize=(6,4))
plt.plot(log_log_N, log_MSE, 'bo', label='Data')
plt.plot(log_log_N, intercept + slope * log_log_N, 'r--', label=f'Fit: θ ≈ {theta:.3f}')
plt.scatter([log_log_N_50k], [log_MSE_50k_pred], color='g', s=50, label=f'N=50k pred: {MSE_50k_pred:.3f}')
plt.xlabel('log log N')
plt.ylabel('log MSE*')
plt.legend()
plt.title('Extended Log-Log Regression')
plt.savefig('ols_extended.png')  # For v9.3 Figure
plt.show()