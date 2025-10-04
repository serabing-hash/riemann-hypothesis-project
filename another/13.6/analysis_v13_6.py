import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt
import pandas as pd

N_vals = np.array([8000,12000,16000,20000,50000,100000,200000,500000,
                   1000000,2000000,5000000,10000000,20000000,50000000])
MSE_star = np.array([0.163120,0.167860,0.172909,0.169604,0.180,0.169,
                     0.167,0.160,0.155,0.152,0.145,0.142,0.140,0.138])

log_logN = np.log(np.log(N_vals))
log_MSE = np.log(MSE_star)
slope, intercept, r_val, _, _ = linregress(log_logN, log_MSE)
theta = -slope
print("a =", intercept, "b =", slope, "theta =", theta, "R^2 =", r_val**2)

plt.scatter(log_logN, log_MSE, label="Data")
plt.plot(log_logN, intercept+slope*log_logN, label=f"Fit θ≈{theta:.3f}", color="purple")
plt.xlabel("log log N")
plt.ylabel("log MSE*")
plt.legend()
plt.savefig("figure3.png", dpi=300)
