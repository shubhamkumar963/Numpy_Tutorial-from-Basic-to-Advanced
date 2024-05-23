import numpy as np 
a = np.sin(np.pi/2)
print(a)

#sin values in array 
import numpy as np 
x = np.array([np.pi/2,np.pi/3,np.pi/4,np.pi/5])
y=np.sin(x)
print(y)

#convert degree in radians pi/180[deg2rad() func]

import numpy as np
s= np.array([90,180,270,360])
s1= np.deg2rad(s)
print(s1)

#radians to degrees

import numpy as np
r= np.array([np.pi/2,np.pi,1.5*np.pi,2*np.pi])
r1= np.rad2deg(r)
print(r1)

#arcsin(),arccos(),arctan()-- functions to find the values of trignometric angles

import numpy as np 
ang= np.arcsin(1.0)
print(ang)

import numpy as np
m = np.array([1,-1,0.1])
m1=np.arcsin(m)
print(m1)

#hypot()- function - pythagorous theorem 
import numpy as np 
base=3
perpendicular = 4
hypo = np.hypot(base,perpendicular)
print(hypo)


