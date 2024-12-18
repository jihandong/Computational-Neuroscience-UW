
## Q

Suppose we are diagnosing a very rare illness, which happens only once in 100 million people on average. Luckily, we have a test for this illness but it is not perfectly accurate. If somebody has the disease, it will report positive 99% of the time. If somebody does not have the disease, it will report positive 2% of the time.

Suppose a patient walks in and tests positive for the disease. Using the maximum likelihood (ML) and maximum a posteriori (MAP) criteria, would we diagnose them positive?


## A

Let's define
$$
\begin{align*}
D &: \text{got illness} \\
\~D &: \text{didn't get illness} \\
T_+ &: \text{test positive} \\
T_- &: \text{test negative}
\end{align*}
$$

and

$$
\begin{align*}
P(D) &= 10^{-8} \\
P(T_+|D) &= 0.99 \\
P(T_+|\~D) &= 0.02
\end{align*}
$$

---

For ML criterion, we compare $P(T_+|D)$ and $P(T_+|\~D)$, so we would directly **diagnose positive**.

For MAP criterion, we compare $P(D|T_+)$ and $P(\~D|T_+)$

$$
\begin{align*}
P(D|T_+) &= \frac { P(T_+|D)P(D) } { P(T_+) } =\frac { 0.99 * 10^{-8}}{ P(T_+) } \\
P(\~D|T_+) &= \frac { P(T_+|\~D)P(\~D) } { P(T_+) } =\frac { 0.02 * (1 - 10^{-8}) } { P(T_+) }
\end{align*}
$$

Since we consider the prior $P(D)$, we would **diagnose negative**.