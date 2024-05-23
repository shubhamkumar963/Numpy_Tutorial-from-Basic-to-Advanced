#generation 1-d array with 100 values where each value has to be 3,5,7,9

#probability of 3 is set to 0.1
#probability of 5 is set to 0.3
#probability of 7 is set to 0.6
#probability of 9 is set to 0.0
#sum of all probability set to 1.0

from numpy import random
a= random.choice([3,5,7,9], p =[0.1,0.3,0.4,0.2], size=(100)) #---probability - p
print(a)


#generation 2-d array with 3 rows each contains 5 values
from numpy import random
b= random.choice([13,15,17,19], p =[0.1,0.2,0.4,0.3], size=(3,5)) #---probability - p
print(b)