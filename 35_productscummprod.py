#products: use prod() function 

import numpy as np
a= np.array([1,2,3,4,5])
anew= np.prod(a)
print(anew)

#product of two different array 

import numpy as np
a= np.array([1,2,3,4,5])
b= np.array([6,7,8,9,10])
anew= np.prod([a,b])
print(anew)

#product over axis if axis =1

import numpy as np
a= np.array([1,2,3,4,5])
b= np.array([6,7,8,9,10])
anew= np.prod([a,b],axis=1)
print(anew)

#cummulative product

import numpy as np
a= np.array([1,2,3,4,5])
#b= np.array([6,7,8,9,10])
anew= np.cumproduct([a])
print(anew)

