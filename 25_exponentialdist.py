#exponential dist: used for describing the time till the next event
#parameter- scale(inverse of rate(lam- poisson distr.))

# draw a sample for exponential dist with 2.0 scale and 2*3 size

from numpy import random
a= random.exponential(scale=2, size=(2,3))
print(a)

#visualization of exponential dist

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.exponential(size=1000), hist=False)
plt.show()