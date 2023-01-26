import math 
import numpy as np
import cv2 

img = cv2.imread("image.jpg")

cv2.imshow("Original image",img)

print(img.shape)

img=cv2.blur(img,(3,3))

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray image", img) 

print(img.shape)

genislik=img.shape[1]
yukseklik=img.shape[0] 

kernel = [[1/16, 1/8, 1/16],   
          [1/8, 1/4, 1/8],
          [1/16, 1/8, 1/16]]

gaussian_filtre = np.zeros(shape=(yukseklik, genislik))

for i in range (0,yukseklik-2):
    for j in range (0,genislik-2):
        a = img[i][j]*kernel[0][0] + img[i][j+1]*kernel[0][1] + img[i][j+2]*kernel[0][2]
        b=img[i+1][j]*kernel[1][0] + img[i+1][j+1]*kernel[1][1] + img[i+1][j+2]*kernel[1][2]
        c=img[i+2][j]*kernel[2][0] + img[i+2][j+1]*kernel[2][1] + img[i+2][j+2]*kernel[2][2]
        d=a+b+c
        gaussian_filtre[i+1][j+1]=round(d)
              
gaussian_filtre=np.uint8(gaussian_filtre)        
cv2.imshow("gaussian filtrelenmis resim",gaussian_filtre)        
       
cv2.waitKey(0)
cv2.destroyAllWindows()    
        
