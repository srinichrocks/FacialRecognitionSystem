import cv2 as cv
import os
import numpy as np
img = cv.imread('Photos/sri.jpg')
# cv.imshow('Sri',img)


#Haar cascade
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
haar_cascade = cv.CascadeClassifier('haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 10)
print(f'# of faces: {len(faces_rect)}')
for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness = 2)
cv.imshow('Detected face', img)

#Face recognition using opencv built-in recognizer
# people = ['Sri', 'Kush', 'Shamith']
# # DIR

# p = []
# for i in os.listdir(r'') 

cv.waitKey(0)
