#logistic distribution - use in regression and neural network
#loc(mean=0), scale (standard deviation =1), size
#drae 2*2 samples of logistics with mean at 1 and stdev 2

from numpy import random 
a= random.logistic(loc=1, scale=2, size=(2,3))
print(a)

#vizualization of logistics dist.

from numpy import random 
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.uniform(size=100),hist= False)
plt.show()