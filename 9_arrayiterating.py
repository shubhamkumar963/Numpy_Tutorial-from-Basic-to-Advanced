#iterating array means going throught the elements one by one step like loop

#iterate the element of 1-d
import numpy as np 
a = np.array([1,2,3])
for i in a:
    print(i)

#iterate the element of 2-d

import numpy as np
b = np.array([[1,2,3],[4,5,6]])
for i in b:
    print(i)

#iterate on each scalar element of the 2-d

import numpy as np
c = np.array([[1,2,3],[4,5,6]])
for i in c:
    for d in i:
        print(d)

#iterate the element of 1-d
import numpy as np
e = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
for i in e:
    for f in i:
        for  g in f:
            print(g)

#iterating array using nditer (function)

import numpy as np
sk =np.array([[[1,2],[3,4],[5,6],[7,8]]])
for i in np.nditer(sk):
    print(i)

#iterating array using nditer (function) with different sizes
import numpy as np
z = np.array([[1,2,3,8],[4,5,6,9]])
for i in np.nditer(z[:,::2]):
    print(i)
