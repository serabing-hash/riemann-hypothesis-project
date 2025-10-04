\
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

out = Path(__file__).resolve().parents[1]/"figures"/"band_constants_sum.png"

# Model C_j ~ exp(-c*2^{-j}) * (2^{-j})^{1-eps}
c = 1.0
eps = 0.2
J = np.arange(0,18)
Cj = np.exp(-c*(2.0**(-J))) * (2.0**(-J))**(1.0-eps)
cum = np.cumsum(Cj)

plt.figure()
plt.plot(J, Cj, marker='o', label='C_j (model)')
plt.plot(J, cum, marker='s', label='Partial sum')
plt.xlabel('Band index j')
plt.ylabel('magnitude')
plt.title('Band constants and cumulative sum')
plt.legend()
plt.tight_layout()
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, dpi=300)
print(f"wrote {out}")
