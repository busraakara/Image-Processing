import numpy as np
import cv2
from matplotlib import pyplot as plt
#***************************************************************************************************************
"""
#Thresholding is basically converting image to binary image. 
#the image should be a grayscale image to convert to binary image.
#-----Simple Thresholding-----#
img = cv2.imread("moon1.jpg",cv2.IMREAD_GRAYSCALE) #read as grayscale
ret,thresh1 = cv2.threshold(img,70,255,cv2.THRESH_BINARY)#pixel>ret=255, others=0
ret,thresh2 = cv2.threshold(img,70,255,cv2.THRESH_BINARY_INV)#pixel>ret=0, others=0
ret,thresh3 = cv2.threshold(img,70,255,cv2.THRESH_TRUNC)#pixel>ret=ret,others=pixel
ret,thresh4 = cv2.threshold(img,70,255,cv2.THRESH_TOZERO)#pixel>ret=pixel,others=0
ret,thresh5 = cv2.threshold(img,70,255,cv2.THRESH_TOZERO_INV)#pixel>ret=0,others=pixel
#-----Adaptive Thresholding-----#
th1 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
#-----Otsu's Binarization-----#
ret,th3 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV',
          'ADAPTIVE_MEAN_C','ADAPTIVE_GAUSSIAN_C','OTSU']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5, th1, th2, th3]
for i in range(9):
    plt.subplot(3,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
"""