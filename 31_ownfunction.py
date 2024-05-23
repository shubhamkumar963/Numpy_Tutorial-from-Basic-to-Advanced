#to create own ufunc we have to define a function like in normal function in python then add it to numpy using frompyfunc() method

#for addition 

import numpy as np
def myadd(x,y):
    return x+y
myadd = np.frompyfunc(myadd,2,1)
print(myadd([1,2,3,4],[4,5,6,7]))

#checking if this function is universal or not

import numpy as np
print(type(np.add))
