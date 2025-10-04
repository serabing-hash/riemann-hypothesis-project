import csv
import numpy as np
import matplotlib.pyplot as plt

# Read data
N, MSE, L, U = [], [], [], []
with open('../data/demo_results.csv', 'r', encoding='utf-8') as f:
    rdr = csv.DictReader(f)
    for row in rdr:
        N.append(int(row['N']))
        MSE.append(float(row['MSE']))
        L.append(float(row['CI_low']))
        U.append(float(row['CI_high']))

N = np.array(N)
MSE = np.array(MSE)
L = np.array(L)
U = np.array(U)

# Plot
plt.figure(figsize=(6,4))
yerr = np.vstack([MSE - L, U - MSE])
plt.errorbar(N, MSE, yerr=yerr, fmt='o-', capsize=4)
plt.xlabel('N')
plt.ylabel('Mean Square Error')
plt.title('Small-N Scaling (Demo)')
plt.tight_layout()
plt.savefig('../paper/figures/figure1.png', dpi=300)
print('Saved figure to ../paper/figures/figure1.png')
