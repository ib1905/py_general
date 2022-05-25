# -*- coding: utf-8 -*-

import numpy as np
#dimensions are called axes
#indexed by a tuple of non-negative integers

#import matplotlib

array1=[1,2,1] #array of 1 axis with 3 elements
array2=[[1.,0.,0.],[0.,1.,2.]] #array of 2 axes

ndarray1=np.arange(16).reshape(4,4)
print(ndarray1)
print('ndim:',ndarray1.ndim) #number of dimensions (axes) = len(ndarray1.shape)
print('shape:',ndarray1.shape) #size of array in each direction
print('size:',ndarray1.size) #number of elements in array
print('dtype:',ndarray1.dtype) #type of elements in array
print('itemsize:',ndarray1.itemsize) #size in bytes of each element of array

ndarray2=np.array([6,7,8]) #array creation
print(ndarray2)
#%%
ndarray3=np.array([9.,10.,11.])
print(ndarray3)
#%%
ndarray4=np.array([(1,2,3),(4,5,6)])
#%%
ndarray5=np.array([(1,2,3),(4,5,6),(7,8,9)])
#%%
#ways of creating empty arrays
ndarray6=np.zeros((3,5))
ndarray7=np.ones((4,7))
ndarray8=np.empty((2,8),dtype=np.int16) #explicitly defining data type of elements
print(ndarray6,'\n',ndarray7,'\n',ndarray8)
#%%
#creating sequences of numbers
ndarray9=np.arange(0,100,.1)
print(ndarray9)
ndarray10=np.linspace(1,5,35) #better alternative to arange with floating point arguments
print(ndarray10)