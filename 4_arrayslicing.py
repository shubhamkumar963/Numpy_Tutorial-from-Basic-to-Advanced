#slicing_array

import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9])
print(a[:5])

#negative_slicing

import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9])
print(a[-3:-1])

import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9])
print(a[-6:-2])

import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9])
print(a[::2])

#2D array slicing

import numpy as np
b = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(b[1,1:4])
print(b[0,0:4])
print(b[1, -3:-1])