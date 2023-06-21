#import libraries
import numpy as np
import cv2 

#import image
img = cv2.imread("image.jpg")
cv2.imshow("Original image",img)

#convert image colour bgr to gray scale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Scaled Image",img)

#define height and width
height=img.shape[0]
width=img.shape[1]

#zero padding
median = np.zeros((height+2,width+2))
median[1:height+1, 1:width+1] = img
median_filter = np.zeros(shape=(height, width))

#add 3x3 convolution pixels to list and sort
#the value in the middle of list is median value of 3x3 convolution
for i in range (0,height):
    for j in range (0,width):
        listt=[]
        listt.append(median[i][j])
        listt.append(median[i][j+1])
        listt.append(median[i][j+2])
        listt.append(median[i+1][j])
        listt.append(median[i+1][j+1])
        listt.append(median[i+1][j+2])
        listt.append(median[i+2][j])
        listt.append(median[i+2][j+1])
        listt.append(median[i+2][j+2])
        listt.sort()
        median_filter[i][j]=listt[4]
median_filter=np.uint8(median_filter)  
   
cv2.imshow("Median filtered image",median_filter)  

cv2.waitKey(0)
cv2.destroyAllWindows()      