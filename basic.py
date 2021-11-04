import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np



img = cv.imread('Photos/kush.jpeg')
img2 = cv.imread('Photos/sri.jpg')
# print(img[0])
# cv.imshow('Ripped Jeans', img)

#Rescale Function
def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)


#Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

#Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

#Resize
resized = cv.resize(img, (500, 700))
# cv.imshow('Resized', resized)

#Edge Cascade
canny = cv.Canny(img2, 125, 175)
# cv.imshow('Edges', canny)

#Dilating the image
dilated = cv.dilate(canny, (7,7), iterations = 3)
cv.imshow('Dilated', dilated)

#Eroding
eroded = cv.erode(dilated, (7,7), iterations = 3)
# cv.imshow('Eroded', eroded)

#Cropped
cropped = img[10:20, 20:40]
# cv.imshow('Cropped', cropped)

#Color shift
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)

#Thresholding
threshold, thresh = cv.threshold(img, 225, 255, cv.THRESH_BINARY)
# cv.imshow('Simple Thresholded', thresh)

#Histogram
# my_hist = cv.calcHist([img, img2], [0], None, [256], [0,256])
# kush_hist = cv.calcHist([img,img2], [1], None, [256], [0,256])
# plt.figure()
# plt.title('My histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(kush_hist)
# plt.plot(my_hist)
# plt.xlim([0,256])
# plt.show()


cv.waitKey(0)