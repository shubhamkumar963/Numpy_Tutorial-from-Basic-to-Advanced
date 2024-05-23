#array_split()
#split the array in 3 parts

import numpy as np
a = np.array([1,2,3,4,5,6])
anew = np.array_split(a,6)
print(anew)

# # split array in copy function 

sk = a.copy()
sknew = np.array_split(sk,2)
print(sknew)

# split into array with index

import numpy as np 
b = np.array([1,2,3,4,5,6])
bnew = np.array_split(b,3)
print(bnew[0])
print(bnew[1])
print(bnew[2])

#splitting 2d array 

import numpy as np 
c = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[17,18,19]])
cnew = np.array_split(c,3)
print(cnew)

# splitting the 2d into three 2d along with rows
import numpy as np 
d = np.array([[10,20,30],[40,50,60],[70,80,90],[100,110,120],[130,140,150],[170,180,190]])
dnew = np.array_split(d,3, axis=1)
print(dnew)

# using hsplit

import numpy as np 
e = np.array([[11,21,31],[41,51,61],[71,81,91],[101,111,121],[131,141,151],[171,181,191]])
enew = np.hsplit(e,3)
print(enew)