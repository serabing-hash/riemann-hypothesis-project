
import numpy as np
from scipy.stats import linregress
import pandas as pd

def fit_loglog(csv_path="mse_data.csv"):
    df = pd.read_csv(csv_path)
    N = df["N"].to_numpy(dtype=float)
    y = df["MSE_star"].to_numpy(dtype=float)
    X = np.log(np.log(N))
    Y = np.log(y)
    slope, intercept, r, p, se = linregress(X, Y)
    theta = -slope
    return {
        "intercept": float(intercept),
        "slope": float(slope),
        "theta": float(theta),
        "r_value": float(r),
        "r_squared": float(r*r),
        "stderr": float(se)
    }

if __name__ == "__main__":
    res = fit_loglog()
    print(res)
