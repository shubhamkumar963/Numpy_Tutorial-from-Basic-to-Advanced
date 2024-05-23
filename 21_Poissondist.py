#poisson dist- it estimates how many times an event can happen 
#lam- number of occurence events,size
#generate a random 1*10 dist for occurence 

from numpy import random
a = random.poisson(lam=2,size=10)
print(a)

#visualization of poission distribution

from numpy import random 
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.poisson(lam=2,size=1000),kde=False)
plt.show()

#presenting both normal and poisson distribution in same figure

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.normal(loc=50, scale= 7,size=1000),hist=False, label='Normal')
sns.distplot(random.poisson(lam=50,size=1000),hist=False,label='Poisson')
plt.show()
             