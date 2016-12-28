[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> 34% of the us male population is between the height 5'10" and 6'1".

code:

    import scipy.stats
    u = 178
    sig =7.7
    dist = scipy.stats.norm(loc=u, scale=sig)
    low = dist.cdf(177.8)
    high = dist.cdf(185.4)
    diff = high - low
    print("%age of us male population in the given range is %f", diff*100.0)
