import numpy as np
import cv2
from matplotlib import pyplot as plt
#***************************************************************************************************************
"""
#-----Accessing and Modifying pixel values-----#
image = cv2.imread("image.jpg") #load image
pixel1 = image[100,150] #enter height first then width
print(pixel1) #gives 3 channel value of pixel 
pixel2 = image[100,150,0] #enter index and channel number
print(pixel2) #shows the value of the pixel in the given channel number
image[100,150] = [200,100,88] #changes the color of the pixel whose index is entered
print(image[100,150])#see the value that we changed
cv2.waitKey(1)
"""
#***************************************************************************************************************
"""
#-----Accessing Image Properties-----#
image = cv2.imread("image.jpg")
#shows the shape of the picture. shape[0]:height,shape[1]:width,shape[2]:number of channels
print(image.shape)
print(image.size) #shows how many bytes the image consists of. shape[0] x shape[1] x shape[2]
print(image.dtype) #shows data type
#img.dtype is very important in debugging.
cv2.waitKey(1)
"""
#***************************************************************************************************************
"""
#-----Splitting and Merging Image Channels-----#
image=cv2.imread("image.jpg")
b,g,r = cv2.split(image) #split channels to b, g, r variables
image = cv2.merge((b,g,r)) #merge b, g, r in image variable
b = image[:,:,0] #assigns channel 0 of the picture to variable b
#makes the values of the 2nd channel of the picture 0, so all of the red channel become 0
cv2.waitKey(1)
"""
#***************************************************************************************************************
"""
#-----Making Borders for Images (Padding)-----#
image = cv2.imread("image.jpg")
#entered values->top,bottom,left,right
replicate = cv2.copyMakeBorder(image,20,20,20,20,cv2.BORDER_REPLICATE)
cv2.imshow("replicate",replicate) # aaaaaa|abcdefgh|hhhhhhh
reflect = cv2.copyMakeBorder(image,20,20,20,20,cv2.BORDER_REFLECT)
cv2.imshow("reflect",reflect) #  fedcba|abcdefgh|hgfedcb
reflect101 = cv2.copyMakeBorder(image,20,20,20,20,cv2.BORDER_REFLECT_101)
cv2.imshow("reflect101",reflect101) # gfedcb|abcdefgh|gfedcba
wrap = cv2.copyMakeBorder(image,20,20,20,20,cv2.BORDER_WRAP)
cv2.imshow("wrap",wrap) # cdefgh|abcdefgh|abcdefg
blue = [255,0,0] #for frame around picture
#create blue frame
constant= cv2.copyMakeBorder(image,20,20,20,20,cv2.BORDER_CONSTANT,value=blue)
cv2.imshow("constant",constant) 
plt.subplot(231),plt.imshow(image,'gray'),plt.title('original')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('replicate')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('reflect')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('reflect 101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('wrap')
#here the frame of the picture appears red instead of blue. 
#because Matplotlib uses RGB instead of BGR.
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('constant') 
plt.show() 
cv2.waitKey(1)
"""