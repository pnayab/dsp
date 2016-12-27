[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> The CDF of percentile ranks for 1000 random numbers is a straight line which means its a normal distribution. The PMF is not useful here as the number of values is large. 

Code:

     import random
     import thinkstats2
     import thinkplot

     r = [random.random() for _ in range(1000)]
     pmf = thinkstats2.Pmf(r)
     thinkplot.Pmf(pmf)
     thinkplot.show()

     cdf = thinkstats2.Cdf(r)
     thinkplot.Cdf(cdf)
     thinkplot.show()
