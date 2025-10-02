import numpy as np

def loglog(x): 
    return np.log(np.log(x))

def fit_theta(N, mse):
    X = loglog(np.array(N)).reshape(-1,1)
    y = np.log(np.array(mse))
    X1 = np.hstack([np.ones_like(X), X])
    beta = np.linalg.lstsq(X1, y, rcond=None)[0]
    alpha, slope = beta[0], beta[1]
    theta = -slope
    return alpha, theta

def contradiction_check(N_list, mse_list, eps0=1e-2, theta_min=0.1):
    alpha, theta = fit_theta(N_list, mse_list)
    decaying = theta > theta_min
    persistent = any(mse > eps0 for mse in mse_list[-3:])
    return dict(alpha=alpha, theta=theta, decaying=decaying, persistent=persistent)

if __name__ == '__main__':
    N = [8000, 12000, 16000, 20000, 32000, 100000]
    mse = [0.024, 0.020, 0.016, 0.013, 0.010, 0.0090]
    out = contradiction_check(N, mse, eps0=0.012, theta_min=0.2)
    print(out)
