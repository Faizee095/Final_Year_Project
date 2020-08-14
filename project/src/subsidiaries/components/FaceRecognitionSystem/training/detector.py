import cv2
import numpy as np

faceDetector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cam = cv2.VideoCapture(0)

recog = cv2.face.LBPHFaceRecognizer_create()
recog.read("training\\trainingData.yml")

id = 0
font = cv2.FONT_HERSHEY_SIMPLEX


while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(gray, 1.4, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        id, conf = recog.predict(gray[y : y + h, x : x + w])

        if id == 1:
            id = "Sumit"
        else:
            id = "Unknown"
        cv2.putText(img, str(id), (x, y + h), font, 2, (0, 255, 0), 3)

    cv2.imshow("Face", img)
    if cv2.waitKey(1) == ord("q"):
        break
cam.release()
cv2.destroyAllWindows()
