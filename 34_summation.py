#sum the values in 2 array---all values will be added vertically and will return single value

import numpy as np
a= np.array([7,8,9,5])
b=np.array([4,3,5,6])
c= np.sum([a,b])
print(c)


#summation over axis- means numpy will add each value in array and return value in single array
import numpy as np
a= np.array([7,8,9,5])
b=np.array([4,3,5,6])
c= np.sum([a,b],axis=1)
print(c)

#cummulative sum 
import numpy as np
a= np.array([7,8,9,5])
c= np.cumsum(a)
print(c)