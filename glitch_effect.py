import cv2 

img = cv2.imread("image.jpg")

height , width = img.shape[:2]

img[0:height,0:width,0] = img[0:height,0:width,0]

img[0:height-7, 0:width-7,1]=img[7:height,7:width,1]

img[0:height-15, 0:width-15,2]=img[15:height,15:width,2]

cv2.imshow("glitch image",img)

cv2.waitKey(1)
