import cv2
import mediapipe as mp
import time
import numpy as np
import PoseEstimationModule as pem
cap = cv2.VideoCapture(0)

detector = pem.PoseDetector()

pTime = 0
while True:
    success, img=cap.read()
    img = detector.findPose(img,False)
    imList = detector.findPosition(img,draw=False)
    if len(imList)!=0:
        angle = detector.findAngle(img,12,14,16)
        per = np.interp(angle,(170,50),(0,100))
        print(per)



    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime= cTime
    cv2.putText(img,f"FPS: {int(fps)}",(40,70),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2)
    cv2.imshow("Image",img)
    if cv2.waitKey(1) & 0xFF == ord('q'): #اگر دکمه q رو بزنیم حلقه رو میشکنه
        break