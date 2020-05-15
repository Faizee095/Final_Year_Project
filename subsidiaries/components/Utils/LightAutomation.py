# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 04:21:31 2019

@author: Sumit Kumar Singh
"""

from textSpeech import getVoice
import speech_recognition as sr
import webbrowser as wb

r1 = sr.Recognizer()
r2 = sr.Recognizer()

with sr.Microphone() as source:
    print('[Light Module]')
    audio = r1.listen(source)
    id1 = r1.recognize_google(audio)
    id1.lower()
    print("You said ",id1)
    
    if 'light' in id1:
        with sr.Microphone() as source:
            getVoice('On or Off ?')
            print('On or Off ?')
            audio = r1.listen(source)
            id1 = r1.recognize_google(audio)
            id1.lower()
            print("You said ",id1)
            
            if 'on' in id1:
                wb.get().open_new("http://192.168.0.113/1/0")
                getVoice("Light Turned On")
                print("It is now on")
            elif 'of' in id1:
                wb.get().open_new("http://192.168.0.113/1/1")
                getVoice("Light Turned Off")
                print("It is now off")
                
        