import numpy as np
import cv2
#***************************************************************************************************************
"""
#Image pyramids are used to enlarge or reduce images by 2 times
#There are two kinds of Image Pyramids. 
#1) Gaussian Pyramid and 2) Laplacian Pyramids
#We can find Gaussian pyramids using cv.pyrDown() and cv.pyrUp() functions.
img = cv2.imread("lena.jpg")
twoxdown=cv2.pyrDown(img)
twoxdown1=cv2.pyrDown(twoxdown)
twoxdown2=cv2.pyrDown(twoxdown1)
twoxdown3=cv2.pyrDown(twoxdown2)
twoxup=cv2.pyrUp(twoxdown3)
twoxup1=cv2.pyrUp(twoxdown2)
twoxup2=cv2.pyrUp(twoxdown1)
twoxup3=cv2.pyrUp(twoxdown)
cv2.imshow("Original Image",img)
cv2.imshow("2XDOWN",twoxdown)
cv2.imshow("2XDOWN1",twoxdown1)
cv2.imshow("2XDOWN2",twoxdown2)
cv2.imshow("2XDOWN3",twoxdown3)
cv2.imshow("2XUP",twoxup)
cv2.imshow("2XUP1",twoxup1)
cv2.imshow("2XUP2",twoxup2)
cv2.imshow("2XUP3",twoxup3)
cv2.waitKey(1)
"""