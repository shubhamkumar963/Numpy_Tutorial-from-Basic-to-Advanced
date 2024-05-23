#hyperbolic function : sinh(), cosh(), and tanh()

#here we will find the value of sinh of pi/2

import numpy as np 
x= np.sinh(np.pi/2)
print(x)

#values in array
import numpy as np
r= np.array([np.pi/2,np.pi,1.5*np.pi,2*np.pi])
r1= np.cosh(r)
print(r1)

#finding angles -- taking the values of radians and producing corresponding valuessinh , cosh,tanh using arcsinh(), arccosh(),arctanh() function 

import numpy as np 
ang= np.arcsinh(1.0)         #same for cosh and tanh
print(ang)

##values in array 

import numpy as np
m = np.array([0.1,0.2,0.5])
m1=np.arctanh(m)
print(m1)