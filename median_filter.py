import numpy as np
import cv2 

img = cv2.imread("image.jpg")

cv2.imshow("Original image",img)

print(img.shape)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#bgr to gray çalışma şekli: Y=0.299*R + 0.587*G + 0.114*B
#bu değerlerle bgr kanalları çarpılıp toplam bir sayı elde ediliyor. Bu da gray kanalı

cv2.imshow("Gray image", img) 

print(img.shape)
print(img.shape)

genislik=img.shape[1]
yukseklik=img.shape[0] 

median_filtre = np.zeros(shape=(genislik, yukseklik))

#burda 3x3 kaydırma ile matrisdeki değerleri listeye ekleyip küçükten büyüğe sıraladıktan sonra ortadaki değeri median_filtreye atıyoruz.
for i in range (0,yukseklik-2):
    for j in range (0,genislik-2):
        liste=[]
        liste.append(img[i][j])
        liste.append(img[i][j+1])
        liste.append(img[i][j+2])
        liste.append(img[i+1][j])
        liste.append(img[i+1][j+1])
        liste.append(img[i+1][j+2])
        liste.append(img[i+2][j])
        liste.append(img[i+2][j+1])
        liste.append(img[i+2][j+2])
        liste.sort()
        median_filtre[i+1][j+1]=liste[4]
median_filtre=np.uint8(median_filtre)  
   
cv2.imshow("Medyan filtrelenmis resim",median_filtre)  

cv2.waitKey(0)
cv2.destroyAllWindows()      
