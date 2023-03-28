import numpy as np
import cv2 
import copy

img = cv2.imread("img.png")
#cv2.imshow("Original image",img)
print(img.shape)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#bgr to gray çalışma şekli: Y=0.299*R + 0.587*G + 0.114*B
#bu değerlerle bgr kanalları çarpılıp toplam bir sayı elde ediliyor. Bu da gray kanalı
cv2.imshow("Gray image", img) 

ot=cv2.threshold(img,0,255,cv2.THRESH_OTSU)
cv2.imshow("opencv otsu" , ot[1])


genislik=img.shape[1]
yukseklik=img.shape[0] 

#Creat 1D array for pixels
liste=[]
for i in range (0,yukseklik):
    for j in range (0,genislik):
        liste.append(img[i][j])

#Histogram table
histogram_liste=[]
for i in range(256):
    count = 0
    for j in range(len(liste)):
        if (liste[j] == i):
            count = count+1
    histogram_liste.append(count)        

#Another list for non-zero histogram values          
histogram=[]    
for i in range (256):
    list1=[]
    if (histogram_liste[i] != 0):
        list1.append(histogram_liste[i])
        list1.append(i)
        histogram.append(list1)


background_w=copy.deepcopy(histogram)
for i in range (len(histogram)):
    sum=0
    for j in range (len(histogram)-1):
        sum+=histogram[j][0]
        if (j==i):
            w=sum/len(liste)
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
    w=sum/len(liste)
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
    
    
otsu_degerleri=copy.deepcopy(histogram)    
for i in range(len(histogram)):
    tao=background_w[i][0]*foreground_w[i][0]*((background_u[i][0]-foreground_u[i][0])**2)
    otsu_degerleri[i][0]=tao
    

otsu_degerlerii=copy.deepcopy(otsu_degerleri)
for i in range(len(otsu_degerlerii)):
    for j in range(i + 1, len(otsu_degerlerii)):

        if otsu_degerlerii[i][0] > otsu_degerlerii[j][0]:
           otsu_degerlerii[i], otsu_degerlerii[j] = otsu_degerlerii[j], otsu_degerlerii[i]

a= otsu_degerlerii[(len(otsu_degerlerii)-1)][1]

for i in range (0,yukseklik):
    for j in range (0,genislik):
        if (img[i][j]>=a):
            img[i][j]=255
        elif (img[i][j]<a):
            img[i][j]=0
                
cv2.imshow("Tresholded image",img)          
        
        
cv2.waitKey(0)
cv2.destroyAllWindows()           
