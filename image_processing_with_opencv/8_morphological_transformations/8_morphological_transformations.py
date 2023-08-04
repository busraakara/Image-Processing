import numpy as np
import cv2
from matplotlib import pyplot as plt
#***************************************************************************************************************
"""
kernel1= np.ones((5,5),np.uint8) #used as 2D convolution kernel
#Always try to keep foreground in white
img = cv2.imread("morphology1.png")
#Erosion
#the basic idea of erosion is it erodes away the boundaries of foreground object
#kernel slides through the image (as in 2D convolution). 
##if all the pixels under the kernel are 1,
##the output will be 1, otherwise it will be 0 and it will erode
erosion = cv2.erode(img,kernel1,iterations = 1) 
#Dilation
#it is opposite of erosion.
#if all pixel under the kernel is 0,
#the output will be 0, otherwise it will be 1 and it will dilate
dilation = cv2.dilate(img,kernel1,iterations = 1)
plt.figure(1)
plt.subplot(131),plt.imshow(img,'gray'),plt.title("Original Image")
plt.subplot(132),plt.imshow(erosion,'gray'),plt.title("erosion")
plt.subplot(133),plt.imshow(dilation,'gray'),plt.title("dilation")
plt.show()

#Opening
#Opening is just another name of erosion followed by dilation.
img2 = cv2.imread("morphology2.png")
opening = cv2.morphologyEx(img2, cv2.MORPH_OPEN, kernel1)
plt.figure(2)
plt.subplot(121),plt.imshow(img2,'gray'),plt.title("Original Image")
plt.subplot(122),plt.imshow(opening,'gray'),plt.title("opening")
plt.show()

#Closing
#Closing is reverse of Opening, dilation followed by erosion.
img3 = cv2.imread("morphology3.png")
closing = cv2.morphologyEx(img3, cv2.MORPH_CLOSE, kernel1)
plt.figure(3)
plt.subplot(121),plt.imshow(img3,'gray'),plt.title("Original Image")
plt.subplot(122),plt.imshow(closing,'gray'),plt.title("closing")
plt.show()

kernel2 = np.ones((9,9),np.uint8)

#Morphological Gradient
#It is the difference between dilation and erosion of an image.
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel1)
#Top Hat
#It is the difference between input image and Opening of the image.
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel2)
#Black Hat
#It is the difference between the closing of the input image and input image.
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel2)
plt.figure(4)
plt.subplot(221),plt.imshow(img,'gray'),plt.title("Original Image")
plt.subplot(222),plt.imshow(gradient,'gray'),plt.title("gradient")
plt.subplot(223),plt.imshow(tophat,'gray'),plt.title("tophat")
plt.subplot(224),plt.imshow(blackhat,'gray'),plt.title("blackhat")
plt.show()
"""