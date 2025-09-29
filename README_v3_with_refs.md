# Riemann Hypothesis Project — Version 3

**Goal:** Jointly minimize the main–diag piece and the off-diagonal term under a unified coefficient choice in the NB/BD framework.

## Method
- Basis: multiscale Gaussians over `log n` with a correction mode `mu(n)/n`.
- Coefficients: `a_n = sum_j c_j b_j(n)`.
- Quadratic objective (convex in `c`):
  \[
  \mathcal{J}_\lambda(c) = 2\pi(1 - 2c^Ts_1 + c^T K c) + \lambda\, c^T (B^T W B) c + \rho \|c\|^2,
  \]
  where
  - `K = B^T B`,
  - `s_1 = B^T (1/n)`,
  - `W_{mn} = exp(-|log(m/n)|/2)` for `m != n`, `W_{nn}=0`.

The optimizer is explicit:
\[
c^* = (2\pi K + \lambda B^T W B + \rho I)^{-1} (2\pi s_1).
\]

## Sweep Protocol
Use `v3_sweep.py` to scan `(N, lambda, rho)` and save results as CSV.

## References
- Beurling, A. (1955). *A closure problem related to the Riemann zeta-function*. PNAS, 41, 312–314.
- Nyman, B. (1950). *On some groups and semigroups of translations*. PhD thesis, Uppsala University.
- Báez-Duarte, L. (2003). *A strengthening of the Nyman–Beurling criterion for the Riemann Hypothesis*. Rendiconti Lincei, 14, 5–11.
- Titchmarsh, E. C. (1986). *The Theory of the Riemann Zeta-Function*. 2nd edition, Oxford University Press.
- Conrey, J. B. (2003). *The Riemann Hypothesis*. Notices of the AMS, 50(3), 341–353.

---

Author(s): Serabi & Seraphy  
License: CC-BY-SA-4.0  
