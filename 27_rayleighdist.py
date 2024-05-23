 #rayleigh dist- used for signal processing
#parameters- scale()- standard deviation[default 1.0], size


#scale of 2.0 with size of 2*3
from numpy import random 
a= random.rayleigh(scale=2,size=(2,3))
print(a)

#vizualisation of rayleigh

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.rayleigh(size=1000), hist=False)
plt.show()