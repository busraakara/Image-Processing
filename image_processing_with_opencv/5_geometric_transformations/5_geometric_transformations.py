import numpy as np
import cv2
#***************************************************************************************************************
"""
#-----Scaling(resizing)-----#
image = cv2.imread("image.jpg")
cv2.imshow("original",image)
#shrinking
resize1 = cv2.resize(image,None,fx=0.5,fy=0.5,interpolation = cv2.INTER_AREA) 
cv2.imshow("resize1",resize1)
#OR
height,width = image.shape[0],image.shape[1]
#zooming
resize2=cv2.resize(image,(width*2,height*2),interpolation = cv2.INTER_CUBIC) 
cv2.imshow("resize2",resize2)
#or you can just use cv2.resize() method.
#other methods : cv2.INTER_LINEAR
cv2.waitKey(1)
"""
#***************************************************************************************************************
"""
#-----Affine Transform-----#
##|Affine transformations are a class of mathematical operations that 
##|encompass rotation, scaling, translation, shearing, and 
##|several similar transformations that are regularly used for 
##|various applications in mathematics and computer graphics.
#in this code part we are gonna perform 2d affine transforms 
#but there is also 3D transforms to.
#we need 2x3 matrix for 2d affine transform 
#this matrix used in all affine transforms with different values
#each index in this matrix corresponds to a different transform
#  | a  b  c |  
#  | d  e  f |  
#a(0,0)=scaling along x : b(0,1)=shearing along x : c(0,2)=translation along x
#d(1,0)=shearing along y : e(1,1)=scaling along y : f(1,2)=translation along y
#***************************************************************************************************************
image = cv2.imread("sudoku.jpg",cv2.IMREAD_GRAYSCALE)
height,width = image.shape
#-----Translation(shifting)-----#
#M is our affine transform matrix
M = np.float32([[1,0,100],[0,1,50]]) 
dst = cv2.warpAffine(image,M,(width,height))
cv2.imshow("shifted image",dst)
cv2.waitKey(1)
#***************************************************************************************************************
#-----Rotation-----#
#rotation transform matrix: given its centre, angle and range
M2 = cv2.getRotationMatrix2D(((width-1)/2.0,(height-1)/2.0), 90, 1) 
dst2 = cv2.warpAffine(image, M2, (width,height))
cv2.imshow("rotated image",dst2)
cv2.waitKey(1)
#***************************************************************************************************************
#-----Affine Transform-----#
#all parallel lines in original image will still be parallel in output image
pts1 = np.float32([[50,50],[200,50],[50,200]]) #define 3 points on input image
#define where the points of the image on the input will be on the output
pts2 = np.float32([[10,100],[200,50],[100,250]]) 
M3 = cv2.getAffineTransform(pts1, pts2) #get affine transform matrix
dst3 = cv2.warpAffine(image, M3, (width,height))
cv2.imshow("Affine Transform",dst3)
cv2.waitKey(1)
#***************************************************************************************************************
#-----Perspective Transform-----#
#3x3 transformation matrix needed for perspective transform. 
#Straight lines will remain straight even after the transformation. 
#define 4 points on input image
pts11 = np.float32([[56,65],[368,52],[28,387],[389,390]]) 
#define where the points of the image on the input will be on the output
pts22 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M4 = cv2.getPerspectiveTransform(pts11,pts22) #get perspective transform matrix
dst4 = cv2.warpPerspective(image,M4,(width,height))
cv2.imshow("Percpective Transform",dst4)
cv2.waitKey(1)
"""

