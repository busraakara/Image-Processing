import math 
import numpy as np
import cv2 
import copy

img = cv2.imread("C:/Users/PC/Desktop/subu_vlsi_logo.png")
#cv2.imshow("Original image",img)
print(img.shape)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray image", img) 


ot=cv2.threshold(img,0,255,cv2.THRESH_OTSU)

otsu=ot[1]

cv2.imshow("opencv otsu" , ot[1])

print(img.shape)



kernel = np.ones((3,3), dtype=np.uint8)
opencv_erosion = cv2.erode(otsu, kernel, iterations=1)

cv2.imshow("opencv erezyon",opencv_erosion)


genislik=img.shape[1]
yukseklik=img.shape[0] 

kernel=[[1,1,1],
        [1,1,1],
        [1,1,1]]

erosion_filtre = np.zeros(shape=(genislik, yukseklik))

for i in range (0,yukseklik-2):
    for j in range (0,genislik-2):
        liste=[]
        liste.append(otsu[i][j]*kernel[0][0]) 
        liste.append(otsu[i][j+1]*kernel[0][1])
        liste.append(otsu[i][j+2]*kernel[0][2])
        liste.append(otsu[i+1][j]*kernel[1][0]) 
        liste.append(otsu[i+1][j+1]*kernel[1][1]) 
        liste.append(otsu[i+1][j+2]*kernel[1][2])
        liste.append(otsu[i+2][j]*kernel[2][0])
        liste.append(otsu[i+2][j+1]*kernel[2][1]) 
        liste.append(otsu[i+2][j+2]*kernel[2][2])
        for k in liste:
            if (k == 255):
                a=255
                continue
            elif (k == 0):
                a=0
                break
        erosion_filtre[i+1][j+1]=a
            
erosion_fitre=np.uint8(erosion_filtre)                      
cv2.imshow("erozyon uygulanmis resim",erosion_filtre)  

cv2.waitKey(0)
cv2.destroyAllWindows()   