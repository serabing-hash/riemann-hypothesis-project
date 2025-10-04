# appendixA.py : generate simple placeholder figures (no seaborn)
import numpy as np
import matplotlib.pyplot as plt
import os

# --- user-editable data (replace with your CSV-driven results) ---
Ns = np.array([8000, 12000, 16000, 20000])
mse_star = np.array([0.163, 0.168, 0.173, 0.170])
ci_low   = np.array([0.118, 0.121, 0.123, 0.122])
ci_high  = np.array([0.208, 0.214, 0.223, 0.218])

# plus / minus boundary placeholders (for the comparison plot)
mse_plus  = mse_star * 0.72
mse_minus = mse_star * 1.28
mse_minus_weighted = mse_minus * 0.88  # example "reweighting" improvement

outdir = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(outdir, exist_ok=True)

# Figure 1: MSE scaling with CI
plt.figure()
plt.errorbar(Ns, mse_star, yerr=[mse_star-ci_low, ci_high-mse_star], fmt='o', capsize=3, label='MSE* (95% CI)')
plt.xscale('log')
plt.xlabel('N (log scale)')
plt.ylabel('Mean Square Error')
plt.title('NB/BD Scaling (placeholder)')
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(outdir, 'mse_scaling.png'), dpi=300)
plt.close()

# Figure 2: base vs boundary-reweighted
plt.figure()
plt.plot(Ns, mse_plus, 'o-', label='MSE+')
plt.plot(Ns, mse_minus, 's--', label='MSE− (unweighted)')
plt.plot(Ns, mse_minus_weighted, 'd-.', label='MSE− (weighted, w_-=1.2)')
plt.xscale('log')
plt.xlabel('N (log scale)')
plt.ylabel('MSE (components)')
plt.title('Boundary Reweighting (placeholder)')
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(outdir, 'zero_free_comparison.png'), dpi=300)
plt.close()

# Figure 3: theta fit on log-log axis (toy example)
loglogN = np.log(np.log(Ns))
logM = np.log(mse_star)
# simple linear fit
A = np.vstack([loglogN, np.ones_like(loglogN)]).T
slope, intercept = np.linalg.lstsq(A, logM, rcond=None)[0]

plt.figure()
plt.scatter(loglogN, logM, label='data', zorder=3)
xfit = np.linspace(loglogN.min(), loglogN.max(), 100)
yfit = slope * xfit + intercept
plt.plot(xfit, yfit, label=f'OLS fit: log MSE = {intercept:.3f} + {slope:.3f} log log N')
plt.xlabel('log log N')
plt.ylabel('log MSE*')
plt.title('Theta Fit (placeholder)')
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(outdir, 'theta_fit.png'), dpi=300)
plt.close()

print("Figures saved to:", outdir)
