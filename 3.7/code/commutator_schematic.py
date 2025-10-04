\
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

out = Path(__file__).resolve().parents[1]/"figures"/"commutator_decay.png"

theta = 0.3
N = np.array([4000, 8000, 12000, 16000, 20000, 32000, 64000, 128000, 256000])
y = (np.log(N))**(-2*theta)

plt.figure()
plt.loglog(N, y, marker='o')
plt.xlabel('N')
plt.ylabel('||[E,E*]||  (schematic)')
plt.title('Predicted commutator decay ~ (log N)^(-2θ)')
plt.tight_layout()
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, dpi=300)
print(f"wrote {out}")
