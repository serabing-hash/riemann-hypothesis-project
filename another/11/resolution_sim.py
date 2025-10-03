
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def main(outdir="figures"):
    out = Path(outdir); out.mkdir(parents=True, exist_ok=True)
    N_base  = np.array([8000,12000,16000,20000,50000,100000,200000,1000000])
    M_base  = np.array([0.163,0.168,0.173,0.170,0.180,0.169,0.167,0.155])

    N_v96,  M_v96  = np.array([50000]),   np.array([0.168])
    N_v97,  M_v97  = np.array([100000]),  np.array([0.164])
    N_v98,  M_v98  = np.array([200000]),  np.array([0.160])
    N_v99,  M_v99  = np.array([500000]),  np.array([0.152])
    N_v100, M_v100 = np.array([1000000]), np.array([0.148])
    N_v11,  M_v11  = np.array([2000000]), np.array([0.146])

    plt.figure()
    plt.plot(np.log(np.log(N_base)), np.log(M_base), marker='o', label='Base (data/mixed)')
    plt.plot(np.log(np.log(N_v96)),  np.log(M_v96),  marker='o', label='v9.6')
    plt.plot(np.log(np.log(N_v97)),  np.log(M_v97),  marker='o', label='v9.7')
    plt.plot(np.log(np.log(N_v98)),  np.log(M_v98),  marker='o', label='v9.8')
    plt.plot(np.log(np.log(N_v99)),  np.log(M_v99),  marker='o', label='v9.9')
    plt.plot(np.log(np.log(N_v100)), np.log(M_v100), marker='o', label='v10.0')
    plt.plot(np.log(np.log(N_v11)),  np.log(M_v11),  marker='o', label='v11 Resolution')
    plt.xlabel("log log N"); plt.ylabel("log MSE*")
    plt.title("Figure 10: Comparative Log–Log Scaling (Base → v11 Resolution)")
    plt.legend(loc='best')
    outpath = out/"fig10.png"
    plt.savefig(outpath, dpi=200, bbox_inches="tight")
    plt.close()
    print("Saved", outpath)

if __name__ == "__main__":
    main()
