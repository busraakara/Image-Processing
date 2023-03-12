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

sobel_filter_x = np.zeros(shape=(height, width))
sobel_filter_y = np.zeros(shape=(height, width))
sobel_filter = np.zeros(shape=(height, width))

#use convolution for filter
for i in range (0,height-2):
    for j in range (0,width-2):
           
        block = img[i:i+3 , j:j+3]  

        convolution_x=np.sum(np.multiply(block,kernel_x))
        convolution_y=np.sum(np.multiply(block,kernel_y))
        sobel_filter[i+1][j+1]= np.sqrt(convolution_x**2 + convolution_y**2) 
           
        #some numbers may not be between 0-255 so equalization is required.   
        if (sobel_filter[i+1][j+1]<0):
            sobel_filter[i+1][j+1]=0
        elif (sobel_filter[i+1][j+1]>255):
            sobel_filter[i+1][j+1]=255
                      
        #this part is for visualize x and y filters   
        if (convolution_x<0):
            convolution_x=0
        elif (convolution_x>255):
            convolution_x=255
        sobel_filter_x[i+1][j+1]= convolution_x

        if (convolution_y<0):
            convolution_y=0
        elif (convolution_y>255):
            convolution_y=255
        sobel_filter_y[i+1][j+1]= convolution_y
        
sobel_filter_x=np.uint8(sobel_filter_x) 
sobel_filter_y=np.uint8(sobel_filter_y)
sobel_filter=np.uint8(sobel_filter)       
   
cv2.imshow("Sobel x Filtred Image",sobel_filter_x)        
cv2.imshow("Sobel y Filtred Image",sobel_filter_y) 
cv2.imshow("Sobel Filtred Image",sobel_filter) 
  
cv2.waitKey(0)
cv2.destroyAllWindows() 
