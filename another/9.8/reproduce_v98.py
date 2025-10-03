# reproduce_v98.py
# Reproducibility script for v9.8
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample data for demonstration (mocked for structure)
N = np.array([8000, 12000, 16000, 20000, 50000, 100000, 200000])
MSE_star = np.array([0.163,0.168,0.173,0.170,0.180,0.169,0.167])

# log-log regression
X = np.log(np.log(N)).reshape(-1,1)
y = np.log(MSE_star)
model = LinearRegression().fit(X,y)
a, b = model.intercept_, model.coef_[0]
theta = -b
print("OLS a=%.3f, b=%.3f, theta=%.3f, R^2=%.3f"%(a,b,theta,model.score(X,y)))

# Plot
plt.figure()
plt.plot(np.log(np.log(N)), y, "ko-", label="Data")
plt.plot(np.log(np.log(N)), model.predict(X), "r--", label="Fit")
plt.xlabel("log log N")
plt.ylabel("log MSE*")
plt.title("Strongest Zero-Free Simulation (v9.8)")
plt.legend()
plt.savefig("strongest_zero_free_scaling_v98.png")
