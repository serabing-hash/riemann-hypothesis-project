
# generate_figures_v10_another.py
# Recreates the comparative log–log figure used in v10.0 Another (no explicit colors).
import numpy as np
import matplotlib.pyplot as plt
import os

def main(outdir="figures"):
    os.makedirs(outdir, exist_ok=True)
    N_base = np.array([8000, 12000, 16000, 20000, 50000, 100000, 200000])
    MSE_base = np.array([0.163, 0.168, 0.173, 0.170, 0.180, 0.169, 0.167])

    N_v96 = np.array([50000])
    MSE_v96 = np.array([0.168])

    N_v97 = np.array([100000])
    MSE_v97 = np.array([0.164])

    N_v98 = np.array([200000])
    MSE_v98 = np.array([0.160])

    N_v10 = np.array([1000000])
    MSE_v10 = np.array([0.148])

    plt.figure()
    plt.plot(np.log(np.log(N_base)), np.log(MSE_base), marker='o', label='Base (data)')
    plt.plot(np.log(np.log(N_v96)), np.log(MSE_v96), marker='o', label='v9.6')
    plt.plot(np.log(np.log(N_v97)), np.log(MSE_v97), marker='o', label='v9.7')
    plt.plot(np.log(np.log(N_v98)), np.log(MSE_v98), marker='o', label='v9.8')
    plt.plot(np.log(np.log(N_v10)), np.log(MSE_v10), marker='o', label='v10.0 Another')
    plt.xlabel("log log N")
    plt.ylabel("log MSE*")
    plt.title("Figure 9: Comparative Log–Log Scaling (Base → v10.0 Another)")
    plt.legend(loc='best')
    outpath = os.path.join(outdir, "fig9.png")
    plt.savefig(outpath, dpi=200, bbox_inches="tight")
    plt.close()
    print("Saved:", outpath)

if __name__ == "__main__":
    main()
