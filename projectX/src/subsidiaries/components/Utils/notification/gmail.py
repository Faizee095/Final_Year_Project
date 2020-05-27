# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 23:34:38 2019

@author: Sumit Kumar Singh
"""
import smtplib
import speech_recognition as sr
import webbrowser as wb
import json
from subsidiaries.components.Utils.speech.textSpeech import getVoice

r1 = sr.Recognizer()
r2 = sr.Recognizer()

with sr.Microphone() as source:
    print("[send mail]")
    audio = r1.listen(source)
    id1 = r1.recognize_google(audio)
    id1.lower()
    print("You said ", id1)

if "mail" in id1:
    with sr.Microphone() as source:
        getVoice("Whom do you want to mail ?")
        print("Whom do you want to mail ? ")
        audio = r2.listen(source)
        id1 = str(r2.recognize_google(audio))
        print("you said ", id1)
        l = []

        data = json.load(open("MyContacts.json"))
        for i in id1.split(" and "):
            l.append(data[i.lower()])
        # l = ["susmitkumar266@gmail.com"]
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        getVoice("Sending email")
        print("Sending . . .")
        for i in l:
            s.login("susmitkumar011@gmail.com", "")
            m = " Hi this is awesome "
            s.sendmail("susmitkumar266@gmail.com", i, m)
            getVoice("Sent to " + i)
            print("Sent to ", i)

        s.quit()
        getVoice("Done Task")
        print("Done task")
