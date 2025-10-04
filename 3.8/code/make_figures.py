import numpy as np
import matplotlib.pyplot as plt

# Regenerate the three figures from the paper.
c = 1.0
eps_values = [0.15, 0.20, 0.25]
J = np.arange(0, 18)

# Fig 1
for eps in eps_values:
    Cj = np.exp(-c*(2.0**(-J))) * (2.0**(-J))**(1.0-eps)
    plt.plot(J, Cj, marker='o', label=f'ε={eps:.2f}')
plt.xlabel('Band index j'); plt.ylabel('C_j (scaled)')
plt.title('Band constants vs. ε'); plt.legend(); plt.tight_layout()
plt.savefig('figures/band_constants_vs_eps.png', dpi=300); plt.clf()

# Fig 2
eps = 0.20
Cj = np.exp(-c*(2.0**(-J))) * (2.0**(-J))**(1.0-eps)
cum = np.cumsum(Cj)
plt.plot(J, cum, marker='s', label='Partial sum ∑_{k≤j} C_k')
plt.plot(J, (1-np.exp(-0.7*(J+1)))*cum.max(), linestyle='--', label='Envelope (schematic)')
plt.xlabel('Band index j'); plt.ylabel('Magnitude')
plt.title('Convergence of band partial sums'); plt.legend(); plt.tight_layout()
plt.savefig('figures/band_partial_sums.png', dpi=300); plt.clf()

# Fig 3
N = np.array([4000, 8000, 12000, 16000, 20000, 32000, 64000, 128000, 256000])
for theta in [0.2, 0.3, 0.4]:
    y = (np.log(N))**(-2*theta)
    plt.loglog(N, y, marker='o', label=f'θ={theta:.1f}')
plt.xlabel('N'); plt.ylabel('||[E,E*]|| (schematic)')
plt.title('Predicted commutator decay ~ (log N)^(-2θ)')
plt.legend(); plt.tight_layout()
plt.savefig('figures/commutator_decay_multi.png', dpi=300); plt.clf()

print('Figures saved in figures/.')
