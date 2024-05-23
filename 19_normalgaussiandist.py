#random.normal() method- loc(mean),scale(std.deviation),size

#generating a random normal distribution with 2 rows having 3 values each

from numpy import random 
a = random.normal(size=(2,3))
print(a)

#generating a random normal distribution with 2 rows having 3 values each with mean 1 and standard deviation of 2

from numpy import random 
b= random.normal(loc= 1,scale= 2, size=(2,3))
print(b)

#visualization of normal distribution 
from numpy import random 
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.normal(size=1000),hist=False)
plt.show()

