# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 13:14:24 2022

This tiny program is intended to calculate the mass of
interstellar gas (H) around the Sun in a sphere volume
with the radius of 4.2 light-years
(up to Proxima Centauri)

@author: Иван
"""

from astropy import units as un #lyr(light-year)
from numpy import pi
from astropy.constants import u,M_sun #u(atomic mass)

#input data
R=4.2*un.lyr #radius of our sphere
R=R.to(un.cm) #unifying units of radius, converting from ly to km
D=.1*un.dimensionless_unscaled/un.cm**3 #average density of gas (hydrogen)
M_atom=u

#%%
'''general formula for calculation of ISM mass: volume of 
a sphere*average density of gas (H)*mass of interstellar H
'''
V=(4/3)*pi*R**3 #volume of a sphere
M_total=V*D*M_atom #total mass of interstellar gas
Sun_like_stars=M_total/M_sun
print('Total mass of H gas in the region:',M_total,'\nRelative to the Sun: {:.1%}'.format(Sun_like_stars))
