[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> The mean of the actual distribution is 1.024 and the mean of the biased distribution is 2.403, which is more than double of the actual mean. The plotted figure shows that in the biased distribution there is a higher probability of more children under 18 years.The actual distribution shows a higher probability that there are no children in the family. This is not there in the unbiased distribution. 

Code:
  from __future__ import print_function

  import math
  import numpy as np

  import nsfg
  import first
  import thinkstats2
  import thinkplot
  import chap01soln




  def BiasPmf(pmf, label=''):
      """Returns the Pmf with oversampling proportional to value.


      Args:
        pmf: Pmf object.
        label: string label for the new Pmf.

       Returns:
         Pmf object
      """
      new_pmf = pmf.Copy(label=label)

      for x, p in pmf.Items():
          new_pmf.Mult(x, x)

      new_pmf.Normalize()
      return new_pmf





  def ClassSizes():
      """Generate PMFs of observed and actual class size.
      """
      resp = chap01soln.ReadFemResp()

      # form the pmf
      pmf = thinkstats2.Pmf(resp.numkdhh, label='actual')
      print('mean', pmf.Mean())
      print('var', pmf.Var())

      # Display the pmf
      thinkplot.Pmf(pmf, label = 'numdkdhh')
      thinkplot.show()

      # compute the biased pmf
      biased_pmf = BiasPmf(pmf, label='biased')
      print('Biased mean', biased_pmf.Mean())
      print('Biased var', biased_pmf.Var())

      #Display actual and biased pmf
      thinkplot.PrePlot(2)
      thinkplot.Pmfs([pmf, biased_pmf])
      thinkplot.Show()

  def main(script):
      live, firsts, others = first.MakeFrames()

      ClassSizes()


if __name__ == '__main__':
    import sys
    main(*sys.argv)



