import numpy as np
import statsmodels.api as sm

# Data (extended with N=50000)
N_vals = np.array([8000, 12000, 16000, 20000, 50000])
MSE_star = np.array([0.167, 0.173, 0.174, 0.170, 0.177])

# Regression: log(MSE*) = a + b log log N
X = np.log(np.log(N_vals))
X = sm.add_constant(X)
y = np.log(MSE_star)
model = sm.OLS(y, X).fit()
print(model.summary())

# Predictions
print("OLS coefficients:", model.params)
print("Predicted MSE* at N=50000:", np.exp(model.predict([1, np.log(np.log(50000))])))

# Ridge mock improvement at N=5000
base = 0.160
ridge = base * 0.95
print("Ridge mock improvement:", ridge)
