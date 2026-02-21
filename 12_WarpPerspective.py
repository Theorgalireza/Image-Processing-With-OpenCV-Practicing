import cv2
import numpy as np
img = cv2.imread('c:/Users/alireza/Desktop/Identify.jpg')
width,height = img.shape[0],img.shape[1]
#like we need four points and corner to define a warp perspective for a rectangle shape
pts1=np.float32([[111,219],[287,188],[154,482],[354,440]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("Image",imgOutput)
cv2.waitKey(0)