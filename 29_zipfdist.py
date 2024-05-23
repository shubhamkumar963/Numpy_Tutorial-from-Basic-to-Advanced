#zipf Dist:- 
from numpy import random 
x= random.zipf(a=2, size=(2,3))
print(x)


#vizualization of zipf dist
from numpy import random 
import matplotlib.pyplot as plt
import seaborn as sns
x= random.zipf(a=2,size=500)
sns.distplot(x[x<5], kde=False)
plt.show()
