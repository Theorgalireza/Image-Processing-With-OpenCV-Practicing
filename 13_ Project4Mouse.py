import cv2
import numpy as np
import time
import math
import autopy
import HandTrackingModule as htm

cap = cv2.VideoCapture(0)
wCam = 640
hCam = 480
cap.set(3,wCam)
cap.set(4,hCam)
pTime = 0
detector = htm.HandDetector(maxHands=1)
wScr, hScr = autopy.screen.size()
frameR = 100
smoothening = 7
plocX,plocY = 0,0
clocX,clocY = 0,0

while True:
    success, img = cap.read()
    #1 Find hand landmarks
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    cv2.rectangle(img,(frameR,frameR),(wCam-frameR, hCam-frameR),(255,0,255),2)

    #2 Get the tip of the index and middle finger
    if len(lmList)!=0:
        x1,y1 = lmList[8][1:]
        x2,y2 = lmList[12][1:]

    #3 Check wich fingers are up
        fingers = detector.fingersUp()
        # print(fingers)


        #4 Only index finger: Moving Mode
        if fingers[1]==1 and fingers[2]==0:
            #5 Conver Coordinates
            # cv2.rectangle(img,(frameR,frameR),(wCam-frameR, hCam-frameR),(255,0,255),2)
            x3 = np.interp(x1, (frameR,wCam-frameR),(0,wScr))
            y3 = np.interp(y1, (frameR,hCam-frameR),(0,hScr))
        
            #6 Smoothen Values
            clocX = plocX+(x3 - plocX) /smoothening
            clocY = plocY+(y3 - plocY) /smoothening



            #7 Move Mouse
            autopy.mouse.move(wScr-clocX,clocY)
            cv2.circle(img,(x1,y1),15,(255,0,0),cv2.FILLED)
            plocX,plocY = clocX,clocY

        #8 Both index and middle fingers are up: Clicking mode
        if fingers[1]==1 and fingers[2]==1:
            
            #9 Find Distance between fingers
            length,img,lineInfo = detector.findDistance(8,12,img)
            if length<50:
                cv2.circle(img,(lineInfo[4],lineInfo[5]),15,(0,255,0),cv2.FILLED)
                
                #10 Click Mouse if distance short
                autopy.mouse.click()

    #11 Frame Rate
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime= cTime
    cv2.putText(img,str(int(fps)),(40,70),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2)

    #12 Display
    cv2.imshow("Image",img)
    if cv2.waitKey(1) & 0xFF == ord('q'): #اگر دکمه q رو بزنیم حلقه رو میشکنه
        break