import numpy as np
a = np.array([1,2,3,4])
a1 =[True,False,True,False]
a2 = a[a1]
print(a2)

#creation of filter array
#will return higher value than 43

import numpy as np
b = np.array([41,42,43,44,45,46,47])
empty =[]      #empty list where values are stored
for i in b:
    if i>43:
        empty.append(True)
    else:
        empty.append(False)
b1 = b[empty]
print(empty)
print(b1)

#create a filter array that will return only even elements from the original array

import numpy as np
c = np.array([11,12,13,14,15,16])
c1 = []        #empty list where values are stored
for i in c:
    if i%2 == 0:
        c1.append(True)
    else:
        c1.append(False)
c2 = c[c1]  #c1 value stored in c2
print(c1)
print(c2)


#creation of filter directly from array --alternate way for filter

import numpy as np
d = np.array([51,52,53,54,55,56,57])
d1= d>54
d2 = d[d1] #d1 value stored in d2
print(d1)
print(d2)
