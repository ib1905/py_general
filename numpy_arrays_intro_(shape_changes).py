# -*- coding: utf-8 -*-
"""
Created on Mon May 30 15:46:45 2022

@author: Иван
"""

import numpy as np
rg=np.random.default_rng(1) #instance of default random number generator

array1=np.floor(10*rg.random((3,4)))
print(array1)
print(array1.shape)

#%%
array1_flattened=array1.ravel()
print(array1_flattened)
array1_reshaped=array1.reshape(6,2)
print(array1_reshaped)
array1_transposed=array1.T
print(array1_transposed)
#%%
array1_resized=array1.resize(2,6) #modifies original array
print(array1_resized,'\n',array1)
#%%
array1=array1.reshape(3,-1) #with -1 the other dimensions are calculated automitcally
print(array1)
