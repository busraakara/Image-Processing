#import libraries
import cv2 
import numpy as np

#upload image
img = cv2.imread("img")
cv2.imshow("Original image",img)

#convert image to gray scale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray image", img) 


#apply treshold before erosion 
ret, otsu=cv2.threshold(img,0,255,cv2.THRESH_OTSU)
cv2.imshow("opencv otsu" , otsu)


#for compare module that we write with OpenCV method
kernel = np.ones((3,3), dtype=np.uint8)
opencv_erosion = cv2.erode(otsu, kernel, iterations=1)
cv2.imshow("opencv erosion",opencv_erosion)


#define height and width
height=img.shape[0]
width=img.shape[1]

#define kernel
kernel=[[1,1,1],
        [1,1,1],
        [1,1,1]]

erosion_filter = np.zeros(shape=(height, width))

#zero padding
otsu = np.zeros((height+2,width+2))
otsu[1:height+1 , 1: width+1] = img

#convolution
for i in range (0,height):
    for j in range (0,width):
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
        #if any 0 in list, output value will be 0.
        for k in liste:
            if (k == 255):
                a=255
                continue
            elif (k == 0):
                a=0
                break
        erosion_filter[i][j]=a
            
erosion_fiter=np.uint8(erosion_filter)                      
cv2.imshow("erosion filtered image",erosion_filter)  

cv2.waitKey(0)
cv2.destroyAllWindows()   