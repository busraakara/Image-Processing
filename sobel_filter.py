import math 
import numpy as np
import cv2 

img = cv2.imread("image.jpg")

cv2.imshow("Original image",img)

print(img.shape)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#bgr to gray çalışma şekli: Y=0.299*R + 0.587*G + 0.114*B
#bu değerlerle bgr kanalları çarpılıp toplam bir sayı elde ediliyor. Bu da gray kanalı.

cv2.imshow("Gray image", img) 

print(img.shape)


#kernelx yataydaki renk değişikliklerini algılar
kernelx = [[-1,  0,  1],
           [-2,  0,  2], 
           [-1,  0,  1]]

#kernely dikeydeki renk değişikliklerini algılar
kernely = [[-1, -2, -1], 
           [ 0,  0,  0], 
           [ 1,  2,  1]]


genislik=img.shape[1]
yukseklik=img.shape[0] 


sobel_filtre_x = np.zeros(shape=(yukseklik, genislik))
sobel_filtre_y = np.zeros(shape=(yukseklik, genislik))
sobel_filtre = np.zeros(shape=(yukseklik, genislik))


#Yatayda kenar bulma
for i in range (0,yukseklik-2):
    for j in range (0,genislik-2):
        a=img[i][j]*kernelx[0][0] + img[i][j+1]*kernelx[0][1] + img[i][j+2]*kernelx[0][2]
        b=img[i+1][j]*kernelx[1][0] + img[i+1][j+1]*kernelx[1][1] + img[i+1][j+2]*kernelx[1][2]
        c=img[i+2][j]*kernelx[2][0] + img[i+2][j+1]*kernelx[2][1] + img[i+2][j+2]*kernelx[2][2]
        d=a+b+c
        if (d<0):
            d=0
        elif (d>255):
            d=255
        sobel_filtre_x[i+1][j+1]= d
        
sobel_filtre_x=np.uint8(sobel_filtre_x) 



#Dikeyde kenar bulma    
for i in range (0,yukseklik-2):
    for j in range (0,genislik-2):
        e=img[i][j]*kernely[0][0] + img[i][j+1]*kernely[0][1] + img[i][j+2]*kernely[0][2]
        f=img[i+1][j]*kernely[1][0] + img[i+1][j+1]*kernely[1][1] + img[i+1][j+2]*kernely[1][2]
        g=img[i+2][j]*kernely[2][0] + img[i+2][j+1]*kernely[2][1] + img[i+2][j+2]*kernely[2][2]
        h=e+f+g
        if (h<0):
            h=0
        elif (h>255):
            h=255
        sobel_filtre_y[i+1][j+1]=h
sobel_filtre_y=np.uint8(sobel_filtre_y) 
        


#Yatay ve dikey kenar bulma filtrelerinin birleşimi 
for i in range (0,yukseklik-2):
    for j in range (0,genislik-2):
        a=img[i][j]*kernelx[0][0] + img[i][j+1]*kernelx[0][1] + img[i][j+2]*kernelx[0][2]
        b=img[i+1][j]*kernelx[1][0] + img[i+1][j+1]*kernelx[1][1] + img[i+1][j+2]*kernelx[1][2]
        c=img[i+2][j]*kernelx[2][0] + img[i+2][j+1]*kernelx[2][1] + img[i+2][j+2]*kernelx[2][2]
        d=a+b+c
        if (d<0):
            d=0
        elif (d>255):
            d=255
        e=img[i][j]*kernely[0][0] + img[i][j+1]*kernely[0][1] + img[i][j+2]*kernely[0][2]
        f=img[i+1][j]*kernely[1][0] + img[i+1][j+1]*kernely[1][1] + img[i+1][j+2]*kernely[1][2]
        g=img[i+2][j]*kernely[2][0] + img[i+2][j+1]*kernely[2][1] + img[i+2][j+2]*kernely[2][2]
        h=e+f+g
        if (h<0):
            h=0
        elif (h>255):
            h=255
        #resimdeki 1 piksel değeri için bulunan 2 değerlerle hipotenüs işlemi uygulanır.  
        sobel_filtre[i+1][j+1]= np.sqrt(d**2 + h**2) 
        if (sobel_filtre[i+1][j+1]<0):
            sobel_filtre[i+1][j+1]=0
        elif (sobel_filtre[i+1][j+1]>255):
            sobel_filtre[i+1][j+1]=255
         
        
sobel_filtre=np.uint8(sobel_filtre)        
   

#burda bitwise_or komutu ile hipotenüs almayla aynı iş yapılmış olur.
sobel_bitwise_or=cv2.bitwise_or(sobel_filtre_x,sobel_filtre_y)
cv2.imshow("sobel_bitwise_or",sobel_bitwise_or)

 
 
cv2.imshow("sobelxx filtrelenmis resim",sobel_filtre_x)        
cv2.imshow("sobelyy filtrelenmis resim",sobel_filtre_y) 
cv2.imshow("sobel filtrelenmis resim",sobel_filtre) 

       

    
cv2.waitKey(0)
cv2.destroyAllWindows()         
