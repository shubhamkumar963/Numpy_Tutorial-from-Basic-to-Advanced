#paretodist: 80-20 rule
#parameter- a -shape, size

from numpy import random 
x= random.pareto(a=2, size=(2,3))
print(x)


#vizualixation of pareto

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.pareto(a=2, size=1000))
plt.show()