# Face recognition
# create dataset-> creator
# trainer
# detector

import cv2
import numpy as np

faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

id = int(input("Enter user Id "))

sample_number = 0
while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        sample_number = sample_number + 1
        cv2.imwrite("dataSet/user."+str(id)+"." +
                    str(sample_number)+".jpg", gray[y:y+h, x:x+w])
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.waitKey(100)

    cv2.imshow("Face", img)
    if sample_number > 20:
        break

cam.release()
cv2.destroyAllWindows()
