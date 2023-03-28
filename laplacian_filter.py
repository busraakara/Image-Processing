#Import libraries
import math 
import numpy as np
import cv2 

#Upload image
img = cv2.imread("image.jpg")
cv2.imshow("Original image",img)

#Convert BGR colorful image to gray scale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray image", img) 

genislik=img.shape[1]
yukseklik=img.shape[0] 

#These 2 kernels used for Laplacian filter
kernel1= [[-1, -1, -1], 
        [-1, 8, -1], 
        [-1, -1, -1]]

kernel2= [[0, 1, 0],
          [1, -4, 1],
          [0, 1, 0]]

laplacian_filtre = np.zeros(shape=(yukseklik, genislik))

#Zero padding
laplacian = np.zeros((yukseklik+2,genislik+2))
laplacian[1:yukseklik+1 , 1:genislik+1] = img

#Convolution
for i in range (0,yukseklik):
    for j in range (0,genislik):
        block = laplacian[i:i+3 , j:j+3]
        d = np.sum(np.multiply(block,kernel1))
        laplacian_filtre[i][j]=d
        
#Normalization
minn = np.amin(laplacian_filtre)
maxx = np.amax(laplacian_filtre)
laplacian_filtre = ((laplacian_filtre-maxx)/(maxx-minn)*255.0)              
laplacian_filtre=np.uint8(laplacian_filtre)        
cv2.imshow("laplacian filtred image",laplacian_filtre)    

cv2.waitKey(0)
cv2.destroyAllWindows()    
