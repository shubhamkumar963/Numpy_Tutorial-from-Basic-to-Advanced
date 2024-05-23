#random number generation b/w 0-100
from numpy import random
a = random.randint(10)
print(a)

#float number via rand() function

from numpy import random
b = random.rand()
print(b)

#generation of random array
#1-d array containing 5 random int from 0-100
from numpy import random
c = random.randint(100,size=[10])
print(c)

#generation of random array
#2-d array with 3 rows  each row contains 5 random int from 0-100
from numpy import random
d = random.randint(100,size=(3,5))
print(d)

#generation of random array
#1-d array containing 5 random float from 0-100
from numpy import random
e= random.rand(5)
print(e)


#generation of random array
#2-d array with 3 rows containing 5 random float from 0-100
from numpy import random
f= random.rand(3,5)
print(f)

#random number generation from 1d array---using choice() function

from numpy import random 
x = random.choice([5,8,9,3,1,4,52])
print(x) 

#random number generation from 2d array
from numpy import random 
x = random.choice([5,8,9,3,1,4,52], size=(3,3))
print(x)