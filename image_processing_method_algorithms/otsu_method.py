#import libraries
import cv2 
import copy

#import image
img = cv2.imread("image.jpg")
cv2.imshow("Original Image",img)

#convert image colour bgr to gray scale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Scaled Image",img)
"""
We can also use :
b , g , r = img[:,:,0] , img[:,:,1] , img[:,:,2]
img = np.uint8(np.round((b * 0.114 + g * 0.587 + r * 0.299)))
this method is Luminosity method to convert image to gray scale
Luminosity method : b * 0.114 + g * 0.587 + r * 0.299
(b * 0.0722  + g * 0.7152 + r * 0.2126 also used)
"""
#implement OpenCV Otsu method to compare 
ret,ot=cv2.threshold(img,0,255,cv2.THRESH_OTSU)
cv2.imshow("opencv otsu" , ot)

width=img.shape[1]
height=img.shape[0] 

#Creat 1D array of image pixels
listt=[]
for i in range (0,height):
    for j in range (0,width):
        listt.append(img[i][j])

#Histogram table
histogram_list=[]
for i in range(256):
    count = 0
    for j in range(len(listt)):
        if (listt[j] == i):
            count = count+1
    histogram_list.append(count)        

#Another list for non-zero histogram values          
histogram=[]    
for i in range (256):
    list1=[]
    if (histogram_list[i] != 0):
        list1.append(histogram_list[i])
        list1.append(i)
        histogram.append(list1)


background_w=copy.deepcopy(histogram)
for i in range (len(histogram)):
    sum=0
    for j in range (len(histogram)-1):
        sum+=histogram[j][0]
        if (j==i):
            w=sum/len(listt)
            background_w[i+1][0]=w
background_w[0][0]=0
        

background_u=copy.deepcopy(histogram)   
for i in range (len(histogram)):
    sum=0
    sum2=0
    for j in range (len(histogram)-1):
        sum2+=histogram[j][0]
        sum+=histogram[j][0]*histogram[j][1]
        if (j==i):
            w=sum/sum2
            background_u[i+1][0]=w     
background_u[0][0]=0

   
foreground_w=copy.deepcopy(histogram)
for i in range (len(histogram)):
    sum=0
    for j in range(i,len(histogram)):
        sum+=histogram[j][0]
    w=sum/len(listt)
    foreground_w[i][0]=w
  
    
foreground_u=copy.deepcopy(histogram)
for i in range (len(histogram)):
    sum=0
    sum2=0
    for j in range(i,len(histogram)):
        sum2+=histogram[j][0]
        sum+=histogram[j][0]*histogram[j][1]
    w=sum/sum2
    foreground_u[i][0]=w  
    
    
otsu_values=copy.deepcopy(histogram)    
for i in range(len(histogram)):
    tao=background_w[i][0]*foreground_w[i][0]*((background_u[i][0]-foreground_u[i][0])**2)
    otsu_values[i][0]=tao
    

otsu_values1=copy.deepcopy(otsu_values)
for i in range(len(otsu_values1)):
    for j in range(i + 1, len(otsu_values1)):
        if otsu_values1[i][0] > otsu_values1[j][0]:
           otsu_values1[i], otsu_values1[j] = otsu_values1[j], otsu_values1[i]

a= otsu_values1[(len(otsu_values1)-1)][1]

for i in range (0,height):
    for j in range (0,width):
        if (img[i][j]>=a):
            img[i][j]=255
        elif (img[i][j]<a):
            img[i][j]=0
                
cv2.imshow("Tresholded image",img)          
        
        
cv2.waitKey(0)
cv2.destroyAllWindows()           