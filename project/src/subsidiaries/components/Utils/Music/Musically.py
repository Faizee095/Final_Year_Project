# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 22:12:12 2019

@author: 
"""

import webbrowser as wb
import speech_recognition as sr
from src.subsidiaries.components.Utils.speech.speechText import SpeechRecogReg
from src.subsidiaries.components.Utils.speech.textSpeech import VoiceEngine
import vlc
import os
import sys
from pathlib import Path
import json
import eel


def play():
    bundle_dir = sys._MEIPASS
    path = bundle_dir + "\\user-settings.json"

    with open(path, "r") as f:
        data = json.load(f)["music-library-path"]

    eel.show_info("Which song do you wanna play ?")
    VoiceEngine.getVoice("Which song do you wanna play ?")

    filename = SpeechRecogReg()

    eel.show_info("You said ", filename)
    VoiceEngine.getVoice("Playing " + filename)

    # x = input("Enter song name ")
    s = vlc.MediaPlayer(data + filename + ".mp3")
    s.play()
    s.audio_set_volume(35)
    stopper = SpeechRecogReg()
    while "terminate" not in stopper:
        print("Listening ")
        eel.show_info("Listening")
        stopper = SpeechRecogReg()

        if "volume up" in stopper:
            s.audio_set_volume(50)
        if "pause" in stopper:
            s.audio_set_mute(True)
        if "continue" in stopper:
            s.audio_set_mute(False)
        if "volume down" in stopper:
            s.audio_set_volume(35)
        print("You said ", stopper)

    s.stop()

    return "session ended"
