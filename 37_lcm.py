#lcm()- function 

import numpy as np 
a=5
b=6
c=np.lcm(a,b)
print(c)

#finding lcm in array 

import numpy as np
x= np.array([4,5,6])
y=np.lcm.reduce(x)   #reduce() function will use the ufunc to reduce the array by 1 dimension 
print(y)

#lcm of all elements of an array contains all integers from 1 to 10

import numpy as np 
a= np.arange(1,12)
a1=np.lcm.reduce(a)
print(a1)


