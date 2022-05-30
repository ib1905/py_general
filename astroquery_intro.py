# -*- coding: utf-8 -*-
"""
Created on Mon May 30 10:09:58 2022

@author: Иван
"""

from astroquery.simbad import Simbad

result_table=Simbad.query_region('m81')
print(result_table)

result_object=Simbad.query_object('m81')
print(result_object)
