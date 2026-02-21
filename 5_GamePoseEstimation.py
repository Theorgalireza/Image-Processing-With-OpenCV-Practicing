import cv2
import time
import PoseEstimationModule as pm


pTime=0
cap = cv2.VideoCapture(0)
detector = pm.PoseDetector()
while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.findPosition(img,draw=False)
    if len(lmList)!=0:
        print(lmList[14])
    cv2.circle(img, (lmList[14][1],lmList[14][2]), 10, (0,0,255), cv2.FILLED)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(
        img,
        f"FPS: {int(fps)}",
        (10, 50),
        cv2.FONT_HERSHEY_DUPLEX,
        1.5,
        (0, 255, 0),
        2
    )    
    cv2.imshow("Image",img)
    cv2.waitKey(1)
