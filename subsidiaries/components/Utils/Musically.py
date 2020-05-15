# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 22:12:12 2019

@author: Susmit kumar
"""

import os

from textSpeech import getVoice

import speech_recognition as sr
import webbrowser as wb

def callback(recog,audio):
    print(recog.recognize_google(audio))
r1 = sr.Recognizer()
m = sr.Microphone()

with m as source1:
    r1.adjust_for_ambient_noise(source1)
    
with sr.Microphone() as source:
    getVoice("Which song do you wanna play ?")
    print("Which song do you wanna play ?")
    audio = r1.listen(source)
    filename = r1.recognize_google(audio)
    
    print("You said ",filename)
    getVoice("Playing "+filename)
    
   # x = input("Enter song name ")
    os.startfile("F:\\song\\"+filename+".mp3")





