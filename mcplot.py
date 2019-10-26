#Sergey Kurennoy
"""
Produces the plot of the sample histogram with fitting distribution.
Assumes that gammalist, deltalist, samples, fitresult are all populated.
"""
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from scipy.stats import genlogistic


numplots = len(deltalist)*len(gammalist)

#Prompt for case index
gdindex = int(input("Which plot (1 to "+str(numplots)+")? ")) - 1

#Determine gamma and delta
gamma = gammalist[gdindex % len(gammalist)]
delta = deltalist[(gdindex - (gdindex % len(gammalist))) // len(gammalist)]
print("(δ,γ)=", delta, gamma)

#Recall remembered sample and fit results
q1r10 = samples[gdindex]
[[lamb, loc, sc], glmax, chisq] = fitresult[gdindex]


#Plotting
matplotlib.style.use('ggplot')

data = pd.Series(q1r10)
#determines left and right limits of fit displayed (adjust numbers for more/less)
x = np.linspace(genlogistic.ppf(0.001, lamb, loc, sc),
                genlogistic.ppf(0.999, lamb, loc, sc), 1000)
y = genlogistic.pdf(x, lamb, loc, sc)
pdf = pd.Series(y, x)

#plot of histogram and fit probability density function
plt.figure(figsize=(8,5), dpi=100)

ax = pdf.plot(lw=2, label="fit λ=" + str("%.3f" % lamb) + 
              " max=" + str("%.2f" % glmax) + 
              " (χ2=" + str("%.0f" % chisq) + ")", legend=True)
data.plot(kind='hist', bins=50, alpha=0.5, 
          label='data δ=' + str("%.2f" % delta) + 
          " γ=" + str("%.2f" % gamma), density=True, legend=True, ax=ax)