import cv2
import numpy as np
img = cv2.imread("c:/Users/alireza/Desktop/Picture1.png")
#in cv2 we have x & y, but y is in opposite of a function

#Resizing
print(img.shape) #Prints (height, weidth, number of channels)
imgResize=cv2.resize(img,(300,140)) #weidth,height: x,y

#Crop
imgCropped = img[0:100,0:200] #height,weidth: y,x
cv2.imshow("Image",imgCropped)
cv2.waitKey(0)