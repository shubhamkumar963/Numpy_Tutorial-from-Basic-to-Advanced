#concatenate()---1d

import numpy as np
a = np.array([1,2,3,4])
a1 = np.array([5,6,7,8])
a2 = np.concatenate((a,a1))
print(a2)

# #concatenate()---2d
import numpy as np
b = np.array([[1,2],[3,4]])
b1 = np.array([[5,6],[7,8]])
b2 = np.concatenate((b,b1), axis=1)
print(b2)


#joining array using stack function 

import numpy as np
c = np.array([9,10,11,12])
c1 = np.array([13,14,15,16])
c2 = np.stack((c,c1),axis=1)
print(c2)

#stacking along with rows: hstack()
import numpy as np
d = np.array([17,27,37,47])
d1 = np.array([58,68,78,88])
d2 = np.hstack((d,d1))
print(d2)

#stacking along with coloumn--vstack

import numpy as np
e = np.array([19,29,39,49])
e1 = np.array([59,69,79,89])
e2 = np.vstack((e,e1))
print(e2)

#stacking along with height(depth)- dstack

import numpy as np
f = np.array([10,20,30,40])
f1 = np.array([50,60,70,80])
f2 = np.dstack((f,f1))
print(f2)
