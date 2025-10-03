import numpy as np
from scipy.stats import linregress

# Extended base data for v11 (N=8k~2M from v10.0/v11)
N_base_v11 = np.array([8000, 12000, 16000, 20000, 50000, 100000, 200000, 500000, 1000000, 2000000])
MSE_star_base_v11 = np.array([0.163120, 0.167860, 0.172909, 0.169604, 0.180, 0.169, 0.167, 0.160, 0.155, 0.152])  # From v11 trend

# Base OLS
log_log_N_v11 = np.log(np.log(N_base_v11))
log_MSE_base_v11 = np.log(MSE_star_base_v11)
slope_base_v11, intercept_base_v11, r_base_v11, _, _ = linregress(log_log_N_v11, log_MSE_base_v11)
a_base_v11