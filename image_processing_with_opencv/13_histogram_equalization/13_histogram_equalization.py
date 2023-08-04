import numpy as np
import cv2
from matplotlib import pyplot as plt
#***************************************************************************************************************
"""
#-----Histogram Equalization-----#
#if we are gonna look at high quality images histogram tables, 
#pixel values appear evenly distributed.
#But on low quality images pixel values appear to be gathered in one place.
#so we have to strech this low quality images histogram tables. 
#And to do it we use the histogram equalization.

#first we load our low quality image grayscale.
image = cv2.imread('unequalized.jpg', cv2.IMREAD_GRAYSCALE)
#i just resize image here because it was to big.
img = cv2.resize(image,(900,500))
#get histgram table of unequalized image and show
plt.hist(img.ravel(),256,[0,256]); plt.show()
#equalize image
equ = cv2.equalizeHist(img)
#get histogram table of equalized image and show
plt.hist(equ.ravel(),256,[0,256]); plt.show()
#stack both image to see difference
res = np.hstack((img, equ))
cv2.imshow("original-equalized",res)
"""


cv2.waitKey(1)