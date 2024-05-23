# data type in numpy

# i for integer
# bool for boolean
# u for unsigned integer
# f for float
# c for complex float
# m for timedelta
# M for date time
# O for object
# S for string
# U for Unicode string
# V- junk memory allocation

# #checking the data type of numpy array - dtype
import numpy as np
a = np.array([1,2,3,4])
print(a.dtype)

# #checking the data type of numpy array string
import numpy as np
b = np.array(['apple','microsoft','logitech','windows'])
print(b.dtype)

# #checking array with a defined data type:
import numpy as np
z = np.array([1,2,3,4], dtype='S')
print(z)
print(z.dtype)

#converting floating data type to integer in existing array - astype()

# import numpy as np
e = np.array([1.1,2.3,4.5,3.6,6.3])
e1 = e.astype('i')
print(e1)
print(e1.dtype)

#converting integer data type to boolean in existing array - astype()

import numpy as np
h = np.array([1,0,1,3])
h1 = h.astype(bool)
print(h1)
print(h1.dtype)


