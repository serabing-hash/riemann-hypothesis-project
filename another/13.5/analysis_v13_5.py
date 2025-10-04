
import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt
import pandas as pd

# Base data (v13.4)
N_base = np.array([8000, 12000, 16000, 20000, 50000, 100000, 200000, 500000, 1000000, 2000000, 5000000, 10000000])
MSE_star_base = np.array([0.163120, 0.167860, 0.172909, 0.169604, 0.180, 0.169, 0.167, 0.160, 0.155, 0.152, 0.145, 0.142])

# Incremental v13.5 (ε=0.10; simulated)
N_inc = np.array([20000000])
MSE_plus_inc = np.array([0.092])
MSE_minus_w_inc = np.array([0.175])
MSE_star_inc = np.array([0.141])

# Fits
x_base = np.log(np.log(N_base))
y_base = np.log(MSE_star_base)
slope_b, intercept_b, r_b, _, _ = linregress(x_base, y_base)
theta_b, r2_b = -slope_b, r_b**2

N_ext = np.concatenate([N_base, N_inc])
MSE_star_ext = np.concatenate([MSE_star_base, MSE_star_inc])
x_ext = np.log(np.log(N_ext))
y_ext = np.log(MSE_star_ext)
slope_e, intercept_e, r_e, _, _ = linregress(x_ext, y_ext)
theta_e, r2_e = -slope_e, r_e**2

print("Base fit (≤10M): a={:.6f}, b={:.6f}, theta={:.6f}, R2={:.6f}".format(intercept_b, slope_b, theta_b, r2_b))
print("Extended fit (≤20M incl. v13.5): a={:.6f}, b={:.6f}, theta={:.6f}, R2={:.6f}".format(intercept_e, slope_e, theta_e, r2_e))

# Save CSVs
df_data = pd.DataFrame([
    *({"N": int(n), "MSE_plus": "", "MSE_minus_w": "", "MSE_star": float(m), "note": "base v13.4"} for n, m in zip(N_base, MSE_star_base)),
    {"N": int(N_inc[0]), "MSE_plus": float(MSE_plus_inc[0]), "MSE_minus_w": float(MSE_minus_w_inc[0]), "MSE_star": float(MSE_star_inc[0]), "note": "v13.5 incremental (simulated)"},
])
df_data.to_csv("data_v13_5.csv", index=False)

df_results = pd.DataFrame([
    {"fit": "base (≤10M)", "intercept_a": intercept_b, "slope_b": slope_b, "theta": theta_b, "R2": r2_b},
    {"fit": "extended (≤20M incl. v13.5)", "intercept_a": intercept_e, "slope_b": slope_e, "theta": theta_e, "R2": r2_e},
])
df_results.to_csv("results_v13_5.csv", index=False)

# Plot
plt.figure(figsize=(8,6))
plt.scatter(x_base, y_base, label="Base data (≤10M)")
plt.scatter(np.log(np.log(N_inc)), np.log(MSE_star_inc), label="v13.5 point (20M)")
xx = np.linspace(min(x_base.min(), np.log(np.log(N_inc)).min())*0.98, max(x_ext.max(), x_base.max())*1.02, 200)
plt.plot(xx, intercept_b + slope_b*xx, label=f"Base OLS (θ={theta_b:.3f}, R²={r2_b:.3f})")
plt.plot(xx, intercept_e + slope_e*xx, label=f"Extended OLS (θ={theta_e:.3f}, R²={r2_e:.3f})", linestyle="--")
plt.xlabel("log log N")
plt.ylabel("log MSE*")
plt.title("Incremental Comparative Log-Log Regression (v13.5)")
plt.legend()
plt.grid(True)
plt.savefig("figure3.png", dpi=300)
plt.close()
