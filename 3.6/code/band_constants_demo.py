#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def band_constants(c=0.35, eps=0.20, Jmax=14):
    j = np.arange(0, Jmax+1)
    Cj = np.exp(-c * (2.0**(-j))) * (2.0**(-j))**(1.0 - eps)
    S = np.cumsum(Cj)
    return j, Cj, S

def main(out_png='figures/band_constants_sum.png', c=0.35, eps=0.20, Jmax=14):
    j, Cj, S = band_constants(c=c, eps=eps, Jmax=Jmax)
    plt.figure(figsize=(6,4))
    plt.plot(j, Cj, marker='o', label='C_j')
    plt.plot(j, S, marker='s', linestyle='--', label='Partial sum')
    plt.xlabel('Band index j')
    plt.ylabel('Magnitude')
    plt.title('Band-wise constants C_j and their partial sums')
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_png, dpi=300)
    print(f"Saved figure to {out_png}")

if __name__ == "__main__":
    main()
