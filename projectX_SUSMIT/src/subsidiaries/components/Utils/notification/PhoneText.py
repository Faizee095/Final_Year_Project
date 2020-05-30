# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 07:26:52 2019

@author: Sumit Kumar Singh
"""

from src.subsidiaries.components.Utils.speech.textSpeech import VoiceEngine
from src.subsidiaries.components.Utils.speech.speechText import SpeechRecogReg
import speech_recognition as sr
import webbrowser as wb
import requests
import json
from pathlib import Path


def sender(number, msg):
    URL = "http://www.way2sms.com/api/v1/sendCampaign"

    # get request
    def sendPostRequest(
        reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage
    ):
        req_params = {
            "apikey": apiKey,
            "secret": secretKey,
            "usetype": useType,
            "phone": phoneNo,
            "message": textMessage,
            "senderid": senderId,
        }
        return requests.post(reqUrl, req_params)

    # get response
    response = sendPostRequest(
        URL,
        "7ZRA0OQ1COMUGOALBRKQTIFOMQSS3FNL",
        "7A3HVUBJLY4LNZJF",
        "stage",
        number,
        "x",
        msg,
    )
    """
              Note:-
                you must provide apikey, secretkey, usetype, mobile, senderid and message values
                and then requst to api
            """


def sendMessage():
    # print response if you want
    flag = False
    path = Path(__file__).parent / "MyContacts.json"
    with path.open() as f:
        data = json.load(f)["phones"]
    print("Phones -> ", data)

    VoiceEngine.getVoice("Whom do you want to message ?")
    print("Who do you wanna msg ?")
    a2 = SpeechRecogReg().lower()
    print("You said ", a2)

    while a2 not in data:
        VoiceEngine.getVoice("Could find any contact for ", a2)
        VoiceEngine.getVoice("Boss wanna terminate process or try again ?")
        answer = SpeechRecogReg()
        if "terminate" in answer:
            flag = True
            break

    if (flag == True):
        return

    VoiceEngine.getVoice("What do you want to say ?")
    print("What do you want to say ?")
    msg = SpeechRecogReg()
    print("You said ", msg)

    sender(data[a2], msg)
    VoiceEngine.getVoice(" Message sent successfully ")
