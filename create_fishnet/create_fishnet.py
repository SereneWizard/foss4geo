# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 10:27:51 2017

@author: vdahal2
"""

import shapefile as shp
import numpy as np
import math



minx,maxx,miny,maxy = 448262.080078, 450360.750122, 6262492.020081, 6262938.950073
dx = 100
dy = 100

nx = int(math.ceil(abs(maxx - minx)/dx))
ny = int(math.ceil(abs(maxy - miny)/dy))

w = shp.Writer(shp.POLYGON)
w.autoBalance = 1
w.field("ID")
id=0

for i in range(ny):
    for j in range(nx):
        id+=1
        vertices = []
        parts = []
        vertices.append([min(minx+dx*j,maxx),max(maxy-dy*i,miny)])
        vertices.append([min(minx+dx*(j+1),maxx),max(maxy-dy*i,miny)])
        vertices.append([min(minx+dx*(j+1),maxx),max(maxy-dy*(i+1),miny)])
        vertices.append([min(minx+dx*j,maxx),max(maxy-dy*(i+1),miny)])
        parts.append(vertices)
        w.poly(parts)
        w.record(id)

w.save('polygon_grid')

"""

minx,maxx,miny,maxy = 448262.080078, 450360.750122, 6262492.020081, 6262938.950073
dx = 100
dy = 100


nx = int(math.ceil(abs(maxx - minx)/dx)) + 1
ny = int(math.ceil(abs(maxy - miny)/dy)) + 1
        """