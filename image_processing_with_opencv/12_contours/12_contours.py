import numpy as np
import cv2
#***************************************************************************************************************
"""
#What are contours?
#Contours can be explained simply as a curve joining all the continuous points 
#(along the boundary), having same color or intensity.
#with Opencv, we can analize and manipulate contours to make inferences about objects.
#-----CONTOUR BASICS-----#
image = cv2.imread("objects.png")
#first convert image to binary
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh  = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)
#detect contours
#this method gives 2 output: contours and hierarchy.
#contours is a array of contours coordinates that found. 
#we gonna learn about hierarcy, RETR_EXTERNAL and CHAIN_APPROX_SIMPLE below
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#the length of contours is number of contours that found with findContours module,
#and in this contour numbers there are coordinates of the contour.
print("Number of contours found = {}".format(len(contours)))
#we use original image to draw contours because we find contours on binary image
#we have to convert this binary image to 3-channel image or we can use original.
cv2.drawContours(image, contours, -1, (0,255,0), 3)
cv2.imshow("Contours",image)


#-----Importance of Pre-Processing-----#
#as we mentioned above we have to use binary images to find contours.
#you can use grayscale image too, opencv allows this.
#But just because you can do it doesn't mean you should.
#we are gonna see the results in both ways.
image2 = cv2.imread("tree.jpg")
#copy image to display both output
image2_copy2 = image2.copy()
#first convert image to grayscale
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
#we invert gray image with bitwise_not to keep foreground white.
gray_inverted = cv2.bitwise_not(gray2)
#find contours on gray image
contours, hierarchy = cv2.findContours(gray_inverted, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(image2, contours, -1, (0, 255, 0), 2)
cv2.imshow("grayscale image contours",image2)
#now convert gray image to binary and find contours
_, binary = cv2.threshold(gray_inverted, 100, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image2_copy2, contours, -1, (0, 0, 255), 2)
cv2.imshow("binary image contours",image2_copy2)



#if threshold doesn't work with your image because objects have different intensity
#either you can use Canny for find edges, or adaptive threshold.
#-----Contour Detection With Canny-----#
image3= cv2.imread("chess.jpg")
blurred_image = cv2.GaussianBlur(image3.copy(),(5,5),0)
edges = cv2.Canny(blurred_image, 100, 200)
cv2.imshow("edges",edges)
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image3, contours, -1, (0, 255, 0), 2)
cv2.imshow("contours with canny",image3)

#-----Contour Detection With Adaptive Threshold-----#
image3_copy2 = image3.copy()
blurred = cv2.GaussianBlur(image3_copy2,(3,3),0)
gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
binary = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV, 11, 5)
cv2.imshow("binary",binary)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image3_copy2, contours, -1, (0, 255, 0), 2)
cv2.imshow("contours with adaptive thresh",image3_copy2)
"""
#***************************************************************************************************************
"""
#-----Contouring Modes-----#
#before modes we have to learn about methods
#CHAIN_APPROX_NONE : this method keeps every contour coordinates in list
#CHAIN_APPROX_SIMPLE :this method keeps only usefull contour coordinates in list

image = cv2.imread("objects.png")
image1= image.copy()
image2= image.copy()
image3= image.copy()
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh  = cv2.threshold(imageGray, 125, 255, cv2.THRESH_BINARY)
#cv2.RETR_LIST
#whith RETR_LIST mode we are finding every contours in image without any hierarchy
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#draw contours
#-1 is for draw all contours found. but you can just draw certain contours with its index
cv2.drawContours(image, contours, -1, (0,255,0), 3);
#Find contour numbers that are found
print("Number of contours found: {}".format(len(contours)))
cv2.imshow("RETR_LIST",image)

#RETR_EXTERNAL
#with RETR_EXTERNAL mode we are finding only external contours.
contours1, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#draw all contours
cv2.drawContours(image1, contours1, -1, (0,255,0), 3);
#find contour numbers that are found
print("Number of contours found: {}".format(len(contours1)))
cv2.imshow("RETR_EXTERNAL",image1)

#RETR_TREE
#with RETR_TREE mode we are finding every contour with hierarchy.
contours2, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#draw all contours
cv2.drawContours(image2, contours2, -1, (0,255,0), 3);
#find contour numbers that are found
print("Number of contours found: {}".format(len(contours2)))
cv2.imshow("RETR_TREE",image2)

#RETR_CCOMP
#with RETR_CCOMP mode we are finding all contours with hierarchy
#but difference between RETR_TREE and RETR_CCOMP is in RETR_CCOMP you can define holes of object
contours3, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
for i,cont in enumerate(contours3):
    #if hierarchy level of contour is 1 : draw green contour
    if hierarchy[0][i][3] == -1:
        image3 = cv2.drawContours(image3, cont, -1, (0,255,0), 3)
    #else draw red contours (holes)
    else:
        image3 = cv2.drawContours(image3, cont, -1, (255,0,0), 3)
#find contour numbers that are found
print("Number of contours found: {}".format(len(contours)))
cv2.imshow("RETR_CCOOMP",image3)
"""
#***************************************************************************************************************
"""
#-----Contour Manupilation-----#
#with contour manupilation we can work on usefull contours and analize them.
image = cv2.imread("objects.png")
image1 = image.copy()
image2 = image.copy()
image3 = image.copy()

#-----Finding The Biggest Contour-----#
#first convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh  = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)
#find contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
#cv2.contourArea : Since contours are closed curves, they have areas. 
#The contourArea gives us its areas.
#with max module we can get contour with biggest area with contourArea key.
biggest_contour = max(contours, key = cv2.contourArea)
#draw the biggest contour
cv2.drawContours(image, biggest_contour, -1, (0,255,0), 4)
cv2.imshow("biggest contour",image)

#-----Ordering Contours-----#
contours1, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#sort contours from biggest to smallest with contourArea key
sorted_contours = sorted(contours1, key=cv2.contourArea, reverse= True)
#
for i, cont in enumerate(sorted_contours,1):
    #draw contours
    cv2.drawContours(image1, cont, -1, (0,255,0), 3)
    #write contours numbers according to sorting
    cv2.putText(image1, str(i), (cont[0,0,0], cont[0,0,1]-10), cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0, 0, 255),4)
cv2.imshow("sorted contours",image1)


#-----Draw Boxes To Contours-----#
contours2, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE,)
#get the contour points
x, y, w, h = cv2.boundingRect(contours[0])
#draw rectangle box around object
cv2.rectangle(image2, (x, y), (x+w, y+h), (0, 255, 0), 3)
cv2.imshow("rect contour",image2)
#find the smallest area that contour can fit
rect = cv2.minAreaRect(contours[0])
#get the points of this smallest area
box =  cv2.boxPoints(rect).astype('int')
#draw rectangle box around object
cv2.drawContours(image3,[box],0,(0,255,0),3)
cv2.imshow("bbox contour",image3)

#-----Drawing Convex Hull-----#
#we can draw lines betweens maximum points of object and
#these lines create Convex Hull for our object in image
image = cv2.imread("C:/Users/PC/Desktop/tree.jpg")
image_hull = image.copy()
#convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#convert image to binary
_, binary = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY_INV)
#find contours
contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#we get first contour in contours list. Cause we know we have just one object on this image
cnt = contours[0]
hull = cv2.convexHull(cnt)
#draw Convex Hull
cv2.drawContours(image_hull, [hull], 0 , (0,0,255), 3) 
#draw contours
cv2.drawContours(image, [cnt], 0, (0,0,255), 3)
cv2.imshow("contoursss",image)
cv2.imshow("convex-hull",image_hull)
"""
#***************************************************************************************************************
"""
#-----Finding Shapes By Contours-----#
#in this apllication, we have image with various shapes: 
#Rectangle, circle, square, triangle etc. 
#and we want to detect them by their corner points.
#first we create a function to detect corners and shapes. 
#After that we are gonna send our image to this function and see the result.

def getContours(img):
    #conver image to grayscale
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #apply blur to image to get rid of noises
    imgGR_blur = cv2.GaussianBlur(imgGray,(11,11),2)
    #use canny to find edges
    imgCanny = cv2.Canny(imgGR_blur,100,200)
    #find contours
    contours,_ = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    #loop for processing contours
    for cnt in contours:
        #get contour area
        area = cv2.contourArea(cnt)
        #if area is bigger than 300: continue. To get rid of noises again.
        if area > 300:
            #draw contours to display
            cv2.drawContours(img,cnt,-1,[255,0,0],3)
            #get arc length. True because our shapes are closed.
            length = cv2.arcLength(cnt,True)
            #approxPolyDP approximates a contour shape to another shape 
            #with less number of vertices depending upon the precision we specify.
            cornerPoints= cv2.approxPolyDP(cnt, 0.02*length, True)
            #get how many corner points of our shape has
            cornerCount = len(cornerPoints)
            #get points to draw box
            x, y, w, h = cv2.boundingRect(cornerPoints)
            #draw rectangle around our shape. 
            cv2.rectangle(img,(x,y-15),(x+w,y+h),[0,255,0],2)
            #if cornerCount is 3, then our shape is triangle.
            if cornerCount == 3:
                #write triangle top of the shape
                cv2.putText(img,"TRIANGLE",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.7,[0,0,0])
            #if cornerCount is 4 then our shape is either a square or a rectangle
            elif cornerCount == 4:
                #to detect square we can look at the aspect ratio. 
                h = float(h) #height
                w = float(w) #width
                ratio = w/h
                #we set a range because ratio can't be 1 all the time
                #if ratio between these numbers than our shape is square
                if ratio > 0.8 and ratio < 1.2:
                    #write square top of the shape
                    cv2.putText(img,"SQUARE",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.7,[0,0,0])
               #else it is rectangle
                else:
                    #write rectangle top of the shape
                    cv2.putText(img,"RECTANGLE",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.7,[0,0,0])
            #if there are no corner points then it is circle
            else:
                #write circle top of the shape
                cv2.putText(img,"CIRCLE",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.7,[0,0,0])
    return img

img = cv2.imread("shapes.png")
shapes = getContours(img)
cv2.imshow("output",shapes)
"""


cv2.waitKey(1)