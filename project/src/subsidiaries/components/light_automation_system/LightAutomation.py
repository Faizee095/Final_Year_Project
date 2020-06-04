# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 04:21:31 2019

@author: Sumit Kumar Singh
"""

from src.subsidiaries.components.Utils.speech.textSpeech import VoiceEngine
from src.subsidiaries.components.Utils.speech.speechText import SpeechRecogReg
#import webbrowser as wb
import requests as req
import speech_recognition as sr
from pathlib import Path
import json


def lightSystemCall(textForm):
    number = textForm[textForm.index("number")+7: textForm.index("number")+8]
    status = textForm[textForm.index("number")+9:]

    path = Path(__file__).parent / "appliances.json"
    with path.open() as f:
        data = json.load(f)

    print("In the [Light Module]")

    while(data["light "+number] is None):
        key = data["light "+number]
        print(key)
        VoiceEngine.getVoice(
            "I am sorry, could you please say that again or you wanna exit?")
        textForm = SpeechRecogReg()

        if "exit" in textForm:
            return
        number = textForm[textForm.index(
            "number")+7: textForm.index("number")+8]
        status = textForm[textForm.index("number")+9:]
    try:
        if "on" in status:
            url = data["light "+number] + number + "/0"
            # wb.get().open_new(url)
            response = req.get(url)
            VoiceEngine.getVoice("Light Turned On")
            print("It is now on : ", url)
        elif "of" or "off" in status:
            url = data["light "+number] + number + "/1"
            #wb.get().open_new(data["light " + number] + number + "/1")
            resonse = req.get(url)
            VoiceEngine.getVoice("Light Turned Off")
            print("It is now off:", url)
    except:
        VoiceEngine.getVoice(
            "Uh! I am facing some network problem. Why don't Try again later?")
    return
