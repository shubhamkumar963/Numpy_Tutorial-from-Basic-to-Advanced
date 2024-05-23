#remainder -mod() and remainder() function 
import numpy as np
x= np.array([81,38,38,69])
y= np.array([9,6,8,9])
z= np.mod(x,y)
print(z)

#add()
import numpy as np
a= np.array([1,2,3,4,5])
b= np.array([5,6,7,8,9])
c= np.add(a,b)
print(c)

#subtract()
import numpy as np
s= np.array([5,6,7,8,9])
s1= np.array([1,2,3,4,5])
s2= np.subtract(s,s1)
print(s2)

#multiply()

import numpy as np
m= np.array([5,6,7,8,9])
m1= np.array([1,2,3,4,5])
m2= np.multiply(m,m1)
print(m2)

#divide()
import numpy as np
d= np.array([5,6,9,8,10])
d1= np.array([1,2,3,4,5])
d2= np.divide(d,d1)
print(d2)

#power()
import numpy as np
p= np.array([5,6,7,8,9])
p1= np.array([1,2,3,4,5])
p2= np.power(p,p1)
print(p2)

#quotient and mod[remainder]---together- using divmod() function

import numpy as np
q= np.array([5,6,7,8,9])
q1= np.array([1,2,3,4,5])
q2= np.divmod(q,q1)
print(q2)

#absolute value- negative to positive and vise versa using abs() or absolute() function 

import numpy as np
ab= np.array([-5,-6,-7,-8,-9])
ab1= np.abs(ab)
print(ab1)


