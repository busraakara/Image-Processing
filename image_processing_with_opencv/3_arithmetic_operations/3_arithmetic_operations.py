import numpy as np
import cv2
from matplotlib import pyplot as plt
#***************************************************************************************************************
"""
#-----Understanding np.uint8-----#
#images take 8bit unsigned (positive) values between 0-255.
#if the picture contains values less than 0 or greater than 255, 
#it takes the first 8 bits from the left and displays it as such
#sometimes it is necessary to handle numbers with commas or larger than 8 bits, 
#but eventually the values need to be converted to 8bit.
pixel1 = np.uint8([250])
pixel2 = np.uint8([10])
print(cv2.add(pixel1,pixel2)) #250+10 = 260 => 255
print(pixel1+pixel2) #250+10 = 260 % 256 = 4
"""
#***************************************************************************************************************
"""
#-----Image Blending-----
image1 = cv2.imread("image1.jpg")
image2 = cv2.imread("image2.jpg")  
#two images should be the same size when blending images
#if you dont know how to resize images to be same size check out 5_geometric_transformations
blend = cv2.addWeighted(image1,0.7,image2,0.3,0) #blend = (image1 x 0.7) + (image2 x 0.3)
cv2.imshow("Blended image",blend)
cv2.waitKey(1)
"""
#***************************************************************************************************************
"""
#-----Bitwise Operations-----#
#create white square with black background
square = np.zeros((300,300) , dtype=np.uint8) 
cv2.rectangle(square,(25,25),(275,275),255,-1)
#create white circle with black bacground
circle = np.zeros((300,300),dtype=np.uint8) 
cv2.circle(circle,(150,150),150,255,-1)
#bitwiseAnd = & 
bitwiseAnd = cv2.bitwise_and(square,circle)
cv2.imshow("bitwise-and",bitwiseAnd)
#bitwiseOr = |
bitwiseOr = cv2.bitwise_or(square,circle)
cv2.imshow("bitwise-or",bitwiseOr)
#bitwiseXor = ^
bitwiseXor = cv2.bitwise_xor(square,circle)
cv2.imshow("bitwise-xor",bitwiseXor)
#bitwiseNot = ~
bitwiseNot_square = cv2.bitwise_not(square)
bitwiseNot_circle = cv2.bitwise_not(circle)
cv2.imshow("bitwise-not-square",bitwiseNot_square)
cv2.imshow("bitwise-not-circle",bitwiseNot_circle)
cv2.waitKey(1)
"""
#***************************************************************************************************************
"""
#+++++Image Merge With Bitwise+++++#
#We will use bitwise operators to add moon image to the top left of the kiz kulesi 
img1 = cv2.imread("moon.jpg")
img2 = cv2.imread("kiz_kulesi.jpg")
#define height and width of the img2
height,width,channel = img2.shape
#define top left part of img1
roi = img1[0:height , 0:width]
#create mask for img2 because moon have to be on the foreground
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY) #change img2 to gray channel
#ret->threshold value ,mask->binary image
#if pixel is grater than threshold equals to 255, less than threshold equals to 0
ret, mask = cv2.threshold(img2gray, 50, 255, cv2.THRESH_BINARY) 
#mask-inv for img1 because we have to create background for moon 
mask_inv = cv2.bitwise_not(mask) #bitwise_not-> perform inversion 1->0 , 0->1
img1_bg = cv2.bitwise_and(roi, roi, mask= mask_inv) #create background of kiz kulesi for moon
img2_fg = cv2.bitwise_and(img2, img2, mask = mask) #pull out moon image with black background
dst = cv2.add(img1_bg,img2_fg) #add two image (foreground of moon and background of kiz kulesi)
img1[0:height , 0:width] = dst #place the last image to top left of kiz kulesi
cv2.imshow("last",img1)
cv2.waitKey(1)
"""