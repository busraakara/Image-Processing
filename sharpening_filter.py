import numpy as np
import cv2

img = cv2.imread("C:/Users/PC/Desktop/moonnnn.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

height0 = img.shape[0]
width0 = img.shape[1]

gaussian_filter=np.zeros((height0,width0))

zero_padd_img = np.zeros((height0+2,width0+2))
zero_padd_img[1:height0+1 , 1:width0+1] = img

kernel_gauss = np.array([[1/16, 1/8, 1/16],   
                         [ 1/8, 1/4,  1/8],
                         [1/16, 1/8, 1/16]])

height1 = zero_padd_img.shape[0]
width1 = zero_padd_img.shape[1]

for i in range(height1-2):
    for j in range(width1-2):
        block = zero_padd_img[i:i+3 , j:j+3]
        gaussian_filter[i][j] = round(np.sum(np.multiply(block,kernel_gauss)))

laplacian_filter=np.zeros((height0,width0))

zero_padd_gauss=np.zeros((height0+2,width0+2))
zero_padd_gauss[1:height0+1 , 1:width0+1] = gaussian_filter

kernel_laplacian = np.array([[-1, -1, -1],
                             [-1,  8, -1],
                             [-1, -1, -1]])

height2 = zero_padd_gauss.shape[0]
width2 = zero_padd_gauss.shape[1]

for i in range(height2-2):
    for j in range(width2-2):
        block = zero_padd_gauss[i:i+3 , j:j+3]
        laplacian_filter[i][j] = np.sum(np.multiply(block,kernel_laplacian))
        
sharpening_filter=np.zeros((height0,width0))        
for i in range(height0):
    for j in range(width0):
        sharpening_filter[i][j] = img[i][j] + laplacian_filter[i][j]
        if sharpening_filter[i][j] < 0:
            sharpening_filter[i][j] = 0
        elif sharpening_filter[i][j] > 255:
            sharpening_filter[i][j] = 255
sharpening_filter = np.uint8(sharpening_filter)      
      
cv2.imshow("first image",img)
cv2.imshow("sharpened image",sharpening_filter)    

cv2.waitKey(0)
cv2.destroyAllWindows()        
        
        
        
            