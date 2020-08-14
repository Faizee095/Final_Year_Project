# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 00:59:08 2019

@author: Sumit Kumar Singh
"""
from src.subsidiaries.components.Utils.searcher.helpers.GoogleAnswer import (
    getGoogleAnswer,
)
from src.subsidiaries.components.Utils.searcher.helpers.youtubePlayer import (
    playOnYoutube,
)
from src.subsidiaries.components.Utils.speech.textSpeech import VoiceEngine
from src.subsidiaries.components.Utils.speech.speechText import SpeechRecogReg
import webbrowser as wb
from src.subsidiaries.components.Utils.speech import textSpeech, textSpeech
import eel


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
        eel.show_info(answer)
        VoiceEngine.getVoice(answer)
    except Exception as e:
        print("failed".format(e))


def youTubeSearcher():
    url = "https://www.youtube.com/results?search_query="
    print("what to search on youtube ?")

    audio2345 = SpeechRecogReg()
    print("You searched ", audio2345)

    try:
        get = audio2345
        get.replace(" ", "+")
        print("Search String ", get)
        wb.get().open_new(playOnYoutube(get))
    except Exception as e:
        print("failed".format(e))
