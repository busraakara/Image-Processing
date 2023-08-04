import cv2
import numpy as np
#***************************************************************************************************************
"""
#IMAGE
image = cv2.imread("image.jpg") #load image with imread
cv2.imshow("resim",image) #display with imshow
cv2.waitKey(5000) #display picture on the screen up to the millisecond entered
cv2.destroyAllWindows() #close windows so there are no processes running in the background
#cv.imwrite("saved_image.png", image) #save image with imwrite
"""
#***************************************************************************************************************
"""
#VIDEO
cap = cv2.VideoCapture("world.mp4") #load video
#video consists of many picture frames. So we use loop to see the video frame by frame
while True:
    success , img = cap.read() #success->True or False , img->video frames
    cv2.imshow("video",img) #show video
    if cv2.waitKey(1) & 0xFF == ord("q"): #video closes when press the "q" key. 
        break
""" 
#*************************************************************************************************************** 
"""
#CAMERA
cap = cv2.VideoCapture(0) #turn on main camera
cap.set(3,640) #3->set width
cap.set(4,480) #4->set hight
while True:
    success,img = cap.read() #success->True or False , img->camera frames
    cv2.imshow("kamera",img) #show camera
    if cv2.waitKey(1) & 0xFF == ord("q"): #camera closes when press the "q" key.
        break
cap.release() #release camera
"""
#***************************************************************************************************************
"""
#DRAWING
#create 3-channel 300x400 full black image
img = np.zeros((400,400,3),dtype=np.uint8) 
#draw a blue line of thickness 3 from top left to bottom right
cv2.line(img,(0,0),(400,400),(255,0,0),3) 
#draw rectangle with upper left and lower right values entered
cv2.rectangle(img,(100,100),(300,300),(0,255,0),5) 
#draw circle given center, radius, color and thickness 
cv2.circle(img,(200,200),90,(0,0,255),5) 
#fills the inside of the shape when -1 is written to the thickness.
#draw ellipse given center, axis, angle, start and stop angle, color and thickness
cv2.ellipse(img,(200,200),(50,20),0,0,360,(50,100,200),-1) 
font = cv2.FONT_HERSHEY_SIMPLEX #font of the text
#write text given left bottom start value, font, scale, color, thickness, line type
cv2.putText(img, ("SUBU"), (30,90), font, 4, (0,200,180),2,cv2.LINE_AA)  
cv2.imshow("drawing",img) #display image
cv2.waitKey(1)
"""
#***************************************************************************************************************
"""
#+++++Trackbar as the Color Palette+++++#
#this function is for changing color of trackbars continually
def empty(a):
    pass
#create 3-channel 300x400 full black image
img = np.zeros((200,400,3),np.uint8) 
cv2.namedWindow("palette") #create window to add image, trackbars inside
#create separate color bar for each channel
cv2.createTrackbar("R","palette",0,255,empty)
cv2.createTrackbar("G","palette",0,255,empty)
cv2.createTrackbar("B","palette",0,255,empty)
while True:
    cv2.imshow("palette",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    #transfer the value of tracbars to r, g, b variables
    r = cv2.getTrackbarPos("R", "palette") 
    g = cv2.getTrackbarPos("G", "palette")
    b = cv2.getTrackbarPos("B", "palette")
    #add r, g, b variables to image channels
    img[:] = [b,g,r]
cv2.destroyAllWindows()
"""