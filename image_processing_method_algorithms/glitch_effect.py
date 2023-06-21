#import libraries
import cv2 
import numpy as np
#upload image
img = cv2.imread("image.jpg")
cv2.imshow("Original image",img)

#define height and width
height , width = img.shape[:2]

#leave blue channel the same.
img[0:height,0:width,0] = img[0:height,0:width,0]

#Shift green channel 7 pixels to the right.
img[0:height-7, 0:width-7,1]=img[7:height,7:width,1]

#Shift red channel 15 pixels to the right.
img[0:height-15, 0:width-15,2]=img[15:height,15:width,2]

cv2.imshow("glitch image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()