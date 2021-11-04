import cv2 as cv
import numpy as np

img = cv.imread('Photos/kush.jpeg')
# cv.imshow('Kush', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


#Laplacian edge detection
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)
#Sobel edge detection
# Sobel Edge Detection
sobelx = cv.Sobel(src=img, ddepth=cv.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
sobely = cv.Sobel(src=img, ddepth=cv.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
sobelxy = cv.Sobel(src=img, ddepth=cv.CV_64F, dx=1, dy=1, ksize=5) #

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Sobel XY', sobelxy)

cv.waitKey(0)