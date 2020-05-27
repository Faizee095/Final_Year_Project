
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
#os.add_dll_directory(r'C:\\Program Files\\VideoLAN\\VLC')


def callback(recog, audio):
    print(recog.recognize_google(audio))


def play():
        VoiceEngine.getVoice("Which song do you wanna play ?")
        print("Which song do you wanna play ?")
        filename=SpeechRecogReg()

        print("You said ", filename)
        VoiceEngine.getVoice("Playing "+filename)

    # x = input("Enter song name ")
        s = vlc.MediaPlayer(
            "F:\\song\\"+filename+".mp3")
        s.play()
        #os.startfile("F:\\song\\"+filename+".mp3")
        print("press 1 to play, 2 to stop")

        stopper = SpeechRecogReg()
        while(stopper != "stop"):
            print("Listening ")
            stopper = SpeechRecogReg()
            print("You said ",stopper)
        
        s.stop()

