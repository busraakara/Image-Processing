#Import libraries
import math 
import numpy as np
import cv2 

#Upload image
img = cv2.imread("image.jpg")
cv2.imshow("Original image",img)

#convert image colour bgr to gray scale
b , g , r = img[:,:,0] , img[:,:,1] , img[:,:,2]
img = np.uint8(np.round((b * 0.114 + g * 0.587 + r * 0.299)))
"""
We can use :
cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
this Opencv method use Luminosity method to convert
Luminosity method : b * 0.114 + g * 0.587 + r * 0.299
(but b * 0.0722  + g * 0.7152 + r * 0.2126 also used)
"""
cv2.imshow("Gray Scaled Image",img)

cv2.waitKey(0)
cv2.destroyAllWindows() 