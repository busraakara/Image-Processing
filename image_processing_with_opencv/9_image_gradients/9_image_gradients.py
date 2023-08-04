import numpy as np
import cv2
from matplotlib import pyplot as plt
#***************************************************************************************************************
"""
#Sobel, Laplacian and Scharr filters are used in edge detection.
#For example, Sobel is a filter in the Canny edge detection algorithm.
#Laplacian is used to find edges in image sharpening.
img = cv2.imread("C:/Users/PC/Desktop/Opencv/lena.jpg",cv2.IMREAD_GRAYSCALE)
#Kernels used for Laplacian:          Kernels used for Sobel:
# |0  1  0|    |1  1  1|             |-1  0  1|       |-1 -2 -1|
# |1 -4  1| or |1 -8  1|             |-2  0  2| = X   | 0  0  0| = Y
# |0  1  0|    |1  1  1|             |-1  0  1|       | 1  2  1|
laplacian = cv2.Laplacian(img,cv2.CV_64F)#When using 64 bit matplotlib will fix this with normalization.
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)#but if we want to see it with opencv it will give wrong result.
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)#you cant try to see it
#When you want to display it with opencv, opencv takes the first 8 bits from the left of a 64 bit number and displays it.
cv2.imshow("sobelx",sobelx)
plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show()
cv2.waitKey(1)
"""