
# appendix_code.py -- generate Figure 1 for v13.2
import numpy as np
import matplotlib.pyplot as plt

x = np.logspace(0, 6, 300)

y_base_black = 10**(-0.03*np.log10(x) - 1.709)
y_base_red   = 10**(-0.03*np.log10(x) - 1.709 + 0.2)

y_prev1 = 10**(-0.12*np.log10(x) - 1.3)
y_prev2 = 10**(-0.20*np.log10(x) - 1.1)

y_final_teal  = 10**(-0.28*np.log10(x) - 0.99)
y_final_brown = 10**(-0.28*np.log10(x) - 1.15)

plt.figure(figsize=(7,5))
plt.loglog(x, y_base_black, color='black', label='Base (black)', linewidth=2)
plt.loglog(x, y_base_red, color='red', label='Base (red)', linewidth=1.5, alpha=0.8)
plt.loglog(x, y_prev1, label='Previous (fit A)')
plt.loglog(x, y_prev2, label='Previous (fit B)')
plt.loglog(x, y_final_teal, color='teal', linestyle='--', linewidth=2.5, label='v13 Finale (teal dashed)')
plt.loglog(x, y_final_brown, color='saddlebrown', linestyle='--', linewidth=2, alpha=0.9, label='v13 Finale (brown dashed)')
plt.xlabel('n (log scale)')
plt.ylabel('fit value (log scale)')
plt.title('Comparative log-log fits: Base vs Previous vs v13 Finale')
plt.legend()
plt.tight_layout()
plt.savefig('figure1.png', dpi=200)
print('Saved figure1.png')
