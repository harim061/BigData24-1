# -*- coding: utf-8 -*-
"""
Created on Sat May 18 21:54:24 2024

@author: doris
"""

import numpy as np

ar1 =np.array([1, 2,3,4,5])
ar1
type(ar1)

ar2 =np.array([[10,20,30],[40,50,60]])
ar2

ar3= np.arange(1,11,2)

ar4 = np.array([1,2,3,4,5,6]).reshape(3,2)
ar4

ar5=np.zeros((2,3))
ar5

ar6= ar2[0:2,0:2]
ar6

ar7 = ar2[0,:]
ar7

ar8 = ar1 +10
ar8

ar8 -ar1

ar1 * 2

ar1 /2

ar9 = np.dot(ar2,ar4)
ar9



myarray = [1,2,3]

print(type(myarray))

mynumpy = np.array([1,2,3])
print(type(mynumpy))

print(myarray[0],myarray[1], myarray[2])
print(mynumpy.shape)
print(mynumpy[0],mynumpy[1],mynumpy[2])

myarray[0] = 5
print(myarray)

mynumpy[0] = 5
print(mynumpy)

print(sum(myarray))
print(np.sum(mynumpy))

print(myarray.sort())

print(np.sort(mynumpy))

print(myarray*2)
print(mynumpy*2)


yourarray = [[1,2,3],[4,5,6]]
print(yourarray[0])

ynumpy = np.array([[1,2,3],[4,5,6]])
print(ynumpy.shape)

x = [[1,2],[3,4]]
y = [[5,6],[7,8]]
print(x+y)

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

print(x+y)
print(np.add(x,y))


