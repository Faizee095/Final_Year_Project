# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 07:26:52 2019

@author: Susmit kumar
"""

from textSpeech import getVoice
import speech_recognition as sr
import webbrowser as wb
import requests
import json

def sender(number,msg):
            URL = 'http://www.way2sms.com/api/v1/sendCampaign'

            # get request
            def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
              req_params = {
              'apikey':apiKey,
              'secret':secretKey,
              'usetype':useType,
              'phone': phoneNo,
              'message':textMessage,
              'senderid':senderId
              }
              return requests.post(reqUrl, req_params)

            # get response
            response = sendPostRequest(URL, '7ZRA0OQ1COMUGOALBRKQTIFOMQSS3FNL', '7A3HVUBJLY4LNZJF', 'stage', number, 'x', msg )
            """
              Note:-
                you must provide apikey, secretkey, usetype, mobile, senderid and message values
                and then requst to api
            """
# print response if you want
            
mydict = {"why":"8810507596", "x":"8709442967"}
r1 = sr.Recognizer()

with sr.Microphone() as source:
    getVoice("Whom do you want to message ?")
    print("Who do you wanna msg ?")
    a = r1.listen(source)
    a2 = r1.recognize_google(a)
    print("You said ",a2)
    
    getVoice("What do you want to say ?")
    print("What do you want to say ?")
    a3 = r1.listen(source)
    msg = r1.recognize_google(a3)
    print("You said ",msg)
    
    sender(mydict[a2.lower()],msg)
    getVoice(" Message sent successfully ")
        
        