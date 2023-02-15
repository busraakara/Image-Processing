import numpy as np
import cv2 

img = cv2.imread("image.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#bgr to gray: Y= 0.299*R + 0.587*G + 0.114*B

#x-gradient
kernel_x = [[-1,  0,  1],
           [-2,  0,  2], 
           [-1,  0,  1]]

#y-gradient
kernel_y = [[-1, -2, -1], 
           [ 0,  0,  0], 
           [ 1,  2,  1]]


height=img.shape[0] 
width=img.shape[1]


sobel_filter_x = np.zeros(shape=(height, width))
sobel_filter_y = np.zeros(shape=(height, width))
sobel_filter = np.zeros(shape=(height, width))


for i in range (0,height-2):
    for j in range (0,width-2):
        block = img[i:i+3 , j:j+3]   
        convolution_x=np.sum(np.multiply(block,kernel_x))
        convolution_y=np.sum(np.multiply(block,kernel_y))
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
       
        sobel_filter[i+1][j+1]= np.sqrt(convolution_x**2 + convolution_y**2) 
        if (sobel_filter[i+1][j+1]<0):
            sobel_filter[i+1][j+1]=0
        elif (sobel_filter[i+1][j+1]>255):
            sobel_filter[i+1][j+1]=255
        
        
sobel_filter_x=np.uint8(sobel_filter_x) 
sobel_filter_y=np.uint8(sobel_filter_y)
sobel_filter=np.uint8(sobel_filter)       
   

#With the bitwise_or command, the same thing is done as taking the hypotenuse.
sobel_bitwise_or=cv2.bitwise_or(sobel_filter_x,sobel_filter_y)
 
cv2.imshow("sobel_x filtred image",sobel_filter_x)        
cv2.imshow("sobel_y filtred image",sobel_filter_y) 
cv2.imshow("sobel filtred image",sobel_filter) 
cv2.imshow("sobel_bitwise_or",sobel_bitwise_or)

      
    
cv2.waitKey(0)
cv2.destroyAllWindows()         
