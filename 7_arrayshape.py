
# import numpy as np 
# a = np.array([[1,2,3,4],[5,6,7,8]])

# print(a.shape)

#5d array shape using ndmin:

import numpy as np
b = np.array([1,2,3,4], ndmin = 5)
print(b)
print(b.shape)
print('shape of an array is ',b.shape)
