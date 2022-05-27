# -*- coding: utf-8 -*-
"""
Created on Fri May 27 09:20:08 2022

@author: Иван
"""

import numpy as np

array1=np.arange(10)**3
print(array1)
print(array1[2])
print(array1[2:5])
array1[:6:2]=1000 #set every second element from beginning to position 6 exclusive to value
print(array1)
array1=array1[::-1] #reverse array
print(array1)

for element in array1:
    print(np.sqrt(element))
