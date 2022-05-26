# -*- coding: utf-8 -*-
"""
Created on Thu May 26 08:50:44 2022

@author: Иван
"""

import numpy as np
import sys

array_1d=np.arange(6) #1d-array
array_2d=np.arange(12).reshape(4,3) #2d-array
#array_2d_m=np.arange(12).reshape(2,6)
array_3d=np.arange(24).reshape(2,3,4) #3d-array

print('1d-array:\n',array_1d,'\n\n2d-array:\n',array_2d,'\n\n3d-array:\n',array_3d)
#%%
print(np.arange(1000)) #attempt to print large array
np.set_printoptions(threshold=sys.maxsize) #force to print entire array
print(np.arange(1000)) #now the entire array was printed
