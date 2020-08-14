# Face recognition
# create dataset-> creator
# trainer
# detector

import cv2
import numpy as np

# from module.code.db_operations import insertOrUpdate, view, getLastRowId
import sqlite3


class Collector:
    def __init__(self):
        """" To make it dynamic Modify as -> __init__(self, name, age, gender) """
        faceDetector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        cam = cv2.VideoCapture(0)

        id = int(input("Enter user Id "))

        sample_number = 0
        while True:
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = faceDetector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                sample_number = sample_number + 1
                cv2.imwrite(
                    "dataSet/user." + str(id) + "." + str(sample_number) + ".jpg",
                    gray[y : y + h, x : x + w],
                )
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.waitKey(100)

            cv2.imshow("Face", img)
            if sample_number > 20:
                break

        cam.release()
        cv2.destroyAllWindows()


# ----------------------------------------tmp code here---------------------------------------------------
def createConnection():
    con = sqlite3.connect(
        "C:\\Users\\sumitsingh\\Documents\\Python\\face-recogModule\\module\\code\\db\\database.db"
    )
    return con


def destroyConnection(con):
    con.commit()
    con.close()


def insertOrUpdate(id, name, age, gender):
    # BELOW CODE IS FOR DYNAMIC INSERTION
    con = createConnection()
    user = (name, age, gender)
    insertQuery = "INSERT INTO users(name, age, gender) VALUES (?,?,?)"
    cursor = con.execute(insertQuery, user)
    destroyConnection(con)
    return cursor.rowcount


def view():
    res = any
    con = createConnection()
    cmd = "select * from users"
    cursor = con.execute(cmd)
    res = cursor.fetchall()
    destroyConnection(con)
    return res


def getLastRowId():
    con = createConnection()
    cmd = "select id from users ORDER BY id DESC LIMIT 1;"
    cursor = con.execute(cmd)
    data = cursor.fetchone()
    destroyConnection(con)
    return data


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    """ s = input("Enter user name, age and gender\n").split(" ")

    id = insertOrUpdate(1, s[0], s[1], s[2])
    print(id) """
    # view()

    # print(getLastRowId()[0])
    # collector_object = Collector(getLastRowId()[0])

o = Collector()
