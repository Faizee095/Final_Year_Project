
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 22:12:12 2019

@author: Sumit Kumar Singh
"""

import webbrowser as wb
import speech_recognition as sr
from src.subsidiaries.components.Utils.speech.speechText import SpeechRecogReg
from src.subsidiaries.components.Utils.speech.textSpeech import VoiceEngine
import vlc
import os
os.add_dll_directory(r'C:\\Program Files\\VideoLAN\\VLC')


def callback(recog, audio):
    print(recog.recognize_google(audio))


def play():
    r1 = sr.Recognizer()
    m = sr.Microphone()

    with m as source1:
        r1.adjust_for_ambient_noise(source1)

    with sr.Microphone() as source:
        VoiceEngine.getVoice("Which song do you wanna play ?")
        print("Which song do you wanna play ?")
        audio = r1.listen(source)
        filename = r1.recognize_google(audio)

        print("You said ", filename)
        VoiceEngine.getVoice("Playing "+filename)

    # x = input("Enter song name ")
        s = vlc.MediaPlayer(
            "C:\\Users\\sumitsingh\\Documents\\Python\\hma"+filename+".mp3")
        s.play()
        print("press 1 to play, 2 to stop")

        r1 = sr.Recognizer()
        stopper = ""
        while(stopper != "stop"):
            print("Listening ")
            audio1 = r1.listen(source)
            stopper = r1.recognize_google(audio1)
    #        print("You said ",stopper)
        s.stop()


play()
