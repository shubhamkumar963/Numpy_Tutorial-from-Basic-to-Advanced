#searching array- search an array for a certain value and return the index that get the match by using where()

import numpy as np
a = np.array([1,2,3,4,5,6,4,4,9])
anew = np.where(a==4)
print(anew)

# #finding the index of even numbers

import numpy as np
b = np.array([11,12,13,14,15,16,17,18,19,20,2,1,22,24,26,25,27])
bnew = np.where(b%2==0)
print(bnew)

# #finding the index of odd numbers


import numpy as np
c = np.array([11,12,13,14,15,16,17,18,19,20,2,1,22,24,26,25,27])
cnew = np.where(b%2==1)
print(cnew)

#searchsorted()- perform binary search in array - return index value
#finding the index value where the value 7 is inserted
import numpy as np 
d= np.array([5,6,7,8,8,7,9,7])
dnew=np.searchsorted(d,7)
print(dnew)

#finding the index value from right side
import numpy as np 
e= np.array([5,6,7,8,8,7,9,7])
enew=np.searchsorted(e,7,side='right')
print(enew)

#how to search multiple values
import numpy as np 
f= np.array([1,3,5,7,9])
fnew=np.searchsorted(f,[2,4,6,8])
print(fnew)