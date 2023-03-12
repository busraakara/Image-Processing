#import libraries
import numpy as np
import cv2 

#import image
img = cv2.imread("image.jpg")
cv2.imshow("Original Image",img)

#convert image colour bgr to gray scale
"""
We can use :
cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
this Opencv method use Luminosity method to convert
Luminosity method : b * 0.114 + g * 0.587 + r * 0.299
(but b * 0.0722  + g * 0.7152 + r * 0.2126 also used)
"""
b , g , r = img[:,:,0] , img[:,:,1] , img[:,:,2]
img = np.uint8(np.round((b * 0.114 + g * 0.587 + r * 0.299)))
cv2.imshow("Gray Scaled Image",img)

#define height and width
height0 = img.shape[0]
width0 = img.shape[1]

#first implement gaussian filter
gaussian_filter=np.zeros((height0,width0))

zero_padd_img = np.zeros((height0+2,width0+2))
zero_padd_img[1:height0+1 , 1:width0+1] = img

kernel_gauss = np.array([[1/16, 1/8, 1/16],   
                         [ 1/8, 1/4,  1/8],
                         [1/16, 1/8, 1/16]])

height1 = zero_padd_img.shape[0]
width1 = zero_padd_img.shape[1]

for i in range(height1-2):
    for j in range(width1-2):
        block = zero_padd_img[i:i+3 , j:j+3]
        gaussian_filter[i][j] = round(np.sum(np.multiply(block,kernel_gauss)))

#and then implement laplacian filter 
laplacian_filter=np.zeros((height0,width0))
zero_padd_gauss=np.zeros((height0+2,width0+2))
zero_padd_gauss[1:height0+1 , 1:width0+1] = gaussian_filter

kernel_laplacian = np.array([[-1, -1, -1],
                             [-1,  8, -1],
                             [-1, -1, -1]])

height2 = zero_padd_gauss.shape[0]
width2 = zero_padd_gauss.shape[1]

for i in range(height2-2):
    for j in range(width2-2):
        block = zero_padd_gauss[i:i+3 , j:j+3]
        laplacian_filter[i][j] = np.sum(np.multiply(block,kernel_laplacian))
        
# sum image pixels and laplacian pixels        
sharpening_filter=np.zeros((height0,width0))        
for i in range(height0):
    for j in range(width0):
        sharpening_filter[i][j] = img[i][j] + laplacian_filter[i][j]
        if sharpening_filter[i][j] < 0:
            sharpening_filter[i][j] = 0
        elif sharpening_filter[i][j] > 255:
            sharpening_filter[i][j] = 255
sharpening_filter = np.uint8(sharpening_filter)      
      
cv2.imshow("first image",img)
cv2.imshow("sharpened image",sharpening_filter)    

cv2.waitKey(0)
cv2.destroyAllWindows()         
