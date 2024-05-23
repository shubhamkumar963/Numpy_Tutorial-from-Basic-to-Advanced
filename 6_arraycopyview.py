#numoy array copy and view

#copy array
import numpy as np
a= np.array([1,2,3,4,5,6,7,8,9])
a1 =a.copy()
print(a)
print(a1)

#view array

import numpy as np
b= np.array([1,2,3,4,5,6,7,8,9])
b1 = b.view()


