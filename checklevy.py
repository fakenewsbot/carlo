#Sergey Kurennoy
"""
Just checks the stability property of the stable distribution
"""

from scipy.stats import levy_stable
import numpy as np

points = 1000000
#jennys_constant = 8675309

alpha = 1.7
beta = 0.0
delta = 1.0
gamma = 1.0

draw1 = levy_stable.rvs(alpha, beta, gamma, delta, size=points, random_state=None)
draw2 = levy_stable.rvs(alpha, beta, gamma, delta, size=points, random_state=None)

draw = np.zeros(points)
for i in range(points):
    draw[i] = draw1[i] + draw2[i]

#use scipy's quantile estimator to estimate the parameters and convert to S parameterization
#pconv = lambda alpha, beta, mu, sigma: (alpha, beta, mu - sigma * beta * np.tan(np.pi * alpha / 2.0), sigma)

print(levy_stable._fitstart(draw1))
print(levy_stable._fitstart(draw2))
print(levy_stable._fitstart(draw))