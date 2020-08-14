from src.subsidiaries.components.Utils.speech.textSpeech import VoiceEngine
from src.subsidiaries.components.Utils.Music.MyMusicDownloader import YouTubeDownloader
from src.subsidiaries.components.Utils.searcher.helpers.youtubePlayer import (
    playOnYoutube,
)
from src.subsidiaries.components.Utils.speech.speechText import SpeechRecogReg
from src.subsidiaries.components.Utils.weather.weather import getWeatherData
from src.subsidiaries.components.Utils.notification.gmail import mailer
from src.subsidiaries.components.Utils.notification.PhoneText import sendMessage
from src.subsidiaries.components.light_automation_system.LightAutomation import (
    lightSystemCall,
)
from src.subsidiaries.components.Utils.date.date import timedate
from src.subsidiaries.components.Utils.searcher.Searcher import (
    googleSearcher,
    youTubeSearcher,
)
from src.subsidiaries.components.Utils.news.news import newsFeed
import eel

# from src.subsidiaries.components.Utils.Music.Musically import play


class ActionDecider:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if ActionDecider.__instance == None:
            ActionDecider()
        return ActionDecider.__instance

    @staticmethod
    def decideTakeAction(textForm):
        print("You said", textForm)
        if "Google" in textForm:
            VoiceEngine.getVoice("I understand you want to Search Google")
            googleSearcher()
        elif "date" in textForm:
            VoiceEngine.getVoice("I understand you want to know date and time")
            VoiceEngine.getVoice("The date and time is")
            timedate()
        elif "YouTube" in textForm:
            VoiceEngine.getVoice("I understand you want to search youtube")
            youTubeSearcher()
        elif "download music" in textForm:
            VoiceEngine.getVoice(
                "I understand you want to download music. Let me process . . ."
            )
            VoiceEngine.getVoice("Which song you wanna download ?")
            search_string = SpeechRecogReg()
            print("Your search string is ", search_string)
            eel.show_info("Your search string is ", search_string)
            search_url = playOnYoutube(search_string)
            ydl = YouTubeDownloader(search_string)
            print("object created")
            ydl.download(search_url)
            VoiceEngine.getVoice("downloading file. . .please wait !")
            # del ydl

        elif "email" in textForm:
            VoiceEngine.getVoice("I understand you want to send an Email")
            mailer()
            # Calls Email
        elif "text" in textForm:
            VoiceEngine.getVoice("I understand you want to send text Messages")
            sendMessage()
            # Calls PhoneText
        elif "reset security system" in textForm:
            VoiceEngine.getVoice("I understand you want to reset the Security System")
            # Call Reset Security System
        elif "light" in textForm:
            VoiceEngine.getVoice("I understand you want to turn the lights off")
            lightSystemCall(textForm)
            # Call a simple web api
        elif "kill yourself" in textForm:
            VoiceEngine.getVoice("Alight I am gonna rest now! Bye Bye")
            return 1
        elif "play music" in textForm:
            VoiceEngine.getVoice("Which song maester?")
            # play()
        elif "weather" in textForm:
            VoiceEngine.getVoice("Yo Boss Gimme a second")
            getWeatherData()
        elif "news" in textForm:
            newsFeed()
        else:
            VoiceEngine.getVoice(
                "I am sorry I cannot do that ! But you can teach me how"
            )

        eel.stop_listening()
        return

    def __init__(self):
        """ Virtually private constructor. """
        if ActionDecider.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            ActionDecider.__instance = self
