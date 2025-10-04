#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def fig_band_constants_vs_eps():
    eps = np.linspace(0.02, 0.20, 200)
    Cj = 1/(1+5*eps) + 0.1*np.log(1+eps)
    plt.figure()
    plt.plot(eps, Cj, label="C_j(ε) schematic")
    plt.xlabel("ε")
    plt.ylabel("C_j(ε)")
    plt.title("Band constants vs ε (schematic)")
    plt.legend()
    plt.tight_layout()
    plt.savefig("figures/band_constants_vs_eps.png", dpi=200)
    plt.close()

def fig_band_partial_sums():
    j = np.arange(1, 25)
    C = 0.3*np.exp(-j/6.0) + 0.02
    partial = np.cumsum(C)
    plt.figure()
    plt.plot(j, partial, marker="o", label="∑_{k≤j} C_k (schematic)")
    plt.xlabel("j (log bands)")
    plt.ylabel("Partial Sum")
    plt.title("Partial sums of band contributions (schematic)")
    plt.legend()
    plt.tight_layout()
    plt.savefig("figures/band_partial_sums.png", dpi=200)
    plt.close()

def fig_commutator_decay_multi():
    N = np.logspace(3.5, 5.5, 120)
    theta_vals = [0.10, 0.15, 0.20]
    plt.figure()
    for th in theta_vals:
        decay = (np.log(N))**(-2*th)
        plt.plot(N, decay, label=f"‖[E,E*]‖ ~ (log N)^(-{2*th:.2f})")
    plt.xscale("log"); plt.yscale("log")
    plt.xlabel("N (log scale)")
    plt.ylabel("Commutator norm (schematic)")
    plt.title("Predicted commutator decay for various θ")
    plt.legend()
    plt.tight_layout()
    plt.savefig("figures/commutator_decay_multi.png", dpi=200)
    plt.close()

if __name__ == "__main__":
    fig_band_constants_vs_eps()
    fig_band_partial_sums()
    fig_commutator_decay_multi()
    print("Figures saved under ./figures")
