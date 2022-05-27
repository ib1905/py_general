# -*- coding: utf-8 -*-
"""
Created on Thu May 26 14:36:54 2022

@author: Иван
"""

import numpy as np

#universal functions (common mathematical ones) are applied elementwise producing new array

array1=np.arange(3)
array2=np.exp(array1)
array3=np.sqrt(array2)
array4=np.arange(3)+array1
print(array1,array2,array3,array4)