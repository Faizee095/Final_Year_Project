
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
from pathlib import Path
import json


def play():
        path = Path(__file__).parent / \
        "../../settings/user-settings.json"

        with path.open() as f:
            data = json.load(f)["music-library-path"]

        VoiceEngine.getVoice("Which song do you wanna play ?")
        print("Which song do you wanna play ?")
        filename=SpeechRecogReg()

        print("You said ", filename)
        VoiceEngine.getVoice("Playing "+filename)

    # x = input("Enter song name ")
        s = vlc.MediaPlayer(
            data+filename+".mp3")
        s.play()
        s.audio_set_volume(35)
        stopper = SpeechRecogReg()
        while(stopper != "stop"):
            print("Listening ")
            stopper = SpeechRecogReg()

            if ( "volume up" in stopper):
                s.audio_set_volume(50)
            if ("pause" in stopper):
                s.audio_set_mute(True)
            if ("continue" in stopper):
                s.audio_set_mute(False)
            if ("volume down" in stopper):
                s.audio_set_volume(35)
            print("You said ",stopper)
        
        s.stop()

        return "session ended"
