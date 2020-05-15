# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 00:59:08 2019

@author: Susmit kumar prasad
"""
from GoogleAnswer import getGoogleAnswer
from youtubePlayer import playOnYoutube
from textSpeech import getVoice
import speech_recognition as sr
import webbrowser as wb
r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    print('[search google: search youtube]')
    print('speak')
    audio = r3.listen(source)
    audio1234 = r2.recognize_google(audio)
    print("You said ",audio1234)

if 'Google' in audio1234:
    
    r2 = sr.Recognizer()
    url = 'https://www.google.com/search?q='
    with sr.Microphone() as source:
        print('search ')
        audio = r2.listen(source)
        audio2345 =r2.recognize_google(audio)
        print("You searched ",audio2345)
        try:
            get = audio2345 #.replace(" ","+")
            print("Search String = ",get)
            #wb.get().open_new(get)
            answer = getGoogleAnswer(get)
            print("Answer is "+answer)
            getVoice(answer)
        except sr.UnknownValueError:
            print('error')
        except sr.RequestError as e:
            print('failed'.format(e))

if 'YouTube' in audio1234:
    r1 = sr.Recognizer()
    url = 'https://www.youtube.com/results?search_query='
    with sr.Microphone() as source:
        print('search ')
        audio = r1.listen(source)
        audio2345 =r1.recognize_google(audio)
        print("You searched ",audio2345)

        try:
            get = audio2345
            get.replace(" ","+")
            print("Search String ",get)
            wb.get().open_new(playOnYoutube(get))
        except sr.UnknownValueError:
            print('error')
        except sr.RequestError as e:
            print('failed'.format(e))