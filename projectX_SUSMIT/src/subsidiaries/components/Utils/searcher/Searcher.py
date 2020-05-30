# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 00:59:08 2019

@author: Sumit Kumar Singh
"""
from src.subsidiaries.components.Utils.searcher.helpers.GoogleAnswer import getGoogleAnswer
from src.subsidiaries.components.Utils.searcher.helpers.youtubePlayer import playOnYoutube
from src.subsidiaries.components.Utils.speech.textSpeech import VoiceEngine
from src.subsidiaries.components.Utils.speech.speechText import SpeechRecogReg
import webbrowser as wb
from src.subsidiaries.components.Utils.speech import textSpeech, textSpeech

def googleSearcher():
        url = "https://www.google.com/search?q="
        print("search ")
        audio2345 = SpeechRecogReg()
        print("You searched ", audio2345)
        try:
            get = audio2345  # .replace(" ","+")
            print("Search String = ", get)
            # wb.get().open_new(get)
            answer = getGoogleAnswer(get)
            print("Answer is " + answer)
            VoiceEngine.getVoice(answer)
        except sr.UnknownValueError:
            print("error")
        except sr.RequestError as e:
            print("failed".format(e))


def youTubeSearcher():
    url = "https://www.youtube.com/results?search_query="
    with sr.Microphone() as source:
        print("search ")
        
        audio2345 = SpeechRecogReg()
        print("You searched ", audio2345)

        try:
            get = audio2345
            get.replace(" ", "+")
            print("Search String ", get)
            wb.get().open_new(playOnYoutube(get))
        except sr.UnknownValueError:
            print("error")
        except sr.RequestError as e:
            print("failed".format(e))

    