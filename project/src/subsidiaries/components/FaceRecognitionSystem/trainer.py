# trainer
import os
from typing import List
import cv2
import numpy as np
from PIL import Image
import logging
import sys

sys.setrecursionlimit(9000)
format = "%(asctime)s:%(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

recog = cv2.face.LBPHFaceRecognizer_create()
logging.info("recognizer is init()")
path = (
    "C:\\Users\\sumitsingh\\Documents\\Python\\face-recogModule\\module\\code\\dataSet"
)


def getImagesWithId(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    Ids: List[int] = []

    for ip in imagePaths:
        faceImage = Image.open(ip).convert("L")
        faceNp = np.array(faceImage, "uint8")
        Id = os.path.split(ip)[-1].split(".")[1]
        faces.append(faceNp)
        Ids.append(int(Id))
        # print(Ids)
        cv2.imshow("Training", faceNp)
        cv2.waitKey(10)
    return Ids, faces


Ids, faces = getImagesWithId(path)
logging.info("Loaded labeled faces.")
cv2.destroyAllWindows()

print(Ids)

x = recog.train(np.array(faces), np.array(Ids))

logging.info("Training Completed")
recog.save(
    "C:\\Users\\sumitsingh\\Documents\\Python\\face-recogModule\\module\\Lib\\site-packages\\cv2\\data\\trainingData.yml"
)
logging.info("Successfully saved as .yml")
