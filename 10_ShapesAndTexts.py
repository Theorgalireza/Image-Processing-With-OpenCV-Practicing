import cv2
import numpy as np
#defining a black img with 512 512 and 3 channels to coloring
img = np.zeros((512,512,3),np.uint8)
# img[200:300,100:300] = 250,0,0 //Coloring

cv2.line(img,(0,200),(img.shape[1],img.shape[0]),(0,255,0),3)#Line
cv2.rectangle(img,(0,0),(200,200),(0,0,255),cv2.FILLED)#rectangle: (img,(starting point),(ending point),(Color),(thickness <or filling>))
cv2.circle(img,(400,50),30,(255,255,0),1)# Circle

cv2.putText(img,"OpenCV ",(256,256),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)#Text:(img,"Text",(Starting Point),Font,scale,(color),thickness) 
cv2.imshow('Image',img)
cv2.waitKey(0)