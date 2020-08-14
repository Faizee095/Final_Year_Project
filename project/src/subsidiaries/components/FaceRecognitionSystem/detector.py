import cv2
import numpy as np
from datetime import datetime
import sys
import eel

# from src.subsidiaries.components.Utils.speech.textSpeech import VoiceEngine
from collections import defaultdict
import threading

active_event_list = []


def notify(a, s):
    global active_event_list
    label = max(s, key=s.get)
    if s[label] != 0:
        active_event_list.append(label + " is at the door")
        return


def detector():
    a = sys._MEIPASS
    defaultdict = {}
    defaultdict["Rohit"] = 0
    defaultdict["Argh"] = 0
    defaultdict["Antima"] = 0
    defaultdict["Rakesh"] = 0
    defaultdict["unknown"] = 0

    lastSeen = datetime.now()

    faceDetector = cv2.CascadeClassifier(a + "\\haarcascade_frontalface_default.xml")
    cam = cv2.VideoCapture(0)

    recog = cv2.face.LBPHFaceRecognizer_create()
    recog.read(a + "\\trainingData.yml")

    id = 0
    label = ""
    font = cv2.FONT_HERSHEY_SIMPLEX

    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetector.detectMultiScale(gray, 1.15, 3, minSize=(50, 50))
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            id, conf = recog.predict(gray[y : y + h, x : x + w])

            if id == 1:
                label = "Sumit"
            elif id == 2:
                label = "Rohit"
            elif id == 3:
                label = "Rakesh"
            elif id == 4:
                label = "Antima"
            else:
                label = "unknown"
            cv2.putText(img, label, (x, y + h), font, 2, (0, 255, 0), 3)
            defaultdict[label] = defaultdict[label] + 1
            # asyncio.run(notify(v, label+" is at the door"))

        currentSeen = datetime.now()
        if (currentSeen - lastSeen).seconds > 30:
            print("Intruder alert", defaultdict)
            lastSeen = currentSeen
            threading.Thread(target=notify, args=(a, defaultdict)).start()
            defaultdict = dict.fromkeys(defaultdict, 0)
            eel.sleep(10)

        cv2.imshow("Face", img)
        if cv2.waitKey(1) == ord("q"):
            break

    cam.release()
    cv2.destroyAllWindows()


# detector()
