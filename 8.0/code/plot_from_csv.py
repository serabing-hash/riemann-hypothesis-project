# plot_from_csv.py
import pandas as pd
import matplotlib.pyplot as plt

def main(csv_path="results.csv", out_png="scaling_plot.png"):
    df = pd.read_csv(csv_path).sort_values("N")
    has_ci = {"CI_low","CI_high"}.issubset(df.columns)
    plt.figure()
    if has_ci:
        yerr = [df["MSE"]-df["CI_low"], df["CI_high"]-df["MSE"]]
        plt.errorbar(df["N"], df["MSE"], yerr=yerr, fmt='o-', capsize=4)
    else:
        plt.plot(df["N"], df["MSE"], 'o-')
    plt.xscale("log")
    plt.xlabel("N (log scale)")
    plt.ylabel("Mean Square Error")
    plt.title("NB/BD Approximation Scaling (test grid)")
    plt.grid(True)
    plt.savefig(out_png, dpi=200, bbox_inches="tight")
    print("Saved:", out_png)

if __name__ == "__main__":
    main()
