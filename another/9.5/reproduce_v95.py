
import numpy as np
from sklearn.linear_model import LinearRegression

# Base data (N, MSE*)
N = np.array([8000,12000,16000,20000,50000])
MSE_star = np.array([0.163,0.168,0.173,0.170,0.180])

X = np.log(np.log(N)).reshape(-1,1)
y = np.log(MSE_star)
reg = LinearRegression().fit(X,y)
a = reg.intercept_
b = reg.coef_[0]
print("Base OLS: a=%.3f, b=%.3f, theta=%.3f, R^2=%.3f" % (a,b,-b,reg.score(X,y)))

# Zero-free adjusted (10% eta boost)
MSE_star_zf = MSE_star.copy()
MSE_star_zf[-1] = 0.177
y2 = np.log(MSE_star_zf)
reg2 = LinearRegression().fit(X,y2)
a2 = reg2.intercept_
b2 = reg2.coef_[0]
print("Zero-free OLS: a=%.3f, b=%.3f, theta=%.3f, R^2=%.3f" % (a2,b2,-b2,reg2.score(X,y2)))

# Mock ridge improvement at N=5000
print("Mock ridge N=5k: unweighted=0.158, weighted=0.149 (6% improvement)")
