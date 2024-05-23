#ufunc= universal functions that operates on ndarray
#ufunc also takes additional arguments like, where, dtype and out
#vectorization - converting the iterative statements into a vector based statements

#example without ufunc, here we will use python inbuilt function zip()

x=[1,2,3,4]
y=[4,5,6,7]
z=[]
for i,j in zip(x,y):
    z.append(i+j)
print(z)

#with ufunc we wil use add() function

import numpy as np
x=[1,2,3,4]
y=[4,5,6,7]
z= np.add(x,y)
print(z)