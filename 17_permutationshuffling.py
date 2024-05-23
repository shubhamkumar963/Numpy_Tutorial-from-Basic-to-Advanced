#numpy random module provides 2 methods: shuffle() and permutation()
#shuffle method make changes to original array
'''from numpy import random 
import numpy as np
a= np.array([1,2,3,4,5,6])
random.shuffle(a)
print(a)'''

#2nd example---permutation make chages to copy of array not orignal one
from numpy import random 
import numpy as np
b= np.array([1,2,3,4,5,6])
b1= b.copy()
random.permutation(b1)
print(b)
print(random.permutation(b1))

#seaborn is a library

#seaborn uses matplotlib to plot graph using pyplot