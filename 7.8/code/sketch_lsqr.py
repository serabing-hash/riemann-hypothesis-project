
import numpy as np
from sklearn.linear_model import HuberRegressor, LinearRegression

# Example synthetic log-log data
N = np.array([8000, 12000, 16000, 20000, 32000, 100000])
mse = np.array([0.024, 0.020, 0.016, 0.013, 0.010, 0.0090])
X = np.log(np.log(N)).reshape(-1,1)
y = np.log(mse)

# OLS regression
ols = LinearRegression().fit(X,y)
print("OLS slope theta:", -ols.coef_[0], "intercept:", ols.intercept_)

# Huber regression (robust)
huber = HuberRegressor().fit(X,y)
print("Huber slope theta:", -huber.coef_[0], "intercept:", huber.intercept_)

# Preconditioner sketch for A = I+E
def preconditioner(A):
    # Diagonal+band preconditioner
    P = np.diag(np.diag(A))
    k=3
    for i in range(len(A)):
        for j in range(max(0,i-k),min(len(A),i+k+1)):
            P[i,j] = A[i,j]
    return P
