# NB/BD Sampler (train/test split + ζ target + bootstrap CI)

## What this does
- Fits Dirichlet polynomial coefficients `a_n` to approximate `1/zeta(1/2+it)` on a **train grid**, 
  then evaluates MSE and **bootstrap CI** on a **disjoint test grid**.
- Prevents the trivial MSE=0 artifact by separating train/test and using ζ.

## Quick start
```bash
pip install mpmath numpy matplotlib pandas
python nbbd_sampler.py --Ns 8000,12000,16000 --T_points 256 --T_max 60 --ridge 1e-2 --boot 200 --csv results.csv
python plot_from_csv.py  # -> scaling_plot.png
```

For multiple batches:
```bash
python run_batch.py
```

## Tips for low-spec PCs
- Increase `T_points` (e.g., 256~512) rather than pushing `N` too high at first.
- Keep `ridge >= 1e-2` to stabilize solves.
- Use `--boot 100~200` initially; raise later for tighter CIs.

## Output
- `results.csv`: rows of (N, MSE, CI_low, CI_high, T_points, T_max, ridge, boot, seed)
- `scaling_plot.png`: MSE vs N (log x-axis) with error bars if CI present.
