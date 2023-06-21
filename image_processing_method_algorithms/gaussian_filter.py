#import libraries
import numpy as np
import cv2 

#upload image
img = cv2.imread("image.jpg")
cv2.imshow("Original image",img)


img=cv2.blur(img,(3,3))

#convert image colour bgr to gray scale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Scaled Image",img)

#define height and width
height=img.shape[0]
width=img.shape[1] 

#define kernel
kernel = [[1/16, 1/8, 1/16],   
          [1/8, 1/4, 1/8],
          [1/16, 1/8, 1/16]]

#zero padding
gauss=np.zeros((height+2,width+2))
gauss[1:height+1,1:width+1] = img

gaussian_filter = np.zeros(shape=(height, width))

#convolution
for i in range (0,height-2):
    for j in range (0,width-2):
        block = gauss[i:i+3 , j:j+3]  
        convolution=np.sum(np.multiply(block,kernel))
        gaussian_filter[i][j]=convolution
              
gaussian_filter=np.uint8(gaussian_filter)        
cv2.imshow("gaussian filtered image",gaussian_filter)        
       
cv2.waitKey(0)
cv2.destroyAllWindows()    