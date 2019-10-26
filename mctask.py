#Sergey Kurennoy
"""
Generates samples of 1% percentile overlapping 10-day proportional returns 
based on a stable distribution for log-price difference. Fits the sample to 
a generalized logistic distribution, and remembers the results.
Plots are produced in mcplot.py, which recalls remembered data.
"""
import numpy as np
import scipy.stats as st
from scipy.stats import levy_stable, genlogistic

#given length of time series
N = 750

#initialize arrays of returns: only N-9 overlapping 10-day returns
r1 = np.zeros(N)
r10 = np.zeros(N-9)

def generate_series(N, return1, return10, alpha, beta, delta, gamma):
    #generate random variables sequentially according to Levy alpha-stable distribution
    randomvariable = np.zeros(N)
    for i in range(N):
        randomvariable[i] = levy_stable.rvs(alpha, beta, delta, gamma, random_state=None)
    
    ##initialize prices
    price = np.zeros(N+1)
    price[0] = 100.0 #arbitrary initial price
        
    ##Standard practice, as prescribed by Mandelbrot (1963)
    ##presumes that the daily change in natural logarithms
    ##of prices is represented by said random variable:
    ##  X = log_e[P_(i+1)] - log_e[P_i] , or equivalently
    ##  P_(i+1) = P_i * exp(X)
    exprv = np.exp(randomvariable)
    for i in range(N):
        price[i+1] = price[i] * exprv[i]
    
    #Use the equations given for fractional daily returns:
    #  r^1_i = ( P_(i+1) - P_i ) / P_i
    #  r^10_i = ( P_(i+10) - P_i ) / P_i
    for i in range(N):
        return1[i] = (price[i+1] / price[i]) - 1
        #shortcut return1[i] = exprv[i] - 1
        if (i < N - 9):
            return10[i] = (price[i+10] / price[i]) - 1 


def drawplots(arrays):
    #Used for looking at time series
    fig = plt.figure(figsize=(10,8), dpi=100)
    
    nplots = len(arrays)
    for k in range(len(arrays)):
        plt.subplot(nplots,1,k+1)
        plt.plot(arrays[k])


#Given parameters of Levy alpha-stable distribution,
#where delta=location parameter comes before gamma=scale parameter
#to coincide with the order in the scipy.ststs.levy_stable specification:
#  rvs(alpha, beta, loc=0, scale=1, size=1, random_state=None)
alpha, beta, delta, gamma = 1.7, 0.0, 0.01, 0.02
#(delta and gamma to be varied)
#deltalist = [-0.02, 0.0, 0.02, 0.04, 0.06]
#gammalist = [0.01, 0.03, 0.05]

#number of independent time series in each sample
points = 1200

#collection of samples and fit parameters for different delta&gamma cases:
samples = []
fitresult = []

for delta in deltalist:
    for gamma in gammalist:
        print("Timeseries via params (α,β,δ,γ)=", alpha, beta, delta, gamma)
        q1r10 = np.zeros(points)
        
        #Collect each sample from generated independent time series
        for j in range(points):
            if (j % 200 == 0): print(j*100.0/points,"% done")
            generate_series(N, r1, r10, alpha, beta, delta, gamma)
            q1r10[j] = np.quantile(r10, 0.01)
        #remember sample
        samples.append(q1r10)
        
        #Fit the sample to generalized logistic distribution, 
        #with shape parameter lamb, as well as location and shape parameters
        [lamb, loc, sc] = genlogistic.fit(q1r10)
        #compute the location of the mode: maximum of probability density function
        glmax = loc + sc * np.log(lamb)
        print("Gen.logistic fit parameters:", lamb, loc, sc, " with max=",glmax)
        
        #Calculate chi-square test statistic:
        k = 33 #number of bins in histogram
        #use numpy histogram for the expected value
        observed, hist_binedges = np.histogram(q1r10, bins=k)
        #use the cumulative density function (c.d.f.)
        #of the distribution for the expected value
        cdf = genlogistic.cdf(hist_binedges, lamb, loc, sc)
        expected = len(q1r10) * np.diff(cdf)
        #use scipy.stats chisquare function, where 
        #ddof is the adjustment to the k-1 degrees of freedom, 
        #which is the number of distribution parameters
        chisq, pval = st.chisquare(observed, expected, ddof=3)
        print("Chi-square = ", chisq)
        #remember fit results
        fitresult.append([[lamb, loc, sc], glmax, chisq])


