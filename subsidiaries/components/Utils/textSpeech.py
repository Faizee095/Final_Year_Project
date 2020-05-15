# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 03:23:24 2019

@author: Sumit Kumar Singh
"""

import pyttsx3

def getVoice(text):
    e = pyttsx3.init()
    e.setProperty('rate',125)
    voices = e.getProperty('voices')
    e.setProperty('voice',voices[1].id)
    e.say(text)
    e.runAndWait()
    return



getVoice("How Can I Help You")
