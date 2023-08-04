import numpy as np
import cv2
#***************************************************************************************************************
"""
img = cv2.imread("noise.jpg")
cv2.imshow("original image",img)
#Gaussian Blurring
#this method includes src: source, ksize: kernel size, 
#sigmaX: Gaussian kernel standard deviation in the X direction
#if sigmaY is not given, it takes whatever is in sigmaX
gaussian_filter = cv2.GaussianBlur(img,(9,9),0)
cv2.imshow("Gauss Filtered Image",gaussian_filter)
cv2.waitKey(1)
#***************************************************************************************************************
#Median Blurring
#this blurring method highly effective against salt-and-pepper noise in an image
median_filter = cv2.medianBlur(img,9)
cv2.imshow("Median Filtered Image",median_filter)
cv2.waitKey(1)
#***************************************************************************************************************
#2D Convolution
#we can create our own kernel and filter the image with convolution using filter2D
#filter we apply does not have to be just a blur filter
kernel = (np.array([[1,1,1],
                   [1,1,1],
                   [1,1,1]]))/9
#this method includes src: source, ddepth and kernel
#ddepth is to determine what range of values the image is in
#-1 means the output image will have same depth as input image
convolution = cv2.filter2D(img, -1, kernel)
cv2.imshow("Custom Filter",convolution)
cv2.waitKey(1)
#***************************************************************************************************************
#Bilateral Filter
#Bilteral filter is highly effective in noise removal while keeping edges sharp
#but the operation is slower compared to other filters
bilateral = cv2.bilateralFilter(img,9,75,75)
cv2.imshow("Bilateral Filtered Image",bilateral)
cv2.waitKey(1)
"""