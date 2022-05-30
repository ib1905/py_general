# -*- coding: utf-8 -*-
"""
Created on Mon May 30 08:56:28 2022

@author: Иван
"""

import numpy as np

def func(x,y): #arguments sent are: (0,0),(0,1),(0,2)..(1,0),(2,0),(3,0),etc.
    return 10*x+y

array_func=np.fromfunction(func,(5,4),dtype=int)

print(array_func)
print(array_func[2,3])
print(array_func[:,1]) #each row in 2nd column
print(array_func[0,:]) #each column in 1st row
print(array_func[-1]) #last row

#%%
array_3d=np.array([[[0,1,2],[10,12,13]],[[100,101,102],[110,112,113]]]) #3d array (2 stacked 2d arrays)

#print(array_3d)
print(array_3d[1])
print(array_3d[-1])
print(array_3d[...,0])
print(array_3d[...,1])
print(array_3d[...,-1])
#%%
for row in array_3d:
    print(row)

for element in array_3d.flat:
    print(element)