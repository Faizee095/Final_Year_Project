import youtube_dl
import pandas as pd
import os
from src.subsidiaries.components.Utils.speech.textSpeech import VoiceEngine
import logging
import sys
import json
import eel

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class YouTubeDownloader:
    def __init__(self, filename):
        path = sys._MEIPASS + "\\user-settings.json"
        with open(path, "r") as f:
            data = json.load(f)["music-library-path"]
        self.SAVE_PATH = data
        self.options = {
            "format": "bestaudio/best",  # choice of quality
            "extractaudio": True,  # only keep the audio
            "audioformat": "mp3",  # convert to mp3
            # name the file the ID of the video
            "outtmpl": self.SAVE_PATH + "//" + filename + ".mp3",
            "noplaylist": True,
        }  # only download single song, not playlist
        self.ydl = youtube_dl.YoutubeDL(self.options)

    def download(self, url):
        try:
            with self.ydl:
                # self.__ydl__.cache.remove()
                info_dict = self.ydl.extract_info(url, download=False)
                self.ydl.prepare_filename(info_dict)
                VoiceEngine.getVoice("Downloading file. Please wait!")
                self.ydl.download([url])
                eel.show_info("Music file has been downloaded")
                VoiceEngine.getVoice("Your music has been downloaded . . .")
                return True
        except Exception as error:
            logger.info("Exception has ocurred")
            logger.exception(error)
            return False

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")
