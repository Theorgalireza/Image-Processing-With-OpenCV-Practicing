import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm
cap = cv2.VideoCapture(0)
detector = htm.HandDetector()
pTime = 0
cTime = 0
while True:
    success, img = cap.read()


    img = detector.findHands(img,draw=True)
    lmList = detector.findPosition(img,draw=True)
    if len(lmList) !=0:
        print(lmList[8])
    cTime = time.time()
    fps = 1 / (cTime - pTime) if (cTime - pTime) > 0 else 0
    pTime = cTime

    cv2.putText(
        img, str(int(fps)), (10, 70),
        cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 255), 3
    )
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break