#Sergey Kurennoy
"""
Just used for generating the picture of 
the family of generalized logistic distributions for 
different shape parameters
"""

import numpy as np
from scipy.stats import levy_stable, genlogistic
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

c = 0.05
mean, var, skew, kurt = genlogistic.stats(c, moments='mvsk')
print("For shape = ",c," mean, var, skew, kurt:\n  ",mean, var, skew, kurt)
x = np.linspace(genlogistic.ppf(0.2, c),genlogistic.ppf(0.99, c), 100)
ax.plot(x, genlogistic.pdf(x, c),
        'r-', lw=2, alpha=0.6, label='λ=0.05')

c = 0.075
mean, var, skew, kurt = genlogistic.stats(c, moments='mvsk')
print("For shape = ",c," mean, var, skew, kurt:\n  ",mean, var, skew, kurt)
x = np.linspace(genlogistic.ppf(0.1, c),genlogistic.ppf(0.99, c), 100)
ax.plot(x, genlogistic.pdf(x, c),
        'g-', lw=2, alpha=0.6, label='λ=0.075')

c = 0.10
mean, var, skew, kurt = genlogistic.stats(c, moments='mvsk')
print("For shape = ",c," mean, var, skew, kurt:\n  ",mean, var, skew, kurt)
x = np.linspace(genlogistic.ppf(0.05, c),genlogistic.ppf(0.99, c), 100)
ax.plot(x, genlogistic.pdf(x, c),
        'k-', lw=2, alpha=0.6, label='λ=0.10')

c = 0.15
mean, var, skew, kurt = genlogistic.stats(c, moments='mvsk')
print("For shape = ",c," mean, var, skew, kurt:\n  ",mean, var, skew, kurt)
x = np.linspace(genlogistic.ppf(0.015, c),genlogistic.ppf(0.99, c), 100)
ax.plot(x, genlogistic.pdf(x, c),
        'b-', lw=2, alpha=0.6, label='λ=0.15')

c = 0.2
mean, var, skew, kurt = genlogistic.stats(c, moments='mvsk')
print("For shape = ",c," mean, var, skew, kurt:\n  ",mean, var, skew, kurt)
x = np.linspace(genlogistic.ppf(0.005, c),genlogistic.ppf(0.99, c), 100)
ax.plot(x, genlogistic.pdf(x, c),
        'm-', lw=2, alpha=0.6, label='λ=0.20')

#ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='upper left', prop={'size': 24}, frameon=False)
plt.show(dpi=100)

"""
#alpha, beta, gamma, delta = 1.7, 0.0, 0.01, 0.02
#mean, var, skew, kurt = levy_stable.stats(alpha, beta, gamma, delta, moments='mvsk')
#print("For alpha, beta, gamma, delta = ",alpha,',',beta,',',gamma,',',delta,
#      " mean, var, skew, kurt:\n  ",mean, var, skew, kurt)
#
y = np.linspace(levy_stable.ppf(0.01, alpha, beta, gamma, delta),
                levy_stable.ppf(0.99, alpha, beta, gamma, delta), 100)
plt.plot(y, levy_stable.pdf(y, alpha, beta, gamma, delta),
        'b-', lw=2, alpha=0.6, label='levy_stable pdf')

#draw = levy_stable.rvs(alpha, beta, 1.0, 1.0, size=points, random_state=None)
#draw = levy_stable.rvs(loc=1.0, scale=sq2, size=points, random_state=None)

#print(np.quantile(draw, 0.01),levy_stable.ppf(0.01, alpha, beta, 1.0, 1.0))
#print(scipy.quantile(draw, 0.01),norm.ppf(0.01, loc=1.0, scale=sq2))
"""

