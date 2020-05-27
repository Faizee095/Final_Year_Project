from src.subsidiaries.components.Utils.speech.textSpeech import VoiceEngine
from src.subsidiaries.components.Utils.Music.MyMusicDownloader import YouTubeDownloader
from src.subsidiaries.components.Utils.searcher.helpers.youtubePlayer import playOnYoutube
from src.subsidiaries.components.Utils.speech.speechText import SpeechRecogReg


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
        if "search Google" in textForm:
            VoiceEngine.getVoice("I understand you want to Search Google")
            # Call Search Google
        elif "YouTube" in textForm:
            VoiceEngine.getVoice("I understand you want to search youtube")
            # Call Search Youtube
        elif "download music" in textForm:

            VoiceEngine.getVoice(
                "I understand you want to download music. Let me process . . .")
            VoiceEngine.getVoice("Which song you wanna download ?")
            search_string = SpeechRecogReg()
            print("Your search string is ", search_string)
            search_url = playOnYoutube(search_string)
            ydl = YouTubeDownloader()
            print("object created")
            ydl.download(search_url)
            VoiceEngine.getVoice("downloading file. . .please wait !")
            # del ydl

        elif "email" in textForm:
            VoiceEngine.getVoice("I understand you want to send an Email")
            # Call Email
        elif "text" in textForm:
            VoiceEngine.getVoice("I understand you want to send text Messages")
            # Call PhoneText
        elif "reset security system" in textForm:
            VoiceEngine.getVoice(
                "I understand you want to reset the Security System")
            # Call Reset Security System
        elif "turn lights on" in textForm:
            VoiceEngine.getVoice("I understand you want to turn the lights on")
            # Call a simple web api
        elif "turn lights off" in textForm:
            VoiceEngine.getVoice(
                "I understand you want to turn the lights off")
            # Call a simple web api
        elif "kill yourself" in textForm:
            VoiceEngine.getVoice("Alight I am gonna rest now!")
            return 1
        elif "play music" in textForm:
            VoiceEngine.getVoice("Which song maester?")

        else:
            VoiceEngine.getVoice(
                "I am sorry I cannot do that ! But you can teach me how")
        return

    def __init__(self):
        """ Virtually private constructor. """
        if ActionDecider.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            ActionDecider.__instance = self
