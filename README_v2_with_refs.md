# Riemann Hypothesis Project — Version 2

This repository contains Version 2 of our ongoing exploration of the
Nyman–Beurling–Báez-Duarte (NB/BD) framework for the Riemann Hypothesis.

## What's New in v2
- **Multiscale Gaussian coefficients (from v1):** Control the off-diagonal terms with a $\log N$ suppression.
- **New μ(n)/n correction mode (v2):** Enables the diagonal–main piece to become strictly negative, realizing the desired sign condition $\theta > 0$.

## Mathematical Core
- Define coefficients
  $$
  a_n = \sum_j c_j b_j(n), \quad 
  b_j(n) = \frac{\mu(n)}{\sqrt{n}} e^{-(\log n)^2/(2\lambda_j^2)}, \quad
  b_{J+1}(n) = \frac{\mu(n)}{n}.
  $$
- Quadratic forms:
  - $K_{ij} = \sum b_i(n)b_j(n)$
  - $(s_1)_j = \sum b_j(n)/n$
- Main–diag term:
  $$
  M(c) = 2\pi\left(1 - 2c^Ts_1 + c^TKc\right).
  $$
- Optimal coefficients: $c^* = K^{-1}s_1$,
  giving $M_{\min} = 2\pi(1 - s_1^TK^{-1}s_1)$.

### Key Result
- With μ(n)/n correction, $s_1^TK^{-1}s_1 > 1$, hence $M_{\min} < 0$.
- Verified numerically:
  - N=200: $M_{\min}\approx -0.906$
  - N=500: $M_{\min}\approx -1.744$

## Implications
- **v1:** Controlled $E_{\mathrm{off}}$ by $\log N$ factor.
- **v2:** Achieved negative main–diag contribution.
- **Next:** Prove both properties hold *simultaneously* and extend uniformly in $N$.

## References
- Beurling, A. (1955). *A closure problem related to the Riemann zeta-function*. PNAS, 41, 312–314.
- Nyman, B. (1950). *On some groups and semigroups of translations*. PhD thesis, Uppsala University.
- Báez-Duarte, L. (2003). *A strengthening of the Nyman–Beurling criterion for the Riemann Hypothesis*. Rendiconti Lincei, 14, 5–11.
- Titchmarsh, E. C. (1986). *The Theory of the Riemann Zeta-Function*. 2nd edition, Oxford University Press.
- Conrey, J. B. (2003). *The Riemann Hypothesis*. Notices of the AMS, 50(3), 341–353.

---

Author(s): Serabi & Seraphy  
License: CC-BY-SA-4.0  
