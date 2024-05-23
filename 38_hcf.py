import numpy as np 
a= 45
b= 15
c= np.gcd(a,b)
print(c)


#finding gcd in an array

import numpy as np
x= np.array([14,42,36])
y=np.gcd.reduce(x)   #reduce() function will use the ufunc to reduce the array by 1 dimension 
print(y)
