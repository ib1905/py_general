# -*- coding: utf-8 -*-
"""
Created on Tue May 31 09:58:54 2022

@author: Иван
"""

import numpy as np
rg=np.random.default_rng(1) #instance of default random number generator

array1=np.floor(10*rg.random((2,2)))
array2=np.floor(10*rg.random((2,2)))
print(array1,array2)

array3=np.vstack((array1,array2)) #vertical stacking
array4=np.hstack((array1,array2)) #horizontal stacking
print('\n',array3,'\n',array4)
