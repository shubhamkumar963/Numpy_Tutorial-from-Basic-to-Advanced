#binomial dist - discrete dist- binary output
#n = no. of trials, p= probability

#given 10 trials for a coin which will generate 10 data points:

from numpy import random 
a = random.binomial(n=10,p=0.5,size=10)
print(a)

#visualization of binomial dist

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True)
plt.show()

#difference between binomial distribution(discrete) and normal distribution(continue)

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.normal(loc=50,scale=5,size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')
plt.show()
