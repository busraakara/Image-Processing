import numpy as np
import cv2
from matplotlib import pyplot as plt
#***************************************************************************************************************
"""
#Canny is a very effective opencv method for edge detection
#It is a combination of Gaussian, Sobel and some Tresholds
img = cv2.imread("image.jpg",cv2.IMREAD_GRAYSCALE)
edges = cv2.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
"""