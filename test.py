import cv2
import mediapipe as mp

mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh()

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)

    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            for id, lm in enumerate(faceLms.landmark):
                h, w, c = img.shape
                x, y = int(lm.x * w), int(lm.y * h)
                cv2.circle(img, (x, y), 1, (0, 255, 0), -1)

    cv2.imshow("Face Mesh", img)
    cv2.waitKey(1)