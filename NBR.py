# -*- coding: utf-8 -*-

import rasterio
import numpy as np
from matplotlib import pyplot

def NBR(image, bandNIR,bandSWIR): # calculate Normalized Burn Ratio
    NIR = image[bandNIR,:,:]
    SWIR = image[bandSWIR,:,:]
    BurnRatio = (NIR-SWIR)//(NIR+SWIR)
    return BurnRatio

def BurnLevel(pix): # determine burn level
    if pix<=-0.25:
        return 0
    elif pix>-0.25 and pix<=-0.1:
        return 1
    elif pix>-0.1 and pix<=0.1:
        return 2
    elif pix>0.1 and pix<=0.27:
        return 3
    elif pix>0.27 and pix<=0.44:
        return 4
    elif pix>0.44:
        return 5
    else:
        return "Error!"

bandNIR = 5 # for landsat 8 
bandSWIR = 6 # for landsat 8

time1 = rasterio.open("time1.tif").read() # read time1 file

time2 = rasterio.open("time2.tif").read() # read time 2 file

time1NBR = NBR(time1, bandNIR, bandSWIR) # time1 NBR

time2NBR = NBR(time2, bandNIR, bandSWIR) # time2 NBR 

NormalizedBurnRatio = time2NBR - time1NBR

[x,y] = NormalizedBurnRatio.shape

BurnArea = np.zeros([x,y])

for i in range(x):
    for j in range(y):
        BurnArea[i,j] = BurnLevel(NormalizedBurnRatio[i,j])
    
pyplot.imshow(BurnArea)
