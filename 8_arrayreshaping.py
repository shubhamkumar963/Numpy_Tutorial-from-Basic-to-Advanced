
#reshaping from 1d to 2d

import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
a1 = a.reshape(4,3)
print(a1)

#reshaping from 1-d to 3-d

import numpy as np
b = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
b1 = b.reshape(2,3,2)
print(b1)

import numpy as np
b = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
b1 = b.reshape(3,4)
print(b1)

#pass -1
import numpy as np
c = np.array([1,2,3,4,5,6,7,8])
c1 = c.reshape(2,2,-1)
print(c1)

#flattening the aaray

import numpy as np
d = np.array([[1,2,3],[4,5,6]])
d1 = d.reshape(-1)
print(d1)


