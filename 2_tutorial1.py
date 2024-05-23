import numpy as np
y =np.array((1,2,3,4,5))
print(y)
print(type(y))


#0_d array

x=np.array(42)
print(x)

#2-d array

x= np.array([[1,2,3],[4,5,6]])
print(x)

#3d array with 2d array

x= np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
print(x)

#check how many dimensions the array have: ndim

a = np.array(42)
b = np.array([1,2,3,4,5])
c = np.array([[1,2,3],[4,5,6]])
d = np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#conversion of 1d array to 5d array: ndmin

a =np.array([1,2,3,4,5],ndmin=7)
print(a)
print('number of dimensions ',a.ndim)

