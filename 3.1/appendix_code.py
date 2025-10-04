
import numpy as np
import matplotlib.pyplot as plt

# Data (weighted w_- = 1.20, sigma = 0.05)
N = np.array([8000, 12000, 16000, 20000])
MSE_plus = np.array([0.118995, 0.121417, 0.12328, 0.121589])
MSE_minus = np.array([0.207245, 0.214303, 0.222539, 0.21762])
MSE_star = np.array([0.16312, 0.16786, 0.172909, 0.169604])

# Figure 1
plt.figure()
plt.plot(N, MSE_star, marker='o')
plt.xlabel("N")
plt.ylabel("MSE* (combined)")
plt.title("NB/BD Combined MSE* vs N (w_- = 1.20, σ = 0.05)")
plt.tight_layout()
plt.savefig("figures/figure1_mse_star.png", dpi=300)

# Figure 2
x = np.arange(len(N))
width = 0.27
plt.figure()
plt.bar(x - width, MSE_plus, width, label='MSE+')
plt.bar(x, MSE_minus, width, label='MSE-')
plt.bar(x + width, MSE_star, width, label='MSE*')
plt.xticks(x, [str(n) for n in N])
plt.xlabel("N")
plt.ylabel("MSE")
plt.title("Boundary Reweighting (w_- = 1.20, σ = 0.05)")
plt.legend()
plt.tight_layout()
plt.savefig("figures/figure2_boundaries.png", dpi=300)
