import cv2
import numpy as np

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,130)
myPoints = [] #[x,y,colorID]

myColors = [[66, 41, 54, 91, 75, 79],[105, 69, 53, 122, 141, 153]]
myColorValues=[[5,156,0], #BGR
               [255,17,0]]
def findColor(img,myColors,myColorValues):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count=0
    newPoints=[]
    for color in myColors:
        lower = np.array(color[0:3], dtype=np.uint8)
        upper = np.array(color[3:6], dtype=np.uint8)
        mask = cv2.inRange(imgHSV,lower,upper)
        getContours(mask)
        x,y = getContours(mask)
        cv2.circle(imgResult,(x,y),10,myColorValues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count +=1
        # cv2.imshow(str(color[0]),mask)
    return newPoints
    
def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            #cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            #print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2,y
def drawOnCanvas(myPoints,myColorValues):
    for Point in myPoints:
        cv2.circle(imgResult,(Point[0],Point[1]),10,myColorValues[Point[2]],cv2.FILLED)
frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 130)


while True:
    success, img = cap.read() #cap.read() میاد فریم جدید ویدیو رو میخونه و اونو برمیگردونه
    imgResult=img.copy()
    newPoints = findColor(img,myColors,myColorValues)
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints,myColorValues)
    cv2.imshow("Video", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'): #اگر دکمه q رو بزنیم حلقه رو میشکنه
        break

