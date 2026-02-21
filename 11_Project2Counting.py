import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm
import os

cap = cv2.VideoCapture(0)
detector = htm.HandDetector()
pTime = 0

folderPath = "D:/Developling/Xerox/Video2/Project2"
myList = os.listdir(folderPath)
print(myList)
overlayList = []
for imPath in myList:
    image = cv2.imread(f"{folderPath}/{imPath}")
    overlayList.append(image)

tipIds = [4, 8, 12, 16, 20]

while True:
    success, img=cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img,draw=False)
    
    if len(lmList)!=0:
        fingers = []
        #Thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
            fingers.append(1)
        else: fingers.append(0) 
     
        #4 finger  
        for id in range(1,5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                fingers.append(1)
            else: fingers.append(0)
        print(fingers)
        totalFingers = fingers.count(1)
        overlayImg = overlayList[totalFingers]
        h, w, _ = overlayImg.shape
        crop = overlayImg[0:200, 0:200]  # اگر مطمئنی از بالا و چپ مناسبشه
        img[0:200, 0:200] = crop
        cv2.rectangle(img,(20,255),(170,425),(0,255,0),cv2.FILLED)
        


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime= cTime
    cv2.putText(img,f"FPS: {int(fps)}",(40,70),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2)
    cv2.imshow("Image",img)
    if cv2.waitKey(1) & 0xFF == ord('q'): #اگر دکمه q رو بزنیم حلقه رو میشکنه
        break