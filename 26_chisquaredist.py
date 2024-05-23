#chi square dist- used as a basis to verify the hypothesis
#parameter- df(degree of freedom), size

#chi square dist with df=2 size=2*3

from numpy import random 
a= random.chisquare(df=2,size=(2,3))
print(a)

#vizualisation of chisquare

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.chisquare(df= 1,size=1000), hist=False)
plt.show()