import cv2 as cv
import numpy as np

img = cv.imread('Photos/kush.jpeg')
img2 = cv.imread('Photos/sri.jpg')
resized = cv.resize(img, (500, 600))
resized2 = cv.resize(img2, (500,600))

blank = np.zeros(img.shape[:2], dtype='uint8')
# cv.imshow('Blank', blank)

mask = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 200, 255, -1)
# cv.imshow('Mask',mask)

masked_image = cv.bitwise_and(img, img, mask = mask)
# cv.imshow('Masked Image',masked_image)







# cv.imshow('Combined', np.bitwise_xor(resized, resized2))
# blank = np.zeros((400,400), dtype='uint8')
# rectangle = cv.rectangle(blank.copy(), (30, 30), (370,370), 255, -1)
# circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)
# cv.imshow('Bitwise',np.bitwise_and(rectangle,circle))
# cv.imshow('Rectangle', rectangle)
# cv.imshow('Circle', circle)

cv.waitKey(0)

