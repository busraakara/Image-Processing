import numpy as np
import cv2
import copy
import matplotlib.pyplot as plt

img = cv2.imread("C:/Users/PC/Desktop/t/moon.jpg")
#convert image to grayscale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original Image",img)

#define height and width
height = img.shape[0]
width = img.shape[1]

#create histogram table for unequalized image
histogram = [0] * 256

#do a cumulative addition
for i in range(height):
    for j in range(width):
        histogram[img[i][j]] += 1


#create histogram plot and show
plt.figure(1,figsize= (7,7))
pixels = np.linspace(0,255,256,dtype="int16")
plt.subplot(1, 1,1)
plt.plot(pixels,histogram)
plt.title("Unequalized histogram table")
plt.show()


#find the min value other than 0 of cumulative addition list
for i in histogram:
    if i != 0:
        cdf_min = i
        break
    
#Equalize pixel values
cdf = copy.deepcopy(histogram)    
count = 0    
for i in range(len(cdf)):
    count = count + histogram[i]
    cdf[i] = count
mxn = height * width

h = copy.deepcopy(cdf)
for i in range(len(h)):
    h[i] = round(((cdf[i] - cdf_min) / (mxn - cdf_min)) * 255)
    

#change pixel values with equalized values
for i in range(height):
    for j in range(width): 
            a = img[i][j]
            img[i][j] = h[a]
            
cv2.imshow("Equalized image",img)             

#create histogram table with equalized image pixel values and show
histogram_e = [0] * 256
for i in range(height):
    for j in range(width):
        histogram_e[img[i][j]] += 1
        
plt.figure(2,figsize=(7,7))
pixels = np.linspace(0,255,256,dtype="int16")            
plt.plot(pixels,histogram_e)
plt.title("Equalized histogram table")
plt.show()

cv2.waitKey(1)