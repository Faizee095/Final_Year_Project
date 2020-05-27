# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 03:23:24 2019
@author: Sumit Kumar Singh
"""
import pyttsx3


class VoiceEngine:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if VoiceEngine.__instance == None:
            VoiceEngine()
        return VoiceEngine.__instance

    @staticmethod
    def getVoice(text):
        VoiceEngine.__instance.say(text)
        VoiceEngine.__instance.runAndWait()
        return

    def __init__(self):
        """ Virtually private constructor. """
        if VoiceEngine.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            VoiceEngine.__instance = pyttsx3.init()
            VoiceEngine.__instance.setProperty("rate", 125)
            voices = VoiceEngine.__instance.getProperty("voices")
            VoiceEngine.__instance.setProperty("voice", voices[1].id)


""" def getVoice(text):
    e = pyttsx3.init()
    e.setProperty("rate", 125)
    voices = e.getProperty("voices")
    e.setProperty("voice", voices[1].id)
    e.say(text)
    e.runAndWait()
    return """
