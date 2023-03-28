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

#define kernels        
#x-gradient
kernel_x = [[-1,  0,  1],
            [-2,  0,  2], 
            [-1,  0,  1]]

#y-gradient
kernel_y = [[-1, -2, -1], 
            [ 0,  0,  0], 
            [ 1,  2,  1]]

#define height and width
height=img.shape[0]
width=img.shape[1]

#zero padding
sobel=np.zeros((height+2,width+2))
sobel[1:height+1,1:width+1] = img

sobel_filter = np.zeros(shape=(height, width))

#use convolution for filter
for i in range (0,height):
    for j in range (0,width):
        block = sobel[i:i+3 , j:j+3]  
        convolution_x=np.sum(np.multiply(block,kernel_x))
        convolution_y=np.sum(np.multiply(block,kernel_y))
        sobel_filter[i][j]= np.sqrt(convolution_x**2 + convolution_y**2)

#apply normalization to filtered image
#because after convolution some pixel values are above 255. 
#We have to scale image values between 0-255.
minn = np.amin(sobel_filter)
maxx = np.amax(sobel_filter)
sobel_filter = ((sobel_filter-maxx)/(maxx-minn)*255.0)
#this equation creates floating point values. 
#We have to change image type to 8 bit unsigned integer.
sobel_filter=np.uint8(sobel_filter)
cv2.imshow("Sobel Filtred Image",sobel_filter) 
  
cv2.waitKey(0)
cv2.destroyAllWindows() 
