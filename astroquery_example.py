# -*- coding: utf-8 -*-
"""
Created on Mon May 30 11:29:48 2022

@author: Иван
"""

from astropy import units as u
from astropy.coordinates import SkyCoord
from astropy.wcs import WCS
from astroquery.skyview import SkyView
from astroquery.vizier import Vizier
import matplotlib.pyplot as plt

center=SkyCoord.from_name('Orion KL')
imglist=SkyView.get_images(position=center,survey='2MASS-J')
img=imglist[0]
mywcs=WCS(img[0].header)
fig=plt.figure(1)
fig.clf()
ax=fig.add_axes([0.15,0.1,0.8,0.8],projection=mywcs)
ax.set_xlabel('RA')
ax.set_ylabel('Dec')
ax.imshow(img[0].data,cmap='gray_r',interpolation='none',origin='lower',norm=plt.matplotlib.colors.LogNorm())

tablelist=Vizier.query_region(center,radius=5*u.arcmin,catalog='J/ApJ/826/16/table1')
result=tablelist[0]
tbl_crds=SkyCoord(result['RAJ2000'],result['DEJ2000'],unit=(u.hour,u.deg),frame='fk5')

tablelist2=Vizier(row_limit=10000).query_region(center,radius=5*u.arcmin,catalog='J/ApJ/540/236')
result2=tablelist2[0]
tbl_crds2=SkyCoord(result2['RAJ2000'],result2['DEJ2000'],unit=(u.hour,u.deg),frame='fk5')

ax.plot(tbl_crds.ra,tbl_crds.dec,'*',transform=ax.get_transform('fk5'),mec='b',mfc='none')
ax.axis([100,200,100,200])
plt.show()
