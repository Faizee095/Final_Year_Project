# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 23:34:38 2019

@author: Sumit Kumar Singh
"""
import smtplib
import sys
import speech_recognition as sr
import webbrowser as wb
import json
from src.subsidiaries.components.Utils.speech.textSpeech import VoiceEngine
from src.subsidiaries.components.Utils.speech.speechText import SpeechRecogReg
from pathlib import Path
import eel


def mailer():
    path = sys._MEIPASS + "\\user-settings.json"
    print("path->", path)

    user_emailId = "7jhonwick0777@gmail.com"
    user_password = "dontkillmydog"

    with open(path) as f:
        data = json.load(f)
        user_emailId = data["emailId"]
        user_password = data["password"]

    print(user_emailId, user_password)

    print("[send mail]")
    id1 = SpeechRecogReg().lower()
    print("You said ", id1)

    if "mail" in id1:
        VoiceEngine.getVoice("Whom do you want to mail ?")
        print("Whom do you want to mail ? ")
        id1 = SpeechRecogReg()
        print("you said ", id1)
        l = []

        with open(sys._MEIPASS + "\\MyContacts.json", "r") as f:
            data = json.load(f)["emails"]

        for i in id1.split(" and "):
            if data[i.lower()] != None:
                l.append(data[i.lower()])
            else:
                VoiceEngine.getVoice("Could not find email for ", i)

        VoiceEngine.getVoice("What's the message boss ?")
        message = SpeechRecogReg()

        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        VoiceEngine.getVoice("Sending email, give me some time")
        eel.show_info("Sending . . .")
        print("Sending . . .")
        try:
            for recipientEmailId in l:
                s.login(user_emailId, user_password)
                s.sendmail(user_emailId, recipientEmailId, message)
                VoiceEngine.getVoice("Sent to " + recipientEmailId)
                print("Sent to ", recipientEmailId)
        except:
            print("exception occurred")
            VoiceEngine.getVoice(
                "Boss, I am facing some issues. Why don't we try again later?"
            )

        s.quit()
        VoiceEngine.getVoice("Done Task")
        print("Done task")
