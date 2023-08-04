import numpy as np
import cv2
#***************************************************************************************************************
"""
#CHANGING COLOR SPACES
img = cv2.imread("image.jpg")
#changing color 3-channel to 1-channel gray scale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray image",gray)
#changing color gr to hsv h:hue s:saturation v:value
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("hsv channel image",hsv)
#changing color bgr to hsv h:hue s:saturation l:lightness 
hsl = cv2.cvtColor(img,cv2.COLOR_BGR2HLS)
cv2.imshow("hsl channel image",hsl)
#changing color bgr to YCbCr Y:luma(brightness) Cb:blue minus luma(B-Y) Cr:red minus luma(R-Y)
YCrCb = cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)
cv2.imshow("YCrCb channel image",YCrCb)
cv2.waitKey(1)
"""
#***************************************************************************************************************
"""
#+++++Color Tracking+++++#
cap = cv2.VideoCapture(0)
while(1):
    _, frame = cap.read() 
    # Convert BGR color channel to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([100,50,50]) #there is range of blue color in HSV.
    upper_blue = np.array([130,255,255]) #with lower and upper we get the range of the blue value.
    #with "mask":pixels in this range in the image will be 1 and the others will be 0.
    mask = cv2.inRange(hsv, lower_blue, upper_blue) 
    #with bitwise-and white part of the mask will be real color of image and others will be black.
    last = cv2.bitwise_and(frame,frame, mask= mask) 
    cv2.imshow('frame',frame) #real camera image
    cv2.imshow('mask',mask) #mask that we define blue range as 1 (white).
    cv2.imshow('filter',last) #blue color tracking
    if cv2.waitKey(1) & 0xFF == ord("q"): #break point to exit the camera.
        break
cv2.destroyAllWindows()
"""