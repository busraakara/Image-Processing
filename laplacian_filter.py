import math 
import numpy as np
import cv2 

img = cv2.imread("img.png")
cv2.imshow("Original image",img)
print(img.shape)


img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray image", img) 
print(img.shape)

genislik=img.shape[1]
yukseklik=img.shape[0] 

#Bu 2 kernel da Laplacian Filter için kullanılır
kernel= [[-1, -1, -1], 
        [-1, 8, -1], 
        [-1, -1, -1]]

kernel2= [[0, 1, 0],
          [1, -4, 1],
          [0, 1, 0]]

laplacian_filtre = np.zeros(shape=(yukseklik, genislik))

for i in range (0,yukseklik-2):
    for j in range (0,genislik-2):
        block = img[i:i+3 , j:j+3]
        d = np.sum(np.multiply(block,kernel1))
        if(d<0):
            d=0
        elif(d>255):
            d=255   
        laplacian_filtre[i+1][j+1]=d
              
laplacian_filtre=np.uint8(laplacian_filtre)        
cv2.imshow("laplacian filtrelenmis resim",laplacian_filtre)    


cv2.waitKey(0)
cv2.destroyAllWindows()    

