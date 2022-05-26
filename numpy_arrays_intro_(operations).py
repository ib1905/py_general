# -*- coding: utf-8 -*-
"""
Created on Thu May 26 09:26:17 2022

@author: Иван
"""

import numpy as np

#arithmetic operators on arrays apply elementwise
array1=np.array([20,30,40,50])
array2=np.arange(4)
array3=array1-array2
print(array3)
print(array2**2)
print(array1<35)
#%%
array4=np.array([[1,1],[0,1]])
array5=np.array([[2,0],[3,4]])
print(array4,array5)
array6=array4*array5 #elementwise product
array7=array4@array5 #matrix product
print('elementwise product:',array6)
print('matrix product:',array7)
#%%
rg=np.random.default_rng(1) #instance of default random number generator
array8=np.ones((2,3),dtype=int)
array9=rg.random((2,3))
array8*=3
array9+=array8
#%%
#unary operations often implemented as methods of ndarray class
#rg=np.random.default_rng(1) #instance of default random number generator
array10=rg.random((2,3))
print(array10)
print('sum:',array10.sum(),'\nmin:',array10.min(),'\nmax:',array10.max())
#%%
array11=np.arange(12).reshape(3,4)
print('sum of each column:',array11.sum(axis=0))
print('sum of each row:',array11.sum(axis=1))
