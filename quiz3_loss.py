import numpy as np
from scipy.stats import norm
from scipy.optimize import minimize
import matplotlib.pyplot as plt

m1 = 5.
s1 = 0.5
m2 = 7.
s2 = 1.
x0 = 5.

# solution
solution = minimize(
    # loss1 = w1 * cdf2(x)
    # loss2 = w2 * (1 - cdf1(x))
    lambda x: norm.cdf(x, m2, s2) - 2 * norm.cdf(x, m1, s1),
    x0)

print(solution)

# illustration
x = np.linspace(0, 10, 1000)
n1 = norm.pdf(x, m1, s1)
n2 = norm.pdf(x, m2, s2)
y = norm.cdf(x, m2, s2) - 2 * norm.cdf(x, m1, s1) 

plt.plot(x, n1, label="Normal Distribution 1", color='blue')
plt.plot(x, n2, label="Normal Distribution 2", color='yellow')
plt.plot(x, y, label="Loss", color='green')
plt.legend()
plt.show()
