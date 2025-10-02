# run_batch.py
import subprocess, sys

batches = [
    ("8000,12000,16000", 256, 60, 1e-2, 200),
    ("20000,24000", 256, 80, 1e-2, 200),
    ("28000,32000", 256, 80, 5e-3, 150),
]

for Ns, Tpt, Tmax, ridge, boot in batches:
    cmd = [
        sys.executable, "nbbd_sampler.py",
        "--Ns", Ns,
        "--T_points", str(Tpt),
        "--T_max", str(Tmax),
        "--ridge", str(ridge),
        "--boot", str(boot),
        "--csv", "results.csv",
    ]
    print("Running:", " ".join(map(str, cmd)))
    subprocess.run(cmd, check=True)
print("Done. Results aggregated in results.csv")
